# 將營運中的網頁應用程式實作為 LINE MINI App（Implementing web apps in operation as LINE MINI Apps）

如果你想將自己的網頁應用程式（web app）實作為 LINE MINI App，可能會不知道該如何著手。本頁提供 LINE MINI App 的概觀，以及將網頁應用程式實作為 LINE MINI App 所需的知識與步驟。閱讀本頁後，你將能掌握把網頁應用程式實作為 LINE MINI App 的整體樣貌。

<!-- table of contents -->

## What is LINE MINI App 

首先，LINE MINI App 是一種可在 LINE App 中使用的網頁應用程式，並使用 [LIFF（LINE Front-end Framework）](https://developers.line.biz/en/docs/liff/overview/) 來實作。透過 LIFF 的各項功能，你的應用程式可以為 LINE 使用者提供流暢的登入體驗，並取得使用者個人檔案（profile）。

此外，[service messages](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/) 功能讓 LINE MINI App 能夠針對使用者在 LINE MINI App 上的操作，向使用者發送通知。幾乎所有的 HTML5 規格也都受到支援，例如可使用 [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) 來取得使用者的位置資訊。

![](https://developers.line.biz/media/line-mini-app/develop/product-image.png)

如上所述，藉由將網頁應用程式實作為 LINE MINI App，你可以避免使用者因為不便的登入、個人檔案輸入等流程而離開應用程式。此外，LINE MINI App 也可以直接從 LINE App 立即開始使用，且所有操作都能在 LINE App 中完成，因此能提升使用者體驗。

<!-- tip start -->

**LINE MINI App 與原生應用程式（native app）的比較**

關於 LINE MINI App 相較於原生應用程式的優勢，詳情請參閱 [The differences between native apps and LINE MINI Apps](https://developers.line.biz/en/docs/line-mini-app/discover/native-mini/)。

<!-- tip end -->

## Requirements 

將營運中的網頁應用程式實作為 LINE MINI App 需要哪些條件呢？首先，我們將說明把網頁應用程式實作為 LINE MINI App 的需求。

要將網頁應用程式實作為 LINE MINI App，需要具備以下條件：

- 開發與發布網頁應用程式的知識與技術
- 一組 Business ID

LINE MINI App 是在 LINE App 上執行的網頁應用程式。因此，開發營運中網頁應用程式時所使用的知識與技術都可以直接沿用。例如，HTML、CSS 與 JavaScript 的知識，以及文字編輯器等開發環境都會派上用場。你同樣會持續需要一台用來發布網頁應用程式的網頁伺服器。

此外，開發 LINE MINI App 時會使用 [LINE Developers Console](https://developers.line.biz/console/)。因此，你會需要 LINE Developers Console 所需的 Business ID。關於 Business ID 的詳情，請參閱 LINE Developers Console 文件中的 [Log in to the LINE Developers Console](https://developers.line.biz/en/docs/line-developers-console/login-account/)。

## Procedure for implementing a web app as a LINE MINI App 

接下來，我們將說明把網頁應用程式實作為 LINE MINI App 的具體步驟。這裡會以一個處理使用者資訊、且營運中的網頁應用程式與 LINE 帳號連動的範例來說明。

1. 建立 LINE MINI App channel
1. 在網頁應用程式端載入 LIFF SDK
1. 初始化 LIFF app
1. 實作所需的功能
1. 設定 LINE MINI App channel
1. 申請 LINE MINI App 的審查

以下將逐一說明各個步驟。

### 1. Create a LINE MINI App channel 

要將你的 LINE MINI App 發布給使用者，你會需要一個稱為 LINE MINI App channel 的[頻道（channel）](https://developers.line.biz/en/glossary/#channel)。首先，請登入 [LINE Developers Console](https://developers.line.biz/console/) 並建立 LINE MINI App channel。關於如何建立 LINE MINI App channel 的詳情，請參閱 [LINE Developers Console Guide for LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/)。

### 2. Load the LIFF SDK on the web app side 

LINE MINI App 是以使用 [LIFF（LINE Front-end Framework）](https://developers.line.biz/en/docs/liff/overview/) 的 LIFF app 形式執行。因此，首先必須在網頁應用程式端載入 LIFF SDK。

載入 LIFF SDK 有兩種方式：從 CDN 載入，或使用 npm 套件。例如，要從 CDN 載入 LIFF SDK，請撰寫以下程式碼：

```html
<script charset="utf-8" src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>
```

關於載入 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

### 3. Initialize the LIFF app 

要使用 LIFF SDK，你需要執行 `liff.init()` 方法來初始化你的 LIFF app。此時，請指定 LIFF ID，該 ID 可在步驟 1 所建立的 LINE MINI App channel 中找到。關於如何確認 LIFF ID 的詳情，請參閱 [Confirm LIFF ID and set endpoint URL](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#confirm-liff-id-and-set-endpoint-url)。

要使用 `liff.init()` 初始化 LIFF app，請實作以下程式碼：

```javascript
liff
  .init({
    liffId: "123456-abcdefg", // Specify LIFF ID
  })
  .then(() => {
    // Use the LIFF API
  })
  .catch((err) => {
    // When an error occurs during initialization
    console.log(err.code, err.message);
  });
```

### 4. Implement the necessary features 

到了這個階段，你已經準備好可以實作功能了。下一步就是實作所需的功能。在 LINE MINI App 中可以使用以下功能與規格：

- LIFF API
- Service messages
- HTML5 規格

以下將逐一說明。

#### LIFF API 

初始化 LIFF app 之後，你就可以使用 LIFF API 來實作所需的功能。LIFF API 讓你能處理使用者登入並取得使用者個人檔案。例如，若要取得使用者 ID，首先使用 `liff.getIDToken()` 取得 ID 權杖（ID token）。

```javascript
const idToken = liff.getIDToken();
```

這個 `idToken` 會被傳送到伺服器端，並可透過 [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token) 端點（endpoint）進行驗證以取得使用者 ID。例如，將取得的使用者 ID 與營運中網頁應用程式的會員資訊連動，便可發送為該使用者最佳化的訊息。

關於 LIFF API 的詳情，請參閱 LIFF 文件中的 [Calling the LIFF API](https://developers.line.biz/en/docs/liff/developing-liff-apps/#calling-liff-api)。

#### Service messages 

LINE MINI App 具備一項稱為 service messages 的功能。Service messages 讓 LINE MINI App 能夠針對使用者在 LINE MINI App 上的操作，向使用者發送通知。關於 service messages 的詳情，請參閱 [Sending service messages](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)。

#### HTML5 specifications 

LINE MINI App 支援幾乎所有的 HTML5 規格。例如，可使用 [Geolocation API](https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API) 來取得使用者的位置資訊。詳情請參閱 [LINE MINI App specifications](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)。

### 5. Configure the LINE MINI App channel 

當你的網頁應用程式已能作為 LIFF app 運作後，下一步就是讓它能夠作為 LINE MINI App 運作。為此，你需要在步驟 1 所建立的 LINE MINI App channel 中，將網頁應用程式的 URL（例如 `https://example.com`）設定為 endpoint URL。關於設定 endpoint URL 的詳情，請參閱 [Confirm LIFF ID and set endpoint URL](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#confirm-liff-id-and-set-endpoint-url)。

### 6. Request a review of your LINE MINI App 

完成上述步驟後，請將已發布頻道的 LIFF URL 分享給使用者，讓他們開始使用你的 LINE MINI App。你可以將 LINE MINI App 發布為[未驗證的 MINI App（unverified MINI App）](https://developers.line.biz/en/glossary/#unverified-mini-app)，或[已驗證的 MINI App（verified MINI App）](https://developers.line.biz/en/glossary/#verified-mini-app)。

若要將你的 LINE MINI App 發布為已驗證的 MINI App，它必須通過 LY Corporation 的審查。關於審查流程的詳情，請參閱 [Submitting LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)。

## Next step 

開發 LINE MINI App 時，請參閱 [LINE MINI App development guidelines](https://developers.line.biz/en/docs/line-mini-app/development-guidelines/)。這些指南包含向 LINE Platform 發送請求時應注意的要點，以及關於儲存日誌（log）的內容。

此外，[Custom Features](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/) 這個章節說明了可進一步提升使用者體驗的功能。例如，有一項功能可在使用者裝置的主畫面上新增 LINE MINI App 的捷徑。
