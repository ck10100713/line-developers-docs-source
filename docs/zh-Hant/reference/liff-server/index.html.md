# Server API

<!-- tip start -->

**版本號碼與 LIFF SDK 不同**

server API 的版本號碼與 LIFF SDK 的版本號碼不同。目前發行的 LIFF SDK 版本為 `v2`，但 server API 的版本則為 `v1`。

<!-- tip end -->

## Server API 

### Preparing a channel access token 

LIFF server API 用於操作 LINE Login 頻道（channel）上的 LIFF apps。因此，為了使用 server API，需要 LINE Login 頻道的頻道存取權杖（channel access token）。可使用的頻道存取權杖類型為[短期頻道存取權杖（short-lived channel access tokens）](https://developers.line.biz/en/reference/messaging-api/#issue-shortlived-channel-access-token)或[無狀態頻道存取權杖（stateless channel access tokens）](https://developers.line.biz/en/reference/messaging-api/#issue-stateless-channel-access-token)。

### Adding the LIFF app to a channel 

將 LIFF app 加入頻道。一個頻道最多可加入 30 個 LIFF apps。

<!-- tip start -->

**我們建議將 LIFF app 建立為 LINE MINI App**

未來 LIFF 與 LINE MINI App 將整合為單一品牌。整合後，LIFF 將被併入 LINE MINI App。因此，我們建議您將新的 LIFF app 建立為 LINE MINI App。詳情請參閱 [2025 年 2 月 12 日](https://developers.line.biz/en/news/2025/02/12/line-mini-app/)的消息。

<!-- tip end -->

_Example_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/liff/v1/apps \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
    "view": {
        "type": "full",
        "url": "https://example.com/myservice"
    },
    "description": "Service Example",
    "features": {
        "qrCode": true
    },
    "permanentLinkPattern": "concat",
    "scope": ["profile", "chat_message.write"],
    "botPrompt": "none"
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/liff/v1/apps`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
詳情請參閱 [Preparing a channel access token](https://developers.line.biz/en/reference/liff-server/#preparing-channel-access-token)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

view.type

String

LIFF app 視圖（view）的大小。請指定下列其中一個值：

- `compact`
- `tall`
- `full`

詳情請參閱 [Size of the LIFF app view](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

view.url

String

端點（endpoint）URL。這是實作 LIFF app 的 web app 的 URL（例如 `https://example.com`）。在使用 LIFF URL 啟動 LIFF app 時使用。

URL scheme 必須為 **https**。不可指定 URL fragment（#URL-fragment）。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

view.moduleMode

Boolean

設為 `true` 即可在模組模式（modular mode）下使用 LIFF app。在模組模式下，標頭中的動作按鈕不會顯示。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

description

String

LIFF app 的名稱。

LIFF app 名稱不可包含「LINE」或類似的字串，或不適當的字串。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

features.qrCode

Boolean

設為 `true` 即可在 LIFF app 中使用 2D 條碼讀取器，否則設為 `false`。預設值為 `false`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

permanentLinkPattern

String

LIFF URL 中附加資訊的處理方式。請指定 `concat`。

詳情請參閱 LIFF 文件中的 [Opening a LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

scope

Array of strings

部分 LIFF SDK 方法運作時所需的 scope 陣列。

- `openid`
- `email`
- `profile`
- `chat_message.write`

預設值為 `["profile", "chat_message.write"]`。各 scope 的詳情請參閱 LIFF 文件中的 [Adding the LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

botPrompt

String

以下列其中一個值指定[加入好友選項（add friend option）](https://developers.line.biz/en/docs/line-login/link-a-bot/)的設定：

- `normal`：在頻道同意畫面中顯示將 LINE 官方帳號加為好友的選項。
- `aggressive`：在頻道同意畫面後顯示一個帶有將 LINE 官方帳號加為好友選項的畫面。
- `none`：不顯示將 LINE 官方帳號加為好友的選項。

預設值為 `none`。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與帶有下列屬性的 JSON 物件。

<!-- parameter start -->

liffId

String

LIFF app ID

<!-- parameter end -->

_Example_

<!-- tab start `json` -->

```json
{
  "liffId": "{liffId}"
}
```

<!-- tab end -->

#### Error response 

回傳下列其中一個狀態碼。

| Status code | Description |
| --- | --- |
| 400 | 此狀態碼表示下列其中一種情況：<ul><li>請求包含無效的值。</li><li>已達到該頻道可加入的 LIFF apps 最大數量。</li></ul> |
| 401 | 認證失敗。 |

### Update LIFF app settings 

部分更新 LIFF app 設定。

_Example_

<!-- tab start `shell` -->

```sh
curl -X PUT https://api.line.me/liff/v1/apps/{liffId} \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
    "view": {
        "url": "https://new.example.com"
    }
}'
```

<!-- tab end -->

#### HTTP request 

`PUT https://api.line.me/liff/v1/apps/{liffId}`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
詳情請參閱 [Preparing a channel access token](https://developers.line.biz/en/reference/liff-server/#preparing-channel-access-token)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

liffId

要更新的 LIFF app 的 ID

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: optional) -->

view.type

String

LIFF app 視圖（view）的大小。請指定下列其中一個值：

- `compact`
- `tall`
- `full`

詳情請參閱 [Size of the LIFF app view](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

view.url

String

端點（endpoint）URL。這是實作 LIFF app 的 web app 的 URL（例如 `https://example.com`）。在使用 LIFF URL 啟動 LIFF app 時使用。

URL scheme 必須為 **https**。不可指定 URL fragment（#URL-fragment）。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

view.moduleMode

Boolean

設為 `true` 即可在模組模式（modular mode）下使用 LIFF app。在模組模式下，標頭中的動作按鈕不會顯示。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

description

String

LIFF app 的名稱。

LIFF app 名稱不可包含「LINE」或類似的字串，或不適當的字串。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

features.qrCode

Boolean

設為 `true` 即可在 LIFF app 中使用 2D 條碼讀取器，否則設為 `false`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

permanentLinkPattern

String

LIFF URL 中附加資訊的處理方式。請指定 `concat`。

詳情請參閱 LIFF 文件中的 [Opening a LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

scope

Array of strings

部分 LIFF SDK 方法運作時所需的 scope 陣列。

- `openid`
- `email`
- `profile`
- `chat_message.write`

各 scope 的詳情請參閱 LIFF 文件中的 [Adding the LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

botPrompt

String

以下列其中一個值指定[加入好友選項（add friend option）](https://developers.line.biz/en/docs/line-login/link-a-bot/)的設定：

- `normal`：在頻道同意畫面中顯示將 LINE 官方帳號加為好友的選項。
- `aggressive`：在頻道同意畫面後顯示一個帶有將 LINE 官方帳號加為好友選項的畫面。
- `none`：不顯示將 LINE 官方帳號加為好友的選項。

<!-- parameter end -->

<!-- note start -->

**注意**

僅會更新 request body 中所指定的屬性。

<!-- note end -->

#### Response 

回傳狀態碼 `200`。

#### Error response 

回傳下列其中一個狀態碼。

| Status code | Description |
| --- | --- |
| 400 | 請求包含無效的值。 |
| 401 | 認證失敗。 |
| 404 | 此狀態碼表示下列其中一種情況：<ul><li>指定的 LIFF app 不存在。</li><li>指定的 LIFF app 已被加入另一個頻道。</li></ul> |

### Get all LIFF apps 

取得已加入該頻道的所有 LIFF apps 的資訊。

_Example_

<!-- tab start `shell` -->

```sh
curl -X GET https://api.line.me/liff/v1/apps \
-H "Authorization: Bearer {channel access token}"
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/liff/v1/apps`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
詳情請參閱 [Preparing a channel access token](https://developers.line.biz/en/reference/liff-server/#preparing-channel-access-token)。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與帶有下列屬性的 JSON 物件。

<!-- parameter start -->

apps

Array of objects

LIFF app 物件的陣列

<!-- parameter end -->
<!-- parameter start -->

apps\[].liffId

String

LIFF app ID

<!-- parameter end -->
<!-- parameter start -->

apps[].view.type

String

LIFF app 視圖（view）的大小。為下列其中一個值：

- `compact`
- `tall`
- `full`

詳情請參閱 [Size of the LIFF app view](https://developers.line.biz/en/docs/liff/overview/#screen-size)。

<!-- parameter end -->
<!-- parameter start -->

apps[].view.url

String

端點（endpoint）URL。這是實作 LIFF app 的 web app 的 URL（例如 `https://example.com`）。在使用 LIFF URL 啟動 LIFF app 時使用。

<!-- parameter end -->
<!-- parameter start -->

apps[].view.moduleMode

Boolean

設為 `true` 即可在模組模式（modular mode）下使用 LIFF app。在模組模式下，標頭中的動作按鈕不會顯示。

<!-- parameter end -->
<!-- parameter start -->

apps\[].description

String

LIFF app 的名稱

<!-- parameter end -->
<!-- parameter start -->

apps[].features.ble

Boolean

若 LIFF app 支援用於 LINE Things 的 Bluetooth® Low Energy 則為 `true`，否則為 `false`。

<!-- parameter end -->
<!-- parameter start -->

apps[].features.qrCode

Boolean

若可在 LIFF app 中啟動 2D 條碼讀取器則為 `true`，否則為 `false`。

<!-- parameter end -->
<!-- parameter start -->

apps\[].permanentLinkPattern

String

LIFF URL 中附加資訊的處理方式。回傳 `concat`。

詳情請參閱 LIFF 文件中的 [Opening a LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

<!-- parameter end -->
<!-- parameter start -->

apps\[].scope

Array of strings

LIFF app 的 scope。

- `openid`
- `email`
- `profile`
- `chat_message.write`

各 scope 的詳情請參閱 LIFF 文件中的 [Adding the LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

<!-- parameter end -->
<!-- parameter start -->

apps\[].botPrompt

String

[加入好友選項（add friend option）](https://developers.line.biz/en/docs/line-login/link-a-bot/)的設定。

- `normal`：在頻道同意畫面中顯示將 LINE 官方帳號加為好友的選項。
- `aggressive`：在頻道同意畫面後顯示一個帶有將 LINE 官方帳號加為好友選項的畫面。
- `none`：不顯示將 LINE 官方帳號加為好友的選項。

<!-- parameter end -->

_Example_

<!-- tab start `json` -->

```json
{
  "apps": [
    {
      "liffId": "{liffId}",
      "view": {
        "type": "full",
        "url": "https://example.com/myservice"
      },
      "description": "Happy New York",
      "permanentLinkPattern": "concat"
    },
    {
      "liffId": "{liffId}",
      "view": {
        "type": "tall",
        "url": "https://example.com/myservice2"
      },
      "features": {
        "ble": true,
        "qrCode": true
      },
      "permanentLinkPattern": "concat",
      "scope": ["profile", "chat_message.write"],
      "botPrompt": "none"
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列其中一個狀態碼。

| Status code | Description                          |
| ----------- | ------------------------------------ |
| 401         | 認證失敗。               |
| 404         | 該頻道上沒有任何 LIFF app。 |

### Delete LIFF app from a channel 

從頻道刪除 LIFF app。

_Example_

<!-- tab start `shell` -->

```sh
curl -X DELETE https://api.line.me/liff/v1/apps/{liffId} \
-H "Authorization: Bearer {channel access token}"
```

<!-- tab end -->

#### HTTP request 

`DELETE https://api.line.me/liff/v1/apps/{liffId}`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
詳情請參閱 [Preparing a channel access token](https://developers.line.biz/en/reference/liff-server/#preparing-channel-access-token)。

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

liffId

要刪除的 LIFF app 的 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200`。

#### Error response 

回傳下列其中一個狀態碼。

| Status code | Description |
| --- | --- |
| 401 | 認證失敗。 |
| 404 | 此狀態碼表示下列其中一種情況：<ul><li>指定的 LIFF app 不存在。</li><li>指定的 LIFF app 已被加入另一個頻道。</li></ul> |
