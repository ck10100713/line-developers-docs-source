# 營運你的服務（Running your service）

我們強烈建議服務設計者（Service Designer）、營運者（Operator）與行銷人員（Marketer）詳閱本指南並據以做好準備。

<!-- table of contents -->

## Sharing the LINE MINI App Link 

當你要分享 LINE MINI App 或其頁面時，你需要[建立永久連結（permanent link）](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)。在考慮透過以下方式分享 LINE MINI App 時，請特別使用永久連結：

- 在 LINE 以外的地方分享連結時，例如透過網頁、電子郵件與社群媒體。
- [透過 LINE 官方帳號（LINE Official Account）的圖文訊息或圖文選單分享時](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/)
- [實作自訂動作按鈕（custom action button）時](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/)
- 使用[服務訊息（service message）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)分享時。
- 使用附帶 QR code 的 LINE MINI App [POP template](https://creativelab-tips.line.me/ja/line-miniapp/creative/)（僅提供日文版）時

## Conditions for service messages 

你只能在作為對 LINE MINI App 上使用者動作的確認或回應時，才可發送[服務訊息（service message）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)。

### Notifications allowed by service messages 

服務訊息允許以下通知：

| Type | Use Case |
| --- | --- |
| 動作確認通知（Action Confirmation Notification） | <ul><li>餐廳與住宿預訂的確認通知</li><li>已購買票券與商品的確認通知</li></ul> |
| 動作結果通知（Action Result Notification） | <ul><li>報到完成通知</li><li>訂單出貨完成通知</li></ul> |
| 提醒通知（Reminder Notification） | <ul><li>餐廳與住宿預訂的提醒通知</li><li>已購買票券的戲劇、電影或演唱會提醒</li></ul> |

### Notifications disallowed by service messages 

服務訊息不允許以下通知：

- 並非對 LINE MINI App 上使用者動作的確認或回應的通知，例如從售票機購買票券時的購買完成通知與提醒通知。
- 廣告與活動通知，包括折扣、購物回饋、新產品、折扣券或促銷活動的資訊。

若服務訊息發送了不被允許的內容，service message API 的使用權將被禁止一段時間。重複違反條款與條件可能導致你的 LINE MINI App 被從 LINE 上移除。

### Message Count Limit 

- 每個使用者動作最多可發送 5 則訊息。此限制分別適用於動作確認、動作結果與提醒通知的各個使用情境。
- 訊息數量限制可能會依使用情境而變更。若限制變更，LY Corporation 會在[審查（review）](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)時通知你。

### Service Message Templates 

- [新增服務訊息範本（service message template）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#service-message-templates)至你的 LINE MINI App 頻道（channel）。
- 每個 LINE MINI App 頻道最多可設定 20 組範本。

## Channel consent simplification 

LIFF app 若要取得使用者資訊或向使用者發送訊息，使用者必須在首次存取該 LIFF app 時，於頻道同意畫面（channel consent screen）上同意對應的權限。

在 LINE MINI App 中，透過「Channel consent simplification」功能，使用者只需同意簡化授權一次。之後當使用者首次存取另一個 LINE MINI App 時，頻道同意畫面會被略過，讓使用者能立即開始使用該 LINE MINI App。

不過，根據 LY Corporation 的隱私權政策，「Channel consent simplification」功能唯一會略過同意的權限是取得[使用者 ID（user ID）](https://developers.line.biz/en/glossary/#user-id)。對於取得使用者個人檔案資訊或發送訊息所需的權限，驗證畫面會在需要這些權限時於各個 LINE MINI App 內顯示。

啟用「Channel consent simplification」功能可讓使用者更容易存取 LINE MINI App。為了改善使用者體驗，我們建議啟用「Channel consent simplification」功能。

對於日本的新 LINE MINI App 頻道，「Channel consent simplification」功能一律為啟用狀態。

如需更多資訊，請參閱 [LINE MINI App authorization flow](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/)。
