# Messaging API 收費方式

本頁說明使用 Messaging API 發送訊息的費用。

<!-- table of contents -->

## Pricing system 

LINE 官方帳號（LINE Official Account）同時提供免費方案，以及採固定月費的方案。

所有方案每月都允許您免費發送一定數量的訊息。可免費發送的訊息數量會依訂閱方案而有所不同。如果您在月中升級至較高方案，即可增加當月可免費發送的訊息數量。

部分方案允許您在免費訊息上限之外發送額外的訊息。系統會依您發送的額外訊息數量收費。若要發送額外訊息，請開啟 [LINE Official Account Manager](https://manager.line.biz/)，選擇您的 LINE 官方帳號，然後選擇允許發送額外訊息的訂閱方案。在此設定額外訊息的數量上限。

### Pricing plans by country or region 

各國家或地區的收費方案請參閱下表：

| Country or Region | Price information |
| --- | --- |
| Japan | [LINE Official Account pricing plan](https://www.lycbiz.com/jp/service/line-official-account/plan/) <br> [Activity and billing (subscription plan changes and payment related management)](https://www.lycbiz.com/jp/manual/OfficialAccountManager/account-settings_plan/) |
| Taiwan | [LINE Official Account](https://tw.linebiz.com/service/account-solutions/line-official-account/) <br> [LINE Official Account - FAQ](https://tw.linebiz.com/faq/oa-price/) |
| Thailand | [LINE Official Account](https://lineforbusiness.com/th/service/line-oa-features/broadcast-message) |
| Other regions | [LINE Official Account](https://www.lycbiz.jp/en/other/) |

### Example of subscription plans 

下表為日本訂閱方案的範例：

|  | Communication Plan | Light Plan | Standard Plan |
| :-- | :-: | :-: | :-: |
| 固定月費 [^1] | 免費 | JPY 5,000 | JPY 15,000 |
| 每月免費訊息數量 | 最多 200 則 | 最多 5,000 則 | 最多 30,000 則 |
| 額外訊息費用 [^1] | 不適用 | 不適用 | 每則最多 JPY 3 [^2] |

[^1]: 未含稅。

[^2]: 額外訊息的單價會依發送的訊息數量而有所不同。

舉例來說，如果您每月想發送 1,000 則訊息，請選擇含 5,000 則免費訊息的 Light Plan。

若每月要發送 40,000 則訊息，您必須選擇含 30,000 則免費訊息的 Standard Plan，並針對超出免費訊息上限的 10,000 則訊息支付額外費用。

收費方案會因國家或地區而異，因此請查看[您所在地區的方案](https://developers.line.biz/en/docs/messaging-api/pricing/#global-pricing)。

## When you exceed the limit of free messages 

當您超過單月可發送的訊息上限時，系統會回傳錯誤回應，且訊息不會被發送。詳情請參閱 Messaging API 參考資料中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

您可以透過下列端點（endpoint）查看當月的使用量：

- [Get the target limit for sending messages this month](https://developers.line.biz/en/reference/messaging-api/#get-quota)
- [Get number of messages sent this month](https://developers.line.biz/en/reference/messaging-api/#get-consumption)

關於如何變更方案以增加免費訊息數量或發送額外訊息的資訊，請參閱 [Pricing system](https://developers.line.biz/en/docs/messaging-api/pricing/#pricing-system)。

## How to count the number of messages sent 

訊息數量是依您發送對象的人數計算。假設您在單一請求中以四個[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)向一個有五個人的聊天室發送 push 訊息，此時發送的訊息數量為五則。請求中的訊息物件數量並不會影響發送的訊息數量。

如果您向已封鎖您 LINE 官方帳號的使用者，或向不存在的使用者 ID 發送訊息，該訊息不會被計算。若使用者無法收到您的訊息，該訊息便不計為已發送。

## Sending methods that are counted towards the number of messages for the subscription plan 

關於 Messaging API，並非所有發送的訊息都會計入訂閱方案的訊息數量。以下為計入與不計入訊息數量的發送方式：

- 會計入訊息數量的發送方式
  - [Push messages](https://developers.line.biz/en/reference/messaging-api/#send-push-message)
  - [Multicast messages](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)
  - [Broadcast messages](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)
  - [Narrowcast messages](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)
- 不會計入訊息數量的發送方式
  - [Reply messages](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)

關於 Messaging API 以外的訊息功能收費資訊，請參閱 LINE for Business 中的 [Chargeable Messages](https://www.lycbiz.com/jp/service/line-official-account/plan/)（僅提供日文版）。
