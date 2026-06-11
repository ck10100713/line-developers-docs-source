# LIFF 概觀（LIFF overview）

LINE Front-end Framework（LIFF）是 LY Corporation 提供的網頁應用程式平台。在此平台上執行的網頁應用程式稱為 LIFF app。

LIFF app 可以從 LINE Platform 取得資料，例如 LINE 使用者 ID。LIFF app 可運用這類資料，提供利用使用者資料的功能，並代表使用者傳送訊息。

如需 LIFF v2 新增功能的詳細資訊，請參閱[版本資訊](https://developers.line.biz/en/docs/liff/release-notes/)。

<!-- tip start -->

**在網頁上試用 LIFF 功能**

LY Corporation 為開發者提供了一個名為 [LIFF Playground](https://liff-playground.netlify.app/) 的網頁應用程式（LIFF app）。透過 LIFF Playground，您可以在網頁上試用基本的 LIFF 功能。[LIFF Playground 的原始碼](https://github.com/line/liff-playground)已在 GitHub 上公開。

<!-- tip end -->

<!-- note start -->

**LIFF app 不相容於 OpenChat**

目前 LIFF app 在 OpenChat 中尚未獲得官方支援，這表示有些功能無法運作。例如，在大多數情況下，無法透過 LIFF app 取得使用者的個人檔案資訊。

<!-- note end -->

## Recommended operating environment 

LIFF 建議的作業系統與 LINE 版本如下。

您可以使用哪些功能，取決於 LIFF app 是在 [LIFF browser](https://developers.line.biz/en/docs/liff/overview/#liff-browser) 還是[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟。例如，您無法在外部瀏覽器中使用 `liff.scanCode()`。如需詳細資訊，請參閱 [LIFF API reference](https://developers.line.biz/en/reference/liff/)。

### When the LIFF app is opened in a LIFF browser 

| 項目 | 建議環境 | 最低運作環境 |
| --- | --- | --- |
| iOS | 最新版本。使用 [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview)。 | 符合 LINE 的建議系統規格。\* |
| Android | 最新版本。使用 [Android WebView](https://developer.android.com/reference/android/webkit/WebView)。 | 符合 LINE 的建議系統規格。\* |
| LINE | 最新版本 | 符合 LINE 的建議系統規格。\* |

<!-- note start -->

**我們建議在 LIFF app 上使用最新版本的 OS 與 LINE**

我們建議您在 LIFF app 上使用最新版本的 OS 與 LINE。即使在上述「最低運作環境」之後的版本，部分功能仍可能無法運作，或畫面可能因設定而無法正常顯示。

<!-- note end -->

\* 如需 LINE 建議系統規格的詳細資訊，請參閱說明中心的 [Recommended system specifications for LINE](https://help.line.me/line/ios/pc?lang=en&contentId=10002433)。

### When the LIFF app is opened in an external browser 

LIFF app 在這些瀏覽器的最新版本上執行：

Microsoft Edge、Google Chrome、Firefox、Safari

## LIFF browser 

LIFF browser 是專為 LIFF app 設計的瀏覽器。當使用者在 LINE 中開啟 LIFF URL 時，LIFF app 會在 LIFF browser 中開啟。

![LIFF browser](https://developers.line.biz/media/liff/overview/liffBrowser.png)

由於 LIFF browser 在 LINE 中執行，LIFF app 無需提示使用者登入即可存取使用者資料。LIFF browser 還提供 LINE 特有的功能，例如能夠分享 LIFF app 以及傳送訊息給好友。

## LIFF browser specifications 

LIFF browser 在 iOS 中使用 [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview)，在 Android 中使用 [Android WebView](https://developer.android.com/reference/android/webkit/WebView)。因此，LIFF browser 的規格與行為也會依循這些機制。

LIFF browser 並不支援外部瀏覽器所支援的部分網頁技術。如需詳細資訊，請參閱 [The differences between the LIFF browser and external browser](https://developers.line.biz/en/docs/liff/differences-between-liff-browser-and-external-browser/)。

## LIFF browser cache 

LIFF browser 所使用的 [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) 與 [Android WebView](https://developer.android.com/reference/android/webkit/WebView)，可能會依據 HTTP 標頭（例如 [Cache-Control](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/Cache-Control)）的指示，將顯示的內容儲存為快取並加以使用。

請使用 HTTP 標頭（例如 [Cache-Control](https://developer.mozilla.org/ja/docs/Web/HTTP/Reference/Headers/Cache-Control)）來控制 LIFF browser 中的快取。

<!-- note start -->

**關於刪除快取**

目前沒有任何方法可以明確刪除儲存在 LIFF browser 中的快取。

<!-- note end -->

## Size of the LIFF browser 

LIFF browser 可以下列三種尺寸之一顯示。

![View size](https://developers.line.biz/media/liff/overview/viewTypes.png)

請在將 LIFF app 新增至您的 LINE Login 頻道（channel）時設定檢視尺寸。如需詳細資訊，請參閱 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

## Action button 

LIFF app 的檢視尺寸設定為 `Full` 時，預設會在標頭中顯示動作按鈕。

![](https://developers.line.biz/media/liff/overview/liff-header.png)

<!-- tip start -->

**隱藏動作按鈕**

在 LINE Developers Console 中啟用 LIFF app 的 **Module mode**，即可隱藏動作按鈕。如需詳細資訊，請參閱 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/)。

<!-- tip end -->

當您點擊動作按鈕時，會依您的 LINE app 版本顯示下列功能。動作按鈕的圖示會因您的 LINE 版本而有所不同。

| LINE app 版本                             | 可用功能          |
| ----------------------------------------- | ----------------- |
| 26.7.0 或更新版本                         | 下拉式選單        |
| 15.12.0 或更新版本，且早於 26.7.0          | 多分頁檢視        |
| 早於 15.12.0                              | 選項              |

### Dropdown menu 

在 LINE 26.7.0 或更新版本中，點擊動作按鈕會顯示下列下拉式選單：

| 項目 | 說明 |
| --- | --- |
| **All tabs** | 顯示[多分頁檢視（Multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)。 |
| **Refresh** | 重新載入目前頁面。 |
| **Minimize browser** | 將 LIFF browser 最小化。如需詳細資訊，請參閱 [Minimizing LIFF browser](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/)。 |
| **Share** | 透過 LINE 訊息分享目前頁面的[永久連結（permanent link）](https://developers.line.biz/en/glossary/#permanent-link-liff)。 |
| **Permission settings** | 開啟權限設定畫面。權限設定畫面可讓使用者檢視目前開啟的 LIFF app 的相機與麥克風權限。無法進行任何變更。於 LINE 14.6.0 或更新版本中可用。 |

<!-- note start -->

**永久連結分享可能失敗**

如果目前頁面的 URL 並非以 LINE Developers Console 的 **Endpoint URL** 中所指定的 URL 開頭，則無法取得永久連結，分享將會失敗。

<!-- note end -->

### Multi-tab view 

多分頁檢視會顯示您最近使用的服務。最近使用的服務區塊包含使用者開啟過的 LIFF app，依最近使用的順序顯示，最多 50 筆。

當使用者關閉 LIFF app 或開啟新的 LIFF app 時，會以該時間點擷取的螢幕截圖作為使用記錄顯示。使用者可透過使用記錄重新開啟 LIFF app。

當從使用記錄再次開啟 LIFF app 時，LIFF app 會恢復（resume）或重新載入（reload）。恢復與重新載入的規格如下：

| 重新開啟時的行為 | 條件 | 規格 |
| --- | --- | --- |
| LIFF app 將恢復 | <p>同時符合下列兩項條件的 LIFF app：</p><ul><li>在過去 12 小時內使用過的 LIFF app</li><li>包含在最近 10 筆使用記錄中的 LIFF app</li></ul> | LIFF app 將從使用者離開時的畫面恢復。存取權杖、瀏覽記錄與畫面捲動位置都會保留。 |
| LIFF app 將重新載入 | 若不符合恢復的條件 | LIFF app 將在使用者離開時的 URL 進行初始化。存取權杖、瀏覽記錄與畫面捲動位置都會被捨棄。 |

#### Conditions for appearing in recently used services 

若要將 LIFF app 顯示在最近使用的服務中，必須符合下列所有條件：

- LINE app 版本為 15.12.0 或更新版本
- 您的 LIFF app 的[螢幕尺寸（screen size）](https://developers.line.biz/en/docs/liff/overview/#screen-size)指定為 `Full`
- 您的 LIFF app 的 module mode 為關閉

#### Units displayed for recently used services 

在最近使用的服務中，LIFF app 會依 LIFF ID 顯示。如果使用者從最近使用的服務區塊以外的地方重新開啟同一個 LIFF app，則會開啟一個新的 LIFF app，而舊的 LIFF app 將被捨棄。

請注意，如果使用者在 LIFF 之間轉換（LIFF-to-LIFF transition）的過程中開啟另一個 LIFF app，即使 LIFF ID 不同，這些 LIFF app 也會被歸為一組，並顯示為單一 LIFF app。

#### The `liff.sendMessages()` method can't be used after reloading a LIFF app 

如果您在從最近使用的服務區塊重新載入的 LIFF app 中使用 [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 方法，將會發生錯誤。因此，當 LIFF app 被重新載入時，您無法使用 `liff.sendMessages()` 方法。

若要在重新載入 LIFF app 後使用 `liff.sendMessages()` 方法，請透過點擊聊天室等處的 LIFF URL 來重新開啟 LIFF app。

## Development guidelines 

使用 LIFF 開發網頁應用程式時，請遵循這些 [LIFF app 開發準則](https://developers.line.biz/en/docs/liff/development-guidelines/)。

## Tools to support LIFF app development 

LY Corporation 提供下列工具，協助開發者更順利地開發 LIFF app。

| 工具名稱 | 此工具的功能 |
| --- | --- |
| [LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/) | 這是為初次學習 LIFF 的人準備的入門應用程式。LIFF starter app 只是 LIFF app 初始化的示範，可協助您了解如何開始開發 LIFF app。建議給想要先做出能運作的東西、並大致了解 LIFF 是什麼的人使用。 |
| [Create LIFF App](https://developers.line.biz/en/docs/liff/cli-tool-create-liff-app/) | 此 CLI 工具可讓您用單一指令建立 LIFF app 的開發環境。就像 React 的 [Create React App](https://github.com/facebook/create-react-app) 或 Next.js 的 [Create Next App](https://nextjs.org/docs/pages/api-reference/cli/create-next-app) 一樣，透過回答 Create LIFF App 的問題，即可為您產生包含 LIFF app 範本的開發環境，並立即開始開發。 |
| [LIFF CLI](https://developers.line.biz/en/docs/liff/liff-cli/) | <p>一個協助您更順利開發 LIFF app 的 CLI 工具。LIFF CLI 可讓您執行下列操作：</p><ul><li>建立、更新、列出與刪除 LIFF app</li><li>建立 LIFF app 開發環境</li><li>使用 [LIFF Inspector](https://developers.line.biz/en/docs/liff/liff-plugin/#liff-inspector) 對您的 LIFF app 進行除錯</li><li>啟動具有 HTTPS 的本地開發伺服器</li></ul>[LIFF Mock](https://developers.line.biz/en/docs/liff/liff-plugin/#liff-mock) 功能將於未來的更新中加入。 |
| [LIFF Playground](https://liff-playground.netlify.app/) | 您可以線上試用 LIFF 的功能。[LIFF Playground 的原始碼](https://github.com/line/liff-playground)已在 GitHub 上公開，因此開發者可以設定自己的 LIFF ID，並在伺服器上部署自己的 LIFF Playground。 |

## Workflow 

若要讓終端使用者能夠使用 LIFF app，請依照下列步驟操作：

1. [建立一個頻道（channel）](https://developers.line.biz/en/docs/liff/getting-started/)，以便新增您的 LIFF app。
1. [試用 LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/)，或[開發 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/)。
