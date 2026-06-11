# 在 App 與伺服器之間建立安全的登入流程

本頁說明在使用 [LINE SDK](https://developers.line.biz/en/docs/line-login/overview/#native-app) 於原生 App 中導入 LINE Login 時，如何安全地處理使用者註冊與登入。

## Information that's safe to send and receive 

當使用者透過 LINE Login 登入您的 App 時，用戶端 App 與伺服器可以從 LINE Platform 收發以下資訊：

- ❌ 使用者個人資料（profile）細節
- ❌ 頻道 ID（Channel ID）

不過，上述這類資訊容易遭到偽冒（spoofing）及其他類型的攻擊。舉例來說，當用戶端傳送這類資訊時，伺服器若盲目信任將會非常危險。取而代之，您的用戶端應該傳送以下資料給伺服器：

- ✅ 存取權杖（access token）
- ✅ ID 權杖（ID token）

這些權杖能讓您的伺服器直接從 LINE Platform 取得可靠的資訊。

<!-- tip start -->

**如何使用本頁內容**

本節說明我們建議在使用 LINE SDK 時採用的設計概念。這些只是指引，並非範本。請務必在充分理解風險的前提下建立安全的系統。

<!-- tip end -->

## Using access tokens to register new users 

當新使用者使用 LINE Login 登入您的 App 時，您會想利用他們的 LINE 個人資料細節在資料庫中建立一位新使用者。

然而，如果您允許用戶端 App 直接將個人資料資訊傳送到伺服器，就會讓自己暴露在攻擊風險之中。

<!-- note start -->

**注意**

以下範例凸顯了使用者註冊與登入流程中潛在的弱點。

<!-- note end -->

![](https://developers.line.biz/media/line-login/new-user-login-bad.svg)

用戶端 App 應傳送存取權杖給伺服器，而非個人資料資訊。伺服器應驗證該存取權杖，並直接從 LINE Platform 取得使用者個人資料：

![Interactive SVG](https://developers.line.biz/media/line-login/new-user-login-standard.svg)

若要進一步了解圖中的 API 呼叫，請參閱 LINE Login v2.1 API 參考文件中的以下主題：

- [Verify that an access token is valid (GET /oauth2/v2.1/verify)](https://developers.line.biz/en/reference/line-login/#verify-access-token)
- [Get user profile (GET /v2/profile)](https://developers.line.biz/en/reference/line-login/#get-user-profile)

<!-- note start -->

**驗證存取權杖後仍需進一步確認**

當 LINE Login API 成功驗證存取權杖後，回應中會包含 `client_id` 屬性（即頻道 ID）與 `expires_in` 屬性（距離權杖過期的剩餘時間）。在使用該存取權杖之前，請確認這些屬性符合以下條件。

| 屬性 | 條件 |
| --- | --- |
| `client_id` | 與連結至原生 App 的 LINE Login 頻道之頻道 ID 相同 |
| `expires_in` | 正值 |

<!-- note end -->

## Using OpenID to register new users 

如果您的 App 支援 [OpenID Connect](https://openid.net/developers/how-connect-works/)，就不需要驗證存取權杖。取而代之，用戶端 App 會將 ID 權杖傳送到伺服器。伺服器應使用 LINE Platform 提供的端點（endpoint）來驗證您的 ID 權杖，以取得使用者的個人資料資訊：

<!-- tip start -->

**nonce：一次性使用的數字（number used once）**

nonce 是隨機產生的數字，用來讓每次登入嘗試都具有可唯一識別的特性。

正確使用 nonce 有助於防範[重送攻擊（replay attack）](https://en.wikipedia.org/wiki/Replay_attack)。

<!-- tip end -->

![Interactive SVG](https://developers.line.biz/media/line-login/new-user-login-openid.svg)

若要進一步了解圖中的 API 呼叫，請參閱 LINE Login API 參考文件中的以下主題：

- [Verify ID token (POST /oauth2/v2.1/verify)](https://developers.line.biz/en/reference/line-login/#verify-id-token)

關於如何在伺服器上處理 ID 權杖與 nonce 的細節，請參閱以下項目：

- [Using ID tokens on your server](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/#get-id-token)（LINE SDK for iOS Swift）
- [Using ID token on your server ](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#get-id-token)（LINE SDK for Android）

## Next steps 

前述範例大致說明了如何設計安全的使用者註冊與登入流程。但若需要將 LINE Login 整合進您 App 的具體操作說明，請參閱以下項目：

- LINE SDK for iOS Swift：
  - [Integrating LINE Login with your iOS app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/)
    - [Managing users](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/)
    - [Managing access tokens](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-access-tokens/)
- LINE SDK for Android：
  - [Integrating LINE Login with your Android app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/)
    - [Managing users](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/)
    - [Managing access tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/)
