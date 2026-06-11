# 接收訊息（webhook）（Receive messages (webhook)）

每當使用者將你的 LINE 官方帳號加為好友或傳送訊息給它時，LINE Platform 就會將帶有 webhook 事件物件的 HTTP POST 請求傳送到你在 [LINE Developers Console](https://developers.line.biz/console/) 註冊的 webhook URL（bot 伺服器）。

請確保你的 bot 伺服器有正確處理 webhook 事件物件。如果你的 bot 伺服器長時間無法接收 webhook，LINE Platform 可能會暫停向你的 bot 伺服器傳送 webhook。

<!-- warning start -->

**安全警告**

你的 bot 伺服器可能會收到來自 LINE Platform 以外來源的 HTTP POST 請求，而這類請求可能帶有惡意。在處理 webhook 事件物件之前，請務必先[驗證簽章](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#verify-signature)。

<!-- warning end -->

<!-- tip start -->

**我們建議以非同步方式處理事件**

我們建議你以非同步方式處理 webhook 事件，以避免後續請求必須等待目前的請求處理完畢。

<!-- tip end -->

## Verify signature 

當 bot 伺服器收到 webhook 事件時，請在處理 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)之前，先驗證請求標頭中所含的簽章。這個驗證步驟很重要，可以確認 webhook 確實來自 LINE Platform，且在傳輸過程中未遭竄改。

如需更多資訊，請參閱[驗證 webhook 簽章](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/)。

## Webhook event types 

你可以根據 webhook 事件物件中的資料來控制 bot 的反應方式，也可以讓 bot 執行某些動作或回應使用者。你可以取得[聊天](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-event-in-one-on-one-talk-or-group-chat)以及 [beacon 與帳號連動](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#other-webhook-events)的 webhook 事件。如需更多資訊，請參閱 Messaging API 參考文件中的 [Webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)。

### Webhook events for chats 

你的 bot 伺服器在一對一聊天或[群組聊天與多人聊天](https://developers.line.biz/en/docs/messaging-api/group-chats/)中接收到的 webhook 事件如下：

| Webhook 事件 | 接收時機 | 一對一聊天 | 群組聊天與多人聊天 |
| --- | --- | --- | --- |
| [Message event](https://developers.line.biz/en/reference/messaging-api/#message-event) | 當使用者傳送訊息時。你可以回覆此事件。 | ✅ | ✅ |
| [Unsend event](https://developers.line.biz/en/reference/messaging-api/#unsend-event) | 當使用者收回訊息時。如需更多關於處理此事件的資訊，請參閱[收到 unsend 事件時的處理](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-unsend-message)。 | ✅ | ✅ |
| [Follow event](https://developers.line.biz/en/reference/messaging-api/#follow-event) | 當使用者將你的 LINE 官方帳號加為好友，或解除封鎖你的 LINE 官方帳號時。你可以回覆此事件。 | ✅ | ❌ |
| [Unfollow event](https://developers.line.biz/en/reference/messaging-api/#unfollow-event) | 當使用者封鎖你的 LINE 官方帳號時 | ✅ | ❌ |
| [Join event](https://developers.line.biz/en/reference/messaging-api/#join-event) | 當你的 LINE 官方帳號加入群組聊天或多人聊天時。你可以回覆此事件。 | ❌ | ✅ |
| [Leave event](https://developers.line.biz/en/reference/messaging-api/#leave-event) | 當使用者從群組聊天或多人聊天中刪除你的 LINE 官方帳號，或你的 LINE 官方帳號離開時 | ❌ | ✅ |
| [Member join event](https://developers.line.biz/en/reference/messaging-api/#member-joined-event) | 當使用者加入你的 LINE 官方帳號所屬的群組聊天或多人聊天時。你可以回覆此事件。 | ❌ | ✅ |
| [Member leave event](https://developers.line.biz/en/reference/messaging-api/#member-left-event) | 當使用者離開你的 LINE 官方帳號所屬的群組聊天或多人聊天時 | ❌ | ✅ |
| [Postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) | 當使用者觸發 [postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action) 時。你可以回覆此事件。 | ✅ | ✅ |
| [Video viewing complete event](https://developers.line.biz/en/reference/messaging-api/#video-viewing-complete) | 當使用者看完由 LINE 官方帳號傳送、且指定了 `trackingId` 的影片訊息時。你可以回覆此事件。 | ✅ | ❌ |

✅ 你的 bot 伺服器會接收此事件&nbsp;&nbsp;&nbsp;&nbsp;❌ 你的 bot 伺服器不會接收此事件

#### Webhook when sending a message using liff.sendMessages() 

使用者無法從 LINE app 傳送[範本訊息（template message）](https://developers.line.biz/en/reference/messaging-api/#template-messages)或 [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)。不過，開發者可以使用 [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages)，代替使用者將訊息傳送到目前開啟 LINE MINI App 或 LIFF app 的聊天畫面。

當使用者透過 `liff.sendMessages()` 傳送範本訊息或 Flex Message 時，LINE Platform 不會傳送 webhook。對於所有其他[訊息類型](https://developers.line.biz/en/docs/messaging-api/message-types/)，則會傳送 webhook。

#### Receive quote messages sent by users via webhook 

當使用者引用過去的訊息來傳送訊息時，你可以在 webhook 的 `message` 屬性所含的 `quotedMessageId` 屬性中查看被引用訊息的 ID。在此情況下，你可以查看被引用訊息的 ID，但無法取得該訊息的內容（例如文字或貼圖）。

![](https://developers.line.biz/media/messaging-api/receiving-messages/chat-reply.png)

以下是當使用者引用過去訊息來傳送訊息時，送達你的 bot 伺服器的 webhook 範例。

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "message",
      "message": {
        "type": "text",
        "id": "468789577898262530", // ID of the sent message
        "quotedMessageId": "468789532432007169", // ID of the quoted message
        "quoteToken": "q3Plxr4AgKd...",
        "text": "Chicken, please." // Text of the sent message
      },
      "webhookEventId": "01H810YECXQQZ37VAXPF6H9E6T",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1692251666727,
      "source": {
        "type": "group",
        "groupId": "Ca56f94637c...",
        "userId": "U4af4980629..."
      },
      "replyToken": "38ef843bde154d9b91c21320ffd17a0f",
      "mode": "active"
    }
  ]
}
```

如需更多關於 `quotedMessageId` 屬性的資訊，請參閱 Messaging API 參考文件中 [Message event](https://developers.line.biz/en/reference/messaging-api/#message-event) 的 [text](https://developers.line.biz/en/reference/messaging-api/#wh-text) 與 [sticker](https://developers.line.biz/en/reference/messaging-api/#wh-sticker)。

如需更多關於使用者如何傳送引用訊息的資訊，請參閱 LINE 使用者指南中的[使用聊天回覆功能](https://guide.line.me/ja/friends-and-groups/create-groups.html)（僅提供日文版）。

#### Webhook when a message including a mention to a bot is sent 

如果使用者傳送的訊息提及（mention）你的 bot，傳送到 bot 伺服器的 webhook 事件中，文字訊息物件會設定以下值：

- `mention.mentionees[].type` 會被設為 `user`。
- `mention.mentionees[].userId` 會被設為 bot 的 user ID。
- `mention.mentionees[].isSelf` 會被設為 `true`。

例如，包含以下 message event 的 webhook 事件物件會被傳送到 bot 伺服器：

```json
"message": {
  "id": "444573844083572737",
  "type": "text",
  "quoteToken": "q3Plxr4AgKd...",
  "text": "@example_bot Good Morning!!",
  "mention": {
    "mentionees": [
      {
        "index": 0,
        "length": 12,
        "userId": "{user ID of the bot}",
        "type": "user",
        "isSelf": true
      }
    ]
  }
}
```

你可以在 [webhook 的請求主體](https://developers.line.biz/en/reference/messaging-api/#request-body)中的 `destination` 屬性，以及使用[取得 LINE 官方帳號（bot）資訊](https://developers.line.biz/en/reference/messaging-api/#get-bot-info)端點所取得的 `userId` 屬性中，查看 bot 的 user ID。

### Other webhook events 

beacon 與帳號連動也有以下 webhook 事件可供使用：

| Webhook 事件 | 接收時機 |
| --- | --- |
| [Beacon event](https://developers.line.biz/en/reference/messaging-api/#beacon-event) | 當使用者進入 Beacon 的接收範圍時。你可以回覆此事件。如需更多資訊，請參閱[在 LINE 中使用 beacon](https://developers.line.biz/en/docs/messaging-api/using-beacons/)。 |
| [Account link event](https://developers.line.biz/en/reference/messaging-api/#account-link-event) | 當使用者將其 LINE 帳號與你（身為服務供應商）服務的帳號連動時。你可以回覆此事件。如需更多資訊，請參閱[使用者帳號連動](https://developers.line.biz/en/docs/messaging-api/linking-accounts/)。 |

## Processing on receipt of unsend event 

使用者在傳送訊息後的一段有限時間內，可以收回訊息。

當使用者收回已傳送的訊息時，[unsend event](https://developers.line.biz/en/reference/messaging-api/#unsend-event) 會被傳送到 bot 伺服器。收到 unsend 事件時，我們建議服務供應商尊重使用者收回已傳送訊息的意願，並以最謹慎的態度妥善處理該訊息，使目標訊息在未來無法被查看或使用。

例如，你應該以下列方式處理使用者已收回的訊息：

- 取消顯示在你自己管理畫面等處的目標訊息。
- 刪除儲存在資料庫或其他儲存裝置中的目標訊息。

如需更多關於如何在 LINE app 中收回已傳送訊息的資訊，請參閱 LINE 使用者指南中的[使用收回訊息功能](https://guide.line.me/ja/chats-calls-notifications/chats/chat-delete.html)（僅提供日文版）。

## Redeliver a webhook that failed to be received 

Messaging API 提供重新傳遞（redeliver）你的 bot 伺服器接收失敗之 webhook 的功能。即使你的 bot 伺服器因暫時的過量存取或其他原因而未能正常回應 webhook，LINE Platform 也會在一段時間內重新傳遞該 webhook，因此你的 bot 伺服器可以在恢復後接收到該 webhook。

webhook 重新傳遞功能適用於所有 Messaging API 頻道（channel）。

<!-- note start -->

**啟用 webhook 重新傳遞前的注意事項**

- 由於網路路由問題等不同原因，同一個 webhook 事件可能會被多次傳送到你的 bot 伺服器。若要偵測重複，請使用 webhook 事件物件中的 `webhookEventId`。
- 如果 LINE Platform 重新傳遞 webhook，你接收 webhook 事件的順序可能會與事件實際發生的順序不同。如果這會造成問題，請查看 webhook 事件物件的 `timestamp` 以確認前後脈絡。

<!-- note end -->

### Redelivered webhooks 

重新傳遞的 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)內容，除了 `deliveryContext.isRedelivery` 的值之外，與原始的 webhook 事件物件相同。webhook 事件 ID 與回覆權杖（reply token）等值維持不變。

重新傳遞的 webhook 事件物件中所含的回覆權杖，除了某些特定情況外皆可使用。如需更多關於回覆權杖的資訊，請參閱 Messaging API 參考文件中的 [Reply token](https://developers.line.biz/en/reference/messaging-api/#send-reply-message-reply-token)。

### Enable webhook redelivery 

webhook 重新傳遞功能預設為停用。若要啟用 webhook 重新傳遞：

1. 從 [LINE Developers Console](https://developers.line.biz/console/) 開啟頻道設定畫面。
1. 點擊 **Messaging API** 分頁。
1. 啟用 **Use webhook**。
1. 啟用 **Webhook redelivery**。

當你啟用 **Webhook redelivery** 時，會顯示一則關於 webhook 重新傳遞的注意事項供你參考。請在啟用前閱讀並理解該注意事項。

![](https://developers.line.biz/media/messaging-api/receiving-messages/enable-webhook-redelivery-en.png)

### Conditions for webhook redelivery 

當符合以下條件時，LINE Platform 會以預先定義的次數與時間間隔重新傳送失敗的 webhook：

- [已啟用 webhook 重新傳遞](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#enable-webhook-redelivery)。
- bot 伺服器未針對該 webhook 回傳 `2xx` 狀態碼。

webhook 重新傳遞的次數與間隔並未公開。此外，次數與間隔可能在未事先通知的情況下變更。

<!-- note start -->

**可能無法重新傳遞 webhook**

請注意，webhook 重新傳遞並不保證 webhook 一定能可靠地送達。此外，如果 webhook 重新傳遞的次數突然增加，並被判定為會影響 LINE Platform 的運作，webhook 重新傳遞可能會被強制停用。

<!-- note end -->

## Check the cause of the webhook errors 

Messaging API 提供在傳送 webhook 時檢查錯誤原因與統計資料的功能。當 webhook 因 bot 伺服器上的問題等原因而未被接收時，這項功能有助於了解傳送 webhook 的狀態。

如需更多資訊，請參閱[檢查 webhook 錯誤原因與統計資料](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/)。

## Get user-sent content with webhook 

你可以使用 [webhook](https://developers.line.biz/en/reference/messaging-api/#webhooks) 中的訊息 ID，取得使用者所傳送的內容。可取得的內容類型如下：

- [圖片、影片、音訊、檔案](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#getting-content-file-sent-by-users)
- [圖片或影片的預覽圖片](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#getting-content-preview-image)

<!-- note start -->

**注意**

- 使用者傳送的內容會在一段時間後自動刪除。
- 你可以透過 webhook 的 [text](https://developers.line.biz/en/reference/messaging-api/#wh-text) 訊息物件取得使用者所傳送的文字。在接收 webhook 之後，並沒有可再次取得該文字的 API。

<!-- note end -->

### Get images, videos, audio, and files 

你可以使用 webhook 中的訊息 ID，取得使用者所傳送的[圖片](https://developers.line.biz/en/reference/messaging-api/#wh-image)、[影片](https://developers.line.biz/en/reference/messaging-api/#wh-video)、[音訊](https://developers.line.biz/en/reference/messaging-api/#wh-audio)與[檔案](https://developers.line.biz/en/reference/messaging-api/#wh-file)。

請求範例

```sh
curl -v -X GET https://api-data.line.me/v2/bot/message/{messageId}/content \
-H 'Authorization: Bearer {channel access token}'
```

如需更多資訊，請參閱 Messaging API 參考文件中的 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content)。

### Get a preview image of the image or video 

你可以使用 webhook 中的訊息 ID，取得使用者所傳送之圖片或影片的預覽圖片。

請求範例

```sh
curl -v -X GET https://api-data.line.me/v2/bot/message/{messageId}/content/preview \
-H 'Authorization: Bearer {channel access token}'
```

預覽圖片是將圖片資料轉換成比原始內容更小的資料大小。

例如，預覽圖片可作為縮圖使用。當你建置類似 CRM 的網站時，可以在下載大型圖片或影片的同時顯示縮圖。這讓使用者能快速掌握內容概要，提升系統的使用者體驗。

如需更多資訊，請參閱 Messaging API 參考文件中的 [Get a preview image of the image or video](https://developers.line.biz/en/reference/messaging-api/#get-image-or-video-preview)。

## Get user profile 

你可以使用 [webhook](https://developers.line.biz/en/reference/messaging-api/#webhooks) 中所含的使用者 ID，取得使用者的 LINE Profile（使用者的顯示名稱、user ID、個人檔案圖片 URL、狀態消息等）。

請求範例

```sh
curl -v -X GET https://api.line.me/v2/bot/profile/{userId} \
-H 'Authorization: Bearer {channel access token}'
```

若成功，會回傳一個 JSON 物件。

```json
{
  "displayName": "LINE Botto",
  "userId": "U4af4980629...",
  "pictureUrl": "https://profile.line-scdn.net/ch/v2/p/uf9da5ee2b...",
  "statusMessage": "Hello world!"
}
```

如需更多資訊，請參閱 Messaging API 參考文件中的 [Get profile](https://developers.line.biz/en/reference/messaging-api/#get-profile)。
