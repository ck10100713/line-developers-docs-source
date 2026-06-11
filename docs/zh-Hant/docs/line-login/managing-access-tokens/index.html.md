# 管理存取權杖（Managing access tokens）

透過 LINE Login API 管理的存取權杖（access token）可驗證 app 是否已取得授權，能存取儲存在 LINE Platform 上的使用者資料（例如使用者 ID、顯示名稱、個人資料圖片與狀態消息）。

## Get the user's access token 

使用者驗證完成後，LINE Platform 會回傳一組存取權杖。此時你可以假定該 app 已取得存取使用者資料的權限。

如需深入了解，請參閱：

**LINE Login：**

- [Integrating LINE Login with your web app](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
- [Integrating LINE Login with your iOS app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/)
- [Integrating LINE Login with your Android app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/)
- [Integrating LINE Login with your Unity game](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/integrate-line-login/)
- [LINE SDK for Flutter](https://developers.line.biz/en/docs/line-login-sdks/flutter-sdk/)

**LIFF SDK：**

- [Developing a LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/)

<!-- note start -->

**存取權杖的有效期間（Access token validity period）**

存取權杖在發行後有效期間為 30 天。任何包含存取權杖的回應，也會在 `expires_in` 屬性中包含距離權杖到期的剩餘秒數。

<!-- note end -->

### Refresh tokens 

使用者驗證完成後，會連同存取權杖一併回傳一組更新權杖（refresh token）。

當存取權杖到期時，你可以使用更新權杖來取得新的存取權杖。如需深入了解，請參閱 LINE Login v2.1 API 參考文件中的 [Refresh access token](https://developers.line.biz/en/reference/line-login/#refresh-access-token)。

<!-- note start -->

**更新權杖的有效期間（Refresh token validity period）**

更新權杖自其對應的存取權杖發行起，最長有效期間為 90 天。若更新權杖到期，你必須提示使用者重新登入，以產生新的存取權杖。

<!-- note end -->

## Verify access tokens 

在你自己的伺服器上使用任何從 app 或外部伺服器接收到的存取權杖之前，請先驗證該存取權杖。

如需深入了解如何驗證存取權杖，請參閱 [Using access tokens to register new users](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-access-tokens)。
