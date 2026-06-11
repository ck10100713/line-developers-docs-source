# 管理存取權杖（Managing access tokens）

本主題說明如何執行下列存取權杖（access token）管理作業：

- [Refreshing access tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/#refresh-token)
- [Getting the current access token](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/#get-current-token)
- [Verifying access tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/#verify-access-token)

<!-- tip start -->

**建立安全的登入流程**

關於如何安全處理使用者註冊與登入的一般建議，請參閱[在你的 App 與伺服器之間建立安全的登入流程](https://developers.line.biz/en/docs/line-login/secure-login-process/)。

<!-- tip end -->

## Refreshing access tokens 

LINE SDK 在授權成功後會儲存使用者有效的存取權杖，並用它來發出 API 請求。你可以如下取得存取權杖的有效期間（validity period）：

```java
LineAccessToken accessToken = lineApiClient.getCurrentAccessToken().getResponseData();
Log.i(TAG, accessToken.getExpiresInMillis());
```

當發出 API 請求時，LINE SDK 會透過 `LineApiClient` 介面自動更新任何已過期的存取權杖。不過，若權杖已過期很長一段時間，更新作業就會失敗。此時會發生錯誤，你需要請使用者重新登入。

**不建議**自行更新存取權杖。由 LINE SDK 自動管理存取權杖較為簡便，且對日後升級也更安全。不過，你還是可以如下手動更新存取權杖：

```java
LineAccessToken newAccessToken = lineApiClient.refreshAccessToken().getResponseData();
```

## Getting the current access token 

當建構主從式（client-server）應用程式時，可使用存取權杖在你的 App 與伺服器之間傳送使用者資料。如果你在 App 中取得存取權杖並將其傳送至伺服器，就能從該伺服器發出 LINE Login API 呼叫。若要進一步了解，請參閱 [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

若要取得 LINE SDK 儲存在你 App 中的存取權杖，請呼叫 `getCurrentAccessToken()` 方法。

```java
String accessToken = lineApiClient.getCurrentAccessToken().getResponseData().getTokenString();
```

<!-- note start -->

**注意**

建議你在透過 SSL 連線將存取權杖傳送至伺服器之前，先將其加密。

在伺服器上使用存取權杖之前，請先確認下列條件皆成立：

- 伺服器所收到的存取權杖，與用來發出 LINE Login API 呼叫的存取權杖相同。
- 用來發出 LINE Login API 呼叫的頻道 ID（channel ID）與你自己的頻道 ID 相符。

<!-- note end -->

## Verifying access tokens 

在你的 App 中呼叫 `verifyToken()` 方法，以驗證 LINE SDK 所儲存的存取權杖是否有效。此方法會回傳一個包含結果的 `LineApiResponse` 物件。接著你可以呼叫 `isSuccess()` 方法來檢查權杖是否有效。

若 `isSuccess()` 方法回傳 `true`，表示權杖有效。否則，表示該存取權杖無效或已過期，或是 LINE SDK 中的 LINE Login API 呼叫因某些原因失敗。

若 `isSuccess()` 方法回傳 `false`，你可以使用 `LineApiResponse.getErrorData()` 方法來判斷 `verifyToken()` 方法失敗的原因。在此情況下，`getResponseData()` 方法會回傳 `null`。

```java
LineApiResponse verifyResponse = lineApiClient.verifyToken();

if (verifyResponse.isSuccess()) {

    Log.i(TAG, "getResponseData: " + verifyResponse.getResponseData().toString());
    Log.i(TAG, "getResponseCode: " + verifyResponse.getResponseCode().toString());

    return true;
} else {

    Log.i(TAG, "getResponseCode: " + verifyResponse.getResponseCode());
    Log.i(TAG, "getErrorData: " + verifyResponse.getErrorData());

    return false;

}
```

若要取得與存取權杖關聯的權限範圍（scope）清單，請呼叫 `LineApiResponse.getResponseData().getScopes()`。下列範例示範如何在 toast 中顯示權限範圍清單。

```java
protected void onPostExecute(LineApiResponse response){
    if (response.isSuccess()){
        LineCredential lineCredential = response.getResponseData();
        List<Scope> scopes = lineCredential.getScopes();
        String scopesString = Scope.join(scopes);
        Toast.makeText(getApplicationContext(), scopesString, Toast.LENGTH_SHORT).show();
    }
}
```
