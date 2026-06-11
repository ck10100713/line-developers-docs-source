# 自訂圖示與顯示名稱（Customize icon and display name）

您可以在使用這些 API 傳送訊息時，自訂 LINE 官方帳號的圖示與顯示名稱。可使用的 [Message 物件](https://developers.line.biz/en/reference/messaging-api/#message-objects)類型沒有任何限制。

- [傳送推播訊息（Send push messages）](https://developers.line.biz/en/reference/messaging-api/#send-push-message)
- [傳送群發訊息（Send multicast messages）](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)
- [傳送窄播訊息（Send narrowcast messages）](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)
- [傳送廣播訊息（Send broadcast messages）](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)
- [傳送回覆訊息（Send reply messages）](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)

若您未替訊息指定圖示或顯示名稱，則會顯示預設圖示與您的 LINE 官方帳號名稱。

自訂圖示與顯示名稱時，我們建議您先以自訂的圖示與顯示名稱傳送推播訊息給您自己的 LINE 帳號，以確認訊息的呈現外觀。

## Customize the icon and display name 

請比較預設訊息與指定了圖示及顯示名稱的訊息之間的差異。如下所示，顯示名稱後方會附加 `from 'account name'`。此附加文字的目的是協助使用者輕鬆辨識您的 LINE 官方帳號，避免將您與他人混淆。聊天畫面頂端所顯示的帳號名稱在所有情況下皆維持不變。

![](https://developers.line.biz/media/messaging-api/icon-nickname-switch/icon-nickname-switch.jpg)

### Example request 

以下是傳送帶有自訂圖示與顯示名稱訊息的範例請求。

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-d '{
    "to": "U1234....",
    "messages": [
        {
            "type": "text",
            "text": "Hello, I am Cony!!",
            "sender": {
                "name": "Cony",
                "iconUrl": "https://line.me/conyprof"
            }
        }
    ]
}'
```

## Icon and display name customization scope 

本節將說明圖示與顯示名稱的自訂功能適用於哪些範圍。

### Chat rooms 

您為訊息指定的圖示與顯示名稱，僅會影響該則訊息本身的圖示與顯示名稱。

- 訊息泡泡：會顯示自訂的圖示與顯示名稱（`display name from 'account name'`）。
- 聊天室名稱：頂端顯示的聊天室名稱仍維持為您的 LINE 官方帳號名稱。
- 商家檔案頁面：您 LINE 官方帳號商家檔案頁面上的檔案圖片與顯示名稱無法自訂。

### Message search result 

在搜尋結果中，帶有自訂圖示與顯示名稱的訊息會顯示自訂的圖示與顯示名稱，並附加 `from 'account name'`。

### Chat list and preview 

聊天列表中您 LINE 官方帳號的圖示與顯示名稱無法自訂。但非文字訊息的預覽會顯示自訂的圖示與顯示名稱。例如，若您以自訂的顯示名稱傳送一張相片，預覽訊息會顯示「(顯示名稱) 傳送了一張相片」。

### Chat list search result 

在聊天搜尋結果中，您的 LINE 官方帳號會顯示其預設圖示與顯示名稱。

### Friends list 

在好友列表中，您的 LINE 官方帳號會顯示其預設圖示與顯示名稱。

## Learn more 

如需更多有關自訂圖示與顯示名稱規格的資訊，請參閱 Messaging API 參考文件中的 [Change icon and display name](https://developers.line.biz/en/reference/messaging-api/#icon-nickname-switch)。
