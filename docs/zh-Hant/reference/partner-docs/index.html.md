# 企業客戶選用功能 API 參考文件（Options for corporate customers API reference）

<!-- note start -->

**使用選用功能需要提出申請**

只有提交所需申請的企業使用者，才能使用本文件所述的功能。若要在您的 LINE 官方帳號（LINE Official Account）上使用這些功能，請聯絡您的業務負責窗口，或聯絡[我們的銷售夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

<!-- table of contents -->

## Common specifications 

### Status codes 

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes)。

### Response headers 

企業客戶選用功能 API 的回應中會包含以下 HTTP 標頭：

| Response header   | Description                                   |
| ----------------- | --------------------------------------------- |
| x-line-request-id | 請求 ID。每個請求都會核發一個 ID。 |

## Mission Sticker API 

任務貼圖（Mission sticker）會在使用者完成特定目標後提供給使用者。以貼圖作為誘因，鼓勵使用者「綁定 ID 資訊」、「註冊成為會員」或「回答問卷」。

### Provide mission stickers to the users 

授予已完成特定目標的使用者下載您的任務貼圖的權限。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/shop/v3/mission \
-H "Content-Type: application/json" \
-H "Authorization: Bearer {channel access token}" \
-d '{
    "to": "U4af4980629...",
    "productType": "STICKER",
    "productId": "0000",
    "sendPresentMessage": false
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/shop/v3/mission`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

to

String

要授予下載權限的使用者的 User ID

<!-- parameter end -->
<!-- parameter start (props: required) -->

productType

String

`STICKER`

<!-- parameter end -->
<!-- parameter start (props: required) -->

productId

String

一組貼圖的 Package ID

<!-- parameter end -->
<!-- parameter start (props: required) -->

sendPresentMessage

Boolean

`false`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及空白的回應主體。

#### Error response 

發生錯誤時，回應主體會回傳對應錯誤的 HTTP 狀態碼及這筆 JSON 資料。

<!-- parameter start -->

message

String

包含錯誤資訊的訊息。詳情請參閱 [Error messages](https://developers.line.biz/en/reference/partner-docs/#send-mission-stickers-v3-error-messages)。

<!-- parameter end -->

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "invalid request"
}
```

<!-- tab end -->

##### Error messages 

主要錯誤的 HTTP 狀態碼，以及位於 JSON 資料 `message` 屬性中的錯誤訊息如下：

| Code | Message | Description |
| --- | --- | --- |
| `400` | invalid request | `to` 所指定的目標 User ID 無效。 |
| `400` | illegal argument | `productId` 所指定的貼圖組未設定為任務貼圖。 |
| `400` | not in sales period | `productId` 所指定的貼圖組已超出有效期間。 |
| `400` | sticker set not available for channel | 該頻道沒有使用 `productId` 所指定貼圖組的權限。 |
| `400` | not available | 因以下其中一項原因而無法授予貼圖：<ul><li>`productId` 所指定的貼圖組無法在 `to` 所指定目標使用者所在的國家或地區購買。</li><li>`to` 所指定目標使用者的裝置不支援 `productId` 所指定的貼圖組。</li><li>`to` 所指定目標使用者所使用的 LINE 應用程式版本不支援 `productId` 所指定的貼圖組。</li></ul> |
| `403` | not allowed to use the API | 該頻道未被授予 Mission Sticker API 所需的權限。 |
| `404` | not found | `productId` 所指定的貼圖組不存在。 |
| `500` | internal error | 發生內部伺服器錯誤。請稍候片刻後再試一次。 |
| `502` | upstream error | 發生內部網路錯誤。請稍候片刻後再試一次。 |

## Mark as read API (old) 

### Mark messages from users as read 

可將特定使用者所傳送的所有訊息顯示為「已讀」。

<!-- tip start -->

**請使用新的端點來標記為已讀**

Mark as read API（old）仍可繼續使用。不過，若您今後要實作將使用者訊息標記為已讀的功能，請使用 Messaging API 的 [Mark messages as read](https://developers.line.biz/en/reference/messaging-api/#mark-as-read) 端點。「Mark messages as read」端點無需申請，且可搭配聊天（chat）功能一起使用。

<!-- tip end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/markAsRead \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel_access_token}' \
-d '{
    "chat": {
        "userId": "Uxxxxxxxxxxxxxxxxxx"
    }
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/bot/message/markAsRead`

#### Rate limit 

每秒 2,000 次請求

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

chat.userId

String

目標 User ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code  | Description                      |
| ----- | -------------------------------- |
| `400` | 指定了無效的 User ID。 |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The property, 'chat.chatId', in the request body is invalid (line: -, column: -)"
}
```

<!-- tab end -->

## Module 

### Attach by operation of the module channel provider 

將模組頻道（module channel）連結（attach）到 LINE 官方帳號。為了進行連結，您必須向 LINE 官方帳號的管理員請求授權，並取得授權碼（authorization code）。如需模組授權流程的詳細資訊，請參閱模組文件中的 [Attach Module Channel](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/)。

使用此 API 時，您需要透過 `Authorization` 標頭或請求主體來指定模組頻道的 channel ID 與 channel secret。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://manager.line.biz/module/auth/v1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=1234567890abcde' \
--data-urlencode 'redirect_uri=https://example.com/auth?key=value' \
-d 'code_verifier=ayjtZgTunh96nHCvgLEiXzqVQOOC0SwMRs39bh1l5dx' \
-d 'client_id=1234567890' \
-d 'client_secret=1234567890abcdefghij1234567890ab' \
-d 'region=JP' \
-d 'basic_search_id=@linedevelopers' \
-d 'scope=message%3Asend%20message%3Areceive' \
-d 'brand_type=premium'
```

<!-- tab end -->

#### HTTP request 

`POST https://manager.line.biz/module/auth/v1/token`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

`application/x-www-form-urlencoded`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

Authorization

`Basic {base64({Channel ID}:{Channel Secret})}`

`{base64({Channel ID}:{Channel Secret})}` 的部分，請指定將「Module Channel ID」與「Module Channel Secret」以 `:` 串接後進行 Base64 編碼的字串。您可以在 [LINE Developers Console](https://developers.line.biz/console/) 中找到模組頻道的 channel ID 與 channel secret。

您可以使用此標頭來指定模組頻道的 channel ID 與 channel secret，以取代在請求主體中使用 `client_id` 與 `client_secret`。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

grant_type

String

`authorization_code`

<!-- parameter end -->
<!-- parameter start (props: required) -->

code

String

從 LINE Platform 收到的[授權碼（Authorization code）](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#receive-authorization-code)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

redirect_uri

String

請指定您在[認證與授權 URL](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin-query-parameters) 中所指定的 `redirect_uri`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

code_verifier

String

當使用 OAuth 2.0 擴充規格中所定義的 PKCE（Proof Key for Code Exchange，授權碼驗證金鑰）作為防範授權碼攔截攻擊的對策時指定。

符合 [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

client_id

String

您可以使用此參數來指定模組頻道的 channel ID，以取代使用 `Authorization` 標頭。您可以在 [LINE Developers Console](https://developers.line.biz/console/) 中找到模組頻道的 channel ID。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

client_secret

String

您可以使用此參數來指定模組頻道的 channel secret，以取代使用 `Authorization` 標頭。您可以在 [LINE Developers Console](https://developers.line.biz/console/) 中找到模組頻道的 channel secret。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

region

String

若您在[認證與授權 URL](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin-query-parameters) 中為 `region` 指定了值，請指定相同的值。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

basic_search_id

String

若您在認證與授權 URL 中為 `basic_search_id` 指定了值，請指定相同的值。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

scope

String

若您在認證與授權 URL 中為 `scope` 指定了值，請指定相同的值。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

brand_type

String

若您在認證與授權 URL 中為 `brand_type` 指定了值，請指定相同的值。

<!-- parameter end -->

#### Response 

成功時回傳一個帶有狀態碼 `200` 及此資訊的 JSON 物件。

<!-- parameter start -->

bot_id

String

LINE 官方帳號上 bot 的 User ID。

bot 的 user ID 會在呼叫 [Messaging API](https://developers.line.biz/en/reference/messaging-api/) 或 [Acquire Control API](https://developers.line.biz/en/reference/partner-docs/#acquire-control-api) 時使用。

<!-- note start -->

**注意**

bot 的 user ID 並非 Messaging API 頻道於 [LINE Developers Console](https://developers.line.biz/console/) **Basic Settings** 分頁上所顯示的 **Your user ID**。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start -->

scope

String

由 LINE 官方帳號管理員所授予的權限（scope）。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "bot_id": "U45c5c51f0050ef0f0ee7261d57fd3c56",
  "scopes": [
    "message:send",
    "message:receive"
  ]
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼：

- `400 Bad Request`
- `403 Forbidden`

### Unlink (detach) the module channel by the operation of the module channel administrator 

由模組頻道管理員呼叫 Detach API，將模組頻道從 LINE 官方帳號解除連結（detach）。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/channel/detach \
-H 'Content-Type:application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{"botId":"U45c5c51f0050ef0f0ee7261d57fd3c56"}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/bot/channel/detach`

#### Rate limit 

每秒 2,000 次請求

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

`Bearer {channel access token}`

`{channel access token}` 的部分，請指定您模組頻道的頻道存取權杖（channel access token）。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

botId

String

連結到模組頻道的 LINE 官方帳號 bot 的 user ID。

您可以從 [Attach by operation of the module channel provider](https://developers.line.biz/en/reference/partner-docs/#link-attach-by-operation-module-channel-provider) 的回應或 [Attached event](https://developers.line.biz/en/reference/partner-docs/#attached-event) 取得 bot 的 user ID。

<!-- parameter end -->

#### Response 

成功時回傳 `200` 狀態碼。

#### Error Response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法解除連結（detach）模組頻道。可能的原因如下：<ul><li>指定了無效的 LINE 官方帳號 bot user ID。</li><li>指定了不存在的 LINE 官方帳號 bot。</li><li>模組頻道未連結（attach）。</li><li>為非模組頻道指定了頻道存取權杖。</li></ul> |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID of the LINE Official Account bot (400 Bad Request)
{
  "message": "user/group/room Id is not available."
}

// If the module channel isn't linked (attached) (400 Bad Request)
{
  "message": "Specified channel is not detachable"
}
```

<!-- tab end -->

### Acquire Control API 

若待命頻道（Standby Channel）想要取得主導權（Chat Control），則呼叫 Acquire Control API。

先前為主動頻道（Active Channel）的頻道將自動切換為待命頻道（Standby Channel）。

<!-- warning start -->

**警告**

在目前提供的模組架構中，無需呼叫此 API。因此，此 API 的實作為選用。

此 API 目前僅在因非預期問題而切換聊天主導權時使用。

<!-- warning end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/chat/{chatId}/control/acquire \
-H 'Content-Type:application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'Header specifying the bot user ID:xxxxxx' \
-d '{"expired":true,"ttl":3600}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/bot/chat/{chatId}/control/acquire`

#### Rate limit 

每秒 2,000 次請求

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

`Bearer {channel access token}`

`{channel access token}` 的部分，請指定您模組頻道的頻道存取權杖（channel access token）。

<!-- parameter end -->
<!-- parameter start (props: required) -->

指定 bot user ID 的標頭

連結到模組頻道的 LINE 官方帳號 bot 的 user ID。

您可以從 [Attach by operation of the module channel provider](https://developers.line.biz/en/reference/partner-docs/#link-attach-by-operation-module-channel-provider) 的回應或 [Attached event](https://developers.line.biz/en/reference/partner-docs/#attached-event) 取得 bot 的 user ID。

<!-- note start -->

**此特定標頭將於加入後提供**

此標頭的名稱（參數名稱）僅向參加 [LINE Marketplace](https://line-marketplace.com/jp/inquiry)（僅提供日文）的客戶公開。

<!-- note end -->

<!-- parameter end -->

#### Path parameter 

<!-- parameter start (props: required) -->

chatId

`userId`、`roomId` 或 `groupId`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: optional) -->

expired

Boolean

- `True`：經過時間限制（ttl）後，主導權（Chat Control）將回到主要頻道（Primary Channel）。（預設）
- `False`：沒有時間限制，主導權（Chat Control）不會隨時間改變。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

ttl

Number

主導權（Chat Control）回到主要頻道（Primary Channel）所需的時間（即模組頻道維持為主動頻道（Active Channel）的時間）。此值以秒為單位指定。最大值為一年（3600 \* 24 \* 365）。預設值為 `3600`（1 小時）。

\* 若 `expired` 的值為 `false` 則會被忽略。

<!-- parameter end -->

#### Response 

成功時回傳 200 狀態碼。

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | `chatId` 參數中指定了無效的 ID。 |
| `404` | 無法取得主導權（Chat Control）。可能的原因如下：<ul><li>指定了尚未將連結到模組的 LINE 官方帳號加為好友的使用者。</li><li>指定了連結到模組的 LINE 官方帳號未參與的群組。</li><li>指定了連結到模組的 LINE 官方帳號未參與的多人聊天室。</li></ul> |
| `423` | 另一個頻道已在一定時間內（約數秒）取得主導權（Chat Control）。 |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specfy an invalid ID is specified in the chatId parameter (400 Bad Request)
{
  "message": "The value for the 'chatId' parameter is invalid"
}
```

<!-- tab end -->

### Release Control API 

若要將主動頻道（Active Channel）的主導權（Chat Control）交還給主要頻道（Primary Channel），請呼叫 Release Control API。

<!-- warning start -->

**警告**

在目前提供的模組架構中，無需呼叫此 API。因此，此 API 的實作為選用。

此 API 目前僅在因非預期問題而切換聊天主導權時使用。

<!-- warning end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/chat/{chatId}/control/release \
-H 'Content-Type:application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'Header specifying the bot user ID:xxxxxx'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/bot/chat/{chatId}/control/release`

#### Rate limit 

每秒 2,000 次請求

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

`Bearer {channel access token}`

`{channel access token}` 的部分，請指定您模組頻道的頻道存取權杖（channel access token）。

<!-- parameter end -->
<!-- parameter start (props: required) -->

指定 bot user ID 的標頭

連結到模組頻道的 LINE 官方帳號 bot 的 user ID。

您可以從 [Attach by operation of the module channel provider](https://developers.line.biz/en/reference/partner-docs/#link-attach-by-operation-module-channel-provider) 的回應或 [Attached event](https://developers.line.biz/en/reference/partner-docs/#attached-event) 取得 bot 的 user ID。

<!-- note start -->

**此特定標頭將於加入後提供**

此標頭的名稱（參數名稱）僅向參加 [LINE Marketplace](https://line-marketplace.com/jp/inquiry)（僅提供日文）的客戶公開。

<!-- note end -->

<!-- parameter end -->

#### Path parameter 

<!-- parameter start (props: required) -->

chatId

`userId`、`roomId` 或 `groupId`

<!-- parameter end -->

#### Response 

成功時回傳 `200` 狀態碼。

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code  | Description                                           |
| ----- | ----------------------------------------------------- |
| `400` | `chatId` 參數中指定了無效的 ID。 |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specfy an invalid ID is specified in the chatId parameter (400 Bad Request)
{
  "message": "The value for the 'chatId' parameter is invalid"
}
```

<!-- tab end -->

### Module channel-specific webhook events 

#### Attached event 

此事件表示模組頻道已連結（attach）到 LINE 官方帳號。會傳送到模組頻道的 Webhook URL 伺服器。

<!-- parameter start -->

timestamp 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

不過，`mode` 固定為 `active`。

<!-- parameter end -->
<!-- parameter start -->

type

String

`module`

<!-- parameter end -->
<!-- parameter start -->

module.type

String

`attached`

<!-- parameter end -->
<!-- parameter start -->

module.botId

String

已連結的 LINE 官方帳號上 bot 的 User ID

<!-- parameter end -->
<!-- parameter start -->

module.scopes

Array of strings

表示由 LINE 官方帳號管理員所許可之 scope 的字串陣列。

<!-- parameter end -->

_Attached event 範例_

<!-- tab start `json` -->

```sh
{
  "destination": "U53387d54817...",
  "events": [
    {
      "type": "module",
      "module": {
        "type": "attached",
        "botId": "U53387d54817...",
        "scopes": [
          "message:send",
          "message:receive"
        ]
      },
      "webhookEventId": "01G3GCEEXNWREGSSFVTPYH8465",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1653038594997,
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

#### Detached event 

此事件表示模組頻道已從 LINE 官方帳號解除連結（detach）。會傳送到模組頻道的 Webhook URL 伺服器。

<!-- note start -->

**刪除 LINE 官方帳號時不會進行解除連結（detach）**

當使用 LINE Official Account Manager 刪除 LINE 官方帳號時，並不會解除連結模組頻道。

在執行刪除帳號操作後經過三個月，且包含 LINE 官方帳號分析資料在內的所有資訊都已完全刪除後，該帳號才會自動被解除連結。

<!-- note end -->

<!-- parameter start -->

timestamp 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

不過，`mode` 固定為 `active`。

<!-- parameter end -->
<!-- parameter start -->

type

String

`module`

<!-- parameter end -->
<!-- parameter start -->

module.type

String

`detached`

<!-- parameter end -->
<!-- parameter start -->

module.botId

String

已解除連結的 LINE 官方帳號 bot user ID

<!-- parameter end -->
<!-- parameter start -->

module.reason

String

解除連結的原因

`bot_deleted`：包含 LINE 官方帳號分析資料在內的所有資訊都已完全刪除。

<!-- parameter end -->

_Detached event 範例_

<!-- tab start `json` -->

```sh
{
  "destination": "U5fac33f633e72c192759f09afc41fa28",
  "events": [
    {
      "type": "module",
      "module": {
        "type": "detached",
        "botId": "U5fac33f633e72c192759f09afc41fa28"
      },
      "webhookEventId": "01G4CPSV08QGNT1DWFC4DSWDNP",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1653988977672,
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

#### Activated event 

此事件表示模組頻道因呼叫 Acquire Control API 而切換為主動頻道（Active Channel）。會傳送到模組頻道的 Webhook URL 伺服器。

<!-- note start -->

**注意**

若 Acquire Control API 中所指定的有效期間已到期，並因此切換了主導權（Chat Control），則不會傳送 activated event。

<!-- note end -->

<!-- parameter start -->

timestamp 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

不過，`mode` 固定為 `active`。

<!-- parameter end -->
<!-- parameter start -->

type

String

`activated`

<!-- parameter end -->
<!-- parameter start -->

chatControl.expireAt

Number

維持「active」狀態的時間限制。

<!-- parameter end -->

_Activated event 範例_

<!-- tab start `json` -->

```sh
  {
  "destination": "U5fac33f633e72c192759f09afc41fa28",
  "events": [
    {
      "type": "activated",
      "chatControl": {
        "expireAt": 1653994422933
      },
      "webhookEventId": "01G4CRJ54J7TT4WN190KKHBXXT",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1653990823058,
      "source": {
        "type": "user",
        "userId": "LUb577ef3cbe..."
      },
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

#### Deactivated event 

此事件表示模組頻道因呼叫 Acquire Control API 或 Release Control API 而切換為待命頻道（Standby Channel）。會傳送到模組頻道的 Webhook URL 伺服器。

<!-- note start -->

**注意**

若 Acquire Control API 中所指定的有效期間已到期，並因此切換了主導權（Chat Control），則不會傳送 deactivated event。

<!-- note end -->

<!-- parameter start -->

timestamp 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

不過，`mode` 固定為 `active`。

<!-- parameter end -->
<!-- parameter start -->

type

String

`deactivated`

<!-- parameter end -->

_Deactivated event 範例_

<!-- tab start `json` -->

```sh
{
  "destination": "U5fac33f633e72c192759f09afc41fa28",
  "events": [
    {
      "type": "deactivated",
      "webhookEventId": "01G4CRJ51100K1D1791KC9J4G4",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1653990822945,
      "source": {
        "type": "user",
        "userId": "LUb577ef3cbe..."
      },
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

#### botSuspend event 

此事件表示 LINE 官方帳號已被暫停（Suspend）。會傳送到模組頻道的 Webhook URL 伺服器。

當您收到此事件時，建議您執行以下動作：

- 在模組頻道的管理畫面上顯示如「由於 LINE 官方帳號無法使用，此管理畫面無法使用」之類的訊息，並停止使用該管理畫面。
- 即使進入暫停狀態，仍可能從暫停狀態恢復（可能會收到 botResume event）。建議保留所有資訊。

<!-- note start -->

**注意**

botSuspend event 不會傳送到主要頻道（Primary Channel）。

若您在收到 botSuspend event 後又收到 Detached event，這表示 LINE 官方帳號已停止使用該模組頻道並取消了合約。

<!-- note end -->

<!-- parameter start -->

timestamp 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

不過，`mode` 固定為 `active`。

<!-- parameter end -->
<!-- parameter start -->

type

String

`botSuspended`

<!-- parameter end -->

_botSuspend event 範例_

<!-- tab start `json` -->

```sh
{
  "destination": "U53387d548170020e6cedef5f41d1e01d",
  "events": [
    {
      "type": "botSuspended",
      "webhookEventId": "01G4CRJ54J7TT4WN190KKHBXXT",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1616390574119,
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

#### botResumed event 

此事件表示 LINE 官方帳號已從暫停狀態恢復。會傳送到模組頻道的 Webhook URL 伺服器。

當您收到此事件時，建議您將模組頻道管理頁面上的「由於 LINE 官方帳號無法使用，此管理頁面無法使用」訊息隱藏，並恢復使用該管理頁面。

<!-- note start -->

**注意**

botResumed event 不會傳送到主要頻道（Primary Channel）。

<!-- note end -->

<!-- parameter start -->

timestamp 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

不過，`mode` 固定為 `active`。

<!-- parameter end -->
<!-- parameter start -->

type

String

`botResumed`

<!-- parameter end -->

_botResumed event 範例_

<!-- tab start `json` -->

```sh
{
  "destination": "U5fac33f633e72c192759f09afc41fa28",
  "events": [
    {
      "type": "botResumed",
      "webhookEventId": "01G4CS8T91R1V1JCE0G43DQND8",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1653991565601,
      "mode": "active"
    }
  ]
}
```

<!-- tab end -->

### Get a list of bots to which the module is attached 

取得已連結模組頻道的多個 LINE 官方帳號 bot 的基本資訊清單。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET "https://api.line.me/v2/bot/list?limit={limit}&start={continuationToken}" \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/v2/bot/list?limit={limit}&start={continuationToken}`

#### Rate limit 

每秒 2,000 次請求

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

`Bearer {channel access token}`

`{channel access token}` 的部分，請指定您模組頻道的頻道存取權杖（channel access token）。

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

limit

指定您要取得基本資訊的 bot 數量上限。預設值為 `100`。\
最大值：`100`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

start

回應所回傳之 JSON 物件 `next` 屬性中的延續權杖（continuation token）值。若您無法在一次請求中取得所有 bot 的基本資訊，請包含此參數以取得剩餘的陣列。

<!-- parameter end -->

#### Response 

成功時回傳一個帶有狀態碼 `200` 及此資訊的 JSON 物件。

<!-- parameter start -->

bots

Array

代表 bot 基本資訊的 Bot list Item 物件陣列。

<!-- parameter end -->
<!-- parameter start -->

bots\[].userId

String

Bot 的 user ID

<!-- parameter end -->
<!-- parameter start -->

bots\[].basicId

String

Bot 的 basic ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

bots\[].premiumId

String

Bot 的 [premium ID](https://developers.line.biz/en/glossary/#premium-id)。若未設定 premium ID，則回應中不會包含此項目。

<!-- parameter end -->
<!-- parameter start -->

bots\[].displayName

String

Bot 的顯示名稱

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

bots\[].pictureUrl

String

個人檔案圖片 URL。以「https://」開頭的圖片 URL。若 bot 沒有個人檔案圖片，則回應中不會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

延續權杖（Continuation token）。用於取得下一批 bot 基本資訊的陣列。只有在尚有未回傳的結果時，才會回傳此屬性。

延續權杖會在 24 小時（86,400 秒）後到期。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "bots": [
    {
      "userId": "Uf2dd6e8b081d2ff9c05c98a8a8b269c9",
      "basicId": "@628...",
      "displayName": "Test01",
      "pictureUrl": "https://profile.line-scdn.net/0hyxytJNAlJldEDQzlatVZAHhIKDoz..."
    },
    {
      "userId": "Ua831d37bfe8232808202b85127663f70",
      "basicId": "@076lu...",
      "displayName": "Test02",
      "pictureUrl": "https://profile.line-scdn.net/0hohnizdyzMEdTECbnVo9PEG9VPiok..."
    },
    {
      "userId": "Ub77ea431fba86f7c159a0c0f5be43d9f",
      "basicId": "@290n...",
      "displayName": "Test03"
    },
    {
      "userId": "Ub8ec80a14e879e9c6833fb4cee0e632b",
      "basicId": "@793j...",
      "displayName": "Test04"
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code  | Description                                 |
| ----- | ------------------------------------------- |
| `400` | 指定了無效的延續權杖（continuation token）。 |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid continuation token, such as expired (400 Bad Request)
{
  "message": "Invalid start param"
}
```

<!-- tab end -->
