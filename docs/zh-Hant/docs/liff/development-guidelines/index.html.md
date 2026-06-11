# LIFF app 開發準則（LIFF app development guidelines）

使用 LIFF 開發網頁應用程式時，請遵循下列開發準則。

- [Be sure to securely handle user data](https://developers.line.biz/en/docs/liff/development-guidelines/#liff-development-rules1)
- [Cautions for initializing LIFF apps](https://developers.line.biz/en/docs/liff/development-guidelines/#liff-development-rules2)
- [LIFF app development rules](https://developers.line.biz/en/docs/liff/development-guidelines/#liff-development-rules3)
- [Prohibiting mass requests to the LINE Platform](https://developers.line.biz/en/docs/liff/development-guidelines/#prohibiting-mass-requests-to-line-platform)
- [Deauthorize your app when a user unregisters from your app](https://developers.line.biz/en/docs/liff/development-guidelines/#deauthorize)

LIFF 使用的是 LINE Login 提供的系統。因此，請遵守 LINE Login 文件中的 [LINE Login development guidelines](https://developers.line.biz/en/docs/line-login/development-guidelines/)。

<!-- note start -->

**Note**

LIFF 開發的基本規則是以 [Terms and Policies](https://developers.line.biz/en/terms-and-policies/) 中所述的內容為依據。

<!-- note end -->

## Be sure to securely handle user data 

- 在 LIFF app 與伺服器中使用使用者資料時，若未妥善處理使用者資料，LIFF app 將容易遭受冒用（spoofing）等各種攻擊。關於 LIFF app 與伺服器如何安全地使用從 LIFF app 取得的使用者資料，詳情請參閱 [Using user data in LIFF apps and servers](https://developers.line.biz/en/docs/liff/using-user-profile/)。
- LIFF endpoint URL 以及 LIFF URL 的 URL 片段（URL fragment）含有存取權杖（access token）與使用者 ID 等敏感資訊，請小心避免資料外洩。

## Cautions for initializing LIFF apps 

請參閱 [Important points to consider when initializing the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#initializing-liff-app-notes)。

## LIFF app development rules 

- 若要將 LIFF app 建置為 SPA（single page application，單頁應用程式），請使用 [History API](https://html.spec.whatwg.org/multipage/nav-history-apis.html#the-history-interface)。LIFF 對使用片段（fragment）進行路由的相容性有限。
- 當你實作會使用到下列任一裝置或 OS 功能的 API 時，請將該 API 實作為由使用者操作來觸發 API 呼叫。
  - 取得位置資訊
  - 存取相機
  - 存取麥克風
- 未取得使用者同意前，請勿透過 cookie、localStorage 或 sessionStorage 追蹤使用者，也不要將 LINE 使用者資料與外部工作階段（session）資訊連結。
- 在應用程式的測試階段，請透過你的網頁應用程式限制 LIFF app 的存取權限。
- LIFF app 的 URL scheme 以及任何在 LIFF app 中開啟的內容都必須是 **https**。若 URL scheme 為 http，內容會顯示在 [LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab) 中。在此情況下，即使該網頁應用程式已註冊為 LIFF app，它也不會以 LIFF app 的形式運作。

<!-- note start -->

**Use of cookies, localStorage, or sessionStorage in your LIFF app**

你可以在 LIFF app 中使用 cookie、localStorage 或 sessionStorage。不過，OS 的變更未來可能會限制它們的使用。

<!-- note end -->

## Prohibiting mass requests to the LINE Platform 

請勿為了負載測試（load testing）的目的，透過 [LIFF scheme](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-a-liff-app)（`https://liff.line.me/{liffId}`）存取 LIFF app，或對 [LIFF API](https://developers.line.biz/en/reference/liff/) 發出大量請求。要對 LIFF app 進行負載測試時，請準備一個不會對 LINE Platform 產生大量請求的測試環境。

<!-- note start -->

**Note**

若超過速率限制（rate limit），將回傳 `429 Too Many Requests` 並發生錯誤。

<!-- note end -->

## Deauthorize your app when a user unregisters from your app 

當使用者取消註冊你的 LIFF app，或使用者解除你的應用程式與 LINE app 之間的連結時，你必須執行下列動作：

1. 必須使用 [Deauthorize your app to which the user has granted permissions](https://developers.line.biz/en/reference/line-login/#deauthorize) 端點，代表使用者撤銷該已授權應用程式所獲得的權限。
1. 請在功能附近，或在使用者於註冊或授權時所同意的條款與條件中，說明當使用者取消註冊你的應用程式或解除你的應用程式與 LINE app 之間的連結時會發生什麼事，例如：
   - 例如：若你取消訂閱本服務，LY Corporation 將會收到你已取消訂閱的通知，且本服務與 LINE app 之間的連結將被解除。
   - 例如：若你執行此操作，LY Corporation 將會收到通知，且本服務與 LINE app 之間的連結將被解除。

下列使用情境需要進行撤銷授權（deauthorization）。

![Steps from linking your account to deauthorize app](https://developers.line.biz/media/line-login/development-guidelines/deauthorize-your-app-en.png)

當使用者登入整合了 LINE Login 與其 LINE 帳號的應用程式，並在頻道（channel）同意畫面上 [authorize the app](https://developers.line.biz/en/docs/line-login/integrate-line-login/#authorization-process) 後，該目標應用程式會出現在 LINE app 的 **設定** > **帳號** > **已授權的應用程式** 中。請撤銷該應用程式的授權，讓使用者在取消註冊你的應用程式後，權限不會繼續維持在已授權的狀態。

關於使用者如何撤銷其授予應用程式的權限，詳情請參閱 LINE Login 文件中的 [Managing authorized apps](https://developers.line.biz/en/docs/line-login/managing-authorized-apps/)。
