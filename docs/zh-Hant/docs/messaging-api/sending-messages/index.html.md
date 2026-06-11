# 傳送訊息（Send messages）

透過 Messaging API，你可以讓你的機器人（bot）傳送訊息給使用者。你隨時都可以主動傳送訊息給使用者，也可以回覆使用者的訊息。你還能使用各種不同的訊息類型。

| | |
| --- | --- |
| 傳送方式（Messaging types） | <ul><li>回覆訊息（Reply message）</li><li>推播訊息（Push message）：一對一</li><li>多人發送訊息（Multicast message）：一對多（以使用者 ID 清單為目標）</li><li>分眾訊息（Narrowcast message）：一對多（以分眾清單為目標）</li><li>群發訊息（Broadcast message）：一對多（以所有好友為目標）</li></ul> |
| 訊息類型（Message types） | <ul><li>文字訊息（Text message）</li><li>文字訊息（Text message）(v2)</li><li>貼圖訊息（Sticker message）</li><li>圖片訊息（Image message）</li><li>影片訊息（Video message）</li><li>音訊訊息（Audio message）</li><li>位置訊息（Location message）</li><li>圖文訊息（Imagemap message）</li><li>範本訊息（Template message）</li><li>Flex Message</li></ul>有關訊息類型的更多資訊，請參閱 [Message types](https://developers.line.biz/en/docs/messaging-api/message-types/)。 |

## Messaging types 

Messaging API 提供兩種主要的傳送方法供你使用。

- [回覆使用者的訊息與動作（回覆訊息）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#reply-messages)
- [隨時傳送訊息](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-messages-at-any-time)

### Reply to messages and actions from users (reply messages) 

當使用者將你的 LINE 官方帳號（LINE Official Account）加為好友，或向你的 LINE 官方帳號傳送訊息時，你可以透過 Messaging API 進行回覆。請將 `replyToken` 屬性設定為你透過使用者動作所收到的 [Webhook 事件（webhook event）](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects) 中取得的回覆權杖（reply token）。在單一請求中，你最多可以傳送五個[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)。

<!-- tip start -->

**你可以在準備回覆訊息時顯示載入動畫**

當你的 LINE 官方帳號收到使用者的訊息後，因為訊息準備或預約處理，回應可能需要一些時間。在這種情況下，你可以透過顯示載入動畫，以視覺方式告訴使用者你希望他們稍候。有關更多資訊，請參閱 [Display a loading animation](https://developers.line.biz/en/docs/messaging-api/use-loading-indicator/)。

<!-- tip end -->

以下是傳送回覆訊息的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/message/reply \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "replyToken":"nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
    "messages":[
        {
            "type":"text",
            "text":"Hello, user"
        },
        {
            "type":"text",
            "text":"May I help you?"
        }
    ]
}'
```

有關更多資訊，請參閱 Messaging API 參考文件中的 [Send reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)。

### Send messages at any time 

你可以使用以下任一方法，隨時向使用者傳送訊息：

| 傳送方式（Messaging type） | 說明 |
| --- | --- |
| [推播訊息（Push message）](https://developers.line.biz/en/reference/messaging-api/#send-push-message)  | 向使用者、群組聊天室與多人聊天室傳送訊息。例如，你可以用它來通知使用者，他們在你的購物網站上購買的商品已出貨。 |
| [多人發送訊息（Multicast message）](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message) | 一次向多位使用者傳送訊息。它與分眾訊息的差異在於，你是以使用者 ID 指定目標收件者。例如，你可以用它來通知你購物網站的所有會員某項新功能。 |
| [分眾訊息（Narrowcast message）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-narrowcast-message)  | 一次向多位使用者傳送訊息。它與多人發送訊息的差異在於，你是以使用者的屬性資料或再行銷（受眾，audiences）指定目標收件者。使用者屬性資料包含性別、年齡、OS 類型、地區等。 |
| [群發訊息（Broadcast message）](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)  | 你可以向所有與你的 LINE 官方帳號為好友的使用者傳送相同的訊息。 |

在單一請求中，你最多可以傳送五個[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)。

<!-- tip start -->

**如何計算訊息數量**

被計為已傳送的訊息數量，是你傳送對象的人數。你在單一請求中指定的[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)數量，不會影響傳送的訊息數量。假設你在單一請求中以四個訊息物件向一個包含五人的聊天室傳送推播訊息。在此情況下，傳送的訊息數量為五。

傳送給不會收到你訊息的使用者所發送的訊息，會被排除在計數之外。這類使用者是指其使用者 ID 已封鎖你的 LINE 官方帳號，或其使用者 ID 不存在的使用者。

<!-- tip end -->

以下是傳送推播訊息的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": "U4af4980629...",
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        },
        {
            "type":"text",
            "text":"Hello, world2"
        }
    ]
}'
```

## Send narrowcast messages 

分眾訊息讓你可以在想要的時候，向多位使用者傳送訊息。你無法將分眾訊息傳送至群組聊天室或多人聊天室。對於分眾訊息，請以年齡、性別、OS、地區等屬性資料，或透過再行銷（受眾，audiences）來指定收件者。

要傳送分眾訊息：

1. [準備受眾或請求 ID](https://developers.line.biz/en/docs/messaging-api/sending-messages/#prepare-audience-or-request-id)
1. [開始傳送分眾訊息](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-narrowcast-message-detail)
1. [查詢分眾訊息的狀態](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-narrowcast-progress-status)

### Prepare audience or request ID 

要傳送分眾訊息，你必須依目標收件者準備一個受眾或請求 ID。你可以使用邏輯運算子（AND、OR、NOT）組合目標收件者。例如，你可以用 OR 運算，將收到訊息 A 的使用者與點擊訊息 B 中 URL 的使用者，都納入目標收件者。

| 目標收件者 | 需準備的資料 |
| --- | --- |
| 所有將你的 LINE 官方帳號加為好友的使用者 | 不需要 |
| 可透過[使用者 ID（user ID）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#user-id)或廣告識別碼（Identifier for Advertisers，IFA）識別的使用者 | <ul><li>[上傳使用者 ID 的受眾（以 JSON）](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group)</li><li>[上傳使用者 ID 的受眾（以檔案）](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group-by-file)</li></ul> |
| 點擊你所傳送訊息中 URL 的使用者 | [訊息點擊受眾（Message click audience）](https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group) |
| 開啟你所傳送訊息的使用者 | [訊息曝光受眾（Message impression audience）](https://developers.line.biz/en/reference/messaging-api/#create-imp-audience-group) |
| 收到分眾訊息的使用者 | 在[收件者物件（recipient object）](https://developers.line.biz/en/reference/messaging-api/#narrowcast-recipient)的重新發送物件（redelivery object）中，指定先前發送的分眾訊息的請求 ID。 |
| 在聊天中具有特定標籤的使用者 | 聊天標籤受眾（Chat tag audience）。請使用 [LINE Official Account Manager](https://manager.line.biz/) 建立。 |
| 透過特定路徑將你的 LINE 官方帳號加為好友的使用者 | 好友路徑受眾（Friend path audience）。請使用 [LINE Official Account Manager](https://manager.line.biz/)。 |
| 先前曾預約到訪的使用者 | 預約受眾（Reservation audience）。請使用 [LINE Official Account Manager](https://manager.line.biz/) 建立。 |
| 瀏覽過圖文選單（rich menu）的使用者 | 圖文選單曝光受眾（Rich menu impression audience）。請使用 [LINE Official Account Manager](https://manager.line.biz/) 建立。 |
| 點擊過圖文選單的使用者 | 圖文選單點擊受眾（Rich menu click audience）。請使用 [LINE Official Account Manager](https://manager.line.biz/) 建立。 |
| 以 LINE Tag 追蹤資訊篩選出的使用者 | 網站流量受眾（Web traffic audience，LINE Tag）。請使用 [LINE Official Account Manager](https://manager.line.biz/) 或 [LINE Ad Manager](https://admanager.line.biz/) 建立。 |
| 以 Tracking Tag 資訊篩選出的使用者 | 網站流量受眾（Web traffic audience，Tracking Tag）。請使用 [LINE Official Account Manager](https://manager.line.biz/) 建立。 |
| 觀看過你所傳送影片的使用者 | 影片觀看受眾（Video view audience）。請使用 [LINE Ad Manager](https://admanager.line.biz/) 建立。 |
| 在 App 內參與特定事件的使用者（例如：開啟 App、在 App 內進行購買） | App 事件受眾（App event audience）。請使用 [LINE Ad Manager](https://admanager.line.biz/) 建立。 |
| 點擊過你所傳送圖片的使用者 | 圖片點擊受眾（Image click audience）。請使用 [LINE Ad Manager](https://admanager.line.biz/) 建立。 |
| 看過[Beacon 橫幅（beacon banner）](https://developers.line.biz/en/docs/messaging-api/using-beacons/#beacon-banner)的使用者 | LINE Beacon Network 廣告曝光受眾（LINE Beacon Network ad impression audience）。請使用 [LINE Ad Manager](https://admanager.line.biz/) 建立。LINE Beacon Network 廣告曝光受眾僅供台灣使用者所建立的 LINE 官方帳號使用。 |

<!-- note start -->

**注意**

你無法透過 Messaging API 建立以下類型的受眾：

- 聊天標籤受眾（Chat tag audience）
- 好友路徑受眾（Friend path audience）
- 預約受眾（Reservation audience）
- 圖文選單曝光受眾（Rich menu impression audience）
- 圖文選單點擊受眾（Rich menu click audience）
- 網站流量受眾（Web traffic audience，LINE Tag）
- 網站流量受眾（Web traffic audience，Tracking Tag）
- App 事件受眾（App event audience）
- 影片觀看受眾（Video view audience）
- 圖片點擊受眾（Image click audience）
- LINE Beacon Network 廣告曝光受眾（LINE Beacon Network ad impression audience）

<!-- note end -->

建立受眾後，請依下列說明確認它已準備好可接受訊息。

#### Confirm that the audience can be used for delivery 

受眾是在背景以非同步方式建立的。在向某個受眾傳送分眾訊息前，請確認該受眾的狀態為 `READY`（已準備好可接受訊息）。

你可以使用以下端點查詢受眾的狀態：

```sh
curl -v -X GET https://api.line.me/v2/bot/audienceGroup/{audienceGroupId} \
-H 'Authorization: Bearer {channel access token}'
```

如果回應中的 `status` 屬性為 `READY`（已準備好可接受訊息），那麼你就可以向該受眾傳送分眾訊息。

有關如何查詢受眾狀態的更多資訊，請參閱 Messaging API 參考文件中的 [Get audience data](https://developers.line.biz/en/reference/messaging-api/#get-audience-group)。

### Begin sending narrowcast messages 

當你傳送分眾訊息時，可以組合以下這些物件來縮小目標收件者範圍。

- [收件者物件（Recipient object）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#recipient-object)
  - [受眾物件（Audience object）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#audience-object)
  - [重新發送物件（Redelivery object）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#redelivery-object)
- [人口屬性篩選物件（Demographic filter object）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#demographic-filter-object)
- [運算子物件（Operator object）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#operator-object)
- [上限物件（Limit object）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#limit-object)

例如，你可以指定目標收件者為來自兩個受眾、且年齡不在 15-20 歲之間的女性。你可以用邏輯運算子（AND、OR、NOT）組合這些物件。

![](https://developers.line.biz/media/messaging-api/narrowcast-message/narrow_cast.png)

你每月可傳送的訊息數量有上限。如果你試圖傳送超過上限，傳送將會失敗。為了讓外發訊息的數量不超過上限，請將 `limit.upToRemainingQuota` 屬性設定為 `true`。有關你可傳送訊息數量上限的更多資訊，請參閱 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。

<!-- note start -->

**在分眾訊息傳送完成前，其他訊息可能會傳送失敗**

當你傳送分眾訊息時，無論實際傳送的訊息數量為何，你可能會達到該月份可預留訊息數的概略上限。一旦達到此概略上限，你就必須等到分眾訊息傳送完成，因為你無法超過上限。如果你在該狀態下嘗試傳送其他訊息，將會回傳 `You have reached your monthly limit.`，且該訊息將傳送失敗。

有關更多資訊，請參閱 Messaging API 參考文件中的 [Note regarding the number of remaining messages to be sent during the current month](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-cautions)。

<!-- note end -->

#### Recipient object 

當你傳送分眾訊息時，請在請求主體（request body）中以 `messages` 屬性指定訊息內容，並以 `recipient` 屬性指定訊息目標。如果你未指定 `recipient` 屬性，訊息收件者將會是所有將你的 LINE 官方帳號加為好友的使用者。

對於 `recipient` 屬性，你可以指定[受眾物件（audience objects）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#audience-object)或[重新發送物件（redelivery objects）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#redelivery-object)。

##### Audience object 

要向某個受眾傳送分眾訊息，請將請求主體中的 `recipient` 屬性設定為一個受眾物件。要建立受眾物件，請在物件中以 `type` 屬性指定 `"audience"`，並以 `audienceGroupId` 屬性指定你的受眾 ID。如果你還沒有受眾，請使用[管理受眾（managing audience）](https://developers.line.biz/en/reference/messaging-api/#manage-audience-group) API 建立一個。

以下是受眾物件的範例：

```json
{
  "type": "audience",
  "audienceGroupId": 5614991017776
}
```

##### Redelivery object 

要向先前曾收到分眾訊息的使用者傳送分眾訊息，請將請求主體中的 `recipient` 屬性設定為一個重新發送物件。重新發送物件的 `type` 屬性設定為 `"redelivery"`。請將 `requestId` 屬性設定為你傳送分眾訊息時所取得的請求 ID（`X-Line-Request-Id`）。

以下是重新發送物件的範例：

```json
{
  "type": "redelivery",
  "requestId": "5b59509c-c57b-11e9-aa8c-2a2ae2dbcce4"
}
```

![Interactive SVG](https://developers.line.biz/media/news/redeliver-narrowcast-en.svg)

<!-- note start -->

**&quot;There weren't enough recipients&quot; 錯誤**

如果你嘗試以重新發送物件指定先前已傳送訊息的請求 ID 來傳送訊息，但回傳了 `errorCode` 為 `2`（這表示因為收件者數量不足而發生錯誤），則可能的原因如下：

- 先前的目標收件者中，有部分人在收到所參照的分眾訊息後封鎖了你的 LINE 官方帳號，導致數量減少。
- 由於你使用[運算子（operators）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#operator-object)（AND 或 NOT）將其與其他受眾物件或人口屬性篩選物件組合，使目標收件者數量減少。

為防止有人猜測收件者的屬性，當收件者數量少於所需的最低數量時，你將無法傳送分眾訊息。有關更多資訊，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。

<!-- note end -->

有關受眾物件與重新發送物件的更多資訊，請參閱 Messaging API 參考文件中的 [Recipient object](https://developers.line.biz/en/reference/messaging-api/#narrowcast-recipient)。

#### Demographic filter object 

透過指定人口屬性篩選物件（`filter.demographic` 屬性），你可以依據使用者的屬性（性別、年齡、OS 類型、地區等）進行分眾發送訊息。

以下是依性別篩選的人口屬性篩選物件範例：

```json
{
  "type": "gender",
  "oneOf": ["male", "female"]
}
```

有關更多資訊，請參閱 Messaging API 參考文件中的 [Demographic filter object](https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter)。

#### Operator object 

使用運算子物件的乘積集（AND）、聯集（OR）與差集（NOT），可以組合收件者物件與人口屬性篩選物件的多個條件，以指定目標收件者。

![](https://developers.line.biz/media/messaging-api/narrowcast-message/operator_object.png)

以下是以運算子物件指定的收件者物件範例：

```json
"recipient": {
    "type": "operator",
    "and": [
        {
            "type": "audience",
            "audienceGroupId": 5614991017776
        },
        {
            "type": "operator",
            "not": {
                "type": "redelivery",
                "requestId": "5b59509c-c57b-11e9-aa8c-2a2ae2dbcce4"
            }
        }
    ]
}
```

<!-- tip start -->

**你可以使用運算子物件以巢狀結構指定目標收件者**

你可以使用運算子物件將收件者物件與人口屬性篩選物件巢狀組合，以指定收件者。運算子物件會從巢狀的最深層級開始優先套用。

此圖中的目標收件者會被解讀為「**符合 A、B 與 E，但不符合 C 與 D 的使用者**（`AudienceA AND AudienceB AND NOT (AudienceC AND Audience D) AND Audience E`）」。

![](https://developers.line.biz/media/messaging-api/narrowcast-message/operator_object_nest_sample.png)

```json
{
    "type": "operator",
    "and": [
        {
            "type": "audience",
            "audienceGroupId": AudienceA
        },
        {
            "type": "audience",
            "audienceGroupId": AudienceB
        },
        {
            "type": "operator",
            "not": {
                "type": "operator",
                "and": [
                    {
                       "type": "audience",
                       "audienceGroupId": AudienceC
                    },
                    {
                       "type": "audience",
                       "audienceGroupId": AudienceD
                    },
                 ]
            }
        },
        {
            "type": "audience",
            "audienceGroupId": AudienceE
        },
    ]
}
```

<!-- tip end -->

#### Limit object 

你可以透過設定上限物件，為可傳送的分眾訊息設定最大數量上限。如果收件者受到限制，將會隨機選取收件者。

以下是上限物件的範例：

```json
{
  "max": 100,
  "upToRemainingQuota": true,
  "forbidPartialDelivery": true
}
```

有關更多資訊，請參閱 Messaging API 參考文件中的 [Limit objects](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-limit)。

##### Controlling the maximum number of messages to send with limit objects 

以下是使用上限物件控制最大傳送數量的範例：

| 條件 \* | 觸及目標數：100<br>每月上限：90<br>目標收件者：80 | 觸及目標數：100<br>每月上限：50<br>目標收件者：80 |
| --- | --- | --- |
| 未指定上限物件 | ❌ 請求錯誤<br>（觸及目標數超過每月上限） | ❌ 請求錯誤<br>（觸及目標數超過每月上限） |
| 未指定 `max`<br>`upToRemainingQuota`=`true`<br>`forbidPartialDelivery`=`false` | ✅ 傳送給所有收件者 | ✅ 傳送給 50 位收件者，在每月上限範圍內 |
| 未指定 `max`<br>`upToRemainingQuota`=`true`<br>`forbidPartialDelivery`=`true` | ✅ 傳送給所有收件者 | ❌ 因部分傳送而取消傳送 |
| `max`=30<br>`upToRemainingQuota`=`true`<br>`forbidPartialDelivery`=`false` |  ✅ 傳送給 30 位收件者，等於 `max` 值 | ✅ 傳送給 30 位收件者，等於 `max` 值 |
| `max`=30<br>`upToRemainingQuota`=`true`<br>`forbidPartialDelivery`=`true` | ❌ 因部分傳送而取消傳送 | ❌ 因部分傳送而取消傳送 |

\* 條件中所用詞彙的說明如下：

- 觸及目標數（Target reach）：你可透過訊息觸及的使用者數量。
- 每月上限（Monthly limit）：當月傳送訊息的估計上限。有關更多資訊，請參閱 Messaging API 參考文件中的 [Get the target limit for sending messages this month](https://developers.line.biz/en/reference/messaging-api/#get-quota)。
- 目標收件者（Target recipients）：依屬性（如年齡、性別、OS 與地區）或再行銷（受眾，audiences）篩選出的收件者。

### Example request to send a narrowcast message 

假設我們想要請求向符合以下條件的使用者傳送分眾訊息：

- 屬於某個受眾（受眾 ID：`5614991017776`）
- 未收到分眾訊息（請求 ID：`5b59509c-c57b-11e9-aa8c-2a2ae2dbcce4`）
- 是 20-25 歲之間的男性或女性
- 居住於秋田縣或愛知縣
- 已成為此範例 LINE 官方帳號的好友 7 至 30 天
- 是 35 至 40 歲之間的女性（排除男性）

以下是向上述指定目標收件者傳送分眾訊息的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/message/narrowcast \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "messages": [
        {
            "type": "text",
            "text": "test message"
        }
    ],
    "recipient": {
        "type": "operator",
        "and": [
            {
                "type": "audience",
                "audienceGroupId": 5614991017776
            },
            {
                "type": "operator",
                "not": {
                    "type": "redelivery",
                    "requestId": "5b59509c-c57b-11e9-aa8c-2a2ae2dbcce4"
                }
            }
        ]
    },
    "filter": {
        "demographic": {
            "type": "operator",
            "or": [
                {
                    "type": "operator",
                    "and": [
                        {
                            "type": "gender",
                            "oneOf": [
                                "male",
                                "female"
                            ]
                        },
                        {
                            "type": "age",
                            "gte": "age_20",
                            "lt": "age_25"
                        },
                        {
                            "type": "appType",
                            "oneOf": [
                                "android",
                                "ios"
                            ]
                        },
                        {
                            "type": "area",
                            "oneOf": [
                                "jp_23",
                                "jp_05"
                            ]
                        },
                        {
                            "type": "subscriptionPeriod",
                            "gte": "day_7",
                            "lt": "day_30"
                        }
                    ]
                },
                {
                    "type": "operator",
                    "and": [
                        {
                            "type": "age",
                            "gte": "age_35",
                            "lt": "age_40"
                        },
                        {
                            "type": "operator",
                            "not": {
                                "type": "gender",
                                "oneOf": [
                                    "male"
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    },
    "limit": {
        "max": 100,
        "upToRemainingQuota": true
    }
}'
```

有關更多資訊，請參閱 Messaging API 參考文件中的 [Sending narrowcast messages](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)。

### Check the status of a narrowcast message 

分眾訊息是在背景以非同步方式傳送的。要查詢分眾訊息是否傳送成功，請如下方範例所示執行 [Get narrowcast message status](https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status) 端點。

```sh
curl -v -X GET 'https://api.line.me/v2/bot/message/progress/narrowcast?requestId={request_id}' \
-H 'Authorization: Bearer {channel access token}'
```

## Send quote messages 

你可以使用 Messaging API 傳送引用過去訊息的訊息。

![](https://developers.line.biz/media/messaging-api/sending-messages/quote-message.png)

要傳送引用過去訊息的訊息，請指定要引用訊息的引用權杖（quote token，`quoteToken`）。有關如何取得引用權杖的更多資訊，請參閱 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

**引用過去訊息的推播訊息請求範例**

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
  "to": "U4af4980629...",
  "messages": [
    {
      "type": "text",
      "text": "Yes, you can.",
      "quoteToken": "yHAz4Ua2wx7..." // Specify the quote token of the message to be quoted
    }
  ]
}'
```

請注意，如果要引用訊息的傳送已被取消，或過去的聊天記錄已從裝置中刪除，則引用的訊息將不會顯示。

![If the message to be quoted does not exist, it will be displayed as "Message unavailable."](https://developers.line.biz/media/messaging-api/sending-messages/delete-quoted-message-en.png)

你只能在以下端點使用引用權杖來傳送訊息：

- [Send reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)
- [Send push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message)

此外，使用引用權杖傳送訊息時，你只能使用以下訊息物件：

- [文字訊息（Text message）](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)
- [文字訊息（Text message）(v2)](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages-v2)
- [貼圖訊息（Sticker message）](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)
