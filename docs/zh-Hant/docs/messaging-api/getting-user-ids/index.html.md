# 取得使用者 ID（Get user IDs）

若要透過 Messaging API 向使用者傳送訊息，您必須以使用者 ID（user ID）指定該使用者。本文說明如何取得使用者 ID。

<!-- table of contents -->

## What is user ID 

使用者 ID 是使用者的唯一識別碼，與顯示名稱（display name）或使用者為了讓好友可搜尋而註冊的 LINE ID 不同。LINE Platform 會發行格式為 `U[0-9a-f]{32}`（正規表示式）的字串作為使用者 ID。使用者 ID 的範例如：`U8189cf6745fc0d808977bdb0b9f22995`。

![](https://developers.line.biz/media/messaging-api/getting-user-ids/display-name-and-id-and-user-id-en.png)

### Unit for issuing user IDs 

即使是同一位使用者，每個供應商（provider）所發行的使用者 ID 值也各不相同。若供應商相同，則無論頻道類型（channel）為何（LINE Login 頻道或 Messaging API 頻道），使用者 ID 都相同。

舉例來說，假設同一個供應商底下有一個 Messaging API 頻道與一個 LINE Login 頻道，您從各個頻道取得的使用者 A 的使用者 ID 會是相同的值。但是，您從不同供應商底下的頻道所取得的使用者 A 的使用者 ID 則會是不同的值。

![](https://developers.line.biz/media/messaging-api/getting-user-ids/user-id-for-each-provider-en.png)

## Getting a user ID 

您可以透過以下四種方法取得使用者 ID：

1. [開發者取得自己的使用者 ID](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-own-user-id)
1. [從 webhook 取得使用者 ID](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-user-ids-in-webhook)
1. [取得所有好友的使用者 ID](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-all-friends-user-ids)
1. [取得群組與多人聊天室成員的使用者 ID](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-member-user-ids)

### Developer gets their own user ID 

身為開發者，您可以在 [LINE Developers Console](https://developers.line.biz/console/) 中頻道的 **Basic settings** 分頁的 **Your user ID** 找到自己的使用者 ID。詳情請參閱 LINE Developers Console 文件中的 [Channel roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel)。目前沒有可供開發者取得自己使用者 ID 的 API。

<!-- tip start -->

**您必須將 LINE 帳號與 Business ID 連結**

如果您的 Business ID 尚未連結到 LINE 帳號，**Basic settings** 分頁的 **Your user ID** 將不會顯示。依 LINE 帳號連結狀態的顯示差異如下：

| LINE 帳號已連結 | LINE 帳號未連結 |
| --- | --- |
| ![](https://developers.line.biz/media/messaging-api/getting-user-ids/get-own-user-id-linked-line-account-en.png) | ![](https://developers.line.biz/media/messaging-api/getting-user-ids/get-own-user-id-unlinked-line-account-en.png) |

如需如何連結 LINE 帳號的詳情，請參閱 LINE Developers Console 文件中的 [Link your Business ID with your LINE account](https://developers.line.biz/en/docs/line-developers-console/login-account/#link-business-account-with-line-account)。

<!-- tip end -->

### Get a user ID from webhook 

當使用者將您的 LINE 官方帳號加為好友，或向您的 LINE 官方帳號傳送訊息時，LINE Platform 會將 webhook 傳送到 LINE Developers Console 中 **Webhook URL** 所指定的 URL（bot 伺服器）。使用者 ID 會包含在該 webhook 中。

以下是當使用者將 LINE 官方帳號加為好友時，LINE Platform 所傳送的 [webhook event 物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)範例：

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "follow",
      "timestamp": 1462629479859,
      "source": {
        // You can get the user ID from the userId property of the source object
        "type": "user",
        "userId": "U8189cf6745fc0d808977bdb0b9f22995"
      },
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "mode": "active",
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      }
    }
  ]
}
```

如果使用者未同意存取其個人檔案資訊，則 webhook 中不會包含使用者 ID。詳情請參閱 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。

### Get user IDs of all of your friends 

您可以透過 [Get a list of users who added your LINE Official Account as a friend](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids) 端點，取得所有將您的 LINE 官方帳號加為好友的使用者的使用者 ID。

<!-- note start -->

**Note**

此功能僅供已認證帳號（verified account）或[進階帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)使用。如需帳號類型的詳情，請參閱 LINE for Business 上的 [Account Types of LINE Official Account](https://www.linebiz.com/jp-en/service/line-official-account/account-type/)。

<!-- note end -->

### Get all user IDs of group and multi-person chat members 

您可以使用以下端點，取得您的 LINE 官方帳號所參與的群組或多人聊天室中所有成員的使用者 ID：

- [Get group chat member user IDs](https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids)
- [Get multi-person chat member user IDs](https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids)

<!-- note start -->

**Note**

此功能僅供已認證帳號（verified account）或[進階帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)使用。如需帳號類型的詳情，請參閱 LINE for Business 上的 [Account Types of LINE Official Account](https://www.linebiz.com/jp-en/service/line-official-account/account-type/)。

<!-- note end -->

<!-- tip start -->

**您也可以從 webhook 取得使用者 ID**

當使用者加入群組或多人聊天室，或在其中傳送訊息時，webhook 會被傳送到 bot 伺服器。該 webhook 中包含使用者 ID，因此您無需發出 API 請求即可取得使用者 ID。詳情請參閱 [從 webhook 取得使用者 ID](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-user-ids-in-webhook)。

<!-- tip end -->

## User ID validation 

即使您持有使用者 ID，若該使用者 ID 無效，仍無法傳送訊息。

若要檢查使用者 ID 是否有效，請使用 [Get profile](https://developers.line.biz/en/reference/messaging-api/#get-profile) 端點。如果使用者 ID 有效，會回傳 HTTP 狀態碼 `200`。如果回傳的不是 `200`，表示該使用者 ID 無效，您無法向此使用者傳送訊息。
