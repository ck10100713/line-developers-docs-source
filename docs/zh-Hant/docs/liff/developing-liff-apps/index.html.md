# 開發 LIFF app（Developing a LIFF app）

LIFF app 是一個以 HTML 與 JavaScript 為基礎的 web app。在此，我們會說明開發 LIFF app 的流程，以及建構 LIFF app 時特有的處理程序。

<!-- table of contents -->

## Setting the title of the LIFF app 

LIFF app 的標題會顯示在 LIFF app 的標頭。請在 LIFF app HTML 原始碼的 `<title>` 元素中指定 LIFF app 的名稱。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The title</title>
```

## Integrating the LIFF SDK with the LIFF app 

你可以使用以下方法將 LIFF SDK 嵌入 LIFF app：

- [指定 CDN 路徑](https://developers.line.biz/en/docs/liff/developing-liff-apps/#specify-cdn-path)
- [使用 npm 套件](https://developers.line.biz/en/docs/liff/developing-liff-apps/#use-npm-package)

### Specify the CDN path 

若要使用 LIFF SDK 的功能，請在 LIFF app HTML 原始碼的 `<script>` 元素的 `src` 屬性中指定 LIFF SDK 的 URL。我們為 LIFF 準備了以下兩種 CDN 路徑。請依你的用途指定適合的 CDN 路徑。

| CDN 路徑 | 說明 |
| --- | --- |
| CDN edge path | 這是只包含 MAJOR 版本的 CDN 路徑。如果你想隨時使用最新的 LIFF 功能，請使用此 CDN 路徑。只有在發布新的 MAJOR 版本時，你才需要更新 URL。<br>例如：https://static.line-scdn.net/liff/edge/**2**/sdk.js |
| CDN fixed path | 這是包含到 PATCH 版本的 CDN 路徑。如果你想使用特定版本的 LIFF 功能，請使用此 CDN 路徑。只要你不更新 LIFF app，就可以持續使用指定的 PATCH 版本。只有當你想要套用我們的新功能、安全性更新與錯誤修正時，才需要更新 URL。它不會自動更新，也不會受到 LIFF SDK 更新的影響。<br>例如：https://static.line-scdn.net/liff/edge/**versions/2.22.3**/sdk.js |

<!-- note start -->

**你應該使用哪個版本？**

使用 CDN fixed path 的開發者需要自行決定何時更新 LIFF app。你可以透過經常查看 LIFF 文件中的[Release notes](https://developers.line.biz/en/docs/liff/release-notes/)來評估我們提供的每次更新，並決定該更新是否適合你。

<!-- note end -->

指定 CDN fixed path 的範例：

```html
<script charset="utf-8" src="https://static.line-scdn.net/liff/edge/versions/2.22.3/sdk.js"></script>
```

<!-- note start -->

**LIFF SDK 以 UTF-8 編寫**

LIFF SDK 是以 UTF-8 編寫的，因此如果你的 HTML 原始碼使用了與 UTF-8 不同的字元編碼，請務必同時指定 `charset="utf-8"`。

<!-- note end -->

### Use the npm package 

LIFF SDK 也以 npm 套件的形式提供。你可以使用 npm 安裝 LIFF SDK。

<!-- note start -->

**管理你的 SDK 版本**

使用適當的 SDK 版本是開發者的責任。為了讓你的 SDK 版本保持最新，請定期查看 [LIFF release notes](https://developers.line.biz/en/docs/liff/release-notes/)，並經常更新你本地的 SDK。如需更多關於 LIFF 版本政策的資訊，請參閱 [LIFF SDK (sdk.js) update policy](https://developers.line.biz/en/docs/liff/versioning-policy/#update-policy)。

<!-- note end -->

<!-- note start -->

**在使用 webpack v5 的專案中使用 npm 版的 LIFF v2.16.0 或更早版本時，建構期間會發生錯誤。**

[webpack v5 已移除 Node.js polyfill。](https://webpack.js.org/blog/2020-10-10-webpack-5-release/#automatic-nodejs-polyfills-removed)因此，如果你在使用 webpack v5 的專案中使用 npm 版的 LIFF v2.16.0 或更早版本，將會得到建構錯誤。如需更多資訊，請參閱 2021 年 10 月 26 日的消息 [LIFF v2.16.1 released](https://developers.line.biz/en/news/2021/10/26/release-liff-2-16-1/)。

<!-- note end -->

若要透過 npm 安裝 LIFF SDK 並匯入你的 app，請依照以下步驟操作：

1. 在你的終端機執行以下指令，透過 npm 安裝 LIFF SDK：

   ```bash
   $ npm install --save @line/liff
   ```

   或者，你也可以在終端機執行以下指令，透過 Yarn 安裝 LIFF SDK：

   ```bash
   $ yarn add @line/liff
   ```

1. 將 SDK 匯入你的 app

   在你的 JavaScript 或 TypeScript 檔案中加入以下程式碼：

   ```js
   import liff from "@line/liff";

   liff.init({
     liffId: "1234567890-AbcdEfgh", // Use own liffId
   });
   ```

   `@line/liff` 套件中已包含 TypeScript 的型別定義。

   <!-- note start -->

   **不要宣告或修改 window.liff**

   為了向後相容，請勿宣告或修改全域 LIFF 執行個體 `window.liff`。宣告或修改 window.liff 可能會導致 LINE app 故障。

   <!-- note end -->

相關頁面：[https://www.npmjs.com/package/@line/liff](https://www.npmjs.com/package/@line/liff)

<!-- tip start -->

**縮減 LIFF SDK 的檔案大小**

使用 pluggable SDK 可縮減 LIFF SDK 的檔案大小。如需更多資訊，請參閱 [Pluggable SDK](https://developers.line.biz/en/docs/liff/pluggable-sdk/)。

<!-- tip end -->

## Initializing the LIFF app 

[`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法會初始化 LIFF app，讓你能從 LIFF app 呼叫 LIFF SDK 的其他方法。

LIFF app 必須在每次開啟頁面時初始化。即使是在同一個 LIFF app 內的頁面轉換，當你開啟新頁面時，也應該執行 `liff.init()` 方法。

如果你在未正確初始化 LIFF app 的情況下使用 LIFF 功能，我們不保證這些功能能正常運作。

從使用者在 LINE app 上存取 [LIFF URL](https://developers.line.biz/en/glossary/#liff-url) 到 LIFF app 完成初始化的流程如下：

![Interactive SVG](https://developers.line.biz/media/liff/initializing-liff-app-flow-liff-browser-en.svg)

如需更多資訊，請參閱 [LIFF Behaviors from accessing the LIFF URL to opening the LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

<!-- note start -->

**LIFF app 的查詢參數**

當你存取 LIFF URL 或執行 LIFF-to-LIFF 轉換時，可能會在 URL 加上以下查詢參數：

- `liff.state`：表示在 LIFF URL 中指定的額外資訊。
- `liff.referrer`：表示 LIFF-to-LIFF 轉換之前的 URL。如需更多資訊，請參閱 [Get URL from before LIFF-to-LIFF transition](https://developers.line.biz/en/docs/liff/opening-liff-app/#using-liff-referrer)。
- `lineAppVersion`：當 LIFF app 在 LINE for Android 中開啟時可能會包含此參數。

上述查詢參數是由 LIFF SDK 加上的，目的是讓 LIFF app 能正常運作。當你對 LIFF app 的 URL 執行自訂處理時，在 `liff.init()` 方法 resolve 之前，請勿修改 LIFF SDK 給定的查詢參數，以確保 LIFF app 能正常運作，例如在開啟時或 LIFF-to-LIFF 轉換期間。

此外，也可能會加上其他查詢參數。基於此原因，請將你的 app 設計成：在存取 LIFF URL 或執行 LIFF-to-LIFF 轉換時所加上的查詢參數不會被修改。

<!-- note end -->

<!-- tip start -->

**即使在 LIFF app 初始化之前也能執行的功能**

以下這些屬性或方法即使在 `liff.init()` 方法執行之前也可使用。例如，你可以在初始化 LIFF app 之前取得 LIFF app 執行的環境。

- [liff.ready](https://developers.line.biz/en/reference/liff/#ready)
- [liff.getOS()](https://developers.line.biz/en/reference/liff/#get-os)
- [liff.getAppLanguage()](https://developers.line.biz/en/reference/liff/#get-app-language)
- [liff.getLanguage()](https://developers.line.biz/en/reference/liff/#get-language)（已淘汰）
- [liff.getVersion()](https://developers.line.biz/en/reference/liff/#get-version)
- [liff.getLineVersion()](https://developers.line.biz/en/reference/liff/#get-line-version)
- [liff.isInClient()](https://developers.line.biz/en/reference/liff/#is-in-client)
- [liff.closeWindow()](https://developers.line.biz/en/reference/liff/#close-window)
- [liff.use()](https://developers.line.biz/en/reference/liff/#use)
- [liff.i18n.setLang()](https://developers.line.biz/en/reference/liff/#i18n-set-lang)

若要在 `liff.init()` 完成 LIFF app 初始化之前使用 `liff.closeWindow()` 方法，你的 LIFF SDK 版本必須是 v2.4.0 或更新版本。

<!-- tip end -->

<!-- tip start -->

**在外部瀏覽器中初始化 LIFF app 時，啟用自動執行 liff.login() 方法**

在 `liff.init()` 方法的 `config` 物件的 `withLoginOnExternalBrowser` 屬性中指定 `true`，即可在外部瀏覽器中初始化 LIFF app 時自動執行 `liff.login()` 方法。

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

<!-- tip end -->

`liffId` 需要指定的 LIFF app ID，你可以透過將 LIFF app 加入頻道（channel）來取得。如需更多資訊，請參閱 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/)。

```javascript
liff
  .init({
    liffId: "1234567890-AbcdEfgh", // Use own liffId
  })
  .then(() => {
    // start to use LIFF's api
  })
  .catch((err) => {
    console.log(err);
  });
```

此外，透過 `liff.ready`，你可以取得在啟動 LIFF app 後第一次執行 `liff.init()` 時會 resolve 的 `Promise` 物件。

如需更多資訊，請參閱 LIFF API reference 中的 [liff.init()](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 與 [liff.ready](https://developers.line.biz/en/reference/liff/#ready) 章節。

### Important points to consider when initializing the LIFF app 

以下是初始化 LIFF app 時需要考量的重要事項。在開始開發 LIFF app 之前，請閱讀並理解這些事項。

- [在端點 URL（endpoint URL）或更下層執行 `liff.init()`](https://developers.line.biz/en/docs/liff/developing-liff-apps/#initializing-liff-app-notes-1)
- [在主要重新導向 URL 與次要重新導向 URL 各執行一次 `liff.init()`](https://developers.line.biz/en/docs/liff/developing-liff-apps/#initializing-liff-app-notes-2)
- [在 `liff.init()` 完成後再處理 URL 變更](https://developers.line.biz/en/docs/liff/developing-liff-apps/#initializing-liff-app-notes-3)
- [處理主要重新導向 URL 時請小心](https://developers.line.biz/en/docs/liff/developing-liff-apps/#initializing-liff-app-notes-4)

#### Execute `liff.init()` at the endpoint URL or at a lower level 

`liff.init()` 方法只會在與端點 URL（endpoint URL）完全相同的 URL，或位於端點 URL 更下層的 URL 上運作。如果 LIFF app 轉換到這些之外的 URL，則不保證 `liff.init()` 方法能正常運作。

以下範例顯示當端點 URL 為 `https://example.com/path1/` 時，執行 `liff.init()` 方法的 URL 其行為是否受到保證。某些 LIFF app 功能，例如 [multi-tab view](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)，在行為不受保證的 URL 上可能無法正常運作。

| 執行 `liff.init()` 的 URL          | 保證可運作 |
| ------------------------------------- | ------------------ |
| `https://example.com/`                | ❌                 |
| `https://example.com/path1/`          | ✅                 |
| `https://example.com/path1/language/` | ✅                 |
| `https://example.com/path2/`          | ❌                 |

<!-- note start -->

**執行 liff.init() 方法時，主控台（console）出現警告訊息「liff.init() was called with a current URL that is not related to the endpoint URL.」**

在 LIFF v2.27.2 或更新版本中，當 `liff.init()` 方法在行為不受保證的 URL 上執行時，會出現警告訊息。

例如，如果某個 LIFF app 的端點 URL 為 `https://example.com/path1/path2/`，而執行 `liff.init()` 方法的 URL 為 `https://example.com/path1/`，則會出現以下警告訊息：

```
liff.init() was called with a current URL that is not related to the endpoint URL.
https://example.com/path1/ is not under https://example.com/path1/path2/
```

如果你看到上述警告訊息，請考慮將端點 URL 改為 `https://example.com/` 或 `https://example.com/path1/`。改用這些 URL 可保證 `liff.init()` 方法能正常運作。

<!-- note end -->

#### Execute `liff.init()` once for both the primary redirect URL and once at the secondary redirect URL 

`liff.init()` 方法會根據賦予主要重新導向 URL 的資訊（例如 `liff.state` 與 `access_token=xxx`）來執行初始化處理。如果你的端點 URL 包含查詢參數或路徑，為了正確初始化 LIFF app，請在主要重新導向 URL 與次要重新導向 URL 各執行一次 `liff.init()` 方法。如需更多資訊，請參閱 [Behaviors from accessing the LIFF URL to opening the LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

#### Process URL changes after `liff.init()` completes 

請在 `liff.init()` 方法回傳的 `Promise` 物件 resolve 之後，再執行會變更 URL 的處理。

```javascript
// Example using window.location.replace()
liff
  .init({
    liffId: "1234567890-AbcdEfgh", // Use own liffId
  })
  .then(() => {
    // Redirect to another page after the returned Promise object has been resolved
    window.location.replace(location.href + "/entry/");
  });
```

如果你在 `Promise` 物件 resolve 之前執行以下任一種 URL 操作，LIFF app 可能無法正常開啟：

- 使用 [`Document.location`](https://developer.mozilla.org/en-US/docs/Web/API/Document/location) 屬性或 [`Window.location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location) 屬性變更 URL
- 使用 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 的 [`history.pushState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) 方法或 [`history.replaceState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) 方法變更 URL
- 在伺服器端回傳狀態碼 `301` 或 `302` 並重新導向到另一個 URL

#### Use caution when handling the primary redirect URL 

自動賦予主要重新導向 URL 的 `access_token=xxx` 是使用者的存取權杖（機密資訊）。請勿將主要重新導向 URL 傳送到外部記錄工具（例如 Google Analytics）。

請注意，在 LIFF v2.11.0 或更新版本中，當 `liff.init()` 方法 resolve 時，憑證資訊會從 URL 中排除。因此，你可以如以下範例，在 `then()` 方法中傳送頁面瀏覽量（page view），以防止洩漏憑證資訊。如果你想使用記錄工具，我們建議你將 LIFF app 升級到 v2.11.0 或更新版本。如需更多關於 LIFF v2.11.0 更新內容的資訊，請參閱 [Release Notes](https://developers.line.biz/en/docs/liff/release-notes/#liff-v2-11-0)。

```javascript
liff
  .init({
    liffId: "1234567890-AbcdEfgh", // Use own liffId
  })
  .then(() => {
    ga("send", "pageview");
  });
```

### To use LINE Login in an external browser 

若要在外部瀏覽器中使用 LINE Login，請如下所示呼叫 `liff.init()` 方法兩次。

1. 在載入 LIFF SDK 後呼叫 `liff.init()` 方法。
1. 呼叫 `liff.login()` 方法。當認證頁面與授權畫面的處理完成後，你會被重新導向回 LIFF app（`redirectUri`）。再次呼叫 `liff.init()` 方法。

   如果在 `liff.init()` 方法的處理過程中發生錯誤，或使用者在登入時取消授權，則會執行 `errorCallback`。

![Flow diagram](https://developers.line.biz/media/liff/initializing-liff-app-flow.png)

<!-- note start -->

**LIFF 瀏覽器內的授權請求**

LIFF 瀏覽器內的 LINE Login 授權請求行為不受保證。此外，當從外部瀏覽器或 LINE 的應用程式內瀏覽器開啟 LIFF app 時，請務必使用 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法來進行登入處理，而不是使用 [authorization requests with LINE Login](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)。

<!-- note end -->

## Calling the LIFF API 

在完成 LIFF SDK 整合與 LIFF 初始化之後，你可以執行以下這些操作。

- [取得 LIFF app 執行的環境](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-environment)
- [執行登入處理](https://developers.line.biz/en/docs/liff/developing-liff-apps/#login-with-line-login)
- [開啟 URL](https://developers.line.biz/en/docs/liff/developing-liff-apps/#opening-url)
- [開啟 2D code 讀取器](https://developers.line.biz/en/docs/liff/developing-liff-apps/#opening-two-dimensional-code-reader)
- [取得啟動 LIFF app 的畫面類型](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-context)
- [取得使用者的個人檔案](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-user-profile)
- [取得使用者與 LINE 官方帳號之間的好友關係狀態](https://developers.line.biz/en/docs/liff/developing-liff-apps/#get-friendship-status)
- [取得目前頁面的永久連結](https://developers.line.biz/en/docs/liff/developing-liff-apps/#get-permanent-link)
- [傳送訊息到目前的聊天室](https://developers.line.biz/en/docs/liff/developing-liff-apps/#sending-messages)
- [傳送訊息給使用者的好友（share target picker）](https://developers.line.biz/en/docs/liff/developing-liff-apps/#share-target-picker)
- [關閉 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#closing-liff-app)

### Getting the environment in which the LIFF app is running 

呼叫 `liff.isInClient()` 方法與 `liff.getOS()` 方法，以取得 LIFF app 執行的環境。

```javascript
// print the environment in which the LIFF app is running
console.log(liff.getAppLanguage());
console.log(liff.getVersion());
console.log(liff.isInClient());
console.log(liff.isLoggedIn());
console.log(liff.getOS());
console.log(liff.getLineVersion());
```

如需更多資訊，請參閱 LIFF API reference 中的各個方法。

- [liff.getAppLanguage()](https://developers.line.biz/en/reference/liff/#get-app-language)
- [liff.getVersion()](https://developers.line.biz/en/reference/liff/#get-version)
- [liff.isInClient()](https://developers.line.biz/en/reference/liff/#is-in-client)
- [liff.isLoggedIn()](https://developers.line.biz/en/reference/liff/#is-logged-in)
- [liff.getOS()](https://developers.line.biz/en/reference/liff/#get-os)
- [liff.getLineVersion()](https://developers.line.biz/en/reference/liff/#get-line-version)

### Performing a login process 

呼叫 `liff.login()` 方法，以在 [LINE 的應用程式內瀏覽器](https://developers.line.biz/en/glossary/#line-iab)與[外部瀏覽器](https://developers.line.biz/en/glossary/#external-browser)中執行登入處理。

<!-- note start -->

**注意**

你無法在 LIFF 瀏覽器中使用 `liff.login()`，因為它會在執行 `liff.init()` 時自動執行。

<!-- note end -->

<!-- tip start -->

**如果你在執行 liff.init() 方法時於 withLoginOnExternalBrowser 屬性中指定了 true**

如果你在 `liff.init()` 方法的 `withLoginOnExternalBrowser` 屬性中指定了 `true`，則即使在外部瀏覽器中，當你初始化 LIFF app 時也會自動執行 `liff.login()` 方法。如需更多資訊，請參閱 LIFF API reference 中的 [liff.init()](https://developers.line.biz/en/reference/liff/#initialize-liff-app)。

<!-- tip end -->

```javascript
// login call, only when external browser or LINE's in-app browser is used
if (!liff.isLoggedIn()) {
  liff.login();
}
```

你也可以呼叫 `liff.logout()` 方法來登出。

```javascript
// logout call only when external browse or LINE's in-app browser is used
if (liff.isLoggedIn()) {
  liff.logout();
  window.location.reload();
}
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.login()](https://developers.line.biz/en/reference/liff/#login) 與 [liff.logout()](https://developers.line.biz/en/reference/liff/#logout)。

### Opening a URL 

`liff.openWindow()` 方法會在 LINE 的應用程式內瀏覽器或外部瀏覽器中開啟指定的 URL。

以下程式碼會在外部瀏覽器中開啟 `https://line.me`。

```javascript
// openWindow call
liff.openWindow({
  url: "https://line.me",
  external: true,
});
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.openWindow()](https://developers.line.biz/en/reference/liff/#open-window)。

### Opening the 2D code reader 

呼叫 `liff.scanCodeV2()` 方法以啟動 2D code 讀取器，並取得使用者讀取的字串。

```javascript
// scanCodeV2 call
liff
  .scanCodeV2()
  .then((result) => {
    // e.g. result = { value: 'Hello LIFF app!' }
  })
  .catch((err) => {
    console.log(err);
  });
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.scanCodeV2()](https://developers.line.biz/en/reference/liff/#scan-code-v2)。

<!-- note start -->

**liff.scanCode() 方法已淘汰**

傳統的 `liff.scanCode()` 方法已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)。我們建議使用 `liff.scanCodeV2()` 方法來實作 2D code 讀取器。

<!-- note end -->

<!-- note start -->

**liff.scanCode2() 方法的運作環境**

`liff.scanCodeV2()` 方法可在以下環境中運作：

- iOS：iOS 14.3 或更新版本
- Android：所有版本
- 外部瀏覽器：支援 [WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) 的 web 瀏覽器

<table>
  <thead>
    <tr>
      <th>OS</th>
      <th>Version</th>
      <th>LIFF browser</th>
      <th>External browser</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">iOS</td>
      <td>11-14.2</td>
      <td>❌</td>
      <td>✅ *1</td>
    </tr>
    <tr>
      <td>14.3 or later</td>
      <td>✅ *2</td>
      <td>✅ *1</td>
    </tr>
    <tr>
      <td>Android</td>
      <td>All versions</td>
      <td>✅ *2</td>
      <td>✅ *1</td>
    </tr>
    <tr>
      <td>PC</td>
      <td>All versions</td>
      <td>❌</td>
      <td>✅ *1</td>
    </tr>
  </tbody>
</table>

\*1 你只能使用支援 [WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) 的 web 瀏覽器。

\*2 僅在 LIFF 瀏覽器的螢幕大小為 `Full` 時可用。詳情請參閱 LIFF 文件中的 [Size of the LIFF browser](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

<!-- note end -->

<!-- note start -->

**開啟 [Scan QR] 以啟動 2D code 讀取器**

在 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/) 時，請開啟 **Scan QR**。即使在將 LIFF app 加入頻道後，仍可從 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁更新 **Scan QR** 設定。

<!-- note end -->

### Getting the screen type from which the LIFF app was launched 

執行 `liff.getContext()` 方法，以取得指定啟動 LIFF app 的畫面類型（一對一聊天、群組聊天、多人聊天或外部瀏覽器）的值。

```javascript
const context = liff.getContext();
console.log(context);
// {"type": "utou", "userId": "U70e153189a29f1188b045366285346bc", "viewType": "full", "accessTokenHash": "ArIXhlwQMAZyW7SDHm7L2g", "availability": {"shareTargetPicker": {"permission": true, "minVer": "10.3.0"}, "multipleLiffTransition": {"permission": true, "minVer": "10.18.0"}}}
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.getContext()](https://developers.line.biz/en/reference/liff/#get-context)。

### Get user profile 

在 LIFF app 中透過取得 ID token 來取得使用者個人檔案有兩種方式。請依你的預期用途使用對應的方法。

- [將使用者資料傳送到伺服器](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-tokens)
- [在 LIFF app 中顯示使用者資料](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-decoded-id-token)

<!-- note start -->

**選擇 scope**

在 [adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/) 時，請選擇 `openid` scope。如果你未選擇此 scope，或使用者未授予權限，你將無法取得 ID token。即使在加入 LIFF app 後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- note end -->

<!-- tip start -->

**你可以取得使用者的電子郵件地址**

若要取得使用者的電子郵件地址，請在 [adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/) 時選擇 `email` scope。一旦使用者授予權限，你就能取得電子郵件地址。即使在加入 LIFF app 後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- tip end -->

#### Send user data to the server 

當 LIFF app 將使用者資料傳送到伺服器時，它會傳送透過此方法取得的存取權杖或 ID token。如需更多資訊，請參閱 LIFF 文件中的 [Using user data in LIFF apps and servers](https://developers.line.biz/en/docs/liff/using-user-profile/)。

- 執行 `liff.getAccessToken()` 方法以取得目前使用者的存取權杖。如需更多資訊，請參閱 LIFF API reference 中的 [liff.getAccessToken()](https://developers.line.biz/en/reference/liff/#get-access-token)。

  ```javascript
  // get access token
  if (!liff.isLoggedIn() && !liff.isInClient()) {
    window.alert(
      'To get an access token, you need to be logged in. Tap the "login" button below and try again.',
    );
  } else {
    const accessToken = liff.getAccessToken();
    console.log(accessToken);
  }
  ```

- 執行 `liff.getIDToken()` 方法以取得目前使用者的原始 ID token。如需更多資訊，請參閱 LIFF API reference 中的 [liff.getIDToken()](https://developers.line.biz/en/reference/liff/#get-id-token)。

  ```javascript
  liff.init(() => {
    const idToken = liff.getIDToken();
    console.log(idToken); // print raw idToken object
  });
  ```

#### Display user data to the LIFF app 

執行 `liff.getDecodedIDToken()` 方法，以取得目前使用者的個人檔案資訊與電子郵件地址。

使用此 API，以在 LIFF app 中使用使用者的顯示名稱。

<!-- warning start -->

**請勿將使用者資料傳送到伺服器**

請勿將透過 `liff.getDecodedIDToken()` 取得的使用者資料傳送到伺服器。請改為傳送以 [`liff.getIDToken()`](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-tokens) 取得的 ID token。

<!-- warning end -->

```javascript
liff.init(() => {
  const idToken = liff.getDecodedIDToken();
  console.log(idToken); // print decoded idToken object
});
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.getDecodedIDToken()](https://developers.line.biz/en/reference/liff/#get-decoded-id-token)。

### Getting the friendship status between the user and the LINE Official Account 

取得使用者與 LINE 官方帳號之間的好友關係狀態，該 LINE 官方帳號連結至加入 LIFF app 的 LINE Login 頻道。

進一步瞭解如何在 LINE Login 文件中 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。

```javascript
liff.getFriendship().then((data) => {
  if (data.friendFlag) {
    // something you want to do
  }
});
```

進一步瞭解 LIFF API reference 中的 [liff.getFriendship()](https://developers.line.biz/en/reference/liff/#get-friendship)。

<!-- note start -->

**選擇 scope**

在 [adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/) 時，請選擇 `profile` scope。如果你未選擇此 scope，或使用者未授予權限，你將無法取得好友關係狀態。即使在加入 LIFF app 後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- note end -->

### Requesting the user to add the LINE Official Account as a friend or unblock it 

顯示一個子視窗，提示使用者將 LINE 官方帳號加為好友，或解除封鎖。

![](https://developers.line.biz/media/liff/request-friendship/request-friendship-add-friend-en.png)

- 如果使用者尚未將 LINE 官方帳號加為好友，會顯示一個提示使用者將其加為好友的子視窗。
- 如果使用者已封鎖該 LINE 官方帳號，會顯示一個提示使用者解除封鎖的子視窗。
- 如果使用者已經是該 LINE 官方帳號的好友，子視窗會顯示後自動關閉。

```javascript
try {
  await liff.requestFriendship();
} catch (error) {
  console.log(error);
}
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.requestFriendship()](https://developers.line.biz/en/reference/liff/#request-friendship)。

### Getting the permanent link of any page in the LIFF app 

執行 `liff.permanentLink.createUrlBy()` 方法，以取得 LIFF app 中任意頁面的永久連結。

```javascript
// For example, if the endpoint URL of the LIFF app is https://example.com/path1?q1=v1 and its LIFF ID is 1234567890-AbcdEfgh
liff.permanentLink
  .createUrlBy("https://example.com/path1?q1=v1")
  .then((permanentLink) => {
    // https://liff.line.me/1234567890-AbcdEfgh
    console.log(permanentLink);
  });

liff.permanentLink
  .createUrlBy("https://example.com/path1/path2?q1=v1&q2=v2")
  .then((permanentLink) => {
    // https://liff.line.me/1234567890-AbcdEfgh/path2?q=2=v2
    console.log(permanentLink);
  });
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.permanentLink.createUrlBy()](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by)。

### Sending messages to the current chat room 

`liff.sendMessages()` 方法會代表使用者，將訊息傳送到開啟 LIFF app 的聊天室。你可以在單一請求中傳送最多 5 個訊息物件。

以下程式碼會將「Hello, World!」作為使用者的訊息傳送到顯示 LIFF app 的聊天室。

```javascript
liff
  .sendMessages([
    {
      type: "text",
      text: "Hello, World!",
    },
  ])
  .then(() => {
    console.log("message sent");
  })
  .catch((err) => {
    console.log("error", err);
  });
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.sendMessages()](https://developers.line.biz/en/reference/liff/#send-messages)。

### Sending messages to a user's friend (share target picker) 

執行 `liff.shareTargetPicker()` 方法以顯示 target picker（選擇群組或好友的畫面），並將開發者建立的訊息傳送給選定的對象。這則訊息對你的群組或好友來說，看起來就像是你親自傳送的一樣。

在 target picker 中，只能選擇使用者參與的好友（包含 LINE 官方帳號）與群組。不包含 OpenChat。

![target picker](https://developers.line.biz/media/liff/share-target-picker_tobe_en.png)

#### Using the share target picker 

若要使用 share target picker，開發者需要依照以下說明同意「Agreement Regarding Use of Information」。每個頻道都需要進行此同意。

1. 在 [LINE Developers Console](https://developers.line.biz/console/) 中，選擇要加入 LIFF app 的 LINE Login 頻道。
1. 在 **LIFF** 分頁上點擊 **shareTargetPicker**，便會顯示「Agreement Regarding Use of Information」。
1. 仔細閱讀顯示的內容，並勾選 **I have read and agree to the Agreement Regarding Use of Information**，然後點擊 **Enable**。

#### Sample code of the share target picker 

以下程式碼會顯示 target picker，並將「Hello, World!」作為使用者的訊息傳送給選定的群組或好友。如果你想確認 target picker 在啟動 LIFF app 的環境中是否可用，請先執行 `liff.isApiAvailable()`。

```javascript
if (liff.isApiAvailable("shareTargetPicker")) {
  liff.shareTargetPicker([
    {
      type: "text",
      text: "Hello, World!",
    },
  ]);
}
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.isApiAvailable()](https://developers.line.biz/en/reference/liff/#is-api-available) 與 [liff.shareTargetPicker()](https://developers.line.biz/en/reference/liff/#share-target-picker)。

### Closing the LIFF app 

`liff.closeWindow()` 方法會關閉開啟的 LIFF app。

```javascript
// closeWindow call
if (!liff.isInClient()) {
  window.alert(
    "This button is unavailable as LIFF is currently being opened in an external browser.",
  );
} else {
  liff.closeWindow();
}
```

如需更多資訊，請參閱 LIFF API reference 中的 [liff.closeWindow()](https://developers.line.biz/en/reference/liff/#close-window)。

<!-- note start -->

**注意**

`liff.closeWindow()` 在外部瀏覽器中不保證能正常運作。

<!-- note end -->

## Setting the OGP tags 

透過為 LIFF app 的每個頁面設定 OGP tag，舉例來說，當你在 LINE 聊天室等處分享 LIFF app 的 URL（`https://liff.line.me/{liffId}`）時，便可顯示任意的標題、描述或縮圖。

以下是 LIFF 支援的 OGP tag。如需更多關於 OGP tag 的資訊，請參閱 [The Open Graph protocol](https://ogp.me/)。

```html
<html lang="ja" prefix="og: http://ogp.me/ns#">
<meta property="og:title" content="The title">
<meta property="og:type" content="`website`, `blog`, or `article`">
<meta property="og:description" content="A one to two sentence description">
<meta property="og:url" content="The URL">
<meta property="og:site_name" content="The name that represents the overall site">
<meta property="og:image" content="An image URL">
```

<!-- note start -->

**注意**

當以 `line://app/{liffId}`（已淘汰）格式分享 LIFF app 的 URL 時，OGP tag 會被忽略。

<!-- note end -->

## When opening an external site that isn't a LIFF app 

當從在 LIFF 瀏覽器中開啟的 LIFF app 開啟一個非 LIFF app 的外部網站時，會出現一個彈出視窗，表示「This is an external page」。

![A popup when moving to the external site](https://developers.line.biz/media/news/2022/liff-opening-external-site-en.jpg)

只有在同一個視窗中開啟外部網站時才會出現此彈出視窗。如果在不同的視窗中開啟外部網站，則不會出現彈出視窗。

<!-- note start -->

**轉換到比 LIFF 端點 URL 更上層的位置**

當在 LIFF app 中轉換到比端點 URL（例如 `https://example.com/path`）本身更上層的位置（例如 `https://example.com/`）時，其行為不受保證。

<!-- note end -->

## Behavior when closing the LIFF app 

當在 LIFF 瀏覽器中開啟的 LIFF app 被使用者關閉，或透過 [`liff.closeWindow()`](https://developers.line.biz/en/reference/liff/#close-window) 方法關閉時，其行為會依 LINE app 版本與 LIFF app 設定而有所不同。

### If the LINE app version is 15.12.0 or later 

如果 LINE app 版本為 15.12.0 或更新版本，關閉 LIFF app 時的行為會依該 LIFF app 是否符合 multi-tab view 中[出現在「最近使用的服務」區段的條件](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view-condition)而改變。

| | |
| --- | --- |
| 符合條件時 | 使用者即使關閉了 LIFF app，仍可在 12 小時內重新啟動它。存取權杖、瀏覽記錄與畫面捲動位置都會被保留。 |
| 不符合條件時 | 當使用者關閉 LIFF app 時，LIFF app 會結束。因此，當 LIFF app 被關閉時，存取權杖會過期。 |

如需更多資訊，請參閱 [Recently used services](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view-recent-service)。

### If the LINE app version is earlier than 15.12.0 

如果 LINE app 版本早於 15.12.0，當使用者關閉 LIFF app 時，LIFF app 會結束。因此，當 LIFF app 被關閉時，存取權杖會過期。

## Next steps 

在開發完 LIFF app 後，將它部署到任何伺服器上。部署完成後，請執行以下這些操作：

1. [將 LIFF app 加入你的頻道。](https://developers.line.biz/en/docs/liff/registering-liff-apps/)
1. [開啟 LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)
