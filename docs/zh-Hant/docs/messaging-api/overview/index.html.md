# Messaging API 總覽（Messaging API overview）

使用 Messaging API 來建立機器人，為您的使用者在 LINE 上提供個人化的體驗。

<!-- tip start -->

**什麼是 LINE 官方帳號（LINE Official Account）**

如果您對 LINE 官方帳號還不熟悉，請造訪完整的學習平台 [LY Marketing Campus](https://lymcampus.jp/)（僅提供日文版）。

<!-- tip end -->

## How the Messaging API works 

透過 Messaging API，機器人伺服器可以與 LINE Platform 互相傳送與接收資料。請求以 JSON 格式透過 HTTPS 傳送。機器人伺服器與 LINE Platform 之間的通訊流程如下：

1. 使用者傳送訊息給 LINE 官方帳號。
1. LINE Platform 將 Webhook 事件傳送至機器人伺服器的 Webhook URL。
1. 機器人伺服器檢查 Webhook 事件，並透過 LINE Platform 回應使用者。

![](https://developers.line.biz/media/messaging-api/overview/messaging-api-architecture.png)

## Try the demo 

試用範例，親自體驗 Messaging API。您可以在智慧型手機上檢視範例。掃描 QR code，將範例用的 LINE 官方帳號加為好友。

![](https://developers.line.biz/media/messaging-api/demo/messaging-api-demo-qr-code-en.png)

<!-- note start -->

**範例 App 取得的資料**

範例用的 LINE 官方帳號具備傳送您裝置位置資訊的功能。如果您不希望傳送此資訊，請在使用此服務前關閉裝置上的位置分享功能。我們也會從您的 LINE 帳號收集部分個人檔案資訊（user ID）。不過，這些資訊不會儲存在伺服器上。請在使用此服務前理解上述內容。

<!-- note end -->

## What you can do with the Messaging API 

以下是您可以透過 Messaging API 做到的事情。

### Send reply messages 

透過 Messaging API，您可以向已將您的 LINE 官方帳號加為好友的使用者傳送回覆訊息（reply message）。詳情請參閱 [Sending messages](https://developers.line.biz/en/docs/messaging-api/sending-messages/)。

### Send messages at any time 

透過 Messaging API，您可以隨時直接向使用者傳送訊息。詳情請參閱 [Sending messages](https://developers.line.biz/en/docs/messaging-api/sending-messages/)。

### Send different message types 

透過 Messaging API，您可以向使用者傳送以下列出的各種類型訊息。有關這些訊息的規格詳情，請參閱 [Message types](https://developers.line.biz/en/docs/messaging-api/message-types/)。

- [Text message](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)
- [Text message (v2)](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages-v2)
- [Sticker message](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)
- [Image message](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)
- [Video message](https://developers.line.biz/en/docs/messaging-api/message-types/#video-messages)
- [Audio message](https://developers.line.biz/en/docs/messaging-api/message-types/#audio-messages)
- [Location message](https://developers.line.biz/en/docs/messaging-api/message-types/#location-messages)
- [Coupon message](https://developers.line.biz/en/docs/messaging-api/message-types/#coupon-messages)
- [Imagemap message](https://developers.line.biz/en/docs/messaging-api/message-types/#imagemap-messages)
- [Template message](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)
- [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages)

### Get content sent by users 

透過 Messaging API，您可以取得使用者傳送的圖片、影片、音訊與檔案。使用者傳送的內容會在一段時間後自動刪除。詳情請參閱 Messaging API 參考文件中的 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content)。

### Get user profiles 

透過 Messaging API，您可以在一對一聊天與群組聊天中，取得與您的 LINE 官方帳號互動之使用者的個人檔案資訊。您可以取得的個人檔案資訊類型包括使用者的顯示名稱、語言、個人檔案圖片與狀態訊息。詳情請參閱 Messaging API 參考文件中的 [Get profile](https://developers.line.biz/en/reference/messaging-api/#get-profile)。

### Join group chats 

透過 Messaging API，您可以在群組聊天中傳送訊息，並取得群組聊天成員的資訊。詳情請參閱 [Group chats and multi-person chats](https://developers.line.biz/en/docs/messaging-api/group-chats/)。

### Use rich menus 

透過 Messaging API，您可以在聊天中設定並自訂圖文選單（rich menu）。圖文選單可協助使用者了解如何與您的 LINE 官方帳號互動。使用者可隨時在聊天中使用此選單。詳情請參閱 [Use rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)。

### Use beacons 

透過 LINE Beacon，您可以設定您的 LINE 官方帳號，使其與進入 Beacon 範圍的使用者互動。詳情請參閱 [Use beacons with LINE](https://developers.line.biz/en/docs/messaging-api/using-beacons/)。

### Use account link 

透過 Messaging API，您可以在使用者已將您的 LINE 官方帳號加為好友的情況下，安全地將您服務中的使用者帳號與其 LINE 帳號連結。詳情請參閱 [User account linking](https://developers.line.biz/en/docs/messaging-api/linking-accounts/)。

### Get the number of sent messages 

透過 Messaging API，您可以取得從您的 LINE 官方帳號傳送的訊息數量。此 API 僅回傳透過 Messaging API 傳送的訊息數量，不包含透過 LINE Official Account Manager 傳送的訊息。詳情請參閱以下參考文件：

- [Get the target limit for sending messages this month](https://developers.line.biz/en/reference/messaging-api/#get-quota)
- [Get number of messages sent this month](https://developers.line.biz/en/reference/messaging-api/#get-consumption)
- [Get number of sent reply messages](https://developers.line.biz/en/reference/messaging-api/#get-number-of-reply-messages)
- [Get number of sent push messages](https://developers.line.biz/en/reference/messaging-api/#get-number-of-push-messages)
- [Get number of sent multicast messages](https://developers.line.biz/en/reference/messaging-api/#get-number-of-multicast-messages)
- [Get number of sent broadcast messages](https://developers.line.biz/en/reference/messaging-api/#get-number-of-broadcast-messages)

## Messaging API pricing 

您可以免費開始使用 Messaging API。任何人都可以使用 Messaging API 從 LINE 官方帳號傳送訊息。

您每個月可以免費傳送一定數量的訊息。免費訊息的數量取決於您 LINE 官方帳號的[訂閱方案](https://www.lycbiz.com/jp/service/line-official-account/plan/)（僅提供日文版）。訂閱方案可能因國家或地區而異。詳情請參閱您所在地區的訂閱方案。

有關 Messaging API 收費的更多資訊，請參閱 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。

## Next steps 

接下來，請[開始使用 Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/) 來建立機器人。首先，建立一個 LINE 官方帳號。建立 LINE 官方帳號後，您就可以為該 LINE 官方帳號建立 Messaging API 頻道（channel）。

## Learn more 

- [Messaging API development guidelines](https://developers.line.biz/en/docs/messaging-api/development-guidelines/)
- [LINE Messaging API SDKs](https://developers.line.biz/en/docs/messaging-api/line-bot-sdk/)
- [Messaging API reference](https://developers.line.biz/en/reference/messaging-api/)
