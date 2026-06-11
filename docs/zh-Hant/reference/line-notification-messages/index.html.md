# LINE 通知訊息 API 參考文件（LINE notification messages API reference）

<!-- note start -->

**使用選用功能需要提出申請**

只有已提交必要申請的企業用戶才能使用本文件所述的功能。若要在您的 LINE 官方帳號中使用這些功能，請聯絡您的業務代表，或聯絡[我們的銷售合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

<!-- table of contents -->

## Common specifications 

### Status codes 

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes)。

### Response headers 

LINE 通知訊息 API 的回應中包含以下 HTTP 標頭：

| Response header   | 說明                                   |
| ----------------- | --------------------------------------------- |
| x-line-request-id | 請求 ID。每個請求都會發放一個 ID。 |

## LINE notification messages (template) 

- [Send a LINE notification message (template)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template)
- [Get number of sent LINE notification messages (template)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-template)

### Send a LINE notification message (template) 

透過指定用戶的電話號碼來發送 LINE 通知訊息（template）的 API。

詳情請參閱 LINE 通知訊息文件中的 [LINE notification messages (template)](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/)。

<!-- warning start -->

**請勿限制請求來源 IP 位址**

發送 LINE 通知訊息時，請勿在 Messaging API 頻道的 [**Security Settings**] 分頁中註冊可呼叫 LINE Platform API 的伺服器 IP 位址。在限制來源 IP 位址的情況下發送 LINE 通知訊息可能導致發送失敗。

關於如何確認您是否限制了請求的 IP 位址，詳情請參閱 Messaging API 文件中的 [Restrict who can call the API when using a long-lived channel access token (optional)](https://developers.line.biz/en/docs/messaging-api/building-bot/#configure-security-settings)。

<!-- warning end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/pnp/templated/push \
-H 'Authorization: Bearer {channel_access_token}' \
-H 'Content-Type:application/json' \
-H 'X-Line-Delivery-Tag:15034552939884E28681A7D668CEA94C147C716C0EC9DFE8B80B44EF3B57F6BD0602366BC3menu01' \
-d '{
    "to": "c9fb9ae95bff879cbcdfc9edf6716640bc40841f3b7352140daa1431af4c319e",
    "templateKey": "shipment_completed_ja",
    "body": {
        "emphasizedItem": {
            "itemKey": "date_002_ja",
            "content": "Saturday, August 10, 2024"
        },
        "items": [
            {
                "itemKey": "time_range_001_ja",
                "content": "A.M."
            },
            {
                "itemKey": "number_001_ja",
                "content": "1234567"
            },
            {
                "itemKey": "price_001_ja",
                "content": "120 USD"
            },
            {
                "itemKey": "name_010_ja",
                "content": "Frozen Soup Set"
            }
        ],
        "buttons": [
            {
                "buttonKey": "check_delivery_status_ja",
                "url": "https://example.com/CheckDeliveryStatus/"
            },
            {
                "buttonKey": "contact_ja",
                "url": "https://example.com/ContactUs/"
            }
        ]
    }
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/bot/message/pnp/templated/push`

#### Rate limit 

每秒 2,000 次請求

#### Request headers 

<!-- note start -->

**不支援的功能**

LINE 通知訊息 API 不允許使用[重試金鑰（retry keys）](https://developers.line.biz/en/reference/messaging-api/#retry-api-request)（`X-Line-Retry-Key`）來重試 API 請求。

<!-- note end -->

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

X-Line-Delivery-Tag

透過 Webhook 在[發送完成事件（delivery completion event）](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event)的 `delivery.data` 屬性中回傳的字串。詳情請參閱 [Get message delivery notifications](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#receive-delivery-event)。\
最少字元數：16\
最多字元數：100

<!-- parameter end -->

_Example X-Line-Delivery-Tag_

<!-- tab start `shell` -->

```sh
15034552939884E28681A7D668CEA94C147C716C0EC9DFE8B80B44EF3B57F6BD0602366BC3menu01
```

<!-- tab end -->

#### Request body 

<!-- parameter start (props: required) -->

to

String

訊息發送目標。指定一個已正規化為 [E.164](https://developers.line.biz/en/glossary/#e164) 格式並[以 SHA256 雜湊](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#phone-number-hashed)的電話號碼。

關於發送訊息的條件，詳情請參閱 [Conditions for sending LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#conditions-for-sending-line-notification-messages)。

<!-- note start -->

**注意**

- 您無法指定[群組聊天或多人聊天](https://developers.line.biz/en/docs/messaging-api/group-chats/#group-chat-types)。
- 您無法指定多個電話號碼作為發送目標。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: required) -->

templateKey

String

指定您要發送的範本的 `Key`。

可用的 `Key` 請參閱 [Templates](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/#templates)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

body

Object

您要發送的範本的 body 物件。以三個物件指定訊息的內容。您不能在單一訊息中多次指定同一個項目。

- `emphasizedItem`：要強調的[項目（item）](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-items)。
- `items`：[項目（items）](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-items)的陣列。
- `buttons`：[按鈕（buttons）](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-buttons)的陣列。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

body.emphasizedItem

Object

指定您要在訊息中強調的[項目（item）](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-items)。\
物件數量上限：1

<!-- parameter end -->
<!-- parameter start (props: optional) -->

body.items

Array of objects

指定您要包含在訊息中的[項目（items）](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-items)陣列。 \
物件數量下限：0\
物件數量上限：15

<!-- parameter end -->
<!-- parameter start (props: optional) -->

body.buttons

Array of objects

指定您要包含在訊息中的[按鈕（buttons）](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template-buttons)陣列。 \
物件數量下限：0\
物件數量上限：2

<!-- parameter end -->

##### Items 

<!-- parameter start (props: required) -->

itemKey

String

指定您要包含的項目的 `Key`。

可用的 `Key` 請參閱 [Items](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/#items)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

content

String

指定要作為項目值顯示的字串。\
字元數上限：`body.emphasizedItem` 為 15，`body.items` 為 300

<!-- parameter end -->

_Example item_

<!-- tab start `json` -->

```json
{
  "itemKey": "time_range_001_ja",
  "content": "A.M."
}
```

<!-- tab end -->

##### Buttons 

<!-- parameter start (props: required) -->

buttonKey

String

指定您要包含的按鈕的 `Key`。

可用的 `Key` 請參閱 [Buttons](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/#buttons)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

url

String

指定當用戶按下按鈕時要開啟的頁面 URL。\
字元數上限：1000

<!-- parameter end -->

_Example button_

<!-- tab start `json` -->

```json
{
  "buttonKey": "contact_ja",
  "url": "https://example.com/ContactUs/"
}
```

<!-- tab end -->

#### Response 

回傳狀態碼 `202` 及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code | 說明 |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的訊息發送目標。</li><li>指定了無效的訊息物件。</li><li>您的 LINE 官方帳號無法使用指定的範本。</li></ul> |
| `403` | 無權使用此端點。 |
| `422` | 使用 LINE 通知訊息 API 發送 LINE 通知訊息失敗。可能的原因如下：<ul><li>沒有與指定為發送目標的電話號碼關聯的 LINE 用戶。</li><li>指定為訊息發送目標的電話號碼並非在 LINE 通知訊息服務目標國家發放。詳情請參閱 [Conditions for sending LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#conditions-for-sending-line-notification-messages)。</li><li>與指定為訊息發送目標的電話號碼關聯的 LINE 用戶已[拒絕接收 LINE 通知訊息](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#how-to-consent-for-line-notification-messages)。</li><li>與指定為訊息發送目標的電話號碼關聯的 LINE 用戶尚未同意 LINE 的隱私權政策（2022 年 3 月或之後修訂的版本）。</li></ul> |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 及 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a template that doesn't exist or that you aren't authorized to use (400 Bad Request)
{
  "message": "Invalid templateKey: reserve_004",
  "details": [
    {
      "message": "The specified template doesn't exist, or you don't have the permission",
      "property": "templateKey"
    }
  ]
}

// If you specify a non-existent item (400 Bad Request)
{
  "message": "The request body has 1 invalid key(s).",
  "details": [
    {
      "message": "The specified item key does not exist: datetime_000",
      "property": "body.items[0].itemKey"
    }
  ]
}

// If you specify the duplicate items (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Duplicate itemKey in items or between emphasizedItem and items are not allowed: date_002_ja",
      "property": "body.emphasizedItem.itemKey"
    }
  ]
}

// If you specify an invalid message destination (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "The value must be a valid SHA-256 digest.",
      "property": "to"
    }
  ]
}

// If you don't have permission to send LINE notification messages (template) (403 Forbidden)
{
  "message": "Access to this API is not available for your account"
}

// If sending a LINE notification message fails (422 Unprocessable Entity)
{
  "message": "Failed to send messages"
}
```

<!-- tab end -->

### Get number of sent LINE notification messages (template) 

取得使用 [Send a LINE notification message (template)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template) 端點發送的 LINE 通知訊息（template）數量。

詳情請參閱 LINE 通知訊息文件中的 [Get the number of sent LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#get-number-of-sent-line-notification-messages)。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/message/delivery/pnp/templated?date=20240916' \
-H 'Authorization: Bearer {channel_access_token}'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/v2/bot/message/delivery/pnp/templated`

#### Rate limit 

每秒 2,000 次請求

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameter 

<!-- parameter start (props: required) -->

date

訊息發送的日期

- 格式：`yyyyMMdd`（範例：`20240916`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含以下資訊的 JSON 物件。

<!-- parameter start -->

status

String

彙總處理狀態。以下其中之一：

- `ready`：您可以取得訊息數量。
- `unready`：`date` 中指定日期的訊息總數尚未完成統計。請稍後再次嘗試請求。彙總處理通常會在隔天完成。
- `out_of_service`：`date` 中指定的日期早於彙總系統開始運作的日期（2018 年 3 月 31 日）。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

success

Number

在 `date` 中指定的日期使用 LINE 通知訊息 API 發送的訊息數量。只有當 `status` 的值為 `ready` 時，才會包含在回應中。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "status": "ready",
  "success": 3
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code | 說明 |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的日期。</li><li>未指定日期。</li></ul> |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 及 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid date (400 Bad Request)
{
  "message": "The value for the 'date' parameter is invalid"
}
```

<!-- tab end -->

## LINE notification messages (flexible) 

- [Send a LINE notification message (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-flexible)
- [Get number of sent LINE notification messages (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-flexible)

### Send a LINE notification message (flexible) 

透過指定用戶的電話號碼來發送 LINE 通知訊息（flexible）的 API。

<!-- tip start -->

**既有的「LINE notification messages」名稱已變更為「LINE notification messages (flexible)」**

新增了一項名為「LINE notification messages (template)」的功能，讓您可以透過組合預製範本、項目等方式輕鬆建立訊息。

因此，先前需要 UX 審查的「LINE notification messages」已更名為「LINE notification messages (flexible)」。

詳情請參閱 2025 年 6 月 2 日發布給企業客戶的公告 [LINE notification messages (template) now available](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20250602)。

<!-- tip end -->

<!-- warning start -->

**請勿限制請求來源 IP 位址**

發送 LINE 通知訊息時，請勿在 Messaging API 頻道的 [**Security Settings**] 分頁中註冊可呼叫 LINE Platform API 的伺服器 IP 位址。在限制來源 IP 位址的情況下發送 LINE 通知訊息可能導致發送失敗。

關於如何確認您是否限制了請求的 IP 位址，詳情請參閱 Messaging API 文件中的 [Restrict who can call the API when using a long-lived channel access token (optional)](https://developers.line.biz/en/docs/messaging-api/building-bot/#configure-security-settings)。

<!-- warning end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/bot/pnp/push \
-H 'Authorization: Bearer {channel_access_token}' \
-H 'Content-Type:application/json' \
-d '{
    "to": "{hashed_phone_number}",
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

#Example request (with X-Line-Delivery-Tag)
curl -v -X POST https://api.line.me/bot/pnp/push \
-H 'Authorization: Bearer {channel_access_token}' \
-H 'Content-Type:application/json' \
-H 'X-Line-Delivery-Tag:{delivery_tag}' \
-d '{
    "to": "{hashed_phone_number}",
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

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/bot/pnp/push`

#### Rate limit 

每秒 2,000 次請求

#### Request header 

<!-- note start -->

**不支援的功能**

LINE 通知訊息 API 不允許使用[重試金鑰（retry keys）](https://developers.line.biz/en/reference/messaging-api/#retry-api-request)（`X-Line-Retry-Key`）來重試 API 請求。

<!-- note end -->

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

X-Line-Delivery-Tag

透過 Webhook 在[發送完成事件（delivery completion event）](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event)的 `delivery.data` 屬性中回傳的字串。詳情請參閱 [Get message delivery notifications](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#receive-delivery-event)。\
最少字元數：16\
最多字元數：100

<!-- parameter end -->

_Example X-Line-Delivery-Tag_

<!-- tab start `shell` -->

```sh
15034552939884E28681A7D668CEA94C147C716C0EC9DFE8B80B44EF3B57F6BD0602366BC3menu01
```

<!-- tab end -->

#### Request body 

<!-- parameter start (props: required) -->

to

String

訊息發送目標。指定一個已正規化為 [E.164](https://developers.line.biz/en/glossary/#e164) 格式並[以 SHA256 雜湊](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#phone-number-hashed)的電話號碼。

關於發送訊息的條件，詳情請參閱 [Conditions for sending LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#conditions-for-sending-line-notification-messages)。

<!-- note start -->

**注意**

- 您無法指定[群組聊天及多人聊天](https://developers.line.biz/en/docs/messaging-api/group-chats/#group-chat-types)。
- 您無法指定多個電話號碼作為發送目標。

<!-- note end -->

<!-- parameter end -->

<!-- parameter start (props: required) -->

messages

[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)陣列

要發送的訊息。上限：5

詳情請參閱 [Message types that can be sent in LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#message-types-that-can-be-sent)。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code | 說明 |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的訊息發送目標。</li><li>指定了無效的訊息物件。</li></ul> |
| `422` | 使用 LINE 通知訊息 API 發送 LINE 通知訊息失敗。可能的原因如下：<ul><li>沒有與指定為發送目標的電話號碼關聯的 LINE 用戶。</li><li>指定為訊息發送目標的電話號碼並非在 LINE 通知訊息服務目標國家發放。詳情請參閱 [Conditions for sending LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#conditions-for-sending-line-notification-messages)。</li><li>與指定為訊息發送目標的電話號碼關聯的 LINE 用戶已[拒絕接收 LINE 通知訊息](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#how-to-consent-for-line-notification-messages)。</li><li>與指定為訊息發送目標的電話號碼關聯的 LINE 用戶尚未同意 LINE 的隱私權政策（2022 年 3 月或之後修訂的版本）。</li></ul> |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 及 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid message destination (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "The value must be a valid SHA-256 digest.",
      "property": "to"
    }
  ]
}

// When sending a LINE notification message fails (422 Unprocessable Entity)
{
  "message": "Failed to send messages"
}
```

<!-- tab end -->

### Get number of sent LINE notification messages (flexible) 

取得使用 [Send a LINE notification message (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-flexible) 端點發送的 LINE 通知訊息（flexible）數量。

詳情請參閱 LINE 通知訊息文件中的 [Get the number of sent LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#get-number-of-sent-line-notification-messages)。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/message/delivery/pnp?date=20211231' \
-H 'Authorization: Bearer {channel_access_token}'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/v2/bot/message/delivery/pnp`

#### Rate limit 

每秒 2,000 次請求

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameter 

<!-- parameter start (props: required) -->

date

訊息發送的日期

- 格式：`yyyyMMdd`（範例：`20211231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含以下資訊的 JSON 物件。

<!-- parameter start -->

status

String

彙總處理狀態。以下其中之一：

- `ready`：您可以取得訊息數量。
- `unready`：`date` 中指定日期的訊息總數尚未完成統計。請稍後再次嘗試請求。彙總處理通常會在隔天完成。
- `out_of_service`：`date` 中指定的日期早於彙總系統開始運作的日期（2018 年 3 月 31 日）。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

success

Number

在 `date` 中指定的日期使用 LINE 通知訊息 API 發送的訊息數量。只有當 `status` 的值為 `ready` 時，才會包含在回應中。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "status": "ready",
  "success": 3
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼及錯誤回應：

| Code | 說明 |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的日期。</li><li>未指定日期。</li></ul> |

詳情請參閱 Messaging API 參考文件中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 及 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid date (400 Bad Request)
{
  "message": "The value for the 'date' parameter is invalid"
}
```

<!-- tab end -->
