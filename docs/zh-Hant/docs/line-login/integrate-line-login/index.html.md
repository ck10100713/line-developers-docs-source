# 將 LINE Login 整合至你的 Web 應用程式（Integrating LINE Login with your web app）

[LINE Login v2.1](https://developers.line.biz/en/docs/line-login/overview/) 支援 [OpenID Connect](https://openid.net/developers/how-connect-works/) 協定，可讓你透過 ID token 取得使用者資料。本指南將說明如何將其整合到你的 Web 應用程式中。

如果你還沒有可更新以支援 LINE Login 的現有應用程式，可以使用範例應用程式來跟著操作。如需瞭解更多資訊，請參閱 [Getting started with LINE Login](https://developers.line.biz/en/docs/line-login/getting-started/)。

<!-- note start -->

**Note**

- 如果你要將 LINE Login v2.0 整合至 Web 應用程式，請參閱 [Integrating LINE Login (v2.0) with your web app](https://developers.line.biz/en/docs/line-login/integrate-line-login-v2/)。
- 如果你的開發環境有可用的 LINE SDK，我們強烈建議使用 LINE SDK 來建構 LINE Login 整合。我們不建議在原生應用程式（native app）上使用本頁所述的流程。如需瞭解使用 LINE SDK 的更多資訊，請參閱 [Integrating with native apps](https://developers.line.biz/en/docs/line-login/overview/#native-app)。

<!-- note end -->

## Login flow 

Web 應用程式的 LINE Login 流程（網頁登入）是以 [OAuth 2.0 authorization code grant flow](https://datatracker.ietf.org/doc/html/rfc6749) 與 [OpenID Connect](https://openid.net/developers/how-connect-works/) 協定為基礎。網頁登入流程的概觀如下所示。

Web 應用程式必須實作流程圖中與其相關的所有登入流程部分。

![Web login flow](https://developers.line.biz/media/line-login/web-login-flow.svg)

## Create a channel 

[建立一個 LINE Login 頻道（channel）](https://developers.line.biz/en/docs/line-login/getting-started/#step-1-create-channel)，並將其設定為可搭配 Web 應用程式使用。

- [設定 callback URL](https://developers.line.biz/en/docs/line-login/integrate-line-login/#setting-callback-url)
- [申請存取使用者電子郵件地址的權限](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)

### Setting a callback URL 

在使用者通過驗證並授權你的 Web 應用程式之後，授權碼（authorization code）與 `state` 會被傳送至 callback URL。

請在 [LINE Developers Console](https://developers.line.biz/console/) 中你的頻道設定的 **LINE Login** 分頁設定 callback URL。你可以透過新增一行的方式，為每個頻道指定多個 callback URL。

![Redirect settings](https://developers.line.biz/media/line-login/integrate-login-web/redirect-settings-en.png)

### Requesting permission to access the user's email address 

LINE Login v2.1 可讓你取得任何使用 LINE Login 登入你應用程式之使用者的電子郵件地址。

若要透過 Web 應用程式取得使用者的電子郵件地址，你必須先在 [LINE Developers Console](https://developers.line.biz/console/) 申請相關權限。

1. 在 **Basic settings** 分頁中，於 **OpenID Connect** 下方點擊 **Apply**。

   ![Requesting permission to access the user's email address](https://developers.line.biz/media/line-login/integrate-login-web/apply-email.png)

1. 同意條款，並上傳一張畫面截圖，該畫面需說明你正在收集使用者的電子郵件地址，以及收集用途。

   一旦你的申請表單被接受，**Email address permission** 下方會顯示「Applied」。

## Authenticating users and making authorization requests 

開始進行使用者於 LINE Platform 的驗證程序，並對你的應用程式進行授權。當使用者點擊 LINE Login 按鈕時，將他們重新導向至帶有必要查詢參數的授權 URL，如下方範例所示。

```
https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%3Fkey%3Dvalue&state=12345abcde&scope=profile%20openid&nonce=09876xyz
```

你可以將下列查詢參數傳遞給授權 URL。

| Parameters | Type | Required? | Description |
| --- | --- | --- | --- |
| `response_type` | String | Required  | `code` |
| `client_id` | String | Required  | LINE Login 頻道 ID。你可以在 [LINE Developers Console](https://developers.line.biz/console/) 找到。 |
| `redirect_uri` | String | Required  | 在 [LINE Developers Console](https://developers.line.biz/console/) 註冊的 callback URL 經 URL 編碼後的字串。你可以加入任何查詢參數。 |
| `state` | String | Required  | 用於防止[跨站請求偽造（cross-site request forgery）](https://wikipedia.org/wiki/Cross-site_request_forgery)的唯一英數字串。**你的 Web 應用程式應該為每個登入工作階段（login session）產生一個隨機值。** 此值不可為 URL 編碼字串。 |
| `scope` | String | Required  | 向使用者要求的權限。如需瞭解更多資訊，請參閱 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。 |
| `nonce` | String | Optional  | 用於防止[重放攻擊（replay attacks）](https://en.wikipedia.org/wiki/Replay_attack)的字串。此值會回傳於 [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) 中。 |
| `prompt` | String | Optional  | <p>決定是否顯示驗證或授權畫面的設定。你可以設定下列其中一個值：</p><ul><li>`consent`：用於即使使用者已授予所有要求的權限，仍強制顯示同意畫面。</li><li>`none`：當[自動登入（auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)已啟用，且使用者已登入並同意授予目標頻道權限時，用於略過[單一登入（Single Sign On，SSO）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-sso-login)驗證畫面。</li><li>`login`：用於即使使用者已登入或仍有單一登入工作階段，仍顯示驗證畫面。請注意，若你設定 `login`，自動登入將會被停用。你也可以在回應中回傳的 [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) 的 `amr` 中查看所使用的驗證方法。</li></ul> |
| `max_age` | Number | Optional  | 自上次驗證使用者以來，所允許經過的時間（以秒為單位）。對應於 [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) 之「Authentication Request」章節中定義的 `max_age` 參數。 |
| `ui_locales` | String | Optional  | LINE Login 畫面的顯示語言。以一個或多個 [RFC 5646 (BCP 47)](https://datatracker.ietf.org/doc/html/rfc5646) 語言標籤指定，以空格分隔，並依偏好順序排列。對應於 [OpenID Connect Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) 之「Authentication Request」章節中定義的 `ui_locales` 參數。 |
| `bot_prompt` | String | Optional  | 在登入期間顯示將 LINE 官方帳號加為好友的選項。設定為 `normal` 或 `aggressive`。如需瞭解更多資訊，請參閱 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。 |
| `initial_amr_display` | String | Optional  | 若指定 `lineqr`，則預設會顯示[使用 QR code 登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login)，而非[使用電子郵件地址登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login)。 |
| `switch_amr` | Boolean | Optional  | 若設定為 `false`，則隱藏用於變更登入方法的按鈕，例如「使用電子郵件登入」或「QR code 登入」。預設值為 `true`。 |
| `disable_auto_login` | Boolean | Optional  | 若設定為 `true`，[自動登入（auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)將被停用。預設值為 `false`。<br>當此值為 `true` 時，若 SSO 可用，則顯示[單一登入（Single Sign On，SSO）登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-sso-login)；若不可用，則顯示[使用電子郵件地址登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login)。 |
| `disable_ios_auto_login` | Boolean | Optional  | 若設定為 `true`，[自動登入（auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)將在 iOS 上被停用。預設值為 `false`。我們建議使用後來新增的 `disable_auto_login` 參數。 |
| `code_challenge` | String | Optional  | 用於支援 LINE Login PKCE 的必要參數。此為將唯一的 `code_verifier` 以 SHA256 雜湊後，再編碼為 Base64URL 格式所得的值。預設值為 `null`。若未指定值，則該請求不支援 PKCE。<br>如需瞭解如何實作 PKCE 的更多資訊，請參閱 LINE Login 文件中的 [Implement PKCE for LINE Login](https://developers.line.biz/en/docs/line-login/integrate-pkce/#how-to-integrate-pkce)。 |
| `code_challenge_method` | String | Optional  | `S256`（代表雜湊函式 `SHA256`。）<br>指定 `code_verifier` 的轉換方法。基於安全考量，LINE Login 僅支援 `S256`。<br>如需瞭解如何實作 PKCE 的更多資訊，請參閱 LINE Login 文件中的 [Implement PKCE for LINE Login](https://developers.line.biz/en/docs/line-login/integrate-pkce/#how-to-integrate-pkce)。 |
| `response_mode` | String | Optional  | <p>決定授權回應參數如何回傳給你的 Web 應用程式的設定。你可以設定下列其中一個值。預設值為 `query`。</p><ul><li>`query`：授權回應參數以查詢參數的形式回傳至 callback URL。\*1</li><li>`form_post`：授權回應參數以 HTTP POST 請求的請求本文（request body）回傳。\*2</li><li>`query.jwt`：授權回應參數被放入 JWT 中，並以查詢參數的形式回傳至 callback URL。與設定 `jwt` 時相同。\*3</li><li>`form_post.jwt`：授權回應參數被放入 JWT 中，並以 HTTP POST 請求的請求本文回傳。\*3</li><li>`jwt`：授權回應參數被放入 JWT 中，並以 callback URL 的查詢參數形式回傳。與設定 `query.jwt` 時相同。\*3</li></ul>\*1 對應於 [OAuth 2.0 Multiple Response Type Encoding Practices](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html) 之 [2.1. Response Modes](https://openid.net/specs/oauth-v2-multiple-response-types-1_0.html#ResponseModes) 章節中定義的 `query`。<br>\*2 對應於 [OAuth 2.0 Form Post Response Mode](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html) 之 [2. Form Post Response Mode](https://openid.net/specs/oauth-v2-form-post-response-mode-1_0.html#FormPostResponseMode) 章節中定義的 `form_post`。<br>\*3 對應於 [Financial-grade API: JWT Secured Authorization Response Mode for OAuth 2.0 (JARM)](https://openid.net/specs/openid-financial-api-jarm.html) 之 [4.3. Response Encoding](https://openid.net/specs/openid-financial-api-jarm.html#response-encoding) 章節中定義的 `query.jwt`、`form_post.jwt` 與 `jwt`。 |

<!-- tip start -->

**Tip**

- 在你的 Web 應用程式中加入 LINE Login 按鈕時，請遵循 [LINE Login button design guidelines](https://developers.line.biz/en/docs/line-login/login-button/)。
- 你也可以直接連結至授權 URL，而不顯示 LINE Login 按鈕。
- 使用者的驗證憑證不會被傳送至你的 Web 應用程式。

<!-- tip end -->

<!-- note start -->

**Authorization requests within LIFF browser**

在 LIFF 瀏覽器中進行 LINE Login 授權請求的行為無法獲得保證。此外，當從外部瀏覽器開啟 LIFF App 時，請使用 [liff.login()](https://developers.line.biz/en/reference/liff/#login) 而非透過 LINE Login 的授權請求。

<!-- note end -->

### Scopes 

你可以使用 `scope` 參數指定下列 scope。若要指定多個 scope，請使用 URL 編碼的空白字元（%20）分隔。

| Scope | Profile<br>information | [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens)<br>(including user ID) | Display name<br>in [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) | Profile image URL<br>in [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) | Email address<br>in [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) |
| --- | --- | --- | --- | --- | --- |
| `profile` | ✓ | - | - | - | - |
| `profile%20openid` | ✓ | ✓ | ✓ | ✓ | - |
| `profile%20openid%20email` | ✓ | ✓ | ✓ | ✓ | ✓（請見註解） |
| `openid` | - | ✓ | - | - | - |
| `openid%20email` | - | ✓ | - | - | ✓（請見註解） |

**Note：** 在你能夠指定 `email` scope 並向使用者要求取得其電子郵件地址權限之前，你必須先[提交申請以要求存取使用者的電子郵件地址](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)。

<!-- tip start -->

**Requesting scopes not listed above**

- 如果你希望取得使用者向 LINE Profile+ 註冊的資訊（姓名、性別、生日、電話號碼、地址），你需要經過申請流程。如需瞭解更多資訊，請參閱企業客戶選項文件中的 [LINE Profile+](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/)。
- 你需要具備 `profile` scope 的存取權杖（access token），才能[判斷使用者是否已將 LINE 官方帳號加為好友](https://developers.line.biz/en/docs/line-login/link-a-bot/#use-line-login-api)。

<!-- tip end -->

### User authentication 

<!-- tip start -->

**User authentication is handled directly by the LINE Platform**

支援 LINE Login 的 Web 應用程式不必自行實作驗證程序。

<!-- tip end -->

使用者被重新導向至授權 URL 後，可透過下列其中一種驗證方法登入。

| Authentication method | Description |
| --- | --- |
| [自動登入（Auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login) | 無需使用者操作即可登入。不會顯示 LINE Login 畫面或確認畫面 |
| [使用電子郵件地址登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login) | 在 LINE Login 畫面輸入電子郵件地址與密碼以登入 |
| [使用 QR code 登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login) | 使用智慧型手機 LINE app 上的 QR code 讀取器掃描 LINE Login 畫面上顯示的 QR code 以登入 |
| [單一登入（Single Sign On，SSO）登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-sso-login) | 在顯示「Continue as」的確認畫面上點擊登入按鈕以登入 |

在自動登入可用的環境中，自動登入會優先採用。當自動登入不可用時，若 SSO 可用，則顯示[單一登入（Single Sign On，SSO）登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-sso-login)；若不可用，則顯示[使用電子郵件地址登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login)。

<!-- note start -->

**Auto login takes precedence over SSO login**

在自動登入與 SSO 登入皆已啟用的環境中，自動登入會優先採用。如需瞭解更多資訊，請參閱 2021 年 7 月 12 日發布的新聞「[Auto login will take precedence over SSO login for LINE Login](https://developers.line.biz/en/news/2021/07/12/auto-login-takes-precedence-over-sso/)」。

如果你希望使用者透過 SSO 登入而非自動登入，可以在[驗證使用者並進行授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)時，於授權 URL 加入特定查詢參數（`disable_auto_login`）以停用自動登入。

<!-- note end -->

<!-- note start -->

**Login notification**

登入後，LINE 官方帳號會傳送登入通知。如需瞭解登入通知的更多資訊，請參閱說明中心的 [I got a notification about a detected login](https://help.line.me/line/android/pc?lang=en&contentId=20014794)。

<!-- note end -->

<!-- tip start -->

**Authentication method chosen by the user**

你可以檢查 ID token 來判斷使用者選擇了哪種驗證方法。如需瞭解 ID token 的更多資訊，請參閱 [Getting an access token](https://developers.line.biz/en/docs/line-login/integrate-line-login/#get-access-token) 的「Response」章節。

<!-- tip end -->

#### Auto login 

無需使用者操作即可啟用登入。不會顯示 LINE Login 畫面或確認畫面。

當使用者在登入智慧型手機 LINE app 的狀態下，從下列其中一種瀏覽器造訪授權 URL 時，會自動登入。

- LINE 的應用程式內瀏覽器（in-app browser）
- 用於 LINE Login 的外部瀏覽器

如下所示，登入時會自動啟動 LINE app，使用者無需任何操作即可登入：

![](https://developers.line.biz/media/line-login/integrate-login-web/auto-ligin-animation.gif)

<!-- note start -->

**Auto login doesn't work on LINE for PC**

如需瞭解可使用自動登入之環境的更多資訊，請參閱 FAQ 中的 [How does auto login work?](https://developers.line.biz/en/faq/#how-does-auto-login-work)。

<!-- note end -->

<!-- note start -->

**Auto login may fail**

如果使用者在啟用私密瀏覽（private browsing）的情況下存取 Web 應用程式，自動登入可能會失敗。

在其他情況下，視使用者 OS 的規格而定，自動登入也可能失敗。由於 OS 的規格並未完全公開，LINE Platform 可能難以避免自動登入失敗的條件。

如需瞭解更多資訊，請參閱 [How to handle auto login failure](https://developers.line.biz/en/docs/line-login/how-to-handle-auto-login-failure/)。

<!-- note end -->

<!-- tip start -->

**About automatic login from the Yahoo! JAPAN app**

當從 Yahoo! Japan app 存取整合了具 PKCE 實作之 LINE Login 的 Web 應用程式時，會啟用自動登入。如需瞭解 LINE Login PKCE 支援的更多資訊，請參閱 LINE Login 文件中的 [PKCE support for LINE Login](https://developers.line.biz/en/docs/line-login/integrate-pkce/)。

<!-- tip end -->

#### Log in with email address or QR code 

使用者可透過下列其中一種驗證方法登入。

- 使用電子郵件地址登入
- 使用 QR code 登入

![Login dialog](https://developers.line.biz/media/line-login/integrate-login-web/login-with-new-session.png)

當使用者在外部瀏覽器中首次存取授權 URL，且未登入智慧型手機 LINE app 時，可使用這些登入方法。

#### Single Sign On (SSO) login 

使用者只需點擊登入按鈕即可登入。

![Confirmation Screen](https://developers.line.biz/media/line-login/integrate-login-web/sso.png)

當使用者在先前曾用於登入 LINE 的外部瀏覽器中造訪授權 URL 時，SSO 即可使用。

<!-- note start -->

**SSO is a function that uses cookies**

當你從 Web 應用程式執行 LINE Login 後，cookie 會儲存在網域名稱 `access.line.me` 之下。只要該 cookie 仍有效，在同一瀏覽器中登入時就會顯示 SSO 畫面。

<!-- note end -->

<!-- note start -->

**Auto login takes precedence over SSO login**

在自動登入與 SSO 登入皆已啟用的環境中，自動登入會優先採用。如需瞭解更多資訊，請參閱 2021 年 7 月 12 日發布的新聞「[Auto login will take precedence over SSO login for LINE Login](https://developers.line.biz/en/news/2021/07/12/auto-login-takes-precedence-over-sso/)」。

如果你希望使用者透過 SSO 登入而非自動登入，可以在[驗證使用者並進行授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)時，於授權 URL 加入特定查詢參數（`disable_auto_login`）以停用自動登入。

<!-- note end -->

### User authorization 

<!-- tip start -->

**User authorization is handled directly by the LINE Platform**

支援 LINE Login 的 Web 應用程式不必自行實作授權程序。

<!-- tip end -->

開發人員在 `scope` 參數中指定想要存取的資訊，使用者則會被要求授權這些請求。

請注意，使用者可能在未授予部分或全部要求權限的情況下存取你的 Web 應用程式。在建構 Web 應用程式時，你應該考慮到使用者可能不會授予你在授權 URL 中指定的權限。

**同意畫面範例：**

![Consent screen](https://developers.line.biz/media/line-login/integrate-login-web/consent-screen-en.png)

<!-- note start -->

**The consent screen may not always be shown**

- 如果 `scope` 參數中指定的權限為 `profile` 和／或 `openid`，且使用者已授予所有權限，則不會顯示同意畫面。
- 如果權限包含 `email`，除非使用者的電子郵件地址有變更，否則在一段期間內不會顯示同意畫面。

<!-- note end -->

## Receiving the authorization response or error response with a web app 

當使用者完成驗證與授權程序後，會被重新導向至 callback URL。

如果使用者已授予你的應用程式存取權，則會回傳包含授權碼的授權回應。如果使用者未授予你的應用程式存取權，則會回傳錯誤回應。

### Receiving the authorization code 

當使用者通過驗證並完成授權步驟後，會被重新導向至 callback URL。包含授權碼在內的授權回應參數如何接收，取決於授權請求的 `response_mode` 參數的值。如需瞭解更多資訊，請參閱 [Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)。

授權回應參數如下：

| Parameter | Type | Description |
| --- | --- | --- |
| `code` | String | 用於取得存取權杖的授權碼。有效期間為 10 分鐘。此授權碼僅能使用一次。 |
| `state` | String | 用於防止[跨站請求偽造（cross-site request forgery）](https://wikipedia.org/wiki/Cross-site_request_forgery)的唯一英數字串。請驗證此值是否與你提供給授權 URL 的 `state` 參數值相符。 |
| `friendship_status_changed` | Boolean | 當使用者登入時，若使用者與連結至該頻道的 LINE 官方帳號之間的好友關係狀態（friendship status）有所變更，則為 `true`。否則為 `false`。此參數僅在你[驗證使用者並進行授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)時指定 `bot_prompt` 查詢參數，且使用者在登入時被提供將你的 LINE 官方帳號加為好友的選項時才會回傳。如需瞭解更多資訊，請參閱 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。 |
| `liffClientId` | String | LINE Login 頻道 ID。此參數僅在使用 LIFF app 中的 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法執行登入程序時才會回傳。為確保 LIFF app 正常運作，請勿變更此參數。 |
| `liffRedirectUri` | String | 登入後於 LIFF app 中顯示的 URL。為 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法的 `redirectUri` 屬性中所指定的值。此參數僅在使用 LIFF app 中的 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法執行登入程序時才會回傳。為確保 LIFF app 正常運作，請勿變更此參數。 |

當授權請求的 `query` 參數設定為 `query.jwt` 時的重新導向目標 URL 範例：

```
https://example.com/callback?code=abcd1234&state=0987poi&friendship_status_changed=true
```

當授權請求的 `response_mode` 參數設定為 `query.jwt` 或 `jwt` 時的重新導向目標 URL 範例：

```
https://example.com/callback?response=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### Receiving an error response 

如果使用者拒絕授予你的應用程式權限，或請求失敗（`client_id` 或 `redirect_uri` 查詢參數含有無效值的情況除外），他們會被重新導向至帶有下列查詢參數的 callback URL：

| Parameter | Type | Required  | Description |
| --- | --- | --- | --- |
| `error` | String | Required | [錯誤碼（Error code）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#error-codes)。 |
| `error_description` | String | Optional  | 錯誤的描述。 |
| `state` | String | Optional  | 授權 URL 中包含的 `state` 參數。你可以使用此值來判斷哪個程序被拒絕。 |

重新導向目標的 URL 範例：

```
https://example.com/callback?error=ACCESS_DENIED&error_description=The+resource+owner+denied+the+request.&state=0987poi
```

#### Error codes 

| Error code | Description |
| --- | --- |
| `INVALID_REQUEST` | 請求有問題。請檢查授權 URL 的查詢參數。 |
| `ACCESS_DENIED` | 使用者在同意畫面上取消，並拒絕授予你的應用程式權限。 |
| `UNSUPPORTED_RESPONSE_TYPE` | `response_type` 查詢參數的值有問題。LINE Login 僅支援 `code`。 |
| `INVALID_SCOPE` | <p>`scope` 查詢參數的值有問題。請確認你已指定適當的值。</p><ul><li>需要 `profile` 或 `openid`。</li><li>若你指定 `email`，則也必須指定 `openid`。</li></ul> |
| `SERVER_ERROR` | LINE Login 伺服器發生未預期的錯誤。 |
| `LOGIN_REQUIRED` | 你為 `prompt` 參數指定了 `none`，但自動登入無法在使用者的裝置上運作，或使用者未登入。 |
| `INTERACTION_REQUIRED` | 你為 `prompt` 參數指定了 `none`，但自動登入無法在使用者的裝置上運作。 |

## Getting an access token with a web app 

如果你從 LINE Platform 連同授權碼一起收到的 `state` 參數，與你在[驗證使用者並進行授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)時所指定的 `state` 參數相符，你就可以取得存取權杖。

如需瞭解取得存取權杖的更多資訊，請參閱 LINE Login v2.1 API 參考文件中的 [issue access token](https://developers.line.biz/en/reference/line-login/#issue-access-token)。

請求範例：

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=1234567890abcde' \
--data-urlencode 'redirect_uri=https://example.com/auth?key=value' \
-d 'client_id=1234567890' \
-d 'client_secret=1234567890abcdefghij1234567890ab'
```

### Response 

LINE Platform 會驗證請求，並回傳如下表所示的存取權杖與其他資料。

<!-- note start -->

**Note**

新增或變更的 LINE Login 功能可能會導致 payload JSON 物件結構的變化。這些變化可能包含新增的屬性、屬性順序的變動，以及新增／移除的空白字元和換行。請將你的後端設計成能夠處理具有非預期結構的 payload 資料物件。

<!-- note end -->

| Property | Type | Description |
| --- | --- | --- |
| `access_token` | String | 存取權杖。有效期間為 30 天。 |
| `expires_in` | Number | 存取權杖到期前的剩餘時間（以秒為單位）。 |
| `id_token` | String | 包含使用者資訊的 [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)。此欄位僅在 scope 中指定 openid 時才會回傳。如需瞭解更多資訊，請參閱 [Get profile information from ID tokens](https://developers.line.biz/en/docs/line-login/verify-id-token/)。 |
| `refresh_token` | String | 用於取得新存取權杖的權杖。有效期間至存取權杖核發後 90 天為止。 |
| `scope` | String | 使用者授予的權限。但即使已授予 `email` scope 的權限，它也不會作為 `scope` 屬性的值回傳。 |
| `token_type` | String | `Bearer` |

回應範例：

```json
{
  "access_token": "bNl4YEFPI/hjFWhTqexp4MuEw5YPs...",
  "expires_in": 2592000,
  "id_token": "eyJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "Aa1FdeggRhTnPNNpxr8p",
  "scope": "profile",
  "token_type": "Bearer"
}
```

如需瞭解更多資訊，請參閱 LINE Login v2.1 API 參考文件中的 [Issuing access tokens](https://developers.line.biz/en/reference/line-login/#issue-access-token)。

## Getting profile information from ID tokens 

LINE Platform 會核發符合 [OpenID Connect](https://openid.net/developers/how-connect-works/) 規範的 ID token，讓你能夠安全地從 LINE Platform 取得使用者的[個人檔案資訊（profile information）](https://developers.line.biz/en/glossary/#profile-information)（user ID、顯示名稱、個人檔案圖片、電子郵件地址）。

如需瞭解更多資訊，請參閱 [Get profile information from ID tokens](https://developers.line.biz/en/docs/line-login/verify-id-token/)。

## Next steps 

當你取得存取權杖後，可以使用它來執行下列操作：

- [取得使用者與 LINE 官方帳號的好友關係狀態](https://developers.line.biz/en/docs/line-login/link-a-bot/#use-line-login-api)
- [管理存取權杖](https://developers.line.biz/en/docs/line-login/managing-access-tokens/)
- [管理使用者](https://developers.line.biz/en/docs/line-login/managing-users/)
