# 顯示載入動畫（Display a loading animation）

當你的 LINE 官方帳號收到使用者傳來的訊息後，由於需要準備訊息或進行預約處理，回覆可能會花上一些時間。在這種情況下，你可以透過顯示載入動畫，以視覺方式告知使用者請稍候。

![](https://developers.line.biz/media/messaging-api/loading-indicator/loading-indicator.png)

## Display a loading animation 

透過使用 [Display a loading animation](https://developers.line.biz/en/reference/messaging-api/#display-a-loading-indicator) 端點（endpoint），你可以在使用者與 LINE 官方帳號之間的一對一聊天中顯示載入動畫。載入動畫會在經過指定的秒數（5 到 60 秒）後，或當你的 LINE 官方帳號傳來新訊息時自動消失。

![](https://developers.line.biz/media/messaging-api/loading-indicator/loading-animation.gif)

你可以指定使用者 ID 作為顯示對象，在使用者與你的 LINE 官方帳號之間的一對一聊天中顯示載入動畫。你無法指定群組聊天或多人聊天。

載入動畫只會在使用者正在檢視與你 LINE 官方帳號的聊天畫面時顯示。如果你在使用者並未檢視聊天畫面時請求顯示載入動畫，將不會顯示任何通知。即使使用者稍後開啟聊天畫面，動畫也不會顯示。

如果你在載入動畫仍在顯示時再次請求顯示載入動畫，動畫會持續顯示，且直到消失為止的時間將被第二次請求所指定的秒數覆寫。

### Example request 

以下是顯示載入動畫 5 秒的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/chat/loading/start \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "chatId": "U4af4980629...",
    "loadingSeconds": 5
}'
```

如需更多資訊，請參閱 Messaging API 參考文件中的 [Display a loading animation](https://developers.line.biz/en/reference/messaging-api/#display-a-loading-indicator)。
