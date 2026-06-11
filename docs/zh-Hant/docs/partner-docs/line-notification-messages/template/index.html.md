# LINE 通知訊息（template）

<!-- note start -->

**使用選用功能須提出申請**

只有已提交必要申請的企業用戶才能使用本文件所述的功能。若要在您的 LINE 官方帳號上使用這些功能，請聯絡您的業務負責人，或聯絡[我們的銷售合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

<!-- table of contents -->

## What are LINE notification messages (template) 

LINE 通知訊息（template）是一項功能，可讓您將事先準備好的範本（template）與項目（item）組合來建立訊息，並透過指定用戶的電話號碼來傳送訊息給他們。即使用戶尚未將您的 LINE 官方帳號加為好友，您也可以從您的 LINE 官方帳號傳送訊息給他們。

LINE 通知訊息（template）僅能用於在日本、泰國與台灣建立的 LINE 官方帳號。

選擇[範本（template）](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/#templates)後，您可以組合[項目（item）](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/#items)與[按鈕（button）](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/#buttons)，並為各項目指定任意文字或 URL 來建立 JSON，接著使用 [Send LINE notification message (template)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template) 端點來傳送 LINE 通知訊息（template）。

可用的範本、項目與按鈕類型在日本、泰國與台灣各不相同，並會由傳送訊息的 LINE 官方帳號自動決定。您無法變更訊息的頁首（header）與頁尾（footer）。

![Sample of a LINE notification message (template)](https://developers.line.biz/media/line-notification-message/notification-messages-template.png)

例如，上述訊息可透過建立以下 JSON 來傳送：

```json
{
  "to": "{hashed_phone_number}",
  "templateKey": "shipment_completed_ja",
  "body": {
    "emphasizedItem": {
      "itemKey": "date_002_ja",
      "content": "Saturday, August 10, 2024"
    },
    "items": [
      {
        "itemKey": "time_range_001_ja",
        "content": "A.M."
      },
      {
        "itemKey": "number_001_ja",
        "content": "1234567"
      },
      {
        "itemKey": "price_001_ja",
        "content": "120 USD"
      },
      {
        "itemKey": "name_010_ja",
        "content": "Frozen Soup Set"
      }
    ],
    "buttons": [
      {
        "buttonKey": "check_delivery_status_ja",
        "url": "https://example.com/CheckDeliveryStatus/"
      },
      {
        "buttonKey": "contact_ja",
        "url": "https://example.com/ContactUs/"
      }
    ]
  }
}
```

您可以使用 API 查詢 LINE 通知訊息（template）的數量。如需詳細資訊，請參閱 [Get the number of sent LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#get-number-of-sent-line-notification-messages)。

## Templates 

透過傳送指定範本鍵（`Key`）的 LINE 通知訊息（template），目標範本的標題（`Title`）與說明（`Description`）會顯示在訊息的最上方。

![](https://developers.line.biz/media/line-notification-message/notification-messages-template-templates.png)

<!-- templates -->

## Items 

您可以透過指定項目的鍵（`Key`），在範本中包含多個項目。您可以將任意字串設定為指定項目的值。

![](https://developers.line.biz/media/line-notification-message/notification-messages-template-items.png)

<!-- templates -->

## Buttons 

您可以透過指定按鈕的鍵（`Key`），在範本中包含多個按鈕。您可以將任意 URL 設定為按鈕的跳轉目的地。

![](https://developers.line.biz/media/line-notification-message/notification-messages-template-buttons.png)

<!-- templates -->
