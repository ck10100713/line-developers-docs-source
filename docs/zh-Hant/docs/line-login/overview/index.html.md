# LINE Login 總覽（LINE Login overview）

<!-- tip start -->

**開發者文件**

您正在閱讀的是 LINE 開發者文件。如果您想尋找使用 LINE app 或如何登入的協助，請參閱[說明中心](https://help.line.me/)。

<!-- tip end -->

## What is LINE Login 

LINE Login 是一項社群登入服務，可讓使用者運用自己的 LINE 帳號登入。LINE Login 免費提供。

將 LINE Login 整合至您的網站或 app 後，使用者就能依下列方式輕鬆註冊與登入：

- 當使用者註冊成為會員時，事先在 LINE 上登錄的[個人檔案資訊（profile information）](https://developers.line.biz/en/glossary/#profile-information)會自動填入，省去使用者輸入資訊的麻煩。
- 使用者可以透過 LINE Login 按鈕輕鬆登入，無需為每個網站記住電子郵件地址與密碼。

LINE Login 不僅適用於 iOS 與 Android 原生 app，也適用於網頁 app（網站）與 Unity 遊戲。

<!-- tip start -->

**整合 LINE Login 的網站範例**

舉例來說，電子書商店 [BOOK WALKER](https://global.bookwalker.jp/) 整合了包括 LINE Login 在內的多種社群登入服務，讓使用者能輕鬆註冊會員並持續使用該網站。

![E-bookstore login screen](https://developers.line.biz/media/line-login/overview/line-login-bookwalker-01-ja.png)

<!-- tip end -->

## Experience LINE Login on the demo site 

請試用示範體驗，親自感受 LINE Login。您可以用智慧型手機掃描 QR code 來存取示範網站，在手機上檢視這個示範。

![](https://developers.line.biz/media/line-login/demo/login-demo-qr-code-en.png)

<!-- note start -->

**示範網站取得的資料**

使用前請注意，LINE Login 示範 app 會從使用示範的使用者的 LINE 帳號取得個人檔案資訊（顯示名稱、個人檔案圖片 URL，以及使用者 ID）。在所取得的資訊中，只有使用者 ID 會儲存在伺服器上，且儲存的資料會每日刪除。

<!-- note end -->

## Start development to integrate LINE Login 

若要開始進行 LINE Login 整合開發，您首先需要建立一個 LINE Login 頻道（channel）。若要瞭解更多，請參閱 [LINE Login 入門](https://developers.line.biz/en/docs/line-login/getting-started/)。

### Integrating with web apps 

將 LINE Login 整合至您的網頁 app（網站），讓使用者更容易建立帳號與登入。透過 LINE Login，如果使用者已在裝置上登入 LINE，他們便能自動登入您的網頁 app。其驗證與授權流程是以 [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) 與 [OpenID® Connect](https://openid.net/specs/openid-connect-core-1_0.html) 協定為基礎。若要瞭解更多，請參閱[將 LINE Login 整合至您的網頁 app](https://developers.line.biz/en/docs/line-login/integrate-line-login/)。

關於 LINE Login 如何為使用者提供更佳體驗的範例，請參閱 [LINE STORE](https://store.line.me/) 網站。

![LINE Login](https://developers.line.biz/media/line-login/overview/line-login-web.png)

### Integrating with native apps 

使用我們的 SDK 將 LINE Login 加入您的 app，並讓 LINE 處理使用者驗證。當使用者已在行動裝置上登入 LINE 時，他們無需輸入電子郵件地址與密碼即可登入您的 app。我們為 Android、iOS 與 Unity 提供 SDK：

- [LINE SDK for iOS Swift overview](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/overview/)
- [LINE SDK for Android overview](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/overview/)
- [LINE SDK for Unity overview](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/overview/)
- [LINE SDK for Flutter](https://developers.line.biz/en/docs/line-login-sdks/flutter-sdk/)

舉例來說，LINE Rangers 遊戲就使用 LINE Login，讓使用者能以自己的 LINE 帳號輕鬆建立遊戲帳號。

![LINE Rangers 1](https://developers.line.biz/media/line-login/overview/line-login-rangers-1.png)
![LINE Rangers 3](https://developers.line.biz/media/line-login/overview/line-login-rangers-3.png)

## LINE Login authentication methods 

對於整合了 LINE Login 的網頁 app，使用者可以使用下列其中一種驗證方式：

| Authentication method | Description |
| --- | --- |
| [Auto login](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login) | 無需使用者操作即可登入。不會顯示 LINE Login 畫面或確認畫面 |
| [Log in with email address](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login) | 在 LINE Login 畫面輸入電子郵件地址與密碼以登入 |
| [Log in with QR code](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login) | 使用智慧型手機 LINE app 上的 QR code 讀取器，掃描顯示於 LINE Login 畫面上的 QR code 以登入 |
| [Single Sign On (SSO) login](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-sso-login) | 在顯示「Continue as」的確認畫面上點擊登入按鈕以登入 |

若要瞭解每種驗證方式實際顯示的畫面，以及這些畫面出現的條件，請參閱[使用者驗證](https://developers.line.biz/en/docs/line-login/integrate-line-login/#authentication-process)。

## Identifying users 

當使用者透過 LINE Login 登入您的 app，且您的 app 已取得該使用者的存取權杖（access token）後，app 便能取得該使用者在 LINE 上登錄的個人檔案資訊。

您可以取得使用者的 ID、顯示名稱、個人檔案圖片 URL 以及狀態訊息。

若要瞭解更多，請參閱[取得使用者個人檔案](https://developers.line.biz/en/docs/line-login/managing-users/#get-profile)。

## LINE Login versions 

LINE Login 支援 [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html)。關於 OpenID provider 的資訊，請參閱 [OpenID Provider Configuration Document](https://access.line.me/.well-known/openid-configuration)。

以下這些 LINE Login 版本皆已發布。每個版本支援的功能集各不相同。

| Version | Status | Description |
| --- | --- | --- |
| LINE Login v2.1 | [Active](https://developers.line.biz/en/glossary/#active)  | 此版本可以處理以 [OAuth 2.0 授權碼流程（authorization code flow）](https://datatracker.ietf.org/doc/html/rfc6749)為基礎的登入請求。它同時支援 [OpenID Connect](https://openid.net/developers/how-connect-works/) 協定，並允許您透過 ID token 取得使用者資料。<br>此版本於 2017 年 9 月 28 日發布。若要瞭解更多，請參閱 [LINE Login v2.1 released](https://developers.line.biz/en/news/2017/09/28/line-login-v21/)。 |
| LINE Login v2.0 | [Deprecated](https://developers.line.biz/en/glossary/#deprecated)  | 此版本於 2017 年 1 月 24 日發布，目前已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)，[生命週期結束（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)的日期尚未確定。我們建議您使用目前的版本（LINE Login v2.1）。在生命週期結束的公告與實際生命週期結束之間，會有一段緩衝期。 |
| LINE Login v1 | [End-of-life](https://developers.line.biz/en/glossary/#end-of-life) | **所有功能已於 2018 年 6 月 30 日終止，目前已無法使用。**若要瞭解更多，請參閱 [LINE Login v1 to be discontinued](https://developers.line.biz/en/news/2018/02/28/line-login-v1-notice/)。 |

## Require two-factor authentication 

具有 Admin 角色的使用者可以將頻道設定為：當使用者登入該頻道時要求進行雙重驗證（two-factor authentication）。

透過使用雙重驗證，您更有可能降低未經授權登入的風險，例如清單型攻擊（list-based attacks）。

從使用者保護的觀點來看，我們建議您要求進行雙重驗證。不過請注意，這可能會對使用者造成限制，例如需要一支已安裝 LINE app 的智慧型手機。

### What is two-factor authentication? 

雙重驗證是一種使用兩種要素來驗證使用者的方法：只有使用者本人知道的知識（例如密碼）、使用者所持有的物品（例如 IC 卡或智慧型手機），以及生物特徵資訊（例如指紋或臉部）。雙重驗證提高了即使密碼被第三方得知時，仍能防止未經授權登入的可能性。

LINE Login 透過對 LINE 帳號進行密碼驗證，並將畫面上顯示的驗證碼輸入到智慧型手機的 LINE 畫面中，以執行雙重驗證。

如果使用者是首次登入該服務，或是裝置或瀏覽器有所變更，使用者在輸入密碼後會被提示輸入驗證碼。

![](https://developers.line.biz/media/news/2023/login-flow-with-2fa-en.png)

除非使用者切換帳號或刪除瀏覽器的 cookie，否則他們會在 365 天內維持受信任狀態，期間不會被要求輸入驗證碼。

此外，如果他們已經使用同一個瀏覽器登入，雙重驗證將會被略過。

<!-- tip start -->

**建議使用 LINE Login v2.1**

雙重驗證可在 LINE Login v2.1 中使用。如果您使用的是 LINE Login v1.0（[生命週期結束（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)）或 LINE Login v2.0（[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)），我們建議您更新至 LINE Login v2.1。

關於各版本之間差異的更多資訊，請參閱 [LINE Login versions](https://developers.line.biz/en/docs/line-login/overview/#versions)。

<!-- tip end -->

### Require two-factor authentication setting on the LINE Developers Console 

要求雙重驗證可以在 [LINE Developers Console](https://developers.line.biz/console/) 上建立新頻道時以及編輯既有頻道時設定。

| Channel type       | When creating | When editing |
| ------------------ | ------------- | ------------ |
| LINE Login         | ✅            | ✅           |
| Blockchain Service | ✅            | ✅           |
| Messaging API      | - \*1         | ✅ \*2       |
| LINE MINI App      | ❌            | ❌           |

\*1 您無法在 LINE Developers Console 上建立 Messaging API 頻道

\*2 僅當先前建立的頻道持有 LIFF 時

#### Set when creating a channel 

當您在 LINE Developers Console 上建立新頻道時，可以將 **Require two-factor authentication** 開關切換至「開啟」（右側）來啟用此設定。預設設定為「開啟」。

![](https://developers.line.biz/media/news/2023/2fa-on-a-channel-en.png)

#### Set when editing an existing channel 

當您在 LINE Developers Console 上編輯既有頻道時，可以開啟／關閉 **Require two-factor authentication** 設定。

只有具備該頻道 Admin 角色的成員才能編輯此設定。若為 Member 角色，編輯頻道時不會顯示該設定欄位。

**Require two-factor authentication** 設定位於各頻道類型下方的分頁中：

| Channel type       | Tab name   |
| ------------------ | ---------- |
| LINE Login         | LINE Login |
| Blockchain Service | LINE Login |
| Messaging API      | LIFF       |

### Priority with the Two-factor Authentication Switch function 

LINE app 的[雙重驗證開關（Two-factor Authentication Switch）](https://developers.line.biz/en/news/2022/04/26/2fa-switch-function/)是一項功能：若使用者裝置上 **Home** > **Settings** > **Accounts** > **Two-factor authentication** 的切換開關為「ON」（右側），則在登入使用 LINE Login v2.1 的服務時，會提供雙重驗證。

頻道中的「要求雙重驗證」設定會覆寫使用者的裝置設定。換句話說，如果您在某個頻道上啟用 **Require two-factor authentication**，即使使用者裝置上的雙重驗證開關為關閉，使用者仍會被要求進行雙重驗證。

使用者裝置上的雙重驗證開關與頻道設定之間的關係如下：

|  | 使用者裝置上的設定 <br>OFF | 使用者裝置上的設定<br>ON |
| :-: | :-: | :-: |
| **頻道設定**<br>**OFF** | 雙重驗證停用 | 雙重驗證啟用 |
| **頻道設定**<br>**ON** | 雙重驗證啟用 | 雙重驗證啟用 |

### Differences in LINE Login behavior depending on authentication method 

依據 [LINE Login 驗證方式](https://developers.line.biz/en/docs/line-login/overview/#auth-method)的不同，即使您已開啟 **Require two-factor authentication**，使用者也可能不會被提示輸入驗證碼：

| Authentication method      | Two-factor authentication |
| -------------------------- | ------------------------- |
| Log in with email address  | 必須                       |
| Log in with QR code        | 必須                       |
| Auto login                 | 不需要                     |
| Single Sign On (SSO) login | 不需要                     |

## Related pages 

- [LINE Login 開發指南](https://developers.line.biz/en/docs/line-login/development-guidelines/)
- [LINE Login 安全檢查清單](https://developers.line.biz/en/docs/line-login/security-checklist/)
- [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)
