# 在外部瀏覽器中開啟 LINE MINI App（Open a LINE MINI App in an external browser）

<!-- tip start -->

**自 2025 年 10 月起，LINE MINI App 可在外部瀏覽器中使用**

如需更多資訊，請參閱 2025 年 9 月 26 日的新聞 [On October 1, 2025, all LINE MINI App users will be able to use the service in a web browser](https://developers.line.biz/en/news/2025/09/26/mini-app-browser/)。

<!-- tip end -->

開發 LINE MINI App 時，請確保當使用者以[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)存取端點 URL 時，LINE MINI App 服務也能正常使用。

在外部瀏覽器中使用 LINE MINI App 時，請注意以下事項：

<!-- table of contents -->

## Explicitly handle logging in for services that require LINE Login 

在外部瀏覽器中開啟 LINE MINI App 時，與 LIFF 瀏覽器不同，僅執行 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法並不會執行 LINE Login。

因此，如果您的服務需要透過 LINE Login 才能使用，請使用下列其中一種方法明確地執行 LINE Login：

### 1. Automatic execution of LINE Login at initialization 

在 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法的 `config` 物件中，將 `withLoginOnExternalBrowser` 屬性指定為 `true`，即可在外部瀏覽器中初始化 LIFF app 時自動執行 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法。

範例：

```js
liff
  .init({
    liffId: "1234567890-AbcdEfgh", // Use own liffId
    withLoginOnExternalBrowser: true, // Enable automatic login process
  })
  .then(() => {
    // Start to use liff's api
  });
```

### 2. Execute LINE Login when a user isn't logged in 

如果使用者尚未透過 LINE Login 登入，而您的服務又需要登入，您可以直接執行 LINE Login。

使用 [`liff.isLoggedIn()`](https://developers.line.biz/en/reference/liff/#is-logged-in) 方法檢查使用者的登入狀態，若使用者尚未登入，則執行 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法。

範例：

```js
if (!liff.isLoggedIn()) {
  liff.login();
}
```

如需更多資訊，請參閱 LIFF 文件中的 [To use LINE Login in an external browser](https://developers.line.biz/en/docs/liff/developing-liff-apps/#to-use-line-login-in-external-browser)。

## Direct users to the LINE app when using features that aren't available in an external browser 

如果您的 LINE MINI App 需要使用外部瀏覽器無法使用的功能，使用者就必須在 LINE app 上開啟該 LINE MINI App。

無法在外部瀏覽器中使用、且不保證能正常運作的功能如下：

- [liff.sendMessages()](https://developers.line.biz/en/reference/liff/#send-messages)
- [liff.openWindow()](https://developers.line.biz/en/reference/liff/#open-window)
- [liff.closeWindow()](https://developers.line.biz/en/reference/liff/#close-window)
- [liff.scanCode()](https://developers.line.biz/en/reference/liff/#scan-code)（已淘汰）
- [liff.iap.\*（應用程式內購買）](https://developers.line.biz/en/reference/line-mini-app/#in-app-purchase)

當在外部瀏覽器中開啟使用這些功能的 LINE MINI App 時，建議在畫面上放置一個指向該 LINE MINI App 的連結，並附上「若要使用此功能，您必須在 LINE app 中開啟 LINE MINI App」的文字。

請注意，[`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 與 [`liff.isInClient()`](https://developers.line.biz/en/reference/liff/#is-in-client) 方法可用於取得 LINE MINI App 的執行環境。如果您想根據 LINE MINI App 的執行環境變更顯示內容，建議使用這些方法。

## Assume that non-LINE users will open the LINE MINI App 

為了讓未使用 LINE 的使用者也能使用 LINE MINI App，請確保在外部瀏覽器中開啟 LINE MINI App 後，即使不需要 LINE Login 也能正常使用服務。

在外部瀏覽器中無需 LINE Login 即可使用的 LIFF API 屬性與方法如下：

- [liff.id](https://developers.line.biz/en/reference/liff/#id)
- [liff.ready](https://developers.line.biz/en/reference/liff/#ready)
- [liff.init()](https://developers.line.biz/en/reference/liff/#initialize-liff-app)
- [liff.getOS()](https://developers.line.biz/en/reference/liff/#get-os)
- [liff.getAppLanguage()](https://developers.line.biz/en/reference/liff/#get-app-language)
- [liff.getLanguage()](https://developers.line.biz/en/reference/liff/#get-language)（已淘汰）
- [liff.getVersion()](https://developers.line.biz/en/reference/liff/#get-version)
- [liff.getLineVersion()](https://developers.line.biz/en/reference/liff/#get-line-version)
- [liff.isInClient()](https://developers.line.biz/en/reference/liff/#is-in-client)
- [liff.isLoggedIn()](https://developers.line.biz/en/reference/liff/#is-logged-in)
- [liff.permanentLink.createUrlBy()](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by)
- [liff.use()](https://developers.line.biz/en/reference/liff/#use)
