# LINE Login API v2.0 參考文件（LINE Login API v2.0 reference）

<!-- warning start -->

**LINE Login v2.0 已淘汰**

本頁面包含 LINE Login 舊版 v2.0 的說明文件。LINE Login v2.0 已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)，其[終止支援（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)日期尚未確定，因此我們建議您使用目前的版本（LINE Login v2.1）。終止支援公告與實際終止支援之間會有一段緩衝期。詳情請參閱 [LINE Login versions](https://developers.line.biz/en/docs/line-login/overview/#versions)。

<!-- warning end -->

## Common specifications

### Rate limits 

如果您在短時間內向 LINE Login API 發送大量請求，且判定會影響 LINE Platform 的運作，我們可能會暫時限制您的請求。請勿基於任何目的（包括負載測試）發送大量請求。

<!-- tip start -->

**關於速率限制門檻**

LINE Login API 的速率限制（rate limit）門檻並未公開。

<!-- tip end -->

### Status codes 

呼叫 API 後會回傳以下 HTTP 狀態碼。除非另有說明，否則我們遵循 [HTTP 狀態碼規範](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。

狀態碼 | 說明
---- | ----
200 OK | 請求成功
400 Bad Request | 請求有問題。請檢查請求參數與 JSON 格式。
401 Unauthorized | 請檢查授權標頭（authorization header）是否正確。
403 Forbidden | 未獲授權使用此 API。請確認您的帳號或方案是否已獲授權使用此 API。
413 Payload Too Large | 請求超過 2MB 的大小上限。請將請求縮小到 2MB 以下後再試一次。
429 Too Many Requests | 因大量請求超過[速率限制（rate-limit）](https://developers.line.biz/en/reference/line-login-v2/#rate-limits)而暫時限制請求。
500 Internal Server Error | API 伺服器的暫時性錯誤。

## OAuth

### Issue access token 

簽發存取權杖（access token）。

透過 LINE Login API 管理的存取權杖代表某個應用程式已獲准存取儲存在 LINE Platform 上的使用者資料（例如使用者 ID、顯示名稱、個人圖片與狀態消息）。

呼叫 LINE Login API 時，您必須提供先前回應中所傳送的存取權杖或重新整理權杖（refresh token）。

<!-- note start -->

**注意**

這是 LINE Login v2.0 端點（endpoint）的說明。關於 v2.1 端點的資訊，請參閱 v2.1 API 參考文件中的 [Issue access token](https://developers.line.biz/en/reference/line-login/#issue-access-token)。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/accessToken \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=b5fd32eacc791df' \
-d 'redirect_uri=https%3A%2F%2Fexample.com%2Fauth' \
-d 'client_id=12345' \
-d 'client_secret=d6524edacc8742aeedf98f'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/oauth/accessToken`

#### Request headers 

<!-- parameter start (props: required) -->
Content-Type

application/x-www-form-urlencoded

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

從 LINE Platform 收到的[授權碼（authorization code）](https://developers.line.biz/en/docs/line-login/integrate-line-login-v2/#receiving-the-authorization-code)

<!-- parameter end -->
<!-- parameter start (props: required) -->
redirect_uri
String

回呼網址（Callback URL）

<!-- parameter end -->
<!-- parameter start (props: required) -->
client_id
String

頻道 ID（Channel ID）。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->
<!-- parameter start (props: required) -->
client_secret
String

頻道密鑰（Channel secret）。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->

#### Response 

此 API 會回傳 `200` 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- parameter start -->
access_token
String

存取權杖。有效期間為 30 天。

<!-- parameter end -->
<!-- parameter start -->
expires_in
Number

存取權杖到期前的秒數。

<!-- parameter end -->
<!-- parameter start -->
refresh_token
String

用來取得新存取權杖的權杖（重新整理權杖）。在存取權杖到期後最多 10 天內有效。

詳情請參閱 [Refresh access token](https://developers.line.biz/en/reference/line-login-v2/#refresh-access-token)。

<!-- parameter end -->
<!-- parameter start -->
scope
String

授予該存取權杖的權限。

- `P`：您擁有存取使用者個人資料資訊的權限。

<!-- parameter end -->
<!-- parameter start -->
token_type
String

`Bearer`

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
    "access_token": "bNl4YEFPI/hjFWhTqexp4MuEw5YPs7qhr6dJDXKwNPuLka...",
    "expires_in": 2591977,
    "refresh_token": "8iFFRdyxNVNLWYeteMMJ",
    "scope": "P",
    "token_type": "Bearer"
}
```

<!-- tab end -->

### Verify access token validity 

驗證存取權杖是否有效。

關於如何使用存取權杖安全地處理使用者註冊與登入的一般建議，請參閱 LINE Login 說明文件中的 [Verify access tokens](https://developers.line.biz/en/docs/line-login/managing-access-tokens-v2/#verify-access-token)。

<!-- note start -->

**注意**

這是 LINE Login v2.0 端點的參考文件。關於 v2.1 端點的資訊，請參閱 LINE Login v2.1 API 參考文件中的 [Verify access token validity](https://developers.line.biz/en/reference/line-login/#verify-access-token)。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/verify \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'access_token=bNl4YEFPI/hjFWhTqexp4MuEw5YPs7qhr6dJDXKwNPuLka...'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/oauth/verify`

#### Request headers 

<!-- parameter start (props: required) -->
Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start -->
access_token
String

存取權杖

<!-- parameter end -->

#### Response 

如果存取權杖有效，會回傳 `200 OK` 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- parameter start -->
scope
String

授予該存取權杖的權限。

- `P`：您擁有存取使用者個人資料資訊的權限。

<!-- parameter end -->
<!-- parameter start -->
client_id
String

簽發該存取權杖的頻道 ID。

<!-- parameter end -->
<!-- parameter start -->
expires_in
Number

存取權杖到期前的秒數。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
   "scope":"P",
   "client_id":"1350031035",
   "expires_in":2591965
}
```

<!-- tab end -->

#### Error response 

如果存取權杖已過期，會回傳 `400 Bad Request` 狀態碼，以及一個 JSON 物件。

_Example error response_

<!-- tab start `json` -->

```json
{
    "error": "invalid_request",
    "error_description": "access_token invalid"
}
```

<!-- tab end -->

### Refresh access token 

使用重新整理權杖取得新的存取權杖。當使用者授權您的應用程式時，重新整理權杖會與存取權杖一併回傳。

<!-- note start -->

**注意**

- 這是 LINE Login v2.0 端點的參考文件。關於 v2.1 端點的資訊，請參閱 LINE Login v2.1 API 參考文件中的 [Refresh access token](https://developers.line.biz/en/reference/line-login/#refresh-access-token)。
- 您無法使用此端點重新整理 Messaging API 的頻道存取權杖（channel access token）。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/accessToken \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=refresh_token' \
--data-urlencode 'client_id={channel ID}' \
--data-urlencode 'client_secret={channel secret}' \
--data-urlencode 'refresh_token={refresh token}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/oauth/accessToken`

#### Request headers 

<!-- parameter start (props: required) -->
Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start -->
grant_type
String

`refresh_token`

<!-- parameter end -->
<!-- parameter start -->
refresh_token
String

對應於要重新簽發之存取權杖的重新整理權杖。在存取權杖到期後最多 10 天內有效。如果重新整理權杖過期，您必須提示使用者重新登入，以產生新的存取權杖。

<!-- parameter end -->
<!-- parameter start -->
client_id
String

頻道 ID（Channel ID）。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->
<!-- parameter start -->
client_secret
String

頻道密鑰（Channel secret）。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->

#### Response 

如果存取權杖成功重新整理，會回傳新的存取權杖與重新整理權杖。

<!-- parameter start -->
token_type
String

`Bearer`

<!-- parameter end -->
<!-- parameter start -->
scope
String

授予該存取權杖的權限。

- `P`：您擁有存取使用者個人資料資訊的權限。

<!-- parameter end -->
<!-- parameter start -->
access_token
String

存取權杖

<!-- parameter end -->
<!-- parameter start -->
expires_in
Number

存取權杖到期前的秒數。

<!-- parameter end -->
<!-- parameter start -->
refresh_token
String

用來取得新存取權杖的權杖（重新整理權杖）。在存取權杖到期後最多 10 天內有效。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
   "token_type":"Bearer",
   "scope":"P",
   "access_token":"bNl4YEFPI/hjFWhTqexp4MuEw...",
   "expires_in":2591977,
   "refresh_token":"8iFFRdyxNVNLWYeteMMJ"
}
```

<!-- tab end -->

#### Error response 

如果重新整理權杖已過期，會回傳 `400 Bad Request` 狀態碼，以及一個 JSON 物件。

_Example error response_

<!-- tab start `json` -->

```json
{
    "error": "invalid_grant",
    "error_description": "invalid refresh_token"
}
```

<!-- tab end -->

### Revoke access token 

使使用者的存取權杖失效。

<!-- note start -->

**注意**

- 這是 LINE Login v2.0 端點的參考文件。關於 v2.1 端點的資訊，請參閱 LINE Login v2.1 API 參考文件中的 [Revoke access token](https://developers.line.biz/en/reference/line-login/#revoke-access-token)。
- 您無法使用此端點使 Messaging API 的頻道存取權杖失效。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/revoke \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'refresh_token={refresh token}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/v2/oauth/revoke`

#### Request headers 

<!-- parameter start (props: required) -->
Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start -->
refresh_token
String

對應於要使其失效之存取權杖的重新整理權杖。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及空白的回應主體。

## Profile

### Get user profile 

取得使用者的 ID、顯示名稱、個人圖片與狀態消息。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/profile \
-H 'Authorization: Bearer {access token}'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/v2/profile`

#### Request headers 

<!-- parameter start (props: required) -->
Authorization

Bearer `{access token}`

<!-- parameter end -->

#### Response 

<!-- parameter start -->
userId
String

使用者 ID

<!-- parameter end -->
<!-- parameter start -->
displayName
String

使用者的顯示名稱

<!-- parameter end -->
<!-- parameter start -->
pictureUrl
String

個人圖片網址。這是一個 HTTPS 網址。如果使用者沒有設定個人圖片，回應中不會包含此欄位。

個人圖片縮圖：

您可以在使用者的個人圖片網址後面附加下列任一字尾，以取得縮圖版本的個人圖片。

字尾 | 縮圖尺寸
-------- | ------
`/large` | 200 x 200
`/small` | 51 x 51

例如：`https://profile.line-scdn.net/abcdefghijklmn/large`

<!-- parameter end -->
<!-- parameter start -->
statusMessage
String

使用者的狀態消息。如果使用者沒有設定狀態消息，回應中不會包含此欄位。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "userId":"U4af4980629...",
  "displayName":"Brown",
  "pictureUrl":"https://profile.line-scdn.net/abcdefghijklmn",
  "statusMessage":"Hello, LINE!"
}
```

<!-- tab end -->
