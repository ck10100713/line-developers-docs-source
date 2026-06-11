# 管理使用者（Managing users）

本主題說明如何執行以下使用者管理工作：

- [Getting user profiles](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/#get-profile)
- [Using ID tokens to verify user identities](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/#get-id-token)
- [Logging out users](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/#logout)

<!-- tip start -->

**建立安全的登入流程**

關於如何安全地處理使用者註冊與登入的一般建議，請參閱[Creating a secure login process between your app and server](https://developers.line.biz/en/docs/line-login/secure-login-process/)。

<!-- tip end -->

## Getting user profiles 

如果登入要求是以 `.profile` scope 送出，你就可以取得使用者的 LINE 個人檔案資訊。使用者個人檔案包含使用者 ID、顯示名稱、個人檔案媒體（圖片或影片）以及狀態消息。

如下方式呼叫 `API.getProfile` 方法：

```swift
API.getProfile { result in
    switch result {
    case .success(let profile):
        print("User ID: \(profile.userID)")
        print("User Display Name: \(profile.displayName)")
        print("User Status Message: \(profile.statusMessage)")
        print("User Icon: \(String(describing: profile.pictureURL))")
    case .failure(let error):
        print(error)
    }
}
```

`API.getProfile` 方法取得的是登入當下的值，而使用者隨時都能在 LINE 中變更自己的顯示名稱、個人檔案媒體與狀態消息。若要識別使用者，請使用不會改變的 `userID` 屬性的值。

## Using ID tokens to verify user identities 

[OpenID Connect](https://openid.net/developers/how-connect-works/) 1.0 規格是建構於 OAuth 2.0 協定之上的身分層（identity layer）。透過 OpenID Connect，你可以安全地與 LINE Platform 交換資訊。目前，你可以藉由發行符合 OpenID Connect 規格的 ID token，從 LINE Platform 取得使用者的個人檔案與電子郵件地址。

### Applying for email permission 

你可以要求使用 LINE Login 登入的使用者，授予你的應用程式取得其電子郵件地址的權限。若要這麼做，請在 [LINE Developers Console](https://developers.line.biz/console/) 中申請該權限。詳情請參閱 LINE Login 指南中的[Applying for email permission](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)。

### Login with the OpenID and email scopes 

一旦你的頻道（channel）取得電子郵件權限後，你就可以讓使用者以 `.openID` 與 `.email` scope 登入，並如下方式從 ID token 取得使用者的電子郵件地址：

```swift
LoginManager.shared.login(permissions: [.openID, .email], in: self) {
    result in
    switch result {
    case .success(let loginResult):
        if let email = loginResult.accessToken.IDToken?.payload.email {
            print("User Email: \(email)")
        }
    case .failure(let error):
        print(error)
    }
}
```

ID token 是一個經過簽署的 [JSON Web Token](https://datatracker.ietf.org/doc/html/rfc7519)。LINE SDK 會替你檢查其簽章與有效期間（validity period）來驗證 token，以防範其中含有任何格式錯誤的資料。

### Using ID tokens on your server 

<!-- warning start -->

**使用者冒充（User impersonation）**

請勿信任用戶端送往你後端伺服器的使用者 ID 或其他資訊。惡意的用戶端可能會送出任意的使用者 ID 或格式錯誤的資訊到你的伺服器，藉以冒充某位使用者。

正確的做法是，用戶端應將原始的 ID token 字串送至你的伺服器。在透過 ID token 驗證 API 驗證該 token 之後，伺服器即可取得使用者 ID 或任何其他資訊。

<!-- warning end -->

#### Sending raw ID token string 

當以 `.openID` 權限登入時，你可以為 `IDTokenNonce` 參數指定一個自訂的值：

```swift
var parameters = LoginManager.Parameters()
parameters.IDTokenNonce = "<a randomly-generated string>"
LoginManager.shared.login(permissions: [.profile, .openID], parameters: parameters) {
    result in
    // ...
}
```

雖然在未指定值的情況下 LINE SDK 會自動為 `IDTokenNonce` 指定一個值，但我們建議在你的伺服器上隨機產生一個 nonce 值，並將其儲存在那裡。你之後可以使用原始的 nonce，透過 LINE Login 來[verify the ID token](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/#verify-id-token-on-server)。使用 `nonce` 驗證 ID token 有助於防範[replay attacks](https://en.wikipedia.org/wiki/Replay_attack)（重送攻擊）。

以 `.openID` 權限成功登入之後，你可以像這樣取得原始的 ID token 字串：

```swift
LoginManager.shared.login(permissions: [.profile, .openID], parameters: parameters) {
    result in
    switch result {
    case .success(let loginResult):
        if let idToken = loginResult.accessToken.IDTokenRaw {
            // Send `idToken` to your server.
        } else {
            // Something went wrong. You should fail the login.
        }

    case .failure(let error):
        print(error)
```

接著你可以將 `idToken` 送至你的伺服器以進行[verified](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/#verify-id-token-on-server)。

#### Verify ID token on your server 

在收到 ID token 之後，你的伺服器應將該 token 與對應的 `nonce` 值一併送至 LINE Platform 的 ID token 驗證端點（endpoint）。如果該 token 有效，此 API 會回傳一個包含 ID token claims 的 JSON 格式物件。

關於應從你的後端呼叫哪些 API，請於下列頁面了解更多：

- [Verify the ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token)

### Treating user data carefully 

請勿在你的應用程式或伺服器中以純文字（plain text）儲存任何敏感的使用者資料，或透過非安全的 HTTP 通訊傳輸這些資料。此類資料包括存取權杖（access token）、使用者 ID、使用者名稱，以及 ID token 中的任何資訊。LINE SDK 會替你儲存使用者的存取權杖。如有需要，你可以在授權之後使用以下程式碼存取它：

```swift
if let token = AccessTokenStore.shared.current {
    print(token.value)
}
```

ID token 僅在登入當下發行。若要更新 ID token，你必須讓使用者重新登入。不過，如果你在登入要求中設定了 `.profile` scope，便可以呼叫 `API.getProfile` 方法來取得使用者的個人檔案資訊。

## Logging out users 

你可以將使用者從你的應用程式登出。為了打造更好的使用者體驗，我們建議提供讓使用者從你的應用程式登出的方式。

若要使存取權杖失效並將使用者從你的應用程式登出，請呼叫 `logout` 方法。當你使存取權杖失效時，使用者就會從你的應用程式登出。登出之後，使用者必須再次經歷登入流程才能登入。

```swift
LoginManager.shared.logout { result in
    switch result {
    case .success:
        print("Logout from LINE")
    case .failure(let error):
        print(error)
    }
}
```
