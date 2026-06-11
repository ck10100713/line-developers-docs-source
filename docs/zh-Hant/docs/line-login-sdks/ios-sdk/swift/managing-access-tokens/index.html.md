# 管理存取權杖（Managing access tokens）

本主題說明如何執行以下存取權杖（access token）管理作業：

- [Refreshing access tokens](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-access-tokens/#refresh-token)
- [Getting the current access token](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-access-tokens/#get-current-token)
- [Verifying access tokens](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-access-tokens/#verify-access-token)

<!-- tip start -->

**建立安全的登入流程**

關於如何安全處理使用者註冊與登入的一般建議，請參閱[Creating a secure login process between your app and server](https://developers.line.biz/en/docs/line-login/secure-login-process/)。

<!-- tip end -->

## Refreshing access tokens 

LINE SDK 會在授權成功後儲存使用者的有效存取權杖，並用它來發出 API 請求。你可以如下取得存取權杖的到期日：

```swift
if let token = AccessTokenStore.shared.current {
    print("Token expires at:\(token.expiresAt)")
}
```

透過 `API` 型別發出 API 請求時，LINE SDK 會自動重新整理任何已過期的存取權杖。不過，若權杖已過期很長一段時間，重新整理作業就會失敗。此時會發生錯誤，你需要讓使用者重新登入。請參閱[Handling errors](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/error-handling/)以了解更多資訊。

<!-- note start -->

**存取權杖自動重新整理**

只有 `API` 型別的方法會自動重新整理存取權杖。其他型別（例如 `API.Auth`）的方法不會觸發存取權杖的自動重新整理。

<!-- note end -->

我們建議你**不要**自行重新整理存取權杖。讓 LINE SDK 自動管理存取權杖較為簡單，也較能因應未來變化。不過，若有必要，你可以像這樣手動重新整理存取權杖：

```swift
API.Auth.refreshAccessToken { result in
    switch result {
    case .success(let token):
        print("Token Refreshed: \(token)")
    case .failure(let error):
        print(error)
    }
}
```

## Getting the current access token 

在建置主從式（client-server）應用程式時，可使用存取權杖在你的應用程式與伺服器之間傳送使用者資料。

如果你在應用程式中取得存取權杖並將其傳送到伺服器，便可以從該伺服器發出 LINE Login API 呼叫。

若要了解更多資訊，請參閱[LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

若要取得 LINE SDK 儲存在你應用程式中的存取權杖，請使用共用的 `AccessTokenStore` 物件的 `current` 屬性，如下所示。

```swift
if let token = AccessTokenStore.shared.current {
    print(token.value)
}
```

<!-- note start -->

**注意**

將存取權杖傳送到你的伺服器時，我們建議將權杖加密，並使用 SSL 傳送加密後的資料。你也應該驗證伺服器收到的存取權杖與用來呼叫 LINE Login 的存取權杖相符，且頻道 ID（channel ID）與你頻道（channel）的頻道 ID 相符。

<!-- note end -->

## Verifying access tokens 

呼叫 `API.Auth.verifyAccessToken` 方法可驗證目前的存取權杖是否有效。此方法會回傳一個包含結果的 `AccessTokenVerifyResult` 物件。若權杖已成功通過驗證，回應會包含 `channelID`、`permissions` 與 `expiresIn` 等屬性。否則表示該權杖無效、已被撤銷或已過期，並會回傳錯誤。

```swift
API.Auth.verifyAccessToken { result in
    switch result {
    case .success(let value):
        print(value.channelID) // Bound channel ID of the token.
        print(value.permissions) // The permissions of this token.
        print(value.expiresIn) // How long it is before the token expires.
    case .failure(let error):
        print(error)
    }
}
```
