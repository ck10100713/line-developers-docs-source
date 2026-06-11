# LINE Login v2.1 API 參考文件（LINE Login v2.1 API reference）

## Common specifications 

### Rate limits 

如果您在短時間內向 LINE Login API 發送大量請求，且經判斷會影響 LINE Platform 的運作，我們可能會暫時限制您的請求。請勿基於任何目的（包括負載測試）發送大量請求。

<!-- tip start -->

**關於速率限制門檻**

LINE Login API 的速率限制（rate limit）門檻並未公開。

<!-- tip end -->

### Status codes 

以下 HTTP 狀態碼會在 API 呼叫後回傳。除非另有說明，否則我們遵循 [HTTP 狀態碼規範](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。

| Status code | Description |
| --- | --- |
| 200 OK | 請求成功。 |
| 400 Bad Request | 請求有問題。請檢查請求參數與 JSON 格式。 |
| 401 Unauthorized | 請檢查授權標頭（authorization header）是否正確。 |
| 403 Forbidden | 您未獲授權使用此 API。請確認您的帳號或方案已獲授權使用此 API。 |
| 413 Payload Too Large | 請求超過 2MB 的最大限制。請將請求縮小至 2MB 以下後重試。 |
| 429 Too Many Requests | 因大量請求超過[速率限制](https://developers.line.biz/en/reference/line-login/#rate-limits)而暫時限制請求。 |
| 500 Internal Server Error | API 伺服器發生暫時性錯誤。 |

### Response headers 

LINE Login API 回應中包含以下 HTTP 標頭：

| Response header | Description |
| --- | --- |
| x-line-request-id | 請求 ID。每個請求都會核發一個 ID。 |

## OAuth 

### Issue access token 

端點（endpoint）：`POST` `https://api.line.me/oauth2/v2.1/token`

核發存取權杖（access token）。

透過 LINE Login API 管理的存取權杖，可證明應用程式已獲授權存取儲存於 LINE Platform 上的使用者資料（例如使用者 ID、顯示名稱、個人檔案圖片與狀態消息）。

LINE Login API 呼叫要求您提供先前回應中所傳送的存取權杖或刷新權杖（refresh token）。

<!-- note start -->

**Note**

- 這是 LINE Login v2.1 端點的參考文件。關於 v2.0 端點的資訊，請參閱 v2.0 API 參考文件中的 [Issue access token](https://developers.line.biz/en/reference/line-login-v2/#issue-access-token)。
- 隨著新的 LINE Login 功能加入以及既有功能修改，回應與 ID token 中 JSON 物件的結構可能會變動。這些變動可能導致屬性新增或排序不同；元素之間的空白與換行被加入或移除；以及資料大小有所變化。請將您的後端設計為能容忍未來結構不同的 payload。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=1234567890abcde' \
--data-urlencode 'redirect_uri=https://example.com/auth?key=value' \
-d 'client_id=1234567890' \
-d 'client_secret=1234567890abcdefghij1234567890ab' \
-d 'code_verifier=wJKN8qz5t8SSI9lMFhBB6qwNkQBkuPZoCxzRhwLRUo1'
```

<!-- tab end -->

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

從 LINE Platform 收到的[授權碼（authorization code）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code)

<!-- parameter end -->
<!-- parameter start (props: required) -->

redirect_uri

String

與[授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)中指定的 `redirect_uri` 相同的值。

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
<!-- parameter start (props: optional) -->

code_verifier

String

由單位元組英數字元與符號組成的 43-128 字元隨機字串（例如 `wJKN8qz5t8SSI9lMFhBB6qwNkQBkuPZoCxzRhwLRUo1`）。<br><br>如果您的 LINE Login 實作了 PKCE，您可以加入此參數，讓 LINE Platform 端在回傳存取權杖前驗證 `code_verifier` 的有效性。<br><br>關於如何實作 PKCE 的更多資訊，請參閱 LINE Login 文件中的 [Implement PKCE for LINE Login](https://developers.line.biz/en/docs/line-login/integrate-pkce/#how-to-integrate-pkce)。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與包含以下資訊的 JSON 物件。

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

id_token

String

包含使用者資訊的 [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)。僅在您請求了 `openid` scope 時才會回傳此屬性。關於 ID token 的更多資訊，請參閱 [Get profile information from ID tokens](https://developers.line.biz/en/docs/line-login/verify-id-token/)。

<!-- parameter end -->
<!-- parameter start -->

refresh_token

String

用於取得新存取權杖的權杖（刷新權杖，refresh token）。在存取權杖核發後 90 天內有效。

如需更多資訊，請參閱 [Refresh access token](https://developers.line.biz/en/reference/line-login/#refresh-access-token)。

<!-- parameter end -->
<!-- parameter start -->

scope

String

授予存取權杖的權限。關於 scope 的更多資訊，請參閱 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

請注意，即使已授予 `email` scope 的存取權限，它也不會作為 `scope` 屬性的值回傳。

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
  "access_token": "bNl4YEFPI/hjFWhTqexp4MuEw5YPs...",
  "expires_in": 2592000,
  "id_token": "eyJhbGciOiJIUzI1NiJ9...",
  "refresh_token": "Aa1FdeggRhTnPNNpxr8p",
  "scope": "profile",
  "token_type": "Bearer"
}
```

<!-- tab end -->

### Verify access token validity 

驗證存取權杖是否有效。

關於如何使用存取權杖安全處理使用者註冊與登入的一般建議，請參閱 LINE Login 文件中的 [Creating a secure login process between your app and server](https://developers.line.biz/en/docs/line-login/secure-login-process/)。

<!-- note start -->

**Note**

這是 LINE Login v2.1 端點的參考文件。關於 v2.0 端點的資訊，請參閱 LINE Login v2.0 API 參考文件中的 [Verify access token validity](https://developers.line.biz/en/reference/line-login-v2/#verify-access-token)。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET \
'https://api.line.me/oauth2/v2.1/verify?access_token=eyJhbGciOiJIUzI1NiJ9.UnQ_o-GP0VtnwDjbK0C8E_NvK...'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/oauth2/v2.1/verify`

#### Query parameters 

<!-- parameter start (props: required) -->

access_token

存取權杖

<!-- parameter end -->

#### Response 

如果存取權杖有效，會回傳 `200 OK` 狀態碼以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

scope

String

授予存取權杖的權限。若要進一步了解 scope，請參閱 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

<!-- parameter end -->
<!-- parameter start -->

client_id

String

核發此存取權杖的頻道 ID

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
  "scope": "profile",
  "client_id": "1440057261",
  "expires_in": 2591659
}
```

<!-- tab end -->

#### Error response 

如果存取權杖已過期，會回傳 `400 Bad Request` HTTP 狀態碼與 JSON 回應。

_Example error response_

<!-- tab start `json` -->

```json
{
  "error": "invalid_request",
  "error_description": "access token expired"
}
```

<!-- tab end -->

### Refresh access token 

使用刷新權杖取得新的存取權杖。

當使用者驗證完成後，刷新權杖會與存取權杖一同回傳。

<!-- note start -->

**Note**

- 這是 LINE Login v2.1 端點的參考文件。關於 v2.0 端點的資訊，請參閱 LINE Login v2.0 API 參考文件中的 [Refresh access token](https://developers.line.biz/en/reference/line-login-v2/#refresh-access-token)。
- 您無法使用此端點來刷新 Messaging API 的頻道存取權杖（channel access token）。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=refresh_token&refresh_token={your_refresh_token}&client_id={your_channel_id}&client_secret={your_channel_secret}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/oauth2/v2.1/token`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

grant_type

String

`refresh_token`

<!-- parameter end -->
<!-- parameter start (props: required) -->

refresh_token

String

與要重新核發的存取權杖對應的刷新權杖。在存取權杖核發後最多 90 天內有效。如果刷新權杖過期，您必須提示使用者重新登入以產生新的存取權杖。

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_id

String

頻道 ID。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

client_secret

String

頻道密鑰。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

- 對於 **App types** 僅為 **Web app** 的頻道為必填。
- 對於 **App types** 為 **Mobile app** 與 **Web app** 的頻道會被忽略。
- 對於 **App types** 僅為 **Mobile app** 的頻道會被忽略。

<!-- parameter end -->

#### Response 

如果存取權杖成功刷新，會回傳新的存取權杖與刷新權杖。

<!-- parameter start -->

access_token

String

存取權杖。有效期間為 30 天。

<!-- parameter end -->
<!-- parameter start -->

token_type

String

`Bearer`

<!-- parameter end -->
<!-- parameter start -->

refresh_token

String

您在請求重新核發存取權杖時為 `refresh_token` 屬性所指定的刷新權杖。取得新的存取權杖不會延長刷新權杖的有效期間。

<!-- parameter end -->
<!-- parameter start -->

expires_in

Number

存取權杖的有效期間。以從 API 被呼叫時起算到期前的剩餘秒數表示。

<!-- parameter end -->
<!-- parameter start -->

scope

String

透過存取權杖取得的權限。關於 scope 的更多資訊，請參閱 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "token_type": "Bearer",
  "scope": "profile",
  "access_token": "bNl4YEFPI/hjFWhTqexp4MuEw...",
  "expires_in": 2591977,
  "refresh_token": "8iFFRdyxNVNLWYeteMMJ"
}
```

<!-- tab end -->

#### Error response 

如果刷新權杖已過期，會回傳 `400 Bad Request` HTTP 狀態碼與 JSON 回應。

_Example error response_

<!-- tab start `json` -->

```json
{
  "error": "invalid_grant",
  "error_description": "invalid refresh token"
}
```

<!-- tab end -->

### Revoke access token 

使使用者的存取權杖失效。

<!-- note start -->

**Note**

- 這是 LINE Login v2.1 端點的參考文件。關於 v2.0 端點的資訊，請參閱 LINE Login v2.0 API 參考文件中的 [Revoke access token](https://developers.line.biz/en/reference/line-login-v2/#revoke-access-token)。
- 您無法使用此端點來使 Messaging API 的頻道存取權杖失效。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/revoke \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "client_id={channel id}&client_secret={channel secret}&access_token={access token}"
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/oauth2/v2.1/revoke`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

access_token

String

存取權杖

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_id

String

頻道 ID。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

client_secret

String

頻道密鑰。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

- 對於 **App types** 僅為 **Web app** 的頻道為必填。
- 對於 **App types** 為 **Mobile app** 與 **Web app** 的頻道會被忽略。
- 對於 **App types** 僅為 **Mobile app** 的頻道會被忽略。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與空的回應主體。

### Deauthorize your app to which the user has granted permissions 

代表使用者取消對您應用程式的授權，撤銷（revoke）使用者先前授予的權限。如需更多資訊，請參閱 [LINE Login 開發準則](https://developers.line.biz/en/docs/line-login/development-guidelines/)中的必要事項「[Deauthorize your app when a user unregisters from your app](https://developers.line.biz/en/docs/line-login/development-guidelines/#deauthorize)」。

您也可以使用此端點撤銷 LIFF apps 與 LINE MINI Apps 的權限。

關於使用者如何取消對其已授予權限的應用程式之授權，請參閱 LINE Login 文件中的 [Managing authorized apps](https://developers.line.biz/en/docs/line-login/managing-authorized-apps/)。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/user/v1/deauthorize \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "userAccessToken": "{user access token}"
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/user/v1/deauthorize`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

可使用以下類型的頻道存取權杖：

- [使用者指定到期時間的頻道存取權杖（Channel access token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)
- [無狀態頻道存取權杖（Stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)

關於如何核發頻道存取權杖的更多資訊，請參閱 LINE Platform basics 中的 [Channel access token](https://developers.line.biz/en/docs/basics/channel-access-token/)。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

userAccessToken

String

目標使用者的存取權杖

<!-- parameter end -->

#### Response 

回傳狀態碼 `204` 與空的回應主體。

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 目標使用者的存取權杖無效。請考慮以下原因：<ul><li>使用者已取消對您應用程式的授權。</li><li>您已透過 API 代表使用者取消對您應用程式的授權。</li></ul> |

_Error response example_

<!-- tab start `json` -->

```json
// If the access token for the target user is invalid (400 Bad Request)
{
  "message": "invalid token"
}
```

<!-- tab end -->

### Verify ID token 

ID token 是包含使用者資訊的 JSON web token (JWT)。攻擊者有可能偽造 [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens)。請使用此呼叫來驗證所收到的 ID token 是否為真，意即您可以用它來取得使用者的個人檔案資訊與電子郵件。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST 'https://api.line.me/oauth2/v2.1/verify' \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'id_token=eyJraWQiOiIxNmUwNGQ0ZTU2NzgzYTc5MmRjYjQ2ODRkOD...' \
--data-urlencode 'client_id=1234567890'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/oauth2/v2.1/verify`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

id_token

String

ID token

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_id

String

預期的頻道 ID。LINE Platform 為您的頻道核發的唯一識別碼。可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

nonce

String

預期的 `nonce` 值。請使用授權請求中提供的 `nonce` 值。如果授權請求中未指定 `nonce` 值，請省略。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

user_id

String

預期的使用者 ID。請從 [Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile) 了解如何取得使用者 ID。

<!-- parameter end -->

#### Response 

當指定的 ID token 成功通過驗證時，會回傳 ID token payload。

<!-- parameter start -->

iss

String

用於產生 ID token 的 URL。

<!-- parameter end -->
<!-- parameter start -->

sub

String

產生 ID token 所對應的使用者 ID。

<!-- parameter end -->
<!-- parameter start -->

aud

String

頻道 ID

<!-- parameter end -->
<!-- parameter start -->

exp

Number

ID token 的到期時間，以 UNIX 時間（秒）表示。

<!-- parameter end -->
<!-- parameter start -->

iat

Number

產生 ID token 的時間，以 UNIX 時間（秒）表示。

<!-- parameter end -->
<!-- parameter start -->

auth_time

Number

使用者被驗證的時間，以 UNIX 時間（秒）表示。如果授權請求中未指定 `max_age` 值則不會包含。

<!-- parameter end -->
<!-- parameter start -->

nonce

String

授權 URL 中指定的 `nonce` 值。如果授權請求中未指定 `nonce` 值則不會包含。

<!-- parameter end -->
<!-- parameter start -->

amr

Array of strings

使用者所使用的驗證方法清單。在某些條件下不會包含於 payload 中。

以下一項或多項：

- `pwd`：使用電子郵件與密碼登入
- `lineautologin`：LINE 自動登入（包括透過 LINE SDK）
- `lineqr`：使用 QR code 登入
- `linesso`：使用單一登入（single sign-on）登入
- `mfa`：使用雙重驗證登入

<!-- parameter end -->
<!-- parameter start -->

name

String

使用者的顯示名稱。如果授權請求中未指定 `profile` scope 則不會包含。

<!-- parameter end -->
<!-- parameter start -->

picture

String

使用者的個人檔案圖片 URL。如果授權請求中未指定 `profile` scope 則不會包含。

<!-- parameter end -->
<!-- parameter start -->

email

String

使用者的電子郵件地址。如果授權請求中未指定 `email` scope 則不會包含。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "iss": "https://access.line.me",
  "sub": "U1234567890abcdef1234567890abcdef",
  "aud": "1234567890",
  "exp": 1504169092,
  "iat": 1504263657,
  "nonce": "0987654asdf",
  "amr": ["pwd"],
  "name": "Taro Line",
  "picture": "https://sample_line.me/aBcdefg123456",
  "email": "taro.line@example.com"
}
```

<!-- tab end -->

#### Error response 

當指定的 ID token 驗證失敗時，會回傳一個 JSON 物件。

| error_description | Description |
| --- | --- |
| Invalid IdToken. | ID token 格式不正確，或簽章無效。 |
| Invalid IdToken Issuer. | ID token 在「https://access.line.me」以外的網站產生。 |
| IdToken expired. | ID token 已過期。 |
| Invalid IdToken Audience. | ID token 的 Audience 值與請求中指定的 `client_id` 不同。 |
| Invalid IdToken Nonce. | ID token 的 Nonce 值與請求中指定的 `nonce` 不同。 |
| Invalid IdToken Subject Identifier. | ID token 的 SubjectIdentifier 值與請求中指定的 `user_id` 不同。 |

_Example error response_

<!-- tab start `json` -->

```json
{
  "error": "invalid_request",
  "error_description": "Invalid IdToken."
}
```

<!-- tab end -->

### Get user information 

取得使用者的 ID、顯示名稱與個人檔案圖片。存取權杖所需的 scope 與 [Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile) 端點不同。

您只能取得主要個人檔案資訊。您無法取得使用者的[子個人檔案（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

<!-- note start -->

**Note**

需要具備 `openid` scope 的存取權杖。如需更多資訊，請參閱 LINE Login 文件中的 [Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request) 與 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/oauth2/v2.1/userinfo \
-H 'Authorization: Bearer {access token}'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/oauth2/v2.1/userinfo`

`POST https://api.line.me/oauth2/v2.1/userinfo`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{access token}`

<!-- parameter end -->

#### Response 

<!-- parameter start -->

sub

String

使用者 ID

<!-- parameter end -->
<!-- parameter start -->

name

String

使用者的顯示名稱。如果授權請求中未指定 `profile` scope 則不會包含。

<!-- parameter end -->
<!-- parameter start -->

picture

String

使用者的個人檔案圖片 URL。如果授權請求中未指定 `profile` scope 則不會包含。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "sub": "U1234567890abcdef1234567890abcdef",
  "name": "Taro Line",
  "picture": "https://profile.line-scdn.net/0h8pWWElvzZ19qLk3ywQYYCFZraTIdAGEXEhx9ak56MDxDHiUIVEEsPBspMG1EGSEPAk4uP01t0m5G"
}
```

<!-- tab end -->

## Profile 

### Get user profile 

取得使用者的 ID、顯示名稱、個人檔案圖片與狀態消息。存取權杖所需的 scope 與 [Get user information](https://developers.line.biz/en/reference/line-login/#userinfo) 端點不同。

您只能取得主要個人檔案資訊。您無法取得使用者的[子個人檔案（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

<!-- note start -->

**Note**

需要具備 `profile` scope 的存取權杖。如需更多資訊，請參閱 LINE Login 文件中的 [Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request) 與 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

<!-- note end -->

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

個人檔案圖片 URL。這是一個 HTTPS URL。僅在使用者已設定個人檔案圖片時才會包含於回應中。

個人檔案圖片縮圖：

您可以在使用者的個人檔案圖片 URL 後附加以下任一字尾，以取得使用者個人檔案圖片的縮圖版本。

| Suffix   | Thumbnail size |
| -------- | -------------- |
| `/large` | 200 x 200      |
| `/small` | 51 x 51        |

例如 `https://profile.line-scdn.net/abcdefghijklmn/large`

<!-- parameter end -->
<!-- parameter start -->

statusMessage

String

使用者的狀態消息。如果使用者沒有狀態消息則不會包含於回應中。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "userId": "U4af4980629...",
  "displayName": "Brown",
  "pictureUrl": "https://profile.line-scdn.net/abcdefghijklmn",
  "statusMessage": "Hello, LINE!"
}
```

<!-- tab end -->

## Friendship status 

### Get friendship status 

取得使用者與連結至您 LINE Login 頻道的 LINE 官方帳號之間的好友狀態。

關於如何使用加入好友選項的更多資訊，請參閱 LINE Login 文件中的 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/friendship/v1/status \
-H 'Authorization: Bearer {access token}'
```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/friendship/v1/status`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{access token}`

<!-- parameter end -->

<!-- note start -->

**Note**

需要具備 `profile` scope 的存取權杖。如需更多資訊，請參閱 LINE Login 文件中的 [Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request) 與 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

<!-- note end -->

#### Response 

<!-- parameter start -->

friendFlag

Boolean

- `true`：使用者已將 LINE 官方帳號加為好友且未將其封鎖。
- 否則為 `false`。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "friendFlag": true
}
```

<!-- tab end -->
