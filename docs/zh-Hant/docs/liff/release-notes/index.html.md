# 發行說明（Release notes）

## LIFF version and release date

從 LIFF v2.2.0 開始，LIFF 將遵循[語意化版本控制](https://semver.org/)（Semantic Versioning，SemVer）。詳情請參閱 [LIFF versioning policy](https://developers.line.biz/en/docs/liff/versioning-policy/)。

<!-- tip start -->

**CDN 路徑**

我們提供兩種 CDN 路徑：fixed 與 edge。如果你使用 CDN edge 路徑，就會永遠保持在最新的 MINOR 與 PATCH 更新。如果你使用 CDN fixed 路徑，則每次更新時都需要手動更新你的 URL。

詳情請參閱 LIFF versioning policy 文件中的 [LIFF SDK (sdk.js) update policy](https://developers.line.biz/en/docs/liff/versioning-policy/#update-policy)。

<!-- tip end -->

### Current version

當你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`）時，你隨時都能使用 LIFF v2 的最新功能。

[LIFF v2.29.0：2026 年 5 月 13 日](https://developers.line.biz/en/docs/liff/release-notes/#liff-v2-29-0)

### Version list 

當你使用 CDN fixed 路徑（例如 `https://static.line-scdn.net/liff/edge/versions/2.29.0/sdk.js`）時，你可以使用所指定 LIFF 版本的功能。

:toc{maxDepth=2}

2026/05/13

## LIFF v2.29.0 released 

我們已發行 LIFF v2.29.0。

在 LIFF v2.29.0 中，我們變更了 LIFF SDK 的內部行為。功能上沒有變更。

### How to update to LIFF v2.29.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.29.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.29.0` 或 `yarn add @line/liff@2.29.0` 來更新至 v2.29.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2026/03/24

## LIFF v2.28.0 released 

我們已發行 LIFF v2.28.0。

在 LIFF v2.28.0 中，我們做了以下變更。

### We've added the `liff.requestFriendship()` method which prompts the user to add the LINE Official Account as a friend 

我們新增了 [`liff.requestFriendship()`](https://developers.line.biz/en/reference/liff/#request-friendship) 方法，會顯示一個子視窗，提示使用者將 LINE 官方帳號（LINE Official Account）加為好友，或將其解除封鎖。

詳情請參閱 LIFF 文件中的 [Requesting the user to add the LINE Official Account as a friend or unblock it](https://developers.line.biz/en/docs/liff/developing-liff-apps/#request-friendship)。

### How to update to LIFF v2.28.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.28.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.28.0` 或 `yarn add @line/liff@2.28.0` 來更新至 v2.28.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2025/11/17

## LIFF v2.27.3 released 

我們已發行 LIFF v2.27.3。

在 LIFF v2.27.3 中，我們變更了 LIFF SDK 的內部行為。功能上沒有變更。

### How to update to LIFF v2.27.3 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.27.3。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.27.3` 或 `yarn add @line/liff@2.27.3` 來更新至 v2.27.3。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2025/09/08

## LIFF v2.27.2 released 

我們已發行 LIFF v2.27.2。

在 LIFF v2.27.2 中，我們做了以下改善。

### A warning message will now appear in a browser console if the URL of the page where the `liff.init()` method is executed doesn't start with the endpoint URL 

[`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法只會在與端點 URL（endpoint URL）相同的 URL（\*），或在端點 URL 下層的 URL 上運作。因此，如果在其他任何 URL 上執行 `liff.init()` 方法，部分 LIFF app 功能（例如[多分頁檢視（multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)）可能無法正常運作。

為了幫助開發者更容易辨識這個問題，現在如果執行 `liff.init()` 方法的頁面 URL 不是以端點 URL 開頭，主控台（console）就會出現警告訊息。

例如，如果某 LIFF app 的端點 URL 為 `https://example.com/path1/path2/`，而執行 `liff.init()` 方法的 URL 為 `https://example.com/path1/`，就會出現以下警告訊息：

```
liff.init() was called with a current URL that is not related to the endpoint URL.
https://example.com/path1/ is not under https://example.com/path1/path2/
```

如果你看到上述警告訊息，請考慮將端點 URL 變更為 `https://example.com/` 或 `https://example.com/path1/`。變更為這些 URL 可確保 `liff.init()` 方法正常運作。

\* 在 LINE Developers Console 的 **Endpoint URL** 中所指定的 URL。

### How to update to LIFF v2.27.2 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.27.2。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.27.2` 或 `yarn add @line/liff@2.27.2` 來更新至 v2.27.2。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2025/07/24

## LIFF v2.27.1 released 

我們已發行 LIFF v2.27.1。

在 LIFF v2.27.1 中，我們變更了 LIFF SDK 的內部行為。功能上沒有變更。

### How to update to LIFF v2.27.1 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.27.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.27.1` 或 `yarn add @line/liff@2.27.1` 來更新至 v2.27.1。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2025/6/25

## LIFF v2.27.0 released 

我們已發行 LIFF v2.27.0。

在 LIFF v2.27.0 中，我們新增了以下功能。

### You can now get a list of scopes for which the user has agreed to grant permission 

我們在 LIFF SDK 中新增了 [`liff.permission.getGrantedAll()`](https://developers.line.biz/en/reference/liff/#permission-get-granted-all) 方法。使用 `liff.permission.getGrantedAll()` 方法可以取得使用者已同意授予權限的所有範圍（scope）。

```javascript
liff.permission.getGrantedAll().then((scopes) => {
  // ["profile", "chat_message.write", "openid", "email"]
  console.log(scopes);
});
```

你可以透過此方法取得的範圍如下：

- [`profile`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`chat_message.write`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`openid`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)
- [`email`](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)

<!-- tip start -->

**liff.getContext() 與 liff.permission.getGrantedAll() 的差異**

[`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法會取得該 LIFF app 的範圍清單（\*）。

另一方面，`liff.permission.getGrantedAll()` 方法則會在該 LIFF app 的範圍中，取得使用者已同意授予權限的範圍清單。

\* 在 LINE Login 頻道（channel）中 **LIFF** 分頁下「Scope」區段所指定的範圍

<!-- tip end -->

詳情請參閱 LIFF API reference 中的 [liff.permission.getGrantedAll()](https://developers.line.biz/en/reference/liff/#permission-get-granted-all)。

### How to update to LIFF v2.27.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.27.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.27.0` 或 `yarn add @line/liff@2.27.0` 來更新至 v2.27.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2025/5/26

## LIFF v2.26.1 released 

我們已發行 LIFF v2.26.1。

在 LIFF v2.26.1 中，我們修正了以下錯誤。

### We've fixed a bug where accessing a LIFF URL caused the LIFF app to navigate to an unintended secondary redirect URL 

在 LIFF app 中，存取 [LIFF URL](https://developers.line.biz/en/glossary/#liff-url) 時，LIFF app 會先導向主要重新導向 URL（primary redirect URL），再導向次要重新導向 URL（secondary redirect URL）。在次要重新導向 URL 路徑結尾附加斜線（`/`）的條件中曾有一個錯誤，導致 LIFF app 導向非預期的次要重新導向 URL。

#### Conditions that append a slash (`/`) to the end of the path of the secondary redirect URL 

在 LIFF v2.26.0 或更早版本中，若符合以下任一條件，就會在次要重新導向 URL 路徑的結尾附加斜線（`/`）：

- 端點 URL 以斜線（`/`）結尾
- `liff.state` 以斜線（`/`）結尾

例如，如果 LIFF app 的端點 URL 為 `https://example.com/?key=value/`，而存取的 LIFF URL 為 `https://liff.line.me/1234567890-AbcdEfgh/foo/bar`，正確的次要重新導向 URL 應為 `https://example.com/foo/bar?key=value/`。

然而，由於在此情況下符合「端點 URL 以斜線（`/`）結尾」這個條件，LIFF app 實際上會導向 `https://example.com/foo/bar/?key=value/`，路徑結尾多了一個斜線（`/`）。

| Correct secondary redirect URL | Actual secondary redirect URL |
| --- | --- |
| https://example.com/foo/bar?key=value/ | https://example.com/foo/bar<b style="color: red">/</b>?key=value/ |

在 LIFF v2.26.1 中，我們套用了修正，使得只有在符合以下任一條件時，才會在次要重新導向 URL 結尾附加斜線（`/`）。因此，LIFF app 現在會導向正確的次要重新導向 URL。

- 端點 URL 的路徑以斜線（`/`）結尾
- `liff.state` 的路徑以斜線（`/`）結尾

關於存取 LIFF URL 時的行為詳情，請參閱 LIFF 文件中的 [Behaviors from accessing the LIFF URL to opening the LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

### We've fixed a bug where the `liff.init()` method replaced POST requests with GET requests in the browser's session history when excluding credential information 

在 LIFF app 中，當 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法解析（resolve）時，會從 URL 中排除存取權杖（access token）等憑證資訊（credential information）。此時，在某些環境中曾有一個錯誤，導致瀏覽器的工作階段歷史記錄（session history）中的 POST 請求被替換為 GET 請求。

在 LIFF v2.26.1 中，我們修正了這個錯誤，使其保留正確的歷史記錄。

#### Example of a POST request in the browser's session history being replaced by a GET request 

例如，假設你依以下順序操作 LIFF app：

1. 開啟一個 LIFF app
1. 以 POST 請求導向 `/path1`
1. 以 GET 請求導向 `/path2`
1. 點擊瀏覽器的返回按鈕

在此情況下，預期 LIFF app 應以 POST 請求導向 `/path1`，但在某些環境中，LIFF app 卻以 GET 請求導向 `/path1`。

### How to update to LIFF v2.26.1 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.26.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.26.1` 或 `yarn add @line/liff@2.26.1` 來更新至 v2.26.1。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2025/4/22

## LIFF v2.26.0 released 

我們已發行 LIFF v2.26.0。

在 LIFF v2.26.0 中，我們修正了以下錯誤。

### We've fixed a bug where an incorrect error message was returned when a certain method is executed in an external browser while not logged in 

曾有一個錯誤：在使用者未登入的情況下，於[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中執行以下方法時，會回傳不正確的錯誤訊息。

- [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 方法
- [`liff.getFriendship()`](https://developers.line.biz/en/reference/liff/#get-friendship) 方法
- [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 方法

在 LIFF v2.26.0 中，我們修正了這個錯誤，使其回傳正確的錯誤訊息。

| Error message before the fix | Error message after the fix |
| --- | --- |
| `LiffId is not found.` | `Need access_token for api call, Please login first` |

### How to update to LIFF v2.26.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.26.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.26.0` 或 `yarn add @line/liff@2.26.0` 來更新至 v2.26.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2024/12/13

## LIFF v2.25.1 released 

我們已發行 LIFF v2.25.1。

在 LIFF v2.25.1 中，我們變更了 LIFF SDK 的內部行為。功能上沒有變更。

### How to update to LIFF v2.25.1 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.25.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.25.1` 或 `yarn add @line/liff@2.25.1` 來更新至 v2.25.1。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2024/11/12

## LIFF v2.25.0 released 

我們已發行 LIFF v2.25.0。

在 LIFF v2.25.0 中，我們做了以下變更。

### We've changed the URLs generated by the `liff.permanentLink.createUrlBy()` method

如同 [2024 年 11 月 11 日](https://developers.line.biz/en/news/2024/11/11/liff-server-update/)所公告，我們對 LIFF 伺服器端進行了變更，以確保 URL 處理符合 [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)。因此，[`liff.permanentLink.createUrlBy()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by) 方法所產生的 URL 中，查詢字串（query）內字元與編碼的處理結果變更如下：

| Characters and codes | Before change | After change (current) |
| -------------------- | ------------- | ---------------------- |
| `+`                  | `+`           | `%2B`                  |
| `*`                  | `*`           | `%2A`                  |
| `%7E`                | `%7E`         | `~`                    |
| `%20`                | `+`           | `%20`                  |
| `;` \*               | Deleted       | `%3B`                  |

\* `;` 的處理結果僅在 `;` 位於查詢字串結尾時才會套用。

詳情請參閱 [As of November 11, 2024, the results of URLs generated by some LIFF features changed in certain versions of the LINE app and LIFF SDK](https://developers.line.biz/en/news/2024/11/11/liff-server-update/)。

### How to update to LIFF v2.25.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.25.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.25.0` 或 `yarn add @line/liff@2.25.0` 來更新至 v2.25.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2024/7/23

## LIFF v2.24.0 released 

我們已發行 LIFF v2.24.0。

在 LIFF v2.24.0 中，我們新增了以下功能。

### We've added the `liff.getAppLanguage()` method which gets the language setting of the LINE app running the LIFF app 

我們新增了 [`liff.getAppLanguage()`](https://developers.line.biz/en/reference/liff/#get-app-language) 方法，可取得執行該 LIFF app 的 LINE app 語言設定。

LIFF SDK 有一個類似的方法 [`liff.getLanguage()`](https://developers.line.biz/en/reference/liff/#get-language)。你可以使用 `liff.getLanguage()` 方法取得執行該 LIFF app 環境的語言設定，但在某些 iOS 環境中有一個錯誤，會反映 OS 的語言設定，而非 LINE app 的語言設定。

因此，隨著 `liff.getAppLanguage()` 方法的新增，`liff.getLanguage()` 方法已被棄用（deprecated）。請從今以後改用 `liff.getAppLanguage()` 方法。

關於 LINE app 語言設定的詳情，請參閱 Help Center 中的 [Changing the LINE app language setting](https://help.line.me/line/?contentId=20007465&lang=en)。

### How to update to LIFF v2.24.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.24.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.24.0` 或 `yarn add @line/liff@2.24.0` 來更新至 v2.24.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2024/2/15

## LIFF v2.23.2 released 

我們已發行 LIFF v2.23.2。

在 LIFF v2.23.2 中，我們做了以下改善與一項錯誤修正。

### The cause of the LIFF SDK loading failures can now be checked in a log and `LiffError` 

當 LIFF SDK 載入失敗時，現在可以在主控台記錄（console log）中，或在 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors) 物件的 `cause` 屬性中查看失敗原因。

### We've fixed a bug that caused some parameters of the URL fragment to be unintentionally removed when initializing a LIFF app 

在 LIFF app 中，基於安全因素，會在 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法解析時，從[主要重新導向 URL](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow) 的 URL 片段（URL fragment）中移除以下以字串為鍵（key）的參數。

- `access_token`
- `client_id`
- `context_token`
- `feature_token`
- `id_token`

曾有一個錯誤，導致鍵為以這些字串結尾之字串（例如 `prefix_access_token`）的參數被非預期地從 URL 片段中移除。在 v2.23.2 中，我們修正了這個錯誤，使其只移除以上述字串為鍵的參數。

### How to update to LIFF v2.23.2 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.23.2。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.23.2` 或 `yarn add @line/liff@2.23.2` 來更新至 v2.23.2。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2024/1/15

## LIFF v2.23.1 released 

<!-- note start -->

**2024 年 1 月 23 日更新**

由於一個錯誤導致部分裝置上 2D 條碼的讀取準確度下降，[`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法已還原至本次發行前的狀態。你無需更新 LIFF SDK 或修改 LIFF app 中的程式碼。對於造成的不便，我們深表歉意。

<!-- note end -->

我們已發行 LIFF v2.23.1。

在 LIFF v2.23.1 中，我們做了以下改善。同時，我們也變更了 LIFF SDK 的內部行為以提升安全性。

### We've improved the reading accuracy of the `liff.scanCodeV2()` method 

我們改善了 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法的 2D 條碼讀取準確度。請注意，讀取準確度取決於裝置的相機效能，因此視使用者的裝置而定，可能不會有明顯的改善。

此項改善會自動套用到所有 LIFF app，因此你無需更新 LIFF SDK 或修改 LIFF app 中的程式碼。

### How to update to LIFF v2.23.1 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.23.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.23.1` 或 `yarn add @line/liff@2.23.1` 來更新至 v2.23.1。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2023/11/30

## LIFF v2.23.0 released 

我們已發行 LIFF v2.23.0。

在 LIFF v2.23.0 中，我們變更了 LIFF SDK 的內部行為。功能上沒有變更。

### How to update to LIFF v2.23.0 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.23.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.23.0` 或 `yarn add @line/liff@2.23.0` 來更新至 v2.23.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2023/10/2

## LIFF v2.22.4 released 

我們已發行 LIFF v2.22.4。

在 LIFF v2.22.4 中，我們變更了 LIFF SDK 的內部行為。同時也做了以下變更與修正。

### Due to the intra-group reorganization, we've changed the company name and copyright of the LIFF SDK and open source projects 

如同 [2023 年 10 月 2 日](https://developers.line.biz/en/news/2023/10/02/merger-announcement/)所公告，由於集團內部重組，LINE Corporation 已成為 LY Corporation。隨之，我們變更了 LIFF SDK 及以下開源專案的公司名稱與版權：

- [LIFF starter app](https://github.com/line/line-liff-v2-starter)
- [LIFF Playground](https://github.com/line/liff-playground)
- [Create LIFF App](https://github.com/line/create-liff-app)
- [LIFF Inspector](https://github.com/line/liff-inspector)
- [LIFF Mock](https://github.com/line/liff-mock)

### We've fixed a bug where an error might not be returned correctly when the `liff.permission.requestAll()` method failed to execute 

曾有一個錯誤：當 [`liff.permission.requestAll()`](https://developers.line.biz/en/reference/liff/#permission-request-all) 方法執行失敗時，可能無法正確回傳錯誤。在 LIFF v2.22.4 中已修正此錯誤，使其能正確回傳錯誤。

### How to update to LIFF v2.22.4 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.22.4。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.22.4` 或 `yarn add @line/liff@2.22.4` 來更新至 v2.22.4。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2023/8/24

## LIFF v2.22.3 released 

我們已發行 LIFF v2.22.3。

在 LIFF v2.22.3 中，我們變更了 LIFF SDK 的內部行為。功能上沒有變更。

### How to update to LIFF v2.22.3 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.22.3。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.22.3` 或 `yarn add @line/liff@2.22.3` 來更新至 v2.22.3。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2023/6/27

## LIFF v2.22.2 released 

我們已發行 LIFF v2.22.2。

在 LIFF v2.22.2 中，我們做了以下改善與一項錯誤修正。

### We've improved the auto login process on external browsers on Android 

如同 [2022 年 7 月 6 日](https://developers.line.biz/en/news/2022/07/06/release-liff-2-20-3/#android-external-browser-20220706)所公告，從 LIFF v2.20.3 開始，作為解決 Android [外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)上[自動登入（auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)無法正常運作之錯誤的暫時措施，會在自動登入後顯示提示訊息。

在 LINE for Android 版本 13.10.0 中，外部瀏覽器上的自動登入流程將獲得改善，因此不再需要該暫時措施。所以，在 LIFF v2.22.2 或更新版本中，自動登入後顯示的提示訊息將不再顯示。

請注意，即使你 LIFF app 的 LIFF SDK 版本為 v2.22.2 或更新版本，如果使用者的 LINE for Android 版本早於 13.10.0，提示訊息仍會持續顯示。

<table>
  <thead>
    <tr>
      <th></th>
      <th>LIFF v2.20.3 - v2.22.1</th>
      <th>LIFF v2.22.2 or later</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>LINE for Android version earlier than 13.10.0</th>
      <td>Display the alert</td>
      <td>Display the alert</td>
    </tr>
    <tr>
      <th>LINE for Android version 13.10.0 or later</th>
      <td>Display the alert</td>
      <td>Not display the alert</td>
    </tr>
  </tbody>
</table>

### The LIFF SDK npm package can now be imported in non-browser environments 

LIFF SDK npm 套件現在可以在 Node.js 等非瀏覽器環境中匯入（import）。

### We've fixed a bug where an invalid URL would be opened after login when executing the `liff.login()` method with a URL with no query parameter specified in the redirectUri property on external browsers on Android 

在 Android 的外部瀏覽器上，當執行 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 方法且 `redirectUri` 屬性中指定的 URL 未含查詢參數（query parameter）時，登入後會開啟一個無效的 URL。

此錯誤已在 LIFF v2.22.2 中修正，使其在登入後開啟正確的 URL。

<table>
  <tbody>
    <tr>
      <th>Example of a URL specified in the <code>redirectUri</code> property</th>
      <td><code>https://example.com/path</code></td>
    </tr>
    <tr>
      <th>Example of an invalid URL opened after login</th>
      <td><code>https://example.com/path&liffIsEscapedFromApp=true</code></td>
    </tr>
    <tr>
      <th>Example of the correct URL after login</th>
      <td><code>https://example.com/path?liffIsEscapedFromApp=true</code></td>
    </tr>
  </tbody>
</table>

### How to update to LIFF v2.22.2 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.22.2。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.22.2` 或 `yarn add @line/liff@2.22.2` 來更新至 v2.22.2。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2023/5/24

## LIFF v2.22.1 released 

我們已發行 LIFF v2.22.1。

在 LIFF v2.22.1 中，我們重構了 LIFF SDK。同時也做了以下修正。

### We've fixed the TypeScript type definitions for LIFF API modules in the pluggable SDK 

我們修正了 [pluggable SDK](https://developers.line.biz/en/docs/liff/pluggable-sdk/) 中 LIFF API 模組的 TypeScript 型別定義。

修正了 TypeScript 型別定義的 LIFF API 模組及詳情如下：

| LIFF API module | Detail |
| --- | --- |
| `@line/liff/get-id-token` | 將 `getIdToken` 修正為 `getIDToken`。 |
| `@line/liff/get-decoded-id-token` | 將 `getDecodedIdToken` 修正為 `getDecodedIDToken`。 |

### How to update to LIFF v2.22.1 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.22.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.22.1` 或 `yarn add @line/liff@2.22.1` 來更新至 v2.22.1。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2023/3/29

## LIFF v2.22.0 released 

我們已發行 LIFF v2.22.0。

在 LIFF v2.22.0 中，新增了以下功能。

### We've added the pluggable SDK feature that can reduce the LIFF SDK file size by up to about 34% 

在 LIFF SDK 的 npm 套件中，我們新增了 pluggable SDK 功能，讓你可以選擇要在 LIFF SDK 中包含哪些 LIFF API。

只包含你 LIFF app 所使用的 LIFF API，最多可將 LIFF SDK 檔案大小縮減約 34%。因此，你可以提升 LIFF app 的顯示速度。

#### How to use the pluggable SDK 

首先，從 `@line/liff/core` 匯入 `liff` 物件。請注意，這與匯入 `liff` 物件的傳統來源 `@line/liff` 不同。

```js
import liff from "@line/liff/core";
```

這個 `liff` 物件與傳統的 `liff` 物件不同之處在於，它只包含以下屬性與方法：

- [`liff.id`](https://developers.line.biz/en/reference/liff/#id) 屬性
- [`liff.ready`](https://developers.line.biz/en/reference/liff/#ready) 屬性
- [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法
- [`liff.getVersion()`](https://developers.line.biz/en/reference/liff/#get-version) 方法
- [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法

若要使用上述以外的 LIFF API，請匯入對應的模組。在以下範例中，為 [`liff.getOS()`](https://developers.line.biz/en/reference/liff/#get-os) 方法與 [`liff.getLanguage()`](https://developers.line.biz/en/reference/liff/#get-language) 方法匯入了對應的模組：

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";
import GetLanguage from "@line/liff/get-language";
```

接著，將匯入的 LIFF API 模組傳給 `liff.use()` 方法以啟用這些 LIFF API。由於 LIFF API 模組是以類別（class）定義，你需要將實例（instance）傳給 `liff.use()` 方法。

一旦 LIFF API 被啟用，你就可以使用這些 LIFF API。

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";
import GetLanguage from "@line/liff/get-language";

liff.use(new GetOS());
liff.use(new GetLanguage());

liff.init({
  liffId: "123456-abcedfg",
});

liff.getOS();
liff.getLanguage();
```

關於 pluggable SDK 的詳情，請參閱 LIFF 文件中的 [Pluggable SDK](https://developers.line.biz/en/docs/liff/pluggable-sdk/)。

<!-- tip start -->

**使用傳統的 LIFF SDK**

你可以使用傳統的 LIFF SDK。使用 LIFF SDK 的方式沒有變更。

```js
// The conventional liff object
import liff from "@line/liff";

// The liff object in the pluggable SDK
import liff from "@line/liff/core";
```

<!-- tip end -->

2022/12/13

## LIFF v2.21.4 released 

我們已發行 LIFF v2.21.4。

### We've officially released the LIFF SDK npm package 

我們正式發行了 LIFF SDK npm 套件，此套件自 [2020 年 7 月](https://developers.line.biz/en/news/2020/07/01/published-liff-npm-package/)起即以試用形式提供。

早於 v2.21.4 的 LIFF SDK npm 套件仍如以往一樣可用。使用方式沒有變更。

關於 LIFF SDK npm 套件的詳情，請參閱 LIFF 文件中的 [Use the npm package](https://developers.line.biz/en/docs/liff/developing-liff-apps/#use-npm-package)。

### How to update to LIFF v2.21.4 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.21.4。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.21.4` 或 `yarn add @line/liff@2.21.4` 來更新至 v2.21.4。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/11/10

## LIFF v2.21.3 released 

我們已發行 LIFF v2.21.3。

在 LIFF v2.21.3 中，我們修正了以下錯誤。

### We've fixed a bug where an error would occur when importing the npm package of the LIFF SDK as an ES module 

曾有一個錯誤：當以 ES module 形式匯入 LIFF SDK 的 npm 套件時，會發生 `Uncaught ReferenceError: require is not defined` 錯誤。

此錯誤已在 LIFF v2.21.3 中修正，使其即使在上述情況下也不會發生錯誤。

### How to update to LIFF v2.21.3 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.21.3。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.21.3` 或 `yarn add @line/liff@2.21.3` 來更新至 v2.21.3。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/10/12

## LIFF v2.21.2 released 

我們已發行 LIFF v2.21.2。

在 LIFF v2.21.2 中，我們重構了 LIFF SDK 以提升 LIFF SDK 的穩定性。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.21.2。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.21.2` 或 `yarn add @line/liff@2.21.2` 來更新至 v2.21.2。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/9/5

## LIFF v2.21.1 released 

我們已發行 LIFF v2.21.1。

在 LIFF v2.21.1 中，我們重構了 LIFF SDK。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.21.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.21.1` 或 `yarn add @line/liff@2.21.1` 來更新至 v2.21.1。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/8/4

## LIFF v2.21.0 released 

我們已發行 LIFF v2.21.0。

在 LIFF v2.21.0 中，我們新增並改善了以下功能：

- [The text displayed by the LIFF SDK now supports multiple languages](https://developers.line.biz/en/docs/liff/release-notes/#i18n-20220804)
- [The language of the text displayed by the LIFF SDK can now be specified](https://developers.line.biz/en/docs/liff/release-notes/#liff-i18n-setLang-20220804)
- [We've fixed a bug where the `liff.init()` method could succeed with an invalid LIFF ID](https://developers.line.biz/en/docs/liff/release-notes/#liff-init-20220804)
- [The Typescript type definition for profile information retrieved by the `liff.getProfile()` method is now available](https://developers.line.biz/en/docs/liff/release-notes/#liff-get-profile-20220804)

### The text displayed by the LIFF SDK now supports multiple languages 

LIFF SDK 顯示的文字現在支援多種語言。這表示 LIFF SDK 顯示的每段文字，都會以從 [`navigator.language`](https://developer.mozilla.org/en-US/docs/Web/API/Navigator/language) 取得的使用者語言顯示。

不過，目前尚未套用任何翻譯，因此所有文字都會以英文顯示。翻譯將會逐步套用。

### The language of the text displayed by the LIFF SDK can now be specified 

我們新增了 [`liff.i18n.setLang()`](https://developers.line.biz/en/reference/liff/#i18n-set-lang) 方法，透過它你可以指定 LIFF SDK 顯示文字的語言。使用 `liff.i18n.setLang()` 方法，LIFF SDK 的文字會以指定的語言顯示，無論使用者的語言為何。

```js
liff.i18n.setLang("en");
```

尚無翻譯的文字不受此方法影響。

詳情請參閱 LIFF API reference 中的 [liff.i18n.setLang()](https://developers.line.biz/en/reference/liff/#i18n-set-lang)。

### We've fixed a bug where the `liff.init()` method could succeed with an invalid LIFF ID 

曾有一個錯誤：[`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 可能在 LIFF ID 無效的情況下仍成功。在 LIFF v2.21.0 中，此錯誤已修正，使得 `liff.init()` 方法在 LIFF ID 無效時會失敗。

### The Typescript type definition for profile information retrieved by the `liff.getProfile()` method is now available 

在 LIFF SDK 的 npm 套件中，現在可以使用透過 `liff.getProfile()` 方法取得的[個人檔案資訊（profile information）](https://developers.line.biz/en/glossary/#profile-information)的 Typescript 型別定義。你可以從 `@liff/get-profile` 套件匯入 `Profile` 型別。

```ts
import { Profile } from "@liff/get-profile";
```

2022/7/6

## LIFF v2.20.3 released 

我們已發行 LIFF v2.20.3。

在 LIFF v2.20.3 中，我們修正了以下錯誤。

### An alert is now displayed after auto login as a temporary measure to solve a bug that auto login on external browsers on Android doesn't work properly 

曾有 Android [外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)上自動登入無法正常運作的情況。作為暫時措施，現在會在 Android 外部瀏覽器上自動登入後顯示以下提示訊息：

```
Login successfully!
```

我們計畫在未來的 LIFF SDK 更新中改善此提示訊息的顯示。

### How to update to LIFF v2.20.3 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.20.3。

如果你使用 npm 套件，請執行 `npm install @line/liff@2.20.3` 或 `yarn add @line/liff@2.20.3` 來更新至 v2.20.3。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/6/8

## LIFF v2.20.2 released 

我們已發行 LIFF v2.20.2。

在 LIFF v2.20.2 中，我們做了內部改善。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.20.2。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.20.2` 或 `yarn add @line/liff@2.20.2` 來更新至 v2.20.2。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/5/24

## LIFF v2.20.1 released 

<!-- note start -->

**2022 年 5 月 25 日新增**

由於 npm 端的錯誤，導致 LIFF v2.20.1 的 npm 套件無法安裝的問題已解決。

詳情請參閱 [the npm status page](https://status.npmjs.org/incidents/4zkt80fxq1nb)。

<!-- note end -->

我們已發行 LIFF v2.20.1。

在 LIFF v2.20.1 中，我們做了以下改善。

### An error is now returned when executing the liff.scanCodeV2() method in an external browser without login 

要執行 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法，需要使用者登入。

在 LIFF v2.19.1 或更早版本中，在未登入的情況下於[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中執行 `liff.scanCodeV2()` 方法時，會開啟一個子視窗並顯示空白頁面。此外，`Promise` 會維持在 pending 狀態。

在 LIFF 2.20.1 中，上述情況下子視窗將不再開啟。此外，`Promise` 會被 reject 並傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

關於 `liff.scanCodeV2()` 方法的詳情，請參閱 LIFF API reference 中的 [liff.scanCodeV2()](https://developers.line.biz/en/reference/liff/#scan-code-v2)。

<!-- note start -->

**LIFF v2.20.0 已被棄用**

由於一個錯誤導致部分使用 Android 外部瀏覽器的使用者無法登入，LIFF v2.20.0 已被[棄用（deprecated）](https://developers.line.biz/en/glossary/#deprecated)。如果你正在使用 LIFF v2.20.0，請更新至 LIFF v2.20.1。

<!-- note end -->

2022/4/18

## LIFF v2.19.1 released 

<!-- note start -->

** 2022 年 4 月 25 日新增**

如先前所公告，我們今天發行了 LIFF Inspector 與 LIFF Mock。詳情請參閱 2022 年 4 月 25 日的消息 [LIFF Inspector and LIFF Mock released](https://developers.line.biz/en/news/2022/04/25/liff-plugin/)。

<!-- note end -->

我們已發行 LIFF v2.19.1。

在 LIFF v2.19.1 中，新增了以下功能。

### We've added the LIFF plugin feature that can extend the LIFF SDK 

我們新增了在去年 11 月舉辦的 LINE DEVELOPER DAY 2021 中，於「[For Improvement of Developer Experience of All LIFF App Developers](https://linedevday.linecorp.com/2021/en/sessions/142/)」議程所介紹的 LIFF plugin 功能。

LIFF plugin 是用於擴充 LIFF SDK 的功能。使用 LIFF plugin，你可以為 LIFF SDK 新增自己的 API，或變更 LIFF API 的行為。

此外，如先前所公告，以下 LIFF plugin 現已可用：

- [LIFF Inspector](https://developers.line.biz/en/docs/liff/release-notes/#liff-inspector-20220418)
- [LIFF Mock](https://developers.line.biz/en/docs/liff/release-notes/#liff-mock-20220418)

#### LIFF Inspector 

LIFF Inspector 是用於除錯（debug）你 LIFF app 的 LIFF plugin。使用 LIFF Inspector，你可以在與執行 LIFF app 的裝置不同的另一台 PC 上，使用 [Chrome DevTools](https://developer.chrome.com/docs/devtools/) 來為你的 LIFF app 除錯。

#### LIFF Mock 

LIFF Mock 是讓測試你 LIFF app 變得容易的 LIFF plugin。使用 LIFF Mock，你可以為 LIFF SDK 新增 mock 模式。在 mock 模式中，你的 LIFF app 獨立於 LIFF 伺服器之外，且 LIFF API 會回傳 mock 資料。因此，你可以更輕鬆地執行單元測試或負載測試。

關於 LIFF plugin 的詳情，請參閱 LIFF 文件中的 [LIFF plugin](https://developers.line.biz/en/docs/liff/liff-plugin/)。

2022/3/22

## LIFF v2.19.0 released 

我們已發行 LIFF v2.19.0。

在 LIFF v2.19.0 中，我們做了內部改善。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.19.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.19.0` 或 `yarn add @line/liff@2.19.0` 來更新至 v2.19.0。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2022/2/14

## LIFF v2.18.2 released 

我們已發行 LIFF v2.18.2。

在 LIFF v2.18.2 中，做了以下改善：

- [An alert to encourage users to update LINE will be displayed on LINE for iOS or iPadOS version 12.0.0](https://developers.line.biz/en/docs/liff/release-notes/#liff-send-messages-2022-02-14)
- [We've fixed a bug where scanning a 2D code encoded in UTF-8 with the liff.scanCodeV2() method would cause character corruption](https://developers.line.biz/en/docs/liff/release-notes/#scan-code-v2-2022-02-14)
- [We've fixed a bug where the correct permanent link couldn't be obtained when passing a URL containing a percent-encoded path to the liff.permanentLink.createUrlBy() method](https://developers.line.biz/en/docs/liff/release-notes/#permanent-link-create-url-by-2022-02-14)

### An alert to encourage users to update LINE will be displayed on LINE for iOS or iPadOS version 12.0.0 

如同 [2022 年 1 月 14 日](https://developers.line.biz/en/news/2022/01/14/liff-outage/)所公告，曾有一個錯誤：在特定條件下，[`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 無法正常運作並回傳狀態碼 `403` 的錯誤。將使用者的 LINE 版本更新至 12.0.1 或更新版本即可解決此錯誤。

為了鼓勵使用者更新至已修正的 LINE 版本，當在 LINE for iOS 或 iPadOS 版本 12.0.0 上執行 `liff.sendMessages()` 方法發生狀態碼 `403` 的錯誤時，將會顯示提示訊息。

將顯示的提示訊息如下：

![LINEアプリをLINE 12.0.1以降にアップデートしてください。Please update your LINE app to LINE 12.0.1 or later.](https://developers.line.biz/media/news/liff-send-messages-v2-18-2.png)

### We've fixed a bug where scanning a 2D code encoded in UTF-8 with the liff.scanCodeV2() method would cause character corruption 

我們修正了一個錯誤：使用 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法掃描以 UTF-8 編碼的 2D 條碼時會造成亂碼。

此錯誤修正會自動套用到所有 LIFF app，因此你無需更新 LIFF SDK 或修改 LIFF app 中的程式碼。

### We've fixed a bug where the correct permanent link couldn't be obtained when passing a URL containing a percent-encoded path to the liff.permanentLink.createUrlBy() method 

我們修正了一個錯誤：將含有[百分比編碼（percent-encoded）](https://en.wikipedia.org/wiki/Percent-encoding)路徑的 URL 傳給 [`liff.permanentLink.createUrlBy()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by) 方法時，會回傳不正確的永久連結（permanent link）或造成狀態碼 `500` 的錯誤。

此錯誤修正會自動套用到所有 LIFF app，因此你無需更新 LIFF SDK 或修改 LIFF app 中的程式碼。

### How to update to LIFF v2.18.2 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），LIFF 會自動更新至 v2.18.2。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.18.2` 或 `yarn add @line/liff@2.18.2` 來更新至 v2.18.2。

關於整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/12/21

## LIFF v2.18.1 released 

我們已發行 LIFF v2.18.1。

在 LIFF v2.18.1 中，修正了以下錯誤。

### Fixed a bug in TypeScript that caused an error when building 

我們修正了 LIFF v2.18.0 中的一個錯誤：使用 TypeScript 建置（build）在 [Message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中含有 [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action) 的程式碼時會造成錯誤。

#### Target methods 

- [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages)
- [`liff.shareTargetPicker()`](https://developers.line.biz/en/reference/liff/#share-target-picker)

### How to update to LIFF v2.18.1

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），你將自動更新至 v2.18.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.18.1` 或 `yarn add @line/liff@2.18.1` 來更新至 v2.18.1。

關於整合 LIFF SDK 的詳情，請參閱 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/12/9

## LIFF v2.18.0 released 

我們已發行 LIFF v2.18.0。

在 LIFF v2.18.0 中，新增了以下功能。

### It's now possible to get the permanent link of any page in the LIFF app 

我們新增了 [`liff.permanentLink.createUrlBy()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by) 方法，透過它你可以取得 LIFF app 中任何頁面的永久連結（permanent link）。

使用 [`liff.permanentLink.createUrl()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url) 方法時，你只能取得目前頁面的永久連結。但使用 `liff.permanentLink.createUrlBy()` 方法時，除了目前頁面之外，你還可以取得 LIFF app 中任何頁面的永久連結。

此外，使用 `liff.permanentLink.createUrl()` 方法時，若要取得已附加查詢參數的永久連結，你需要事先執行 [`liff.permanentLink.setExtraQueryParam()`](https://developers.line.biz/en/reference/liff/#permanent-linke-set-extra-query-param) 方法。但使用 `liff.permanentLink.createUrlBy()` 方法時，你可以在執行該方法的同時指定想附加的查詢參數。此外，`liff.permanentLink.createUrlBy()` 方法不受 `liff.permanentLink.setExtraQueryParam()` 方法影響。

#### Difference between `liff.permanentLink.createUrl()` method and `liff.permanentLink.createUrlBy()` method 

||`liff.permanentLink.createUrl()`|`liff.permanentLink.createUrlBy()`|
|---|---|---|
|可取得永久連結的 LIFF app 頁面|目前頁面|任何頁面|
|如何為永久連結附加任意查詢參數|事先執行 `liff.permanentLink.setExtraQueryParam()` 方法|在執行 `liff.permanentLink.createUrlBy()` 方法時指定|
|回傳值|String|`Promise` 物件|

#### Sample code of the `liff.permanentLink.createUrlBy()` method 

```javascript
// For example, if the endpoint URL of the LIFF app is https://example.com/path1?q1=v1
// and its LIFF ID is 1234567890-AbcdEfgh
liff.permanentLink
  .createUrlBy('https://example.com/path1?q1=v1')
  .then((permanentLink) => {
    // https://liff.line.me/1234567890-AbcdEfgh
    console.log(permanentLink);
  });

liff.permanentLink
  .createUrlBy('https://example.com/path1/path2?q1=v1&q2=v2')
  .then((permanentLink) => {
    // https://liff.line.me/1234567890-AbcdEfgh/path2?q=2=v2
    console.log(permanentLink);
  });
```

<!-- note start -->

**liff.permanentLink.createUrl() 方法可能在下一個主要版本更新中被棄用**

由於技術問題，`liff.permanentLink.createUrl()` 方法可能在下一個主要版本更新中被棄用。若要取得目前頁面的永久連結，我們建議使用 `liff.permanentLink.createUrlBy()` 方法。

<!-- note end -->

詳情請參閱 LIFF API reference 中的 [liff.permanentLink.createUrlBy()](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by)。

2021/11/11

## LIFF v2.17.0 released 

我們已發行 LIFF v2.17.0。

在 LIFF v2.17.0 中，修正了以下錯誤。

### We've fixed a bug where executing the `liff.openWindow()` method in LINE for iOS would open URLs with unintended query parameters added to the end of the URL fragment 

如果 `url` 屬性不含查詢參數但含有 URL 片段（URL fragment），在 LINE for iOS 中執行 [`liff.openWindow()`](https://developers.line.biz/en/reference/liff/#open-window) 方法時，會開啟在 URL 片段結尾附加了非預期查詢參數的 URL。

此錯誤已在 LIFF v2.17.0 中修正，使其即使在上述情況下也能開啟正確的 URL。

#### Examples of URL opened when executing the `liff.openWindow()` method 

| LIFF SDK version | `url` property | URL opened |
| ---- | ---- | ---- |
| v2.16.1 | `https://example.com#URL-fragment` | `https://example.com#URL-fragment?is_liff_external_open_window=false` |
| v2.17.0 | `https://example.com#URL-fragment` | `https://example.com#URL-fragment` |

關於 `liff.openWindow()` 方法的詳情，請參閱 LIFF API reference 中的 [liff.openWindow()](https://developers.line.biz/en/reference/liff/#open-window)。

2021/10/26

## LIFF v2.16.1 released 

我們已發行 LIFF v2.16.1。

在 LIFF v2.16.1 中，修正了以下錯誤。

### We've fixed the bug that caused the file size to become enlarged in the CDN version of LIFF v2.14.0 or later 

由於 [LIFF v2.14.0](https://developers.line.biz/en/docs/liff/release-notes/#liff-v2-14-0) 內部原始碼的變更，LIFF v2.14.0 或更新版本的 CDN 版本有一個錯誤，導致檔案大小變大。此錯誤已在 LIFF v2.16.1 中修正，使檔案大小不會變大。

### We've fixed the bug that caused an error when building a project using webpack v5 

[Node.js polyfill 已從 webpack v5 中移除。](https://webpack.js.org/blog/2020-10-10-webpack-5-release/#automatic-nodejs-polyfills-removed)因此，如果你在使用 webpack v5 的專案中使用 npm 版本的 LIFF v2.16.0 或更早版本，建置時會發生錯誤並顯示以下訊息。

```
Module not found: Error: Can't resolve 'crypto' in 'node_modules/js-crypto-env/dist'

BREAKING CHANGE: webpack < 5 used to include polyfills for node.js core modules by default.
This is no longer the case. Verify if you need this module and configure a polyfill for it.

If you want to include a polyfill, you need to:
- add a fallback 'resolve.fallback: { "crypto": require.resolve("crypto-browserify") }'
- install 'crypto-browserify'
If you don't want to include a polyfill, you can use an empty module like this:
resolve.fallback: { "crypto": false }
```

這是因為 LIFF v2.16.0 或更早版本的實作依賴 LIFF SDK 內的 Node.js polyfill。在 LIFF v2.16.1 中，實作不再依賴 Node.js polyfill，因此不再發生上述錯誤。

#### Using the npm version of LIFF v2.16.0 or earlier in a project using webpack v5 

若要在維持相同 LIFF SDK 版本的情況下修正此錯誤，你需要安裝 Node.js polyfill 並設定 `webpack.config.js`。

首先，安裝 Node.js polyfill `crypto-browserify` 與 `stream-browserify`。

```bash
# For npm
$ npm install crypto-browserify stream-browserify

# For Yarn
$ yarn add crypto-browserify stream-browserify
```

接著，如下所示設定 `webpack.config.js` 的 `resolve.fallback`：

```js
module.exports = {
  resolve: {
    fallback: {
      crypto: require.resolve('crypto-browserify'),
      stream: require.resolve('stream-browserify'),
    },
  },
};
```

<br>

### How to update to LIFF v2.16.1 

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），你將自動更新至 v2.16.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.16.1` 或 `yarn add @line/liff@2.16.1` 來更新至 v2.16.1。

關於整合 LIFF SDK 的詳情，請參閱 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/10/12

## LIFF v2.16.0 released 

我們已發行 LIFF v2.16.0。

在 LIFF v2.16.0 中，新增了以下功能。

### The share target picker now has an option to control whether to send to multiple recipients or just one 

`liff.shareTargetPicker()` 方法新增了 `isMultiple` 屬性。透過設定 `isMultiple` 屬性，使用者現在可以控制是否允許在 target picker 中選擇多個訊息接收者。

如果你將 `isMultiple` 屬性設為 `true`，使用者可以在 target picker 中選擇多個訊息接收者。如果你設為 `false`，使用者只能選擇一位好友作為訊息接收者。預設值為 `true`。

|  `isMultiple` value  |  Available target recipients |  Available number of selection  |
| ---- | ---- | ---- |
|  `true`  |  Groups, friends, chats |  Can select multiple recipients |
|  `false`  |  Friend  |  Can select only 1 recipient  |

<!-- note start -->

**將 isMultiple 設為 false 並不保證訊息只會傳給一位好友**

即使你將 `isMultiple` 屬性設為 `false`，仍然可以透過多次呼叫 share target picker，或將同一則訊息重新分享給不同接收者，來將訊息傳給多位使用者。若要嚴格限制使用者只能向一位好友傳送訊息一次，請在實作 LIFF app 時加入限制。

以下是傳送含有 URL 的訊息並限制對該 URL 存取的範例。
1. 為該 URL 賦予一個唯一的權杖（token）並傳送訊息。
2. 當訊息中的 URL 被存取時，伺服器端驗證該權杖，並限制多位使用者的存取。

<!-- note end -->

<!-- note start -->

**我們不會擷取使用者透過 share target picker 傳送訊息的對象人數**

為了保護使用者隱私，我們既不收集也不提供關於有多少人透過 share target picker 收到使用者訊息的資訊。

<!-- note end -->

**為 `liff.shareTargetPicker()` 方法加上 `isMultiple` 屬性的範例程式碼：**

```js
if (liff.isApiAvailable('shareTargetPicker')) {
  liff.shareTargetPicker(
      [
        {
          type: "text",
          text: "Hello, World!",
        },
      ],
      {
        isMultiple: true,
      }
    )
    .then(function (res) {
      if (res) {
        // succeeded in sending a message through TargetPicker
        console.log(`[${res.status}] Message sent!`)
      } else {
        const [majorVer, minorVer] = (liff.getLineVersion() || "").split('.');
        if (parseInt(majorVer) == 10 && parseInt(minorVer) < 11) {
          // LINE 10.3.0 - 10.10.0
          // Old LINE will access here regardless of user's action
          console.log('TargetPicker was opened at least. Whether succeeded to send message is unclear')
        } else {
          // LINE 10.11.0 -
          // sending message canceled
          console.log('TargetPicker was closed!')
        }
      }
    }).catch(function (error) {
      // something went wrong before sending a message
      console.log('something wrong happen')
    })
}
```

詳情請參閱 LIFF API reference 中的 [liff.shareTargetPicker()](https://developers.line.biz/en/reference/liff/#share-target-picker)。

2021/10/01

## LIFF v1 has been discontinued on October 1, 2021 

如同 [2021 年 9 月 17 日](https://developers.line.biz/en/news/2021/09/17/liff-v1-discontinue/)所公告，2021 年 10 月 1 日標誌著 LIFF v1 的[生命週期終止（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)。

不過，由於 [Server API](https://developers.line.biz/en/reference/liff-server/) 是以與 LIFF v1 不同的時程管理，因此不受此次停止服務影響。

### Target version

LIFF v1

<!-- warning start -->

**如果你正在使用 LIFF v1，請遷移至 LIFF v2**

關於遷移至 LIFF v2 的詳情，請參閱 [2021 年 4 月 5 日](https://developers.line.biz/en/news/2021/04/05/liff-v1-deprecated/)消息中的 [Migrate to LIFF v2](https://developers.line.biz/en/news/2021/04/05/liff-v1-deprecated/#migrate-to-v2)。

<!-- warning end -->

### Scheduled date of discontinuation

2021 年 10 月 1 日

### Impact

逐步地，你將無法再參照 LIFF SDK URL（`https://d.line-scdn.net/liff/1.0/sdk.js`）或使用 [LIFF v1 API](https://developers.line.biz/en/reference/liff-v1/)。

LINE 將持續為客戶提升服務品質。感謝你的理解。

2021/09/30

## LIFF v2.15.0 released 

我們已發行 LIFF v2.15.0。

在 LIFF v2.15.0 中，新增了以下功能。

- [The 2D code reader feature has been added](https://developers.line.biz/en/docs/liff/release-notes/#liff-scan-code-v2-2021-09-30)
- [The option of automatically executing the `liff.login()` method when initializing LIFF apps in external browsers has been added](https://developers.line.biz/en/docs/liff/release-notes/#liff-init-auto-login-2021-09-30)

### The 2D code reader feature has been added 

新增了 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法，可在 LIFF app 中啟動 2D 條碼讀取器。

由於技術問題，[`liff.scanCode()`](https://developers.line.biz/en/reference/liff/#scan-code) 無法在 LINE for iOS 版本 9.19.0 或更新版本，或外部瀏覽器上使用，但使用 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2)，你現在即使在最新版本的 LINE for iOS 與外部瀏覽器上也能啟動 2D 條碼讀取器。

<!-- note start -->

**liff.scanCodeV2() 的運作規格**

`liff.scanCodeV2()` 在內部使用了名為 [jsQR](https://github.com/cozmo/jsQR) 的外部函式庫。
因此，執行 `liff.scanCodeV2()` 方法時所啟動的 2D 條碼讀取器，取決於 [jsQR](https://github.com/cozmo/jsQR) 的運作規格。所使用的函式庫可能會在不另行通知的情況下更新或變更。

<!-- note end -->

<!-- note start -->

**liff.scanCode() 方法已被棄用**

傳統的 `liff.scanCode()` 方法已被[棄用（deprecated）](https://developers.line.biz/en/glossary/#deprecated)。我們建議使用 `liff.scanCodeV2()` 方法來實作 2D 條碼讀取器。

<!-- note end -->

#### Implementing a 2D code reader with `liff.scanCodeV2()` 

使用 `liff.scanCodeV2()` 實作 2D 條碼讀取器，與使用 `liff.scanCode()` 相同。在依照以下步驟實作 `liff.scanCodeV2()` 之前，請先從 [LINE Developers Console](https://developers.line.biz/console/) 的 LIFF 分頁開啟 **Scan QR**。

<br>

###### `liff.scanCodeV2()` sample code: 

```javascript
liff.scanCodeV2().then(result => {
  // result = { value: '' }
});
```

<!-- note start -->

**LINE MINI App 上的 2D 條碼讀取器支援預定於 2021 年 10 月 7 日**

使用 `liff.scanCodeV2()` 啟動 2D 條碼讀取器，需要從 [LINE Developers Console](https://developers.line.biz/console/) 中 LINE Login 頻道的 LIFF 分頁開啟 **Scan QR**。**Scan QR** 設定預定於 **2021 年 10 月 7 日**新增至 LINE MINI App 頻道。目前，截至 **2021 年 9 月 30 日**，`liff.scanCodeV2()` 尚無法用於 LINE MINI App 頻道。

![Scan QR](https://developers.line.biz/media/liff/console-scanqr-en.png)

<!-- note end -->

#### The operating environment of the `liff.scanCodeV2()` method 

以下是 `liff.scanCodeV2()` 方法及所顯示之 2D 條碼讀取器的運作環境：

- [Operating environments](https://developers.line.biz/en/docs/liff/release-notes/#operating-environments-of-scan-code-v2)
- [2D code reader](https://developers.line.biz/en/docs/liff/release-notes/#two-dimensional-code-reader)

##### Operating environments 

由於技術問題，傳統的 [`liff.scanCode()`](https://developers.line.biz/en/reference/liff/#scan-code) 方法無法在 LINE for iOS 版本 9.19.0 或更新版本，或外部瀏覽器上使用。然而，新增的 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 方法在最新版本的 LINE for iOS 與外部瀏覽器上皆可使用。

<table>
  <thead>
    <tr>
      <th rowspan="2">OS</th>
      <th rowspan="2">Version</th>
      <th colspan="3">LINE app version</th>
      <th rowspan="2">External browser</th>
    </tr>
    <tr>
      <th>9.18.0 or earlier</th>
      <th>9.19.0-11.6.x</th>
      <th>11.7.0 or later</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">iOS</td>
      <td>11-14.2</td>
      <td>✅</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅ *1</td>
    </tr>
    <tr>
      <td>14.3 or later</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅ *2</td>
      <td>✅ *1</td>
    </tr>
    <tr>
      <td>Android</td>
      <td>All versions</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅ *2</td>
      <td>✅ *1</td>
    </tr>
    <tr>
      <td>PC</td>
      <td>All versions</td>
      <td>❌</td>
      <td>❌</td>
      <td>❌</td>
      <td>✅ *1</td>
    </tr>
  </tbody>
</table>

*1 你只能使用支援 [WebRTC API](https://developer.mozilla.org/en-US/docs/Web/API/WebRTC_API) 的網頁瀏覽器。

*2 僅在 LIFF 瀏覽器的螢幕尺寸為 `Full` 時可用。詳情請參閱 LIFF 文件中的 [Size of the LIFF browser](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

##### 2D code reader 

對於 `liff.scanCode()` 方法，Android 與 iOS 各有不同的 2D 條碼讀取器畫面，但對於 `liff.scanCodeV2()` 方法，無論 OS 為何，都會顯示以下相同的畫面。

![2D code reader screen](https://developers.line.biz/media/liff/two_dimensional_code_reader_en.png)

如果你啟動 2D 條碼讀取器，會在 `Full` 尺寸的 LIFF app 畫面底部顯示一個 `Tall` 尺寸的子視窗。此外，如果你點擊位於畫面右下方的 ![2D code selection](https://developers.line.biz/media/liff/two-dimensional-code-file-selection.png) 圖示，就可以從照片中選擇要讀取的 2D 條碼。

<br>

關於使用 `liff.scanCodeV2()` 實作 2D 條碼讀取器的詳情，請參閱 LIFF 文件中的 [Opening the 2D code reader](https://developers.line.biz/en/docs/liff/developing-liff-apps/#opening-two-dimensional-code-reader)。

### The option of automatically executing the `liff.login()` method when initializing LIFF apps in external browsers has been added 

`liff.init()` 方法新增了 `withLoginOnExternalBrowser` 屬性。通常，當你在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)上存取 LIFF 應用程式時，你需要使用 `liff.login()` 方法明確地進行登入流程。透過在新增的 `withLoginOnExternalBrowser` 屬性中指定 `true`，你可以在 LIFF app 初始化時自動執行 `liff.login()` 方法。

![Login](https://developers.line.biz/media/liff/liff_autologin_en.png)

**為 `liff.init()` 方法加上 `withLoginOnExternalBrowser` 屬性的範例程式碼：**

```js
liff.init({
  liffId: "123456-abcdef",
  withLoginOnExternalBrowser: true, // Enable automatic login process
}).then(() =>
  // Start to use liff's api
});
```

詳情請參閱 LIFF API reference 中的 [liff.init()](https://developers.line.biz/en/reference/liff/#initialize-liff-app)。

2021/09/17

## LIFF v1 discontinue 

如同 [2021 年 4 月 5 日](https://developers.line.biz/en/news/2021/04/05/liff-v1-deprecated/)所公告，LIFF v1 將於 2021 年 10 月 1 日[生命週期終止（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)，這標誌著其[棄用（deprecation）](https://developers.line.biz/en/glossary/#deprecated)期間的結束。

### Target version

LIFF v1

<!-- warning start -->

**如果你正在使用 LIFF v1，請遷移至 LIFF v2**

關於遷移至 LIFF v2 的詳情，請參閱 [2021 年 4 月 5 日](https://developers.line.biz/en/news/2021/04/05/liff-v1-deprecated/)消息中的 [Migrate to LIFF v2](https://developers.line.biz/en/news/2021/04/05/liff-v1-deprecated/#migrate-to-v2)。

<!-- warning end -->

### Scheduled date of discontinuation

2021 年 10 月 1 日

### Impact

在 2021 年 10 月 1 日停止 LIFF v1 服務後，你將逐步無法再參照 LIFF SDK URL（`https://d.line-scdn.net/liff/1.0/sdk.js`）或使用 [LIFF v1 API](https://developers.line.biz/en/reference/liff-v1/)。

LINE 將持續為客戶提升服務品質。感謝你的理解。

2021/09/14

## LIFF v2.14.0 released 

我們已發行 LIFF v2.14.0。

此次更新只包含 SDK 的重構。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），它會自動更新至 v2.14.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.14.0` 或 `yarn add @line/liff@2.14.0` 來升級至 v2.14.0。

關於如何整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/08/12

## LIFF v2.13.0 released 

我們已發行 LIFF v2.13.0。

在 LIFF v2.13.0 中，新增了以下功能，並修正了錯誤。

- [The "Channel consent simplification" feature has been added to enable skipping the LINE MINI App consent screen](https://developers.line.biz/en/docs/liff/release-notes/#channel-consent-simplification-2021-8-12)
- [We've fixed bugs in the npm package version of the LIFF SDK](https://developers.line.biz/en/docs/liff/release-notes/#npm-bug-fix-2021-8-12)

### The "Channel consent simplification" feature has been added to enable skipping the LINE MINI App consent screen 

為了使用[今天（2021 年 8 月 12 日）發行](https://developers.line.biz/en/news/2021/08/12/channel-consent-simplification/)的「Channel consent simplification」功能，你需要將 LINE MINI App 的 LIFF SDK 升級至 v.2.13.0。

當你啟用「Channel consent simplification」功能後，使用者可以略過首次存取 LINE MINI App 時所顯示的「同意畫面（consent screen）」。

關於 LIFF SDK 版本以外的使用條件（例如行為與設定）的詳情，請參閱 LINE MINI App 文件中的 [Skipping the consent screen](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/)。

### We've fixed bugs in the npm package version of the LIFF SDK 

修正了 npm 套件版本內部的部分錯誤。

如果你使用 npm 套件版本，我們建議執行 `npm install @line/liff@2.13.0` 或 `yarn add @line/liff@2.13.0` 來升級至 v2.13.0。

關於如何整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/07/12

## LIFF v2.12.0 released 

我們已發行 LIFF v2.12.0。

此次更新只變更了 SDK 的內部行為。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），它會自動更新至 v2.12.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.12.0` 或 `yarn add @line/liff@2.12.0` 來升級至 v2.12.0。

關於如何整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/06/24

## LIFF v2.11.1 released 

我們已發行 LIFF v2.11.1。

在 LIFF v2.11.1 中，修正了以下錯誤。

### We fixed the bug that caused URL fragments to be URL-encoded after the LIFF app is initialized 

在 [LIFF v2.11.0](https://developers.line.biz/en/docs/liff/release-notes/#liff-v2-11-0) 中，當你存取含有 URL 片段（例如 `#url-fragment`）的 LIFF URL 時，曾有一個錯誤導致 URL 片段在 LIFF app 初始化後（執行 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 之後）被 URL 編碼。

我們已在 LIFF v2.11.1 中修正此錯誤，使得即使在 `liff.init()` 之後，URL 片段也不會被 URL 編碼。

#### Example of URL fragment after liff.init() 

在下方的 LIFF v2.11.0 範例中，URL 片段（`#url/fragment`）中的斜線（`/`）被 URL 編碼（`%2F`）。

| LIFF version | LIFF URL | URL after `liff.init()` |
| --- | --- | --- |
| v2.11.0 | https://liff.line.me/{liffId}<b style="color:blue">#url</b><b style="color:red">/</b><b style="color:blue">fragment</b> | https://liff.line.me/{liffId}<b style="color:blue">#url</b><b style="color:red">%2F</b><b style="color:blue">fragment</b> |
| v2.11.1 | https://liff.line.me/{liffId}<b style="color:blue">#url</b><b style="color:red">/</b><b style="color:blue">fragment</b> | https://liff.line.me/{liffId}<b style="color:blue">#url</b><b style="color:red">/</b><b style="color:blue">fragment</b> |

<!-- note start -->

**我們建議更新至 LIFF v2.11.1**

在 LIFF app 的 LIFF v2.11.0 中，此錯誤無論瀏覽器類型（[LIFF browser](https://developers.line.biz/en/glossary/#liff-browser)、[LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab)、[external browser](https://developers.line.biz/en/glossary/#external-browser)）皆會發生。當你不僅直接存取 LIFF URL（例如 `https://liff.line.me/{liffId}/#url/fragment`），也直接存取端點 URL（例如 `https://example.com/#url/fragment`）時，同樣的錯誤也會發生。

如果你正在使用 v2.11.0，我們建議你更新至 v2.11.1 以避免非預期的行為。

<!-- note end -->

關於如何整合 LIFF SDK 的詳情，請參閱 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/06/14

## LIFF v2.11.0 released 

我們已發行 LIFF v2.11.0。

在 LIFF v2.11.0 中，做了以下安全性改善。

### Credential information is now excluded from the primary redirect URL after liff.init() 

基於安全因素，當 `liff.init()` 解析時，含有存取權杖（access token）等憑證資訊（credential information）的 URL 片段現在會從主要重新導向 URL（primary redirect URL）中排除。因此，在方法鏈（method chain）的 `then()` 方法中，會將不含憑證資訊的主要重新導向 URL 作為目前 URL 處理。

#### Redirect example 

如果 LIFF URL 為 `https://liff.line.me/{liffId}/path`，端點 URL 為 `https://example.com`，你將會依以下方式重新導向：

![When confidential information is excluded](https://developers.line.biz/media/news/remove_credential_information-en.png)

| Number | Item | URL |
| --- | --- | --- |
| (1) | LIFF URL | https://liff.line.me/{liffId}<span style="color:blue">/path</span> |
| (2) | Primary redirect URL | https://example.com/<span style="color:blue">?liff.state=path</span><br/><b style="color:red">#access_token=xxx&context_token=xxx&<br/>feature_token=xxx&id_token=xxx&client_id=xxx</b> |
| (3) | URL after `liff.init()` | https://example.com/<span style="color:blue">?liff.state=path</span> |
| (4) | Secondary redirect URL | https://example.com<span style="color:blue">/path</span> |

#### liff.init() sample code 

憑證資訊會在 `liff.init().then()` 方法內被排除。

``` js
console.log(window.location.href);
// https://example.com/?liff.state=path#access_token=xxx&context_token=xxx&feature_token=xxx&id_token=xxx&client_id=xxx

liff.init({liffId: myLiffId}).then(() => {
  console.log(window.location.href);
  // https://example.com/?liff.state=path
});
```

<!-- note start -->

**關於使用 Google Analytics 等外部記錄工具**

若要使用 Google Analytics 等外部記錄工具，我們建議更新至 LIFF v2.11.0，以更妥善保護存取 LIFF app 的使用者憑證資訊。請務必在執行 `liff.init()` 之後，將不含憑證資訊的 URL 傳送給外部記錄工具。

``` js
liff.init({liffId: myLiffId}).then(() => {
    ga('send', 'pageview');
})
```

<!-- note end -->

關於如何整合 LIFF SDK 的詳情，請參閱 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/05/17

## LIFF v2.10.0 released 

我們已發行 LIFF v2.10.0。

在 LIFF v2.10.0 中，修正了以下錯誤。

### We fixed the bug that caused old context tokens to be referenced when initializing the LIFF app in external browsers 

當使用者在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中使用 LIFF v2.9.1 或更早版本登入 LIFF app 時，會參照到在先前工作階段中 LIFF app 初始化（執行 `liff.init()` 方法）時儲存在 localStorage 中的舊 context token，導致非預期的行為，但我們已修正此錯誤。

<!-- tip start -->

**什麼是 context token？**

context token 保存著 LIFF app 啟動環境的相關資訊，例如螢幕尺寸與使用者 ID，可使用 [`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法取得。當你的 LIFF app 初始化（執行 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法）時，它會以 `context` 鍵（key）儲存在瀏覽器的 localStorage 中。

<!-- tip end -->

#### Updated the timing of checking access token expiration 

當你的 LIFF app 初始化（執行 `liff.init()`）時，會檢查先前工作階段所產生的存取權杖是否過期，若已過期，則丟棄 context token。然而，在 LIFF v2.9.1 或更早版本中，此過期檢查發生在 LIFF app 初始化的最後階段，因此尚未被丟棄的舊權杖會在初始化時被參照，導致非預期的行為。

在 LIFF v2.10.0 中，存取權杖的過期檢查發生在 LIFF app 初始化的開始階段，確保初始化在舊的 context token 被丟棄之後才進行。

<!-- note start -->

**無法保證透過 liff.getContext() 方法取得的資訊為最新**

context token 會在存取權杖過期時被丟棄。即使在 LIFF v2.10.0 中，只要存取權杖尚未過期，你透過 [`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法所能取得的 context 資訊就不會變更。因此，無法保證透過 `liff.getContext()` 方法取得的資訊始終為最新。

<!-- note end -->

#### When to discard context tokens for each version 

以下是 LIFF v2.9.1 或更早版本與 LIFF v2.10.0 在何時檢查存取權杖過期並丟棄 context token 的比較。

| LIFF <br> version | Flow of storing context tokens in the localStorage |
| --- | --- |
| v2.9.1 or earlier | ![Previous timing of when context tokens were discarded](https://developers.line.biz/media/news/context_token_v2-9-1-en.png) |
| v2.10.0 | ![Timing of when context tokens are discarded in v2.10.0 or later](https://developers.line.biz/media/news/context_token_v2-10-0-en.png) |

<!-- note start -->

**在 LIFF browser 與 LINE's in-app browser 的情況下**

[LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 與 [LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab) 不受此版本更新影響。

<!-- note end -->

關於 context token 所儲存資訊的詳情，請參閱 LIFF API reference 中的 [liff.getContext()](https://developers.line.biz/en/reference/liff/#get-context)。

2021/04/27

## LIFF v2.9.1 released 

在 LIFF v2.9.1 中，修正了以下錯誤，但功能上沒有變更。

### We fixed the bug that occurs when using the npm package of the LIFF SDK 

當嘗試在 TypeScript 上使用 LIFF SDK 的 npm 套件時，編譯（compilation）過程中曾發生錯誤，但此錯誤已修正。在 LIFF v2.9.1 中，即使使用 TypeScript，編譯也沒有問題。

此修正同時適用於 npm 版本與 CDN 版本的 LIFF SDK。

關於 LIFF SDK npm 套件的詳情，請參閱 [Use the npm package](https://developers.line.biz/en/docs/liff/developing-liff-apps/#use-npm-package)。

<!-- tip start -->

**如何處理編譯錯誤**

我們建議升級至 LIFF v2.9.1 作為使用 TypeScript 時編譯錯誤的解決方法，但如果你無法升級，請使用此方法來解決編譯錯誤：

如果你透過 `tsconfig.json` 等 TypeScript 設定檔啟用 [`skipLibCheck`](https://www.typescriptlang.org/ja/tsconfig#skipLibCheck) 選項，就不會發生編譯錯誤。

<!-- tip end -->

<br>

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），你的 LIFF 將自動升級至 v2.9.1。

如果你使用 npm 套件，執行 `npm install @line/liff@2.9.1` 或 `yarn add @line/liff@2.9.1` 即可將你的 LIFF 升級至 v2.9.1。

關於如何整合 LIFF SDK 的詳情，請參閱 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/04/13

## LIFF v2.9.0 released 

我們已發行 LIFF v2.9.0。

此次更新只變更了 SDK 的內部行為。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），它會自動更新至 v2.9.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.9.0` 或 `yarn add @line/liff@2.9.0` 來升級至 v2.9.0。

關於如何整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/03/16

## LIFF v2.8.1 released 

我們已發行 LIFF v2.8.1。

此次更新只包含 SDK 的重構。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），它會自動更新至 v2.8.1。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.8.1` 或 `yarn add @line/liff@2.8.1` 來升級至 v2.8.1。

關於如何整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/02/15

## LIFF v2.8.0 released 

我們已發行 LIFF v2.8.0。

在 LIFF v2.8.0 中，修正了以下錯誤。

- [Fixed bug of liff.init() being resolved before being redirected to a secondary redirect URL](https://developers.line.biz/en/docs/liff/release-notes/#liff-resolve-fix)
- [Fixed bug of unintentional decoding of URL encoded query parameters](https://developers.line.biz/en/docs/liff/release-notes/#liff-decode-fix)

功能上沒有變更或新增。

### Fixed bug of liff.init() being resolved before being redirected to a secondary redirect URL 

在早於 LIFF v2.7.1 的版本中，曾有一個錯誤：`liff.init()` 在重新導向到次要重新導向 URL 之前就被解析。由於此錯誤，`then()` 方法會被重複處理，在重新導向到次要重新導向 URL 之前與之後各一次。

在下方的程式碼範例中，提示訊息 `liff.init() is resolved.` 會顯示兩次，因為 `liff.init()` 在重新導向到次要重新導向 URL 之前與之後各被解析一次。

**當 liff.init() 被解析時顯示提示訊息的程式碼範例：**

```javascript
liff.init(myLiffId).then(() => {
  // This process is executed after liff.init() is resolved.
  window.alert("liff.init() is resolved.");
});
```

由於在 LIFF v2.8.0 中，`liff.init()` 在重新導向到次要重新導向 URL 之後才首次被解析，因此 `then()` 方法的重複處理已修正。在上方的程式碼範例中，提示訊息只會顯示一次。

| LIFF Version | Timing when `liff.init()` is resolved |
| --- | --- |
| v2.7.1 or earlier | ![resolve-timing-v2-7-0](https://developers.line.biz/media/news/resolve_timing_v2-7-0_en.png) |
| v2.8.0 | ![resolve-timing-v2-8-0](https://developers.line.biz/media/news/resolve_timing_v2-8-0_en.png) |

### Fixed bug of unintentional decoding of URL encoded query parameters 

在早於 LIFF v2.7.1 的版本中，如果開發者為 LIFF URL 賦予了 URL 編碼的查詢參數（例如 `?t=http%3A%2F%2Fexample.com`），該查詢參數會在重新導向時被解碼（例如 `?t=http://example.com`）。因此，會導向開發者非預期的次要重新導向 URL。

在 LIFF v2.8.0 中，查詢參數不會被解碼，而是維持 URL 編碼狀態重新導向。

**當你開啟 LIFF URL `https://liff.line.me/{liffId}?t=http%3A%2F%2Fexample.com` 時的重新導向流程：**

| LIFF Version | Primary redirect URL | Secondary redirect URL |
| --- | --- | --- |
| v2.7.1 or earlier | https://endpoint.example.jp/?liff.state=<br /><b style="color:blue">?t=http%3A%2F%2Fexample.com</b> | https://endpoint.example.jp/<br /><b style="color:red">?t=http:</b><b style="color:red">//example.com</b> |
| v2.8.0 | https://endpoint.example.jp/?liff.state=<br /><b style="color:blue">%3Ft%3Dhttp%253A%252F%252Fexample.com</b> | https://endpoint.example.jp/<br /><b style="color:blue">?t=http%3A%2F%2Fexample.com</b> |

<!-- tip start -->

**含有查詢參數的 LIFF URL**

當使用含有 URL 編碼查詢參數的 LIFF URL 時，請升級至 v2.8.0 以避免非預期地重新導向到其他 URL。

<!-- tip end -->

關於 LIFF app 上重新導向的詳情，請參閱 LIFF 文件中的 [Behaviors from accessing the LIFF URL to opening the LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

2021/01/20

## LIFF v2.7.1 released 

我們已發行 LIFF v2.7.1。

在 LIFF v2.7.1 中，修正了以下錯誤：

### Fixed a bug that might prevent LIFF apps using LIFF v2.7.0 from launching in external browsers 

我們修正了一個錯誤：使用 [LIFF v2.7.0](https://developers.line.biz/en/docs/liff/release-notes/#liff-v2-7-0) 的 LIFF app 在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟時可能無法啟動。在 LIFF v2.7.1 中，LIFF app 可以在外部瀏覽器中正確啟動。

<!-- note start -->

**當你已在使用 LIFF v2.7.0 時**

如果你已在使用 LIFF v2.7.0，我們建議你將 LIFF app 更新至 LIFF v2.7.1。

當你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`）時，它會自動更新至 v2.7.1。當你使用 CDN fixed 路徑或 npm 套件版本的 LIFF SDK 時，請手動將其更新至 LIFF v2.7.1。

<!-- note end -->

關於嵌入 LIFF SDK 不同方式的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2021/01/14

## LIFF v2.7.0 released 

我們已發行 LIFF v2.7.0。

此次更新的變更如下：

- [The npm package version of LIFF SDK can now be referenced by RequireJS](https://developers.line.biz/en/docs/liff/release-notes/#require-js)
- [Fixed a bug in which the name property of the ID token retrieved by the liff.getDecodedIDToken() method became unreadable](https://developers.line.biz/en/docs/liff/release-notes/#get-decoded-id-token)

### The npm package version of LIFF SDK can now be referenced by RequireJS 

npm 套件版本的 LIFF SDK 現在可以被 [RequireJS](https://requirejs.org/) 參照。

關於如何整合 npm 套件版本 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

### Fixed a bug in which the name property of the ID token retrieved by the liff.getDecodedIDToken() method became unreadable 

在 LIFF v2.6.0 或更早版本中，使用 `liff.getDecodedIDToken()` 方法取得已解碼的 ID token 時，如果使用者名稱含有 ASCII 字元以外的 Unicode 字元（例如日文），`name` 屬性的值會變成亂碼。

在 LIFF v2.7.0 中，此錯誤已修正，現在可以正確取得以日文等 Unicode 字元書寫的使用者名稱。

**如果你取得使用者名稱為 `コニー` 的 ID token**

![user profile of conny](https://developers.line.biz/media/news/conny_en.png)

| LIFF v2.6.0 or earlier | LIFF v2.7.0 |
| :---: | :---: |
| <pre class="language-json"><code><span class="token punctuation">{</span><br/><span class="token property">"iss"</span><span class="token operator">:</span> <span class="token string">"https://access.line.me"</span><span class="token punctuation">,</span><br/><span class="token property">"sub"</span><span class="token operator">:</span> <span class="token string">"U272cada9c6f4c0c933b0713bc2f90f68"</span><span class="token punctuation">,</span><br/><span class="token property">"aud"</span><span class="token operator">:</span> <span class="token string">"1234567890"</span><span class="token punctuation">,</span><br/><span class="token property">"exp"</span><span class="token operator">:</span> <span class="token number">1513142487</span><span class="token punctuation">,</span><br/><span class="token property">"iat"</span><span class="token operator">:</span> <span class="token number">1513138887</span><span class="token punctuation">,</span><br/><span class="token property">"name"</span><span class="token operator">:</span> <span class="token string">"<b style="color:white">ã³ãã¼</b>"</span><span class="token punctuation">,</span><span class="token comment"> //Unreadable</span><br/><span class="token property">"picture"</span><span class="token operator">:</span> <span class="token string">"https://profile.line-scdn.net/..."</span><br/><span class="token punctuation">}</span></code></pre> | <pre class="language-json"><code><span class="token punctuation">{</span><br/><span class="token property">"iss"</span><span class="token operator">:</span> <span class="token string">"https://access.line.me"</span><span class="token punctuation">,</span><br/><span class="token property">"sub"</span><span class="token operator">:</span> <span class="token string">"U272cada9c6f4c0c933b0713bc2f90f68"</span><span class="token punctuation">,</span><br/><span class="token property">"aud"</span><span class="token operator">:</span> <span class="token string">"1234567890"</span><span class="token punctuation">,</span><br/><span class="token property">"exp"</span><span class="token operator">:</span> <span class="token number">1513142487</span><span class="token punctuation">,</span><br/><span class="token property">"iat"</span><span class="token operator">:</span> <span class="token number">1513138887</span><span class="token punctuation">,</span><br/><span class="token property">"name"</span><span class="token operator">:</span> <span class="token string">"<b style="color:white">コニー</b>"</span><span class="token punctuation">,</span><span class="token comment"> //Correctly received</span><br/><span class="token property">"picture"</span><span class="token operator">:</span> <span class="token string">"https://profile.line-scdn.net/..."</span><br/><span class="token punctuation">}</span></code></pre> |

關於 `liff.getDecodedIDToken()` 的詳情，請參閱 LIFF API reference 中的 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token)。

2020/12/01

## LIFF v2.6.0 released 

我們已發行 LIFF v2.6.0。

此次更新只變更了 SDK 的內部行為。功能上沒有變更。

如果你使用 CDN edge 路徑（`https://static.line-scdn.net/liff/edge/2/sdk.js`），它會自動更新至 v2.6.0。

如果你使用 npm 套件，可以執行 `npm install @line/liff@2.6.0` 或 `yarn add @line/liff@2.6.0` 來升級至 v2.6.0。

關於如何整合 LIFF SDK 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

2020/10/29

## LIFF v2.5.0 released 

我們已發行 LIFF v2.5.0。

LIFF v2.5.0 的變更如下。

- [Improved performance of liff.init()](https://developers.line.biz/en/docs/liff/release-notes/#improve-liff-init-performance)
- [Security enhancements](https://developers.line.biz/en/docs/liff/release-notes/#security-enhancement)

此次更新中 LIFF 功能沒有變更。

### Improved performance of liff.init() 

從執行 `liff.init()` 到完成 LIFF app 初始化的速度已獲得改善，提供更愉快的使用者體驗，開啟 LIFF app 的等待時間更短。

關於 `liff.init()` 的詳情，請參閱 LIFF API Reference 中的 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app)。

### Security enhancements 

我們強化了安全性，作為對未知攻擊的預防措施。

<!-- tip start -->

**關於更新你的 LIFF app**

由於這是輕微的安全性強化，因此不需要更新。

<!-- tip end -->

2020/09/28

## LIFF v2.3.3 released 

我們已發行 LIFF v2.3.3。
在 LIFF v2.3.3 中，修正了以下錯誤：

- [Fixed a bug that redirects users to unintended URLs when the endpoint URL ends with /](https://developers.line.biz/en/docs/liff/release-notes/#liff-url-including-path-bug-fix)

此次發行中沒有功能更新。

### Fixed a bug that redirects users to unintended URLs when the endpoint URL ends with / 

在以下條件下，存取 LIFF URL 會導致重新導向到含有雙重路徑分隔符（`//`）的非預期 URL。

- **Endpoint URL** 中所指定的 URL 含有路徑且以 `/` 結尾。例如 `https://example.com/campaign/`
- **Methods for converting additional information in the LIFF URL** 設為 **Concatenate**。
- LIFF URL 含有路徑（`/path`）。例如 `https://liff.line.me/{liffId}/path`

在 LIFF v2.3.3 中，此錯誤已修正，使得即使在上述條件下使用者也會被重新導向到正確的 URL。

| Item | LIFF URL | Primary redirect URL | Secondary redirect URL |
| --- | --- | --- | --- |
| Before spec change | https://liff.line.me/{liffId}/path | https://example.com/campaign<b style="color:red">/</b>?liff.state={urlEncode(/path)} | https://example.com/campaign<b style="color:red">//</b>path |
| After spec change | https://liff.line.me/{liffId}/path | https://example.com/campaign?liff.state={urlEncode(path)} | https://example.com/campaign<b style="color:red">/</b>path |

<!-- note start -->

**對其他版本的影響**

- 如果你正在使用 LIFF v2.3.x，我們建議你更新至此修補版本（patch version）。
- 此錯誤已在 LIFF v2.4.1 中修正。

<!-- note end -->

關於存取 LIFF URL 時會發生什麼的詳情，請參閱 LIFF 文件中的 [Operation from accessing LIFF URL to opening LIFF App](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

2020/09/24

## LIFF v2.4.1 released 

我們已發行 LIFF v2.4.1。
LIFF v2.4.1 的變更如下：

- [Fixed an issue with the feature to open another LIFF app without closing a LIFF app](https://developers.line.biz/en/docs/liff/release-notes/#liff-transition-bug-fix)
- [Added a feature to liff.isApiAvailable() to check whether the transition between LIFF apps is possible](https://developers.line.biz/en/docs/liff/release-notes/#liff-transition-state)
- [Fixed behavior of liff.init() being called twice](https://developers.line.biz/en/docs/liff/release-notes/#call-init-twice-fix)

### Fixed an issue with the feature to open another LIFF app without closing a LIFF app 

我們發現[於 2020 年 8 月 31 日公告](https://developers.line.biz/en/news/2020/08/31/release-liff-2-4-0/#liff-transition)的「在不關閉 LIFF app 的情況下開啟另一個 LIFF app」功能有一個錯誤，即使符合運作條件也無法正確運作。

在 LIFF v2.4.1 中，運作條件已變更如下，且錯誤已修正。

| Items | Before the changes | After the changes |
| --- | --- | --- |
| LIFF SDK | 2.4.0 | 2.4.1 |
| LINE | 10.16.0 | 10.18.0 |

<!-- note start -->

**不再建議使用 LIFF v2.4.0**

由於上述錯誤，不再建議使用 LIFF v2.4.0。
如果你正在使用 LIFF v2.4.0，我們建議你更新至 v2.4.1。

<!-- note end -->

詳情請參閱 LIFF 文件中的 [Opening a LIFF app from another LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff)。

### Added a feature to liff.isApiAvailable() to check whether the transition between LIFF apps is possible 

[`liff.isApiAvailable()`](https://developers.line.biz/en/reference/liff/#is-api-available) 是檢查某 API 是否可用的方法，現在可用於檢查 LIFF app 之間的轉換是否可行。

你現在可以執行 `liff.isApiAvailable('multipleLiffTransition')`，在開啟另一個 LIFF app 之前確認 LIFF app 之間的轉換是否可行。
透過使用此功能，你可以避免開啟另一個 app 時發生錯誤。

```js
if (liff.isApiAvailable('multipleLiffTransition')) {
  window.location.href = "https://line.me/{liffId}", // URL for another LIFF app
}
```

<!-- tip start -->

**透過 liff.getContext() 取得 LIFF app 之間轉換的資訊**

你現在也可以使用取得 LIFF app 資訊的 [`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法，取得 LIFF app 之間轉換是否可行，以及可執行的 LINE 版本等資訊。
- `availability.multipleLiffTransition.permission`：表示 LIFF app 之間的轉換是否可行。
- `availability.multipleLiffTransition.minVer`：表示支援 LIFF app 之間轉換的最低 LINE 版本。

以下是 `liff.getContext()` 回傳值的範例。
```json
{
    "type": "utou",
    "utouId": "UU29e6eb36812f484fd275d41b5af4e760926c516d8c9faa35…b1e8de8fbb6ecb263ee8724e48118565e3368d39778fe648d",
    "userId": "U70e153189a29f1188b045366285346bc",
    "viewType": "full",
    "accessTokenHash": "ArIXhlwQMAZyW7SDHm7L2g",
    "availability": {
        "shareTargetPicker": {
            "permission": true,
            "minVer": "10.3.0"
        },
        "multipleLiffTransition": {
            "permission": true,
            "minVer": "10.18.0"
        }
    }
}
```

<!-- tip end -->

詳情請參閱 LIFF API reference 中的 [liff.isApiAvailable()](https://developers.line.biz/en/reference/liff/#is-api-available) 或 [liff.getContext()](https://developers.line.biz/en/reference/liff/#get-context)。

### Fixed behavior of liff.init() being called twice 

如果在 LIFF App 成功初始化的條件下執行 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 超過一次，會回傳一個被 reject 並帶有錯誤訊息的 `Promise` 物件。

在 LIFF v2.4.1 中，此錯誤已修正，使得如果在 `liff.init()` 成功的條件下執行 `liff.init()` 超過一次，會回傳一個已解析的 `Promise` 物件，並顯示警告訊息。

關於初始化你的 LIFF App 的詳情，請參閱 LIFF 文件 [Initializing LIFF App](https://developers.line.biz/en/docs/liff/developing-liff-apps/#initializing-liff-app)。

2020/09/14

## LIFF v2.1.14, v2.2.1, v2.3.2 released 

LIFF v2.1.14、v2.2.1、v2.3.2 已發行。變更如下：

- [Fixed error in which the URL fragment entered in the LIFF endpoint URL was not correctly handled by liff.permanentLink.createUrl() (v2.3.2)](https://developers.line.biz/en/docs/liff/release-notes/#liff-create-url-error-fix-endpoint-v-2-3-2)
- [Fixed error in which the query parameter entered in the LIFF endpoint URL was not correctly handled by liff.permanentLink.createUrl() (v2.3.2)](https://developers.line.biz/en/docs/liff/release-notes/#liff-create-url-error-fix-query-parameter-v-2-3-2)
- [Fixed error in which the path entered in the LIFF endpoint URL was not correctly handled by liff.permanentLink.createUrl() (v2.3.2)](https://developers.line.biz/en/docs/liff/release-notes/#liff-create-url-redirect-url-fix-2-3-2)
- [Fixed error in which fragment was not included in the secondary redirect URL (v2.3.2)](https://developers.line.biz/en/docs/liff/release-notes/#liff-url-fragment-error-fix-v-2-3-2)
- [Fixed bug in which LIFF URLs were redirected to unintended URLs (v2.1.14, v2.2.1, v2.3.2)](https://developers.line.biz/en/docs/liff/release-notes/#bug-fix-redirect-2-3-2)

### Fixed error in which the URL fragment entered in the LIFF endpoint URL was not correctly handled by liff.permanentLink.createUrl() 

<br />

**Affected version**

- LIFF v2.3.2

**Changes**

當 LIFF 端點 URL 含有 URL 片段（`#URL-fragment`）時，儘管 **Methods for converting additional information in the LIFF URL** 設為 **Replace (Backward compatibility mode)**，該 URL 片段仍會包含在執行 [`liff.permanentLink.createUrl()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url) 後回傳的永久連結中。

<!-- tip start -->

**發生此問題的條件**

- LIFF 端點 URL 中含有 URL 片段
- **Methods for converting additional information in the LIFF URL** 設為 **Replace (Backward compatibility mode)**

<!-- tip end -->

例如，當 **Endpoint URL** 設為 `https://example.com/path#section` 並執行 `liff.permanentLink.createUrl()` 時，會回傳 `https://liff.line.me/{liffId}/path?liff.state=#section` 作為永久連結。在 LIFF v.2.3.2 中，此錯誤已修正，使其正確回傳 `https://liff.line.me/{liffId}`。

### Fixed error in which the query parameter entered in the LIFF endpoint URL was not correctly handled by liff.permanentLink.createUrl() 

<br />

**Affected version**

- LIFF v2.3.2

**Changes**

當 LIFF 端點 URL 含有查詢參數（`?key=value`）時，該查詢參數會在執行 `liff.permanentLink.createUrl()` 後回傳的永久連結中無限增生。

<!-- tip start -->

**發生此問題的條件**

- LIFF 端點 URL 中的查詢參數，與執行 `liff.permanentLink.createUrl()` 時 LIFF URL 中的查詢參數相符。
- **Methods for converting additional information in the LIFF URL** 設為 **Concatenate**

<!-- tip end -->

例如，當 **Endpoint URL** 設為 `https://example.com/path1/?q1=v1&q2=v2`，並在 `https://liff.line.me/{liffid}/?q1=v1&q2=v2` 中執行 `liff.permanentLink.createUrl()` 時，會回傳查詢參數無限增生的永久連結，例如 `https://liff.line.me/{liffid}/?q1=v1&q1=v1&q2=v2&q2=v2`。

在 LIFF v.2.3.2 中，此錯誤已修正，使其正確回傳 `https://liff.line.me/{liffid}/?q1=v1&q2=v2`。

### Fixed error in which the path entered in the LIFF Endpoint URL was not correctly handled by liff.permanentLink.createUrl() 

<br />

**Affected versions**

- LIFF v2.3.2

**Changes**

當 LIFF 端點 URL 中含有路徑且路徑結尾使用斜線（`/`）時，執行 `liff.permanentLink.createUrl()` 取得的永久連結會將你重新導向到如下所示沒有結尾斜線的 URL。

<!-- tip start -->

**發生此問題的條件**

- LIFF 端點 URL 中含有路徑（`/path/`），且路徑結尾使用斜線（`/`）
- LIFF 端點 URL 中含有查詢參數（`?key=value`）或 URL 片段（`#URL-fragment`）
- **Methods for converting additional information in the LIFF URL** 設為 **Concatenate**

<!-- tip end -->

例如，如果 **Endpoint URL** 設為 `https://example.com/path/?id=xxxxxxx`，存取執行 `liff.permanentLink.createUrl()` 取得的永久連結會將你重新導向到沒有結尾斜線的 URL，例如 `https://example.com/path?id=xxxxxxx`。

在 LIFF v2.3.2 中，此錯誤已修正，使其正確地將你重新導向到 `https://example.com/path/?id=xxxxxxx`。

<!-- note start -->

**LIFF v2.4.0 已修正**

如同 [2020 年 8 月 31 日](https://developers.line.biz/en/news/2020/08/31/release-liff-2-4-0/#liff-create-url-error-fix)所公告，此錯誤修正已反映在 LIFF v2.4.0 中。

<!-- note end -->

### Fixed error in which fragment was not included in the secondary redirect URL 

<br />

**Affected version**

- LIFF v2.3.2

**Changes**

當 LIFF 端點 URL 或 LIFF URL 中含有片段（fragment）時，無論基於 **Methods for converting additional information in the LIFF URL** 的設定為何，次要重新導向 URL 都不會包含片段。此錯誤已修正。

關於次要重新導向 URL 或其如何受基於 **Methods for converting additional information in the LIFF URL** 設定影響的詳情，請參閱 LIFF 文件 [Operation from accessing LIFF URL to opening LIFF App](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

### Fixed bug in which LIFF URLs were redirected to unintended URLs 

<br />

**Affected versions**

- LIFF v2.1.14
- LIFF v2.2.1
- LIFF v2.3.2

**Changes**

在主要重新導向目標 URL 中，LIFF URL 中所指定的附加資訊（例如 `path/?key=value`）會包含在 `liff.state` 查詢參數中。當附加資訊包含在 `liff.state` 查詢參數中時，曾有一個錯誤，會將你重新導向到如下所示的非預期 URL。

<!-- tip start -->

**發生此問題的條件**

- `liff.state` 查詢參數的開頭沒有 `/`
- **Methods for converting additional information in the LIFF URL** 設為 **Replace (Backward compatibility mode)**

<!-- tip end -->

例如，當 **Endpoint URL** 設為 `https://example.com`，且 `liff.state` 查詢參數為 `path` 時，網域名稱與路徑之間不會以 `/` 分隔，導致被重新導向到 `https://example.compath`。
在 LIFF v2.1.14、v2.2.1、v2.3.2 中，此錯誤已修正，使其正確地將你重新導向到 `https://example.com/path`。

<!-- note start -->

**關於非預期重新導向所造成的弱點（vulnerability）**

由於此錯誤，使用者有可能被重新導向到惡意網站。如果你使用的 LIFF SDK 版本早於 v2.4.0，我們建議你更新它。

<!-- note end -->

關於存取 LIFF URL 時會發生什麼的詳情，請參閱 LIFF 文件 [Operation from accessing LIFF URL to opening LIFF App](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

2020/08/31

## LIFF v2.4.0 released 

<!-- note start -->

**2020 年 9 月 24 日新增**

由於[在不關閉目前 LIFF app 的情況下轉換到另一個 LIFF app](https://developers.line.biz/en/docs/liff/release-notes/#liff-transition) 功能有一個錯誤，不再建議使用 LIFF v2.4.0。

| Items | Before the changes | After the changes |
| --- | --- | --- |
| LIFF SDK | 2.4.0 | 2.4.1 |
| LINE | 10.16.0 | 10.18.0 |

如果你正在使用 LIFF v2.4.0，我們建議你更新至 v2.4.1。

<!-- note end -->

我們已發行 LIFF v2.4.0。LIFF v2.4.0 的變更如下：

- [You can now use `liff.closeWindow()` before the LIFF app is initialized](https://developers.line.biz/en/docs/liff/release-notes/#liff-close-window)
- [You can now transition to another LIFF app without closing your current LIFF app](https://developers.line.biz/en/docs/liff/release-notes/#liff-transition)
- [The error that LIFF URLs are redirected to unexpected URLs was fixed](https://developers.line.biz/en/docs/liff/release-notes/#bug-fix-redirect)
- [liff.permanentLink.createUrl() error was fixed](https://developers.line.biz/en/docs/liff/release-notes/#liff-create-url-error-fix)
- [The error of fragment not being included in the secondary redirect URL was fixed](https://developers.line.biz/en/docs/liff/release-notes/#liff-url-fragment-error-fix)

### You can now use `liff.closeWindow()` before the LIFF app is initialized 

你現在可以在 LIFF app 初始化之前，甚至在 `liff.init()` 完成 LIFF app 初始化之前，使用 `liff.closeWindow()` 方法。

<!-- note start -->

**在初始化 LIFF app 之前執行 liff.closeWindow() 方法的條件**

若要在 `liff.init()` 完成 LIFF app 初始化之前使用 `liff.closeWindow()` 方法，你的 LIFF SDK 版本必須為 v2.4.0 或更新版本，且使用者的 LINE 版本必須為 10.15.0 或更新版本。

<!-- note end -->

如下所示，如果 LIFF app 因網路錯誤、使用者的 LINE 版本等而初始化失敗，你可以使用 `liff.closeWindow()` 方法關閉 LIFF app。

``` js
liff
  .init({
    liffId: "123456-abcedfg" // Use own liffId
  })
  .then(() => {
    // Start to use liff's api
  })
  .catch((err) => {
    // Error happens during initialization
    console.log(err.code, err.message);
    liff.closeWindow();
  });
```

詳情請參閱 LIFF API Reference 中的 [liff.closeWindow()](https://developers.line.biz/en/reference/liff/#close-window)。

### You can now transition to another LIFF app without closing your current LIFF app 

如果你在螢幕為 `Full` 顯示的 LIFF app 中點擊指向另一個 LIFF app 的連結，你可以在 LIFF 瀏覽器仍開啟的情況下顯示另一個 app。
LIFF 瀏覽器不會關閉，因此你可以透過 LIFF 瀏覽器的返回按鈕返回原本的 LIFF app。

<!-- note start -->

**在不關閉目前 LIFF app 的情況下移動到另一個 LIFF app 的條件（2020 年 9 月 24 日新增）**

LIFF v2.4.0 中有一個錯誤，導致此功能無法正常運作。已對此功能的運作條件做了以下變更：

- LIFF SDK v2.4.1 或更新版本，以及 LINE 10.18.0 或更新版本
- 原本的 LIFF app 螢幕設為 `Full` 顯示
- 要移動到的 LIFF app 已透過 `liff.init()` 正確初始化

<!-- note end -->

![LIFF-apps-transition](https://developers.line.biz/media/liff/liff_transition.png)

詳情請參閱 LIFF 文件中的 [Opening a LIFF app from another LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff)。

### The error that LIFF URLs are redirected to unexpected URLs was fixed 

LIFF URL 中所指定的附加資訊（`path/?key=value`）會包含在主要重新導向 URL 的 `liff.state` 查詢參數中。當 `liff.state` 查詢參數含有附加資訊時，可能會如下所示被重新導向到非預期的次要重新導向 URL。

<!-- tip start -->

**造成此錯誤的條件**

- 當 `liff.state` 查詢參數不以 `/` 開頭時
- 當 **Methods for converting additional information in the LIFF URL** 設為 **Replace (Backward compatibility mode)** 時

<!-- tip end -->

例如，如果 **Endpoint URL** 設為 `https://example.com`，且 `liff.state` 查詢參數被指定為 `path`，由於網域名稱與路徑之間沒有以 `/` 分隔，會被重新導向到 `https://example.compath`。
在 LIFF v2.4.0 中，此錯誤已修正，使得上述 URL 現在能正確地重新導向到 `https://example.com/path`。

關於存取 LIFF URL 時行為的詳情，請參閱 [Behaviors from accessing the LIFF URL to opening the LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

### liff.permanentLink.createUrl() error was fixed

當 LIFF 端點 URL 中含有查詢參數（`?key=value`）或 URL 片段（`#URL-fragment`）等資訊時，在執行 [`liff.permanentLink.createUrl()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url) 時，附加資訊部分有時無法準確反映在永久連結中。此錯誤已修正。

### The error of fragment not being included in the secondary redirct URL was fixed 

當 LIFF 端點 URL 或 LIFF URL 中含有片段時，無論基於 **Methods for converting additional information in the LIFF URL** 的設定為何，次要重新導向 URL 都不會包含片段。此錯誤已修正。

關於次要重新導向 URL 或其如何受基於 **Methods for converting additional information in the LIFF URL** 設定影響的詳情，請參閱 LIFF 文件 [Operation from accessing LIFF URL to opening LIFF App](https://developers.line.biz/en/docs/liff/opening-liff-app/#redirect-flow)。

2020/07/16

## LIFF v2.3.1 released 

我們現已發行 LIFF v2.3.1。
LIFF v2.3.1 的變更如下：

- [Problems with the LIFF SDK npm package documentation were fixed](https://developers.line.biz/en/docs/liff/release-notes/#liff-npm-docs-fix)
- [Installation and usage instructions of the LIFF SDK npm package were moved from the npm official website to LINE Developers site](https://developers.line.biz/en/docs/liff/release-notes/#liff-npm-docs-move)

此次發行中沒有功能更新。

### Problems with the LIFF SDK npm package documentation were fixed 

我們修正了實驗性發行的 LIFF SDK npm 套件在 [npm 官方網站文件](https://www.npmjs.com/package/@line/liff)上的一個問題。

### Installation and usage instructions of the LIFF SDK npm package were moved 

我們將 LIFF SDK npm 套件的安裝與使用說明，從 [npm 官方網站](https://www.npmjs.com/package/@line/liff)移至 LINE Developers 網站。
詳情請參閱 [Use the npm package](https://developers.line.biz/en/docs/liff/developing-liff-apps/#use-npm-package)。

2020/07/15

## New feature has been added to the LIFF header

如同 [2020 年 7 月 6 日](https://developers.line.biz/en/news/2020/07/06/liff-header-design-improvement/)所公告，LIFF header 新增了一項功能。

![LIFF header design to be improved](https://developers.line.biz/media/news/liff-header-design-improvement.png)

- [The LIFF app icon is no longer displayed](https://developers.line.biz/en/docs/liff/release-notes/#remove-liff-app-icon-07-15)
- [The share button has been added](https://developers.line.biz/en/docs/liff/release-notes/#liff-share-button-07-15)

### The LIFF app icon is no longer displayed 

LIFF app 左上角的圖示不再顯示。

### The share button has been added 

[LIFF app 檢視尺寸](https://developers.line.biz/en/docs/liff/overview/#screen-size)設為 `Full` 的 LIFF app，header 中會包含一個分享按鈕。
當使用者點擊分享按鈕時，會出現以下選項：

<ParameterTable>

**Share**:
  description: |
    透過 LINE 訊息分享目前頁面的 URL。
**Refresh**:
  description: |
    重新載入目前頁面。

</ParameterTable>

在 LINE Developers Console 中啟用 LIFF app 的 **Module mode** 可隱藏分享按鈕。
詳情請參閱 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/)。

<!-- note start -->

**運作環境**

分享按鈕將在 iOS 與 Android 的 LINE 版本 10.12.0 或更新版本上可用。

<!-- note end -->

我們將持續提升為開發者提供的服務品質，非常感謝你的理解。

2020/07/01

## LIFF SDK released as an npm package

至今為止，要將 LIFF SDK 包含進 LIFF app，必須[指定 CDN 路徑](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

今天，我們以試用形式發行了 LIFF SDK npm 套件。現在你可以使用 npm 與 Yarn 來安裝 LIFF SDK。

關於 LIFF SDK npm 套件的詳情，請參閱 [https://www.npmjs.com/package/@line/liff](https://www.npmjs.com/package/@line/liff)。

可作為 npm 套件使用的 LIFF SDK 版本為 v2.3.0 或更新版本。未來 LIFF SDK 版本的功能將在 LIFF 文件的 [Release Notes](https://developers.line.biz/en/docs/liff/release-notes/) 中公告。

<!-- note start -->

**npm 套件試用**

npm 套件以試用形式提供。未來可能在不另行通知的情況下變更或刪除。

<!-- note end -->

2020/06/29

## LIFF v2.3.0 released 

我們現已發行 LIFF v2.3.0。
LIFF v2.3.0 的變更如下：

- [You can now use paths and query parameters in the LIFF endpoint URL](https://developers.line.biz/en/docs/liff/release-notes/#endpoint-url)
- [A condition for the liff.permanentLink.createUrl() method to throw an exception added](https://developers.line.biz/en/docs/liff/release-notes/#permanentLink)
- [You can now get the send results of liff.shareTargetPicker()](https://developers.line.biz/en/docs/liff/release-notes/#shareTargetPicker)
- [An error code returned by liff.sendMessages() added](https://developers.line.biz/en/docs/liff/release-notes/#sendMessage)

## You can now use paths and query parameters in the LIFF endpoint URL 

[如先前所公告](https://developers.line.biz/en/news/2020/05/20/liff-endpoint-url-improvement/)，你現在可以在 [LINE Developers Console](https://developers.line.biz/console/) LIFF 分頁的 LIFF 端點 URL 中使用附加的路徑（`/path`）與查詢參數（`?key=value`）。

<!-- note start -->

**現有 LIFF app 在設定變更之前不受影響**

需要在 LINE Developers Console 中變更設定，才能在現有 LIFF app 中使用新規格。現有 LIFF app 在設定變更之前不受新規格影響。

![Methods for converting additional information in the LIFF URL](https://developers.line.biz/media/liff/preserve-full-endpoint-url-en.png)

若要使用新規格，請將 **Methods for converting additional information in the LIFF URL** 設為 **Concatenate**。
如果你的現有 LIFF app 不支援新規格，請勿變更設定。如果設為 **Replace (Backward compatibility mode)**，LIFF app 不受新規格影響。

<!-- note end -->

詳情請參閱 LIFF 文件中的 [Opening a LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

## A condition for the liff.permanentLink.createUrl() method to throw an exception added 

執行 `liff.permanentLink.createUrl()` 方法時，如果目前頁面 URL 不是以 **Endpoint URL** 中所指定的 URL 開頭，就會擲回例外（exception）。

```javascript
try {
    const myLink = liff.permanentLink.createUrl()
}
catch (err) {
    console.log(err.code + ':' + err.message);
}
```

特別是當 **Methods for converting additional information in the LIFF URL** 設為 **Replace (Backward compatibility mode)** 時，**Endpoint URL** 中所指定的路徑與查詢參數（`/2020campaign/?key=value`）可能不會包含在次要重新導向 URL 中。
在此情況下，由於 `liff.permanentLink.createUrl()` 方法符合上述條件，你無法取得永久連結。

詳情請參閱 LIFF v2 API reference 中的 [`liff.permanentLink.createUrl()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url)。

## You can now get the send results of liff.shareTargetPicker() 

如同 [2020 年 4 月 21 日](https://developers.line.biz/en/news/2020/04/21/notice-return-value-of-sharetargetpicker/)所公告，你現在可以取得 `liff.shareTargetPicker()` 的傳送結果。

在規格變更之前，LIFF app 可以確認 target picker 是否已顯示，但無法確認之後訊息是否已傳送。

變更之後，LIFF app 可以檢查訊息是否已傳送，因此你可以依使用者的情況改變 LIFF app 的行為。

<!-- note start -->

**Note**

- 由於此規格變更，`liff.shareTargetPicker()` 的回傳值已變更。
- 此規格變更不影響使用 LINE 10.3.0 - 10.10.0 的使用者。

<!-- note end -->

### Sample code for this spec change

我們建議你依使用者所使用的 LINE 版本處理回傳值，如下所示：

```javascript
if (liff.isApiAvailable('shareTargetPicker')) {
  liff.shareTargetPicker([
    {
      'type': 'text',
      'text': 'Hello, World!'
    }
  ])
    .then(function (res) {
      if (res) {
        // succeeded in sending a message through TargetPicker
        console.log(`[${res.status}] Message sent!`)
      } else {
        const [majorVer, minorVer] = (liff.getLineVersion() || "").split('.');
        if (parseInt(majorVer) == 10 && parseInt(minorVer) < 11) {
          // LINE 10.3.0 - 10.10.0
          // Old LINE will access here regardless of user's action
          console.log('TargetPicker was opened at least. Whether succeeded to send message is unclear')
        } else {
          // LINE 10.11.0 -
          // sending message canceled
          console.log('TargetPicker was closed!')
        }
      }
    }).catch(function (error) {
      // something went wrong before sending a message
      console.log('something wrong happen')
    })
}
```

詳情請參閱 LIFF v2 API reference 中的 [`liff.shareTargetPicker()`](https://developers.line.biz/en/reference/liff/#share-target-picker)。

## An error code returned by liff.sendMessages() added 

先前，如果傳遞錯誤的參數給 `liff.sendMessages()`，會回傳 `400` 作為 `LiffError` 的錯誤碼。規格變更後，改為回傳 `INVALID_ARGUMENT`。

只要處理流程不是依錯誤碼分流，此規格變更就不會影響你的 LIFF app。

規格變更前：

```javascript
liff.sendMessages([
  {
    type: 'text',
    text: 'Hello, World!'
  }
])
  .then(() => {
    console.log('message sent');
  })
  .catch((err) => {
    // Returns "400" if invalid arguments are passed
    if (err.code === "400") {
      console.log("message format error!");
    }
  });
```

規格變更後：

```javascript
liff.sendMessages([
  {
    type: 'text',
    text: 'Hello, World!'
  }
])
  .then(() => {
    console.log('message sent');
  })
  .catch((err) => {
    // Returns "INVALID_ARGUMENT" if invalid arguments are passed
    if (err.code === "INVALID_ARGUMENT") {
      console.log("message format error!");
    }
  });
```

詳情請參閱 LIFF v2 API reference 中的 [Error details](https://developers.line.biz/en/reference/liff/#error-details)。

2020/06/15

## LIFF v2.2.0: LIFF error codes added 

以下方法在 `Promise` 被 reject 時所傳遞的 `LiffError` 錯誤碼已更為詳細，使問題原因更容易理解。

詳情請查看這些方法的 **Error Response** 說明：

- [liff.init()](https://developers.line.biz/en/reference/liff/#initialize-liff-app)
- [liff.getProfile()](https://developers.line.biz/en/reference/liff/#get-profile)
- [liff.getFriendship()](https://developers.line.biz/en/reference/liff/#get-friendship)

2020/04/30

## LIFF v2.1.13: liff.getLineVersion() and liff.id added to LIFF v2 

我們在 LIFF v2 中新增了 `liff.getLineVersion()` 方法與 `liff.id` 屬性。

`liff.getLineVersion()` 讓你可以取得使用者的 LINE 版本。

如果使用者使用 LIFF 瀏覽器開啟 LIFF app，會回傳使用者的 LINE 版本（字串型別）。如果使用者使用外部瀏覽器開啟 LIFF app，則回傳 `null`。

`liff.id` 是保存傳給 `liff.init()` 之 LIFF app ID（String 型別）的屬性。

關於 [`liff.getLineVersion()`](https://developers.line.biz/en/reference/liff/#get-line-version) 與 [`liff.id`](https://developers.line.biz/en/reference/liff/#id) 的詳情，請參閱 LIFF v2 API reference。

2020/04/03

## liff.isApiAvailable() added to LIFF v2

我們在 LIFF v2 中新增了 `liff.isApiAvailable()` 方法。此方法檢查指定的 API 是否可在 LIFF app 啟動的環境中使用。

<!-- note start -->

**Note**

可指定的 API 數量有限。目前你只能指定 `liff.shareTargetPicker()`。未來當有更多 API 可用 `liff.isApiAvailable()` 檢查時，我們會通知你。

<!-- note end -->

## Check if share target picker is available

在執行 `liff.shareTargetPicker()` 之前先執行 `liff.isApiAvailable()`，如果 share target picker 在使用者的裝置環境中不可用，你可以避免使用者在螢幕上看到錯誤訊息。

```javascript
if (liff.isApiAvailable('shareTargetPicker')) {
  liff.shareTargetPicker([
    {
      type: "text",
      text: "Hello, World!"
    }
  ])
    .then(
      alert("ShareTargetPicker was launched")
    ).catch(function(res) {
      alert("Failed to launch ShareTargetPicker")
    })
}
```

關於詳情，請參閱 LIFF v2 API reference 中的 [liff.isApiAvailable()](https://developers.line.biz/en/reference/liff/#is-api-available)。

2020/03/03

## liff.shareTargetPicker() and liff.ready added to LIFF v2

我們在 LIFF v2 中新增了 `liff.shareTargetPicker()` 與 `liff.ready`。

## liff.shareTargetPicker()

執行 `liff.shareTargetPicker()` 方法可顯示 target picker（選擇群組或好友的畫面），並將開發者所建立的訊息傳送給選定的對象。此訊息會以彷彿你傳送的形式出現在你的群組或好友。

![target picker](https://developers.line.biz/media/news/share-target-picker.png)

詳情請參閱 LIFF 文件中的 [Sending messages to a user's friend (share target picker)](https://developers.line.biz/en/docs/liff/developing-liff-apps/#share-target-picker)。

<!-- note start -->

**Target picker 運作環境**

Target picker 由 iOS 與 Android 的 LINE 10.3.0 支援。

<!-- note end -->

## liff.ready

透過 `liff.ready`，你可以取得在啟動 LIFF app 後首次執行 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 時解析的 `Promise` 物件。如果你使用 `liff.ready`，你可以在 `liff.init()` 完成之後執行任何處理。

詳情請參閱 LIFF v2 API reference 中的 [liff.ready](https://developers.line.biz/en/reference/liff/#ready)。

2020/02/07

## Notice about LIFF v1 APIs and discontinuation schedule change

我們[曾公告 LINE Front-end Framework (LIFF) server API 的生命週期終止預定於 2020 年 3 月 31 日](https://developers.line.biz/en/news/2020/01/21/liff-server-api-deprecation/)。由於收到的回饋，我們將繼續提供該 API。

至於 LIFF v1，我們會在停止服務時程確定後立即公告。在此期間，我們建議你盡快從 v1 遷移至 v2。

Feature | Schedule before this update | Schedule after this update
-|-|-
[LIFF v1 Client API](https://developers.line.biz/en/reference/liff-v1/#client-api) | Scheduled for discontinuation | Scheduled for discontinuation (This has not changed)
[LIFF v1 Server API](https://developers.line.biz/en/reference/liff-v1/#server-api)  | Scheduled for discontinuation on March 31, 2020 | **Support continues**

<!-- note start -->

**LIFF v1 仍將停止服務**

如同 [2019 年 10 月 16 日](https://developers.line.biz/en/news/2019/10/16/liff-v2-released/)所公告，LIFF v1 將停止服務。請使用最新版本的 LIFF。

<!-- note end -->

2020/02/05

## Users can no longer add LIFF apps to Messaging API channels

如同 [2019 年 11 月 11 日](https://developers.line.biz/en/news/2019/11/11/liff-cannot-be-used-with-messaging-api-channels/)所公告，由於 LIFF v2 的功能強化，使用者無法再將 LIFF app 新增至 Messaging API 頻道。

關於已新增至 Messaging API 頻道之 LIFF app 的限制，以及如何過渡至 LINE Login 頻道，請參閱上述消息文章。

2020/01/21

## LIFF v1 Server API end-of-life on March 31, 2020

2020 年 3 月 31 日標誌著 **LINE Front-end Framework (LIFF) v1 Server API** 的生命週期終止日。在該日，以下功能將被移除：

- [Server API](https://developers.line.biz/en/reference/liff-server/)
    - [Adding the LIFF app to a channel](https://developers.line.biz/en/reference/liff-server/#add-liff-app)
    - [Update LIFF app settings](https://developers.line.biz/en/reference/liff-server/#update-liff-app)
    - [Get all LIFF apps](https://developers.line.biz/en/reference/liff-server/#get-all-liff-apps)
    - [Delete LIFF app from a channel](https://developers.line.biz/en/reference/liff-server/#delete-liff-app)

<!-- note start -->

**使用最新版本的 LIFF**

如同 [2019 年 10 月 16 日](https://developers.line.biz/en/news/2019/10/16/liff-v2-released/)所公告，LIFF v1 將停止服務。

<!-- note end -->

## Use LIFF v2

所有停止服務的 Server API 功能都可以在 [LINE Developers Console](https://developers.line.biz/console/) 中使用。關於如何將 LIFF app 新增至頻道的詳情，請閱讀以下內容：

- [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/)

你可以用相同的流程使用其他功能。

LINE 將持續提升其服務品質。感謝你的理解。

2020/01/14

## Update your code that uses the suspended LIFF SDK API

如同 [2019 年 11 月 29 日](https://developers.line.biz/en/news/2019/11/29/liff-functions-suspended/)所公告，由於技術問題，以下這些 API 在 LINE v9.19.0 及更新版本的 iOS 上已暫時停用。

* liff.scanCode()
* liff.bluetooth.*

從今天起，對於在 **LINE v9.19.0 及更新版本的 iOS** 上使用 LIFF app 的終端使用者，各 API 的運作方式如下。

API | Function
-|-
liff.scanCode() | API 為 `undefined`
liff.bluetooth.* | 如果在呼叫 `liff.initPlugins(['bluetooth'])` 時 Bluetooth 外掛初始化失敗，會回傳 `FORBIDDEN` 錯誤。

如果你使用 `liff.scanCode()`，我們建議你也考量上述情況並驗證該函式是否存在。

修改前：

```
liff.scanCode().then(result => {
  // result = { value: '' }
});
```

修改後：

```
if (liff.scanCode) {
  liff.scanCode().then(result => {
    // result = { value: '' }
  });
}
```

詳情請參閱 [LIFF v2 API reference](https://developers.line.biz/en/reference/liff/)。

LINE 將持續提升其服務品質。感謝你的理解。

2019/11/29

## Some LIFF functions suspended

由於技術問題，我們已暫時停用以下 LIFF 功能。一旦情況有變，我們會立即通知你。

- `liff.scanCode()`
- `liff.bluetooth.*`

## Impacted environments

Environment | Version
-- | --
LINE for iOS | 在版本 9.19.0 及更新版本上，上述功能暫時無法使用。
LINE for Android | 目前不受影響，但很快會有更多消息。

對於造成的不便，我們深表歉意，並正全力解決問題。

2019/11/11

## Users can no longer add LIFF apps to Messaging API channels

LIFF v2 預定更新為以 LINE Login 作為核心頻道。此外，即將到來的變更將完全禁止使用者將 LIFF app 新增至 Messaging API 頻道。我們強烈建議使用者將 LIFF app 新增至 LINE Login 頻道。

## Scheduled change date

2020 年 2 月初

## Impact

Channel type | Impact
-|-
LINE Login channel | 不受影響。
Messaging API channel| 規格變更後，**無法**將 LIFF app 新增至 Messaging API 頻道。規格變更時已新增至 Messaging API 頻道的 LIFF app 仍可使用。

<!-- note start -->

**請勿將 LIFF app 新增至 Messaging API 頻道**

目前，使用者可以將 LIFF app 新增至 Messaging API 頻道。然而，由於以下限制，我們強烈建議不要這麼做：

- 無法使用 bot link 功能。
- 可能不支援 LIFF 功能擴充。
- LIFF app 未來可能無法使用。

新增至 LINE Login 頻道的 LIFF app 沒有限制，可以使用所有 LIFF v2 功能。

<!-- note end -->

## Transition to the LINE Login channel

若要繼續使用新增至 Messaging API 頻道的 LIFF app，請將該 LIFF app 重新新增至 LINE Login 頻道。重新新增後，LINE Developers Console 會發行新的 LIFF app ID。因此，請注意以下事項：

- 如果你使用 LIFF v2，請變更 `liff.init()` 中所指定的 LIFF app ID。
- 用於啟動 LIFF 的 LIFF URL（例如：line://app/1234567890-AbcdEfgh）將會變更。

<!-- note start -->

**移除新增至 Messaging API 頻道的 LIFF app**

為避免混淆，請在新增至 LINE Login 頻道後，刪除新增至 Messaging API 頻道的 LIFF app。

<!-- note end -->

2019/10/16

## LIFF v2 released 

LINE Front-end Framework (LIFF) v2 是 LINE 提供的網頁應用程式平台。

<!-- note start -->

**使用最新版本的 LIFF**

LIFF v1 將被棄用。

<!-- note end -->

### LIFF apps now run in external browsers

在 LIFF v1 中，LIFF app 只能在 LIFF 瀏覽器中執行。在 LIFF v2 中，LIFF app 也可以在外部瀏覽器中執行。這表示你可以使用與一般網頁應用程式相同的開發環境來開發 LIFF app。

### Get user profile and email

由於與 LINE Login v2.1 的相容性已改善，你可以從 LINE Platform 取得使用者的 ID 與電子郵件地址。你的 LIFF app 可以使用這些資料來提供與使用者資訊及傳送電子郵件相關的功能。

此外，即使你的 LIFF app 在外部瀏覽器中執行，你也可以使用 LINE Login（網頁登入流程）。這表示即使 LIFF app 在外部瀏覽器中執行，你也可以使用相同的資訊。

### Read QR codes

你可以啟動 LINE 的 QR code 讀取器，並取得使用者讀取的字串。

### Get LIFF app environment information

你可以取得 LIFF app 執行環境的以下詳細資訊：

- LIFF app 執行所在的作業系統（iOS、Android、外部瀏覽器）
- LIFF app 是否在 LIFF 瀏覽器中執行（true、false）
- 語言設定

詳情請參閱 [LINE Front-end Framework](https://developers.line.biz/en/docs/liff/overview/)。

2019/04/23

## Improved consent screen in LINE Front-end Framework

我們改善了隨 LINE Front-end Framework (LIFF) 附帶的同意畫面（consent screen）。此改善會自動套用到所有 LIFF app。無需額外的開發工作。

![New consent screen](https://developers.line.biz/media/news/liff-consent-screen-changed-01.png)

如同此次更新之前，使用者可以選擇不允許 LIFF app 向聊天傳送訊息。但如果他們這麼做，與以往不同的是，使用者下次啟動 LIFF app 時，同意畫面會再次出現。

2019/02/07

## You can get access tokens through LIFF SDK

我們在 LIFF SDK 中新增了 `liff.getAccessToken()` 方法。

使用該存取權杖（access token）與 [Social API](https://developers.line.biz/en/docs/social-api/overview/) 互動，以存取 LINE Platform 上的使用者個人檔案資料。

詳情請參閱 [Getting the user's access token](https://developers.line.biz/en/docs/liff/developing-liff-apps/#getting-tokens)。

2018/11/16

## Renewed LIFF server API

現在你可以為你的 LIFF app 設定以下屬性。

 - `description` 屬性
 - `features.ble` 屬性

更新 LIFF app 的 API 端點 HTTP 請求已從 `PUT` 變更為 `PATCH`。現在你可以部分更新你 LIFF app 的屬性。

詳情請參閱以下各節：

 - [Add LIFF app](https://developers.line.biz/en/reference/liff-server/#add-liff-app)
 - [Update LIFF app](https://developers.line.biz/en/reference/liff-server/#update-liff-app)

2018/10/30

## LIFF apps can now be added with the LINE Developers Console

現在你可以使用 [LINE Developers Console](https://developers.line.biz/console/) 新增 LIFF app。如同以往，你仍然可以使用 LIFF server API 新增 LIFF app。

詳情請參閱 [Adding a LIFF app](https://developers.line.biz/en/docs/liff/registering-liff-apps/)。

2018/07/19

## The maximum number of LIFF apps has been increased

現在你可以為一個頻道新增最多 30 個 LIFF app。先前的上限為 10 個。

詳情請參閱 LIFF API reference 文件中的 [Add LIFF app](https://developers.line.biz/en/reference/liff-server/#add-liff-app)。

2018/06/06

## LINE Front-end Framework released

LINE Front-end Framework (LIFF) 是在 LINE 中運行的網頁應用程式平台。

當在 LINE 中啟動已註冊於 LIFF 的網頁應用程式（LIFF app）時，LIFF app 可以從 LINE Platform 取得資料，例如 LINE 使用者 ID。LIFF app 可以使用這類資料來提供運用使用者資訊的功能，並代表使用者傳送訊息。

詳情請參閱 [LINE Front-end Framework](https://developers.line.biz/en/docs/liff/overview/)。
