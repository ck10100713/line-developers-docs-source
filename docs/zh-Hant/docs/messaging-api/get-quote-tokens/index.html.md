# 取得引用權杖（quote token）

當你想用 Messaging API 傳送引用過往訊息的訊息時，會使用引用權杖（quote token）。本頁說明如何取得引用權杖。

<!-- table of contents -->

## What is a quote token 

引用權杖（quote token）是一個類似 `IStG5h1Tz7bsH6xinEQtKQ9IdtcN5wLE15-LwtIDCEYAqDkV741O-XkOhZo1GYxw2UCURKnpHujpZuZaBaeQZVOVpKiaEeAz1Ye3-3ZYbPQVjuXZ4x8ZpISG7WhJDCE8o-hhHh8uMBRyp3b0L_Cxlg` 的字串。要[傳送引用訊息](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-quote-messages)時，必須提供引用權杖。

引用權杖只能在發送了欲引用訊息的一對一聊天、群組聊天，以及多人聊天中使用。引用權杖沒有到期日，同一個引用權杖可以重複使用多次。

## Get quote tokens 

取得引用權杖有兩種方式：

1. [透過 Webhook 取得引用權杖](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/#get-quote-tokens-via-webhook)
1. [傳送訊息時於回應中取得引用權杖](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/#get-quote-tokens-in-the-response)

### Get quote tokens via webhook 

當使用者在已加入你的 LINE 官方帳號的一對一聊天、群組聊天或多人聊天中傳送訊息時，Webhook 的[訊息事件（message event）](https://developers.line.biz/en/reference/messaging-api/#message-event)會被傳送到你的 bot 伺服器。在此訊息事件中，以下訊息物件會包含引用權杖（`quoteToken`）：

- [Text](https://developers.line.biz/en/reference/messaging-api/#wh-text)
- [Sticker](https://developers.line.biz/en/reference/messaging-api/#wh-sticker)
- [Image](https://developers.line.biz/en/reference/messaging-api/#wh-image)
- [Video](https://developers.line.biz/en/reference/messaging-api/#wh-video)

```json
"message": {
  "type": "text",
  "id": "468789577898262530",
  "quoteToken": "q3Plxr4AgKd...", // Quote token
  "text": "Can I reserve a table for dinner tonight?"
}
```

如需更多關於 Webhook 的資訊，請參閱[接收訊息（webhook）](https://developers.line.biz/en/docs/messaging-api/receiving-messages/)。

### Get quote tokens in the response when sending a message 

當你使用 Messaging API 傳送[回覆訊息（reply message）](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)或[推播訊息（push message）](https://developers.line.biz/en/reference/messaging-api/#send-push-message)時，會回傳一個包含 `sentMessages` 屬性的 JSON 物件作為回應。

```json
{
  "sentMessages": [
    {
      "id": "461230966842064897",
      "quoteToken": "IStG5h1Tz7b..."
    }
  ]
}
```

不過，只有在傳送以下這些可被指定為引用對象的訊息物件時，回應中才會包含引用權杖（`sentMessages[].quoteToken`）：

- [文字訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)
- [文字訊息（v2）](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages-v2)
- [貼圖訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)
- [圖片訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)
- [影片訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#video-messages)
- [範本訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)（被引用時只會顯示 `altText`）
- [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages)（被引用時只會顯示 `altText`）

如果你在一則訊息中指定了多個上述訊息物件，你會收到相同數量的引用權杖。在此情況下，`sentMessages` 陣列中元素的順序保證會與傳送時訊息物件的順序相同。

```json
{
  "sentMessages": [
    {
      "id": "471875397094211585",
      "quoteToken": "YKPDqjc2jmW..."
    },
    {
      "id": "471875397127766017",
      "quoteToken": "eG5SfLhgiFX..."
    }
  ]
}
```
