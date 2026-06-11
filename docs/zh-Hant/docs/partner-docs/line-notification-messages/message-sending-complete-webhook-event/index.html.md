# Webhook 投遞完成事件

<!-- note start -->

**使用選用功能須提出申請**

只有已提交必要申請的企業用戶才能使用本文件所述的功能。若要在您的 LINE 官方帳號上使用這些功能，請聯絡您的業務負責人，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## Overview of webhook delivery completion events 

當對 LINE notification messages API 發出請求，並且 LINE notification message 已完成投遞給用戶時，LINE Platform 會將一個專用的 Webhook 事件（投遞完成事件）傳送至 bot 伺服器的 Webhook URL。

- [Webhook 投遞完成事件規格](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event)
- [關於 Webhook 投遞完成事件的補充資訊](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#we-cant-receive-a-delivery-webhook-event)

### Webhook delivery completion event specifications 

| 屬性名稱 | 類型 | 說明 |
| --- | --- | --- |
| type | String | `delivery` |
| mode | Object | 請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。 |
| timestamp | Number | 請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。 |
| webhookEventId | String | 請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。 |
| deliveryContext | Object | 請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。 |
| delivery | Object | 包含經雜湊處理的電話號碼字串，或由 [`X-Line-Delivery-Tag`](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-request-headers) 指定的字串的 delivery 物件。 |
| delivery.data | String | 經雜湊處理的電話號碼字串，或由 [`X-Line-Delivery-Tag`](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-request-headers) 指定的字串。 |

_Webhook 事件範例_

<!-- tab start `json` -->

```json
// Example webhook delivery completion event (without X-Line-Delivery-Tag header specified)
{
  "destination": "Uc7472b39e21dab71c2347e02714630d6",
  "events": [
    {
      "type": "delivery",
      "delivery": {
        "data": "68df277462529930889fab80ecffdc0883906320591df93c25efc08300410fc2"
      },
      "webhookEventId": "01G17DAF0QJ7A3ERC5EJ9MAMH8",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1650590038721,
      "mode": "active"
    }
  ]
}

// Example webhook delivery completion event (with X-Line-Delivery-Tag header specified)
{
  "destination": "Uc7472b39e21dab71c2347e02714630d6",
  "events": [
    {
      "type": "delivery",
      "delivery": {
        "data": "15034552939884E28681A7D668CEA94C147C716C0EC9DFE8B80B44EF3B57F6BD0602366BC3menu01"
      },
      "webhookEventId": "01G17EJCGAVV66J5WNA7ZCTF6H",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1650591346705,
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

<!-- note start -->

**關於 Webhook 投遞完成事件的狀態**

Webhook 投遞完成事件**表示 LINE notification message 已投遞給用戶，且該訊息現在可供檢視**。它並不表示下列情況：

- LINE notification messages API 請求成功
- [用戶收到「設定以接收 LINE notification messages」的訊息](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-1)
- 已同意接收 LINE notification messages
- [用戶收到要求進行 SMS 認證的訊息](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-3)
- 用戶執行 SMS 認證
- 用戶開啟 LINE notification message（已讀）

<!-- note end -->

<!-- note start -->

**Webhook 事件的簽章驗證**

在收到投遞完成事件時，請使用 channel secret 進行[簽章驗證](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#verify-signature)。對於使用 LINE Chat Plus 的頻道，請使用 Switcher Secret 來驗證簽章。

<!-- note end -->

## Additional information on Webhook delivery completion events 

即使已傳送 LINE notification messages API 請求並以 HTTP 狀態碼 `200` 或 `202` 回應，視用戶的 [LINE notification message 接收設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#how-to-consent-for-line-notification-messages)與 SMS 認證狀態而定，LINE notification messages 仍可能未投遞給用戶，或 LINE notification messages 的傳送可能被暫停。

如果已傳送 LINE notification messages API 請求，並且在以 HTTP 狀態碼 `200` 或 `202` 回應後的 24 小時內未收到 [Webhook 投遞完成事件](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/)，即表示 LINE notification message 因下列其中一個原因而未投遞給用戶。

- [用戶已封鎖該 LINE 官方帳號](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#user-blocked-your-account)
- [用戶未提供必要的同意或認證](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#user-didnt-action-taken)

### The user has blocked the LINE Official Account 

即使用戶已封鎖傳送 LINE notification message 的 LINE 官方帳號，[LINE notification messages API 的請求](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#about-pnp-api-block-response)仍會以 HTTP 狀態碼 `200` 或 `202` 回應。

### The user didn't give required consent or authentication 

有可能尚未設定接收 LINE notification messages 的相關設定，或需要進行 SMS 認證，但這些設定或操作尚未執行。如需更多資訊，請參閱 [LINE notification messages API 請求成功但訊息未傳送時](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#why-i-cant-receive-line-notification-messages)。
