# LINE MINI App 介紹（Introducing LINE MINI App）

LINE MINI App 是一種在 LINE 上執行的網頁應用程式。LINE MINI App 讓使用者無需另外安裝原生應用程式（native app），即可享受各種服務。

「LINE MINI App」是正式名稱。

LINE MINI App 是一個網頁瀏覽器，因此可使用大多數的 HTML5 規格。詳情請參閱 [LINE MINI App specifications](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)。

## Introduction 

任何符合 [LINE MINI App Policy](https://terms2.line.me/LINE_MINI_App?lang=en) 中所定義之許可顧客資格者，皆可開發 LINE MINI App。請先參閱 [Quick Start Guide](https://developers.line.biz/en/docs/line-mini-app/quickstart/)。

要開始開發 LINE MINI App 頻道（channel），你需要有一個 [LINE Developers Console](https://developers.line.biz/console/) 帳號。從 LINE MINI App 設定到提交應用程式進行審查等許多作業，都在 LINE Developers Console 上進行。

## Things you can do with LINE MINI App 

LINE MINI App 提供下列[內建功能](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/)。

- 與其他使用者分享 LINE MINI App 的功能
- 請求使用者授權使用服務的功能。

你也可以在 LINE MINI App 上加入下列[自訂功能](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/)，進一步提升使用者體驗。

- Service Messages
- 使用付款系統（Payment Systems）
- 自訂操作按鈕（Custom action button）

<!-- tip start -->

**試用 LINE MINI App**

LY Corporation 為開發者提供一個名為 [LINE MINI App Playground](https://miniapp.line.me/lineminiapp_playground) 的 LINE MINI App。在安裝有 LINE app 的智慧型手機上開啟 LINE MINI App Playground，你便能實際試用 LINE MINI App 的部分功能。

<!-- tip end -->

## Unverified MINI Apps and verified MINI Apps 

LINE MINI App 依其是否通過我們的驗證審查（verification review），分為 unverified MINI App 與 verified MINI App。關於兩者的差異，請參閱下列章節：

### What are unverified MINI Apps 

Unverified MINI App 是指尚未通過我們驗證審查的 LINE MINI App。當你建立 LINE MINI App 頻道後，在通過驗證審查之前，該 LINE MINI App 都會是 unverified MINI App。

任何人都可以建立 unverified MINI App，但如下一節「[What are verified MINI Apps](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#verified-mini-app)」所述，部分功能會受到限制。若要讓你的 LINE MINI App 成為 verified MINI App，請[提交你的 LINE MINI App 進行審查](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)。

### What are verified MINI Apps 

如果你的 LINE MINI App 通過我們的驗證審查，它就會成為 verified MINI App。一旦成為 verified MINI App，它便會在標題列（header）等處顯示驗證徽章（verified badge），如下圖所示：

![](https://developers.line.biz/media/news/2024/line-mini-app-header-after.png)

此外，你還能使用如下功能：

- [將 LINE MINI App 的捷徑加入使用者裝置的主畫面](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)
- [Custom Path](https://developers.line.biz/en/docs/line-mini-app/develop/custom-path/)
- [Channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/)

如上所述，將你的 LINE MINI App 變成 verified MINI App，能在可靠性與便利性方面提升使用者體驗。關於 verified MINI App 可使用的功能的詳細資訊，請參閱 [Custom Features](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/)。

## LINE MINI App Components 

LINE MINI App 頁面由 (A) 標題列（Header）與 (B) 主體（Body）所組成。詳情請參閱 [LINE MINI App UI components](https://developers.line.biz/en/docs/line-mini-app/discover/ui-components/)。

![LINE MINI App structure](https://developers.line.biz/media/line-mini-app/mini_concept.png)

## Ways in which users can access LINE MINI Apps 

使用者不僅能在 LINE 內，也能從 LINE 外存取 LINE MINI App。在 LINE 內存取 LINE MINI App 有多種方式。

### Access from outside of LINE 

如果你能取得 [LINE MINI App Permanent Link](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)，便可從 LINE 外存取 LINE MINI App。你可以透過下列方式與使用者分享 LINE MINI App 的永久連結（permanent link）：

- 張貼於網站、電子郵件、簡訊等
- 為各種媒體建立 QR code

此外，透過[將 LINE MINI App 的捷徑加入使用者裝置的主畫面](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)，使用者便能直接從主畫面存取 LINE MINI App。

### LINE Official Account 

使用者也可以從 LINE 官方帳號（LINE Official Account）存取 LINE MINI App。例如，在你透過 LINE 官方帳號傳送給好友的圖文訊息（rich message），以及顯示於聊天畫面的圖文選單（rich menu）中，都會加入指向 LINE MINI App 的連結。詳情請參閱 [Use LINE Official Account](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/)。

![You can promote your LINE MINI App on the LINE Official Account](https://developers.line.biz/media/line-mini-app/mini_with_oa.png)

### Home Tab 

<!-- note start -->

**將 LINE MINI App 釘選至 LINE 主頁（Home）分頁的功能已停止提供**

詳情請參閱 2024 年 1 月 9 日的消息：[Users can now access recently used LINE MINI Apps from the LINE Home tab](https://developers.line.biz/en/news/2024/01/09/line-mini-app-history/)。

<!-- note end -->

使用者可以從 LINE 主頁（**Home**）分頁的**服務**（**Services**）中存取最近使用過的 LINE MINI App。**服務**區段會依最後使用順序，最多顯示 8 個最近使用過的 LINE MINI App。此功能僅適用於 verified MINI App。

主頁分頁的顯示政策會因提供服務的地區而異。

![](https://developers.line.biz/media/line-mini-app/mini-access-home-tab-en.png)

### Searching on LINE 

你也可以從 LINE 的搜尋功能存取 LINE MINI App。此功能僅適用於 verified MINI App。

![Access from search](https://developers.line.biz/media/line-mini-app/mini_access_search.png)

### LINE Message 

使用者可以輕鬆地與好友分享 LINE MINI App。我們提供[內建操作按鈕（built-in action button）](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)，讓使用者能輕鬆在好友之間分享 LINE MINI App，但你也可以選擇[實作自訂操作按鈕](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/)。

![Share message](https://developers.line.biz/media/line-mini-app/mini_access_share.png)

## Features available on LIFF apps but not on LINE MINI Apps 

| 項目 | 說明 |
| --- | --- |
| 隱藏操作按鈕（Module mode） | 你無法隱藏 LINE MINI App 上的[操作按鈕（action button）](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)。對於已加入 LINE MINI App 頻道的 LIFF app，無法設定 **Module Mode**。 |
| 在同一個頻道中加入多個 LIFF app | 在 LINE MINI App 頻道中，無法在同一個頻道中加入多個網頁應用程式。 |

<!-- tip start -->

**我們建議將 LIFF app 建立為 LINE MINI App**

未來，LIFF 與 LINE MINI App 將整合為單一品牌。整合後，LIFF 將併入 LINE MINI App。因此，我們建議你將新的 LIFF app 建立為 LINE MINI App。詳情請參閱 [2025 年 2 月 12 日](https://developers.line.biz/en/news/2025/02/12/line-mini-app/)的消息。

<!-- tip end -->
