# 開啟 LIFF app（Opening a LIFF app）

LIFF app 可以在 [LIFF 瀏覽器（LIFF browser）](https://developers.line.biz/en/glossary/#liff-browser)或[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟。

本頁說明使用者如何開啟 LIFF app，以及 LIFF app 開啟時的行為。

<!-- table of contents -->

## User actions when opening the LIFF app 

本節說明使用者開啟 LIFF app 時的操作。

1. 使用者存取 [LIFF URL](https://developers.line.biz/en/glossary/#liff-url)。

   LIFF URL 會在[將 LIFF app 新增至你的頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時發行。\
   例如，將 LIFF URL 傳送到 LINE app 的聊天室，並點選泡泡訊息中顯示的 LIFF URL。

   ![](https://developers.line.biz/media/liff/open-liff-app.png)

1. 如果需要使用者授權，會出現頻道同意畫面。使用者在同意畫面上同意授予 LIFF app 所需的權限。

   ![Consent screen](https://developers.line.biz/media/line-login/integrate-login-web/consent-screen-en.png)

1. LIFF app 開啟。

   ![LIFF browser](https://developers.line.biz/media/liff/overview/liffBrowser.png)

### Environment where the LIFF app opens when a user access the LIFF URL 

當使用者存取 LIFF URL 時，LIFF app 會在 LINE app 上的 [LIFF 瀏覽器（LIFF browser）](https://developers.line.biz/en/glossary/#liff-browser)或[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟。

LIFF URL 相容於 iOS 上的 [universal links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/) 與 Android 上的 [app links](https://developer.android.com/training/app-links)。因此，如果你從 LINE app 以外的地方開啟 LIFF URL，LIFF 瀏覽器會在 LINE app 上開啟。

然而，視使用者作業系統的規格而定，即使在 Safari 或 Chrome 等外部瀏覽器上，universal links 或 app links 也可能無法運作，導致 LIFF 瀏覽器無法在 LINE app 上開啟。此外，當在 LINE app 以外的原生 app 上存取 LIFF URL 時，LIFF app 究竟是在外部瀏覽器還是 LIFF 瀏覽器中開啟，取決於該原生 app 的 WebView 規格。

基於這些原因，我們無法保證存取 LIFF URL 時 LIFF app 會在哪個環境中開啟。請注意，即使使用者存取 LIFF URL，LIFF 瀏覽器也可能不會在 LINE app 上開啟。

## Behaviors from accessing the LIFF URL to opening the LIFF app 

以下說明如何設定兩個重新導向目的地，使 LIFF app 在使用者存取 LIFF URL 時能正確開啟，以及在使用者存取 LIFF URL 時何時執行 `liff.init()` 方法。

| Redirect to | Description |
| --- | --- |
| Primary redirect URL | 使用者第一次存取 LIFF URL 時，會從 LIFF 伺服器重新導向至此 URL。當使用者被重新導向至此 URL 時，執行 `liff.init()` 方法。 |
| Secondary redirect URL | 執行 `liff.init()` 方法時，使用者會被重新導向至此 URL。一旦使用者被重新導向至此 URL，便會顯示 LIFF app 頁面。 |

![Redirect flow](https://developers.line.biz/media/liff/redirect-flow-en.png)

### Create a LIFF URL 

LIFF URL 是指向 LY Corporation 所提供之 LIFF 伺服器的 URL。LIFF URL 會在[將 LIFF app 新增至你的頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/)時發行。

LIFF URL 範例：`https://liff.line.me/1234567890-AbcdEfgh`

#### Supported LIFF URLs 

支援下列 LIFF URL：

- `https://liff.line.me/{liffId}`&nbsp;
- `https://miniapp.line.me/{liffId}`（僅適用於 LINE MINI App）

<!-- note start -->

**「https://line.me/R/app/{liffId}」與「line://app/{liffId}」已淘汰**

下列在 [LIFF v1](https://developers.line.biz/en/docs/liff/versioning-policy/#life-cycle-schedule) 中使用的 LIFF URL 格式已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)：

- `https://line.me/R/app/{liffId}`&nbsp;
- `line://app/{liffId}`&nbsp;

<!-- note end -->

### Create a primary redirect URL 

Primary redirect URL 永遠是 LINE Developers Console 的 **Endpoint URL** 中所指定的 URL。

<!-- note start -->

**LIFF URL 中指定的額外資訊**

在 primary redirect URL 中指定的所有額外資訊（例如 `path_A/?key1=value1#URL-fragment`）都會包含在 `liff.state` 查詢參數中。

例如 `https://example.com/2020campaign/?key=value&liff.state=urlencoded(path_A/?key1=value1#URL-fragment)`

如果你未在 LIFF URL 中指定任何額外資訊，則會省略 `liff.state` 查詢參數。

<!-- note end -->

### Create a secondary redirect URL 

Secondary redirect URL 取決於使用者所存取的 URL。

在 LINE Developers Console 的 **Endpoint URL** 中指定的路徑與查詢參數（`/2020campaign/?key=value`）會包含在 secondary redirect URL 中。

| URL that users access | Secondary redirect URL |
| --- | --- |
| LIFF URL (1)<br>例如 `https://liff.line.me/{liffId}` | LINE Developers Console 的 **Endpoint URL** 中所指定的 URL。<br>例如 `https://example.com/2020campaign/?key=value` |
| 包含額外資訊的 LIFF URL (2)<br>例如 `https://liff.line.me/{liffId}/path_A/?key1=value1#URL-fragment` | 如下圖 (2) 所示，此 URL 由 3 種資訊組合而成。<ul><li>在 **Endpoint URL** 中指定的網域名稱（`https://example.com`）</li><li>在 **Endpoint URL** 中指定的路徑與查詢參數（`/2020campaign/?key=value`）。</li><li>在 LIFF URL 中指定的額外資訊（`/path_A/?key1=value1#URL-fragment`）</li></ul>例如 `https://example.com/2020campaign/path_A/?key=value&key1=value1#URL-fragment` |

![Endpoint URL](https://developers.line.biz/media/liff/endpoint-url.png)

## Opening a LIFF app from another LIFF app (LIFF-to-LIFF transition) 

當 LIFF app 在 LIFF 瀏覽器中開啟時，你可以點選連結前往另一個 LIFF app，並在保持 LIFF 瀏覽器開啟的狀態下顯示該另一個 app。由於 LIFF 瀏覽器在 LIFF-to-LIFF 轉換期間不會關閉，因此你可以點選 LIFF 瀏覽器上的返回按鈕，回到轉換前的 LIFF app。

- [使 LIFF-to-LIFF 轉換得以進行的條件](https://developers.line.biz/en/docs/liff/opening-liff-app/#conditions-liff-to-liff)
- [依 LIFF app 畫面大小而定的行為](https://developers.line.biz/en/docs/liff/opening-liff-app/#behavior-by-screen-size)
- [關於 LIFF app 之間轉換後的「chat_message.write」scope](https://developers.line.biz/en/docs/liff/opening-liff-app/#about-chat-message-write-scope)
- [取得 LIFF-to-LIFF 轉換前的 URL](https://developers.line.biz/en/docs/liff/opening-liff-app/#using-liff-referrer)
- [開啟另一個 LIFF app 時顯示的訊息](https://developers.line.biz/en/docs/liff/opening-liff-app/#messages-liff-to-liff)

![LIFF-apps-transition](https://developers.line.biz/media/liff/liff_transition.png)

<!-- note start -->

**非預期的行為**

如果你使用的是較舊版本的 LIFF SDK，可能會遇到下列非預期的行為：

- 儘管你從以路徑（`/path`）指定的 LIFF URL 移動到另一個 LIFF app，你最終仍會停留在 LINE Developers Console 的 **Endpoint URL** 中所指定的 URL。
- 如果你在尋求使用者授權的[同意畫面（Consent screen）](https://developers.line.biz/en/docs/line-login/link-a-bot/)上點選**取消**，你必須先關閉一次 LIFF 瀏覽器。
- 如果目的地是 LINE MINI App，LIFF 瀏覽器標頭的設計不會自動變更。

在設計使多個 LIFF app 之間能夠轉換的功能時，建議你使用最新版本的 LIFF SDK。

<!-- note end -->

### The conditions that make LIFF-to-LIFF transitions possible 

在滿足下列所有條件時，LIFF-to-LIFF 轉換才得以進行：

- LIFF SDK v2.4.1 或更新版本
- 原始 LIFF app 畫面設定為 `Full` 顯示
- 要移動前往的 LIFF app 已正確透過 `liff.init()` 初始化

### Behavior based on screen size of the LIFF app 

- 如果原始 LIFF app 的畫面大小設定為 `Tall` 或 `Compact`，則無論你想移動前往的 LIFF app 畫面大小為何，瀏覽器都會先關閉，之後才會顯示目的地 LIFF app。
- 如果原始 LIFF app 的畫面大小設定為 `Full`，則無論目的地 LIFF app 的畫面大小規格為何，目的地 LIFF app 的畫面大小都會以 `Full` 顯示。
- 如果原始 LIFF app 的畫面大小設定為 `Full`，而轉換目的地 LIFF app 的畫面大小為 `Tall` 或 `Compact`，則轉換後的 LIFF app 中不會顯示[動作按鈕（action button）](https://developers.line.biz/en/docs/liff/overview/#action-button)。

### About the "chat_message.write" scope after transitioning between LIFF apps 

LIFF app 之間轉換後的 `chat_message.write` scope 是否啟用，取決於轉換目的地 URL。

| Transition destination URL | Example URL | The `chat_message.write` scope after transition |
| --- | --- | --- |
| LIFF URL | `https://liff.line.me/{liffId}` | **啟用** |
| 包含額外資訊的 LIFF URL | `https://liff.line.me/{liffId}/path_A/?key1=value1#URL-fragment` | **啟用** |
| Endpoint URL | `https://example.com` | **停用** |

如果 `chat_message.write` scope 已啟用，則可在轉換目的地 LIFF app 中使用 [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 方法。

### Get URL from before LIFF-to-LIFF transition 

當你在 LIFF-to-LIFF 轉換期間開啟 LIFF app 時，查詢參數 `liff.referrer` 會被加入轉換後的 LIFF app URL 中。`liff.referrer` 的值會被設定為 LIFF 伺服器在 LIFF-to-LIFF 轉換期間所收到 `Referer` 請求標頭位址的 [percent-encoded](https://en.wikipedia.org/wiki/Percent-encoding) URL。透過檢查 `liff.referrer` 的值，你可以取得轉換前的 URL。

<!-- note start -->

**在 LINE 版本 12.13.0 至 13.19.x 中，LIFF-to-LIFF 轉換後不會將 liff.referrer 加入 LIFF app URL**

詳情請參閱 2023 年 11 月 30 日的消息，[我們已修正 LINE 版本 12.13.0 或更新版本中 LIFF-to-LIFF 轉換後未加入 liff.referrer 的錯誤](https://developers.line.biz/en/news/2023/11/30/liff-update-line-13-20-0/)。

<!-- note end -->

以下是 LIFF-to-LIFF 轉換期間如何給予 `liff.referrer` 的範例。

|  | 轉換前的 LIFF app URL | 連結的 URL | 轉換後的 LIFF app URL（執行 `liff.init()` 方法後） |
| --- | --- | --- | --- |
| **會給予** | `https://first.example.com/` | `https://liff.line.me/{LIFF ID}`<br> (LIFF URL) | `✅ https://second.example.com/?liff.referrer=https%3A%2F%2Ffirst.example.com%2F` \*1 |
| **不會給予** | `https://first.example.com/` | `https://second.example.com/`<br> (Endpoint URL) | `❌ https://second.example.com/` \*2 |

\*1 除了 `liff.referrer` 之外，轉換後的 LIFF app URL 還可能會被給予 `liff.*` 查詢參數。<br>\*2 如果直接開啟 LIFF app 的 endpoint URL，則不會給予 `liff.referrer`。

### Message displayed when another LIFF app is opened 

當你從某個 LIFF app 存取另一個 URL 時，可能會顯示「Switched to the {LIFF app name} app.」這樣的訊息。

當你開啟的 LIFF app 與最先開啟的 LIFF app（即轉換來源的 LIFF app）擁有不同的 LIFF ID 時，便會顯示此訊息。是否顯示此訊息與 LIFF-to-LIFF 轉換是否成功無關。

![](https://developers.line.biz/media/liff/switched-to-another-app-en.png)
