# 送審 LINE MINI App（Submitting LINE MINI App）

當你建立一個 LINE MINI App 頻道（channel）時，這個 LINE MINI App 屬於未驗證的 MINI App，部分功能會受到限制。若要將開發完成的 LINE MINI App 變成已驗證的 MINI App，必須經過 LY Corporation 的審查。本頁將說明如何送出審查申請。

<!-- tip start -->

**關於台灣或泰國地區 LINE MINI App 的驗證審查**

如果提供服務的國家或地區為台灣或泰國，只有隸屬於[認證提供者（certified provider）](https://developers.line.biz/en/docs/line-developers-console/overview/#certified-provider)的 LINE MINI App 頻道才能申請驗證審查。關於如何申請成為認證提供者的詳細資訊，請參閱以下內容：

- 台灣：[LINE Biz-Solutions](https://tw.linebiz.com/service/other-solutions/line-mini-app/)
- 泰國：[LINE for Business](https://lineforbusiness.com/th/service/mini-app)

<!-- tip end -->

## Things to check prior to requesting review of your LINE MINI App 

在申請審查前，請先確認以下事項：

- 確認你的 LINE MINI App 是否遵守所有指南與規則。<br>特別請確認以下指南與規則：
  - [LINE MINI App 圖示規格與指南](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/)
  - [橫向模式的安全區域](https://developers.line.biz/en/docs/line-mini-app/design/landscape/)
  - [載入圖示](https://developers.line.biz/en/docs/line-mini-app/design/loading-icon/)
  - [實作自訂動作按鈕](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/)
  - [效能指南](https://developers.line.biz/en/docs/line-mini-app/develop/performance-guidelines/)
- 確認你的 LINE MINI App 是否遵守 [LINE MINI App Policy](https://terms2.line.me/LINE_MINI_App?lang=en)
- 確認你在 [LINE Developers Console](https://developers.line.biz/console/) 上為 LINE MINI App 頻道所登錄的資訊是否正確且最新。
  - 提供者名稱必須與「服務提供者」相同。
  - 必須在[頻道說明（Channel description）](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#channel-description)中提供正確的服務說明。
  - 在隱私權政策中，取得使用者資料的公司必須與提供者名稱設定為同一家公司。
- 確認 Published 頻道的 LIFF URL 與 Review 頻道的 LIFF URL 反映的是相同的服務。
  - 審查期間，LY Corporation 會檢查 Review 頻道的 LIFF URL。頻道與 LIFF 中的各項設定會自動複製並反映到 Review 頻道上。然而，請事先確認 Review 頻道的 LIFF URL 反映的服務與 Published 頻道的 LIFF URL 相同。

### Review period 

LY Corporation 完成審查流程大約需要 1 至 2 週。如果你的申請遭到拒絕，重新申請與重新審查可能需要再多花幾天時間。你無法指定審查的完成日期。請預留充裕的時間來進行審查申請。

### When requesting review for multiple LINE MINI Apps 

當你同時申請多個 LINE MINI App 的審查時（同一套裝產品的多個，或同一品牌的多個等等），我們建議遵循以下流程，以避免重複作業並縮短審查時間：

1. 首先，先針對其中一個 LINE MINI App 申請審查。
2. 待該 LINE MINI App 通過核可後，再申請批次審查。

## Review Process 

一般的審查流程如下。

### 1. Submit an application for review in the LINE Developers Console 

在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Review request** 分頁中輸入必填資訊，並送出審查申請。

待 LY Corporation 完成審查流程後，審查結果會顯示在 [LINE Developers Console](https://developers.line.biz/console/) 上，同時也會寄送到你在 LINE Developers Console 上登錄的電子郵件地址。

如果你已透過基本驗證（basic authentication）限制了作為審查對象的 LINE MINI App 的存取權限，請在申請審查時於 **Review request** 分頁的 **Reference materials for the review** 中告知我們使用者名稱與密碼。詳細資訊請參閱[在發布前使用基本驗證限制 LINE MINI App 的存取](https://developers.line.biz/en/docs/line-mini-app/develop/develop-overview/#use-basic-authentication)。

#### Important points about the review 

- 申請審查後，只要審查流程尚未開始，你可以透過 **Review request** 分頁上的 **Cancel review request** 按鈕取消審查。
- 一旦 LY Corporation 開始審查流程，你就無法取消申請，也無法變更已輸入的資訊。
- 一旦審查開始且狀態變為「Reviewing」，你就可以存取 Review 頻道上的 LIFF URL。

#### Services that include actions such as reservations, payments, and orders 

對於包含預約、付款、訂購等動作的服務，在送出審查申請時，你必須在 **Reference materials for the review** 中輸入測試情境（帳號、商品、店家等）。

#### Channel description 

LY Corporation 的審查將以 [LINE Developers Console](https://developers.line.biz/console/) 中 **Basic settings** 分頁的 **Channel description** 所提供的資訊為基礎。因此，請參考以下範例提供正確的服務細節：

|  | Channel name | Channel description |
| --- | --- | --- |
| 不佳的範例 | LINE FRIENDS STORE | LINE FRIENDS STORE 是販售 LINE 角色商品的商店。 |
| 良好的範例 | LINE FRIENDS STORE | 這是 LINE FRIENDS STORE 的行動點餐服務。你可以事先點購並付款，再到店取貨。 |

關於 **Channel description** 的詳細資訊，請參閱[頻道說明（Channel description）](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#channel-description)。

#### When using in-app purchase 

如果你使用[應用程式內購買（in-app purchase）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)，你必須先[申請使用應用程式內購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/request-iap-review/)。

待你的應用程式內購買申請通過核可後，請在 **Review request** 分頁中開啟 **Apply to publish in-app purchase** 切換按鈕以送出審查。如果你的應用程式內購買申請尚未通過核可，即使開啟切換按鈕，你也無法送出審查以成為已驗證的 MINI App。

![](https://developers.line.biz/media/line-mini-app/in-app-purchase/in-app-purchase-toggle-en.png)

在你的應用程式內購買申請審查期間，你無法送出驗證審查申請。

此外，在驗證審查期間，你無法申請使用應用程式內購買功能。

### 2. After your LINE MINI App has been approved 

通過審查核可後的流程，取決於這是[你的 LINE MINI App 首次送審](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/#first-time)，還是[你的 LINE MINI App 已作為已驗證的 MINI App 發布](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/#verified-mini-app)。

#### When submitting your LINE MINI App for the first time 

待你的 LINE MINI App 通過核可後，你的頻道狀態會自動變更為「Approved」，並立即變為「Reflected」。透過 [LINE Developers Console](https://developers.line.biz/console/) 上 **Review request** 分頁的 **Search enable** 按鈕，使用者將能夠在 LINE 內搜尋你的 LINE MINI App。

即使你的狀態變成「Reflected」，由於尚未在 LINE 內啟用搜尋，使用者仍無法搜尋到你的服務。

當你想要讓你的服務可被搜尋時，點擊 **Search enable** 按鈕，使用者便能立即在 LINE 中搜尋到你的 LINE MINI App。然而，如果在狀態變成「Reflected」後 30 天內（含週末與假日）未啟用 **Search enable**，搜尋將會在第 31 天的日本標準時間（JST）上午 9:00 自動啟用。

舉例來說，如果你的 LINE MINI App 狀態在 8 月 1 日變成「Reflected」，「Search enable」功能將會在 8 月 31 日上午 9:00 自動啟用。

一旦啟用了你的 LINE MINI App 的搜尋功能，LINE MINI App 頻道的狀態會回到「Not yet reviewed」，你便能變更設定並重新送審。此時，在再次通過審查流程並點擊 **Publish changes** 按鈕之前，對設定所做的任何變更都不會影響目前已發布的 LINE MINI App。

<!-- note start -->

**狀態變更可能會有些許延遲**

雖然狀態應於第 31 天的日本標準時間（JST）上午 9:00 自動變更，但可能會有 1 至 2 小時的延遲。

<!-- note end -->

#### When your LINE MINI App has already been published as a verified MINI App 

如果 LINE MINI App 已經發布，流程會略有不同。

待你的 LINE MINI App 通過核可後，你的頻道狀態會變更為「Approved」。你必須透過 [LINE Developers Console](https://developers.line.biz/console/) 上 **Review request** 分頁的 **Publish changes** 按鈕，手動將頻道狀態變更為「Reflected」。

一旦你的狀態變成「Reflected」，審查申請時所做的變更會更新到 Published 頻道與 Published 頻道的 LIFF（例如 LINE MINI App 名稱、Channel settings、LIFF Settings 等等）。

當你想要發布你的 LINE MINI App 時，點擊 **Publish changes** 按鈕，狀態會立即變更為「Reflected」。然而，如果在狀態變成「Approved」後 30 天內（含週末與假日）未啟用 **Publish changes**，這些變更將會在第 31 天的日本標準時間（JST）上午 9:00 自動反映。

舉例來說，如果你的 LINE MINI App 狀態在 8 月 1 日變成「Approved」，新的變更將會在 8 月 31 日上午 9:00 自動啟用。

一旦新的變更啟用後，LINE MINI App 頻道的狀態會回到「Not yet reviewed」，你便能變更設定並重新送審。此時，在再次通過審查流程並點擊 **Publish changes** 按鈕之前，對設定所做的任何變更都不會影響目前已發布的 LINE MINI App。

<!-- note start -->

**狀態變更可能會有些許延遲**

雖然狀態應於第 31 天的日本標準時間（JST）上午 9:00 自動變更，但可能會有 1 至 2 小時的延遲。

<!-- note end -->

## Provider of a LINE MINI App channel that has passed review 

如果在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Basic settings** 分頁中將 **Region to provide the service** 設定為「Japan」，當 LINE MINI App 頻道通過審查後，其提供者將成為[認證提供者（certified provider）](https://developers.line.biz/en/docs/line-developers-console/overview/#certified-provider)。
