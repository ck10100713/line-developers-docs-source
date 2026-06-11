# 群組聊天與多人聊天（Group chats and multi-person chats）

LINE 官方帳號可以透過 Messaging API 在群組聊天或多人聊天中與使用者互動。了解你可以如何在群組聊天與多人聊天中運用你的 LINE 官方帳號。

## Types of chats with multiple users 

LINE 有兩種多位使用者參與的聊天類型：**群組聊天（group chats）** 與 **多人聊天（multi-person chats）**。群組聊天或多人聊天中的使用者稱為 **成員（members）**。

<!-- tip start -->

**多人聊天已併入群組聊天**

從 LINE 10.17.0 版開始，多人聊天已併入群組聊天。你可以繼續使用在此之前已建立的多人聊天。但若你在 LINE 10.17.0 版（含）以後與多位好友建立新的聊天，該聊天將會成為群組聊天。請參閱 LINE 使用者指南中的 [Create and manage groups](https://guide.line.me/ja/friends-and-groups/create-groups.html)（僅提供日文版）。

<!-- tip end -->

### Group chats 

群組聊天是設計給多位參與者持續使用的聊天。系統會產生一組 [group ID](https://developers.line.biz/en/glossary/#group-id) 來識別群組聊天。LINE 使用者可以建立群組聊天並自行命名。群組聊天支援相簿、記事本等功能。

<!-- tip start -->

**Tip**

當使用者邀請第三位使用者加入一對一聊天時，便會建立群組聊天。使用者可以設定是否要對受邀加入群組聊天的使用者啟用核准流程。關於如何設定核准流程的詳細資訊，請參閱 LINE 使用者指南中的 [Create and manage groups](https://guide.line.me/ja/friends-and-groups/create-groups.html)（僅提供日文版）。

<!-- tip end -->

### Multi-person chats 

多人聊天是設計給多人臨時使用的聊天。系統會產生一組 [room ID](https://developers.line.biz/en/glossary/#room-id) 來識別多人聊天。多人聊天的名稱會自動設定為聊天成員的名稱。多人聊天不支援相簿、記事本等功能。

從 LINE 10.17.0 版開始，多人聊天已併入群組聊天。你可以繼續使用在此之前已建立的多人聊天。但若你在 LINE 10.17.0 版（含）以後與多位好友建立新的聊天，該聊天將會成為群組聊天。

## Add LINE Official Account in group & multi-person chats 

你可以邀請 LINE 官方帳號加入群組聊天或多人聊天。為了能被邀請，請前往 [LINE Developers Console](https://developers.line.biz/console/) > 你的頻道（channel）的 **Messaging API** 分頁，並啟用 **Allow bot to join group chats**。此設定預設為停用。在任何時候，一個群組聊天或多人聊天中只能有一個 LINE 官方帳號。

## Receive webhook events 

你會收到群組聊天與多人聊天的 Webhook 事件，就像收到一對一聊天的事件一樣。詳細資訊請參閱 Messaging API 參考文件中的 [Webhook events for chats](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-event-in-one-on-one-talk-or-group-chat) 與 [Webhook Event Objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)。

### Tip for using message events 

當使用者在你已加入的群組聊天或多人聊天中傳送訊息時，LINE Platform 會向 bot 伺服器傳送訊息事件，就像在一對一聊天中一樣。

[message event](https://developers.line.biz/en/reference/messaging-api/#message-event) 具有一個 `source` 屬性，用來指定群組聊天的 ID（`groupId`）或多人聊天的 ID（`roomId`）。

```json
"source": {
    "type": "group",
    "groupId": "Ca56f94637c...",
    "userId": "U4af4980629..."
}
```

關於 group ID 與 room ID 的詳細資訊，請參閱 [What are the user ID, group ID, and room ID values?](https://developers.line.biz/en/faq/#what-are-userid-groupid-and-roomid)。

## Send a request to an endpoint 

以下操作為群組聊天與多人聊天專屬。詳細資訊請參閱 [Messaging API reference](https://developers.line.biz/en/reference/messaging-api/)。

- **群組聊天**
  - [Get group chat summary](https://developers.line.biz/en/reference/messaging-api/#get-group-summary)
  - [Get number of users in a group chat](https://developers.line.biz/en/reference/messaging-api/#get-members-group-count)
  - [Get group chat member user IDs](https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids)
  - [Get group chat member profile](https://developers.line.biz/en/reference/messaging-api/#get-group-member-profile)
  - [Leave group chat](https://developers.line.biz/en/reference/messaging-api/#leave-group)
- **多人聊天**
  - [Get number of users in a multi-person chat](https://developers.line.biz/en/reference/messaging-api/#get-members-room-count)
  - [Get multi-person chat member user IDs](https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids)
  - [Get multi-person chat member profile](https://developers.line.biz/en/reference/messaging-api/#get-room-member-profile)
  - [Leave multi-person chat](https://developers.line.biz/en/reference/messaging-api/#leave-room)

### Tip for sending messages 

你可以在群組聊天與多人聊天中傳送 [reply messages](https://developers.line.biz/en/reference/messaging-api/#send-reply-message) 與 [push messages](https://developers.line.biz/en/reference/messaging-api/#send-push-message)，就像在一對一聊天中一樣。

當你傳送推播訊息（push message）時，請在請求主體（request body）的 `to` 屬性中以 group ID 或 room ID 指定接收者。你可以在 [webhook event objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects) 中取得接收者 ID。你在群組聊天與多人聊天中傳送的訊息會顯示給該聊天的所有成員。

<!-- tip start -->

**Tip**

你無法在群組聊天與多人聊天中向多位使用者 [send multicast messages](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)。

<!-- tip end -->
