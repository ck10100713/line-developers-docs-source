# 管理使用者（Managing users）

本主題說明如何執行以下使用者管理工作：

- [Getting user profiles](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#get-profile)
- [Using ID tokens to verify user identities](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#get-id-token)
- [Logging out users](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#logout)

<!-- tip start -->

**建立安全的登入流程**

關於如何安全處理使用者註冊與登入的一般建議，請參閱 [Creating a secure login process between your app and server](https://developers.line.biz/en/docs/line-login/secure-login-process/)。

<!-- tip end -->

## Getting user profiles 

如果登入請求帶有 `Scope.PROFILE` scope，你便能取得使用者的 LINE 個人檔案資訊。使用者個人檔案包含使用者 ID、顯示名稱、個人檔案媒體（圖片或影片）以及狀態消息。

如下方所示呼叫 `LineApiClient.getProfile()` 方法：

```java
LineProfile profile = lineApiClient.getProfile().getResponseData()
Log.i(TAG, profile.getDisplayName());
Log.i(TAG, profile.getUserId());
Log.i(TAG, profile.getStatusMessage());
Log.i(TAG, profile.getPictureUrl().toString());
```

`getDisplayName()`、`getPictureURL()` 與 `getStatusMessage()` 方法取得的是登入當下的值，而使用者隨時可以在 LINE 中變更這些值。若要識別使用者，請使用 `getUserId()` 方法，其回傳值（使用者 ID）不會改變。

你可以在 URL 後加上後綴來變更使用者個人檔案圖片的尺寸。

Image Size | Suffix
-|-
200 x 200 | /large
51 x 51 | /small

## Using ID tokens to verify user identity 

[OpenID Connect](https://openid.net/developers/how-connect-works/) 1.0 規格是建構於 OAuth 2.0 協定之上的身分識別層。透過 OpenID Connect，你可以安全地與 LINE Platform 交換資訊。目前，你可以藉由發行符合 OpenID Connect 規格的 ID 權杖（ID token），從 LINE Platform 取得使用者個人檔案與電子郵件地址。

### Applying for email permission 

你可以請求使用 LINE Login 登入的使用者，授權你的應用程式取得他們的電子郵件地址。若要這麼做，請於 [LINE Developers Console](https://developers.line.biz/console/) 申請該權限。詳情請參閱 LINE Login 指南中的 [Applying for email permission](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)。

### Login with the OpenID and email scopes 

當你的頻道（channel）取得電子郵件權限後，你便能讓使用者使用 `Scope.OPENID_CONNECT` 與 `Scope.OC_EMAIL` scope 登入，並如下方所示從 ID 權杖取得使用者的電子郵件地址：

```java
import java.util.Arrays;

private static final int REQUEST_CODE = 1;

LineAuthenticationParams params = new LineAuthenticationParams.Builder()
                                    .scopes(Arrays.asList(Scope.OPENID_CONNECT, Scope.OC_EMAIL))
                                    .build();

Intent loginIntent = LineLoginApi.getLoginIntent(
                        view.getContext(),
                        Constants.CHANNEL_ID,
                        params);

startActivityForResult(loginIntent, REQUEST_CODE);
```

ID 權杖是一個經過簽章的 [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519)。LINE SDK 會為你檢查權杖的簽章與有效期間（validity period）以驗證該權杖，以防止其中含有任何格式錯誤的資料。若驗證通過，你可以在 `onActivityResult()` 回呼中取得 `LineIdToken` 實例，如下方所示：

```java
public void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode != REQUEST_CODE) {
        Log.e("ERROR", "Unsupported Request");
        return;
    }

    LineLoginResult result = LineLoginApi.getLoginResultFromIntent(data);

    switch (result.getResponseCode()) {
        case SUCCESS:
            // Login successful
            LineIdToken lineIdToken = result.getLineIdToken();
            Log.v("INFO", lineIdToken.getEmail());
    ...
    }
}
```

### Using ID tokens on your server 

<!-- warning start -->

**使用者偽冒（User spoofing）**

請勿信任由用戶端傳送至你後端伺服器的使用者 ID 或其他資訊。惡意的用戶端可能會傳送任意的使用者 ID 或格式錯誤的資訊到你的伺服器，藉此冒充某位使用者。

正確的做法是，用戶端應將原始的 ID 權杖字串傳送至你的伺服器。在透過 ID 權杖驗證 API 驗證該權杖後，伺服器便能擷取使用者 ID 或任何其他資訊。

<!-- warning end -->

#### Sending raw ID token string 

使用 `Scope.OPENID_CONNECT` scope 登入時，你可以為 `nonce` 參數指定自訂的值：

```java
private static final int REQUEST_CODE = 1;
...
LineAuthenticationParams params = new LineAuthenticationParams.Builder()
                                  ...
                                  .nonce("<a randomly-generated string>")
                                  .build();

Intent loginIntent = LineLoginApi.getLoginIntent(
                        view.getContext(),
                        Constants.CHANNEL_ID,
                        params);

startActivityForResult(loginIntent, REQUEST_CODE);
```

即使你未自行指定 `nonce` 的值，LINE SDK 也會自動為其指定一個值，但我們仍建議為 `nonce` 產生一個隨機值並指定給 `nonce` 參數。在透過 LINE Login API [verifying ID tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#verify-id-token-on-server) 時，你可以使用此處為 `nonce` 所指定的值。使用 `nonce` 驗證 ID 權杖有助於防止[重放攻擊（replay attacks）](https://en.wikipedia.org/wiki/Replay_attack)。

以 `Scope.OPENID_CONNECT` scope 成功登入後，你可以像這樣取得原始的 ID 權杖字串：

```java
public void onActivityResult(int requestCode, int resultCode, Intent data) {
    ...
    LineLoginResult result = LineLoginApi.getLoginResultFromIntent(data);

    switch (result.getResponseCode()) {
        case SUCCESS:
            // Login successful
            LineIdToken lineIdToken = result.getLineIdToken();
            String idTokenStr = lineIdToken.getRawString();
            if (idTokenStr != null) {
                // Send `idTokenStr` to your server.
            } else {
                // Something went wrong. You should fail the login.
            }
    ...
}
```

將此處取得的 `idTokenStr` 傳送至你的後端伺服器以[verify ID tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#verify-id-token-on-server)。

#### Verify ID tokens on your backend server 

收到 ID 權杖後，你的伺服器應將該權杖與對應的 `nonce` 值一同傳送至 LINE Platform 的 ID 權杖驗證端點（endpoint）。若權杖有效，該 API 會回傳一個包含 ID 權杖聲明（claims）的 JSON 格式物件。

若要進一步了解該從你的後端伺服器呼叫哪些 API，請參閱：

- [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token)（LINE Login v2.1 API reference）

### Handling user data responsibly 

請勿在你的應用程式或伺服器中以明文儲存任何敏感的使用者資料，也不要透過非安全的 HTTP 通訊傳輸這些資料。此類資料包括存取權杖、使用者 ID、使用者名稱，以及 ID 權杖中的任何資訊。LINE SDK 會為你儲存使用者的存取權杖。如有需要，你可以在授權後使用下方程式碼存取它：

```java
LineAccessToken accessToken = lineApiClient.getCurrentAccessToken().getResponseData();
```

ID 權杖僅在登入時發行。若要更新 ID 權杖，你必須讓使用者再次登入。不過，如果你在登入請求中設定了 `Scope.PROFILE` scope，便可以呼叫 `LineApiClient.getProfile()` 方法來取得使用者的個人檔案資訊。

## Logging out users 

你可以讓使用者從你的應用程式登出。為了打造更好的使用者體驗，我們建議提供讓使用者從你應用程式登出的方式。

若要使存取權杖失效並讓使用者從你的應用程式登出，請呼叫 `logout()` 方法。當你使存取權杖失效時，使用者便會從你的應用程式登出。登出後，使用者必須再次經過登入流程才能登入。

```java
lineApiClient.logout();
```
