# 從 module channel 使用 Messaging API（Using the Messaging API from a module channel）

<!-- note start -->

**使用選用功能需要事先申請**

本文件所述的功能僅供已完成指定申請的企業客戶使用。如果您想使用 module 發布擴充功能，請聯絡業務代表，或透過 [LINE Marketplace Inquiry](https://line-marketplace.com/jp/inquiry)（僅提供日文）與我們聯繫。

<!-- note end -->

Module channel 與 Messaging API channel 一樣，可以使用 Messaging API 來傳送訊息以及切換 rich menu。

- [使用 module channel 的頻道存取權杖來使用 Messaging API](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#using-msg-api-with-module-channel-access-token)
- [接收 webhook](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-webhook)
- [從 module channel 取得 LINE 官方帳號（LINE Official Account）資訊](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-line-oa-info-from-module-channel)
- [注意事項](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#notes)

## Using the Messaging API with the channel access token of a module channel 

- [在 module channel 中使用的使用者 ID](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#user-id-used-in-module-channel)
- [module channel 的頻道存取權杖](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#module-channel-access-token)
- [呼叫 Messaging API 端點（endpoint）](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#call-msg-api-endpoint)
- [使用 Messaging API 的速率限制（rate limit）](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#rate-limits)

### User ID used in a module channel 

在 LINE Market Place 所提供的 module channel 中，識別每位使用者的識別碼，也就是[使用者 ID（user ID）](https://developers.line.biz/en/faq/#what-are-userid-groupid-and-roomid)，是由以字母「L」開頭的 68 位字元字串所組成的識別碼。

即使是同一位使用者，這個識別碼在不同的 LINE 官方帳號之間也會不同。

**以 L 開頭的 68 位識別碼範例：**

```
LUb577ef3cbe786a8da85ff8e902a03fc6-U5fac33f633e72c192759f09afc41fa28
```

### Channel access token of a module channel 

當 module channel 切換為 Active Channel 之後，您就可以使用 module channel 的頻道存取權杖（channel access token）來呼叫 Messaging API 或 Module Channel API。

您可以為 module channel 使用以下其中一種頻道存取權杖。

- [短效期頻道存取權杖（Short-lived channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)
- [可自訂有效期間的頻道存取權杖（Channel access token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)
- [無狀態頻道存取權杖（Stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)

您可以在 [LINE Developers Console](https://developers.line.biz/console/) 上 module channel 的 **Basic settings** 分頁中，找到簽發頻道存取權杖所需的資訊。

<!-- note start -->

**無法使用長效期頻道存取權杖**

長效期頻道存取權杖（Long-lived channel access token）無法用於 module channel。

<!-- note end -->

### Calling a Messaging API endpoint 

您可以使用 module channel 的頻道存取權杖來使用 Messaging API。

不過，請留意 scope 與 request header。

#### Scope 

若要使用 Messaging API，您必須具備為每個端點所定義的 scope。

scope 必須在連接（attach）module channel 時指定，並且必須取得 LINE 官方帳號管理者的使用許可。詳情請參閱[向 LINE 官方帳號管理者請求授權](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin)。

#### Request headers 

從 module channel 呼叫 Messaging API 端點時，請在 `Authorization` header 中指定 module channel 的頻道存取權杖。此外，由於 module channel 是設計用來連接多個 LINE 官方帳號的服務，因此請務必指定下方所述的「指定 bot 使用者 ID 的 header」。

<!-- parameter start (props: required) -->

Authorization

`Bearer {channel access token}`

對於 `{channel access token}`，請指定您 module channel 的頻道存取權杖。

<!-- parameter end -->
<!-- parameter start (props: required) -->

指定 bot 使用者 ID 的 header

連接到 module channel 的 LINE 官方帳號 bot 的使用者 ID。

您可以從[連接 module channel](https://developers.line.biz/en/reference/partner-docs/#link-attach-by-operation-module-channel-provider) 的回應，或 [Attached event](https://developers.line.biz/en/reference/partner-docs/#attached-event) 取得 bot 的使用者 ID。

<!-- note start -->

**具體的 header 將於參與後提供**

此 header 的名稱（參數名稱）僅向參與 [LINE Marketplace](https://line-marketplace.com/jp/inquiry)（僅提供日文）的客戶公開。

<!-- note end -->

<!-- parameter end -->

以下是透過 Messaging API 從 module channel 傳送[推播訊息（push message）](https://developers.line.biz/en/reference/messaging-api/#send-push-message)的範例。

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type:application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'Header specifying the bot user ID: xxxxxxxxxxxxxxxxxxxxxxxx'　\      // NEED THIS HEADER
-d '{
    "to": "LUb577ef3cbe...",
    "messages":[
        {
            "type":"text",
            "text":"Hello, world1"
        }
    ]
}'
```

### Rate limits for using the Messaging API 

從 module channel 使用 Messaging API 的速率限制，是以每個 module channel 為單位，針對連接到該 module channel 的每個 LINE 官方帳號 bot 的每項 API 功能（端點）分別套用。

即使您的 module channel 連接到多個 LINE 官方帳號 bot，速率限制仍會針對 `module channel x LINE 官方帳號 bot x API 功能` 的每個組合分別套用。

如需各端點速率限制的詳細資訊，請參閱 Messaging API 參考文件中的 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

### Get statistics of sent messages from a module channel 

您可以依匯總單位（aggregation unit）取得使用者如何與您傳送給多位使用者的[推播訊息（push message）](https://developers.line.biz/en/reference/messaging-api/#send-push-message)及[群發訊息（multicast message）](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)互動的統計資料。

module channel 的統計資料是使用 LINE 官方帳號 bot 與單位名稱（unit name）的組合來進行匯總。

舉例來說，在單一 module channel 中，名為「Unit A」的單位名稱的訊息分別從 LINE 官方帳號 A 與 B 傳送。此時，每個單位的統計資料會針對各個 LINE 官方帳號分別匯總。

當月（從該月 1 號到最後一天）所指派的單位名稱類型數量，也是以相同方式，使用 LINE 官方帳號 bot 與單位名稱的組合來計算。

如需更多資訊，請參閱 Messaging API 文件中的 [Get statistics of sent messages](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/)。

## Receiving a webhook 

當您在 module channel 中所註冊的 webhook URL 伺服器上收到 webhook 事件時，請檢查 `mode` 與 `destination` 屬性的值。

<!-- note start -->

**注意**

如果 module channel 的 webhook URL 伺服器未收到 webhook 事件，請檢查以下項目：

- module channel 必須連接到 LINE 官方帳號。請確認您可以從 module channel 向已將該 LINE 官方帳號加為好友的使用者傳送推播訊息。
- 在向 LINE 官方帳號管理者請求授權以連接 module channel 時，授權 URL 的 scope 查詢參數中必須指定 `message%3Areceive`（message:receive）。

如需有關 scope 的更多資訊，請參閱[向 LINE 官方帳號管理者請求授權](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin)。

<!-- note end -->

- [`mode` 屬性](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#mode-property)
- [`destination` 屬性](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#destination-property)
- [接收 module channel 專屬的 webhook 事件](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-module-channel-specific-webhook-events)

### `mode` property 

像是使用者傳送的訊息與加入好友等 webhook 事件，會同時傳送給連接到該 LINE 官方帳號的所有頻道（Primary Channel 以及連接到該 LINE 官方帳號的 Module Channel）。

![Chat control](https://developers.line.biz/media/partner-docs/module-technical/chat-control-en.png)

在處理 webhook 事件之前，請先確認各頻道是否擁有回應終端使用者（end user）的主導權（Chat Control）。

若要確認主導權（Chat Control），請使用 webhook 事件的 `mode` 屬性。

| `mode` 屬性的值 | 說明 |
| --- | --- |
| `active` | 收到 webhook 事件的頻道為 active 狀態。<br>收到此 webhook 事件的 webhook URL 伺服器可以傳送回覆訊息（reply message）、推播訊息等。 |
| `standby` | 收到 webhook 事件的頻道為等待中狀態。<br>收到此 webhook 事件的 webhook URL 伺服器不應傳送訊息。<br><br>送達等待中頻道的 webhook 事件不會包含 `replyToken` 屬性。因此，無法使用回覆訊息。 |

在連接到 LINE 官方帳號的各個頻道中，只有一個頻道的 `mode` 屬性會設定為 `active`。其餘所有頻道的 `mode` 屬性都會設定為 `standby`。

以下是當 `mode` 屬性的值為 `active` 或 `standby` 時，所傳送的 webhook 事件範例：

```sh
#Example of a webhook sent to Active Channel
{
    "replyToken": "0f3779fba3b349968c5d07db31eab56f", // NOTICE THIS PROPERTY
    "type": "message",
    "mode": "active", // NOTICE THIS PROPERTY
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "LUb577ef3cbe..."
    },
    "message": {
        "id": "325708",
        "type": "text",
        "text": "Hello, world"
    }
}

#Example of a webhook event sent to the Standby Channel
{
    // replyToken PROPERTY DOES NOT EXIST
    "type": "message",
    "mode": "standby", // NOTICE THIS PROPERTY
    "timestamp": 1462629479859,
    "source": {
        "type": "user",
        "userId": "U4af4980629..."
    },
    "message": {
        "id": "325708",
        "type": "text",
        "text": "Hello, world!"
    }
}
```

### `destination` property 

如下圖所示，module channel 可能連接到多個 LINE 官方帳號（OA「X」、OA「Y」、OA「Z」……）。

![Attach same service](https://developers.line.biz/media/partner-docs/module-technical/attach-same-service-en.png)

因此，請使用 destination 屬性來判斷該 webhook 是從哪個 LINE 官方帳號傳送的。

<!-- parameter start -->

destination

String

傳送該 webhook 事件的 LINE 官方帳號 bot 的使用者 ID。

bot 使用者 ID 的值是符合正規表示式 `U[0-9a-f]{32}` 的字串。

<!-- parameter end -->

以下是 webhook 事件的範例：

```sh
{
  "destination": "U53387d54817...",  // CHECK THIS PROPERTY
  "events": [...]
}
```

### Receiving module channel-specific webhook events 

以下這些 webhook 事件會傳送到 module channel 的 webhook URL 伺服器。

| 事件類型 | 說明 |
| --- | --- |
| [Attached event](https://developers.line.biz/en/reference/partner-docs/#attached-event) | 此事件表示 module channel 已連接到 LINE 官方帳號。 |
| [Detached event](https://developers.line.biz/en/reference/partner-docs/#detached-event) | 此事件表示 module channel 已從 LINE 官方帳號中斷連接。 |
| [Activated event](https://developers.line.biz/en/reference/partner-docs/#activated-event) | 此事件表示透過呼叫 [Acquire Control API](https://developers.line.biz/en/reference/partner-docs/#acquire-control-api)，module channel 已切換為 Active Channel。 |
| [Deactivated event](https://developers.line.biz/en/reference/partner-docs/#deactivated-event) | 此事件表示透過呼叫 [Acquire Control API](https://developers.line.biz/en/reference/partner-docs/#acquire-control-api) 或 [Release Control API](https://developers.line.biz/en/reference/partner-docs/#release-control-api)，module channel 已切換為 Standby Channel。 |
| [botSuspend event](https://developers.line.biz/en/reference/partner-docs/#botsuspend-event) | 此事件表示該 LINE 官方帳號已被停用（Suspend）。 |
| [botResumed event](https://developers.line.biz/en/reference/partner-docs/#botresumed-event)  | 此事件表示該 LINE 官方帳號已從停用狀態恢復。 |

<!-- tip start -->

**如何偵測主導權（Chat Control）的變化**

當 module channel 設定為 Active Channel 時，主導權（Chat Control）可能會在未呼叫 Release Control API 的情況下自動變更。您可以透過以下方式偵測主導權（Chat Control）的變化：

| 事件類型 | 說明 |
| --- | --- |
| <ul><li>[Activated event](https://developers.line.biz/en/reference/partner-docs/#activated-event)</li><li>[Deactivated event](https://developers.line.biz/en/reference/partner-docs/#deactivated-event)</li></ul>  | 當連接到 LINE 官方帳號的 module channel 呼叫 Acquire Control API 或 Release Control API，且聊天的主導權（Chat Control）將被切換時，會傳送此事件。 |
| <ul><li>[Follow event](https://developers.line.biz/en/reference/messaging-api/#follow-event)</li><li>[Unfollow event](https://developers.line.biz/en/reference/messaging-api/#unfollow-event)</li></ul> | 當終端使用者封鎖 LINE 官方帳號後又再次將其加為好友時，會傳送此事件。<br>當終端使用者封鎖 LINE 官方帳號後又再次將其加為好友時，主導權（Chat Control）會自動重設為預設狀態。如果該 module channel 具備 [Default Active](https://developers.line.biz/en/docs/partner-docs/module-technical-chat-control/#default-active) 功能，它就會自動成為 Active Channel。 |

<!-- tip end -->

<!-- tip start -->

**關於 LINE 官方帳號的停用狀態（Suspend）**

無論 module channel 的設定或服務可用性如何，LINE 官方帳號都可能因 LINE 官方帳號營運者的考量而被停用（Suspend）。具體來說，LINE 官方帳號會在以下情況下被停用：

- 當營運者刪除該 LINE 官方帳號時
- 當該 LINE 官方帳號因任何原因被停止使用時

在某些情況下，LINE 官方帳號可能會從停用狀態恢復。當 LINE 官方帳號被停用或恢復時，會傳送 webhook 事件。

請實作 module，使其與 module channel 端所管理的資訊不會產生衝突。

<!-- tip end -->

## Getting the LINE Official Account information from a module channel 

您可以使用以下 API 取得連接到 module channel 的每個 LINE 官方帳號的相關資訊：

- [取得 LINE 官方帳號（bot）資訊](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-bot-info)
- [取得 module 所連接的 bot 清單](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-multiple-bot-info)

### Get LINE Official Account (bot) information 

取得已連接 module channel 的 LINE 官方帳號 bot 的基本資訊。如需更多資訊，請參閱 Messaging API 文件中的 [Get LINE Official Account (bot) info](https://developers.line.biz/en/reference/messaging-api/#get-bot-info)。

此外，請在 request header 中指定以下內容：

<!-- parameter start -->

Authorization

Bearer `{channel access token}`

對於 `{channel access token}`，請指定您 module channel 的頻道存取權杖。

<!-- parameter end -->
<!-- parameter start -->

指定 bot 使用者 ID 的 header

連接到 module channel 的 LINE 官方帳號 bot 的使用者 ID。

您可以從 [Attach by operation of the module channel provider](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#link-attach-by-operation-module-channel-provider) 的回應，或 [Attached event](https://developers.line.biz/en/reference/partner-docs/#attached-event) 取得 bot 的使用者 ID。

<!-- note start -->

**具體的 header 將於參與後提供**

此 header 的名稱（參數名稱）僅向參與 [LINE Marketplace](https://line-marketplace.com/jp/inquiry)（僅提供日文）的客戶公開。

<!-- note end -->

<!-- parameter end -->

### Get a list of bots to which the module is attached 

取得已連接 module channel 的多個 LINE 官方帳號 bot 的基本資訊清單。如需更多資訊，請參閱企業客戶選用功能 API 參考文件中的 [Get a list of bots to which the module is attached](https://developers.line.biz/en/reference/partner-docs/#get-multiple-bot-info-api)。

## Notes 

- 中斷連接 module channel 時，設定的生效會有一段時間差。請勿在中斷連接後傳送請求。
- 如果您想為目標帳號新增 scope，即使是已經連接的帳號，您也可以這麼做。
