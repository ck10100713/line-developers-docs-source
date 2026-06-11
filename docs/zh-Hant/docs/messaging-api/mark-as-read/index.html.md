# 將訊息標示為已讀（Mark messages as read）

在 LINE 聊天中，當收訊者查看了使用者所傳送的訊息時，該訊息會被加上已讀標示。在 LINE 官方帳號中使用聊天功能時，來自使用者的訊息不會自動被標示為已讀。不過，藉由使用 Messaging API，你可以在啟用聊天功能的同時，手動將特定訊息標示為已讀。

本頁說明如何透過 Messaging API，將使用者傳送的訊息加上已讀標示。

<!-- table of contents -->

## Conditions for marking messages as read in the Messaging API 

如果在 [LINE Official Account Manager](https://manager.line.biz/) 的 **Response settings**（回應設定）中關閉了 **Chat**（聊天），則使用者傳送的訊息將會自動被標示為已讀。若要透過 Messaging API 將訊息標示為已讀，**Chat** 必須處於開啟狀態。

## How to mark messages as read using the Messaging API 

若要將使用者傳送的訊息標示為已讀，請依照下列步驟操作：

1. [取得訊息的已讀權杖（read token）](https://developers.line.biz/en/docs/messaging-api/mark-as-read/#get-token)
2. [使用「Mark messages as read」端點（endpoint）](https://developers.line.biz/en/docs/messaging-api/mark-as-read/#use-endpoint)

以下逐一說明各個步驟。

### 1. Get the read token of the message 

當使用者傳送訊息給 LINE 官方帳號時，LINE Platform 會將 Webhook 的[訊息事件（message event）](https://developers.line.biz/en/reference/messaging-api/#message-event)傳送至 bot 伺服器。這個事件物件包含了用來將訊息標示為已讀的 `markAsReadToken` 屬性（已讀權杖）。

以下是 Webhook 訊息事件物件的範例。已讀權杖沒有到期日。

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "message",
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "message": {
        "id": "444573844083572737",
        "type": "text",
        "quoteToken": "q3Plxr4AgKd...",
        "markAsReadToken": "30yhdy232...", // Read token
        "text": "Hello, world!"
      },
      // omitted
    }
  ]
}
```

### 2. Use the "Mark messages as read" endpoint 

若要將訊息標示為已讀，請使用步驟 1 取得的已讀權杖，搭配 [Mark messages as read](https://developers.line.biz/en/reference/messaging-api/#mark-as-read) 端點。你可以執行如下的請求，將指定訊息之前的所有訊息標示為已讀：

```sh
curl -v -X POST https://api.line.me/v2/bot/chat/markAsRead \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
  "markAsReadToken": "{mark as read token}"
}'
```
