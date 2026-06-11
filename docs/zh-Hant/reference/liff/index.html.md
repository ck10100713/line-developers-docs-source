# LIFF API 參考（LIFF API reference）

## Common specifications 

### Operating environment 

如需 LIFF 支援的作業環境（operating environment）詳細資訊，請參閱 LIFF 文件中的 [LIFF overview](https://developers.line.biz/en/docs/liff/overview/)。

您可以使用哪些功能，取決於 LIFF app 是在 LIFF 瀏覽器（LIFF browser）還是外部瀏覽器（external browser）中開啟。例如，您無法在外部瀏覽器中使用 `liff.scanCode()`。詳細資訊請參閱各個用戶端 API（client API）的說明。

<!-- note start -->

**LIFF app 不相容於 OpenChat**

例如，在大多數情況下，無法透過 LIFF app 取得使用者的個人檔案資訊（profile information）。

<!-- note end -->

### LIFF SDK errors 

LIFF SDK 錯誤會以 LiffError 物件回傳。

<!-- note start -->

**辨識錯誤時，請同時參考錯誤碼與錯誤訊息**

由於錯誤訊息可能在不另行通知的情況下變更，僅依據錯誤訊息的完全相符來辨識錯誤，可能導致您的 LIFF app 故障。為確保您的 LIFF app 即使在錯誤訊息變更後仍能正常運作，請同時參考錯誤碼與錯誤訊息來辨識錯誤。

我們計畫進行改善，讓錯誤能僅透過錯誤碼即可唯一辨識。

<!-- note end -->

_Example_

<!-- tab start `json` -->

```json
{
  "code": "INIT_FAILED",
  "message": "Failed to init LIFF SDK"
}
```

<!-- tab end -->

#### LiffError object 

<!-- parameter start -->

code

String

錯誤碼

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

message

String

錯誤訊息

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

cause

Unknown

錯誤原因

<!-- parameter end -->

#### Error details 

| Error code | Description |
| --- | --- |
| 400 | 請求有問題。請檢查請求參數與 JSON 格式。 |
| 401 | 請檢查授權標頭（authorization header）是否正確。 |
| 403 | 未獲授權使用此 API。請確認您的帳號或方案有權使用此 API。 |
| 429 | 請確認您未超過請求的速率限制（rate limit）。 |
| 500 | API 伺服器發生暫時性錯誤。 |
| INIT_FAILED | 初始化 LIFF SDK 失敗。 |
| INVALID_ARGUMENT | 指定了無效的引數。 |
| UNAUTHORIZED | <ul><li>使用者未授權。</li><li>在沒有存取權杖的情況下呼叫 server api。</li><li>在登入前呼叫 share target picker。</li></ul> |
| FORBIDDEN | <ul><li>您沒有所需的權限。</li><li>您嘗試在不支援的環境中使用某項功能。</li></ul> |
| INVALID_CONFIG | 設定無效。<ul><li>請指定 liffId 以使用 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 初始化 LIFF app。</li><li>執行 [`liff.permanentLink.createUrl()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url) 方法的頁面 URL，並非以 **Endpoint URL** 中指定的 URL 開頭。</li></ul> |
| INVALID_ID_TOKEN | 驗證 ID 權杖（ID token）失敗。 |
| EXCEPTION_IN_SUBWINDOW | 子視窗（subwindow）發生問題。<ul><li>例如，target picker（群組或好友選擇畫面）顯示後閒置超過 10 分鐘等情況。</li></ul> |
| UNKNOWN | 未知的錯誤。 |

## LIFF SDK properties 

### liff.id 

此屬性持有傳遞給 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 的 LIFF app ID（`String` 型別）。

在您執行 `liff.init()` 之前，`liff.id` 的值為 `null`。

_Example_

<!-- tab start `javascript` -->

```javascript
const liffId = "my-liff-id";
liff.init({ liffId });

// liff.id equals to liffId
```

<!-- tab end -->

### liff.ready 

此屬性持有一個 `Promise` 物件，當您在啟動 LIFF app 後首次執行 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 時，此 `Promise` 物件會 resolve。

如果您使用 `liff.ready`，便可在 `liff.init()` 完成後執行任何處理。

<!-- tip start -->

**此屬性可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用 `liff.ready`。

<!-- tip end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff.ready.then(() => {
  // do something you want when liff.init finishes
});
```

<!-- tab end -->

<!-- note start -->

**Note**

如果 `liff.init()` 失敗，`liff.ready` 不會被 reject。此外，它也不會回傳 `LiffError` 物件。

<!-- note end -->

## Initialization 

### liff.init() 

初始化 LIFF app。

只有在執行 `liff.init()` 方法之後，您才能呼叫其他 LIFF SDK 方法。LIFF app 在每次開啟頁面時都必須初始化。即使是在同一個 LIFF app 內的轉換，當您開啟新頁面時，也應執行 `liff.init()` 方法。

如果您在未正確初始化 LIFF app 的情況下使用 LIFF 功能，我們不保證這些功能能正常運作。

當您執行 `liff.init()` 方法時，LIFF SDK 會從 LINE Platform 取得使用者的存取權杖（access token）與 ID 權杖（ID token）。

- 若要使用 LIFF SDK 取得的存取權杖，請呼叫 [liff.getAccessToken()](https://developers.line.biz/en/reference/liff/#get-access-token)。
- 若要使用 LIFF SDK 取得的 ID 權杖 payload，請呼叫 [liff.getDecodedIDToken()](https://developers.line.biz/en/reference/liff/#get-decoded-id-token)。

_Example_

<!-- tab start `javascript` -->

```javascript
// Using a Promise object
liff
  .init({
    liffId: "123456-abcedfg", // Use own liffId
  })
  .then(() => {
    // Start to use liff's api
  })
  .catch((err) => {
    // Error happens during initialization
    console.log(err.code, err.message);
  });

// Using a callback
liff.init({ liffId: "123456-abcedfg" }, successCallback, errorCallback);
```

<!-- tab end -->

#### Important points to consider when initializing the LIFF app 

以下是初始化 LIFF app 時需要考量的重要事項。請在開始開發 LIFF app 之前閱讀並理解這些事項。

- [在端點 URL（endpoint URL）或其下層執行 `liff.init()`](https://developers.line.biz/en/reference/liff/#initializing-liff-app-notes-1)
- [針對主要重新導向 URL（primary redirect URL）執行一次 `liff.init()`，並針對次要重新導向 URL（secondary redirect URL）執行一次 `liff.init()`](https://developers.line.biz/en/reference/liff/#initializing-liff-app-notes-2)
- [在 `liff.init()` 完成後再處理 URL 變更](https://developers.line.biz/en/reference/liff/#initializing-liff-app-notes-3)
- [處理主要重新導向 URL 時請小心](https://developers.line.biz/en/reference/liff/#initializing-liff-app-notes-4)

##### Execute `liff.init()` at the endpoint URL or at a lower level 

`liff.init()` 方法只會在與端點 URL 完全相同的 URL，或位於端點 URL 下層的 URL 上運作。如果 LIFF app 轉換到上述以外的 URL，則不保證 `liff.init()` 方法能正常運作。

以下範例顯示，當端點 URL 為 `https://example.com/path1/` 時，執行 `liff.init()` 方法的 URL 是否保證能正常運作。某些 LIFF app 功能，例如[多分頁檢視（multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)，在不保證運作的 URL 上可能無法正常運作。

| URL to execute `liff.init()`          | Guaranteed to work |
| ------------------------------------- | ------------------ |
| `https://example.com/`                | ❌                 |
| `https://example.com/path1/`          | ✅                 |
| `https://example.com/path1/language/` | ✅                 |
| `https://example.com/path2/`          | ❌                 |

<!-- note start -->

**執行 liff.init() 方法時，主控台中出現警告訊息「liff.init() was called with a current URL that is not related to the endpoint URL.」**

在 LIFF v2.27.2 或更新版本中，當 `liff.init()` 方法在不保證運作的 URL 上執行時，會出現警告訊息。

例如，如果 LIFF app 的端點 URL 為 `https://example.com/path1/path2/`，而執行 `liff.init()` 方法的 URL 為 `https://example.com/path1/`，則會出現以下警告訊息：

```
liff.init() was called with a current URL that is not related to the endpoint URL.
https://example.com/path1/ is not under https://example.com/path1/path2/
```

如果您看到上述警告訊息，請考慮將端點 URL 變更為 `https://example.com/` 或 `https://example.com/path1/`。變更為這些 URL 可保證 `liff.init()` 方法正常運作。

<!-- note end -->

##### Execute `liff.init()` once for the primary redirect URL and once for the secondary redirect URL 

`liff.init()` 方法會根據賦予主要重新導向 URL 的資訊（例如 `liff.state` 和 `access_token=xxx`）執行初始化處理。如果您的端點 URL 包含查詢參數（query parameter）或路徑（path），為了正確初始化 LIFF app，請針對主要重新導向 URL 與次要重新導向 URL 各執行一次 `liff.init()` 方法。詳細資訊請參閱 LIFF 文件中的 [Behaviors from accessing the LIFF URL to opening the LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

##### Process URL changes after `liff.init()` completes 

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

如果您在 `Promise` 物件 resolve 之前執行以下任何 URL 操作，LIFF app 可能無法正常開啟：

- 使用 [`Document.location`](https://developer.mozilla.org/en-US/docs/Web/API/Document/location) 屬性或 [`Window.location`](https://developer.mozilla.org/en-US/docs/Web/API/Window/location) 屬性變更 URL
- 使用 [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) 的 [`history.pushState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState) 方法或 [`history.replaceState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState) 方法變更 URL
- 在伺服器端回傳狀態碼 `301` 或 `302` 並重新導向至其他 URL

##### Use caution when handling the primary redirect URL 

自動賦予主要重新導向 URL 的 `access_token=xxx` 是使用者的存取權杖（機密資訊）。請勿將主要重新導向 URL 傳送給外部記錄工具，例如 Google Analytics。

請注意，在 LIFF v2.11.0 或更新版本中，當 `liff.init()` 方法 resolve 時，憑證資訊（credential information）會從 URL 中排除。因此，您可以如下所示，在 `then()` 方法中傳送頁面瀏覽（page view），以防止憑證資訊外洩。如果您想使用記錄工具，我們建議您將 LIFF app 升級至 v2.11.0 或更新版本。如需 LIFF v2.11.0 的更新詳細資訊，請參閱 LIFF 文件中的 [Release Notes](https://developers.line.biz/en/docs/liff/release-notes/#liff-v2-11-0)。

```javascript
liff
  .init({
    liffId: "1234567890-AbcdEfgh", // Use own liffId
  })
  .then(() => {
    ga("send", "pageview");
  });
```

<!-- note start -->

**LIFF app 的查詢參數**

當您存取 LIFF URL 或執行 LIFF-to-LIFF 轉換時，以下查詢參數可能會被加入 URL：

- `liff.state`：表示 LIFF URL 中指定的額外資訊。
- `liff.referrer`：表示 LIFF-to-LIFF 轉換之前的 URL。詳細資訊請參閱 LIFF 文件中的 [Get URL from before LIFF-to-LIFF transition](https://developers.line.biz/en/docs/liff/opening-liff-app/#using-liff-referrer)。
- `lineAppVersion`：當 LIFF app 在 LINE for Android 中開啟時可能會包含此參數。

上述查詢參數是由 LIFF SDK 加入的，以便 LIFF app 能正常運作。當您對 LIFF app 的 URL 執行自訂處理時，在 `liff.init()` 方法 resolve 之前，請勿修改 LIFF SDK 賦予的查詢參數，以確保 LIFF app 能正常運作，例如在開啟或 LIFF-to-LIFF 轉換期間。

也可能會加入其他查詢參數。因此，請將您的 app 設計成在存取 LIFF URL 或執行 LIFF-to-LIFF 轉換時所加入的查詢參數不會被修改。

<!-- note end -->

<!-- tip start -->

**即使在 LIFF app 初始化之前也能執行的功能**

以下這些屬性或方法，即使在執行 `liff.init()` 方法之前也可使用。您可以在初始化 LIFF app 之前取得 LIFF app 執行的環境，或在 LIFF app 初始化失敗時關閉 LIFF app。

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

若要在透過 `liff.init()` 初始化 LIFF app 完成之前使用 `liff.closeWindow()` 方法，您的 LIFF SDK 版本必須為 v2.4.0 或更新版本。

<!-- tip end -->

#### Syntax 

```javascript
liff.init(config, successCallback, errorCallback);
```

#### Arguments 

<!-- parameter start (props: required) -->

config

Object

LIFF app 設定

<!-- parameter end -->
<!-- parameter start (props: required) -->

config.liffId

String

LIFF app ID。可在您將 LIFF app 加入頻道（channel）時取得。詳細資訊請參閱 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/)。\
此處指定的 LIFF app ID 可透過 [`liff.id`](https://developers.line.biz/en/reference/liff/#id) 取得。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

config.withLoginOnExternalBrowser

Boolean

使用以下其中一個值，指定在外部瀏覽器中初始化 LIFF app 時，是否自動執行 `liff.login()` 方法。預設值為 `false`。

- `true`：在外部瀏覽器中自動執行 `liff.login()` 方法。
- `false`：不在外部瀏覽器中自動執行 `liff.login()` 方法。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

successCallback

Function

LIFF app 初始化成功時回傳資料物件的回呼（callback）。

<!-- note start -->

**Note**

successCallback 會在回傳值的 `Promise` 物件 resolve 的同時處理。然而，兩者並無固定的處理先後順序。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

errorCallback

Function

LIFF app 初始化失敗時回傳錯誤物件的回呼。

<!-- note start -->

**Note**

errorCallback 會在回傳值的 `Promise` 物件 reject 的同時處理。然而，兩者並無固定的處理先後順序。

<!-- note end -->

<!-- parameter end -->

#### Return value 

回傳一個 `Promise` 物件。

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

## Getting environment 

### liff.getOS() 

取得使用者執行 LIFF app 的環境。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用此方法。

<!-- tip end -->

#### Syntax 

```javascript
liff.getOS();
```

#### Arguments 

None

#### Return value 

使用者執行 LIFF app 的環境會以字串回傳。由於回傳值是依據 user agent 字串中的 OS 名稱，因此回傳值與瀏覽器類型（[LIFF browser](https://developers.line.biz/en/glossary/#liff-browser)、[LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab)、[external browser](https://developers.line.biz/en/glossary/#external-browser)）無關。

例如，如果使用者使用 iOS，無論使用者使用的是 LIFF 瀏覽器還是 Safari，都會回傳 `ios`。

| Return value | Description          |
| ------------ | -------------------- |
| ios          | iOS 或 iPadOS        |
| android      | Android              |
| web          | 上述以外             |

如需 LIFF app 支援的作業系統與瀏覽器詳細資訊，請參閱 [Operating environment](https://developers.line.biz/en/docs/liff/overview/#operating-environment)。

### liff.getAppLanguage() 

取得執行 LIFF app 的 LINE app 的語言設定。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用此方法。

<!-- tip end -->

#### Conditions of use 

LIFF SDK 版本 v2.24.0 或更新版本

#### Operating conditions 

必須滿足以下所有條件，`liff.getAppLanguage()` 方法才能正常運作：

- LIFF app 在 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中執行。
- LINE app 版本為 14.11.0 或更新版本。

如果未滿足上述條件，`liff.getAppLanguage()` 方法的行為將與 [`liff.getLanguage()`](https://developers.line.biz/en/reference/liff/#get-language) 方法相同。

#### Syntax 

```javascript
liff.getAppLanguage();
```

#### Arguments 

None

#### Return value 

執行 LIFF app 的 LINE app 的語言設定，會以遵循 [RFC 5646](https://datatracker.ietf.org/doc/html/rfc5646) 的字串回傳。

### liff.getLanguage() 

<!-- note start -->

**liff.getLanguage() 方法已淘汰**

`liff.getLanguage()` 方法已淘汰。若要取得 LIFF app 執行環境的語言設定，請使用 [`liff.getAppLanguage()`](https://developers.line.biz/en/reference/liff/#get-app-language) 方法。詳細資訊請參閱 [July 23, 2024](https://developers.line.biz/en/news/2024/07/23/release-liff-2-24-0/) 的消息。

<!-- note end -->

取得 LIFF app 執行環境的語言設定。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用此方法。

<!-- tip end -->

#### Syntax 

```javascript
liff.getLanguage();
```

#### Arguments 

None

#### Return value 

包含 LIFF app 執行環境中 `navigator.language` 所指定語言設定的字串。

### liff.getVersion() 

取得 LIFF SDK 的版本。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用此方法。

<!-- tip end -->

#### Syntax 

```javascript
liff.getVersion();
```

#### Arguments 

None

#### Return value 

LIFF SDK 的版本會以字串回傳。

### liff.getLineVersion() 

取得使用者的 LINE 版本。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用此方法。

<!-- tip end -->

#### Syntax 

```javascript
liff.getLineVersion();
```

#### Arguments 

None

#### Return value 

如果使用者使用 LIFF 瀏覽器開啟 LIFF app，則會以字串回傳使用者的 LINE 版本。如果使用者使用外部瀏覽器開啟 LIFF app，則會回傳 `null`。

### liff.getContext() 

取得啟動 LIFF app 的畫面類型（一對一聊天、群組聊天、多人聊天，或外部瀏覽器）。

<!-- warning start -->

**我們已停止向 LIFF app 提供聊天室的公司內部識別碼**

我們已停止向 LIFF app 提供聊天室的公司內部識別碼（一對一聊天 ID、群組 ID 與聊天室 ID）。詳細資訊請參閱 2023 年 2 月 6 日的消息 [We've discontinued providing company internal identifiers of chat rooms to LIFF apps as of February 6, 2023](https://developers.line.biz/en/news/2023/02/06/liff-spec-change/)。

<!-- warning end -->

_Example_

<!-- tab start `javascript` -->

```javascript
const context = liff.getContext();
console.log(context);
```

<!-- tab end -->

#### Syntax 

```javascript
liff.getContext();
```

#### Arguments 

None

#### Return value 

一個資料物件，包含進行各種 API 呼叫所需的資訊。

<!-- parameter start -->

type

String

啟動 LIFF app 的畫面類型。為以下其中之一：

- `utou`：一對一聊天。
- `group`：群組聊天。
- `room`：多人聊天。
- `external`：外部瀏覽器。
- `none`：一對一聊天、群組聊天、多人聊天或外部瀏覽器以外的畫面。例如，錢包分頁（Wallet tab）。

在 LIFF app 之間轉換後，LIFF app 也會回傳此屬性。

<!-- parameter end -->
<!-- parameter start -->

userId

String

使用者 ID。當 `type` 屬性為 `utou`、`room`、`group`、`none` 或 `external` 時包含此屬性。然而，當 `type` 為 `external` 時可能會回傳 null。

<!-- parameter end -->
<!-- parameter start -->

liffId

String

LIFF ID。

<!-- parameter end -->
<!-- parameter start -->

viewType

String

LIFF app 檢視畫面的大小，只有在 `type` 屬性不是 `external` 時才會回傳。為以下其中之一：

- `compact`
- `tall`
- `full`

詳細資訊請參閱 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/)。

<!-- parameter end -->
<!-- parameter start -->

endpointUrl

String

服務端點的 URL。

<!-- parameter end -->
<!-- parameter start -->

accessTokenHash

String

存取權杖經過 SHA256 雜湊後的值的前半部。用於驗證存取權杖。

<!-- parameter end -->
<!-- parameter start -->

availability

Object

回傳 [`availability` 物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability)，表示 LIFF 功能在啟動 LIFF app 的環境中是否可用。

<!-- parameter end -->
<!-- parameter start -->

scope

Array of strings

回傳 LIFF app 在使用部分 LIFF SDK 方法所需的 scope 中，擁有哪些 scope：

- `openid`：使用 [`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token) 與 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 所需的 scope
- `email`：使用 [`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token) 或 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 取得使用者電子郵件位址所需的 scope
- `profile`：使用 [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 或 [`liff.getFriendship()`](https://developers.line.biz/en/reference/liff/#get-friendship) 所需的 scope
- `chat_message.write`：使用 [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 所需的 scope

如需 scope 的詳細資訊，請參閱 LIFF 文件中的 [Adding the LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

<!-- tip start -->

**liff.getContext() 與 liff.permission.getGrantedAll() 的差異**

`liff.getContext()` 方法會取得 LIFF app 的 scope 清單（\*）。

另一方面，[`liff.permission.getGrantedAll()`](https://developers.line.biz/en/reference/liff/#permission-get-granted-all) 方法則會取得 LIFF app 的 scope 中，使用者已同意授權的 scope 清單。

\* 在 LINE Login 頻道的 **LIFF** 分頁下「Scope」區段中指定的 scope

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start -->

menuColorSetting

Object

回傳 LIFF 瀏覽器標頭的顏色設定，以 [`menuColorSetting` 物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-menucolorsetting)表示。

請注意，我們目前不提供變更標頭顏色設定的功能。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

miniAppId

String

回傳由 LINE MINI App 的 Custom Path 功能設定的字串。如需 Custom Path 功能的詳細資訊，請參閱 LINE MINI App 文件中的 [Configuring Custom Path](https://developers.line.biz/en/docs/line-mini-app/develop/custom-path/)。

<!-- parameter end -->
<!-- parameter start -->

miniDomainAllowed

Boolean

回傳 LINE MINI App 是否在 `miniapp.line.me` 網域上可用。

<!-- parameter end -->
<!-- parameter start -->

permanentLinkPattern

String

LIFF URL 中額外資訊的處理方式。回傳 `concat`。

詳細資訊請參閱 LIFF 文件中的 [Opening a LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Discontinued") -->

utouId

String

此屬性已停止提供。詳細資訊請參閱 2023 年 2 月 6 日的消息 [We've discontinued providing company internal identifiers of chat rooms to LIFF apps as of February 6, 2023](https://developers.line.biz/en/news/2023/02/06/liff-spec-change/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Discontinued") -->

groupId

String

此屬性已停止提供。詳細資訊請參閱 2023 年 2 月 6 日的消息 [We've discontinued providing company internal identifiers of chat rooms to LIFF apps as of February 6, 2023](https://developers.line.biz/en/news/2023/02/06/liff-spec-change/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Discontinued") -->

roomId

String

此屬性已停止提供。詳細資訊請參閱 2023 年 2 月 6 日的消息 [We've discontinued providing company internal identifiers of chat rooms to LIFF apps as of February 6, 2023](https://developers.line.biz/en/news/2023/02/06/liff-spec-change/)。

<!-- parameter end -->

_Example (LIFF browser)_

<!-- tab start `json` -->

```json
{
  "type": "utou",
  "utouId": "e2bff570-...",
  "userId": "U850014438e...",
  "liffId": "123456-abcedfg",
  "viewType": "full",
  "endpointUrl": "https://example.com/",
  "accessTokenHash": "EVWYWo1yYA...",
  "availability": {
    "shareTargetPicker": {
      "permission": true,
      "minVer": "10.3.0"
    },
    "multipleLiffTransition": {
      "permission": true,
      "minVer": "10.18.0"
    },
    "subwindowOpen": {
      "permission": true,
      "minVer": "11.7.0"
    },
    "scanCode": {
      "permission": false,
      "minVer": "9.4.0",
      "unsupportedFromVer": "9.19.0"
    },
    "scanCodeV2": {
      "permission": true,
      "minVer": "11.7.0",
      "minOsVer": "14.3.0"
    },
    "getAdvertisingId": {
      "permission": false,
      "minVer": "7.14.0"
    },
    "addToHomeScreen": {
      "permission": false,
      "minVer": "9.16.0"
    },
    "bluetoothLeFunction": {
      "permission": false,
      "minVer": "9.14.0",
      "unsupportedFromVer": "9.19.0"
    },
    "skipChannelVerificationScreen": {
      "permission": false,
      "minVer": "11.14.0"
    },
    "addToHomeV2": {
      "permission": false,
      "minVer": "13.20.0"
    },
    "addToHomeHideDomain": {
      "permission": false,
      "minVer": "13.20.0"
    },
    "addToHomeLineScheme": {
      "permission": false,
      "minVer": "13.20.0"
    }
  },
  "scope": [
    "chat_message.write",
    "openid",
    "profile"
  ],
  "menuColorSetting": {
    "adaptableColorSchemes": [
      "light"
    ],
    "lightModeColor": {
      "iconColor": "#111111",
      "statusBarColor": "black",
      "titleTextColor": "#111111",
      "titleSubtextColor": "#B7B7B7",
      "titleButtonColor": "#111111",
      "titleBackgroundColor": "#FFFFFF",
      "progressBarColor": "#06C755",
      "progressBackgroundColor": "#FFFFFF"
    },
    "darkModeColor": {
      "iconColor": "#FFFFFF",
      "statusBarColor": "white",
      "titleTextColor": "#FFFFFF",
      "titleSubtextColor": "#949494",
      "titleButtonColor": "#FFFFFF",
      "titleBackgroundColor": "#111111",
      "progressBarColor": "#06C755",
      "progressBackgroundColor": "#111111"
    }
  },
  "miniDomainAllowed": false,
  "permanentLinkPattern": "concat"
}
```

<!-- tab end -->

_Example (external browser)_

<!-- tab start `json` -->

```json
{
  "type": "external",
  "liffId": "123456-abcedfg",
  "endpointUrl": "https://example.com/",
  "accessTokenHash": "EVWYWo1yYA...",
  "availability": {
    "shareTargetPicker": {
      "permission": true,
      "minVer": "10.3.0"
    },
    "multipleLiffTransition": {
      "permission": true,
      "minVer": "10.18.0"
    },
    "subwindowOpen": {
      "permission": true,
      "minVer": "11.7.0"
    },
    "scanCode": {
      "permission": true,
      "minVer": "9.4.0",
      "unsupportedFromVer": "9.19.0"
    },
    "scanCodeV2": {
      "permission": true,
      "minVer": "11.7.0",
      "minOsVer": "14.3.0"
    },
    "getAdvertisingId": {
      "permission": false,
      "minVer": "7.14.0"
    },
    "addToHomeScreen": {
      "permission": false,
      "minVer": "9.16.0"
    },
    "bluetoothLeFunction": {
      "permission": false,
      "minVer": "9.14.0",
      "unsupportedFromVer": "9.19.0"
    },
    "skipChannelVerificationScreen": {
      "permission": false,
      "minVer": "11.14.0"
    },
    "addToHomeV2": {
      "permission": false,
      "minVer": "13.20.0"
    },
    "addToHomeHideDomain": {
      "permission": false,
      "minVer": "13.20.0"
    },
    "addToHomeLineScheme": {
      "permission": false,
      "minVer": "13.20.0"
    }
  },
  "scope": [
    "chat_message.write",
    "openid",
    "profile"
  ],
  "menuColorSetting": {
    "adaptableColorSchemes": [
      "light"
    ],
    "lightModeColor": {
      "iconColor": "#111111",
      "statusBarColor": "black",
      "titleTextColor": "#111111",
      "titleSubtextColor": "#B7B7B7",
      "titleButtonColor": "#111111",
      "titleBackgroundColor": "#FFFFFF",
      "progressBarColor": "#06C755",
      "progressBackgroundColor": "#FFFFFF"
    },
    "darkModeColor": {
      "iconColor": "#FFFFFF",
      "statusBarColor": "white",
      "titleTextColor": "#FFFFFF",
      "titleSubtextColor": "#949494",
      "titleButtonColor": "#FFFFFF",
      "titleBackgroundColor": "#111111",
      "progressBarColor": "#06C755",
      "progressBackgroundColor": "#111111"
    }
  },
  "miniDomainAllowed": false,
  "permanentLinkPattern": "concat"
}
```

<!-- tab end -->

#### `availability` object 

`availability` 物件包含以下屬性：

<!-- parameter start -->

shareTargetPicker

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 [`liff.shareTargetPicker()`](https://developers.line.biz/en/reference/liff/#share-target-picker) 在啟動 LIFF app 的環境中是否可用。

\* 若要取得 `liff.shareTargetPicker()` 是否可用的資訊，我們強烈建議改用 [liff.isApiAvailable('shareTargetPicker')](https://developers.line.biz/en/reference/liff/#is-api-available)。

<!-- parameter end -->
<!-- parameter start -->

multipleLiffTransition

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示在啟動 LIFF app 的環境中，是否可以在 LIFF 瀏覽器內透過 [`liff.openWindow()`](https://developers.line.biz/en/reference/liff/#open-window) 在不關閉 LIFF app 的情況下[轉換到另一個 LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff)。

\* 若要取得多個 LIFF app 之間轉換是否可用的資訊，我們強烈建議改用 [liff.isApiAvailable('multipleLiffTransition')](https://developers.line.biz/en/reference/liff/#is-api-available)。

<!-- parameter end -->
<!-- parameter start -->

subwindowOpen

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示子視窗在啟動 LIFF app 的環境中是否可用。

<!-- parameter end -->
<!-- parameter start -->

scanCode

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 [`liff.scanCode()`](https://developers.line.biz/en/reference/liff/#scan-code) 在啟動 LIFF app 的環境中是否可用。

<!-- parameter end -->
<!-- parameter start -->

scanCodeV2

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 在啟動 LIFF app 的環境中是否可用。

<!-- parameter end -->
<!-- parameter start -->

getAdvertisingId

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 `liff.getAid()` 在啟動 LIFF app 的環境中是否可用。

請注意，我們目前不提供 `liff.getAid()`。

<!-- parameter end -->
<!-- parameter start -->

addToHomeScreen

String

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 `liff.addToHomeScreen()` 在啟動 LIFF app 的環境中是否可用。

請注意，我們目前不提供 `liff.addToHomeScreen()`。

<!-- parameter end -->
<!-- parameter start -->

bluetoothLeFunction

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 LINE Things 的 Bluetooth® Low Energy 在啟動 LIFF app 的環境中是否可用。

請注意，我們目前不提供此功能。

<!-- parameter end -->
<!-- parameter start -->

skipChannelVerificationScreen

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示「Channel consent simplification」功能在啟動 LIFF app 的環境中是否可用。詳細資訊請參閱 LINE MINI App 文件中的 [Skipping the channel consent process](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/)。

<!-- parameter end -->
<!-- parameter start -->

addToHomeV2

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示 [`liff.createShortcutOnHomeScreen()`](https://developers.line.biz/en/reference/liff/#create-shortcut-on-home-screen) 在啟動 LIFF app 的環境中是否可用。

\* 若要取得 `liff.createShortcutOnHomeScreen()` 是否可用的資訊，我們強烈建議改用 [liff.isApiAvailable('createShortcutOnHomeScreen')](https://developers.line.biz/en/reference/liff/#is-api-available)。

<!-- parameter end -->
<!-- parameter start -->

addToHomeHideDomain

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示在顯示將捷徑加入使用者裝置主畫面的畫面時，是否可以隱藏端點 URL。

請注意，我們目前不提供此功能。

<!-- parameter end -->
<!-- parameter start -->

addToHomeLineScheme

Object

回傳[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-availability-common)，表示是否可以建立指定 [LINE URL scheme](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/) 的捷徑。

請注意，我們目前不提供此功能。

<!-- parameter end -->

_Example_

<!-- tab start `json` -->

```json
{
  "shareTargetPicker": {
    "permission": true,
    "minVer": "10.3.0"
  }
}
```

<!-- tab end -->

#### Common properties of the `availability` object 

<!-- parameter start -->

permission

Boolean

指定由 `availability` 物件的屬性名稱所指定的功能，在啟動 LIFF app 的環境中是否可用。

- `true`：該功能可用。
- `false`：該功能不可用。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

minVer

String

支援對應功能的最低 LINE 版本。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

maxVer

String

支援對應功能的最高 LINE 版本。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

unsupportedFromVer

String

不再支援對應功能的 LINE 版本。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

minOsVer

String

支援對應功能的最低 OS 版本。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

maxOsVer

String

支援對應功能的最高 OS 版本。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

unsupportedFromOsVer

String

不再支援對應功能的 OS 版本。

<!-- parameter end -->

#### `menuColorSetting` object 

`menuColorSetting` 物件包含以下屬性：

<!-- parameter start -->

adaptableColorSchemes

Array of strings

固定回傳 `light`。

<!-- parameter end -->
<!-- parameter start -->

lightModeColor

Object

當 `adaptableColorSchemes` 為 `light` 時，以[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-menucolorsetting-common)回傳標頭顏色設定。

<!-- parameter end -->
<!-- parameter start -->

darkModeColor

Object

當 `adaptableColorSchemes` 為 `dark` 時，以[物件](https://developers.line.biz/en/reference/liff/#get-context-return-value-menucolorsetting-common)回傳標頭顏色設定。

請注意，我們目前不提供標頭顏色設定。

<!-- parameter end -->

_Example_

<!-- tab start `json` -->

```json
{
  "adaptableColorSchemes": [
    "light"
  ],
  "lightModeColor": {
    "iconColor": "#111111",
    "statusBarColor": "black",
    "titleTextColor": "#111111",
    "titleSubtextColor": "#B7B7B7",
    "titleButtonColor": "#111111",
    "titleBackgroundColor": "#FFFFFF",
    "progressBarColor": "#06C755",
    "progressBackgroundColor": "#FFFFFF"
  },
  "darkModeColor": {
    "iconColor": "#FFFFFF",
    "statusBarColor": "white",
    "titleTextColor": "#FFFFFF",
    "titleSubtextColor": "#949494",
    "titleButtonColor": "#FFFFFF",
    "titleBackgroundColor": "#111111",
    "progressBarColor": "#06C755",
    "progressBackgroundColor": "#111111"
  }
}
```

<!-- tab end -->

#### Common properties of the `menuColorSetting` object 

<!-- parameter start -->

iconColor

String

標頭圖示的顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->
<!-- parameter start -->

statusBarColor

String

固定回傳 `white`。

<!-- parameter end -->
<!-- parameter start -->

titleTextColor

String

標頭標題文字的顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->
<!-- parameter start -->

titleSubtextColor

String

標頭副標題文字的顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->
<!-- parameter start -->

titleButtonColor

String

標頭按鈕的顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->
<!-- parameter start -->

titleBackgroundColor

String

標頭背景顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->
<!-- parameter start -->

progressBarColor

String

標頭進度條的顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->
<!-- parameter start -->

progressBackgroundColor

String

標頭進度條的背景顏色。顏色以 `#RRGGBB` 格式的十六進位顏色代碼表示。

<!-- parameter end -->

### liff.isInClient() 

判斷 LIFF app 是否在 LIFF 瀏覽器中執行。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

即使在透過 `liff.init()` 初始化 LIFF app 完成之前，您也可以使用此方法。

<!-- tip end -->

#### Syntax 

```javascript
liff.isInClient();
```

#### Arguments 

None

#### Return value 

- `true`：在 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中執行
- `false`：在 [external browser](https://developers.line.biz/en/glossary/#external-browser) 或 [LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab) 中執行

### liff.isLoggedIn() 

檢查使用者是否已登入。

_Example_

<!-- tab start `javascript` -->

```javascript
if (liff.isLoggedIn()) {
  // The user can use an API that requires an access token, such as liff.getProfile().
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.isLoggedIn();
```

#### Arguments 

None

#### Return value 

- `true`：使用者已登入。
- `false`：使用者未登入。

### liff.isApiAvailable() 

檢查指定的 API 或功能在您啟動 LIFF app 的環境中是否可用。具體來說，它會驗證目前的 LINE 版本是否支援該 API，以及該 API 的條款與條件是否已被接受。

_Example_

<!-- tab start `javascript` -->

```javascript
// Check if shareTargetPicker is available
if (liff.isApiAvailable('shareTargetPicker')) {
  liff.shareTargetPicker([
    {
      type: "text",
      text: "Hello, World!"
    }
  ])
    .then(
      console.log("ShareTargetPicker was launched")
    ).catch(function(res) {
      console.log("Failed to launch ShareTargetPicker")
    })
}

// Check if the LIFF-to-LIFF transition is available
if (liff.isApiAvailable('multipleLiffTransition')) {
  window.location.href = "https://line.me/{liffId}", // URL for another LIFF app
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.isApiAvailable(apiName);
```

#### Arguments 

<!-- parameter start (props: required) -->

apiName

String

LIFF 用戶端 API 或功能的名稱。您可以指定以下其中之一：

- `createShortcutOnHomeScreen`：[`liff.createShortcutOnHomeScreen()`](https://developers.line.biz/en/reference/liff/#create-shortcut-on-home-screen) 方法是否可用
- `scanCodeV2`：[`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法是否可用
- `scanCode`：[`liff.scanCode()`](https://developers.line.biz/en/reference/liff/#scan-code) 方法是否可用
- `shareTargetPicker`：[`liff.shareTargetPicker()`](https://developers.line.biz/en/reference/liff/#share-target-picker) 方法是否可用
- `iap`：LINE MINI App 的[應用程式內購買（in-app purchase）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)功能是否可用
- `multipleLiffTransition`：[LIFF-to-LIFF transition](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff) 是否可用
- `skipChannelVerificationScreen`：LINE MINI App 的 [channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#what-is-channel-consent-simplification) 功能是否可用

<!-- parameter end -->

#### Return value 

回傳指定的 API 或功能在目前環境中是否可用。如果可用，回傳 `true`。如果不可用，回傳 `false`。以下是回傳 `false` 的範例：

- 如果 LIFF app 是以不支援該 API 的 LINE 版本啟動
- 如果 LIFF app 是在外部瀏覽器中啟動，而該 API 在外部瀏覽器中不可用
- 如果使用該 API 必須接受條款與條件，而條款與條件尚未被接受
- 如果使用該 API 必須登入，而使用者尚未登入
- 如果使用該 API 必須有有效的存取權杖，而存取權杖已過期

## Authentication 

### liff.login() 

在 [LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab) 或 [external browser](https://developers.line.biz/en/glossary/#external-browser) 中執行登入處理。

<!-- note start -->

**Note**

您無法在 LIFF 瀏覽器中使用 `liff.login()`，因為它會在執行 `liff.init()` 時自動執行。

<!-- note end -->

<!-- note start -->

**LIFF 瀏覽器內的授權請求**

LINE Login 授權請求在 LIFF 瀏覽器內的行為不予保證。此外，當從外部瀏覽器或 LINE's in-app browser 開啟 LIFF app 時，請務必使用此方法進行登入處理，而非[使用 LINE Login 的授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
if (!liff.isLoggedIn()) {
  liff.login({ redirectUri: "https://example.com/path" });
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.login(loginConfig);
```

#### Arguments 

<!-- parameter start (props: optional) -->

loginConfig

Object

登入設定

<!-- parameter end -->
<!-- parameter start (props: optional) -->

loginConfig.redirectUri

String

登入後要在 LIFF app 中開啟的 URL。預設值為 **Endpoint URL** 中設定的 URL。如需如何設定 **Endpoint URL** 的詳細資訊，請參閱 LIFF 文件中的 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

如果在 `redirectUri` 中指定的 URL 並非以 **Endpoint URL** 中指定的 URL 開頭，登入處理會失敗，並顯示錯誤畫面。

![](https://developers.line.biz/media/liff/liff_login_error_screen.png)

例如，如果 **Endpoint URL** 為 `https://example.com/path1/path2?query1=value1`，則登入處理的成功或失敗如下所示。查詢參數與 URL 片段（URL fragment）不會影響登入處理的成功或失敗。

<table>
  <thead>
    <tr>
      <th>redirectUri</th>
      <th>Login process</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>https://example.com/path1/path2?query1=value1</li>
          <li>https://example.com/path1/path2?query2=value2</li>
          <li>https://example.com/path1/path2#URL-fragment</li>
          <li>https://example.com/path1/path2</li>
          <li>https://example.com/path1/path2/</li>
          <li>https://example.com/path1/path2/path3</li>
        </ul>
      </td>
      <td>✅ 成功</td>
    </tr>
    <tr>
      <td>
        <ul>
          <li>https://example.com/path1</li>
          <li>https://example.com/</li>
          <li>https://example.com/path2/path1</li>
        </ul>
      </td>
      <td>❌ 失敗</td>
    </tr>
  </tbody>
</table>

<!-- parameter end -->

#### Return value 

None

### liff.logout() 

登出。

_Example_

<!-- tab start `javascript` -->

```javascript
if (liff.isLoggedIn()) {
  liff.logout();
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.logout();
```

#### Arguments 

None

#### Return value 

None

### liff.getAccessToken() 

取得目前使用者的存取權杖。

您可以使用透過此 API 取得的存取權杖，將使用者資料從 LIFF app 傳送到伺服器。詳細資訊請參閱 LIFF 文件中的 [Using user data in LIFF apps and servers](https://developers.line.biz/en/docs/liff/using-user-profile/)。

#### Access token validity period 

存取權杖在發行後 12 小時內有效。然而，即使在此有效期間內，存取權杖也可能因使用者的操作而被撤銷。

- 當使用者關閉 LIFF app 時，存取權杖可能會被撤銷。詳細資訊請參閱 LIFF 文件中的 [Behavior when closing the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#behavior-when-closing-liff-app)。
- 在啟用「[Channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#what-is-channel-consent-simplification)」功能的 LINE MINI App 中，從驗證畫面授予額外權限會更新存取權杖，並撤銷先前發行的存取權杖。詳細資訊請參閱 LINE MINI App 文件中的 [Request permissions other than the `openid` scope on the verification screen](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

<!-- tip start -->

**取得存取權杖**

- 如果使用者在 LIFF 瀏覽器中啟動 LIFF app，當您呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 時，LIFF SDK 會取得存取權杖。
- 如果使用者在外部瀏覽器中啟動 LIFF app，當滿足以下步驟時，LIFF SDK 會取得存取權杖：
  1. 您呼叫 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login)。
  2. 使用者登入。
  3. 您呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app)。

<!-- tip end -->

_Example_

<!-- tab start `javascript` -->

```javascript
const accessToken = liff.getAccessToken();
if (accessToken) {
  fetch("https://api...", {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${accessToken}`,
    },
    //...
  });
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.getAccessToken();
```

#### Arguments 

None

#### Return value 

以字串回傳目前使用者的存取權杖。

### liff.getIDToken() 

取得 LIFF SDK 所取得的目前使用者的 ID 權杖。ID 權杖是包含使用者資料的 JSON Web Token（JWT）。

當您要將使用者資料從 LIFF app 傳送到伺服器時，可以使用透過此 API 取得的 ID 權杖。詳細資訊請參閱 LIFF 文件中的 [Using user data in LIFF apps and servers](https://developers.line.biz/en/docs/liff/using-user-profile/)。

<!-- note start -->

**選擇 scope**

[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時，請選擇 `openid` scope。如果您未選擇該 scope，或使用者未授予權限，您將無法取得 ID 權杖。即使在加入 LIFF app 之後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- note end -->

<!-- tip start -->

**取得 ID 權杖**

- 如果使用者在 LIFF 瀏覽器中啟動 LIFF app，當您呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 時，LIFF SDK 會取得 ID 權杖。
- 如果使用者在外部瀏覽器中啟動 LIFF app，當滿足以下步驟時，LIFF SDK 會取得 ID 權杖：

  1. 您呼叫 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login)。
  2. 使用者登入。
  3. 您呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app)。

<!-- tip end -->

<!-- tip start -->

**您可以取得使用者的電子郵件位址**

若要取得使用者的電子郵件位址，請在[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時選擇 `email` scope。一旦使用者授予權限，您即可取得電子郵件位址。即使在加入 LIFF app 之後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- tip end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff
  .init({
    liffId: "123456-abcedfg", // Use own liffId
  })
  .then(() => {
    const idToken = liff.getIDToken();
    console.log(idToken); // print idToken object
  });
```

<!-- tab end -->

#### Syntax 

```javascript
liff.getIDToken();
```

#### Argument 

None

#### Return value 

回傳 ID 權杖。

### liff.getDecodedIDToken() 

取得 LIFF SDK 所取得的 ID 權杖的 payload。payload 包含使用者顯示名稱、個人檔案圖片 URL、電子郵件位址等資訊。

當您想要在 LIFF app 中使用使用者的顯示名稱時，請使用此方法。

您只能取得主要個人檔案資訊。您無法取得使用者的[子個人檔案（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

<!-- warning start -->

**請勿將使用者資訊傳送到伺服器**

請勿將透過此方法取得的使用者資料傳送到伺服器。詳細資訊請參閱 LIFF 文件中的 [Using user data in LIFF apps and servers](https://developers.line.biz/en/docs/liff/using-user-profile/)。

<!-- warning end -->

<!-- note start -->

**選擇 scope**

[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時，請選擇 `openid` scope。如果您未選擇該 scope，或使用者未授予權限，您將無法取得 ID 權杖。即使在加入 LIFF app 之後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- note end -->

<!-- tip start -->

**取得 ID 權杖**

- 如果使用者在 LIFF 瀏覽器中啟動 LIFF app，當您呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 時，LIFF SDK 會取得 ID 權杖。
- 如果使用者在外部瀏覽器中啟動 LIFF app，當滿足以下步驟時，LIFF SDK 會取得 ID 權杖：

  1. 您呼叫 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login)。
  2. 使用者登入。
  3. 您呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app)。

<!-- tip end -->

<!-- tip start -->

**您可以取得使用者的電子郵件位址**

若要取得使用者的電子郵件位址，請在[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時選擇 `email` scope。一旦使用者授予權限，您即可取得電子郵件位址。即使在加入 LIFF app 之後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- tip end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff
  .init({
    liffId: "123456-abcedfg", // Use own liffId
  })
  .then(() => {
    const idToken = liff.getDecodedIDToken();
    console.log(idToken); // print decoded idToken object
  });
```

<!-- tab end -->

#### Syntax 

```javascript
liff.getDecodedIDToken();
```

#### Arguments 

None

#### Return value 

取得 ID 權杖的 payload。

如需 ID 權杖 payload 的詳細資訊，請參閱 Integrate LINE Login 文件中 [Get profile information from ID tokens](https://developers.line.biz/en/docs/line-login/verify-id-token/) 的 **Payload** 區段。

_Example_

<!-- tab start `json` -->

```json
{
  "iss": "https://access.line.me",
  "sub": "U1234567890abcdef1234567890abcdef ",
  "aud": "1234567890",
  "exp": 1504169092,
  "iat": 1504263657,
  "amr": ["pwd"],
  "name": "Taro Line",
  "picture": "https://sample_line.me/aBcdefg123456"
}
```

<!-- tab end -->

### liff.permission.getGrantedAll() 

取得使用者已同意授權的 scope 清單。

您可以透過此方法取得的 scope 如下：

- [`profile`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`chat_message.write`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`openid`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`email`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)

<!-- tip start -->

**liff.getContext() 與 liff.permission.getGrantedAll() 的差異**

[`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法會取得 LIFF app 的 scope 清單（\*）。

另一方面，`liff.permission.getGrantedAll()` 方法則會取得 LIFF app 的 scope 中，使用者已同意授權的 scope 清單。

\* 在 LINE Login 頻道的 **LIFF** 分頁下「Scope」區段中指定的 scope

<!-- tip end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff.permission.getGrantedAll().then((scopes) => {
  // ["profile", "chat_message.write", "openid", "email"]
  console.log(scopes);
});
```

<!-- tab end -->

#### Syntax 

```javascript
liff.permission.getGrantedAll();
```

#### Arguments 

None

#### Return value 

當 `Promise` 被 resolve 時，會傳遞使用者已同意授權的 scope 陣列。

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

### liff.permission.query() 

驗證使用者是否同意授予指定的權限。

_Example_

<!-- tab start `javascript` -->

```javascript
liff.permission.query("profile").then((permissionStatus) => {
  // permissionStatus = { state: 'granted' }
});
```

<!-- tab end -->

#### Syntax 

```javascript
liff.permission.query(permission);
```

#### Arguments 

<!-- parameter start (props: required) -->

permission

String

要檢查的權限。請指定以下其中一個 scope：

- [`profile`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`chat_message.write`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`openid`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`email`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)

<!-- parameter end -->

#### Return value 

回傳 `Promise` 物件。

當 `Promise` 被 resolve 時，會回傳包含以下屬性的物件。

<!-- parameter start -->

state

String

包含以下其中一個值：

- `granted`：使用者已同意授權。
- `prompt`：使用者尚未同意授權。
- `unavailable`：不可用，因為該頻道沒有指定的 scope。

<!-- parameter end -->

### liff.permission.requestAll() 

顯示 LINE MINI App 所請求權限的「Verification screen（驗證畫面）」。

![verification screen](https://developers.line.biz/media/line-mini-app/verification-screen-en.png)

<!-- note start -->

**liff.permission.requestAll() 的作業環境**

`liff.permission.requestAll()` 僅在 [LINE MINI Apps](https://developers.line.biz/en/docs/line-mini-app/) 上運作。

若要執行此方法，您需要事先在 [LINE Developers Console](https://developers.line.biz/console/) 上開啟 **Channel consent simplification**。如需設定 Channel consent simplification 功能的詳細資訊，請參閱 LINE MINI App 文件中的 [The "Channel consent simplification" feature setup](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#simplification-feature-setup)。

<!-- note end -->

<!-- note start -->

**執行此方法前，請確認使用者尚未同意所有權限**

如果使用者已同意所有權限，而您執行 `liff.permission.requestAll()`，則 `Promise` 會被 reject 並回傳 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。因此，請使用 [`liff.permission.query()`](https://developers.line.biz/en/reference/liff/#permission-query) 檢查使用者是否已同意所有權限，並僅在使用者有未同意的權限時才執行 `liff.permission.requestAll()`。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff.permission.query("profile").then((permissionStatus) => {
  if (permissionStatus.state === "prompt") {
    liff.permission.requestAll();
  }
});
```

<!-- tab end -->

#### Syntax 

```javascript
liff.permission.requestAll();
```

#### Arguments 

None

#### Return value 

回傳一個 `Promise` 物件。

##### Error response 

如果 **Channel consent simplification** 未開啟，且使用者已同意所有權限，則 `Promise` 會被 reject 並回傳 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

## Profile 

### liff.getProfile() 

取得目前使用者的[個人檔案資訊](https://developers.line.biz/en/glossary/#profile-information)。

您只能取得主要個人檔案資訊。您無法取得使用者的[子個人檔案（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

<!-- warning start -->

**請勿將使用者資訊傳送到伺服器**

請勿將透過此方法取得的使用者資料傳送到伺服器。詳細資訊請參閱 LIFF 文件中的 [Using user data in LIFF apps and servers](https://developers.line.biz/en/docs/liff/using-user-profile/)。

<!-- warning end -->

<!-- note start -->

**選擇 scope**

[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時，請選擇 `profile` scope。如果您未選擇該 scope，或使用者未授予權限，您將無法取得使用者個人檔案。即使在加入 LIFF app 之後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff
  .getProfile()
  .then((profile) => {
    const name = profile.displayName;
  })
  .catch((err) => {
    console.log("error", err);
  });
```

<!-- tab end -->

#### Syntax 

```javascript
liff.getProfile();
```

#### Arguments 

None

#### Return value 

回傳一個 `Promise` 物件。

當 `Promise` 被 resolve 時，會傳遞包含使用者個人檔案資訊的物件。

<!-- parameter start -->

userId

String

使用者 ID

<!-- parameter end -->
<!-- parameter start -->

displayName

String

顯示名稱

<!-- parameter end -->
<!-- parameter start -->

pictureUrl

String

圖片 URL。如果使用者未設定，則不會回傳此屬性。

<!-- parameter end -->
<!-- parameter start -->

statusMessage

String

狀態訊息。如果使用者未設定，則不會回傳此屬性。

<!-- parameter end -->

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

_Example_

<!-- tab start `json` -->

```json
{
  "userId": "U4af4980629...",
  "displayName": "Brown",
  "pictureUrl": "https://profile.line-scdn.net/abcdefghijklmn",
  "statusMessage": "Hello, LINE!"
}
```

<!-- tab end -->

### liff.getFriendship() 

取得使用者與 LINE 官方帳號（LINE Official Account）之間的好友關係狀態。

但是，您只能取得使用者與已連結到您 LIFF app 所加入的同一個 LINE Login 頻道的 LINE 官方帳號之間的好友關係狀態。如需瞭解如何將 LINE 官方帳號連結到 LINE Login 頻道，請參閱 LINE Login 文件中的 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。

<!-- note start -->

**選擇 scope**

[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時，請選擇 `profile` scope。如果您未選擇該 scope，或使用者未授予權限，您將無法取得好友關係狀態。即使在加入 LIFF app 之後，仍可在 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁中變更 scope 的選擇。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff.getFriendship().then((data) => {
  if (data.friendFlag) {
    // something you want to do
  }
});
```

<!-- tab end -->

#### Syntax 

```javascript
liff.getFriendship();
```

#### Arguments 

None

#### Return value 

回傳一個 `Promise` 物件。

當取得好友關係狀態時，`Promise` 會被 resolve 並傳遞好友關係資訊。

<!-- parameter start -->

friendFlag

Boolean

- `true`：使用者已將 LINE 官方帳號加為好友且未封鎖。
- 否則為 `false`。

<!-- parameter end -->

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

_Example_

<!-- tab start `json` -->

```json
{
  "friendFlag": true
}
```

<!-- tab end -->

### liff.requestFriendship() 

顯示一個子視窗，提示使用者將 LINE 官方帳號加為好友，或解除封鎖。

![](https://developers.line.biz/media/liff/request-friendship/request-friendship-add-friend-en.png)

- 如果使用者尚未將 LINE 官方帳號加為好友，會顯示提示使用者將其加為好友的子視窗。
- 如果使用者已封鎖 LINE 官方帳號，會顯示提示使用者解除封鎖的子視窗。
- 如果使用者已經是 LINE 官方帳號的好友，則會顯示子視窗後自動關閉。

提示使用者加為好友或解除封鎖的 LINE 官方帳號，可以透過[將 LINE 官方帳號與您的頻道連結](https://developers.line.biz/en/docs/line-login/link-a-bot/#link-a-line-official-account)來指定。詳細資訊請參閱 LINE Login 文件中的 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。

僅在 LIFF 瀏覽器的螢幕大小為 `Full` 時可用。詳細資訊請參閱 LIFF 文件中的 [Size of the LIFF browser](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

_Example_

<!-- tab start `javascript` -->

```javascript
try {
  await liff.requestFriendship();
} catch (error) {
  console.log(error);
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.requestFriendship();
```

#### Arguments 

None

#### Return value 

回傳一個 `Promise` 物件。

<!-- note start -->

**無法從回傳值確認使用者的操作結果**

無法從回傳值確認使用者是否已將 LINE 官方帳號加為好友或解除封鎖。若要在呼叫 `liff.requestFriendship()` 方法後檢查好友關係狀態，請使用 [`liff.getFriendship()`](https://developers.line.biz/en/reference/liff/#get-friendship) 方法。

<!-- note end -->

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

如果 add friend option 中的 **Linked LINE Official Account** 未設定，或 LIFF app 的螢幕大小不是 `Full`，則會回傳錯誤碼 `FORBIDDEN`。

## Window 

### liff.openWindow() 

在 LINE's in-app browser 或外部瀏覽器中開啟指定的 URL。

<!-- note start -->

**liff.openWindow() 的作業環境**

在外部瀏覽器中使用 `liff.openWindow()` 不予保證。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff.openWindow({
  url: "https://line.me",
  external: true,
});
```

<!-- tab end -->

#### Behavioral differences by LINE version 

當開啟支援 [Universal Links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/) 或 [App Links](https://developer.android.com/training/app-links) 的 URL 時，`liff.openWindow()` 方法的行為會依 LINE 版本與 [`params.external`](https://developers.line.biz/en/reference/liff/#open-window-arguments) 參數的設定而有所不同。行為的差異如下：

|  | `params.external = false`<br>（預設） | `params.external = true` |
| --- | --- | --- |
| LINE 早於 14.20.0（\*） | <ul><li>iOS：在 LINE's in-app browser 中開啟 URL</li><li>Android：轉換到對應的 app</li></ul> | <ul><li>iOS：轉換到對應的 app</li><li>Android：在預設瀏覽器中開啟 URL</li></ul> |
| LINE 14.20.0 或更新版本，<br>或早於 15.20.0 | 轉換到對應的 app | 轉換到對應的 app |
| LINE 15.20.0 或更新版本 | 在 LINE's in-app browser 中開啟 URL | 轉換到對應的 app |

\* 在 LINE 版本 14.20.0 或更新版本中，行為不再因 OS 而異。

#### Syntax 

```javascript
liff.openWindow(params);
```

#### Arguments 

<!-- parameter start (props: required) -->

params

Object

參數物件

<!-- parameter end -->
<!-- parameter start (props: required) -->

params.url

String

URL。請指定完整的 URL。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

params.external

Boolean

是否在外部瀏覽器中開啟 URL。請指定以下其中一個值。預設值為 `false`。

- `true`：在外部瀏覽器中開啟 URL。
- `false`：在 LINE's in-app browser 中開啟 URL。

<!-- parameter end -->

#### Return value 

None

### liff.closeWindow() 

關閉 LIFF app。

關閉 LIFF app 時的行為取決於 LINE app 版本與 LIFF app 的設定。詳細資訊請參閱 LIFF 文件中的 [Behavior when closing the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#behavior-when-closing-liff-app)。

<!-- tip start -->

**此方法可在 LIFF app 初始化之前使用**

若要在透過 `liff.init()` 初始化 LIFF app 完成之前使用 `liff.closeWindow()` 方法，您的 LIFF SDK 版本必須為 v2.4.0 或更新版本。

<!-- tip end -->

<!-- note start -->

**Note**

`liff.closeWindow()` 在外部瀏覽器中不保證能正常運作。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff.closeWindow();
```

<!-- tab end -->

#### Syntax 

```javascript
liff.closeWindow();
```

#### Arguments 

None

#### Return value 

None

## Message 

### liff.sendMessages() 

代表使用者將訊息傳送到開啟 LIFF app 的聊天室。

若要使用此功能，必須滿足以下條件：

- 在從一對一聊天、[群組聊天（group chat）](https://developers.line.biz/en/glossary/#group)或[多人聊天（multi-person chat）](https://developers.line.biz/en/glossary/#room)啟動的 LIFF app 的 LIFF 瀏覽器內
- [`chat_message.write` scope](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app) 已啟用
- LIFF app 尚未從[最近使用的服務（recently used services）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view-recent-service)區段重新載入

如果未滿足這些條件，`liff.sendMessages()` 方法將不可用，並會發生錯誤碼為 `403` 的 `user doesn't grant required permissions yet` 錯誤。以下是會導致此錯誤的案例範例：

- 使用 [Keep Memo](https://help.line.me/line/smartphone/pc?lang=en&contentId=20017696) 功能存取 LIFF app 時。
- 透過網站重新導向處理等方式存取[開啟 LIFF app](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-a-liff-app) 的 URL scheme 時。
- 在 LIFF-to-LIFF 轉換後 `chat_message.write` scope 被停用時。詳細資訊請參閱 LIFF 文件中的 [About the "chat_message.write" scope after transitioning between LIFF apps](https://developers.line.biz/en/docs/liff/opening-liff-app/#about-chat-message-write-scope)。
- 使用者未授予 `chat_message.write` scope 時。

您可以使用 [`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法取得啟動 LIFF app 的畫面類型。

_Example_

<!-- tab start `javascript` -->

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

<!-- tab end -->

#### Syntax 

```javascript
liff.sendMessages(messages);
```

#### Arguments 

<!-- parameter start (props: required) -->

messages

Array of objects

[Message 物件](https://developers.line.biz/en/reference/messaging-api/#message-objects)\
最多：5\
您可以傳送以下類型的 Messaging API 訊息：

- [Text message](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)。但是，`emojis` 屬性與 `quoteToken` 屬性不可用。
- [Sticker message](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)。但是，`quoteToken` 屬性不可用。
- [Image message](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)。
- [Video message](https://developers.line.biz/en/docs/messaging-api/message-types/#video-messages)。但是，`trackingId` 屬性不可用。
- [Audio message](https://developers.line.biz/en/docs/messaging-api/message-types/#audio-messages)。
- [Location message](https://developers.line.biz/en/docs/messaging-api/message-types/#location-messages)。
- [Template message](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)。但是，只能設定 [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action) 作為 action。
- [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages)。但是，只能設定 [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action) 作為 action。

<!-- parameter end -->

當使用者透過 `liff.sendMessages()` 方法傳送 template message 或 Flex Message 時，LINE Platform 不會傳送 webhook。對於所有其他[訊息類型（message types）](https://developers.line.biz/en/docs/messaging-api/message-types/)，則會傳送 webhook。當使用 `liff.sendMessages()` 方法傳送 image、video 與 audio 訊息時，產生的 webhook 事件會包含值為 `external` 的 `contentProvider.type` 屬性。詳細資訊請參閱 Messaging API 參考中的 [Message event](https://developers.line.biz/en/reference/messaging-api/#message-event)。

#### Return value 

回傳一個 `Promise` 物件。

- 如果訊息傳送成功，`Promise` 會被 resolve。不會傳遞任何值。
- 如果傳送訊息失敗，`Promise` 會被 reject 並傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

### liff.shareTargetPicker() 

顯示 target picker（選擇群組或好友的畫面），並將開發者建立的訊息傳送給選定的對象。該訊息對群組或好友來說，會顯示為由使用者本人傳送的訊息。

在 target picker 中，只能選擇使用者所參與的好友（包括 LINE 官方帳號）與群組。不包含 OpenChat。

#### Conditions for using the liff.shareTargetPicker() method 

若要使用 `liff.shareTargetPicker()` 方法，必須滿足以下所有條件：

- 使用者已登入。
- share target picker 已在 [LINE Developers Console](https://developers.line.biz/console/) 中啟用。詳細資訊請參閱 LIFF 文件中的 [Using the share target picker](https://developers.line.biz/en/docs/liff/developing-liff-apps/#using-share-target-picker)。

<!-- note start -->

**在智慧型手機的外部瀏覽器中執行 liff.shareTargetPicker() 方法時，可能會顯示電子郵件位址登入畫面**

若要在[外部瀏覽器](https://developers.line.biz/en/glossary/#external-browser)中顯示 target picker，需要 [Single Sign On (SSO) login](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-sso-login) 工作階段。

在使用[自動登入（auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)的登入處理中，不會發行 SSO login 工作階段。因此，當執行 `liff.shareTargetPicker()` 方法時，target picker 可能不會顯示，而是改為顯示[電子郵件位址登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login)畫面。

在使用者輸入電子郵件位址與密碼登入後，會發行 SSO login 工作階段，target picker 便會正常顯示。

<!-- note end -->

<!-- note start -->

**我們不會擷取使用者透過 share target picker 傳送訊息的對象人數**

為了保護使用者隱私，我們既不收集也不提供有關使用者透過 share target picker 將訊息傳送給多少人的資訊。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff
  .shareTargetPicker(
    [
      {
        type: "text",
        text: "Hello, World!",
      },
    ],
    {
      isMultiple: true,
    },
  )
  .then(function (res) {
    if (res) {
      // succeeded in sending a message through TargetPicker
      console.log(`[${res.status}] Message sent!`);
    } else {
      // sending message canceled
      console.log("TargetPicker was closed!");
    }
  })
  .catch(function (error) {
    // something went wrong before sending a message
    console.log("something wrong happen");
  });
```

<!-- tab end -->

#### Syntax 

```javascript
liff.shareTargetPicker(messages, options);
```

#### Arguments 

<!-- parameter start (props: required) -->

messages

Array of objects

[Message 物件](https://developers.line.biz/en/reference/messaging-api/#message-objects)\
最多：5\
您可以傳送以下類型的 Messaging API 訊息：

- [Text message](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)。但是，`emojis` 屬性與 `quoteToken` 屬性不可用。
- [Image message](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)。
- [Video message](https://developers.line.biz/en/docs/messaging-api/message-types/#video-messages)。但是，`trackingId` 屬性不可用。
- [Audio message](https://developers.line.biz/en/docs/messaging-api/message-types/#audio-messages)。
- [Location message](https://developers.line.biz/en/docs/messaging-api/message-types/#location-messages)。
- [Template message](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)。但是，只能設定 [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action) 作為 action。
- [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages)。但是，只能設定 [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action) 作為 action。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

options

Object

share target picker 選項

<!-- parameter end -->
<!-- parameter start (props: optional) -->

options.isMultiple

Boolean

使用以下其中一個值，指定是否允許使用者透過 target picker 選擇多個訊息收件者。預設值為 `true`。

- `true`：使用者可以從他們的群組、好友與聊天中選擇多個收件者。
- `false`：使用者只能選擇一位好友作為收件者。

<!-- parameter end -->

<!-- note start -->

**將 isMultiple 設為 false 並不保證訊息只會傳送給一位好友**

即使您將 `isMultiple` 屬性設為 `false`，使用者仍可透過多次呼叫 share target picker，或將相同訊息重新分享給不同收件者，來將訊息傳送給多位使用者。若要嚴格限制使用者只能將訊息傳送給一位好友一次，請在實作 LIFF app 時加入限制。

以下是傳送包含 URL 的訊息並限制存取該 URL 的範例。

1. 為 URL 賦予唯一的 token 並傳送訊息。
2. 當訊息中的 URL 被存取時，伺服器端驗證 token 並限制多位使用者存取。

<!-- note end -->

#### Return value

回傳一個 `Promise` 物件。

- 如果訊息正確傳送，`Promise` 會被 resolve 並傳遞具有以下屬性的物件。

    <!-- parameter start -->

  status

  String

  `success`

    <!-- parameter end -->

- 如果使用者在傳送訊息前取消並關閉 target picker，`Promise` 會被 resolve 但不會傳遞物件。

- 如果在 target picker 顯示前發生問題，`Promise` 會被 reject 並傳遞 `LiffError`。如需 LiffError 物件的詳細資訊，請參閱 [LIFF SDK errors](https://developers.line.biz/en/reference/liff/#liff-errors)。

<!-- note start -->

**Note**

在 `Promise` 已被 resolve 與 reject 的回呼函式中，如果開發者使用 `alert()`，LIFF app 在某些裝置上將無法運作。

<!-- note end -->

## Camera 

### liff.scanCodeV2() 

啟動 2D code 讀取器並取得字串。若要啟用 2D code 讀取器，請在 [LINE Developers Console](https://developers.line.biz/console/) 上開啟 **Scan QR**。

<!-- note start -->

**liff.scanCodeV2() 的作業環境**

`liff.scanCodeV2()` 可在以下環境中運作。

- iOS：iOS 14.3 或更新版本
- Android：所有版本
- 外部瀏覽器：支援 [WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) 的網頁瀏覽器

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

\*1 您只能使用支援 [WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) 的網頁瀏覽器。

\*2 僅在 LIFF 瀏覽器的螢幕大小為 `Full` 時可用。詳細資訊請參閱 LIFF 文件中的 [Size of the LIFF browser](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

<!-- note end -->

<!-- note start -->

**開啟 [Scan QR] 以啟動 2D code 讀取器**

[將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時，請開啟 **Scan QR**。即使在將 LIFF app 加入頻道之後，仍可從 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁更新 **Scan QR** 設定。

<!-- note end -->

<!-- note start -->

**liff.scanCodeV2() 的運作規格**

`liff.scanCodeV2()` 內部使用名為 [jsQR](https://github.com/cozmo/jsQR) 的外部函式庫。因此，執行 `liff.scanCodeV2()` 方法時所啟動的 2D code 讀取器，取決於 [jsQR](https://github.com/cozmo/jsQR) 的運作規格。所使用的函式庫可能在不另行通知的情況下更新或變更。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
liff
  .scanCodeV2()
  .then((result) => {
    // result = { value: "" }
  })
  .catch((error) => {
    console.log("error", error);
  });
```

<!-- tab end -->

#### Syntax 

```javascript
liff.scanCodeV2();
```

#### Arguments 

None

#### Return value 

回傳一個 `Promise` 物件。

當 2D code 讀取器讀取到字串時，`Promise` 會被 resolve 並傳遞包含字串的物件。

<!-- parameter start -->

value

String

2D code 讀取器掃描到的字串

<!-- parameter end -->

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

### liff.scanCode() 

<!-- note start -->

**liff.scanCode() 方法已淘汰**

傳統的 `liff.scanCode()` 方法已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)。我們建議使用 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法來實作 2D code 讀取器。

<!-- note end -->

<br>

啟動 2D code 讀取器並取得使用者讀取的字串。若要啟動 2D code 讀取器，請在 [LINE Developers Console](https://developers.line.biz/console/) 上開啟 `ScanQR`。

<!-- note start -->

**在 LINE for iOS 上不可用**

`liff.scanCode()` 可在以下環境中運作。

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
      <td>iOS</td>
      <td>All versions</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>Android</td>
      <td>All versions</td>
      <td>✅</td>
      <td>❌</td>
    </tr>
    <tr>
      <td>PC</td>
      <td>All versions</td>
      <td>❌</td>
      <td>❌</td>
    </tr>
  </tbody>
</table>

由於技術問題，`liff.scanCode` 在 LINE for iOS 中為 `undefined`。請如範例程式碼所示，在確認該函式存在後再使用。若要在 LINE for iOS 或外部瀏覽器中使用 2D code 讀取器，請參閱 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2)。

<!-- note end -->

<!-- note start -->

**開啟 [Scan QR] 以啟動 2D code 讀取器**

- [將 LIFF app 加入頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時，請開啟 **Scan QR**。即使在將 LIFF app 加入頻道之後，仍可從 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁更新 **Scan QR** 設定。
- 您無法在外部瀏覽器中使用 `liff.scanCode()`。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
if (liff.scanCode) {
  liff.scanCode().then((result) => {
    // result = { value: "" }
  });
}
```

<!-- tab end -->

#### Syntax 

```javascript
liff.scanCode();
```

#### Arguments 

None

#### Return value 

回傳一個 `Promise` 物件。

當 2D code 讀取器讀取字串時，`Promise` 會被 resolve 並傳遞包含所讀取字串的物件。

<!-- parameter start -->

value

String

2D code 讀取器讀取的字串

<!-- parameter end -->

## Permanent link 

### liff.permanentLink.createUrlBy() 

取得 LIFF app 中任何頁面的永久連結（permanent link）。

永久連結格式：

```
https://liff.line.me/{liffId}/{path}?{query}#{URL fragment}
```

_Example_

<!-- tab start `javascript` -->

```javascript
// For example, if the endpoint URL of the LIFF app
// is https://example.com/path1?q1=v1
// and its LIFF ID is 1234567890-AbcdEfgh
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

liff.permanentLink
  .createUrlBy("https://example.com/")
  .catch((error) => {
  // Error: currentPageUrl must start with endpoint URL of LIFF App.
  console.log(error);
});
```

<!-- tab end -->

#### Syntax 

```javascript
liff.permanentLink.createUrlBy(url);
```

#### Arguments 

<!-- parameter start (props: required) -->

url

String

要取得永久連結的 URL。您可以加入任何查詢參數或 URL 片段。

<!-- parameter end -->

#### Return value 

回傳一個 `Promise` 物件。

當 `Promise` 被 resolve 時，回傳永久連結的字串。

##### Error responsee 

如果要取得永久連結的 URL 並非以 [LINE Developers Console](https://developers.line.biz/console/) 上 **Endpoint URL** 指定的 URL 開頭，`Promise` 會被 reject 並回傳 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

例如，如果要取得永久連結的 URL（例如 `https://example.com/`）位於 **Endpoint URL**（例如 `https://example.com/path1?q1=v1`）之上，`Promise` 會被 reject。

### liff.permanentLink.createUrl() 

<!-- note start -->

**liff.permanentLink.createUrl() 可能在下一個主要版本更新中被淘汰**

由於技術問題，`liff.permanentLink.createUrl()` 可能在下一個主要版本更新中被淘汰。若要取得目前頁面的永久連結，我們建議使用 [`liff.permanentLink.createUrlBy()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by)。

<!-- note end -->

取得目前頁面的永久連結。

永久連結格式：

```
https://liff.line.me/{liffId}/{path}?{query}#{URL fragment}
```

_Example_

<!-- tab start `javascript` -->

```javascript
// For example, if current location is
// /shopping?item_id=99#details
// (LIFF ID = 1234567890-AbcdEfgh)
const myLink = liff.permanentLink.createUrl();

// myLink equals "https://liff.line.me/1234567890-AbcdEfgh/shopping?item_id=99#details"
```

<!-- tab end -->

#### Syntax 

```javascript
liff.permanentLink.createUrl();
```

#### Arguments 

None

#### Return value 

以字串回傳目前頁面的永久連結。

如果目前的頁面 URL 並非以 LINE Developers Console 的 **Endpoint URL** 中指定的 URL 開頭，則會擲出 `LiffError` 例外。

### liff.permanentLink.setExtraQueryParam() 

<!-- note start -->

**liff.permanentLink.setExtraQueryParam() 可能在下一個主要版本更新中被淘汰**

由於技術問題，`liff.permanentLink.setExtraQueryParam()` 可能在下一個主要版本更新中被淘汰。若要在目前頁面的永久連結中加入任何查詢參數，我們建議使用 [`liff.permanentLink.createUrlBy()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by)。

<!-- note end -->

您可以在目前頁面的永久連結中加入任何查詢參數。

每次您執行 `liff.permanentLink.setExtraQueryParam()` 時，上次加入的查詢參數會被覆寫。

<!-- tip start -->

**刪除已加入的查詢參數**

- 若要刪除已加入的查詢參數，請執行 `liff.permanentLink.setExtraQueryParam("")`。
- 當使用者導覽到另一個頁面時，已加入的查詢參數將被捨棄。

<!-- tip end -->

_Example_

<!-- tab start `javascript` -->

```javascript
// For example, if current location is
// /food?menu=pizza
// (LIFF ID = 1234567890-AbcdEfgh)
liff.permanentLink.setExtraQueryParam("user_tracking_id=8888");
const myLink = liff.permanentLink.createUrl();

// myLink equals "https://liff.line.me/1234567890-AbcdEfgh/food?menu=pizza&user_tracking_id=8888"
```

<!-- tab end -->

#### Syntax 

```javascript
liff.permanentLink.setExtraQueryParam(extraString);
```

#### Arguments 

<!-- parameter start (props: required) -->

extraString

String

要加入的查詢參數

<!-- parameter end -->

#### Return value 

None

## LIFF plugin 

### liff.use() 

在[可插拔 SDK（pluggable SDK）](https://developers.line.biz/en/docs/liff/pluggable-sdk/)或 [LIFF plugin](https://developers.line.biz/en/docs/liff/liff-plugin/) 中啟用並初始化 LIFF API。

_Example of LIFF API in the pluggable SDK_

<!-- tab start `javascript` -->

```javascript
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";

liff.use(new GetOS());

liff.init({
  liffId: "123456-abcedfg", // Use own liffId
});
```

<!-- tab end -->

_Example of LIFF plugin_

<!-- tab start `javascript` -->

```javascript
class greetPlugin {
  constructor() {
    this.name = "greet";
  }

  install() {
    return {
      hello: this.hello,
    };
  }

  hello() {
    console.log("Hello, World!");
  }
}

liff.use(new greetPlugin());
```

<!-- tab end -->

#### Syntax 

```javascript
liff.use(module, option);
```

#### Arguments 

<!-- parameter start (props: required) -->

module

Object

可插拔 SDK 中的 LIFF API 模組或 LIFF plugin。

如果您傳遞 LIFF API 模組，您需要將該 LIFF API 模組實例化。詳細資訊請參閱 LIFF 文件中的 [How to use the pluggable SDK](https://developers.line.biz/en/docs/liff/pluggable-sdk/#how-to-use)。

如果您傳遞 LIFF plugin，且該 LIFF plugin 是類別（class），您需要將該 LIFF plugin 實例化。詳細資訊請參閱 LIFF 文件中的 [Using a LIFF plugin](https://developers.line.biz/en/docs/liff/liff-plugin/#use-liff-plugin)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

option

Any value

要傳遞給 `module` 屬性所指定 LIFF plugin 的值。該值會作為 LIFF plugin 的 [`install()`](https://developers.line.biz/en/docs/liff/liff-plugin/#install) 方法的第二個引數傳遞。詳細資訊請參閱 LIFF 文件中的 [option](https://developers.line.biz/en/docs/liff/liff-plugin/#option)。

<!-- parameter end -->

#### Return value 

回傳 `liff` 物件。

## Internationalization 

### liff.i18n.setLang() 

指定 LIFF SDK 顯示文字的語言。

_Example_

<!-- tab start `javascript` -->

```javascript
liff.i18n.setLang("en");
```

<!-- tab end -->

#### Syntax 

```javascript
liff.i18n.setLang(language);
```

#### Arguments 

<!-- parameter start (props: required) -->

language

String

依 [RFC 5646 (BCP 47)](https://datatracker.ietf.org/doc/html/rfc5646) 定義的語言標籤（language tag）。如果指定的語言標籤沒有翻譯，則會使用 `en` 作為後備（fallback）。

<!-- parameter end -->

#### Return value 

回傳一個 `Promise` 物件。

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

## Others 

### liff.createShortcutOnHomeScreen() 

<!-- tip start -->

**此功能僅供已驗證的 MINI App 使用**

此功能僅供已驗證的 MINI App 使用。對於未驗證的 MINI App，您可以在 Developing 用的內部頻道上測試此功能，但無法在 Published 用的內部頻道上使用此功能。

<!-- tip end -->

顯示一個畫面，將您的 [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/) 捷徑加入使用者裝置的主畫面。

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-ios-en.png)

詳細資訊請參閱 LINE MINI App 文件中的 [Add a shortcut to your LINE MINI App to the home screen of the user's device](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)。

<!-- note start -->

**何時執行 liff.createShortcutOnHomeScreen() 方法**

`liff.createShortcutOnHomeScreen()` 方法應在使用者對您的 LINE MINI App 採取動作（例如點擊）時執行，以免破壞使用者體驗。

<!-- note end -->

_Example_

<!-- tab start `javascript` -->

```javascript
// If the endpoint URL of the LINE MINI App
// is https://example.com/path1/path2
// and its LIFF ID is 1234567890-AbcdEfgh

// Example of specifying the LIFF URL
liff
  .createShortcutOnHomeScreen({
    url: "https://miniapp.line.me/1234567890-AbcdEfgh",
  })
  .then(() => { /* ... */ });

liff
  .createShortcutOnHomeScreen({
    url: "https://liff.line.me/1234567890-AbcdEfgh",
  })
  .then(() => { /* ... */ });

// Example of specifying a permanent link
liff
  .createShortcutOnHomeScreen({
    url: "https://liff.line.me/1234567890-AbcdEfgh/path3",
  })
  .then(() => { /* ... */ });

// Example of specifying the endpoint URL of the LINE MINI App
liff
  .createShortcutOnHomeScreen({
    url: "https://example.com/path1/path2",
  })
  .then(() => { /* ... */ });

// Example of specifying a URL that begins with the endpoint URL of the LINE MINI App
liff
  .createShortcutOnHomeScreen({
    url: "https://example.com/path1/path2/path3",
  })
  .then(() => { /* ... */ });

// Example of specifying a URL that results in an error
liff
  .createShortcutOnHomeScreen({
    url: "https://example.com/invalid-path",
  })
  .then(() => { /* ... */ })
  .catch((error) => {
    // invalid URL.
    console.log(error.message);
  });
```

<!-- tab end -->

#### Conditions of use 

若要使用 `liff.createShortcutOnHomeScreen()` 方法，必須滿足以下所有條件：

- 它是 LINE MINI App。
- LINE MINI App 的 LIFF SDK 版本為 v2.23.0 或更新版本。
- 使用者裝置上的 LINE app 版本為 13.20.0 或更新版本。

#### Operating conditions 

如果使用者裝置的 OS 是 iOS，`liff.createShortcutOnHomeScreen()` 方法能正常運作的條件如下。如果在不支援的環境中執行此方法，將顯示錯誤頁面。

| Default browser | iOS version | Whether it works or not |
| --- | --- | --- |
| Safari | 所有版本 | 可運作 |
| Chrome | 16.4 或更新版本 | 可運作 |
| Safari 與 Chrome 以外的瀏覽器 | 16.4 或更新版本 | 不保證可運作 |
| Safari 以外的瀏覽器 | 早於 16.4 | 無法運作 |

例如，如果您在早於 iOS 16.4 的 Chrome 中執行 `liff.createShortcutOnHomeScreen()` 方法，將顯示以下錯誤頁面：

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-ios-error-en.png)

#### Syntax 

```javascript
liff.createShortcutOnHomeScreen(params);
```

#### Arguments 

<!-- parameter start (props: required) -->

params

Object

參數物件

<!-- parameter end -->
<!-- parameter start (props: required) -->

params.url

String

URL。您可以指定以下 URL：

- [LIFF URL](https://developers.line.biz/en/glossary/#liff-url)
- [永久連結（Permanent link）](https://developers.line.biz/en/glossary/#permanent-link-liff)
- LINE MINI App 的端點 URL
- 以 LINE MINI App 端點 URL 開頭的 URL

<!-- parameter end -->

#### Return value 

回傳一個 `Promise` 物件。

當 Add Shortcut 畫面顯示時，`Promise` 會被 resolve。不會傳遞任何值。

您無法確認使用者是否實際將您的 LINE MINI App 捷徑加入使用者裝置的主畫面。

##### Error response 

當 `Promise` 被 reject 時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。
