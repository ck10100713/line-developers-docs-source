# Messaging API 參考

## Common specifications 

Messaging API 的共通規格，例如端點（endpoint）的網域名稱、請求（request）成功或失敗時的回應（response），以及速率限制（rate limit）。

- [Domain name](https://developers.line.biz/en/reference/messaging-api/#domain-name)
- [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)
- [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes)
- [Response headers](https://developers.line.biz/en/reference/messaging-api/#response-headers)
- [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)
- [Other common specifications](https://developers.line.biz/en/reference/messaging-api/#other-common-specifications)

### Domain name 

在 Messaging API 中，網域名稱會依端點而不同。請注意，每個端點都要使用正確的網域名稱。

| Domain name | Endpoint |
| --- | --- |
| `api-data.line.me`  | <ul><li>[Get content](https://developers.line.biz/en/reference/messaging-api/#get-content)</li><li>[Create audience for uploading user IDs (by file)](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group-by-file)</li><li>[Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file)](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group-by-file)</li><li>[Upload rich menu image](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)</li><li>[Download rich menu image](https://developers.line.biz/en/reference/messaging-api/#download-rich-menu-image)</li></ul> |
| `api.line.me` | 其他 API 端點 |

### Rate limits 

Messaging API 針對每個 API 功能（端點）以每個頻道（channel）為單位套用以下速率限制。如需更多關於速率限制套用範圍的資訊，請參閱 [Scope of rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits-scope)。

<!-- note start -->

**請勿送出超過速率限制的請求**

如果你送出超過速率限制的請求，將會收到一則錯誤訊息：`429 Too Many Requests`。當你使用 Messaging API 開發 LINE Bot 時，請遵循 [Messaging API development guidelines](https://developers.line.biz/en/docs/messaging-api/development-guidelines/)，包括關於速率限制的指引。

<!-- note end -->

| Endpoint | Rate limit |
| --- | --- |
| <ul><li>[Send a narrowcast message](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)</li><li>[Send a broadcast message](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)</li><li>[Get number of message deliveries](https://developers.line.biz/en/reference/messaging-api/#get-number-of-delivery-messages)</li><li>[Get number of friends](https://developers.line.biz/en/reference/messaging-api/#get-number-of-followers)</li><li>[Get friend demographics](https://developers.line.biz/en/reference/messaging-api/#get-demographic)</li><li>[Get user interaction statistics](https://developers.line.biz/en/reference/messaging-api/#get-message-event)</li><li>[Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit)</li><li>[Test webhook endpoint](https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint)</li></ul> | 每小時 60 次請求 |
| <ul><li>[Create audience for uploading user IDs (by JSON)](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group)</li><li>[Create audience for uploading user IDs (by file)](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group-by-file)</li><li>[Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by JSON)](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group)</li><li>[Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file)](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group-by-file)</li><li>[Create message click audience](https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group)</li><li>[Create message impression audience](https://developers.line.biz/en/reference/messaging-api/#create-imp-audience-group)</li><li>[Rename an audience](https://developers.line.biz/en/reference/messaging-api/#set-description-audience-group)</li><li>[Delete audience](https://developers.line.biz/en/reference/messaging-api/#delete-audience-group)</li><li>[Get audience data](https://developers.line.biz/en/reference/messaging-api/#get-audience-group)</li><li>[Get data for multiple audiences](https://developers.line.biz/en/reference/messaging-api/#get-audience-groups)</li><li>[Get shared audience data in Business Manager](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience)</li><li>[Get a list of shared audiences in Business Manager](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience-list)</li></ul> | 每分鐘 60 次請求 |
| <ul><li>[Set webhook endpoint URL](https://developers.line.biz/en/reference/messaging-api/#set-webhook-endpoint-url)</li><li>[Get webhook endpoint information](https://developers.line.biz/en/reference/messaging-api/#get-webhook-endpoint-information)</li></ul> | 每分鐘 1,000 次請求 |
| <ul><li>[Create rich menu](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu)</li><li>[Delete rich menu](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu)</li><li>[Delete rich menu alias](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu-alias)</li><li>[Get the status of rich menu batch control](https://developers.line.biz/en/reference/messaging-api/#get-batch-control-rich-menus-progress-status)</li></ul> | 每小時 100 次請求 \* |
| <ul><li>[Replace or unlink the linked rich menus in batches](https://developers.line.biz/en/reference/messaging-api/#batch-control-rich-menus-of-users)</li></ul> | 每小時 3 次請求 |
| <ul><li>[Get rich menu list](https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-list)</li></ul> | 每秒 10 次請求 |
| <ul><li>[Send multicast message](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)</li><li>[Get a user's membership subscription status](https://developers.line.biz/en/reference/messaging-api/#get-a-users-membership-subscription-status)</li><li>[Get membership plans being offered](https://developers.line.biz/en/reference/messaging-api/#get-membership-plans)</li><li>[Create a coupon](https://developers.line.biz/en/reference/messaging-api/#create-coupon)</li><li>[Discontinue a coupon](https://developers.line.biz/en/reference/messaging-api/#discontinue-coupon)</li><li>[Get a list of coupons](https://developers.line.biz/en/reference/messaging-api/#get-coupons-list)</li><li>[Get details of a coupon](https://developers.line.biz/en/reference/messaging-api/#get-coupon)</li></ul> | 每秒 200 次請求 |
| <ul><li>[Display a loading animation](https://developers.line.biz/en/reference/messaging-api/#display-a-loading-indicator)</li></ul> | 每秒 100 次請求 |
| <ul><li>[Issue short-lived channel access token](https://developers.line.biz/en/reference/messaging-api/#issue-shortlived-channel-access-token)</li></ul> | 每秒 370 次請求 |
| 其他 API 端點 | 每秒 2,000 次請求 |

\* 使用 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 建立與刪除 rich menu 不受此限制。

#### Scope of rate limits 

Messaging API 針對每個 API 功能（端點）以每個頻道為單位套用速率限制。另外請留意以下關於速率限制套用範圍的重點：

- 即使端點 URL 相同，只要 HTTP 方法不同，就視為不同的端點。
- 我們套用速率限制時，不會區分 URL 中的參數值或請求主體的內容。
- 即使你從不同的 IP 位址使用端點，我們套用速率限制時也不會加以區分。
- 如果你從不同頻道對同一個 LINE Official Account 使用端點，我們會針對每個頻道各自獨立套用速率限制。

#### Limit on the number of concurrent operations 

針對建立用於上傳 user ID 的 audience，以及將 user ID 加入 audience，我們對每個 audience ID（`audienceGroupId`）的並行端點操作數設有上限。

以下端點同時被處理的請求總數會被計為並行操作數。

| Endpoint | 並行操作數的</br >上限 |
| --- | --- |
| <ul><li>[Create audience for uploading user IDs (by JSON)](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group)</li><li>[Create audience for uploading user IDs (by file)](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group-by-file)</li><li>[Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by JSON)](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group)</li><li>[Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file)](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group-by-file)</li></ul> | 10 |

超過並行操作數上限的請求，將會回傳帶有 [status code](https://developers.line.biz/en/reference/messaging-api/#status-codes) `429 Too Many Requests` 的錯誤。如果你收到錯誤，請稍候片刻再重新發出請求。

你可以透過以下端點回應的 `jobs` 屬性（property），確認正在處理中的請求數。如果某項工作的狀態（`jobs[].jobStatus` 屬性）為等待執行（`QUEUED`）或執行中（`WORKING`），就會被計為一個操作。

- [Get audience data](https://developers.line.biz/en/reference/messaging-api/#get-audience-group)

### Status codes 

呼叫 API 之後會回傳這些 HTTP 狀態碼。除非另有說明，否則我們遵循 [HTTP status code specification](https://datatracker.ietf.org/doc/html/rfc7231#section-6)。

| Status code | Description |
| --- | --- |
| 200 OK | 請求成功。 |
| 400 Bad Request | 請求有問題。 |
| 401 Unauthorized | 未指定有效的頻道存取權杖（channel access token）。 |
| 403 Forbidden | 未獲授權存取該資源。請確認你的帳號或方案是否獲授權存取該資源。 |
| 404 Not Found | 無法取得個人檔案資訊。可能原因如下：<ul><li>目標 user ID 不存在。</li><li>使用者尚未同意取得其個人檔案資訊。</li><li>使用者尚未將目標 LINE Official Account 加為好友。</li><li>使用者在加為好友後又封鎖了目標 LINE Official Account。</li></ul>如需更多資訊，請參閱 Messaging API 文件中的 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。 |
| 409 Conflict | 已接受過使用相同重試金鑰（retry key）的 API 請求。詳情請參閱 [Retry failed API request](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。 |
| 410 Gone | 存取已不再提供的資源。 |
| 413 Payload Too Large | 請求超過 2MB 的大小上限。請將請求縮小至 2MB 以下後再試一次。 |
| 415 Unsupported Media Type | 上傳檔案的媒體類型不受支援。 |
| 429 Too Many Requests | <ul><li>超過請求的[速率限制](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。</li><li>超過請求的[並行操作數上限](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。</li><li>超過免費訊息數。</li><li>超過你可發送的額外訊息數上限。</li></ul><p>如需更多關於免費訊息數與可發送額外訊息數上限的資訊，請參閱 Messaging API 文件中的 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。</p><p>即使你本月仍有可發送的訊息額度，也可能收到此錯誤。如需更多資訊，請參閱 FAQ 中的 [Why do I get a 429 Too Many Requests error (You have reached your monthly limit.) even though I still have messages available to send for the current month?](https://developers.line.biz/en/faq/#why-do-i-get-429-error-during-message-delivery)。</p> |
| 500 Internal Server Error | 內部伺服器發生錯誤。 |

### Response headers 

Messaging API 的回應中會包含以下 HTTP 標頭：

| Response headers | Description |
| --- | --- |
| X-Line-Request-Id | 請求 ID。每個請求都會發給一個 ID。 |
| X-Line-Accepted-Request-Id 不一定會包含  | 如果請求已使用相同的重試金鑰被接受，則會顯示已接受請求的 `x-line-request-id`。如需更多資訊，請參閱 [Retrying an API request](https://developers.line.biz/en/reference/messaging-api/#retry-api-request)。 |

### Error responses 

發生錯誤時，回應主體中會回傳以下 JSON 資料。

<!-- parameter start -->

message

String

包含錯誤相關資訊的訊息。詳情請參閱 [Error messages](https://developers.line.biz/en/reference/messaging-api/#error-messages)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

details

Array

錯誤詳情的陣列（array）。如果陣列為空，回應中將不會包含此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

details\[].message

String

錯誤的詳細內容。在某些情況下不會包含於回應中。

如需更多關於 Managing Audience 端點錯誤詳情的資訊，請參閱 [Details of the error related to audience management](https://developers.line.biz/en/reference/messaging-api/#manage-audience-error)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

details\[].property

String

錯誤發生的位置。回傳請求中的 JSON 欄位名稱或查詢參數名稱。在某些情況下不會包含於回應中。

<!-- parameter end -->

_錯誤回應範例_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 2 error(s)",
  "details": [
    {
      "message": "May not be empty",
      "property": "messages[0].text"
    },
    {
      "message": "Must be one of the following values: [text, image, video, audio, location, sticker, template, imagemap]",
      "property": "messages[1].type"
    }
  ]
}
```

<!-- tab end -->

#### Error messages 

以下是 JSON 錯誤回應中 `message` 屬性裡常見的主要錯誤訊息。

| Message | Description |
| --- | --- |
| The request body has X error(s) | 請求主體的 JSON 資料中發現錯誤。錯誤數量顯示於「X」處。進一步的詳情會顯示於 `details[].message` 與 `details[].property` 屬性中。 |
| Invalid reply token | 在 [send reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message) 的 `replyToken` 中指定的回覆權杖無效。可能原因如下：<ul><li>使用已過期的回覆權杖發送回覆訊息。</li><li>使用已用過的回覆權杖發送回覆訊息。</li></ul> |
| The property, XXX, in the request body is invalid (line: XXX, column: XXX) | 請求主體中指定了無效的屬性。該特定屬性會顯示於「XXX」處。 |
| The request body could not be parsed as JSON (line: XXX, column: XXX) | 請求主體中的 JSON 無法被解析。會顯示具體的行與列。 |
| The content type, XXX, is not supported | 請求了 API 不支援的內容類型。 |
| Authentication failed due to the following reason: XXX | 呼叫 API 時驗證失敗。原因會顯示於「XXX」處。 |
| Access to this API is not available for your account | 當你呼叫沒有權限使用的 API 時會出現。 |
| Failed to send messages | 當訊息發送失敗時會出現。出現此情況的其中一個原因，是指定的 user ID 不存在。 |
| You have reached your monthly limit. | <ul><li>超過免費訊息數。</li><li>超過你可發送的額外訊息數上限。</li></ul><p>如需更多關於免費訊息數與可發送額外訊息數上限的資訊，請參閱 Messaging API 文件中的 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。</p><p>即使你本月仍有可發送的訊息額度，也可能收到此錯誤。如需更多資訊，請參閱 FAQ 中的 [Why do I get a 429 Too Many Requests error (You have reached your monthly limit.) even though I still have messages available to send for the current month?](https://developers.line.biz/en/faq/#why-do-i-get-429-error-during-message-delivery)。</p> |
| The API rate limit has been exceeded. Try again later. | 超過請求的[速率限制](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。 |
| Not found | 無法取得個人檔案資訊。可能原因如下：<ul><li>目標 user ID 不存在</li><li>使用者尚未同意取得其個人檔案資訊</li><li>使用者尚未將目標 LINE Official Account 加為好友</li><li>使用者在加為好友後又封鎖了目標 LINE Official Account</li></ul>如需更多資訊，請參閱 Messaging API 文件中的 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。 |

### Other common specifications 

#### About the encoding of a URL specified in a request body property 

屬性中的網域名稱、路徑、查詢參數與片段（fragment）應使用 UTF-8 進行[百分比編碼（percent-encoding）](https://en.wikipedia.org/wiki/Percent-encoding)。

例如，如果你指定一個具有以下組成部分的 URI，它應該是 `https://example.com/path?q=Good%20morning#Good%20afternoon`。

| Scheme | Domain name | Path  | Query parameter | Fragment       |
| ------ | ----------- | ----- | --------------- | -------------- |
| https  | example.com | /path | q=Good morning  | Good afternoon |

## Webhooks 

當有事件發生時，例如使用者將你的 LINE Official Account 加為好友或傳送訊息，LINE Platform 會向 webhook URL（bot 伺服器）發送 HTTPS POST 請求。

webhook URL 在 [LINE Developers Console](https://developers.line.biz/console/) 中針對每個頻道進行設定。

<!-- tip start -->

**我們建議你將事件處理改為非同步**

我們建議你將事件處理改為非同步，這樣 HTTP POST 請求的處理就不會延遲後續事件的處理。

<!-- tip end -->

<!-- note start -->

**LINE Platform 的 IP 位址不會公開**

發送 webhook 請求的 LINE Platform IP 位址不會公開。為了更好的安全性，請使用[簽章驗證（signature validation）](https://developers.line.biz/en/reference/messaging-api/#signature-validation)，而非以 IP 位址進行存取控制。

<!-- note end -->

### Request headers 

<!-- parameter start -->

x-line-signature

用於[簽章驗證](https://developers.line.biz/en/reference/messaging-api/#signature-validation)

<!-- parameter end -->

<!-- note start -->

**請求標頭欄位名稱不分大小寫**

[Request headers](https://developers.line.biz/en/reference/messaging-api/#request-headers) 欄位名稱中的大寫與小寫字母可能會在不另行通知的情況下變動。接收 webhook 的 bot 伺服器在處理標頭欄位名稱時，應不區分大小寫。\*1

|                           | 變更前      | 變更後       |
| ------------------------- | ------------------ | ------------------ |
| 標頭欄位名稱範例 | `X-Line-Signature` | `x-line-signature` |

\*1 [https://datatracker.ietf.org/doc/html/rfc7230#section-3.2](https://datatracker.ietf.org/doc/html/rfc7230#section-3.2)

<!-- note end -->

### Request body 

請求主體包含一個 JSON 物件（object），其中含有應接收 webhook 事件的 bot 的 user ID，以及一個 [webhook event objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects) 的陣列。

<!-- parameter start -->

destination

String

應接收 webhook 事件的 bot 的 user ID。user ID 值是一個符合正規表示式 `U[0-9a-f]{32}` 的字串。

<!-- parameter end -->
<!-- parameter start -->

events

Array

[webhook event objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects) 的陣列。LINE Platform 可能會傳送一個不含 webhook event object 的空陣列，以確認通訊狀況。

<!-- parameter end -->

### Response 

bot 伺服器在收到 LINE Platform 發送的 HTTP POST 請求後，必須回傳狀態碼 `200`。

<!-- note start -->

**注意**

- 即使 bot 伺服器未能成功接收 LINE Platform 發送的 HTTP POST 請求，bot 伺服器仍可再次接收此請求。如需更多資訊，請參閱 [Redeliver a webhook that failed to be received](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-redelivery)。
- LINE Platform 可能會傳送一個不含 webhook 事件的 HTTP POST 請求，以確認通訊狀況。在此情況下，請傳回 `200` 狀態碼。

  不含 webhook 事件的 HTTP POST 請求範例：

  ```json
  {
    "destination": "xxxxxxxxxx",
    "events": []
  }
  ```

<!-- note end -->

### Signature validation 

當 bot 伺服器收到 webhook 事件時，請在處理 [webhook event objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects) 之前，先驗證請求標頭中包含的簽章。這個驗證步驟很重要，可確認 webhook 確實來自 LINE Platform，且在傳輸過程中未遭竄改。

如需更多資訊，請參閱 [Verify webhook signature](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/)。

_簽章驗證範例_

<!-- tab start `java` -->

```java
String channelSecret = '...'; // Channel secret string
String httpRequestBody = '...'; // Request body string
SecretKeySpec key = new SecretKeySpec(channelSecret.getBytes(), "HmacSHA256");
Mac mac = Mac.getInstance("HmacSHA256");
mac.init(key);
byte[] source = httpRequestBody.getBytes("UTF-8");
String signature = Base64.encodeBase64String(mac.doFinal(source));
// Compare x-line-signature request header string and the signature
```

<!-- tab end -->
<!-- tab start `ruby` -->

```ruby
CHANNEL_SECRET = '...' # Channel secret string
http_request_body = request.raw_post # Request body string
hash = OpenSSL::HMAC::digest(OpenSSL::Digest::SHA256.new, CHANNEL_SECRET, http_request_body)
signature = Base64.strict_encode64(hash)
# Compare x-line-signature request header string and the signature
```

<!-- tab end -->
<!-- tab start `go` -->

```go
defer req.Body.Close()
body, err := ioutil.ReadAll(req.Body)
if err != nil {
  // ...
}
decoded, err := base64.StdEncoding.DecodeString(req.Header.Get("x-line-signature"))
if err != nil {
  // ...
}
hash := hmac.New(sha256.New, []byte("<channel secret>"))
hash.Write(body)
// Compare decoded signature and `hash.Sum(nil)` by using `hmac.Equal`
```

<!-- tab end -->
<!-- tab start `php` -->

```php
$channelSecret = '...'; // Channel secret string
$httpRequestBody = '...'; // Request body string
$hash = hash_hmac('sha256', $httpRequestBody, $channelSecret, true);
$signature = base64_encode($hash);
// Compare x-line-signature request header string and the signature
```

<!-- tab end -->
<!-- tab start `perl` -->

```perl
use Digest::SHA 'hmac_sha256';
use MIME::Base64 'encode_base64';

my $channel_secret= '...'; # Channel secret string
my $http_body = '...'; # Request body string
my $signature = encode_base64(hmac_sha256($http_body, $channel_secret));
# Compare x-line-signature request header string and the signature
```

<!-- tab end -->
<!-- tab start `python` -->

```python
import base64
import hashlib
import hmac

channel_secret = '...' # Channel secret string
body = '...' # Request body string
hash = hmac.new(channel_secret.encode('utf-8'),
    body.encode('utf-8'), hashlib.sha256).digest()
signature = base64.b64encode(hash)
# Compare x-line-signature request header and the signature
```

<!-- tab end -->
<!-- tab start `nodejs` -->

```javascript
const crypto = require("crypto");

const channelSecret = "..."; // Channel secret string
const body = "..."; // Request body string
const signature = crypto
  .createHmac("SHA256", channelSecret)
  .update(body)
  .digest("base64");
// Compare x-line-signature request header and the signature
```

<!-- tab end -->

## Webhook Event Objects 

這些是包含 LINE Platform 所產生事件的 JSON 物件。

這些事件物件的某些屬性可能沒有值。產生的事件物件不會包含任何沒有值的屬性。

<!-- tip start -->

**單一 webhook 可能包含多個 webhook event object**

LINE Platform 發送的 webhook 可能包含多個 webhook event object。每個 webhook 不一定只對應一位使用者。來自 A 的[訊息事件（message event）](https://developers.line.biz/en/reference/messaging-api/#message-event)與來自 B 的[加入好友事件（follow event）](https://developers.line.biz/en/reference/messaging-api/#follow-event)可能會在同一個 webhook 中。

即使你收到包含多個事件物件的 webhook，也請實作成讓 bot 伺服器能依其內容適當處理。如需更多資訊，請參閱 Webhook 下的 [request body](https://developers.line.biz/en/reference/messaging-api/#request-body)。

<!-- tip end -->

_webhook event object 範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "message",
      "message": {
        "type": "text",
        "id": "14353798921116",
        "text": "Hello, world"
      },
      "timestamp": 1625665242211,
      "source": {
        "type": "user",
        "userId": "U80696558e1aa831..."
      },
      "replyToken": "757913772c4646b784d4b7ce46d12671",
      "mode": "active",
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      }
    },
    {
      "type": "follow",
      "timestamp": 1625665242214,
      "source": {
        "type": "user",
        "userId": "Ufc729a925b3abef..."
      },
      "replyToken": "bb173f4d9cf64aed9d408ab4e36339ad",
      "mode": "active",
      "webhookEventId": "01FZ74ASS536FW97EX38NKCZQK",
      "deliveryContext": {
        "isRedelivery": false
      }
    },
    {
      "type": "unfollow",
      "timestamp": 1625665242215,
      "source": {
        "type": "user",
        "userId": "Ubbd4f124aee5113..."
      },
      "mode": "active",
      "webhookEventId": "01FZ74B5Y0F4TNKA5SCAVKPEDM",
      "deliveryContext": {
        "isRedelivery": false
      }
    }
  ]
}
```

<!-- tab end -->

### Common properties 

以下屬性是 webhook event object 中的共通屬性。

<!-- parameter start -->

type

String

事件類型的識別碼

<!-- parameter end -->
<!-- parameter start -->

mode

String

頻道狀態。

- `active`：頻道為啟用中。你可以從收到此 webhook 事件的 bot 伺服器發送回覆訊息或推播訊息等。
- `standby`：頻道為等待中。當頻道狀態為 `standby` 時，webhook 事件不會包含用於[發送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖。如需更多關於頻道狀態設為 `standby` 的時機資訊，請參閱模組（module）文件中的 [Get webhook event](https://developers.line.biz/en/docs/partner-docs/module/#bot-module-channel-receive-webhook)。

<!-- note start -->

**當頻道狀態為 standby 時，bot 伺服器不應發送任何訊息**

當頻道狀態為 `standby` 時，[模組（module）](https://developers.line.biz/en/docs/partner-docs/module/)可能正在回覆，或以其他方式對收到的 webhook 事件內容做出反應。在使用者與模組互動期間，從 bot 發送訊息會讓使用者感到困惑。因此，收到 `mode` 屬性為 `standby` 的 webhook 事件的 bot 伺服器，不應發送任何訊息。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start -->

timestamp

Number

事件發生的 UNIX 時間（以毫秒為單位）。即使是重新傳遞（redelivered）的 webhook，它代表的也是事件發生的時間，而非重新傳遞的時間。

<!-- note start -->

**如果啟用 webhook 重新傳遞，請檢查 timestamp**

如果啟用了 [webhook 重新傳遞（webhook redelivery）](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-redelivery)，webhook 事件發生的順序與它們抵達 bot 伺服器的順序可能會有明顯差異。如果這構成問題，請透過查看 `timestamp` 來確認上下文脈絡。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

source

Object

來源[使用者（user）](https://developers.line.biz/en/reference/messaging-api/#source-user)、[群組聊天（group chat）](https://developers.line.biz/en/reference/messaging-api/#source-group)或[多人聊天（multi-person chat）](https://developers.line.biz/en/reference/messaging-api/#source-room)物件，內含事件來源的相關資訊。

如果帳號連動失敗，此屬性將不會包含在[帳號連動事件（account link event）](https://developers.line.biz/en/reference/messaging-api/#account-link-event)中。

<!-- parameter end -->
<!-- parameter start -->

webhookEventId

String

Webhook Event ID。可唯一識別 webhook 事件的 ID。這是一個 ULID 格式的字串。

<!-- parameter end -->
<!-- parameter start -->

deliveryContext.isRedelivery

Boolean

該 webhook 事件是否為重新傳遞的事件。如需更多資訊，請參閱 [Redelivered webhooks](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#redelivered-webhooks)。

- `true`：重新傳遞的 webhook 事件。
- `false`：首次發送的 webhook 事件。

<!-- parameter end -->

#### Source user 

<!-- parameter start -->

type

String

`user`

<!-- parameter end -->
<!-- parameter start -->

userId

String

來源使用者的 ID

<!-- parameter end -->

_來源使用者範例_

<!-- tab start `json` -->

```json
  "source": {
    "type": "user",
    "userId": "U4af4980629..."
  }
```

<!-- tab end -->

#### Source group chat 

<!-- parameter start -->

type

String

`group`

<!-- parameter end -->
<!-- parameter start -->

groupId

String

來源群組聊天的 Group ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

userId

String

來源使用者的 ID。只會包含在[訊息事件（message events）](https://developers.line.biz/en/reference/messaging-api/#message-event)中。只有 LINE for iOS 與 LINE for Android 的使用者會被包含在 `userId` 中。如需更多資訊，請參閱 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。

<!-- parameter end -->

_來源群組聊天範例_

<!-- tab start `json` -->

```json
  "source": {
    "type": "group",
    "groupId": "Ca56f94637c...",
    "userId": "U4af4980629..."
  }
```

<!-- tab end -->

#### Source multi-person chat 

<!-- parameter start -->

type

String

`room`

<!-- parameter end -->
<!-- parameter start -->

roomId

String

來源多人聊天的 Room ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

userId

String

來源使用者的 ID。只會包含在[訊息事件（message events）](https://developers.line.biz/en/reference/messaging-api/#message-event)中。只有 LINE for iOS 與 LINE for Android 的使用者會被包含在 `userId` 中。如需更多資訊，請參閱 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。

<!-- parameter end -->

_來源多人聊天範例_

<!-- tab start `json` -->

```json
  "source": {
    "type": "room",
    "roomId": "Ra8dbf4673c...",
    "userId": "U4af4980629..."
  }
```

<!-- tab end -->

### Message event 

包含使用者所傳送訊息的 webhook event object。`message` 屬性包含與訊息類型對應的訊息物件。你可以回覆訊息事件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`message`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[發送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖

<!-- parameter end -->
<!-- parameter start -->

message

Object

包含訊息內容的物件。訊息類型包括：

- [Text](https://developers.line.biz/en/reference/messaging-api/#wh-text)
- [Image](https://developers.line.biz/en/reference/messaging-api/#wh-image)
- [Video](https://developers.line.biz/en/reference/messaging-api/#wh-video)
- [Audio](https://developers.line.biz/en/reference/messaging-api/#wh-audio)
- [File](https://developers.line.biz/en/reference/messaging-api/#wh-file)
- [Location](https://developers.line.biz/en/reference/messaging-api/#wh-location)
- [Sticker](https://developers.line.biz/en/reference/messaging-api/#wh-sticker)

<!-- parameter end -->

#### Text 

包含來源所傳送文字的訊息物件。

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`text`

<!-- parameter end -->
<!-- parameter start -->

quoteToken

String

訊息的引用權杖（quote token）。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖（read token）。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start -->

text

String

訊息文字。

- 如果終端使用者傳送 LINE 表情貼（LINE emoji），該 LINE 表情貼會以字串形式包含於其中，例如 `(hello)` 或 `(love)`。你可以在 `emojis` 屬性中找到 LINE 表情貼的詳情。
- 如果終端使用者提及（mention）某人，收件者 LINE 帳號的顯示名稱會以字串形式包含於其中，例如 `@example`。你可以在 `mention` 屬性中找到提及的詳情。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

emojis

Array

一個或多個 LINE 表情貼物件的陣列。只有當 `text` 屬性包含 LINE 表情貼時，才會包含於訊息事件中。

<!-- note start -->

**已傳送的 LINE 表情貼可能不會包含在 emojis 屬性中**

- 從 LINE for Android 傳送的預設 LINE 表情貼不會被包含在內。
- Unicode 定義的表情符號與舊版的 LINE 表情貼可能無法正確取得。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start -->

emojis\[].index

Number

`text` 中某個字元的索引位置，第一個字元位於位置 `0`。

<!-- parameter end -->
<!-- parameter start -->

emojis\[].length

Number

LINE 表情貼字串的長度。對於 LINE 表情貼 `(hello)`，長度為 `7`。

<!-- parameter end -->
<!-- parameter start -->

emojis\[].productId

String

LINE 表情貼組合的 Product ID。Product ID 的範例請參閱 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- parameter end -->
<!-- parameter start -->

emojis\[].emojiId

String

某個組合內某個 LINE 表情貼的 ID。emoji ID 的範例請參閱 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

mention

Object

包含被提及使用者內容的物件。只有當 `text` 屬性包含提及時，才會包含於訊息事件中。

<!-- parameter end -->
<!-- parameter start -->

mention.mentionees[]

Array of objects

一個或多個提及物件的陣列。

上限：20 個提及

<!-- parameter end -->
<!-- parameter start -->

mention.mentionees[].index

Number

`text` 中某個字元的使用者提及索引位置，第一個字元位於位置 `0`。

<!-- parameter end -->
<!-- parameter start -->

mention.mentionees[].length

Number

被提及使用者文字的長度。對於提及 `@example`，長度為 8。

<!-- parameter end -->
<!-- parameter start -->

mention.mentionees[].type

String

被提及的目標。

- `user`：使用者或 bot。
- `all`：整個群組。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

mention.mentionees[].userId

String

被提及使用者或 bot 的 user ID。只有當 `mention.mentions[].type` 為 `user` 時才會包含。如果被提及者是使用者，只有在[使用者同意](https://developers.line.biz/en/docs/messaging-api/user-consent/) LINE Official Account 取得其個人檔案資訊時才會包含。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

mention.mentionees[].isSelf

Boolean

該提及是否針對收到 webhook 事件的 bot（`destination`）。只有當 `mention.mentionees[].type` 屬性的值為 `user` 時才會包含。

- `true`：這是對收到 webhook 事件的 bot 的提及。
- `false`：這是對另一位使用者的提及。

如需更多資訊，請參閱 Messaging API 文件中的 [Webhook when a message including a mention to a bot is sent](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-message-with-mention-to-bot)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

quotedMessageId

String

被引用訊息的 Message ID。只有當收到的訊息引用了過去的訊息時才會包含。

<!-- parameter end -->

_文字訊息範例_

<!-- tab start `json` -->

```json
// When a user sends a text message containing mention and an emoji in a group chat
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "group",
        "groupId": "Ca56f94637c...",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "message": {
        "id": "444573844083572737",
        "type": "text",
        "quoteToken": "q3Plxr4AgKd...",
        "markAsReadToken": "30yhdy232...",
        "text": "@All @example Good Morning!! (love)",
        "emojis": [
          {
            "index": 29,
            "length": 6,
            "productId": "5ac1bfd5040ab15980c9b435",
            "emojiId": "001"
          }
        ],
        "mention": {
          "mentionees": [
            {
              "index": 0,
              "length": 4,
              "type": "all"
            },
            {
              "index": 5,
              "length": 8,
              "userId": "U49585cd0d5...",
              "type": "user",
              "isSelf": false
            }
          ]
        }
      }
    }
  ]
}
```

<!-- tab end -->

#### Image 

包含來源所傳送圖片內容的訊息物件。

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`image`

<!-- parameter end -->
<!-- parameter start -->

quoteToken

String

訊息的引用權杖。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start -->

contentProvider.type

String

圖片檔案的提供者。

- `line`：圖片由 LINE 使用者傳送。圖片檔案的二進位資料可透過指定 message ID 並呼叫 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content) 端點來取得。
- `external`：圖片檔案的 URL 包含在 `contentProvider.originalContentUrl` 屬性中。如果圖片檔案的提供者為 `external`，則無法使用 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content) 端點取得圖片檔案的二進位資料。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

contentProvider.originalContentUrl

String

圖片檔案的 URL。只有當 `contentProvider.type` 為 `external` 時才會包含。存放圖片檔案的伺服器並非由 LY Corporation 提供。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

contentProvider.previewImageUrl

String

預覽圖片的 URL。只有當 `contentProvider.type` 為 `external` 時才會包含。存放預覽圖片檔案的伺服器並非由 LY Corporation 提供。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

imageSet.id

String

圖片組合 ID。只有當多張圖片同時傳送時才會包含。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

imageSet.index

Number

從 `1` 開始的索引，表示同時傳送的一組圖片中的圖片編號。只有當多張圖片同時傳送時才會包含。但如果傳送者使用的是 LINE 11.15 或更早的 Android 版本，則不會包含。

<!-- tip start -->

**webhook 的傳遞順序是未定義的**

如果使用者同時傳送多張圖片，LINE Platform 會向 bot 伺服器傳送多個 webhook 事件。這些 webhook 是以未定義的順序傳遞，並非依 `imageSet.index` 值的順序。

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

imageSet.total

Number

同時傳送的圖片總數。如果同時傳送兩張圖片，數字為 `2`。只有當多張圖片同時傳送時才會包含。但如果傳送者使用的是 LINE 11.15 或更早的 Android 版本，則不會包含。

<!-- parameter end -->

_圖片訊息範例_

<!-- tab start `json` -->

```json
// When two images are sent simultaneously (First image)
{
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "message",
            "message": {
                "type": "image",
                "id": "354718705033693859",
                "quoteToken": "q3Plxr4AgKd...",
                "markAsReadToken": "30yhdy232...",
                "contentProvider": {
                    "type": "line"
                },
                "imageSet": {
                    "id": "E005D41A7288F41B65593ED38FF6E9834B046AB36A37921A56BC236F13A91855",
                    "index": 1,
                    "total": 2
                }
            },
            "timestamp": 1627356924513,
            "source": {
                "type": "user",
                "userId": "U4af4980629..."
            },
            "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
            "deliveryContext": {
                "isRedelivery": false
            },
            "replyToken": "7840b71058e24a5d91f9b5726c7512c9",
            "mode": "active"
        }
    ]
}

// When two images are sent simultaneously (Second image)
{
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "message",
            "message": {
                "type": "image",
                "id": "354718705033693861",
                "quoteToken": "yHAz4Ua2wx7...",
                "markAsReadToken": "30yhdy232...",
                "contentProvider": {
                    "type": "line"
                },
                "imageSet": {
                    "id": "E005D41A7288F41B65593ED38FF6E9834B046AB36A37921A56BC236F13A91855",
                    "index": 2,
                    "total": 2
                }
            },
            "timestamp": 1627356924722,
            "source": {
                "type": "user",
                "userId": "U4af4980629..."
            },
            "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
            "deliveryContext": {
                "isRedelivery": false
            },
            "replyToken": "fbf94e269485410da6b7e3a5e33283e8",
            "mode": "active"
        }
    ]
}
```

<!-- tab end -->

#### Video 

包含來源所傳送影片內容的訊息物件。聊天中會顯示預覽圖片，點擊圖片時播放影片。

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`video`

<!-- parameter end -->
<!-- parameter start -->

quoteToken

String

訊息的引用權杖。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

duration

Number

影片檔案的長度（毫秒）

<!-- parameter end -->
<!-- parameter start -->

contentProvider.type

String

影片檔案的提供者。

- `line`：影片由 LINE 使用者傳送。影片檔案的二進位資料可透過指定 message ID 並呼叫 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content) 端點來取得。
- `external`：影片檔案的 URL 包含在 `contentProvider.originalContentUrl` 屬性中。如果影片檔案的提供者為 `external`，則無法使用 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content) 端點取得影片檔案的二進位資料。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

contentProvider.originalContentUrl

String

影片檔案的 URL。只有當 `contentProvider.type` 為 `external` 時才會包含。存放影片檔案的伺服器並非由 LY Corporation 提供。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

contentProvider.previewImageUrl

String

預覽圖片的 URL。只有當 `contentProvider.type` 為 `external` 時才會包含。存放預覽圖片檔案的伺服器並非由 LY Corporation 提供。

<!-- parameter end -->

_影片訊息範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "message": {
        "id": "325708",
        "type": "video",
        "quoteToken": "q3Plxr4AgKd...",
        "markAsReadToken": "30yhdy232...",
        "duration": 60000,
        "contentProvider": {
          "type": "external",
          "originalContentUrl": "https://example.com/original.mp4",
          "previewImageUrl": "https://example.com/preview.jpg"
        }
      }
    }
  ]
}
```

<!-- tab end -->

#### Audio 

包含來源所傳送音訊內容的訊息物件。

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`audio`

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

duration

Number

音訊檔案的長度（毫秒）

<!-- parameter end -->
<!-- parameter start -->

contentProvider.type

String

音訊檔案的提供者：

- `line`：音訊由 LINE 使用者傳送。音訊檔案的二進位資料可透過指定 message ID 並呼叫 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content) 端點來取得。
- `external`：音訊檔案的 URL 包含在 `contentProvider.originalContentUrl` 屬性中。如果音訊檔案的提供者為 `external`，則無法使用 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content) 端點取得音訊檔案的二進位資料。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

contentProvider.originalContentUrl

String

音訊檔案的 URL。只有當 `contentProvider.type` 為 `external` 時才會包含。存放音訊檔案的伺服器並非由 LY Corporation 提供。

<!-- parameter end -->

_音訊訊息範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "message": {
        "id": "325708",
        "type": "audio",
        "markAsReadToken": "30yhdy232...",
        "duration": 60000,
        "contentProvider": {
          "type": "line"
        }
      }
    }
  ]
}
```

<!-- tab end -->

#### File 

包含來源所傳送檔案的訊息物件。檔案的二進位資料可透過指定 message ID 並呼叫 API 來取得。如需更多資訊，請參閱 [Get content](https://developers.line.biz/en/reference/messaging-api/#get-content)。

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`file`

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start -->

fileName

String

檔案名稱

<!-- parameter end -->
<!-- parameter start -->

fileSize

Number

檔案大小（位元組）

<!-- parameter end -->

_檔案訊息範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "message": {
        "id": "325708",
        "type": "file",
        "markAsReadToken": "30yhdy232...",
        "fileName": "file.txt",
        "fileSize": 2138
      }
    }
  ]
}
```

<!-- tab end -->

#### Location 

包含來源所傳送位置資料的訊息物件。

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`location`

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

title

String

標題

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

address

String

地址

<!-- parameter end -->
<!-- parameter start -->

latitude

Decimal

緯度

<!-- parameter end -->
<!-- parameter start -->

longitude

Decimal

經度

<!-- parameter end -->

_位置訊息範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "message",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "message": {
        "id": "325708",
        "type": "location",
        "markAsReadToken": "30yhdy232...",
        "title": "my location",
        "address": "1-3 Kioicho, Chiyoda-ku, Tokyo, 102-8282 Japan",
        "latitude": 35.67966,
        "longitude": 139.73669
      }
    }
  ]
}
```

<!-- tab end -->

#### Sticker 

包含來源所傳送貼圖資料的訊息物件。基本 LINE 貼圖與貼圖 ID 的清單，請參閱 [Stickers](https://developers.line.biz/en/docs/messaging-api/sticker-list/)。

<!-- tip start -->

**你無法取得貼圖圖片**

使用者所傳送貼圖的 package ID 與 sticker ID 可透過 webhook 取得，但貼圖圖片本身無法取得。

<!-- tip end -->

<!-- tip start -->

**不支援貼圖排列（Sticker Arranging）功能**

Messaging API 目前不支援貼圖排列（Sticker Arranging）功能，因此你無法取得關於組合了哪些貼圖的資訊。當使用者使用貼圖排列功能傳送貼圖訊息時，webhook 一律會收到以下貼圖資訊。

- Package ID：`30563`
- Sticker ID：`651698630`
- 貼圖資源類型：`STATIC`

<!-- tip end -->

<!-- parameter start -->

id

String

Message ID

<!-- parameter end -->
<!-- parameter start -->

type

String

`sticker`

<!-- parameter end -->
<!-- parameter start -->

quoteToken

String

訊息的引用權杖。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->
<!-- parameter start -->

markAsReadToken

String

已讀權杖。此權杖可讓你將訊息標記為已讀。它沒有到期日。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

<!-- parameter end -->
<!-- parameter start -->

packageId

String

Package ID

<!-- parameter end -->
<!-- parameter start -->

stickerId

String

Sticker ID

<!-- parameter end -->
<!-- parameter start -->

stickerResourceType

String

貼圖資源類型。以下其中之一：

- `STATIC`：靜態圖片
- `ANIMATION`：動態貼圖
- `SOUND`：附音效貼圖
- `ANIMATION_SOUND`：附音效的動態貼圖
- `POPUP`：彈出式貼圖或特效貼圖
- `POPUP_SOUND`：附音效的彈出式貼圖或附音效的特效貼圖
- `CUSTOM`：自訂貼圖。無法取得使用者輸入的文字。
- `MESSAGE`：訊息貼圖
- `NAME_TEXT`：自訂貼圖（已停用）
- `PER_STICKER_TEXT`：訊息貼圖（已停用）

<!-- note start -->

**關於 stickerResourceType**

未來我們可能會在不另行通知的情況下新增資源類型。請確保你的實作能同時處理目前與未來的貼圖資源類型。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

keywords

Array of strings

描述貼圖的關鍵字陣列，最多 15 個。如果某個貼圖有 16 個以上的關鍵字，則會回傳隨機選取的 15 個關鍵字。關鍵字的選取在每次事件中都是隨機的，因此同一個貼圖可能會回傳不同的關鍵字。

<!-- note start -->

**關於 keywords**

`keywords` 屬性目前處於實驗階段，未來可能會發生停用或規格變更。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

text

String

使用者輸入的任何文字。此屬性只會包含在訊息貼圖中。\
字元數上限：100

<!-- tip start -->

**你無法取得自訂貼圖的文字**

在自訂貼圖的情況下，無法取得使用者輸入的文字。

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

quotedMessageId

String

被引用訊息的 Message ID。只有當收到的訊息引用了過去的訊息時才會包含。

<!-- parameter end -->

_貼圖訊息範例_

<!-- tab start `json` -->

```json
// Example of animated sticker
{
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
            "type": "message",
            "mode": "active",
            "timestamp": 1462629479859,
            "source": {
                "type": "user",
                "userId": "U4af4980629..."
            },
            "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
            "deliveryContext": {
                "isRedelivery": false
            },
            "message": {
                "type": "sticker",
                "id": "1501597916",
                "quoteToken": "q3Plxr4AgKd...",
                "markAsReadToken": "30yhdy232...",
                "stickerId": "52002738",
                "packageId": "11537",
                "stickerResourceType": "ANIMATION",
                "keywords": [
                    "cony",
                    "sally",
                    "Staring",
                    "hi",
                    "whatsup",
                    "line",
                    "howdy",
                    "HEY",
                    "Peeking",
                    "wave",
                    "peek",
                    "Hello",
                    "yo",
                    "greetings"
                ]
            }
        }
    ]
}

// Example of message sticker
{
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "type": "message",
            "message": {
                "type": "sticker",
                "id": "123456789012345678",
                "quoteToken": "q3Plxr4AgKd...",
                "markAsReadToken": "30yhdy232...",
                "stickerId": "738839",
                "packageId": "12287",
                "stickerResourceType": "MESSAGE",
                "keywords": [
                    "Anticipation",
                    "Sparkle",
                    "Straight face",
                    "Staring",
                    "Thinking"
                ],
                "text": "Let's\nhang out\nthis weekend!"
            },
            "timestamp": 1635756190879,
            "source": {
                "type": "group",
                "groupId": "C99ae82bcd...",
                "userId": "Ub82c8fd9b..."
            },
            "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
            "deliveryContext": {
                "isRedelivery": false
            },
            "replyToken": "ce8c57ec18374a4b94f40abab97145f8",
            "mode": "active"
        }
    ]
}
```

<!-- tab end -->
### Unsend event 

訊息收回事件（unsend）發生時的事件物件。

當使用者收回（unsend）已傳送的訊息時，會傳送一個收回事件到 bot 伺服器。收到收回事件時，我們建議服務供應商尊重使用者收回已傳送訊息的意圖，並以最謹慎的態度妥善處理該訊息，使目標訊息日後無法被看見或使用。詳情請參閱 Messaging API 文件中的 [Processing on receipt of unsend event](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-unsend-message)。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`unsend`

<!-- parameter end -->
<!-- parameter start -->

unsend.messageId

String

被收回訊息的訊息 ID

<!-- parameter end -->

_收回事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "unsend",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "group",
        "groupId": "Ca56f94637c...",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "unsend": {
        "messageId": "325708"
      }
    }
  ]
}
```

<!-- tab end -->

### Follow event 

當你的 LINE 官方帳號被加為好友（或被解除封鎖）時的事件物件。你可以回覆 follow 事件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`follow`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->
<!-- parameter start -->

follow.isUnblocked

Boolean

- `true`：使用者解除了對該 LINE 官方帳號的封鎖。
- `false`：使用者將該 LINE 官方帳號加為好友。

<!-- note start -->

**follow.isUnblocked 的準確性**

`follow.isUnblocked` 屬性無法保證「加為好友」與「解除封鎖」的完全準確性。

<!-- note end -->

<!-- parameter end -->

_Follow 事件範例_

<!-- tab start `json` -->

```json
// When the user has added the LINE Official Account as a friend
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "85cbe770fa8b4f45bbe077b1d4be4a36",
      "type": "follow",
      "mode": "active",
      "timestamp": 1705891467176,
      "source": {
        "type": "user",
        "userId": "U3d3edab4f36c6292e6d8a8131f141b8b"
      },
      "webhookEventId": "01HMQGW40RZJPJM3RAJP7BHC2Q",
      "deliveryContext": {
        "isRedelivery": false
      },
      "follow": {
        "isUnblocked": false
      }
    }
  ]
}

// When the user has unblocked the LINE Official Account
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "follow",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "follow": {
        "isUnblocked": true
      }
    }
  ]
}
```

<!-- tab end -->

### Unfollow event 

當你的 LINE 官方帳號被封鎖時的事件物件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`unfollow`

<!-- parameter end -->

_Unfollow 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "unfollow",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      }
    }
  ]
}
```

<!-- tab end -->

### Join event 

當你的 LINE 官方帳號加入[群組聊天（group chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#group)或[多人聊天（multi-person chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#room)時的事件物件。你可以回覆 join 事件。

join 事件在群組聊天與多人聊天中觸發的時機不同。

- 群組聊天：當使用者邀請你的 LINE 官方帳號時，會傳送 join 事件。
- 多人聊天：在你的 LINE 官方帳號被加入後，當第一個事件發生（例如使用者傳送訊息或被加入該多人聊天）時，會傳送 join 事件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`join`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->

_Join 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "join",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "group",
        "groupId": "C4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      }
    }
  ]
}
```

<!-- tab end -->

### Leave event 

當使用者將你的 LINE 官方帳號從[群組聊天（group chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#group)中移除，或當你的 LINE 官方帳號離開[群組聊天（group chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#group)或[多人聊天（multi-person chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#room)時的事件物件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`leave`

<!-- parameter end -->

_Leave 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "leave",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "group",
        "groupId": "C4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      }
    }
  ]
}
```

<!-- tab end -->

### Member join event 

當有使用者加入該 LINE 官方帳號所在的[群組聊天（group chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#group)或[多人聊天（multi-person chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#room)時的事件物件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`memberJoined`

<!-- parameter end -->
<!-- parameter start -->

joined.members

Array

加入的使用者。為[來源使用者（source user）](https://developers.line.biz/en/reference/messaging-api/#source-user)物件的陣列。

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->

_Member join 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "0f3779fba3b349968c5d07db31eabf65",
      "type": "memberJoined",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "group",
        "groupId": "C4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "joined": {
        "members": [
          {
            "type": "user",
            "userId": "U4af4980629..."
          },
          {
            "type": "user",
            "userId": "U91eeaf62d9..."
          }
        ]
      }
    }
  ]
}
```

<!-- tab end -->

### Member leave event 

當有使用者離開該 LINE 官方帳號所在的[群組聊天（group chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#group)或[多人聊天（multi-person chat）](https://developers.line.biz/en/docs/messaging-api/group-chats/#room)時的事件物件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`memberLeft`

<!-- parameter end -->
<!-- parameter start -->

left.members

Array

離開的使用者。為[來源使用者（source user）](https://developers.line.biz/en/reference/messaging-api/#source-user)物件的陣列。

<!-- parameter end -->

_Member leave 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "memberLeft",
      "mode": "active",
      "timestamp": 1462629479960,
      "source": {
        "type": "group",
        "groupId": "C4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "left": {
        "members": [
          {
            "type": "user",
            "userId": "U4af4980629..."
          },
          {
            "type": "user",
            "userId": "U91eeaf62d9..."
          }
        ]
      }
    }
  ]
}
```

<!-- tab end -->

### Postback event 

當使用者執行會觸發 postback 的 [postback 動作（postback action）](https://developers.line.biz/en/reference/messaging-api/#postback-action)時的事件物件。你可以回覆 postback 事件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`postback`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->
<!-- parameter start -->

postback.data

String

Postback 資料

<!-- parameter end -->
<!-- parameter start -->

[postback.params](https://developers.line.biz/en/reference/messaging-api/#postback-params-object)

Object

以下任一 JSON 物件：

- [date-time 選擇動作的 `postback.params` 物件](https://developers.line.biz/en/reference/messaging-api/#postback-params-object)。
  - 包含使用者透過 [Datetime picker 動作](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)所選擇的日期與時間的 JSON 物件。
  - 僅針對由 [Datetime picker 動作](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)觸發的 postback 動作回傳。
- [rich menu 切換動作的 `postback.params` 物件](https://developers.line.biz/en/reference/messaging-api/#postback-params-object-for-richmenu-switch-action)。
  - 包含使用者透過 [Rich menu 切換動作](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)所選擇的 rich menu 別名 ID 的 JSON 物件。
  - 僅針對由 [Rich menu 切換動作](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)觸發的 postback 動作回傳。

<!-- parameter end -->

_Postback 事件範例_

<!-- tab start `json` -->

```json
// Postback event for date-time selection action
{
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "replyToken": "b60d432864f44d079f6d8efe86cf404b",
            "type": "postback",
            "mode": "active",
            "source": {
                "userId": "U91eeaf62d...",
                "type": "user"
            },
            "timestamp": 1513669370317,
            "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
            "deliveryContext": {
                "isRedelivery": false
            },
            "postback": {
                "data": "storeId=12345",
                "params": {
                    "datetime": "2017-12-25T01:00"
                }
            }
        }
    ]
}

// Postback event for rich menu switch action
{
    "destination": "xxxxxxxxxx",
    "events": [
        {
            "replyToken": "b60d432864f44d079f6d8efe86cf404b",
            "type": "postback",
            "mode": "active",
            "source": {
                "userId": "U91eeaf62d...",
                "type": "user"
            },
            "timestamp": 1619754620404,
            "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
            "deliveryContext": {
                "isRedelivery": false
            },
            "postback": {
                "data": "richmenu-changed-to-b",
                "params": {
                    "newRichMenuAliasId": "richmenu-alias-b",
                    "status": "SUCCESS"
                }
            }
        }
    ]
}
```

<!-- tab end -->

#### `postback.params` object for date-time selection action 

包含使用者透過 [datetime picker 動作](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)所選擇的日期與時間的物件。`full-date`、`time-hour` 與 `time-minute` 格式遵循 [RFC3339 協定](https://www.ietf.org/rfc/rfc3339.txt)。

| Property | Format | Description |
| --- | --- | --- |
| date | full-date | 使用者所選的日期。僅在 `date` 模式中包含。 |
| time | time-hour ":" time-minute | 使用者所選的時間。僅在 `time` 模式中包含。 |
| datetime | full-date "T" time-hour ":" time-minute | 使用者所選的日期與時間。僅在 `datetime` 模式中包含。 |

_date-time 選擇動作的 postback.params 物件範例_

<!-- tab start `json` -->

```json
{
  "datetime": "2017-12-25T01:00"
}
```

<!-- tab end -->

#### `postback.params`object for rich menu switch action 

包含使用者透過 [rich menu 切換動作](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)所選擇的 rich menu 別名 ID 的物件。

| Property | Format | Description |
| --- | --- | --- |
| newRichMenuAliasId 不一定會包含 | String | 要切換到的 rich menu 別名 ID。若 rich menu 切換失敗，將不會包含此屬性。 |
| status | String | `SUCCESS`：rich menu 切換成功。<br/> `RICHMENU_ALIAS_ID_NOTFOUND`：找不到指定的 rich menu 別名 ID。<br/>`RICHMENU_NOTFOUND`：找不到與指定 rich menu 別名 ID 關聯的 rich menu ID。<br/>`FAILED`：rich menu 切換失敗。 |

_rich menu 切換動作的 postback.params 物件範例_

<!-- tab start `json` -->

```json
{
  "newRichMenuAliasId": "richmenu-alias-b",
  "status": "SUCCESS"
}
```

<!-- tab end -->

### Video viewing complete event 

當使用者至少完整觀看一次由 LINE 官方帳號傳送、且帶有指定 `trackingId` 的影片時所觸發的事件。

<!-- note start -->

**影片觀看次數**

影片觀看完成事件不一定代表使用者觀看影片的次數。

在同一個聊天室的單一工作階段（session）中多次觀看影片並不會產生重複的事件。然而，若你關閉聊天室再重新開啟以再次觀看影片，該事件可能會再次發生。

<!-- note end -->

<!-- note start -->

**imagemap 訊息與 flex 訊息中的影片不支援影片觀看完成事件**

[imagemap 訊息](https://developers.line.biz/en/reference/messaging-api/#imagemap-message)與 [flex 訊息](https://developers.line.biz/en/reference/messaging-api/#flex-message)中的影片無法指定 `trackingId`。

<!-- note end -->

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`videoPlayComplete`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->
<!-- parameter start -->

videoPlayComplete.trackingId

String

用於識別影片的 ID。回傳值與指派給[影片訊息（video message）](https://developers.line.biz/en/reference/messaging-api/#video-message)的 `trackingId` 相同。

<!-- parameter end -->

_影片觀看完成事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "videoPlayComplete",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "videoPlayComplete": {
        "trackingId": "track-id"
      }
    }
  ]
}
```

<!-- tab end -->

### Beacon event 

當使用者進入 [LINE Beacon](https://developers.line.biz/en/docs/messaging-api/using-beacons/) 的接收範圍時的事件物件。你可以回覆 beacon 事件。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`beacon`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->
<!-- parameter start -->

beacon.hwid

String

被偵測到的 beacon 的硬體 ID

<!-- parameter end -->
<!-- parameter start -->

beacon.type

String

Beacon 事件的類型。請參閱 [Beacon event types](https://developers.line.biz/en/reference/messaging-api/#beacon-event-types)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

beacon.dm

String

被偵測到的 beacon 的裝置訊息（device message）。此訊息由 beacon 產生的資料組成，用於向 bot 伺服器傳送通知。僅在來自支援「device message」屬性裝置的 webhook 事件中包含。\
詳情請參閱 [LINE Simple Beacon 規格](https://github.com/line/line-simple-beacon/blob/master/README.en.md#line-simple-beacon-frame)。

<!-- parameter end -->

_Beacon 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "beacon",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "beacon": {
        "hwid": "d41d8cd98f",
        "type": "enter"
      }
    }
  ]
}
```

<!-- tab end -->

#### Beacon event types 

| beacon.type | Description |
| --- | --- |
| `enter` | 進入 beacon 的接收範圍。 |
| `banner` | 點按了 [beacon 橫幅](https://developers.line.biz/en/docs/messaging-api/using-beacons/#beacon-banner)。 |
| `stay` | 使用者位於 beacon 的接收範圍內。<br />此事件會以最短 10 秒的間隔重複傳送。 |

<!-- note start -->

**日本已暫停註冊**

自 2021 年 1 月起，我們在日本已不再接受 `banner` 與 `stay` 事件的新申請，而日本以外的其他地區仍接受新申請。

<!-- note end -->

### Account link event 

當使用者將其 LINE 帳號與供應商的服務帳號連結時的事件物件。你可以回覆 account link 事件。

若連結權杖（link token）已過期或已被使用，則不會傳送任何 webhook 事件，且使用者會看到錯誤訊息。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

若帳號連結失敗，account link 事件中將不會包含 `source` 屬性。

<!-- parameter end -->
<!-- parameter start -->

type

String

`accountLink`

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）。若帳號連結失敗，將不會包含此屬性。

<!-- parameter end -->
<!-- parameter start -->

link.result

String

以下其中一個值，用於表示帳號連結是否成功：

- `ok`：表示帳號連結成功。
- `failed`：表示帳號連結因任何原因（例如使用者冒用身分）而失敗。

<!-- parameter end -->
<!-- parameter start -->

link.nonce

String

驗證使用者 ID 時所指定的 nonce（僅使用一次的數字）。詳情請參閱 Messaging API 文件中的 [Generate a nonce and redirect the user to the LINE Platform](https://developers.line.biz/en/docs/messaging-api/linking-accounts/#step-four-verifying-user-id)。

<!-- parameter end -->

_Account link 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "b60d432864f44d079f6d8efe86cf404b",
      "type": "accountLink",
      "mode": "active",
      "source": {
        "userId": "U91eeaf62d...",
        "type": "user"
      },
      "timestamp": 1513669370317,
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "link": {
        "result": "ok",
        "nonce": "xxxxxxxxxxxxxxx"
      }
    }
  ]
}
```

<!-- tab end -->

### Membership event 

此事件表示使用者加入、續訂或退出了你的 LINE 官方帳號的會員資格（membership）。

若你的 LINE 官方帳號提供多種會員方案，且目前加入某一方案的使用者在同一個月內變更為另一個方案，則會同時針對退出與加入傳送 webhook 事件。若使用者尚未同意允許存取其個人資料資訊，則不會傳送任何 webhook 事件。詳情請參閱 Messaging API 文件中的 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。

<!-- parameter start -->

timestamp、source 等

請參閱 [Common properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

type

String

`membership`

<!-- parameter end -->
<!-- parameter start -->

replyToken

String

用於對此事件[傳送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）

<!-- parameter end -->
<!-- parameter start -->

membership.type

String

會員事件的類型。以下其中一個值：

- `joined`：使用者加入了會員資格。
- `left`：使用者退出了會員資格。
- `renewed`：使用者續訂了會員資格。

<!-- parameter end -->
<!-- parameter start -->

membership.membershipId

Number

使用者所加入、退出或續訂的會員 ID。

<!-- parameter end -->

_Membership 事件範例_

<!-- tab start `json` -->

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "type": "membership",
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "membership": {
        "type": "joined",
        "membershipId": 3189
      },
      "timestamp": 1462629479859,
      "mode": "active",
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      }
    }
  ]
}
```

<!-- tab end -->

## Webhook settings 

你可以設定、測試並取得頻道（channel）webhook 端點（endpoint）的相關資訊。

### Set webhook endpoint URL 

端點：`PUT` `https://api.line.me/v2/bot/channel/webhook/endpoint`

設定 webhook 端點 URL。由於快取的關係，變更最多可能需要 1 分鐘才會生效。

<!-- note start -->

**Webhook URL 驗證規則**

請確保符合以下 webhook URL 驗證規則：

- 輸入有效的 HTTPS URL。
- 必須為 500 個字元以下。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -X PUT \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-H 'Content-Type:application/json' \
-d '{"endpoint":"https://example.com/hoge"}' \
https://api.line.me/v2/bot/channel/webhook/endpoint
```

<!-- tab end -->

#### Rate limit 

每分鐘 1,000 次請求

關於速率限制的詳情，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

endpoint

String

有效的 webhook URL。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的 webhook 端點 URL。 |

詳情請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid webhook endpoint URL (400 Bad Request)
{
  "message": "Invalid webhook endpoint URL"
}
```

<!-- tab end -->

### Get webhook endpoint information 

端點：`GET` `https://api.line.me/v2/bot/channel/webhook/endpoint`

取得 webhook 端點的相關資訊。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -X GET \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-H 'Content-Type:application/json' \
https://api.line.me/v2/bot/channel/webhook/endpoint
```

<!-- tab end -->

#### Rate limit 

每分鐘 1,000 次請求

關於速率限制的詳情，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個包含以下資訊的 JSON 物件。

<!-- parameter start -->

endpoint

String

Webhook URL

<!-- parameter end -->
<!-- parameter start -->

active

Boolean

Webhook 使用狀態。只有在啟用時，LINE Platform 才會將 webhook 事件傳送至 webhook URL。

- `true`：webhook 使用已啟用。
- `false`：webhook 使用已停用。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
// If the webhook URL was set and the webhook usage is enabled
{
  "endpoint": "https://example.com/test",
  "active": true
}

// If the webhook URL was set and the webhook usage is disabled
{
  "endpoint": "https://example.com/test",
  "active": false
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `404` | 該頻道未設定 webhook URL。 |

詳情請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If the webhook URL isn't set (404 Not Found)
{
  "message": "Webhook endpoint not found"
}
```

<!-- tab end -->

### Test webhook endpoint 

端點：`POST` `https://api.line.me/v2/bot/channel/webhook/test`

檢查所設定的 webhook 端點是否能接收測試用的 webhook 事件。

<!-- note start -->

**Webhook URL 驗證規則**

請確保符合以下 webhook URL 驗證規則：

- 輸入有效的 HTTPS URL。
- 必須為 500 個字元以下。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
# To verify a specified URL
curl -X POST \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-H 'Content-Type:application/json' \
-d '{"endpoint":"https://example.com/webhook"}' \
https://api.line.me/v2/bot/channel/webhook/test

# To verify the URL set in the "Webhook URL" section of the LINE Developers Console
curl -X POST \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-H 'Content-Type:application/json' \
-d '{}' \
https://api.line.me/v2/bot/channel/webhook/test
```

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

關於速率限制的詳情，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: optional) -->

endpoint

String

要進行驗證的 webhook URL。

<!-- note start -->

**有無 endpoint 參數時的行為差異**

此 API 端點的行為會依 **Request body** 中是否包含 `endpoint` 參數而有所不同。

**有 endpoint 參數時**

驗證 `endpoint` 參數中指定的端點 URL 是否有效，若有效，則向指定的端點 URL 傳送測試用的 webhook 事件。

**無 endpoint 參數時**

向已設定於該頻道的 webhook 端點傳送測試用的 webhook 事件。若該頻道未設定 webhook 端點，則回傳 `404`。

<!-- note end -->

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個包含以下資訊的 JSON 物件。

<!-- note start -->

**對通訊請求回傳狀態碼 200**

- LINE Platform 會向 webhook URL（bot 伺服器）傳送一個不包含 webhook 事件的 HTTP POST 請求以確認通訊。請將你的 bot 伺服器設計為回傳狀態碼 `200`。

  不包含 webhook 事件的 HTTP POST 請求範例：

  ```json
  {
    "destination": "xxxxxxxxxx",
    "events": []
  }
  ```

<!-- note end -->

<!-- parameter start -->

success

Boolean

從 LINE Platform 到 webhook URL 的通訊結果。

- `true`：成功
- `false`：失敗

若為 `false`，請參閱 Messaging API 文件中的 [Check the reason for errors](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#check-error-reason)。

<!-- parameter end -->
<!-- parameter start -->

timestamp

String

請參閱 [Common Properties](https://developers.line.biz/en/reference/messaging-api/#common-properties)。

<!-- parameter end -->
<!-- parameter start -->

statusCode

Number

HTTP 狀態碼。若未收到 webhook 回應，則狀態碼會被設為零或負數。

<!-- parameter end -->
<!-- parameter start -->

reason

String

回應的原因。詳情請參閱下方表格。

<!-- parameter end -->
<!-- parameter start -->

detail

String

回應的細節。詳情請參閱下方表格。

<!-- parameter end -->

| `reason` | `detail` | Description |
| --- | --- | --- |
| OK | HTTP 狀態碼（例如 `200`） | 成功傳送 webhook。 |
| [COULD_NOT_CONNECT](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-could-not-connect) | 連線失敗 | 無法連線至 webhook 端點。詳情請參閱 Messaging API 文件中的 [The reason is could_not_connect](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-could-not-connect)。 |
| [REQUEST_TIMEOUT](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-request-timeout) | 請求逾時 | 請求逾時。詳情請參閱 Messaging API 文件中的 [The reason is request_timeout](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-request-timeout)。 |
| [ERROR_STATUS_CODE](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-status-code) | HTTP 狀態碼（例如 `400`） | HTTP 狀態碼錯誤回應。詳情請參閱 Messaging API 文件中的 [The reason is error_status_code](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-status-code)。 |
| [UNCLASSIFIED](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-unclassified) | N/A | 未知錯誤。詳情請參閱 Messaging API 文件中的 [The reason is unclassified](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-unclassified)。 |

_回應範例（若 webhook 成功傳送）_

<!-- tab start `json` -->

```json
{
  "success": true,
  "timestamp": "2020-09-30T05:38:20.031Z",
  "statusCode": 200,
  "reason": "OK",
  "detail": "200"
}
```

<!-- tab end -->

_回應範例（若因 bot 伺服器的 SSL/TLS 設定導致與 webhook URL 的通訊失敗）_

<!-- tab start `json` -->

```json
{
  "success": false,
  "timestamp": "2023-07-07T04:29:51.043124Z",
  "statusCode": 0,
  "reason": "COULD_NOT_CONNECT",
  "detail": "TLS handshake failure: https://example.com/webhook"
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                               |
| ----- | ----------------------------------------- |
| `400` | 指定了無效的 webhook URL。      |
| `404` | 該頻道未設定 webhook URL。 |

詳情請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If the domain name specified in the Webhook URL can't be resolved (400 Bad Request)
{
  "message": "Invalid webhook endpoint URL"
}

// If the webhook URL isn't set (404 Not Found)
{
  "message": "Webhook endpoint not found"
}
```

<!-- tab end -->

## Getting content 

你可以使用透過 [webhook](https://developers.line.biz/en/reference/messaging-api/#webhooks) 接收到的訊息 ID，取得使用者傳送給你的 LINE 官方帳號的內容。

### Get content 

端點：`GET` `https://api-data.line.me/v2/bot/message/{messageId}/content`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 中傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

使用透過 webhook 接收到的訊息 ID，取得使用者傳送的[圖片](https://developers.line.biz/en/reference/messaging-api/#wh-image)、[影片](https://developers.line.biz/en/reference/messaging-api/#wh-video)、[音訊](https://developers.line.biz/en/reference/messaging-api/#wh-audio)與[檔案](https://developers.line.biz/en/reference/messaging-api/#wh-file)。

只有在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `contentProvider.type` 屬性為 `line` 時，此端點才可使用。

當使用者傳送大型影片或音訊檔案時，可能需要一段時間才能完成內容二進位資料的準備。若你在二進位資料準備期間嘗試取得內容，會回傳狀態碼 `202` 且無法取得二進位資料。你可以使用 [Verify the preparation status of a video or audio for getting](https://developers.line.biz/en/reference/messaging-api/#verify-video-or-audio-preparation-status) 端點來驗證是否可取得二進位資料。

使用者傳送的內容可能會在內部經過轉換，例如縮小。

<!-- note start -->

**沒有用於擷取文字的 API**

你可以透過 webhook 的 [text](https://developers.line.biz/en/reference/messaging-api/#wh-text) 訊息物件取得使用者傳送的文字。在收到 webhook 後，並沒有 API 可再次取得使用者傳送的文字。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api-data.line.me/v2/bot/message/{messageId}/content \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

messageId

訊息 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與二進位格式的內容。二進位資料的檔案格式會標示在回應的 [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) 標頭中。

內容會在訊息傳送後經過一段時間自動刪除。內容的儲存時間長短無任何保證。

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

- `404 Not Found`
- `410 Gone`

詳情請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a non-existent message ID (404 Not Found)
{
  "message": "not found"
}

// If the user unsends a message (410 Gone)
{
  "message": "The content is gone"
}
```

<!-- tab end -->
### Verify the preparation status of a video or audio for getting 

端點：`GET` `https://api-data.line.me/v2/bot/message/{messageId}/content/transcoding`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 上傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

使用透過 webhook 收到的訊息 ID，取得準備狀態，以便取得使用者傳送的[影片](https://developers.line.biz/en/reference/messaging-api/#wh-video)或[語音](https://developers.line.biz/en/reference/messaging-api/#wh-audio)。

此端點僅在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `contentProvider.type` 屬性為 `line` 時可用。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api-data.line.me/v2/bot/message/{messageId}/content/transcoding \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

messageId

[影片](https://developers.line.biz/en/reference/messaging-api/#wh-video)或[語音](https://developers.line.biz/en/reference/messaging-api/#wh-audio)的訊息 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

status

String

準備狀態。為下列其中之一：

- `processing`：正在準備取得內容。
- `succeeded`：可取得內容。你可以[取得內容](https://developers.line.biz/en/reference/messaging-api/#get-content)（使用者傳送的內容）。
- `failed`：準備取得內容失敗。

<!-- parameter end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應（response）：

- `400 Bad Request`
- `404 Not Found`
- `410 Gone`

詳情請參閱[共通規格](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的[狀態碼](https://developers.line.biz/en/reference/messaging-api/#status-codes)與[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a message ID other than video or audio (400 Bad Request)
{
  "message": "Transcoding status doesn't support this type of content"
}

// If you specify a non-existent message ID (404 Not Found)
{
  "message": "not found"
}

// If the user unsends a message (410 Gone)
{
  "message": "The content is gone"
}
```

<!-- tab end -->

### Get a preview image of the image or video 

端點：`GET` `https://api-data.line.me/v2/bot/message/{messageId}/content/preview`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 上傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

使用透過 webhook 收到的訊息 ID，取得使用者傳送的[圖片](https://developers.line.biz/en/reference/messaging-api/#wh-image)或[影片](https://developers.line.biz/en/reference/messaging-api/#wh-video)的預覽圖片。預覽圖片是將原始內容轉換為較小資料量的圖片資料。

此端點僅在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `contentProvider.type` 屬性為 `line` 時可用。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api-data.line.me/v2/bot/message/{messageId}/content/preview \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

messageId

[圖片](https://developers.line.biz/en/reference/messaging-api/#wh-image)或[影片](https://developers.line.biz/en/reference/messaging-api/#wh-video)的訊息 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及二進位格式的預覽圖片。

預覽圖片會在訊息傳送後經過一段時間自動刪除。對於預覽圖片儲存多久並無保證。

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

- `400 Bad Request`
- `404 Not Found`
- `410 Gone`

詳情請參閱[共通規格](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的[狀態碼](https://developers.line.biz/en/reference/messaging-api/#status-codes)與[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a message ID other than image or video (400 Bad Request)
{
  "message": "The content can not be previewed"
}

// If you specify a non-existent message ID (404 Not Found)
{
  "message": "not found"
}

// If the user unsends a message (410 Gone)
{
  "message": "The content is gone"
}
```

<!-- tab end -->

## Channel access token 

你可以發行、取得或撤銷（revoke）從應用程式呼叫 Messaging API 時所需的頻道存取權杖（channel access token）。詳情請參閱 LINE Platform basics 中的 [Channel access token](https://developers.line.biz/en/docs/basics/channel-access-token/)。

### Issue channel access token v2.1 

端點：`POST` `https://api.line.me/oauth2/v2.1/token`

發行頻道存取權杖，可讓你指定想要的有效期間。此方法讓你能使用 JWT assertion 進行驗證。

channel access token v2.1 每個頻道最多可發行 30 個權杖。若達到上限，後續發行頻道存取權杖的請求將被封鎖。已過期的頻道存取權杖不計入已發行數量。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
--data-urlencode 'client_assertion={JWT}'
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

`client_credentials`

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_assertion_type

String

`urn:ietf:params:oauth:client-assertion-type:jwt-bearer` 的 URL 編碼值

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_assertion

String

指定一個 JSON Web Token assertion，此 assertion 必須由用戶端產生，並以 assertion 簽署金鑰的私鑰簽署。

JWT assertion 必須設定為在產生後 30 分鐘內過期。關於產生 JWT assertion 的詳情，請參閱 [Generate a JWT](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#generate-jwt)。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

access_token

String

頻道存取權杖。

<!-- parameter end -->
<!-- parameter start -->

expires_in

Number

從頻道存取權杖發行到過期的時間量（以秒為單位）

<!-- parameter end -->
<!-- parameter start -->

token_type

String

`Bearer`

<!-- parameter end -->
<!-- parameter start -->

key_id

String

用於識別頻道存取權杖的唯一金鑰 ID。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "access_token": "eyJhbGciOiJIUz.....",
  "token_type": "Bearer",
  "expires_in": 2592000,
  "key_id": "sDTOzw5wIfxxxxPEzcmeQA"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>JWT assertion 驗證失敗。</li><li>JWT assertion 已過期。</li><li>已達到可發行的頻道存取權杖數量上限。</li></ul> |
| `404` | 與 JWT assertion 關聯的簽署金鑰未在頻道中註冊。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// When the maximum number of channel access tokens that can be issued is reached (400 Bad Request)
{
  "message": "The maximum number of access tokens has already been issued"
}

// If the JWT assertion verification fails (400 Bad Request)
{
  "error": "invalid_client",
  "error_description": "iss and clientId of key do not match"
}

// If the signature key associated with the JWT assertion isn't registered in the channel (404 Not Found)
{
  "message": "Cannot find channel key that satisfies the conditions"
}
```

<!-- tab end -->

### Verify the validity of the channel access token v2.1 

端點：`GET` `https://api.line.me/oauth2/v2.1/verify`

你可以驗證[使用者自訂有效期間的頻道存取權杖（Channel Access Token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)是否有效。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/oauth2/v2.1/verify \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'access_token=eyJhbGciOiJIUzI1NiJ9.UnQ_o-GP0VtnwDjbK0C8E_NvK...' \
-G
```

<!-- tab end -->

#### Query parameter 

<!-- parameter start (props: required) -->

access_token

使用者自訂有效期間的頻道存取權杖（Channel Access Token v2.1）。

<!-- parameter end -->

#### Response 

若頻道存取權杖有效，回傳 `200` HTTP 狀態碼以及包含此資訊的 JSON 物件。

<!-- parameter start -->

client_id

String

發行此頻道存取權杖所對應的頻道 ID。

<!-- parameter end -->
<!-- parameter start -->

expires_in

Number

頻道存取權杖過期前的秒數。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

scope

String

授予頻道存取權杖的權限。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "client_id": "1573163733",
  "expires_in": 2591659,
  "scope": "profile chat_message.write"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>指定了格式無效的頻道存取權杖。</li><li>頻道存取權杖已過期。</li><li>指定了不存在的頻道存取權杖。</li></ul> |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If the channel access token has expired (400 Bad Request)
{
    "error": "invalid_request",
    "error_description": "The access token expired"
}

// If you specify an invalidly formatted channel access token (400 Bad Request)
{
    "error": "invalid_request",
    "error_description": "The access token not JWS"
}
```

<!-- tab end -->

### Get all valid channel access token key IDs v2.1 

端點：`GET` `https://api.line.me/oauth2/v2.1/tokens/kid`

取得所有有效的頻道存取權杖金鑰 ID。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -X GET https://api.line.me/oauth2/v2.1/tokens/kid \
--data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
--data-urlencode 'client_assertion={JWT}' \
-G
```

<!-- tab end -->

#### Query parameters 

<!-- parameter start (props: required) -->

client_assertion_type

String

`urn:ietf:params:oauth:client-assertion-type:jwt-bearer` 的 URL 編碼值

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_assertion

String

用戶端需要建立並以私鑰簽署的 [JSON Web Token (JWT)](https://datatracker.ietf.org/doc/html/rfc7519)。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及包含此資訊的 JSON 物件。

<!-- parameter start -->

kids

Array of strings

頻道存取權杖金鑰 ID 的陣列（array）。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "kids": [
    "U_gdnFYKTWRxxxxDVZexGg",
    "sDTOzw5wIfWxxxxzcmeQA",
    "73hDyp3PxGfxxxxD6U5qYA",
    "FHGanaP79smDxxxxyPrVw",
    "CguB-0kxxxxdSM3A5Q_UtQ",
    "G82YP96jhHwyKSxxxx7IFA"
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>JWT assertion 驗證失敗。</li><li>JWT assertion 已過期。</li></ul> |
| `404` | 與 JWT assertion 關聯的簽署金鑰未在頻道中註冊。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If the JWT assertion has expired (400 Bad Request)
{
  "error": "invalid_client",
  "error_description": "Invalid exp"
}

// If the signature key associated with the JWT assertion isn't registered in the channel (404 Not Found)
{
  "message": "Cannot find channel key that satisfies the conditions"
}
```

<!-- tab end -->

### Revoke channel access token v2.1 

端點：`POST` `https://api.line.me/oauth2/v2.1/revoke`

撤銷 channel access token v2.1。

在下列情況下撤銷頻道存取權杖：

- 因為已重新發行頻道存取權杖，舊的頻道存取權杖不再需要時
- 懷疑頻道存取權杖已遭外洩時

無須撤銷已過期的頻道存取權杖。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/oauth2/v2.1/revoke \
--data-urlencode 'client_id={channel ID}' \
--data-urlencode 'client_secret={channel secret}' \
--data-urlencode 'access_token={access token}'
```

<!-- tab end -->

#### Request body 

<!-- parameter start (props: required) -->

client_id

String

頻道 ID

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_secret

String

頻道密鑰（Channel Secret）

<!-- parameter end -->
<!-- parameter start (props: required) -->

access_token

String

頻道存取權杖

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及空的回應內文（response body）。

<!-- note start -->

**Note**

若指定了無效的頻道存取權杖，不會發生錯誤。

<!-- note end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>指定了格式無效的頻道存取權杖。</li><li>指定了不存在的頻道存取權杖。</li><li>指定了格式錯誤的頻道存取。</li></ul> |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalidly formatted channel access token (400 Bad Request)
{
  "error": "invalid_request",
  "error_description": "The access token not JWS"
}

// If you specify a malformed channel access (400 Bad Request)
{
  "error": "invalid_request",
  "error_description": "The access token malformed"
}
```

<!-- tab end -->

### Issue stateless channel access token 

端點：`POST` `https://api.line.me/oauth2/v3/token`

發行僅有效 15 分鐘的頻道存取權杖。可發行的權杖數量沒有限制。一旦發行 stateless channel access token，便無法撤銷。

_從 channel ID 與 channel secret 發行的請求範例_

<code-tabs class="mb-8">
<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/oauth2/v3/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_id={channel ID}' \
--data-urlencode 'client_secret={channel secret}'
```

<!-- tab end -->

_從 JWT assertion 發行的請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/oauth2/v3/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_assertion_type=urn:ietf:params:oauth:client-assertion-type:jwt-bearer' \
--data-urlencode 'client_assertion={JWT assertion}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

發行 stateless channel access token 有兩種方式。無論使用哪一種方式，回應內文的格式都相同：

- [從 channel ID 與 channel secret 發行](https://developers.line.biz/en/reference/messaging-api/#issue-stateless-channel-access-token-request-body-channel-id)
- [從 JWT assertion 發行](https://developers.line.biz/en/reference/messaging-api/#issue-stateless-channel-access-token-request-body-jwt)

##### Issue from channel ID and channel secret 

<!-- parameter start (props: required) -->

grant_type

String

`client_credentials`

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_id

String

頻道 ID。可在 [LINE Developers Console](https://developers.line.biz/console/) 上找到。

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_secret

String

頻道密鑰。可在 [LINE Developers Console](https://developers.line.biz/console/) 上找到。

<!-- parameter end -->

##### Issue from JWT assertion 

<!-- parameter start (props: required) -->

grant_type

String

`client_credentials`

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_assertion_type

String

`urn:ietf:params:oauth:client-assertion-type:jwt-bearer` 的 URL 編碼值

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_assertion

String

指定一個 JSON Web Token assertion，此 assertion 必須由用戶端產生，並以 assertion 簽署金鑰的私鑰簽署。

JWT assertion 必須設定為在產生後 30 分鐘內過期。關於產生 JWT assertion 的詳情，請參閱 [Generate a JWT](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#generate-jwt)。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

token_type

String

`Bearer`

<!-- parameter end -->
<!-- parameter start -->

access_token

String

頻道存取權杖

<!-- parameter end -->
<!-- parameter start -->

expires_in

Number

從頻道存取權杖發行到過期之間的秒數

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "token_type": "Bearer",
  "access_token": "ey....",
  "expires_in": 900
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>指定了無效的頻道 ID。</li><li>指定了無效的頻道密鑰。</li><li>JWT assertion 驗證失敗。</li><li>JWT assertion 已過期。</li></ul> |
| `404` | 與 JWT assertion 關聯的簽署金鑰未在頻道中註冊。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid channel secret (400 Bad Request)
{
  "error": "invalid_request",
  "error_description": "Invalid 'client_credentials'."
}

// If the signature key associated with the JWT assertion isn't registered in the channel (404 Not Found)
{
  "message": "Cannot find channel key that satisfies the conditions"
}
```

<!-- tab end -->

### Issue short-lived channel access token 

端點：`POST` `https://api.line.me/v2/oauth/accessToken`

發行有效期為 30 天的短期頻道存取權杖（short-lived channel access token）。

短期頻道存取權杖每個頻道最多可發行 30 個權杖。若超過上限，最舊的現有頻道存取權杖將被撤銷。已過期的頻道存取權杖不計入已發行數量。

<!-- tip start -->

**Tip**

- 對於 Messaging API 頻道，你可以發行長期頻道存取權杖、使用者自訂有效期間的頻道存取權杖（channel access token v2.1），或 stateless channel access token。詳情請參閱 LINE Platform basics 中的 [Channel access token](https://developers.line.biz/en/docs/basics/channel-access-token/)。
- LINE Login 頻道的頻道存取權杖也可使用此 API 發行。LINE Login 頻道的頻道存取權杖可在 [LIFF Server API](https://developers.line.biz/en/reference/liff-server/) 中使用。

<!-- tip end -->

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/accessToken \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'grant_type=client_credentials' \
--data-urlencode 'client_id={channel ID}' \
--data-urlencode 'client_secret={channel secret}'
```

<!-- tab end -->

#### Rate limit 

每秒 370 次請求

關於速率限制的詳情，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

grant_type

String

`client_credentials`

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_id

String

頻道 ID。可在 [LINE Developers Console](https://developers.line.biz/console/) 上找到。

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_secret

String

頻道密鑰。可在 [LINE Developers Console](https://developers.line.biz/console/) 上找到。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

access_token

String

短期頻道存取權杖。有效期為 30 天。

<!-- note start -->

**Note**

頻道存取權杖無法重新整理（refresh）。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start -->

expires_in

Number

從權杖發行起到頻道存取權杖過期的時間（以秒為單位）

<!-- parameter end -->
<!-- parameter start -->

token_type

String

`Bearer`

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "access_token": "W1TeHCgfH2Liwa.....",
  "expires_in": 2592000,
  "token_type": "Bearer"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>指定了無效的頻道 ID。</li><li>指定了無效的頻道密鑰。</li><li>請求參數格式錯誤。</li></ul> |
| `429` | 超過[速率限制](https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token-rate-limit)。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid channel ID (400 Bad Request)
{
  "error": "invalid_client",
  "error_description": "invalid client_id"
}

// If you specify an invalid channel secret (400 Bad Request)
{
  "error": "invalid_client",
  "error_description": "invalid client_secret"
}
```

<!-- tab end -->

### Verify the validity of short-lived and long-lived channel access tokens 

端點：`POST` `https://api.line.me/v2/oauth/verify`

你可以驗證[短期頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)或[長期頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)是否有效。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/verify \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'access_token=bNl4YEFPI/hjFWhTqexp4MuEw5YPs7qhr6dJDXKwNPuLka...'
```

<!-- tab end -->

#### Request header 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

access_token

String

短期或長期頻道存取權杖。

<!-- parameter end -->

#### Response 

若頻道存取權杖有效，回傳 `200` HTTP 狀態碼以及包含此資訊的 JSON 物件。

<!-- parameter start -->

client_id

String

發行此頻道存取權杖所對應的頻道 ID。

<!-- parameter end -->
<!-- parameter start -->

expires_in

Number

頻道存取權杖過期前的秒數。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

scope

String

授予頻道存取權杖的權限。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "client_id": "1350031035",
  "expires_in": 3138007490,
  "scope": "P CM"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。考慮下列原因：<ul><li>指定了無效的頻道存取權杖。</li><li>指定了格式無效的頻道存取權杖。</li><li>頻道存取權杖已過期。</li></ul> |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid channel access (400 Bad Request)
{
    "error": "invalid_request",
    "error_description": "access_token invalid"
}

// If you specify an invalidly formatted channel access token (400 Bad Request)
{
    "error": "invalid_request",
    "error_description": "access_token in invalid format"
}
```

<!-- tab end -->

### Revoke short-lived or long-lived channel access token 

端點：`POST` `https://api.line.me/v2/oauth/revoke`

撤銷短期或長期頻道存取權杖。

在下列情況下撤銷頻道存取權杖：

- 因為已重新發行頻道存取權杖，舊的頻道存取權杖不再需要時
- 懷疑頻道存取權杖已遭外洩時

無須撤銷已過期的頻道存取權杖。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/oauth/revoke \
-H "Content-Type: application/x-www-form-urlencoded" \
--data-urlencode 'access_token={channel access token}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/x-www-form-urlencoded

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

access_token

String

頻道存取權杖

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及空的回應內文。若指定了無效的頻道存取權杖，不會發生錯誤。

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code  | Description                                               |
| ----- | --------------------------------------------------------- |
| `400` | 指定了格式無效的頻道存取權杖。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalidly formatted channel access token (400 Bad Request)
{
  "error": "invalid_request"
}
```

<!-- tab end -->

## Message 

你可以傳送訊息並取得已傳送訊息的相關資訊。

### Send reply message 

端點：`POST` `https://api.line.me/v2/bot/message/reply`

回應來自使用者、群組聊天或多人聊天的事件，傳送回覆訊息。若要傳送回覆訊息，你需要 reply token，它包含在 webhook 事件物件中。

當事件發生時，你會透過 [webhook](https://developers.line.biz/en/reference/messaging-api/#webhooks) 收到通知。若該事件可被回應，便會發行 reply token。

<!-- tip start -->

**你可以在準備回覆訊息時顯示載入動畫**

當你的 LINE Official Account 收到使用者的訊息後，由於訊息準備或預約處理，回應可能需要一些時間。在這種情況下，你可以透過顯示載入動畫，以視覺方式告訴使用者你希望他們稍候。詳情請參閱 Messaging API 文件中的 [Display a loading animation](https://developers.line.biz/en/docs/messaging-api/use-loading-indicator/)。

<!-- tip end -->

#### Reply token 

使用 reply token 時，請確認下列事項：

- Reply token 只能使用一次。
- Reply token 必須在收到 webhook 後一分鐘內使用。超過一分鐘的使用不保證有效。
- 重新傳遞的 webhook 中所含的 reply token 也可在收到重新傳遞的 webhook 後一分鐘內使用。但在下列情況下無法使用此 reply token：
  - 原始 webhook 中所含的 reply token 已被使用。
  - 自事件發生起已經過 20 分鐘。

<!-- note start -->

**Reply token 應盡快使用**

Reply token 的時間限制可能在不另行通知的情況下變更。此外，實際可使用的時間長度可能因網路延遲及其他因素而有所不同。

因此，請勿在實作上依賴此時間限制。同時，請盡快使用 reply token。

<!-- note end -->

_範例請求_

<!-- tab start `shell` -->

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

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

關於速率限制的詳情，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

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

replyToken

String

透過 webhook 收到的 reply token

<!-- parameter end -->
<!-- parameter start (props: required) -->

messages

[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)的陣列

要傳送的訊息\
上限：5

你可以使用 [Validate message objects of a reply message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-reply-message) 端點來驗證訊息物件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

notificationDisabled

Boolean

- `true`：訊息傳送時，使用者不會收到推播通知。
- `false`：訊息傳送時，使用者會收到推播通知（除非他們已在 LINE 及／或其裝置上停用推播通知）。

預設值：`false`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

sentMessages

Array

已傳送訊息的陣列。<br />上限：5

<!-- parameter end -->
<!-- parameter start -->

sentMessages.id

Number

已傳送訊息的 ID。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

sentMessages.quoteToken

String

訊息的 quote token。僅在可被指定為引用目標的訊息物件以回覆訊息方式傳送時才會包含。詳情請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "sentMessages": [
    {
      "id": "461230966842064897",
      "quoteToken": "IStG5h1Tz7b..."
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法傳送訊息。考慮下列原因：<ul><li>指定了無效的 reply token。</li><li>指定了無效的訊息物件。</li></ul> |

詳情請參閱[共通規格](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的[狀態碼](https://developers.line.biz/en/reference/messaging-api/#status-codes)與[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

若回傳錯誤，則不會傳送訊息。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid reply token such as expired or used (400 Bad Request)
{
  "message": "Invalid reply token"
}
```

<!-- tab end -->

### Send push message 

端點：`POST` `https://api.line.me/v2/bot/message/push`

隨時向使用者、群組聊天或多人聊天傳送訊息。

#### Conditions for sending push message 

你可以在符合下列其中一項條件時傳送推播訊息：

- 已將你的 LINE Official Account 加為好友的使用者
- 你的 LINE Official Account 已加入的群組聊天或多人聊天
- 在一對一聊天中於 7 天內曾向你的 LINE Official Account 傳送訊息的使用者（\*）

當你向下列使用者傳送推播訊息時，會回傳狀態碼 `200`，但使用者不會收到訊息：

- 已刪除其 LINE 帳號的使用者
- 已封鎖傳送該推播訊息之 LINE Official Account 的使用者
- 尚未將你的 LINE Official Account 加為好友的使用者（\*）

\*使用者也可以向尚未加為好友的 LINE Official Account 傳送訊息。若你的 LINE Official Account 在一對一聊天中收到尚未成為你好友的使用者所傳送的訊息，你可以在收到訊息後 7 天內向該使用者傳送推播訊息。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'X-Line-Retry-Key: {UUID}' \
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

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

關於速率限制的詳情，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

X-Line-Retry-Key

重試金鑰。以十六進位格式指定 UUID（例如 123e4567-e89b-12d3-a456-426614174000），可用任何方法產生。重試金鑰並非由 LINE 產生。每位開發者必須自行產生重試金鑰。詳情請參閱 Messaging API 文件中的 [Retry failed API requests](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

to

String

目標收件者的 ID。使用 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#common-properties)中回傳的 `userId`、`groupId` 或 `roomId` 值。

<!-- parameter end -->
<!-- parameter start (props: required) -->

messages

[訊息物件（message objects）](https://developers.line.biz/en/reference/messaging-api/#message-objects)的陣列

要傳送的訊息\
上限：5

你可以使用 [Validate message objects of a push message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-push-message) 端點來驗證訊息物件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

notificationDisabled

Boolean

- `true`：訊息傳送時，使用者不會收到推播通知。
- `false`：訊息傳送時，使用者會收到推播通知（除非他們已在 LINE 及／或其裝置上停用推播通知）。

預設值：`false`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

customAggregationUnits

Array of strings

統計單位（aggregation unit）的名稱。區分大小寫。例如，`Promotion_a` 與 `Promotion_A` 會被視為不同的單位名稱。\
最大單位數：1\
最大字元上限：30\
支援的字元類型：半形英數字元（`a-z`、`A-Z`、`0-9`）與底線（`_`）

關於指派單位名稱的詳情，請參閱 Messaging API 文件中的 [Assign a unit name](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/#assign-names-to-units-when-sending-messages)。

<!-- note start -->

**單位名稱可能未被指派**

在當月期間（從當月 1 日到最後一天），你最多可以使用 1,000 個不同的單位名稱傳送訊息。若你嘗試指派第 1,001 個或之後的單位名稱，訊息仍會被傳送。但該單位名稱不會被指派。

若你有許多種單位名稱，請使用下列其中一種方法確認單位名稱可被指派或已被指派：

- 在傳送訊息前，使用 [Get the number of unit name types assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-the-number-of-unit-name-types-assigned-during-this-month) 端點確認當月的單位名稱數量尚未達到 1,000
- 在傳送訊息後，使用 [Get a list of unit names assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-a-list-of-unit-names-assigned-during-this-month) 端點確認已指派的單位名稱存在

<!-- note end -->

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

sentMessages

Array

已傳送訊息的陣列。<br />上限：5

<!-- parameter end -->
<!-- parameter start -->

sentMessages.id

Number

已傳送訊息的 ID。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

sentMessages.quoteToken

String

訊息的 quote token。僅在可被指定為引用目標的訊息物件以推播訊息方式傳送時才會包含。詳情請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "sentMessages": [
    {
      "id": "461230966842064897",
      "quoteToken": "IStG5h1Tz7b..."
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法傳送訊息。考慮下列原因：<ul><li>指定了此頻道中不存在的使用者 ID，例如從其他 provider 下的頻道取得的使用者 ID。</li><li>指定了不存在的群組，或你的 LINE Official Account 並未參與的群組。</li><li>指定了不存在的多人聊天，或你的 LINE Official Account 並未參與的多人聊天。</li><li>指定了無效的訊息物件。</li></ul> |
| `409` | 含有相同重試金鑰的請求已被接受。詳情請參閱 Retrying an API request 中的 [Response if the request has already been accepted](https://developers.line.biz/en/reference/messaging-api/#retry-api-request-response)。 |
| `429` | 請求數量已超過限制。考慮下列原因：<ul><li>超過此端點的[速率限制](https://developers.line.biz/en/reference/messaging-api/#send-push-message-rate-limit)。</li><li>向同一使用者傳送了大量訊息。</li><li>超過[當月傳送訊息的目標上限](https://developers.line.biz/en/reference/messaging-api/#get-quota)。</li></ul>關於傳送訊息目標上限的詳情，請參閱 Messaging API 文件中的 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。 |

詳情請參閱[共通規格](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的[狀態碼](https://developers.line.biz/en/reference/messaging-api/#status-codes)與[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

若回傳錯誤，則不會傳送訊息。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you failed to send a message (400 Bad Request)
{
  "message": "Failed to send messages"
}
```

<!-- tab end -->
### Send multicast message 

端點（endpoint）：`POST` `https://api.line.me/v2/bot/message/multicast`

可有效率地將同一則訊息傳送給多個使用者 ID 的 API。你無法將訊息傳送至群組聊天或多人聊天。

你也可以將 multicast 訊息傳送給單一使用者。不過，當收件者只有一位使用者時，我們建議使用 [push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message)。Push message 適合用於以低延遲為目的傳送訊息。

#### Conditions for sending multicast message 

你可以將 multicast 訊息傳送給已將你的 LINE 官方帳號加為好友的使用者。

當你將 multicast 訊息傳送給以下這些使用者時，會回傳狀態碼 `200`，但這些使用者不會收到訊息：

- 已刪除 LINE 帳號的使用者
- 已封鎖傳送該 multicast 訊息的 LINE 官方帳號的使用者
- 尚未將你的 LINE 官方帳號加為好友的使用者
- 不存在於該頻道（channel）中的使用者 ID，例如從另一個 provider 下的其他頻道取得的使用者 ID

_請求（request）範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/multicast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'X-Line-Retry-Key: {UUID}' \
-d '{
    "to": ["U4af4980629...","U0c229f96c4..."],
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

#### Rate limit 

每秒 200 次請求

如需更多關於速率限制（rate limit）的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

X-Line-Retry-Key

重試金鑰（retry key）。指定以任何方法產生的十六進位格式 UUID（例如 123e4567-e89b-12d3-a456-426614174000）。重試金鑰並非由 LINE 產生。每位開發者都必須產生自己的重試金鑰。如需更多資訊，請參閱 Messaging API 文件中的 [Retry failed API requests](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

to

字串陣列（Array of strings）

使用者 ID 的陣列（array）。請使用 [webhook event objects](https://developers.line.biz/en/reference/messaging-api/#common-properties) 中回傳的 `userId` 值。請勿使用在 LINE 上找到的 LINE ID。\
上限：500 個使用者 ID

<!-- parameter end -->
<!-- parameter start (props: required) -->

messages

[message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 的陣列

要傳送的訊息\
上限：5

藉由使用 [Validate message objects of a multicast message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-multicast-message) 端點，你可以驗證訊息物件（message object）。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

notificationDisabled

布林值（Boolean）

- `true`：傳送訊息時，使用者不會收到推播通知。
- `false`：傳送訊息時，使用者會收到推播通知（除非他們在 LINE 及／或其裝置上停用了推播通知）。

預設值：`false`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

customAggregationUnits

字串陣列（Array of strings）

彙總單位（aggregation unit）的名稱。區分大小寫。例如，`Promotion_a` 與 `Promotion_A` 會被視為不同的單位名稱。\
單位數量上限：1\
字元數上限：30\
支援的字元類型：半形英數字元（`a-z`、`A-Z`、`0-9`）與底線（`_`）

如需更多關於指派單位名稱的資訊，請參閱 Messaging API 文件中的 [Assign a unit name](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/#assign-names-to-units-when-sending-messages)。

<!-- note start -->

**單位名稱可能無法被指派**

在當月期間（從每月 1 號到當月最後一天），你最多可以使用 1,000 個不同的單位名稱來傳送訊息。如果你嘗試指派第 1,001 個或之後的單位名稱，訊息仍會被傳送，但單位名稱不會被指派。

如果你有許多種類的單位名稱，請使用以下其中一種方法確認單位名稱是否可以被指派或已被指派：

- 在傳送訊息之前，使用 [Get the number of unit name types assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-the-number-of-unit-name-types-assigned-during-this-month) 端點，確認當月的單位名稱數量尚未達到 1,000 個
- 在傳送訊息之後，使用 [Get a list of unit names assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-a-list-of-unit-names-assigned-during-this-month) 端點，確認所指派的單位名稱存在

<!-- note end -->

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應（response）範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法傳送訊息。可考慮以下原因：<ul><li>指定了不存在於此頻道中的使用者 ID，例如從其他 provider 下的頻道取得的使用者 ID。</li><li>指定了非使用者 ID，例如群組 ID。</li><li>指定了無效的訊息物件。</li></ul> |
| `409` | 已接受包含相同重試金鑰的請求。如需更多資訊，請參閱 Retrying an API request 中的 [Response if the request has already been accepted](https://developers.line.biz/en/reference/messaging-api/#retry-api-request-response)。 |
| `429` | 請求數量已超過上限。可考慮以下原因：<ul><li>超過此端點的[速率限制](https://developers.line.biz/en/reference/messaging-api/#send-multicast-rate-limit)。</li><li>超過[本月可傳送訊息的目標上限](https://developers.line.biz/en/reference/messaging-api/#get-quota)。</li></ul>如需更多關於可傳送訊息目標上限的資訊，請參閱 Messaging API 文件中的 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

如果回傳錯誤，訊息不會傳送給任何使用者。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If your request contains invalid parameters（400 Bad Request）
{
  "message": "The property, to[1], in the request body is invalid (line: -, column: -)"
}
```

<!-- tab end -->

### Send narrowcast message 

端點：`POST` `https://api.line.me/v2/bot/message/narrowcast`

將訊息傳送給多個使用者。你可以使用屬性（例如年齡、性別、OS 與地區）指定收件者，或藉由再行銷（受眾，audiences）指定收件者。訊息無法傳送至群組聊天或多人聊天。

在 LINE Platform 收到請求之後，narrowcast 訊息會在背景以非同步方式傳送。因此，即使傳送 narrowcast 訊息的請求成功，一旦訊息開始遞送時仍可能發生失敗。你可以藉由[取得 narrowcast 訊息的進度](https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status)來確認訊息是否成功傳送。

<!-- note start -->

**關於將 narrowcast 訊息傳送給泰國未滿 20 歲的使用者**

當你以特定條件篩選收件者時，泰國未滿 20 歲的使用者將被排除。

<!-- note end -->

#### Conditions for sending narrowcast message 

你可以將 narrowcast 訊息傳送給已將你的 LINE 官方帳號加為好友的使用者。

如果你將 narrowcast 訊息傳送給以下這些使用者，會回傳狀態碼 `202`，但這些使用者將被排除於收件者之外：

- 已刪除 LINE 帳號的使用者
- 已封鎖你的 LINE 官方帳號的使用者
- 尚未將你的 LINE 官方帳號加為好友的使用者
- 不存在於該頻道中的使用者 ID，例如從另一個 provider 下的其他頻道取得的使用者 ID

#### Restrictions on sending messages using attributes and audiences 

使用屬性或受眾時，為了保護使用者隱私，可能會依據傳送條件對所傳送的訊息套用限制。如果所傳送的訊息符合這些限制，在傳送請求或遞送訊息時將會發生錯誤。

- 若要指定屬性資料作為傳送條件，你的 LINE 官方帳號的[目標可觸及人數（target reach）](https://developers.line.biz/en/glossary/#target-reach)必須為 100 人以上。如果你的目標可觸及人數少於 100 人，會回傳 `403` HTTP 狀態碼。
- 當你指定屬性資料或受眾（\*）作為傳送條件時，最終的收件者數量必須為 50 人以上。如果最終收件者數量少於 50 人，仍會回傳 `202` HTTP 狀態碼，但在訊息遞送開始時將會發生錯誤。
- 當你指定多個受眾作為傳送條件時，每個受眾（\*）必須至少有 50 名收件者。如果該受眾的收件者少於 50 人，仍會回傳 `202` HTTP 狀態碼，但在訊息遞送開始時將會發生錯誤。

\* 以下受眾在收件者數量方面沒有限制。不過，對於由其他 LINE 官方帳號建立的受眾，即使是以下這些受眾也會套用該限制：

- 透過從 LINE Official Account Manager 或 Messaging API 上傳使用者 ID 所建立的受眾
- 聊天標籤受眾（chat tag audiences）

#### Note regarding the number of remaining messages to be sent during the current month 

在 LINE Official Account Manager 與 Messaging API 中，在開始傳送訊息後、要傳送的訊息數量確定之前，預定要傳送的訊息數量會從剩餘訊息數量中保留下來。如果在訊息遞送開始時無法保留預定要傳送的訊息數量，訊息將遞送失敗。

無論實際收件者數量為何，narrowcast 訊息都需要為 LINE 官方帳號的目標可觸及人數保留額度。因此，傳送 narrowcast 訊息時，請注意以下事項：

- 如果當月剩餘可傳送的訊息數量少於你的 LINE 官方帳號的目標可觸及人數，在開始遞送 narrowcast 訊息時將會發生錯誤。
- 即使實際收件者數量足夠少，當月剩餘訊息數量仍可能暫時耗盡。如果在 narrowcast 訊息正在遞送時又傳送另一則訊息，將回傳訊息為 `You have reached your monthly limit.` 的 `429 Too Many Requests` 錯誤，且訊息遞送將失敗。

你也許可以藉由在傳送 narrowcast 訊息時限制要傳送的訊息數量來避免這些情況。如需更多資訊，請參閱 [Request body](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-request-body) 上的 [Limit objects](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-limit)。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/narrowcast \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-H 'X-Line-Retry-Key: {UUID}' \
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
                    "type": "audience",
                    "audienceGroupId": 4389303728991
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

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

X-Line-Retry-Key

重試金鑰。指定以任何方法產生的十六進位格式 UUID（例如 123e4567-e89b-12d3-a456-426614174000）。重試金鑰並非由 LINE 產生。每位開發者都必須產生自己的重試金鑰。如需更多資訊，請參閱 Messaging API 文件中的 [Retry failed API requests](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

[message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 的陣列

要傳送的訊息\
上限：5

藉由使用 [Validate message objects of a narrowcast message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-narrowcast-message) 端點，你可以驗證訊息物件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

recipient

物件（Object）

[Recipient object](https://developers.line.biz/en/reference/messaging-api/#narrowcast-recipient)。你最多可以使用合計 10 個受眾與先前傳送的 narrowcast 訊息的請求 ID 來指定訊息收件者。你可以指定的 operator object 數量沒有上限。\
如果省略此項，訊息將傳送給所有已將你的 LINE 官方帳號加為好友的使用者。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

filter.demographic

物件

[Demographic filter object](https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter)。你可以使用好友的屬性來篩選收件者清單。\
如果省略此項，訊息會傳送給所有人，包括屬性值為「unknown」的使用者。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

limit

物件

[Limit object](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-limit)。你可以設定可傳送的 narrowcast 訊息最大數量的上限。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

notificationDisabled

布林值

- `true`：傳送訊息時，使用者不會收到推播通知。
- `false`：傳送訊息時，使用者會收到推播通知（除非他們在 LINE 及／或其裝置上停用了推播通知）。

預設值：`false`

<!-- parameter end -->

##### Recipient objects 

Recipient object 代表受眾物件（audience object）或再遞送物件（redelivery object）。你可以使用邏輯運算子物件（logical operator object）依據條件組合來指定收件者。每個請求最多可以指定合計 10 個受眾物件與再遞送物件。

###### Audience objects 

<!-- parameter start (props: required) -->

type

字串（String）

`audience`

<!-- parameter end -->
<!-- parameter start (props: required) -->

audienceGroupId

數字（Number）

受眾 ID。請使用 [manage audience](https://developers.line.biz/en/reference/messaging-api/#manage-audience-group) API 建立受眾。

<!-- parameter end -->

###### Redelivery object 

<!-- parameter start (props: required) -->

type

字串

`redelivery`

<!-- parameter end -->
<!-- parameter start (props: required) -->

requestId

字串

先前傳送的 narrowcast 訊息的請求 ID。請求 ID 是為每個 Messaging API 請求發出的 ID。它包含於[回應標頭（response header）](https://developers.line.biz/en/reference/messaging-api/#response-headers)中。

<!-- parameter end -->

<!-- note start -->

**指定請求 ID 的條件**

在 `requestId` 屬性中指定的請求 ID 必須符合以下所有條件。如果你指定的請求 ID 不符合這些條件，將回傳 `400` HTTP 狀態碼。

- 該請求 ID 是由遞送 narrowcast 訊息所發出的。
- 該 narrowcast 訊息是在 [Get narrowcast message status](https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status-response) API 端點的 `acceptedTime` 中所顯示的時間戳記起算未滿 14 天（336 小時）內遞送的。
- 遞送程序已完成（[Get narrowcast message status](https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status-response) API 端點回應中的 `phase` 屬性值為 `succeeded`）。

<!-- note end -->

###### Logical operator objects 

使用邏輯 AND、OR 與 NOT 運算子，將多個 recipient object 組合在一起。

<!-- parameter start (props: required) -->

type

字串

`operator`

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

and

recipient object 的陣列

藉由取所指定 recipient object 陣列的邏輯交集（AND）來建立一個新的 recipient object。

![Audience 1 and Audience 2](https://developers.line.biz/media/messaging-api/narrowcast-message/operator_object_for_reference_and_en.png)

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

or

recipient object 的陣列

藉由取所指定 recipient object 陣列的邏輯聯集（OR）來建立一個新的 recipient object。

![Audience 1 or Audience 2](https://developers.line.biz/media/messaging-api/narrowcast-message/operator_object_for_reference_or_en.png)

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

not

recipient object

建立一個排除所指定 recipient object 的新 recipient object。

![not Audience 2](https://developers.line.biz/media/messaging-api/narrowcast-message/operator_object_for_reference_not_en.png)

<!-- parameter end -->

\* 請務必只指定這三個屬性（`and`、`or` 或 `not`）其中之一。你不能指定空陣列。

_recipient object 範例_

<!-- tab start `json` -->

```json
{
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

<!-- tab end -->

##### Demographic filter objects 

Demographic filter object 代表用於篩選收件者清單的條件（例如年齡、性別、OS、地區與好友關係期間）。你可以使用邏輯運算子物件，依據不同條件的組合來篩選收件者。

<!-- note start -->

**使用屬性資料**

- 用於 demographic filter 的屬性資料約為 3 天前的資料（可能更早或更晚）。
- 如果你未指定任何屬性，訊息會傳送給所有人，甚至包括屬性值為「unknown」的使用者。
- 若要使用屬性資料，你的[「目標可觸及人數」](https://developers.line.biz/en/glossary/#target-reach)必須為 100 人以上。
  - 如果你的目標可觸及人數少於 100，會回傳 `403` HTTP 狀態碼。

<!-- note end -->

###### Gender 

<!-- parameter start (props: required) -->

type

字串

`gender`

<!-- parameter end -->
<!-- parameter start (props: required) -->

oneOf

字串陣列

將訊息傳送給特定性別的使用者。以下其中之一：

- `male`
- `female`

<!-- parameter end -->

###### Age 

這讓你可以篩選特定年齡範圍的收件者。

<!-- parameter start (props: required) -->

type

字串

`age`

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

gte

字串

將訊息傳送給至少達到指定年齡的使用者。

你可以指定以下其中一個值。不過，請指定一個小於 `lt` 屬性所指定值的數值。

- `age_15`
- `age_20`
- `age_25`
- `age_30`
- `age_35`
- `age_40`
- `age_45`
- `age_50`
- `age_55`
- `age_60`
- `age_65`
- `age_70`

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

lt

字串

將訊息傳送給比指定年齡更年輕的使用者。

你可以指定以下其中一個值。不過，請指定一個大於 `gte` 屬性所指定值的數值。

- `age_15`
- `age_20`
- `age_25`
- `age_30`
- `age_35`
- `age_40`
- `age_45`
- `age_50`
- `age_55`
- `age_60`
- `age_65`
- `age_70`

<!-- parameter end -->

\* 請務必指定 `gte`、`lt` 或兩者皆指定。

###### Operating system 

<!-- parameter start (props: required) -->

type

字串

`appType`

<!-- parameter end -->
<!-- parameter start (props: required) -->

oneOf

字串陣列

將訊息傳送給使用指定 OS 的使用者。以下其中之一：

- `ios`
- `android`

<!-- parameter end -->

###### Region 

<!-- parameter start (props: required) -->

type

字串

`area`

<!-- parameter end -->
<!-- parameter start (props: required) -->

oneOf

字串陣列

將訊息傳送給指定地區的使用者。以下其中之一：\
**日本 // JP (country code=392)**

- `jp_01`: 北海道 // Hokkaido
- `jp_02`: 青森県 // Aomori
- `jp_03`: 岩手県 // Iwate
- `jp_04`: 宮城県 // Miyagi
- `jp_05`: 秋田県 // Akita
- `jp_06`: 山形県 // Yamagata
- `jp_07`: 福島県 // Fukushima
- `jp_08`: 茨城県 // Ibaraki
- `jp_09`: 栃木県 // Tochigi
- `jp_10`: 群馬県 // Gunma
- `jp_11`: 埼玉県 // Saitama
- `jp_12`: 千葉県 // Chiba
- `jp_13`: 東京都 // Tokyo
- `jp_14`: 神奈川県 // Kanagawa
- `jp_15`: 新潟県 // Niigata
- `jp_16`: 富山県 // Toyama
- `jp_17`: 石川県 // Ishikawa
- `jp_18`: 福井県 // Fukui
- `jp_19`: 山梨県 // Yamanashi
- `jp_20`: 長野県 // Nagano
- `jp_21`: 岐阜県 // Gifu
- `jp_22`: 静岡県 // Shizuoka
- `jp_23`: 愛知県 // Aichi
- `jp_24`: 三重県 // Mie
- `jp_25`: 滋賀県 // Shiga
- `jp_26`: 京都府 // Kyoto
- `jp_27`: 大阪府 // Osaka
- `jp_28`: 兵庫県 // Hyougo
- `jp_29`: 奈良県 // Nara
- `jp_30`: 和歌山県 // Wakayama
- `jp_31`: 鳥取県 // Tottori
- `jp_32`: 島根県 // Shimane
- `jp_33`: 岡山県 // Okayama
- `jp_34`: 広島県 // Hiroshima
- `jp_35`: 山口県 // Yamaguchi
- `jp_36`: 徳島県 // Tokushima
- `jp_37`: 香川県 // Kagawa
- `jp_38`: 愛媛県 // Ehime
- `jp_39`: 高知県 // Kouchi
- `jp_40`: 福岡県 // Fukuoka
- `jp_41`: 佐賀県 // Saga
- `jp_42`: 長崎県 // Nagasaki
- `jp_43`: 熊本県 // Kumamoto
- `jp_44`: 大分県 // Oita
- `jp_45`: 宮崎県 // Miyazaki
- `jp_46`: 鹿児島県 // Kagoshima
- `jp_47`: 沖縄県 // Okinawa

**台湾 // TW (country code=158)**

- `tw_01`: 台北市 // Taipei City
- `tw_02`: 新北市 // New Taipei City
- `tw_03`: 桃園市 // Taoyuan City
- `tw_04`: 台中市 // Taichung City
- `tw_05`: 台南市 // Tainan City
- `tw_06`: 高雄市 // Kaohsiung City
- `tw_07`: 基隆市 // Keelung City
- `tw_08`: 新竹市 // Hsinchu City
- `tw_09`: 嘉義市 // Chiayi City
- `tw_10`: 新竹県 // Hsinchu County
- `tw_11`: 苗栗県 // Miaoli County
- `tw_12`: 彰化県 // Changhua County
- `tw_13`: 南投県 // Nantou County
- `tw_14`: 雲林県 // Yunlin County
- `tw_15`: 嘉義県 // Chiayi County
- `tw_16`: 屏東県 // Pingtung County
- `tw_17`: 宜蘭県 // Yilan County
- `tw_18`: 花蓮県 // Hualien County
- `tw_19`: 台東県 // Taitung County
- `tw_20`: 澎湖県 // Penghu County
- `tw_21`: 金門県 // Kinmen County
- `tw_22`: 連江県 // Lienchiang County

**タイ // TH (country code=764)**

- `th_01`: バンコク // Bangkok
- `th_02`: パタヤ // Pattaya
- `th_03`: 北部 // Northern
- `th_04`: 中央部 // Central
- `th_05`: 南部 // Southern
- `th_06`: 東部 // Eastern
- `th_07`: 東北部 // NorthEastern
- `th_08`: 西部 // Western

<!-- parameter end -->

###### Friendship duration 

這讓你可以篩選特定好友關係期間範圍的收件者。

<!-- parameter start (props: required) -->

type

字串

`subscriptionPeriod`

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

gte

字串

將訊息傳送給已成為你的好友至少達指定天數的使用者。\
你可以指定以下其中一個值。不過，請指定一個小於 `lt` 屬性所指定值的數值。

- `day_7`
- `day_30`
- `day_90`
- `day_180`
- `day_365`

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

lt

字串

將訊息傳送給成為你的好友少於指定天數的使用者。\
你可以指定以下其中一個值。不過，請指定一個大於 `gte` 屬性所指定值的數值。

- `day_7`
- `day_30`
- `day_90`
- `day_180`
- `day_365`

<!-- parameter end -->

\* 請務必指定 `gte`、`lt` 或兩者皆指定。

###### Logical operator objects 

使用邏輯 AND、OR 與 NOT 運算子，將多個 demographic filter object 組合在一起。每個請求最多可以指定 10 個 demographic filter object。

<!-- parameter start (props: required) -->

type

字串

`operator`

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

and

demographic filter object 的陣列

藉由取所指定 demographic filter object 陣列的邏輯交集（AND）來建立一個新的 demographic filter object。

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

or

demographic filter object 的陣列

藉由取所指定 demographic filter object 陣列的邏輯聯集（OR）來建立一個新的 demographic filter object。

<!-- parameter end -->
<!-- parameter start (props: annotation="*") -->

not

demographic filter object

建立一個排除所指定 demographic filter object 陣列的新 demographic filter object。

<!-- parameter end -->

\* 請務必只指定這三個屬性（`and`、`or` 或 `not`）其中之一。你不能指定空陣列。

_針對 gender 的 demographic filter object 範例_

<!-- tab start `json` -->

```json
{
  "type": "gender",
  "oneOf": ["male", "female"]
}
```

<!-- tab end -->

##### Limit objects 

你可以藉由設定 limit object，來設定可傳送的 narrowcast 訊息最大數量的上限。

如需更多關於透過屬性設定控制傳送最大數量的資訊，請參閱 Messaging API 文件中的 [Controlling the maximum number of messages to send with limit objects](https://developers.line.biz/en/docs/messaging-api/sending-messages/#maximum-send-numbers-control)。

<!-- parameter start (props: optional) -->

max

數字

要傳送的 narrowcast 訊息最大數量。使用此參數來限制傳送的 narrowcast 訊息數量。收件者將隨機選取。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

upToRemainingQuota

布林值

如果為 `true`，訊息將在可遞送訊息的最大數量範圍內傳送。預設值為 `false`。目標將隨機選取。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

forbidPartialDelivery

布林值

此選項可防止訊息僅遞送給目標受眾中的一部分人。當你將 `upToRemainingQuota` 屬性設為 `true`，同時也將 `forbidPartialDelivery` 屬性設為 `true` 時，如果收件者數量超過傳送的最大數量，訊息將不會被遞送。

你可以藉由[擷取 narrowcast 訊息進度](https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status)來檢查訊息遞送是否被取消。如果遞送被取消，回應中的 `phase` 屬性將為 `failed`，且 `errorCode` 屬性將為 `5`。

`forbidPartialDelivery` 屬性只有在 `upToRemainingQuota` 屬性設為 `true` 時才能指定。

<!-- parameter end -->

_limit object 範例_

<!-- tab start `json` -->

```json
{
  "max": 100,
  "upToRemainingQuota": true,
  "forbidPartialDelivery": true
}
```

<!-- tab end -->

此表顯示 `max` 屬性設定與 `upToRemainingQuota` 屬性設定，以及保留數量與傳送最大數量之間的關係。

| `max` property | `upToRemainingQuota` property | Number of reservation and maximum number of sending |
| --- | --- | --- |
| 未設定 | false | 目標可觸及人數 |
| 任意數字 | false | 目標可觸及人數與 `max` 屬性兩者中的最小值 |
| 未設定 | true | 目標可觸及人數與當月預估上限兩者中的最小值 |
| 任意數字 | true | 目標可觸及人數、當月預估上限與 `max` 屬性三者中的最小值 |

#### Response 

回傳 `202` HTTP 狀態碼與一個空的 JSON 物件。

Narrowcast 訊息會以非同步方式傳送。如需更多關於如何檢查 narrowcast 訊息狀態的資訊，請參閱 [Get narrowcast message status](https://developers.line.biz/en/reference/messaging-api/#get-narrowcast-progress-status)。

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法傳送訊息。可考慮以下原因：<ul><li>在 [redelivery object](https://developers.line.biz/en/reference/messaging-api/#narrowcast-recipient-redelivery-object) 中指定了無效的請求 ID。</li><li>指定了無效的受眾，例如狀態並非 `READY`。</li><li>指定了無效的訊息物件。</li><li>指定了無效的請求參數組合。</li></ul> |
| `403` | 收件者不足。如需更多資訊，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。 |
| `409` | 已接受包含相同重試金鑰的請求。如需更多資訊，請參閱 Retrying an API request 中的 [Response if the request has already been accepted](https://developers.line.biz/en/reference/messaging-api/#retry-api-request-response)。 |
| `429` | 請求數量已超過上限。可考慮以下原因：<ul><li>超過此端點的[速率限制](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-rate-limit)。</li><li>超過[本月可傳送訊息的目標上限](https://developers.line.biz/en/reference/messaging-api/#get-quota)。</li></ul>如需更多關於可傳送訊息目標上限的資訊，請參閱 Messaging API 文件中的 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

如果回傳錯誤，訊息不會傳送給任何使用者。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid audience ID (400 Bad Request)
{
    "message": "Invalid audience group id: {audience ID}"
}

// If you specify an invalid request ID for redelivery object (400 Bad Request)
{
    "message": "Invalid request id: {request ID}"
}

// If you set limit.forbidPartialDelivery to true without setting limit.upToRemainingQuota to true (400 Bad Request)
{
    "message": "The option forbidPartialDelivery must be used with upToRemainingQuota."
}

// If there are not enough friends (403 Forbidden)
{
    "message": "Your account does not have enough friends"
}
```

<!-- tab end -->

### Get narrowcast message status 

端點：`GET` `https://api.line.me/v2/bot/message/progress/narrowcast`

取得 narrowcast 訊息的狀態。

<!-- note start -->

**當收件者數量少於所需數量時，無法傳送 narrowcast 訊息**

為防止有人猜測收件者的屬性，當收件者數量低於所需的最低數量時，無法傳送 narrowcast 訊息。如需更多資訊，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。

<!-- note end -->

<!-- note start -->

**狀態請求的可用時間範圍**

在 `acceptedTime` 中所顯示的時間戳記起算超過 14 天（336 小時）之後，你將無法再取得 narrowcast 訊息的狀態。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/message/progress/narrowcast?requestId={request_id}' \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

requestId

narrowcast 訊息的請求 ID。每個 Messaging API 請求都有一個請求 ID。可在[回應標頭](https://developers.line.biz/en/reference/messaging-api/#response-headers)中找到它。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼與包含以下資訊的 JSON 物件。

<!-- parameter start -->

phase

字串

目前的狀態。以下其中之一：

- `waiting`：訊息尚未準備好傳送。它們目前正在以某種方式進行篩選或處理。
- `sending`：訊息目前正在傳送中。
- `succeeded`：訊息已成功傳送。這未必表示訊息已成功接收。
- `failed`：訊息傳送失敗。請使用 `failedDescription` 屬性來找出失敗的原因。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

successCount

數字

成功收到訊息的使用者數量。\*

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

failureCount

數字

傳送訊息失敗的使用者數量。\* \
即使 `phase` 為 `succeeded`，除非 `failureCount` 為 0，否則部分使用者可能仍無法收到 narrowcast 訊息。例如，如果使用者在傳送 narrowcast 訊息期間封鎖了 LINE 官方帳號，該情況將被計入 `failureCount`。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

targetCount

數字

訊息的預定收件者數量。\*

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

failedDescription

字串

訊息傳送失敗的原因。此項僅在 `phase` 屬性值為 `failed` 時包含。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

errorCode

數字

錯誤摘要。此項僅在 `phase` 屬性值為 `failed` 時包含。\
以下其中之一：

- `1`：發生內部錯誤。
- `2`：因收件者不足而發生錯誤。
- `3`：因重試已被接受的請求而發生請求衝突錯誤。
- `4`：傳送條件中包含少於 50 名收件者的受眾。
- `5`：為防止訊息僅遞送給目標受眾中的一部分人，訊息遞送已被取消。此錯誤發生於將 [`limit.forbidPartialDelivery`](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-limit) 設為 `true` 且收件者數量超過傳送最大數量而傳送訊息時。

<!-- parameter end -->
<!-- parameter start -->

acceptedTime

字串

narrowcast 訊息請求被接受的時間（毫秒）。

- 格式：[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)（例如 `2020-12-03T10:15:30.121Z`）
- 時區：UTC

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

completedTime

字串

narrowcast 訊息請求處理完成的時間（毫秒）。當 `phase` 屬性為 `succeeded` 或 `failed` 時回傳。

- 格式：[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)（例如 `2020-12-03T10:15:30.121Z`）
- 時區：UTC

<!-- parameter end -->

\* 當 `phase` 屬性為 `waiting` 時無法取得。

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的請求 ID。 |
| `404` | 無法取得狀態。可考慮以下原因：<ul><li>可取得狀態的時間期間已過期。</li><li>指定了 narrowcast 訊息以外的請求 ID。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you couldn't get the status (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Send broadcast message 

端點：`POST` `https://api.line.me/v2/bot/message/broadcast`

隨時將訊息傳送給所有與你的 LINE 官方帳號為好友的使用者。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/broadcast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-H 'X-Line-Retry-Key: {UUID}' \
-d '{
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

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

X-Line-Retry-Key

重試金鑰。指定以任何方法產生的十六進位格式 UUID（例如 123e4567-e89b-12d3-a456-426614174000）。重試金鑰並非由 LINE 產生。每位開發者都必須產生自己的重試金鑰。如需更多資訊，請參閱 Messaging API 文件中的 [Retry failed API requests](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

[message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 的陣列

要傳送的訊息\
上限：5

藉由使用 [Validate message objects of a broadcast message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-broadcast-message) 端點，你可以驗證訊息物件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

notificationDisabled

布林值

- `true`：傳送訊息時，使用者不會收到推播通知。
- `false`：傳送訊息時，使用者會收到推播通知（除非他們在 LINE 及／或其裝置上停用了推播通知）。

預設值：`false`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的訊息物件。 |
| `409` | 已接受包含相同重試金鑰的請求。如需更多資訊，請參閱 Retrying an API request 中的 [Response if the request has already been accepted](https://developers.line.biz/en/reference/messaging-api/#retry-api-request-response)。 |
| `429` | 請求數量已超過上限。可考慮以下原因：<ul><li>超過此端點的[速率限制](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-rate-limit)。</li><li>超過[本月可傳送訊息的目標上限](https://developers.line.biz/en/reference/messaging-api/#get-quota)。</li></ul>如需更多關於可傳送訊息目標上限的資訊，請參閱 Messaging API 文件中的 [Messaging API pricing](https://developers.line.biz/en/docs/messaging-api/pricing/)。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

如果回傳錯誤，訊息不會被傳送。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If your request contains invalid parameters（400 Bad Request）
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "May not be empty",
      "property": "messages[0].type"
    }
  ]
}
```

<!-- tab end -->

### Mark messages as read 

端點：`POST` `https://api.line.me/v2/bot/chat/markAsRead`

將在指定訊息之前傳送的所有訊息標記為已讀。如需更多資訊，請參閱 Messaging API 文件中的 [Mark messages as read](https://developers.line.biz/en/docs/messaging-api/mark-as-read/)。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/chat/markAsRead \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
  "markAsReadToken": "{mark as read token}"
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

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

markAsReadToken

字串

已讀權杖（read token）。包含於 webhook 中 [message event object](https://developers.line.biz/en/reference/messaging-api/#message-event) 的 `markAsReadToken` 屬性內。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                               |
| ----- | ----------------------------------------- |
| `400` | 指定了無效的已讀權杖。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If an invalid read token is specified (400 Bad Request)
{
  "message": "Invalid markAsReadToken. Tokens must be used by the bot that received them via Webhook."
}
```

<!-- tab end -->

### Display a loading animation 

端點：`POST` `https://api.line.me/v2/bot/chat/loading/start`

在使用者與 LINE 官方帳號之間的一對一聊天中顯示載入動畫（loading animation）。

載入動畫會在經過指定的秒數（5 到 60 秒）之後，或當你的 LINE 官方帳號傳來新訊息時，自動消失。

載入動畫只有在使用者正在檢視與你的 LINE 官方帳號的聊天畫面時才會顯示。如果你在使用者並未檢視聊天畫面時請求顯示載入動畫，將不會顯示任何通知。即使使用者稍後開啟聊天畫面，動畫也不會顯示。

如果你在載入動畫仍可見時再次請求顯示，動畫將會繼續顯示，且其消失前的時間會被第二次請求中指定的秒數覆寫。

載入動畫將在以下版本的 LINE 上顯示：

- iOS 或 Android 版 LINE：13.16.0 或更新版本

如需更多資訊，請參閱 Messaging API 文件中的 [Display a loading animation](https://developers.line.biz/en/docs/messaging-api/use-loading-indicator/)。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/chat/loading/start \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "chatId": "U4af4980629...",
    "loadingSeconds": 5
}'
```

<!-- tab end -->

#### Rate limit 

每秒 100 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

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

chatId

字串

要顯示載入動畫的目標使用者的使用者 ID。

如需更多關於如何取得使用者 ID 的資訊，請參閱 Messaging API 文件中的 [Get user IDs](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

loadingSeconds

數字

顯示載入動畫的秒數。你可以指定 `5`、`10`、`15`、`20`、`25`、`30`、`35`、`40`、`45`、`50`、`55` 或 `60` 其中任一個值。

預設值為 `20`。

<!-- parameter end -->

#### Response 

回傳狀態碼 `202` 與一個空的 JSON 物件。

如果你請求對以下使用者顯示載入動畫，會回傳狀態碼 `202`，但載入動畫不會顯示：

- 並未開啟與你的 LINE 官方帳號的聊天畫面的使用者
- 尚未將你的 LINE 官方帳號加為好友的使用者
- 已封鎖你的 LINE 官方帳號的使用者
- 已刪除 LINE 帳號的使用者

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法顯示載入動畫。可考慮以下原因：<ul><li>指定了無效的秒數。</li><li>指定了無效的使用者 ID。</li><li>指定了群組聊天或多人聊天。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

如果回傳錯誤，將不會顯示載入動畫。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid number of seconds (400 Bad Request)
{
  "message": "The request body has 2 error(s)",
  "details": [
    {
      "message": "Must be between 5 and 60",
      "property": "loadingSeconds"
    },
    {
      "message": "must be a multiple of five",
      "property": "loadingSeconds"
    }
  ]
}

// If you specify a group chat or a multi-person chat as the destination (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Only user id is acceptable, please confirm if there are any group/room ids or illegal ids.",
      "property": "chatId"
    }
  ]
}
```

<!-- tab end -->
### Get the target limit for sending messages this month 

Endpoint: `GET` `https://api.line.me/v2/bot/message/quota`

取得當月可傳送訊息的目標上限。回傳免費訊息與額外訊息的總數量。

此端點（endpoint）所取得的訊息數量，包含從 LINE Official Account Manager 傳送的訊息數量。

請透過 LINE Official Account Manager 設定額外訊息的目標上限。關於設定方式的詳細資訊，請參閱 LINE for Business 的 [Using and billing (plan changes and payment management)](https://www.lycbiz.com/jp/manual/OfficialAccountManager/account-settings_plan/?list=7171)（僅提供日文）。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/message/quota \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求（request）

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件（object）。

<!-- parameter start -->

type

String

以下其中一個值，用以表示是否已設定目標上限。

- `none`：表示尚未設定目標上限。
- `limited`：表示已設定目標上限。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

value

Number

當月可傳送訊息的目標上限。當 `type` 屬性（property）的值為 `limited` 時會回傳此屬性。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "type": "limited",
  "value": 1000
}
```

<!-- tab end -->

#### Error Response 

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

### Get number of messages sent this month 

Endpoint: `GET` `https://api.line.me/v2/bot/message/quota/consumption`

取得當月已傳送的訊息數量。

此操作所取得的訊息數量，包含從 LINE Official Account Manager 傳送的訊息數量。

此操作所取得的訊息數量為概略值。若要取得正確的已傳送訊息數量，請使用 LINE Official Account Manager，或執行用於取得已傳送訊息數量的 API 操作。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/message/quota/consumption \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

totalUsage

Number

當月已傳送的訊息數量

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "totalUsage": 500
}
```

<!-- tab end -->

#### Error Response 

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

### Get number of sent reply messages 

Endpoint: `GET` `https://api.line.me/v2/bot/message/delivery/reply`

取得透過 [`/bot/message/reply`](https://developers.line.biz/en/reference/messaging-api/#send-reply-message) 端點傳送的訊息數量。

此操作所取得的訊息數量，不包含從 LINE Official Account Manager 傳送的訊息數量。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET "https://api.line.me/v2/bot/message/delivery/reply?date={yyyyMMdd}" \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

date

訊息傳送的日期

- 格式：`yyyyMMdd`（例如 `20191231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

status

String

計數處理的狀態。會回傳以下其中一個值：

- `ready`：你可以取得訊息數量。
- `unready`：`date` 所指定日期的訊息計數處理尚未完成。請稍後重試你的請求。通常計數處理會在隔天內完成。
- `out_of_service`：`date` 所指定的日期早於計數系統開始運作的日期 2018 年 3 月 31 日。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

success

Number

於 `date` 所指定日期透過 Messaging API 傳送的訊息數量。只有當 `status` 的值為 `ready` 時，回應（response）才會有此屬性。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "status": "ready",
  "success": 10000
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的日期格式。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a date in an invalid format (400 Bad Request)
{
  "message": "The value for the 'date' parameter is invalid"
}
```

<!-- tab end -->

### Get number of sent push messages 

Endpoint: `GET` `https://api.line.me/v2/bot/message/delivery/push`

取得透過 [`/bot/message/push`](https://developers.line.biz/en/reference/messaging-api/#send-push-message) 端點傳送的訊息數量。

此操作所取得的訊息數量，不包含從 LINE Official Account Manager 傳送的訊息數量。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET "https://api.line.me/v2/bot/message/delivery/push?date={yyyyMMdd}" \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

date

訊息傳送的日期

- 格式：`yyyyMMdd`（例如 `20191231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

status

String

計數處理的狀態。會回傳以下其中一個值：

- `ready`：你可以取得訊息數量。
- `unready`：`date` 所指定日期的訊息計數處理尚未完成。請稍後重試你的請求。通常計數處理會在隔天內完成。
- `out_of_service`：`date` 所指定的日期早於計數系統開始運作的日期 2018 年 3 月 31 日。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

success

Number

於 `date` 所指定日期透過 Messaging API 傳送的訊息數量。只有當 `status` 的值為 `ready` 時，回應才會有此屬性。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "status": "ready",
  "success": 10000
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的日期格式。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a date in an invalid format (400 Bad Request)
{
  "message": "The value for the 'date' parameter is invalid"
}
```

<!-- tab end -->

### Get number of sent multicast messages 

Endpoint: `GET` `https://api.line.me/v2/bot/message/delivery/multicast`

取得透過 [`/bot/message/multicast`](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message) 端點傳送的訊息數量。

此操作所取得的訊息數量，不包含從 LINE Official Account Manager 傳送的訊息數量。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET "https://api.line.me/v2/bot/message/delivery/multicast?date={yyyyMMdd}" \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

date

訊息傳送的日期

- 格式：`yyyyMMdd`（例如 `20191231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

status

String

計數處理的狀態。會回傳以下其中一個值：

- `ready`：你可以取得訊息數量。
- `unready`：`date` 所指定日期的訊息計數處理尚未完成。請稍後重試你的請求。通常計數處理會在隔天內完成。
- `out_of_service`：`date` 所指定的日期早於計數系統開始運作的日期 2018 年 3 月 31 日。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

success

Number

於 `date` 所指定日期透過 Messaging API 傳送的訊息數量。只有當 `status` 的值為 `ready` 時，回應才會有此屬性。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "status": "ready",
  "success": 10000
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的日期格式。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a date in an invalid format (400 Bad Request)
{
  "message": "The value for the 'date' parameter is invalid"
}
```

<!-- tab end -->

### Get number of sent broadcast messages 

Endpoint: `GET` `https://api.line.me/v2/bot/message/delivery/broadcast`

取得透過 [`/bot/message/broadcast`](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message) 端點傳送的訊息數量。

此操作所取得的訊息數量，不包含從 LINE Official Account Manager 傳送的訊息數量。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET "https://api.line.me/v2/bot/message/delivery/broadcast?date={yyyyMMdd}" \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

date

訊息傳送的日期

- 格式：`yyyyMMdd`（例如 `20191231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

status

String

計數處理的狀態。會回傳以下其中一個值：

- `ready`：你可以取得訊息數量。
- `unready`：`date` 所指定日期的訊息計數處理尚未完成。請稍後重試你的請求。通常計數處理會在隔天內完成。
- `out_of_service`：`date` 所指定的日期早於計數系統開始運作的日期 2018 年 3 月 31 日。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

success

Number

於 `date` 所指定日期透過 Messaging API 傳送的訊息數量。只有當 `status` 的值為 `ready` 時，回應才會有此屬性。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "status": "ready",
  "success": 10000
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的日期格式。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a date in an invalid format (400 Bad Request)
{
  "message": "The value for the 'date' parameter is invalid"
}
```

<!-- tab end -->

### Validate message objects of a reply message 

Endpoint: `POST` `https://api.line.me/v2/bot/message/validate/reply`

你可以驗證一個 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列（array）是否能作為 [Send reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message) 端點 [request body](https://developers.line.biz/en/reference/messaging-api/#send-reply-message-request-body) 中 `messages` 屬性的有效值。此端點不會驗證 `messages` 屬性以外的其他屬性值。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/validate/reply \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
  "messages": [
    {
      "type": "text",
      "text": "Hello, world"
    }
  ]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

Array of objects

要驗證的 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code  | Description                             |
| ----- | --------------------------------------- |
| `400` | 指定了無效的 message object。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example (If more message objects are specified than the maximum number)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Size must be between 1 and 5",
      "property": "messages"
    }
  ]
}
```

<!-- tab end -->

_Error response example (If more characters are specified in a text message than the maximum number of characters)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Length must be between 0 and 5000",
      "property": "messages[0].text"
    }
  ]
}
```

<!-- tab end -->

### Validate message objects of a push message 

Endpoint: `POST` `https://api.line.me/v2/bot/message/validate/push`

你可以驗證一個 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列是否能作為 [Send push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message) 端點 [request body](https://developers.line.biz/en/reference/messaging-api/#send-push-message-request-body) 中 `messages` 屬性的有效值。此端點不會驗證 `messages` 屬性以外的其他屬性值。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/validate/push \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
  "messages": [
    {
      "type": "text",
      "text": "Hello, world"
    }
  ]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

Array of objects

要驗證的 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code  | Description                             |
| ----- | --------------------------------------- |
| `400` | 指定了無效的 message object。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example (If more message objects are specified than the maximum number)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Size must be between 1 and 5",
      "property": "messages"
    }
  ]
}
```

<!-- tab end -->

_Error response example (If more characters are specified in a text message than the maximum number of characters)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Length must be between 0 and 5000",
      "property": "messages[0].text"
    }
  ]
}
```

<!-- tab end -->

### Validate message objects of a multicast message 

Endpoint: `POST` `https://api.line.me/v2/bot/message/validate/multicast`

你可以驗證一個 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列是否能作為 [Send multicast message](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message) 端點 [request body](https://developers.line.biz/en/reference/messaging-api/#send-multicast-request-body) 中 `messages` 屬性的有效值。此端點不會驗證 `messages` 屬性以外的其他屬性值。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/validate/multicast \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
  "messages": [
    {
      "type": "text",
      "text": "Hello, world"
    }
  ]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

Array of objects

要驗證的 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code  | Description                             |
| ----- | --------------------------------------- |
| `400` | 指定了無效的 message object。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example (If more message objects are specified than the maximum number)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Size must be between 1 and 5",
      "property": "messages"
    }
  ]
}
```

<!-- tab end -->

_Error response example (If more characters are specified in a text message than the maximum number of characters)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Length must be between 0 and 5000",
      "property": "messages[0].text"
    }
  ]
}
```

<!-- tab end -->

### Validate message objects of a narrowcast message 

Endpoint: `POST` `https://api.line.me/v2/bot/message/validate/narrowcast`

你可以驗證一個 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列是否能作為 [Send narrowcast message](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message) 端點 [request body](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-request-body) 中 `messages` 屬性的有效值。此端點不會驗證 `messages` 屬性以外的其他屬性值。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/validate/narrowcast \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
  "messages": [
    {
      "type": "text",
      "text": "Hello, world"
    }
  ]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

Array of objects

要驗證的 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code  | Description                             |
| ----- | --------------------------------------- |
| `400` | 指定了無效的 message object。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example (If more message objects are specified than the maximum number)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Size must be between 1 and 5",
      "property": "messages"
    }
  ]
}
```

<!-- tab end -->

_Error response example (If more characters are specified in a text message than the maximum number of characters)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Length must be between 0 and 5000",
      "property": "messages[0].text"
    }
  ]
}
```

<!-- tab end -->

### Validate message objects of a broadcast message 

Endpoint: `POST` `https://api.line.me/v2/bot/message/validate/broadcast`

你可以驗證一個 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列是否能作為 [Send broadcast message](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message) 端點 [request body](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-request-body) 中 `messages` 屬性的有效值。此端點不會驗證 `messages` 屬性以外的其他屬性值。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/validate/broadcast \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
  "messages": [
    {
      "type": "text",
      "text": "Hello, world"
    }
  ]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

messages

Array of objects

要驗證的 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 陣列

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code  | Description                             |
| ----- | --------------------------------------- |
| `400` | 指定了無效的 message object。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example (If more message objects are specified than the maximum number)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Size must be between 1 and 5",
      "property": "messages"
    }
  ]
}
```

<!-- tab end -->

_Error response example (If more characters are specified in a text message than the maximum number of characters)_

<!-- tab start `json` -->

```json
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Length must be between 0 and 5000",
      "property": "messages[0].text"
    }
  ]
}
```

<!-- tab end -->

### Retrying an API request 

透過在 push 訊息、multicast 訊息、narrowcast 訊息或 broadcast 訊息的 HTTP header 中加入重試金鑰（`X-Line-Retry-Key`），即可重新嘗試同一個 API 請求，以避免重複處理。

LINE Platform 端的重試金鑰管理期間為 24 小時。若你在超過 24 小時後仍使用相同的重試金鑰，該請求將被視為一個新的 API 請求。

關於重試 API 請求的詳細資訊，請參閱 Messaging API 文件中的 [Retry failed API requests](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。

<!-- note start -->

**Don't use the same retry key for more than 24 hours**

若你在超過 24 小時後仍使用相同的重試金鑰，即使含有相同重試金鑰的 API 請求已經成功，該請求仍會以新的 API 請求成功送出。如此一來，將會發送重複的訊息。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-H 'X-Line-Retry-Key: {UUID}' \
-d '{
    "messages": [
        {
            "type": "text",
            "text": "Hello, user"
        }
    ]
}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: annotation="Optional*") -->

X-Line-Retry-Key

任意產生的十六進位表示法 UUID（例如 123e4567-e89b-12d3-a456-426614174000）

<!-- parameter end -->

\* 重試 API 請求時為必填。

#### Response if the request has already been accepted 

若含有相同重試金鑰的請求已被接受，則回傳 `409` 狀態碼、用以表示已被接受請求之請求 ID 的 `x-line-accepted-request-id` header，以及包含此資訊的 JSON 物件。

<!-- parameter start -->

message

String

告知同一個請求已被接受的訊息

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

sentMessages

Array

已傳送訊息的陣列。只有在傳送 push 訊息時，回應才會有此屬性。<br />上限：5

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

sentMessages.id

Number

已傳送訊息的 ID。只有在傳送 push 訊息時，回應才會有此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

sentMessages.quoteToken

String

訊息的引用權杖（quote token）。只有當作為 push 訊息傳送之 message object 可被指定為引用對象時才會包含。詳細資訊請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
HTTP/1.1 409 Conflict
x-line-request-id: 123e4567-e89b-12d3-a456-426655440002
x-line-accepted-request-id: 123e4567-e89b-12d3-a456-426655440001

{
  "message": "The retry key is already accepted",
  "sentMessages": [
    {
      "id": "461230966842064897",
      "quoteToken": "IStG5h1Tz7b..."
    }
  ]
}
```

<!-- tab end -->

## Managing Audience 

你可以建立、更新、啟用或刪除 audience。傳送 narrowcast 訊息時可指定 audience。

也可以使用 [LINE Official Account Manager](https://manager.line.biz/) 建立 audience。詳情請參閱 LINE for Business 的 [Audience](https://www.lycbiz.com/jp/manual/OfficialAccountManager/messages-audience/)。

| Audience | How to create |
| --- | --- |
| 用於上傳 user ID 的 audience | <ul><li>[Messaging API](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group)</li><li>[LINE Official Account Manager](https://manager.line.biz/)</li><li>[LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）</li></ul> |
| Message click audience | <ul><li>[Messaging API](https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group)</li><li>[LINE Official Account Manager](https://manager.line.biz/)</li></ul> |
| Message impression audience | <ul><li>[Messaging API](https://developers.line.biz/en/reference/messaging-api/#create-imp-audience-group)</li><li>[LINE Official Account Manager](https://manager.line.biz/)</li></ul> |
| Chat tag audience | [LINE Official Account Manager](https://manager.line.biz/) |
| Friend path audience | [LINE Official Account Manager](https://manager.line.biz/) |
| Reservation audience | [LINE Official Account Manager](https://manager.line.biz/) |
| Rich menu impression audience | [LINE Official Account Manager](https://manager.line.biz/) |
| Rich menu click audience | [LINE Official Account Manager](https://manager.line.biz/) |
| Web traffic audience (LINE Tag) | <ul><li>[LINE Official Account Manager](https://manager.line.biz/)</li><li>[LINE Ads](https://admanager.line.biz/)</li></ul> |
| Web traffic audience (Tracking Tag) | [LINE Official Account Manager](https://manager.line.biz/) |
| App event audience | [LINE Ads](https://admanager.line.biz/) |
| Video view audience | [LINE Ads](https://admanager.line.biz/) |
| Image click audience | [LINE Ads](https://admanager.line.biz/) |
| LINE Beacon Network ad impression audience \* | [LINE Ads](https://admanager.line.biz/) |

\* LINE Beacon Network ad impression audience 僅適用於由台灣使用者所建立的 LINE 官方帳號。

<!-- note start -->

**Note**

- 只有擁有 LINE 官方帳號的日本（JP）、泰國（TH）與台灣（TW）使用者可以建立 audience。
- 你無法使用 Messaging API 建立以下類型的 audience：
  - Chat tag audience
  - Friend path audience
  - Reservation audience
  - Rich menu impression audience
  - Rich menu click audience
  - Web traffic audience (LINE Tag)
  - Web traffic audience (Tracking Tag)
  - App event audience
  - Video view audience
  - Image click audience
  - LINE Beacon Network ad impression audience

<!-- note end -->

### Details of the error related to audience management 

在 Managing Audience 端點上發生的錯誤詳細資訊，會包含在 JSON 回應的 `details[].message` 屬性中。主要錯誤的詳細資訊如下：

| Message | Description |
| --- | --- |
| `AUDIENCE_GROUP_CAN_NOT_UPLOAD_STATUS_EXPIRED` | 此 audience 無法使用，因為自其建立至今已超過 180 天（15,552,000 秒）。 |
| `AUDIENCE_GROUP_COUNT_MAX_OVER` | 你已建立達到上限數量的 audience（1,000 個）。 |
| `AUDIENCE_GROUP_NAME_SIZE_OVER` | audience 的名稱過長。 |
| `AUDIENCE_GROUP_NAME_WRONG` | audience 的名稱含有無效字元（例如 `\n` 或其他控制字元）。 |
| `AUDIENCE_GROUP_NAME_EMPTY` | audience 的名稱為空或僅含空白。 |
| `AUDIENCE_GROUP_NOT_FOUND` | 找不到 audience。 |
| `AUDIENCE_GROUP_REQUESTID_DUPLICATE` | 已存在使用所指定請求 ID 的 audience。 |
| `AUDIENCE_GROUP_UPLOAD_DESCRIPTION_SIZE_OVER` | audience 的描述過長。 |
| `REQUEST_NOT_FOUND` | 所指定的請求 ID 不正確，或 LINE 尚未準備好以所指定的請求 ID 建立 audience。 |
| `TOO_OLD_MESSAGES` | 你無法為超過 60 天（5,184,000 秒）前傳送的訊息（請求 ID）建立 audience。 |
| `UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT` | <ul><li>`file` 含有無效的 user ID 或 IFA。</li><li>`audiences[].id` 為無效的 user ID 或 IFA。</li></ul>若回傳此訊息，請參閱 [Error-handling methods](https://developers.line.biz/en/reference/messaging-api/#manage-audience-error-handling)。 |
| `UPLOAD_AUDIENCE_GROUP_NO_VALID_AUDIENCE_IDS` | <ul><li>`file` 未含有有效的 user ID 或 IFA。</li><li>`audiences[].id` 並非有效的 user ID 或 IFA。</li></ul> |
| `UPLOAD_AUDIENCE_GROUP_TOO_MANY_AUDIENCE_IDS` | 超過 user ID 或 IFA 的數量上限。 |
| `WRONG_BOT_ID` | 所指定請求 ID 中的 bot ID，與簽發該 channel access token 之 channel 所連結的 bot 不符。 |
| `ALREADY_ACTIVE` | 此 audience group 已處於啟用狀態。 |

#### Error-handling methods 

<!-- note start -->

**If the audiences property contains invalid user IDs**

當回傳 `UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT` 時，請使用 [Get profile information](https://developers.line.biz/en/reference/messaging-api/#get-profile) 端點，取得 JSON 中所指定全部 user ID 的個人檔案資訊。在排除所有回傳非 `200` 狀態碼的 user ID 之後，再次執行失敗的端點。

<!-- note end -->

### Create audience for uploading user IDs (by JSON) 

Endpoint: `POST` `https://api.line.me/v2/bot/audienceGroup/upload`

建立用於上傳 user ID 的 audience。

對於此端點，請使用 JSON 來指定收件者。你也可以使用 [Endpoint that specifies recipients with text file](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group-by-file)。

關於如何取得 user ID 的詳細資訊，請參閱 Messaging API 文件中的 [Get user IDs](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/)。

#### Conditions for users that can be added to the audience 

你可以將與你的 LINE 官方帳號為好友的使用者加入「用於上傳 user ID 的 audience」。即使回傳狀態碼 `202`，以下這些使用者也會被加入 audience。

- 已刪除其 LINE 帳號的使用者
- 已封鎖建立此 audience 之 LINE 官方帳號的使用者
- 尚未將建立此 audience 之 LINE 官方帳號加為好友的使用者

若你使用所建立的 audience 傳送訊息，訊息不會被傳送給上述使用者。

<!-- note start -->

**We have set a limit on the number of concurrent endpoint operations**

針對每個 audience ID（`audienceGroupId`），我們對建立「用於上傳 user ID 的 audience」以及將 user ID 加入 audience 的並行端點操作數量設有限制。詳細資訊請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。

<!-- note end -->

<!-- note start -->

**You must complete additional application forms to specify recipients using Identifiers for Advertisers (IFAs)**

你可以使用 IFA 來指定收件者，但此功能僅供已完成特定申請的企業使用者使用。若要在你的 LINE 官方帳號中使用此功能，請聯絡你的業務代表，或聯絡 [我們的銷售夥伴（Sales partners）](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

<!-- tip start -->

**Audience used for uploading user IDs**

audience 的規格如下：

| Item | Limit |
| --- | --- |
| 每個 channel 的 audience 數量 | 上限：1,000 |
| audience 的保留期間 | 最多 180 天（15,552,000 秒） |
| 每個請求可上傳至 audience 的 user ID 或 IFA 數量 | 使用 JSON 時：上限 10,000<br>使用檔案時：上限 1,500,000 |
| 每個 audience 的使用者數量 | 用於上傳 user ID 的 audience：無限制 |

關於 narrowcast 訊息的限制，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。

<!-- tip end -->

<!-- note start -->

**Verifying a valid user ID**

若 JSON 的 `audiences` 屬性中指定了無效的 user ID，將回傳錯誤回應（`details[].message`：`UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT`），且加入 user ID 將會失敗。在執行此端點前，請檢查 JSON 的 `audiences` 屬性中所指定的全部 user ID 是否皆為有效。

若要確認 user ID 是否有效，請使用 [Get profile information](https://developers.line.biz/en/reference/messaging-api/#get-profile) 端點。若該 user ID 有效，會回傳 HTTP 狀態碼 `200`。若回傳非 `200` 的值，則該 user ID 為無效，不應被納入 `audiences` 屬性中。

<!-- note end -->

<!-- note start -->

**Status of an audience without a user ID**

若在建立 audience 時省略 `audiences` 屬性，或在 JSON 中指定空陣列，將會建立一個空的 audience。

空 audience 所包含的使用者數量（`audienceGroup.audienceCount`）為 0，且該 audience 無法接收訊息。因此，回應中的 `audienceGroup.status` 會維持 `IN_PROGRESS`，而不會變為 `READY`。

<!-- note end -->

<!-- note start -->

**Only users who have agreed to LINE's Privacy Policy (revised in March 2022 or later) will be added**

當你將 user ID 加入「用於上傳 user ID 的 audience」時，任何屬於尚未同意 LINE 隱私權政策（於 2022 年 3 月或之後修訂版本）之使用者的 ID 都會被忽略。只有已同意之使用者的 ID 才會被加入。

因此，audience 的有效收件者數量可能會少於所指定的 user ID 數量。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/audienceGroup/upload \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "description": "audienceGroupName_01"
}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 個請求

關於速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

description

String

audience 的名稱。此為不區分大小寫，意即 `AUDIENCE` 與 `audience` 視為相同。 \
最大字元數限制：120

<!-- parameter end -->
<!-- parameter start (props: optional) -->

isIfaAudience

Boolean

- 若要以 IFA 指定收件者：設為 `true`。
- 若要以 user ID 指定收件者：設為 `false` 或省略 `isIfaAudience` 屬性。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

uploadDescription

String

要為此作業（job）登錄的描述（位於 `jobs[].description`）。\
最大字元數限制：300

<!-- parameter end -->
<!-- parameter start (props: optional) -->

audiences

Array

user ID 或 IFA 的陣列。\
若省略，將會建立一個空的 audience。\
最大數量：10,000

<!-- parameter end -->
<!-- parameter start (props: optional) -->

audiences\[].id

String

一個 user ID 或 IFA。你可以指定空陣列。\
若指定空陣列，將會建立一個空的 audience。

<!-- parameter end -->

#### Response 

回傳 `202` HTTP 狀態碼以及包含以下資訊的 JSON 物件。

<!-- note start -->

**Audience is created asynchronously**

在使用 audience 之前，請先 [確認該 audience 可用於傳送](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-audience-status)。

<!-- note end -->

<!-- parameter start -->

audienceGroupId

Number

audience ID。

<!-- parameter end -->
<!-- parameter start -->

createRoute

String

audience 的建立方式。

- `MESSAGING_API`：以 Messaging API 建立的 audience。

<!-- parameter end -->
<!-- parameter start -->

type

String

audience 類型。

- `UPLOAD`：用於上傳 user ID 的 audience

<!-- parameter end -->
<!-- parameter start -->

description

String

audience 的名稱。

<!-- parameter end -->
<!-- parameter start -->

created

Number

audience 建立時間，以 UNIX 時間表示（單位為秒）。

<!-- parameter end -->
<!-- parameter start -->

permission

String

對所建立 audience 的更新權限。

- `READ_WRITE`：可使用並更新此 audience。

<!-- parameter end -->
<!-- parameter start -->

expireTimestamp

Number

audience 過期時間，以 UNIX 時間表示（單位為秒）

<!-- parameter end -->
<!-- parameter start -->

isIfaAudience

Boolean

建立「用於上傳 user ID 的 audience」時所指定、用以表示傳送對象帳號類型的值。為以下其中之一：

- `true`：帳號以 IFA 指定。
- `false`（預設）：帳號以 user ID 指定。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "audienceGroupId": 1234567890123,
  "createRoute": "MESSAGING_API",
  "type": "UPLOAD",
  "description": "audienceGroupName_01",
  "created": 1613698278,
  "permission": "READ_WRITE",
  "expireTimestamp": 1629250278,
  "isIfaAudience": false
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼以及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。請考慮以下原因：<ul><li>你已建立達到上限數量的 audience（1,000 個）。<li>在 `description` 屬性中指定了超過最大字元數（120）的名稱。</li><li>在 `description` 屬性中指定了無效字元（例如 `\n` 或其他控制字元）。</li><li>`description` 屬性為空或僅含空白。</li><li>在 `uploadDescription` 屬性中指定了超過最大字元數（300）的字串。</li><li>在 `audiences[].id` 屬性中指定了無效的 user ID 或 IFA。</li><li>在 `audiences` 屬性中指定了超過最大數量（10,000）的 user ID 或 IFA。</li></ul> |
| `429` | 已超過並行操作數量的限制。詳細資訊請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。 |

詳細資訊請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 一節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a name longer than the maximum number of characters (120) in the description property (400 Bad Request)
{
  "message": "size over audienceGroupName",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NAME_SIZE_OVER"
    }
  ]
}
```

<!-- tab end -->
### Create audience for uploading user IDs (by file) 

Endpoint: `POST` `https://api-data.line.me/v2/bot/audienceGroup/upload/byFile`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 中傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

建立一個用於上傳使用者 ID 的受眾（audience）。

此端點使用文字檔來指定收件對象。你也可以使用[以 JSON 指定收件對象的端點](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group)。

如需更多關於如何取得使用者 ID 的資訊，請參閱 Messaging API 文件中的 [Get user IDs](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/)。

#### Conditions for users that can be added to the audience 

你可以將與你的 LINE 官方帳號（LINE Official Account）為好友的使用者加入「用於上傳使用者 ID 的受眾」。即使回傳的狀態碼為 `202`，下列使用者仍會被加入受眾：

- 已刪除 LINE 帳號的使用者
- 封鎖了建立該受眾之 LINE 官方帳號的使用者
- 尚未將建立該受眾之 LINE 官方帳號加為好友的使用者

如果你使用所建立的受眾傳送訊息，訊息不會被傳送給上述使用者。

<!-- note start -->

**我們對端點的同時操作數量設有限制**

針對「建立用於上傳使用者 ID 的受眾」以及「將使用者 ID 加入受眾」，我們對每個受眾 ID（`audienceGroupId`）的端點同時操作數量設有限制。如需更多資訊，請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。

<!-- note end -->

<!-- note start -->

**使用廣告識別碼（Identifiers for Advertisers, IFA）指定收件對象須完成額外申請表單**

你可以使用 IFA 來指定收件對象，但此功能僅開放給已完成特定申請的企業用戶使用。若要在你的 LINE 官方帳號上使用此功能，請聯絡你的業務代表或聯絡[我們的銷售合作夥伴（Sales partners）](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

<!-- tip start -->

**用於上傳使用者 ID 的受眾**

受眾規格如下：

| Item | Limit |
| --- | --- |
| 每個頻道的受眾數量 | 上限：1,000 |
| 受眾的保留期間 | 最多 180 天（15,552,000 秒） |
| 每次請求可上傳至受眾的使用者 ID 或 IFA 數量 | 使用 JSON 時：上限 10,000<br>使用檔案時：上限 1,500,000 |
| 每個受眾的使用者數量 | 用於上傳使用者 ID 的受眾：無限制 |

如需關於 narrowcast 訊息限制的資訊，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。

<!-- tip end -->

<!-- note start -->

**只有已同意 LINE 隱私權政策（2022 年 3 月或之後修訂版本）的使用者才會被加入**

當你將使用者 ID 加入「用於上傳使用者 ID 的受眾」時，凡是屬於尚未同意 LINE 隱私權政策（2022 年 3 月或之後修訂版本）之使用者的 ID 都會被忽略。只有已同意的使用者 ID 才會被加入。

因此，受眾中有效收件對象的數量可能會少於所指定的使用者 ID 數量。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api-data.line.me/v2/bot/audienceGroup/upload/byFile \
-H 'Authorization: Bearer {channel access token}' \
-F 'description=audienceGroupName_01' \
-F 'file=@audiences.txt;type=text/plain'
```

<!-- tab end -->

_Text file example_

<!-- tab start `File` -->

```
U4af4980627...
U4af4980628...
U4af4980629...
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制（rate limit）的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`multipart/form-data`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

description

String

受眾的名稱。此欄位不區分大小寫，意即 `AUDIENCE` 與 `audience` 會被視為相同。 \
字元數上限：120

<!-- parameter end -->
<!-- parameter start (props: optional) -->

isIfaAudience

Boolean

- 若要以 IFA 指定收件對象：設為 `true`。
- 若要以使用者 ID 指定收件對象：設為 `false` 或省略 `isIfaAudience` 屬性（property）。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

uploadDescription

String

要為作業（job）註冊的描述（在 `jobs[].description` 中）。\
字元數上限：300

<!-- parameter end -->
<!-- parameter start (props: required) -->

file

File

每行輸入一個使用者 ID 或 IFA 的文字檔。請將 Content-Type 指定為 `text/plain`。\
檔案數量上限：1\
數量上限：1,500,000

<!-- parameter end -->

#### Response 

回傳 `202` HTTP 狀態碼，以及包含下列資訊的 JSON 物件（object）。

<!-- note start -->

**受眾為非同步建立**

在使用受眾之前，請[確認該受眾是否可用於傳送](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-audience-status)。

<!-- note end -->

<!-- parameter start -->

audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

createRoute

String

受眾的建立方式。

- `MESSAGING_API`：以 Messaging API 建立的受眾。

<!-- parameter end -->
<!-- parameter start -->

type

String

受眾類型。

- `UPLOAD`：用於上傳使用者 ID 的受眾。

<!-- parameter end -->
<!-- parameter start -->

description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

created

Number

受眾建立的時間，以 UNIX 時間表示（單位：秒）。

<!-- parameter end -->
<!-- parameter start -->

permission

String

所建立受眾的更新權限。

- `READ_WRITE`：可使用並更新該受眾。

<!-- parameter end -->
<!-- parameter start -->

expireTimestamp

Number

受眾到期時間，以 UNIX 時間表示（單位：秒）

<!-- parameter end -->
<!-- parameter start -->

isIfaAudience

Boolean

在建立「用於上傳使用者 ID 的受眾」時所指定、用以表示傳送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設值）：以使用者 ID 指定帳號。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "audienceGroupId": 1234567890123,
  "createRoute": "MESSAGING_API",
  "type": "UPLOAD",
  "description": "audienceGroupName_01",
  "created": 1613700237,
  "permission": "READ_WRITE",
  "expireTimestamp": 1629252237,
  "isIfaAudience": false
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應（error response）：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>在 `file` 屬性中指定的檔案包含無效的使用者 ID 或 IFA。</li><li>在 `file` 屬性中指定的檔案，其使用者 ID 或 IFA 數量超過上限（1,500,000）。</li><li>在 `file` 屬性中指定的檔案不包含有效的使用者 ID 或 IFA。</li><li>你已建立達到上限數量（1,000）的受眾。</li><li>在 `description` 屬性中指定的名稱超過字元數上限（120）。</li><li>在 `description` 屬性中指定了無效字元（例如 `\n` 或其他控制字元）。</li><li>`description` 屬性為空或僅包含空格。</li><li>在 `uploadDescription` 屬性中指定的字串超過字元數上限（300）。</li></ul> |
| `415` | 在 `file` 屬性中指定了不支援的媒體格式檔案。 |
| `429` | 同時操作數量已超過限制。如需更多資訊，請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a name longer than the maximum number of characters (120) in the description property (400 Bad Request)
{
  "message": "size over audienceGroupName",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NAME_SIZE_OVER"
    }
  ]
}
```

<!-- tab end -->

### Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by JSON) 

Endpoint: `PUT` `https://api.line.me/v2/bot/audienceGroup/upload`

將新的使用者 ID 或 IFA 加入「用於上傳使用者 ID 的受眾」。

此端點使用 JSON 來指定收件對象。你也可以使用[以文字檔指定收件對象的端點](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group-by-file)。

#### Conditions for users that can be added to the audience 

你可以將與你的 LINE 官方帳號為好友的使用者加入「用於上傳使用者 ID 的受眾」。即使回傳的狀態碼為 `202`，下列使用者仍會被加入受眾：

- 已刪除 LINE 帳號的使用者
- 封鎖了建立該受眾之 LINE 官方帳號的使用者
- 尚未將建立該受眾之 LINE 官方帳號加為好友的使用者

如果你使用所建立的受眾傳送訊息，訊息不會被傳送給上述使用者。

<!-- note start -->

**我們對端點的同時操作數量設有限制**

針對「建立用於上傳使用者 ID 的受眾」以及「將使用者 ID 加入受眾」，我們對每個受眾 ID（`audienceGroupId`）的端點同時操作數量設有限制。如需更多資訊，請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。

<!-- note end -->

<!-- note start -->

**請求逾時值**

我們強烈建議使用 30 秒以上的請求逾時值。

<!-- note end -->

<!-- note start -->

**驗證有效的使用者 ID**

如果在 JSON 的 `audiences` 屬性中指定了無效的使用者 ID，將會回傳錯誤回應（`details[].message`：`UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT`），且受眾建立會失敗。在執行此端點之前，請檢查 JSON 的 `audiences` 屬性中所指定的所有使用者 ID 是否皆有效。

若要確認某個使用者 ID 是否有效，請使用 [Get profile information](https://developers.line.biz/en/reference/messaging-api/#get-profile) 端點。如果該使用者 ID 有效，將會回傳 HTTP 狀態碼 `200`。如果回傳的值不是 `200`，則表示該使用者 ID 無效，不應被包含在 `audiences` 屬性中。

<!-- note end -->

<!-- note start -->

**你無法在使用者 ID 與 IFA 之間切換**

請依照你最初建立受眾時所指定的類型，將相同類型的資料（使用者 ID 或 IFA）加入「用於上傳使用者 ID 的受眾」。例如，你無法將使用者 ID 加入一個最初建立時是使用 IFA 的受眾。

你可以使用受眾的 `isIfaAudience` 屬性來判斷該受眾建立時所指定的收件對象類型（使用者 ID 或 IFA）。如需更多細節，請參閱 [Get audience data](https://developers.line.biz/en/reference/messaging-api/#get-audience-group)。

<!-- note end -->

<!-- note start -->

**你無法刪除使用者 ID 或 IFA**

使用者 ID 或 IFA 一經加入後即無法刪除。

<!-- note end -->

<!-- note start -->

**只有已同意 LINE 隱私權政策（2022 年 3 月或之後修訂版本）的使用者才會被加入**

當你將使用者 ID 加入「用於上傳使用者 ID 的受眾」時，凡是屬於尚未同意 LINE 隱私權政策（2022 年 3 月或之後修訂版本）之使用者的 ID 都會被忽略。只有已同意的使用者 ID 才會被加入。

因此，受眾中有效收件對象的數量可能會少於所指定的使用者 ID 數量。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X PUT https://api.line.me/v2/bot/audienceGroup/upload \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "audienceGroupId": 4389303728991,
    "uploadDescription": "fileName",
    "audiences": [
        {
            "id": "U4af4980627..."
        },
        {
            "id": "U4af4980628..."
        }
    ]
}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

audienceGroupId

Number

受眾 ID

<!-- parameter end -->
<!-- parameter start (props: optional) -->

uploadDescription

String

要與作業一起註冊的描述（在 `jobs[].description` 中）。\
字元數上限：300

<!-- parameter end -->
<!-- parameter start (props: required) -->

audiences

Array

使用者 ID 或 IFA 的陣列（array）\
數量上限：10,000

<!-- parameter end -->
<!-- parameter start (props: required) -->

audiences\[].id

String

一個使用者 ID 或 IFA

<!-- parameter end -->

#### Response 

回傳狀態碼 `202` 與一個空的 JSON 物件。

<!-- note start -->

**受眾為非同步建立**

在使用受眾之前，請[確認該受眾是否可用於傳送](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-audience-status)。

<!-- note end -->

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>在 `audiences[].id` 屬性中指定了無效的使用者 ID 或 IFA。</li><li>在 `audiences` 屬性中指定的使用者 ID 或 IFA 數量超過上限（10,000）。</li><li>未在 `audiences[].id` 屬性中指定有效的使用者 ID 或 IFA。</li><li>指定了已超過保留期間的受眾。</li><li>指定了不存在的受眾。</li><li>在 `uploadDescription` 屬性中指定的字串超過字元數上限（300）。</li></ul> |
| `429` | 同時操作數量已超過限制。如需更多資訊，請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID in the audiences[].id property (400 Bad Request)
{
  "message": "Invalid audience id format",
  "details": [
    {
      "message": "UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT",
      "property": "audiences"
    }
  ]
}
```

<!-- tab end -->

### Add user IDs or Identifiers for Advertisers (IFAs) to an audience for uploading user IDs (by file) 

Endpoint: `PUT` `https://api-data.line.me/v2/bot/audienceGroup/upload/byFile`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 中傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

將新的使用者 ID 或 IFA 加入「用於上傳使用者 ID 的受眾」。

此端點使用文字檔來指定收件對象。你也可以使用[以 JSON 指定收件對象的端點](https://developers.line.biz/en/reference/messaging-api/#update-upload-audience-group)。

#### Conditions for users that can be added to the audience 

你可以將與你的 LINE 官方帳號為好友的使用者加入「用於上傳使用者 ID 的受眾」。即使回傳的狀態碼為 `202`，下列使用者仍會被加入受眾：

- 已刪除 LINE 帳號的使用者
- 封鎖了建立該受眾之 LINE 官方帳號的使用者
- 尚未將建立該受眾之 LINE 官方帳號加為好友的使用者

如果你使用所建立的受眾傳送訊息，訊息不會被傳送給上述使用者。

<!-- note start -->

**我們對端點的同時操作數量設有限制**

針對「建立用於上傳使用者 ID 的受眾」以及「將使用者 ID 加入受眾」，我們對每個受眾 ID（`audienceGroupId`）的端點同時操作數量設有限制。如需更多資訊，請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。

<!-- note end -->

<!-- note start -->

**請求逾時值**

我們強烈建議使用 30 秒以上的請求逾時值。

<!-- note end -->

<!-- note start -->

**你無法在使用者 ID 與 IFA 之間切換**

請依照你最初建立受眾時所指定的類型，將相同類型的資料（使用者 ID 或 IFA）加入「用於上傳使用者 ID 的受眾」。例如，你無法將使用者 ID 加入一個最初建立時是使用 IFA 的受眾。

你可以使用受眾的 `isIfaAudience` 屬性來判斷該受眾建立時所指定的收件對象類型（使用者 ID 或 IFA）。如需更多細節，請參閱 [Get audience data](https://developers.line.biz/en/reference/messaging-api/#get-audience-group)。

<!-- note end -->

<!-- note start -->

**你無法刪除使用者 ID 或 IFA**

使用者 ID 或 IFA 一經加入後即無法刪除。

<!-- note end -->

<!-- note start -->

**只有已同意 LINE 隱私權政策（2022 年 3 月或之後修訂版本）的使用者才會被加入**

當你將使用者 ID 加入「用於上傳使用者 ID 的受眾」時，凡是屬於尚未同意 LINE 隱私權政策（2022 年 3 月或之後修訂版本）之使用者的 ID 都會被忽略。只有已同意的使用者 ID 才會被加入。

因此，受眾中有效收件對象的數量可能會少於所指定的使用者 ID 數量。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X PUT https://api-data.line.me/v2/bot/audienceGroup/upload/byFile \
-H 'Authorization: Bearer {channel access token}' \
-F 'audienceGroupId=4389303728991' \
-F 'uploadDescription=fileName' \
-F 'file=@audiences.txt;type=text/plain'
```

<!-- tab end -->

_Example text_

<!-- tab start `File` -->

```sh
U4af4980627...
U4af4980628...
U4af4980629...
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`multipart/form-data`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

audienceGroupId

Number

受眾 ID

<!-- parameter end -->
<!-- parameter start (props: optional) -->

uploadDescription

String

要與作業一起註冊的描述（在 `jobs[].description` 中）\
字元數上限：300

<!-- parameter end -->
<!-- parameter start (props: required) -->

file

File

每行輸入一個使用者 ID 或 IFA 的文字檔。請將 Content-Type 指定為 `text/plain`。\
檔案數量上限：1\
數量上限：1,500,000

<!-- parameter end -->

#### Response 

回傳狀態碼 `202` 與一個空的 JSON 物件。

<!-- note start -->

**受眾為非同步建立**

在使用受眾之前，請[確認該受眾是否可用於傳送](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-audience-status)。

<!-- note end -->

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>在 `file` 屬性中指定的檔案包含無效的使用者 ID 或 IFA。</li><li>在 `file` 屬性中指定的檔案，其使用者 ID 或 IFA 數量超過上限（1,500,000）。</li><li>在 `file` 屬性中指定的檔案不包含有效的使用者 ID 或 IFA。</li><li>指定了已超過保留期間的受眾。</li><li>指定了不存在的受眾。</li><li>在 `uploadDescription` 屬性中指定的字串超過字元數上限（300）。</li></ul> |
| `415` | 在 `file` 屬性中指定了不支援的媒體格式檔案。 |
| `429` | 同時操作數量已超過限制。如需更多資訊，請參閱 [Limit on the number of concurrent operations](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a file that contains an invalid user ID or IFA (400 Bad Request)
{
  "message": "UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT",
  "details": [
    {
      "message": "UPLOAD_AUDIENCE_GROUP_INVALID_AUDIENCE_ID_FORMAT",
      "property": "file"
    }
  ]
}
```

<!-- tab end -->

### Create message click audience 

Endpoint: `POST` `https://api.line.me/v2/bot/audienceGroup/click`

建立一個訊息點擊受眾（message click audience）。

訊息點擊受眾是由曾經點擊 broadcast 或 narrowcast 訊息中所含 URL 的使用者所組成的集合。訊息會傳送給任何至少點擊過一個連結的使用者。

使用請求 ID（request ID）來指定訊息。

<!-- tip start -->

**訊息點擊受眾**

受眾規格如下：

| Item | Limit |
| --- | --- |
| 每個頻道的受眾數量 | 上限：1,000 |
| 受眾的保留期間 | 最多 180 天（15,552,000 秒） |
| 每個受眾的使用者數量 | 最少：每個訊息點擊受眾 50 人 |
| 訊息傳送後可建立 retargeting 受眾\* 的期間   |   上限：60 天（5,184,000 秒） |

\* 訊息點擊受眾與訊息曝光受眾（message impression audience）。

如需更多資訊，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/audienceGroup/click \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "description": "audienceGroupName_01",
    "requestId": "bb9744f9-47fa-4a29-941e-1234567890ab",
    "clickUrl": "https://developers.line.biz/"
}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

description

String

受眾的名稱。此欄位不區分大小寫，意即 `AUDIENCE` 與 `audience` 會被視為相同。 \
字元數上限：120

<!-- parameter end -->
<!-- parameter start (props: required) -->

requestId

String

過去 60 天內傳送的 broadcast 或 narrowcast 訊息的請求 ID。每個 Messaging API 請求都有一個請求 ID。你可以在[回應標頭（response headers）](https://developers.line.biz/en/reference/messaging-api/#response-headers)中找到它。

<!-- note start -->

**注意**

reply 訊息、push 訊息與 multicast 訊息的請求 ID 無法使用。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

clickUrl

String

使用者所點擊的 URL。若為空，則點擊訊息中任何 URL 的使用者都會被加入收件對象清單。 \
字元數上限：2,000

<!-- parameter end -->

#### Response 

回傳 `202` HTTP 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- note start -->

**受眾為非同步建立**

在使用受眾之前，請[確認該受眾是否可用於傳送](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-audience-status)。

<!-- note end -->

<!-- parameter start -->

audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

createRoute

String

受眾的建立方式。

- `MESSAGING_API`：以 Messaging API 建立的受眾

<!-- parameter end -->
<!-- parameter start -->

type

String

受眾類型。

- `CLICK`：訊息點擊受眾

<!-- parameter end -->
<!-- parameter start -->

description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

created

Number

受眾建立的時間，以 UNIX 時間表示（單位：秒）。

<!-- parameter end -->
<!-- parameter start -->

permission

String

所建立受眾的更新權限。

- `READ_WRITE`：可使用並更新該受眾。

<!-- parameter end -->
<!-- parameter start -->

expireTimestamp

Number

受眾到期時間，以 UNIX 時間表示（單位：秒）

<!-- parameter end -->
<!-- parameter start -->

isIfaAudience

Boolean

在建立「用於上傳使用者 ID 的受眾」時所指定、用以表示傳送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設值）：以使用者 ID 指定帳號。

<!-- parameter end -->
<!-- parameter start -->

requestId

String

建立受眾時所指定的請求 ID。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

clickUrl

String

建立受眾時所指定的 URL。只有當你在請求中以 `clickUrl` 屬性指定值時才會包含此欄位。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "audienceGroupId": 1234567890123,
  "createRoute": "MESSAGING_API",
  "type": "CLICK",
  "description": "audienceGroupName_01",
  "created": 1613705240,
  "permission": "READ_WRITE",
  "expireTimestamp": 1629257239,
  "isIfaAudience": false,
  "requestId": "bb9744f9-47fa-4a29-941e-1234567890ab",
  "clickUrl": "https://developers.line.biz/"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>你已建立達到上限數量（1,000）的受眾。</li><li>在 `description` 屬性中指定的名稱超過字元數上限（120）。</li><li>在 `description` 屬性中指定了無效字元（例如 `\n` 或其他控制字元）。</li><li>`requestID` 與 `clickUrl` 屬性的組合值與現有受眾相同。</li><li>建立受眾的時間限制已過期。</li><li>指定了不存在的請求 ID。</li><li>LINE Platform 尚未準備好以指定的請求 ID 建立受眾。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a name longer than the maximum number of characters (120) in the description property (400 Bad Request)
{
  "message": "size over audienceGroupName",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NAME_SIZE_OVER"
    }
  ]
}
```

<!-- tab end -->

### Create message impression audience 

Endpoint: `POST` `https://api.line.me/v2/bot/audienceGroup/imp`

建立一個訊息曝光受眾（message impression audience）。

訊息曝光受眾是由曾經檢視 broadcast 或 narrowcast 訊息的使用者所組成的集合。受眾會包含任何至少檢視過一則訊息泡泡的使用者。

使用請求 ID 來指定訊息。

<!-- tip start -->

**訊息曝光受眾**

受眾規格如下：

| Item | Limit |
| --- | --- |
| 每個頻道的受眾數量 | 上限：1,000 |
| 受眾的保留期間 | 最多 180 天（15,552,000 秒） |
| 每個受眾的使用者數量 | 最少：每個訊息曝光受眾 50 人 |
| 訊息傳送後可建立 retargeting 受眾\* 的期間   |   上限：60 天（5,184,000 秒） |

\* 訊息點擊受眾與訊息曝光受眾。

如需更多資訊，請參閱 [Restrictions on sending messages using attributes and audiences](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/audienceGroup/imp \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "description": "audienceGroupName_01",
    "requestId": "bb9744f9-47fa-4a29-941e-1234567890ab"
}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

description

String

受眾的名稱。此欄位不區分大小寫，意即 `AUDIENCE` 與 `audience` 會被視為相同。 \
字元數上限：120

<!-- parameter end -->
<!-- parameter start (props: required) -->

requestId

String

過去 60 天內傳送的 broadcast 或 narrowcast 訊息的請求 ID。每個 Messaging API 請求都有一個請求 ID。你可以在[回應標頭](https://developers.line.biz/en/reference/messaging-api/#response-headers)中找到它。

<!-- parameter end -->

#### Response 

回傳 `202` HTTP 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- note start -->

**受眾為非同步建立**

在使用受眾之前，請[確認該受眾是否可用於傳送](https://developers.line.biz/en/docs/messaging-api/sending-messages/#get-audience-status)。

<!-- note end -->

<!-- parameter start -->

audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

createRoute

String

受眾的建立方式。

- `MESSAGING_API`：以 Messaging API 建立的受眾。

<!-- parameter end -->
<!-- parameter start -->

type

String

受眾類型。

- `IMP`：訊息曝光受眾。

<!-- parameter end -->
<!-- parameter start -->

description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

created

Number

受眾建立的時間，以 UNIX 時間表示（單位：秒）。

<!-- parameter end -->
<!-- parameter start -->

permission

String

所建立受眾的更新權限。

- `READ_WRITE`：可使用並更新該受眾。

<!-- parameter end -->
<!-- parameter start -->

expireTimestamp

Number

受眾到期時間，以 UNIX 時間表示（單位：秒）

<!-- parameter end -->
<!-- parameter start -->

isIfaAudience

Boolean

在建立「用於上傳使用者 ID 的受眾」時所指定、用以表示傳送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設值）：以使用者 ID 指定帳號。

<!-- parameter end -->
<!-- parameter start -->

requestId

String

建立受眾時所指定的請求 ID。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "audienceGroupId": 1234567890123,
  "createRoute": "MESSAGING_API",
  "type": "IMP",
  "description": "audienceGroupName_01",
  "created": 1613707097,
  "permission": "READ_WRITE",
  "expireTimestamp": 1629259095,
  "isIfaAudience": false,
  "requestId": "bb9744f9-47fa-4a29-941e-1234567890ab"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>你已建立達到上限數量（1,000）的受眾。</li><li>在 `description` 屬性中指定的名稱超過字元數上限（120）。</li><li>在 `description` 屬性中指定了無效字元（例如 `\n` 或其他控制字元）。</li><li>已存在使用指定請求 ID 的受眾。</li><li>建立受眾的時間限制已過期。</li><li>指定了不存在的請求 ID。</li><li>LINE Platform 尚未準備好以指定的請求 ID 建立受眾。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a name longer than the maximum number of characters (120) in the description property (400 Bad Request)
{
  "message": "size over audienceGroupName",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NAME_SIZE_OVER"
    }
  ]
}
```

<!-- tab end -->

### Rename an audience 

Endpoint: `PUT` `https://api.line.me/v2/bot/audienceGroup/{audienceGroupId}/updateDescription`

重新命名一個現有的受眾。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X PUT https://api.line.me/v2/bot/audienceGroup/{audienceGroupId}/updateDescription \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '{
    "description": "audienceGroupName"
}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`application/json`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

audienceGroupId

受眾 ID。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

description

String

受眾的名稱。此欄位不區分大小寫，意即 `AUDIENCE` 與 `audience` 會被視為相同。 \
字元數上限：120

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼與一個空的 JSON 物件。

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>在 `description` 屬性中指定的名稱超過字元數上限（120）。</li><li>在 `description` 屬性中指定了無效字元（例如 `\n` 或其他控制字元）。</li><li>指定了不存在的受眾。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a name longer than the maximum number of characters (120) in the description property (400 Bad Request)
{
  "message": "size over audienceGroupName",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NAME_SIZE_OVER"
    }
  ]
}
```

<!-- tab end -->

### Delete audience 

Endpoint: `DELETE` `https://api.line.me/v2/bot/audienceGroup/{audienceGroupId}`

刪除一個受眾。

<!-- warning start -->

**刪除受眾無法復原**

在刪除受眾之前，請確認該受眾已不再使用。

<!-- warning end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X DELETE https://api.line.me/v2/bot/audienceGroup/{audienceGroupId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

audienceGroupId

受眾 ID。

<!-- parameter end -->

#### Response 

回傳 `202` HTTP 狀態碼與一個空的 JSON 物件。

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code  | Description                           |
| ----- | ------------------------------------- |
| `400` | 指定了不存在的受眾。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a non-existent audience (400 Bad Request)
{
  "message": "audience group not found",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NOT_FOUND"
    }
  ]
}
```

<!-- tab end -->

### Get audience data 

Endpoint: `GET` `https://api.line.me/v2/bot/audienceGroup/{audienceGroupId}`

取得受眾資料。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/audienceGroup/{audienceGroupId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

audienceGroupId

受眾 ID。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

audienceGroup

Object

受眾群組物件（audience group object）。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.createRoute

String

受眾的建立方式。為下列其中之一：

- `OA_MANAGER`：以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾
- `MESSAGING_API`：以 Messaging API 建立的受眾
- `POINT_AD`：以 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅日文）建立的受眾
- `AD_MANAGER`：以 [LINE Ads](https://admanager.line.biz/) 建立的受眾

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.type

String

受眾類型。為下列其中之一：

- `UPLOAD`：用於上傳使用者 ID 的受眾
- `CLICK`：訊息點擊受眾
- `IMP`：訊息曝光受眾
- `CHAT_TAG`：聊天標籤受眾（Chat tag audience）
- `FRIEND_PATH`：好友路徑受眾（Friend path audience）
- `RESERVATION`：預約受眾（Reservation audience）
- `RICHMENU_IMP`：圖文選單曝光受眾（Rich menu impression audience）
- `RICHMENU_CLICK`：圖文選單點擊受眾（Rich menu click audience）
- `APP_EVENT`：App 事件受眾（App event audience）
- `VIDEO_VIEW`：影片觀看受眾（Video view audience）
- `WEBTRAFFIC`：網站流量受眾（Web traffic audience，LINE Tag）
- `TRACKINGTAG_WEBTRAFFIC`：網站流量受眾（Web traffic audience，Tracking Tag）
- `IMAGE_CLICK`：圖片點擊受眾（Image click audience）
- `POP_AD_IMP`：LINE Beacon Network 廣告曝光受眾（LINE Beacon Network ad impression audience）

如需更多資訊，請參閱 LINE for Business 上的 [Audience](https://www.lycbiz.com/jp/manual/OfficialAccountManager/messages-audience/) 頁面。此頁面目前尚未提供英文版本。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.status

String

受眾的狀態。為下列其中之一：

- `IN_PROGRESS`：處理中。狀態變更為 `READY` 可能需要數小時。對於有使用者數量限制的受眾，如果受眾中包含的使用者數量不足（至少需要 50 人），狀態會維持 `IN_PROGRESS` 而不會更新。
- `READY`：已準備好可接受訊息。
- `FAILED`：建立受眾時發生錯誤。
- `EXPIRED`：已過期。受眾會在過期一個月後自動刪除。
- `INACTIVE`：受眾處於非啟用狀態。
- `ACTIVATING`：受眾正在啟用中。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.audienceCount

Number

受眾中包含的使用者數量。為了保護使用者的隱私，當數量少於 20 時會回傳 0，除非受眾類型為下列其中之一：

- 用於上傳使用者 ID 的受眾（以使用者 ID 指定收件對象的情況）
- 聊天標籤受眾

由於受眾中可能包含已封鎖 LINE 官方帳號的使用者，因此 `audienceGroup.audienceCount` 的值與實際會收到訊息的使用者數量會有所不同。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.created

Number

受眾建立的時間，以 UNIX 時間表示（單位：秒）。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.permission

String

受眾的更新權限。如果目前的 Messaging API 頻道可以更新目標受眾，則回傳 `READ_WRITE`；如果無法更新，則回傳 `READ`。

- `READ`：可使用，但無法更新該受眾。
- `READ_WRITE`：可使用並更新該受眾。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.isIfaAudience

Boolean

在建立「用於上傳使用者 ID 的受眾」時所指定、用以表示傳送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設值）：以使用者 ID 指定帳號。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.requestId

String

建立受眾時所指定的請求 ID。只有當 `audienceGroup.type` 為 `CLICK` 或 `IMP` 時才會包含此欄位。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.clickUrl

String

建立受眾時所指定的 URL。只有當 `audienceGroup.type` 為 `CLICK` 且有指定連結 URL 時才會包含此欄位。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.failedType

String

操作失敗的原因。只有當 `audienceGroup.status` 為 `FAILED` 時才會包含此欄位。為下列其中之一：

- `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT`：受眾中包含的使用者數量不足（至少需要 50 人）
- `INTERNAL_ERROR`：內部伺服器錯誤

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.activated

Number

受眾啟用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.inactivatedTimestamp

Number

受眾非啟用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.expireTimestamp

Number

受眾到期時間，以 UNIX 時間表示（單位：秒）。僅針對特定受眾回傳。

<!-- parameter end -->
<!-- parameter start -->

jobs

Array

作業（job）陣列。此陣列用於追蹤每一次將新使用者 ID 或 IFA 加入「用於上傳使用者 ID 的受眾」的嘗試。對於其他任何類型的受眾，會回傳空陣列。<br />上限：50

<!-- parameter end -->
<!-- parameter start -->

jobs\[].audienceGroupJobId

Number

作業 ID。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].description

String

作業的描述。如果你在新增使用者 ID 或 IFA 時未以 `uploadDescription` 屬性指定值，將會回傳 `null`。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].type

String

作業類型。為下列其中之一：

- `DIFF_ADD`：表示經由 Messaging API 新增了使用者 ID 或 IFA。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].status

String

此屬性已棄用。作業的狀態請參閱 `jobs[].jobStatus`。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].failedType

String

操作失敗的原因。只有當 `jobs[].jobStatus` 為 `FAILED` 時才會包含此欄位。為下列其中之一：

- `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT`：受眾中包含的使用者數量不足（至少需要 50 人）
- `INTERNAL_ERROR`：內部伺服器錯誤

如果 `jobs[].jobStatus` 不是 `FAILED`，則回傳 `null`。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].audienceCount

Number

被新增或移除的帳號（收件對象）數量。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].created

Number

作業建立的時間，以 UNIX 時間表示（單位：秒）。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].jobStatus

String

作業的狀態。為下列其中之一：

- `QUEUED`：等待執行
- `WORKING`：執行中
- `FINISHED`：已完成
- `FAILED`：失敗

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

adaccount

Object

廣告帳號物件（Ad account object）。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start -->

adaccount\[].name

String

建立共用受眾的廣告帳號名稱。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// Example of an audience used for uploading user IDs
{
    "audienceGroup": {
        "audienceGroupId": 1234567890123,
        "createRoute": "OA_MANAGER",
        "type": "UPLOAD",
        "description": "audienceGroupName_01",
        "status": "READY",
        "audienceCount": 1887,
        "created": 1608617466,
        "permission": "READ",
        "isIfaAudience": false,
        "expireTimestamp": 1624342266
    },
    "jobs": [
        {
            "audienceGroupJobId": 12345678,
            "audienceGroupId": 1234567890123,
            "description": "audience_list.txt",
            "type": "DIFF_ADD",
            "status": "FINISHED",
            "failedType": null,
            "audienceCount": 0,
            "created": 1608617472,
            "jobStatus": "FINISHED"
        }
    ]
}

// Example of a message click audience
{
    "audienceGroup": {
        "audienceGroupId": 1234567890987,
        "createRoute": "OA_MANAGER",
        "type": "CLICK",
        "description": "audienceGroupName_02",
        "status": "IN_PROGRESS",
        "audienceCount": 8619,
        "created": 1611114828,
        "permission": "READ",
        "isIfaAudience": false,
        "expireTimestamp": 1626753228,
        "requestId": "c10c3d86-f565-...",
        "clickUrl": "https://example.com/"
    },
    "jobs": []
}

// Example of an audience used for app events
{
    "audienceGroup": {
        "audienceGroupId": 2345678909876,
        "createRoute": "AD_MANAGER",
        "type": "APP_EVENT",
        "description": "audienceGroupName_03",
        "status": "READY",
        "audienceCount": 8619,
        "created": 1608619802,
        "permission": "READ",
        "activated": 1610068515,
        "inactiveTimestamp": 1625620516,
        "isIfaAudience": false
    },
    "jobs": [],
    "adaccount": {
        "name": "Ad Account Name"
    }
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code  | Description                           |
| ----- | ------------------------------------- |
| `400` | 指定了不存在的受眾。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a non-existent audience (400 Bad Request)
{
  "message": "audience group not found",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NOT_FOUND"
    }
  ]
}
```

<!-- tab end -->
### Get data for multiple audiences 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/audienceGroup/list`

取得多個受眾（audience）的資料。

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/audienceGroup/list \
--data-urlencode 'page=1' \
--data-urlencode 'description=audienceGroupName' \
--data-urlencode 'size=40' \
--data-urlencode 'createRoute=OA_MANAGER' \
-G \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求（request）

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

page

取得（分頁）結果時要回傳的頁碼。必須為 `1` 或更大。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

description

要回傳的受眾名稱。可以搜尋部分相符的內容。此項目不區分大小寫，亦即 `AUDIENCE` 與 `audience` 視為相同。若省略，則不會以受眾名稱作為搜尋條件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

status

要回傳的受眾狀態。若省略，則不會以受眾狀態作為搜尋條件。為下列其中之一：

- `IN_PROGRESS`：處理中。
- `READY`：已可接收訊息。
- `FAILED`：建立受眾時發生錯誤。
- `EXPIRED`：已過期。受眾在過期後一個月會自動刪除。
- `INACTIVE`：受眾處於停用狀態。
- `ACTIVATING`：受眾正在啟用中。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

每頁的受眾數量。預設值：`20` \
最大值：`40`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

includesExternalPublicGroups

- `true`（預設）：取得與同一個 bot 連結的所有頻道（channel）中建立的公開受眾。
- `false`：取得在同一個頻道中建立的受眾。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

createRoute

受眾的建立方式。若省略，則包含所有受眾。

- `OA_MANAGER`：只回傳以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾。
- `MESSAGING_API`：只回傳以 Messaging API 建立的受眾。
- `POINT_AD`：只回傳以 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾。
- `AD_MANAGER`：只回傳以 [LINE Ads](https://admanager.line.biz/) 建立的受眾。

若指定多個參數（parameter），則使用 OR 條件。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼，以及包含下列資訊的 JSON 物件（object）。

<!-- parameter start -->

audienceGroups

Array

受眾資料的陣列（array）。若沒有符合指定篩選條件的受眾，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].createRoute

String

受眾的建立方式。為下列其中之一：

- `OA_MANAGER`：以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾
- `MESSAGING_API`：以 Messaging API 建立的受眾
- `POINT_AD`：以 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾
- `AD_MANAGER`：以 [LINE Ads](https://admanager.line.biz/) 建立的受眾

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].type

String

受眾類型。為下列其中之一：

- `UPLOAD`：用於上傳使用者 ID 的受眾
- `CLICK`：訊息點擊受眾
- `IMP`：訊息曝光受眾
- `CHAT_TAG`：聊天標籤受眾
- `FRIEND_PATH`：好友路徑受眾
- `RESERVATION`：預約受眾
- `RICHMENU_IMP`：圖文選單曝光受眾
- `RICHMENU_CLICK`：圖文選單點擊受眾
- `APP_EVENT`：App 事件受眾
- `VIDEO_VIEW`：影片觀看受眾
- `WEBTRAFFIC`：網站流量受眾（LINE Tag）
- `TRACKINGTAG_WEBTRAFFIC`：網站流量受眾（Tracking Tag）
- `IMAGE_CLICK`：圖片點擊受眾
- `POP_AD_IMP`：LINE Beacon Network 廣告曝光受眾

如需更多資訊，請參閱 LINE for Business 上的 [Audience](https://www.lycbiz.com/jp/manual/OfficialAccountManager/messages-audience/) 頁面。此頁面目前未提供英文版。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].status

String

受眾的狀態。為下列其中之一：

- `IN_PROGRESS`：處理中。狀態變更為 `READY` 可能需要數小時。對於有使用者數量限制的受眾，若受眾中包含的使用者數量不足（至少需要 50 人），狀態將維持為 `IN_PROGRESS` 而不會更新。
- `READY`：已可接收訊息。
- `FAILED`：建立受眾時發生錯誤。
- `EXPIRED`：已過期。受眾在過期後一個月會自動刪除。
- `INACTIVE`：受眾處於停用狀態。
- `ACTIVATING`：受眾正在啟用中。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].audienceCount

Number

受眾中包含的使用者數量。為保護使用者隱私，當數量少於 20 時會回傳 0，但下列受眾類型除外：

- 用於上傳使用者 ID 的受眾（以使用者 ID 指定收件者的情況）
- 聊天標籤受眾

由於受眾中可能包含已封鎖 LINE 官方帳號（LINE Official Account）的使用者，`audienceGroups[].audienceCount` 的值與實際發送訊息的使用者數量會有所不同。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].created

Number

受眾建立的時間，以 UNIX time 表示（單位為秒）。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].permission

String

受眾的更新權限。若目前的 Messaging API 頻道可以更新目標受眾，回傳 `READ_WRITE`；若無法，則回傳 `READ`。

- `READ`：可使用，但無法更新受眾。
- `READ_WRITE`：可使用並更新受眾。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].isIfaAudience

Boolean

在建立用於上傳使用者 ID 的受眾時所指定的、用以表示發送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設）：以使用者 ID 指定帳號。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].activated

Number

受眾啟用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].inactivatedTimestamp

Number

受眾停用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].expireTimestamp

Number

受眾過期時間，以 UNIX time 表示（單位為秒）。僅針對特定受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].requestId

String

建立受眾時所指定的請求 ID。僅當 `audienceGroups[].type` 為 `CLICK` 或 `IMP` 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].clickUrl

String

建立受眾時所指定的 URL。僅當 `audienceGroups[].type` 為 `CLICK` 且有指定連結 URL 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].failedType

String

操作失敗的原因。僅當 `audienceGroups[].status` 為 `FAILED` 或 `EXPIRED` 時才會包含此項目。為下列其中之一：

- `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT`：受眾中包含的使用者數量不足（至少需要 50 人）
- `INTERNAL_ERROR`：內部伺服器錯誤

<!-- parameter end -->
<!-- parameter start -->

hasNextPage

Boolean

當這不是最後一頁時為 `true`。

<!-- parameter end -->
<!-- parameter start -->

totalCount

Number

使用指定篩選條件可回傳的受眾總數。

<!-- parameter end -->
<!-- parameter start -->

readWriteAudienceGroupTotalCount

Number

在使用指定篩選條件可取得的受眾中，更新權限（`audienceGroups[].permission`）為 `READ_WRITE` 的受眾數量。

<!-- parameter end -->
<!-- parameter start -->

page

Number

目前的頁碼。

<!-- parameter end -->
<!-- parameter start -->

size

Number

目前頁面上的受眾最大數量。

<!-- parameter end -->

_範例回應_

<!-- tab start `json` -->

```json
// Example of when there are two audiences that match the specified filter
{
    "audienceGroups": [
        {
            "audienceGroupId": 1234567890123,
            "createRoute": "OA_MANAGER",
            "type": "CLICK",
            "description": "audienceGroupName_01",
            "status": "IN_PROGRESS",
            "audienceCount": 8619,
            "created": 1611114828,
            "permission": "READ",
            "isIfaAudience": false,
            "expireTimestamp": 1626753228,
            "requestId": "c10c3d86-f565-...",
            "clickUrl": "https://example.com/"
        },
        {
            "audienceGroupId": 2345678901234,
            "createRoute": "AD_MANAGER",
            "type": "APP_EVENT",
            "description": "audienceGroupName_02",
            "status": "READY",
            "audienceCount": 3368,
            "created": 1608619802,
            "permission": "READ",
            "activated": 1610068515,
            "inactiveTimestamp": 1625620516,
            "isIfaAudience": false
        }
    ],
    "hasNextPage": false,
    "totalCount": 2,
    "readWriteAudienceGroupTotalCount": 0,
    "size": 40,
    "page": 1
}

// Example of when there is no audience that matches the specified filter
{
    "audienceGroups": [],
    "hasNextPage": false,
    "totalCount": 0,
    "readWriteAudienceGroupTotalCount": 0,
    "size": 40,
    "page": 1
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code  | Description                              |
| ----- | ---------------------------------------- |
| `400` | 指定了無效的查詢參數。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_範例錯誤回應_

<!-- tab start `json` -->

```json
// If you specify an invalid query parameter (400 Bad Request)
{
  "message": "size: must be less than or equal to 40",
  "details": [
    {
      "message": "TOO_HIGH"
    }
  ]
}
```

<!-- tab end -->

### Get shared audience data in Business Manager 

端點：`GET` `https://api.line.me/v2/bot/audienceGroup/shared/{audienceGroupId}`

取得 [Business Manager](https://data.linebiz.com/solutions/business-manager)（僅提供日文）中的共享受眾。

<!-- tip start -->

**關於 Business Manager**

Business Manager 可讓您在多個服務之間共享特定受眾。透過在 Business Manager 中共享受眾，您可以更好地與終端使用者溝通。

如需更多資訊，請參閱 LINE DATA SOLUTION 中的 [Business Manager](https://data.linebiz.com/solutions/business-manager)（僅提供日文）。

<!-- tip end -->

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/audienceGroup/shared/{audienceGroupId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

audienceGroupId

您想取得相關資訊的受眾 ID。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

audienceGroup

Object

受眾群組物件。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.createRoute

String

受眾的建立方式。為下列其中之一：

- `OA_MANAGER`：以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾
- `MESSAGING_API`：以 Messaging API 建立的受眾
- `POINT_AD`：以 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾
- `AD_MANAGER`：以 [LINE Ads](https://admanager.line.biz/) 建立的受眾
- `BUSINESS_MANAGER`：以 [Business Manager](https://data.linebiz.com/solutions/business-manager) 建立的受眾
- `YAHOO_DISPLAY_ADS`：以 [LY Ads Display Ads](https://www.lycbiz.jp/en/#advertising) 建立的受眾

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.type

String

受眾類型。為下列其中之一：

- `UPLOAD`：用於上傳使用者 ID 的受眾
- `CLICK`：訊息點擊受眾
- `IMP`：訊息曝光受眾
- `CHAT_TAG`：聊天標籤受眾
- `FRIEND_PATH`：好友路徑受眾
- `RESERVATION`：預約受眾
- `RICHMENU_IMP`：圖文選單曝光受眾
- `RICHMENU_CLICK`：圖文選單點擊受眾
- `APP_EVENT`：App 事件受眾
- `VIDEO_VIEW`：影片觀看受眾
- `WEBTRAFFIC`：網站流量受眾（LINE Tag）
- `TRACKINGTAG_WEBTRAFFIC`：網站流量受眾（Tracking Tag）
- `IMAGE_CLICK`：圖片點擊受眾
- `POP_AD_IMP`：LINE Beacon Network 廣告曝光受眾

如需更多資訊，請參閱 LINE for Business 上的 [Audience](https://www.lycbiz.com/jp/manual/OfficialAccountManager/messages-audience/) 頁面。此頁面目前未提供英文版。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.status

String

受眾的狀態。為下列其中之一：

- `IN_PROGRESS`：處理中。狀態變更為 `READY` 可能需要數小時。對於有使用者數量限制的受眾，若受眾中包含的使用者數量不足（至少需要 50 人），狀態將維持為 `IN_PROGRESS` 而不會更新。
- `READY`：已可接收訊息。
- `FAILED`：建立受眾時發生錯誤。
- `EXPIRED`：已過期。受眾在過期後一個月會自動刪除。
- `INACTIVE`：受眾處於停用狀態。
- `ACTIVATING`：受眾正在啟用中。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.audienceCount

Number

受眾中包含的使用者數量。為保護使用者隱私，當數量少於 20 時會回傳 0，但下列受眾類型除外：

- 用於上傳使用者 ID 的受眾（以使用者 ID 指定收件者的情況）
- 聊天標籤受眾

由於受眾中可能包含已封鎖 LINE 官方帳號的使用者，`audienceGroup.audienceCount` 的值與實際發送訊息的使用者數量會有所不同。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.created

Number

受眾建立的時間，以 UNIX time 表示（單位為秒）。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.permission

String

受眾的更新權限。若目前的 Messaging API 頻道可以更新目標受眾，回傳 `READ_WRITE`；若無法，則回傳 `READ`。

- `READ`：可使用，但無法更新受眾。
- `READ_WRITE`：可使用並更新受眾。

<!-- parameter end -->
<!-- parameter start -->

audienceGroup.isIfaAudience

Boolean

在建立用於上傳使用者 ID 的受眾時所指定的、用以表示發送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設）：以使用者 ID 指定帳號。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].webtraffic

Object

[Web traffic object](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience-response-webtraffic)。僅當 `audienceGroups[].type` 為 `WEBTRAFFIC` 或 `TRACKINGTAG_WEBTRAFFIC` 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.requestId

String

建立受眾時所指定的請求 ID。僅當 `audienceGroup.type` 為 `CLICK` 或 `IMP` 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.clickUrl

String

建立受眾時所指定的 URL。僅當 `audienceGroup.type` 為 `CLICK` 且有指定連結 URL 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.failedType

String

操作失敗的原因。僅當 `audienceGroup.status` 為 `FAILED` 時才會包含此項目。為下列其中之一：

- `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT`：受眾中包含的使用者數量不足（至少需要 50 人）
- `INTERNAL_ERROR`：內部伺服器錯誤

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.activated

Number

受眾啟用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.inactivatedTimestamp

Number

受眾停用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroup.expireTimestamp

Number

受眾過期時間，以 UNIX time 表示（單位為秒）。僅針對特定受眾回傳。

<!-- parameter end -->
<!-- parameter start -->

jobs

Array

工作（job）的陣列。此陣列用於追蹤每一次將新使用者 ID 或 IFA 加入用於上傳使用者 ID 之受眾的嘗試。對於任何其他類型的受眾，會回傳空陣列。<br />最大值：50

<!-- parameter end -->
<!-- parameter start -->

jobs\[].audienceGroupJobId

Number

工作 ID。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].description

String

工作的描述。若您在新增使用者 ID 或 IFA 時未以 `uploadDescription` 屬性（property）指定值，則回傳 `null`。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].type

String

工作的類型。為下列其中之一：

- `DIFF_ADD`：表示透過 Messaging API 新增了使用者 ID 或 IFA。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].status

String

此屬性已淘汰。工作的狀態請參閱 `jobs[].jobStatus`。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].failedType

String

操作失敗的原因。僅當 `jobs[].jobStatus` 為 `FAILED` 時才會包含此項目。為下列其中之一：

- `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT`：受眾中包含的使用者數量不足（至少需要 50 人）
- `INTERNAL_ERROR`：內部伺服器錯誤

若 `jobs[].jobStatus` 不是 `FAILED`，則回傳 `null`。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].audienceCount

Number

新增或移除的帳號（收件者）數量。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].created

Number

工作建立的時間，以 UNIX time 表示（單位為秒）。

<!-- parameter end -->
<!-- parameter start -->

jobs\[].jobStatus

String

工作的狀態。為下列其中之一：

- `QUEUED`：等待執行
- `WORKING`：執行中
- `FINISHED`：已完成
- `FAILED`：失敗

<!-- parameter end -->
<!-- parameter start -->

owner.serviceType

String

建立受眾的服務名稱。為下列其中之一：

- `bm`：Business Manager
- `lap`：LINE Ads
- `account`：LINE 官方帳號
- `yda`：LY Ads

<!-- parameter end -->
<!-- parameter start -->

owner.id

String

建立受眾的帳號 ID。

<!-- parameter end -->
<!-- parameter start -->

owner.name

String

建立受眾的帳號名稱。

<!-- parameter end -->

_範例回應_

<!-- tab start `json` -->

```json
// Example of a web traffic audience
{
  "audienceGroup": {
    "audienceGroupId": 1234567890123,
    "createRoute": "BUSINESS_MANAGER",
    "type": "WEBTRAFFIC",
    "description": "Web traffic audience",
    "status": "READY",
    "audienceCount": 0,
    "created": 1668179144,
    "permission": "READ",
    "isIfaAudience": true,
    "webtraffic": {
      "webtrafficIsMyTag": false,
      "webtrafficBmTagSharingStatus": "SHARED",
      "webtrafficIsTagDeleted": false,
      "webtrafficTagCreateRoute": "OA_MANAGER",
      "webtrafficVisitType": "VISIT_ALL",
      "webtrafficRetentionDays": 30,
      "webtrafficTagId": "01234567-8901-2345-6789-012345678901",
      "webtrafficConditionGroup": [],
      "webtrafficTagOwnerName": "LINE Developers (@linedevelopers)"
    }
  },
  "jobs": [],
  "owner": {
    "serviceType": "bm",
    "id": "0123456789ABCDEFGHIJKLMNOP",
    "name": "LINE Developers"
  }
}
```

<!-- tab end -->

##### Web traffic object 

Web traffic object 代表網站流量受眾資料。

<!-- parameter start -->

webtrafficIsMyTag

Boolean

- 對於 LINE Tag：若 LINE Tag 是由連結至您的 Messaging API 頻道的 LINE 官方帳號所建立，則回傳 `true`。
- 對於 Tracking Tag：一律回傳 `false`。

<!-- parameter end -->
<!-- parameter start -->

webtrafficBmTagSharingStatus

String

用以表示網站流量受眾中所使用的 LINE Tag 或 Tracking Tag 在 Business Manager 共享狀態的值。

對於 LINE Tag，為下列其中之一：

- `SHARED`：已在 Business Manager 上共享。
- `UNSHARED`：未在 Business Manager 上共享。
- `ERROR`：因暫時性錯誤而無法取得標籤詳細資訊。

對於 Tracking Tag，為下列其中之一：

- `SHARED`：在 Business Manager 中建立此 Tracking Tag 的組織已連結至該 LINE 官方帳號。
- `UNSHARED`：在 Business Manager 中建立此 Tracking Tag 的組織未連結至該 LINE 官方帳號。
- `ERROR`：因暫時性錯誤而無法取得標籤詳細資訊。

如需更多關於將 Business Manager 組織與 LINE 官方帳號連結的資訊，請參閱 LINE for Business 中的 [How to link a LINE Official Account to an organization](https://help.linebiz.com/lineadshelp/s/article/L000001362?language=ja)（僅提供日文）。

<!-- parameter end -->
<!-- parameter start -->

webtrafficIsTagDeleted

Boolean

- 對於 LINE Tag：若此網站流量受眾中所使用的 LINE Tag 已被刪除，則回傳 `true`。
- 對於 Tracking Tag：一律回傳 `false`。

<!-- parameter end -->
<!-- parameter start -->

webtrafficTagCreateRoute

String

建立此網站流量受眾的途徑。為下列其中一個值：

- `OA_MANAGER`：以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾
- `AD_MANAGER`：以 [LINE Ads](https://admanager.line.biz/) 建立的受眾
- `BUSINESS_MANAGER`：以 [Business Manager](https://data.linebiz.com/solutions/business-manager) 建立的受眾

<!-- parameter end -->
<!-- parameter start -->

webtrafficVisitType

String

LINE Tag 或 Tracking Tag 的比對方式。為下列其中之一：

- `VISIT_ALL`：所有造訪的使用者
- `URL_MATCHING`：URL 條件
- `EVENT_MATCHING`：事件指定

<!-- parameter end -->
<!-- parameter start -->

webtrafficRetentionDays

String

網站流量受眾的保留期間。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

webtrafficTagEventType

String

事件代碼的類型。僅當 `webtrafficVisitType` 為 `EVENT_MATCHING` 時才會包含。為下列其中之一：

- `CONVERSION_EVENT`：轉換代碼
- `CUSTOM_EVENT`：自訂事件代碼

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

webtrafficCustomEventName

String

自訂事件名稱。僅當 `webtrafficVisitType` 為 `EVENT_MATCHING` 且 `webtrafficTagEventType` 為 `CUSTOM_EVENT` 時才會包含。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

webtrafficMatchingType

String

LINE Tag 或 Tracking Tag 的事件比對方式。僅當 `webtrafficVisitType` 為 `EVENT_MATCHING` 或 `URL_MATCHING` 時才會包含。值一律為 `NORMAL`。

<!-- parameter end -->
<!-- parameter start -->

webtrafficConditionGroup

Array

比對條件的陣列。

<!-- parameter end -->
<!-- parameter start -->

webtrafficConditionGroup\[].conditionType

String

`keywords` 陣列中關鍵字的比對條件。為下列其中之一：

- `CONTAIN`：包含關鍵字
- `NOT_CONTAIN`：不包含關鍵字
- `EQUAL_TO`：與關鍵字相符

<!-- parameter end -->
<!-- parameter start -->

webtrafficConditionGroup[].keywords[]

Array of strings

用於比對條件的關鍵字陣列。

<!-- parameter end -->
<!-- parameter start -->

webtrafficTagId

String

LINE Tag 或 Tracking Tag 的標籤 ID。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

webtrafficTagOwnerName

String

發行此 LINE Tag 的帳號名稱。僅當網站流量受眾使用 LINE Tag 時才會包含此項目。

<!-- parameter end -->

_範例_

<!-- tab start `json` -->

```json
{
  "webtrafficIsMyTag": false,
  "webtrafficBmTagSharingStatus": "SHARED",
  "webtrafficIsTagDeleted": false,
  "webtrafficTagCreateRoute": "OA_MANAGER",
  "webtrafficVisitType": "VISIT_ALL",
  "webtrafficRetentionDays": 30,
  "webtrafficTagId": "01234567-8901-2345-6789-012345678901",
  "webtrafficConditionGroup": [],
  "webtrafficTagOwnerName": "LINE Developers (@linedevelopers)"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code  | Description                           |
| ----- | ------------------------------------- |
| `400` | 指定了不存在的受眾。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_範例錯誤回應_

<!-- tab start `json` -->

```json
// If you specify a non-existent audience (400 Bad Request)
{
  "message": "audience group not found",
  "details": [
    {
      "message": "AUDIENCE_GROUP_NOT_FOUND"
    }
  ]
}
```

<!-- tab end -->

### Get a list of shared audiences in Business Manager 

端點：`GET` `https://api.line.me/v2/bot/audienceGroup/shared/list`

取得 [Business Manager](https://data.linebiz.com/solutions/business-manager)（僅提供日文）中的共享受眾清單。

您可以使用 [Get shared audience data in Business Manager](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience) 端點取得每個受眾的更詳細資訊。

<!-- tip start -->

**關於 Business Manager**

Business Manager 可讓您在多個服務之間共享特定受眾。透過在 Business Manager 中共享受眾，您可以更好地與終端使用者溝通。

如需更多資訊，請參閱 LINE DATA SOLUTION 中的 [Business Manager](https://data.linebiz.com/solutions/business-manager)（僅提供日文）。

<!-- tip end -->

_範例請求_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/audienceGroup/shared/list \
--data-urlencode 'page=1' \
--data-urlencode 'description=audienceGroupName' \
--data-urlencode 'size=40' \
--data-urlencode 'createRoute=OA_MANAGER' \
-G \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每分鐘 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

page

取得（分頁）結果時要回傳的頁碼。必須為 `1` 或更大。若省略，則取得第 1 頁。

若您想取得所有受眾，請重複發出請求並遞增 `page` 參數，直到回應中的 `audienceGroups` 陣列小於頁面大小（`size`）為止。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

description

要回傳的受眾名稱。可以搜尋部分相符的內容。此項目不區分大小寫，亦即 `AUDIENCE` 與 `audience` 視為相同。若省略，則不會以受眾名稱作為搜尋條件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

status

要回傳的受眾狀態。若省略，則不會以受眾狀態作為搜尋條件。為下列其中之一：

- `IN_PROGRESS`：處理中。
- `READY`：已可接收訊息。
- `FAILED`：建立受眾時發生錯誤。
- `EXPIRED`：已過期。受眾在過期後一個月會自動刪除。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

每頁的受眾數量。預設值：`20` \
最大值：`40`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

createRoute

受眾的建立方式。若省略，則包含所有受眾。

- `OA_MANAGER`：只回傳以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾。
- `MESSAGING_API`：只回傳以 Messaging API 建立的受眾。
- `POINT_AD`：只回傳以 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾。
- `AD_MANAGER`：只回傳以 [LINE Ads](https://admanager.line.biz/) 建立的受眾。
- `BUSINESS_MANAGER`：只回傳以 [Business Manager](https://data.linebiz.com/solutions/business-manager) 建立的受眾。
- `YAHOO_DISPLAY_ADS`：只回傳以 [LY Ads Display Ads](https://www.lycbiz.jp/en/#advertising) 建立的受眾。

若指定多個參數，則使用 OR 條件。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

includesOwnedAudienceGroups

此設定用以表示除了 Business Manager 中的共享受眾外，是否也包含您的 LINE 官方帳號所建立的受眾。預設值為 `false`。

- `true`：取得受眾，包含您的 LINE 官方帳號所建立的受眾
- `false`：只取得 Business Manager 中的共享受眾

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼，以及包含下列資訊的 JSON 物件。

<!-- parameter start -->

audienceGroups

Array

受眾資料的陣列。若沒有符合指定篩選條件的受眾，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].audienceGroupId

Number

受眾 ID。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].createRoute

String

受眾的建立方式。為下列其中之一：

- `OA_MANAGER`：以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾
- `MESSAGING_API`：以 Messaging API 建立的受眾
- `POINT_AD`：以 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾
- `AD_MANAGER`：以 [LINE Ads](https://admanager.line.biz/) 建立的受眾
- `BUSINESS_MANAGER`：以 [Business Manager](https://data.linebiz.com/solutions/business-manager) 建立的受眾
- `YAHOO_DISPLAY_ADS`：以 [LY Ads Display Ads](https://www.lycbiz.jp/en/#advertising) 建立的受眾

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].type

String

受眾類型。為下列其中之一：

- `UPLOAD`：用於上傳使用者 ID 的受眾
- `CLICK`：訊息點擊受眾
- `IMP`：訊息曝光受眾
- `CHAT_TAG`：聊天標籤受眾
- `FRIEND_PATH`：好友路徑受眾
- `RESERVATION`：預約受眾
- `RICHMENU_IMP`：圖文選單曝光受眾
- `RICHMENU_CLICK`：圖文選單點擊受眾
- `APP_EVENT`：App 事件受眾
- `VIDEO_VIEW`：影片觀看受眾
- `WEBTRAFFIC`：網站流量受眾（LINE Tag）
- `TRACKINGTAG_WEBTRAFFIC`：網站流量受眾（Tracking Tag）
- `IMAGE_CLICK`：圖片點擊受眾
- `POP_AD_IMP`：LINE Beacon Network 廣告曝光受眾

如需更多資訊，請參閱 LINE for Business 上的 [Audience](https://www.lycbiz.com/jp/manual/OfficialAccountManager/messages-audience/)（僅提供日文）。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].description

String

受眾的名稱。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].status

String

受眾的狀態。為下列其中之一：

- `IN_PROGRESS`：處理中。狀態變更為 `READY` 可能需要數小時。對於有使用者數量限制的受眾，若受眾中包含的使用者數量不足（至少需要 50 人），狀態將維持為 `IN_PROGRESS` 而不會更新。
- `READY`：已可接收訊息。
- `FAILED`：建立受眾時發生錯誤。
- `EXPIRED`：已過期。受眾在過期後一個月會自動刪除。
- `INACTIVE`：受眾處於停用狀態。
- `ACTIVATING`：受眾正在啟用中。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].audienceCount

Number

受眾中包含的使用者數量。為保護使用者隱私，當數量少於 20 時會回傳 0，但下列受眾類型除外：

- 用於上傳使用者 ID 的受眾（以使用者 ID 指定收件者的情況）
- 聊天標籤受眾

由於受眾中可能包含已封鎖 LINE 官方帳號的使用者，`audienceGroups[].audienceCount` 的值與實際發送訊息的使用者數量會有所不同。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].created

Number

受眾建立的時間，以 UNIX time 表示（單位為秒）。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].permission

String

受眾的更新權限。若目前的 Messaging API 頻道可以更新目標受眾，回傳 `READ_WRITE`；若無法，則回傳 `READ`。

- `READ`：可使用，但無法更新受眾。
- `READ_WRITE`：可使用並更新受眾。

<!-- parameter end -->
<!-- parameter start -->

audienceGroups\[].isIfaAudience

Boolean

在建立用於上傳使用者 ID 的受眾時所指定的、用以表示發送對象帳號類型的值。為下列其中之一：

- `true`：以 IFA 指定帳號。
- `false`（預設）：以使用者 ID 指定帳號。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].activated

Number

受眾啟用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].inactivatedTimestamp

Number

受眾停用的時間。僅針對以 [LINE Ads](https://admanager.line.biz/) 或 [LINE Points Ads](https://www.lycbiz.com/jp/service/line-point-ad/)（僅提供日文）建立的受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].expireTimestamp

Number

受眾過期時間，以 UNIX time 表示（單位為秒）。僅針對特定受眾回傳。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].webtraffic

Object

[Web traffic object](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience-list-response-webtraffic)。僅當 `audienceGroups[].type` 為 `WEBTRAFFIC` 或 `TRACKINGTAG_WEBTRAFFIC` 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].requestId

String

建立受眾時所指定的請求 ID。僅當 `audienceGroups[].type` 為 `CLICK` 或 `IMP` 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].clickUrl

String

建立受眾時所指定的 URL。僅當 `audienceGroups[].type` 為 `CLICK` 且有指定連結 URL 時才會包含此項目。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

audienceGroups\[].failedType

String

操作失敗的原因。僅當 `audienceGroups[].status` 為 `FAILED` 或 `EXPIRED` 時才會包含此項目。為下列其中之一：

- `AUDIENCE_GROUP_AUDIENCE_INSUFFICIENT`：受眾中包含的使用者數量不足（至少需要 50 人）
- `INTERNAL_ERROR`：內部伺服器錯誤

<!-- parameter end -->
<!-- parameter start -->

hasNextPage

Boolean

當這不是最後一頁時為 `true`。

<!-- parameter end -->
<!-- parameter start -->

totalCount

Number

使用指定篩選條件可回傳的受眾總數。

<!-- parameter end -->
<!-- parameter start -->

readWriteAudienceGroupTotalCount

Number

在使用指定篩選條件可取得的受眾中，更新權限（`audienceGroups[].permission`）為 `READ_WRITE` 的受眾數量。

<!-- parameter end -->
<!-- parameter start -->

page

Number

目前的頁碼。

<!-- parameter end -->
<!-- parameter start -->

size

Number

目前頁面上的受眾最大數量。

<!-- parameter end -->

_範例回應_

<!-- tab start `json` -->

```json
// Example of when there are two audiences that match the specified filter
{
  "audienceGroups": [
    {
      "audienceGroupId": 1234567890123,
      "createRoute": "BUSINESS_MANAGER",
      "type": "WEBTRAFFIC",
      "description": "Web traffic audience",
      "status": "READY",
      "audienceCount": 4871,
      "created": 1668179144,
      "permission": "READ",
      "isIfaAudience": true,
      "webtraffic": {
        "webtrafficIsMyTag": false,
        "webtrafficBmTagSharingStatus": "SHARED",
        "webtrafficIsTagDeleted": false,
        "webtrafficTagCreateRoute": "OA_MANAGER"
      }
    },
    {
      "audienceGroupId": 3210987654321,
      "createRoute": "AD_MANAGER",
      "type": "IMAGE_CLICK",
      "description": "Image click audience",
      "status": "IN_PROGRESS",
      "audienceCount": 2234,
      "created": 1718895503,
      "permission": "READ",
      "isIfaAudience": true
    }
  ],
  "hasNextPage": false,
  "totalCount": 2,
  "readWriteAudienceGroupTotalCount": 0,
  "size": 40,
  "page": 1
}

// Example of when there is no audience that matches the specified filter
{
    "audienceGroups": [],
    "hasNextPage": false,
    "totalCount": 0,
    "readWriteAudienceGroupTotalCount": 0,
    "size": 40,
    "page": 1
}
```

<!-- tab end -->

##### Web traffic object 

Web traffic object 代表網站流量受眾資料。

<!-- parameter start -->

webtrafficIsMyTag

Boolean

- 對於 LINE Tag：若 LINE Tag 是由連結至您的 Messaging API 頻道的 LINE 官方帳號所建立，則回傳 `true`。
- 對於 Tracking Tag：一律回傳 `false`。

<!-- parameter end -->
<!-- parameter start -->

webtrafficBmTagSharingStatus

String

用以表示網站流量受眾中所使用的 LINE Tag 或 Tracking Tag 在 Business Manager 共享狀態的值。

對於 LINE Tag，為下列其中之一：

- `SHARED`：已在 Business Manager 上共享。
- `UNSHARED`：未在 Business Manager 上共享。
- `ERROR`：因暫時性錯誤而無法取得標籤詳細資訊。

對於 Tracking Tag，為下列其中之一：

- `SHARED`：在 Business Manager 中建立此 Tracking Tag 的組織已連結至該 LINE 官方帳號。
- `UNSHARED`：在 Business Manager 中建立此 Tracking Tag 的組織未連結至該 LINE 官方帳號。
- `ERROR`：因暫時性錯誤而無法取得標籤詳細資訊。

如需更多關於將 Business Manager 組織與 LINE 官方帳號連結的資訊，請參閱 LINE for Business 中的 [How to link a LINE Official Account to an organization](https://help.linebiz.com/lineadshelp/s/article/L000001362?language=ja)（僅提供日文）。

<!-- parameter end -->
<!-- parameter start -->

webtrafficIsTagDeleted

Boolean

- 對於 LINE Tag：若此網站流量受眾中所使用的 LINE Tag 已被刪除，則回傳 `true`。
- 對於 Tracking Tag：一律回傳 `false`。

<!-- parameter end -->
<!-- parameter start -->

webtrafficTagCreateRoute

String

建立此網站流量受眾的途徑。為下列其中一個值：

- `OA_MANAGER`：以 [LINE Official Account Manager](https://manager.line.biz/) 建立的受眾
- `AD_MANAGER`：以 [LINE Ads](https://admanager.line.biz/) 建立的受眾
- `BUSINESS_MANAGER`：以 [Business Manager](https://data.linebiz.com/solutions/business-manager) 建立的受眾

<!-- parameter end -->

_範例_

<!-- tab start `json` -->

```json
{
  "webtrafficIsMyTag": false,
  "webtrafficBmTagSharingStatus": "UNSHARED",
  "webtrafficIsTagDeleted": false,
  "webtrafficTagCreateRoute": "BUSINESS_MANAGER"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼與錯誤回應：

| Code  | Description                              |
| ----- | ---------------------------------------- |
| `400` | 指定了無效的查詢參數。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_範例錯誤回應_

<!-- tab start `json` -->

```json
// If you specify an invalid query parameter (400 Bad Request)
{
  "message": "size: must be less than or equal to 40",
  "details": [
    {
      "message": "TOO_HIGH"
    }
  ]
}
```

<!-- tab end -->
## Insights 

你可以取得從 LINE 官方帳號發送的訊息數量、好友數量，以及其他統計資料的相關資訊。

### Get number of message deliveries 

端點（Endpoint）: `GET` `https://api.line.me/v2/bot/insight/message/delivery?date={date}`

回傳在 `date` 所指定的日期當天，從 LINE 官方帳號發送的訊息數量。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/insight/message/delivery?date=20190418' \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制（rate limit）的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

date

要查詢已發送訊息數量的日期。

- 格式：`yyyyMMdd`（例如 `20191231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個帶有下列屬性（property）的 JSON 物件（object）：

<!-- parameter start -->

status

String

計算處理的狀態。為下列其中之一：

- `ready`：計算已完成；數字為最新狀態。
- `unready`：我們尚未完成指定 `date` 的已發送訊息數量計算。請稍後再試。計算通常需要約一天。
- `out_of_service`：指定的 `date` 早於我們開始計算已發送訊息的起始日期（2017 年 3 月 1 日）。

`broadcast` 屬性之後的各屬性，只有在 `state` 屬性為 `ready` 時才會包含。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

broadcast

Number

在 LINE 官方帳號管理介面（LINE Official Account Manager）中選擇 **All Friends** 作為收件對象所發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

targeting

Number

在 LINE 官方帳號管理介面中選擇 **Targeting** 作為收件對象所發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

stepMessage

Number

在 LINE 官方帳號管理介面中以分眾訊息（step messages）發送的訊息數量。

如需更多資訊，請參閱 LINE for Business 中的 [Step messages](https://www.linebiz.com/jp/manual/OfficialAccountManager/step-message/)（僅提供日文）。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

autoResponse

Number

當收到使用者訊息時自動發送的自動回應訊息數量。

如需更多資訊，請參閱 LINE for Business 中的 [Auto-response messages](https://www.lycbiz.com/jp/manual/OfficialAccountManager/Auto-response-messages/)（僅提供日文）。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

welcomeResponse

Number

當使用者將 LINE 官方帳號加為好友時自動發送的問候訊息數量。

如需更多資訊，請參閱 LINE for Business 中的 [Set greeting messages](https://www.lycbiz.com/jp/manual/OfficialAccountManager/greeting-message/)（僅提供日文）。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

chat

Number

從 LINE 官方帳號管理介面 [Chat screen](https://www.lycbiz.com/jp/manual/OfficialAccountManager/chats/)（僅提供日文）發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

apiBroadcast

Number

使用 [Send broadcast message](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message) 端點發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

apiPush

Number

使用 [Send push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message) 端點發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

apiMulticast

Number

使用 [Send multicast message](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message) 端點發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

apiNarrowcast

Number

使用 [Send narrowcast message](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message) 端點發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

apiReply

Number

使用 [Send reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message) 端點發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

ccAutoReply

Number

透過 LINE Chat Plus 自動回覆所發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

ccManualReply

Number

透過 LINE Chat Plus 人工聊天支援所發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pnpNoticeMessage

Number

針對企業客戶選項，使用 [LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/overview/) 所發送的訊息數量。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pnpCallToLine

Number

使用 Call to LINE 所發送的訊息數量。\*

\* Call to LINE 已停止接受新註冊。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

thirdPartyChatTool

Number

從第三方聊天工具發送的訊息數量。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// If the calculation has finished
{
  "status": "ready",
  "broadcast": 5385,
  "targeting": 522
}

// if the calculation hasn't finished yet
{
  "status": "unready"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼以及一個錯誤回應（error response）：

| Code  | Description                   |
| ----- | ----------------------------- |
| `400` | 指定了無效的日期。            |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 區段中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid date (400 Bad Request)
{
  "message": "Bad Request"
}
```

<!-- tab end -->

### Get number of followers 

端點（Endpoint）: `GET` `https://api.line.me/v2/bot/insight/followers?date={date}`

回傳在指定日期當天或之前已加入該 LINE 官方帳號的使用者數量。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/insight/followers?date=20190418' \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

date

要查詢好友數量的日期。

- 格式：`yyyyMMdd`（例如 `20191231`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個帶有下列屬性的 JSON 物件：

<!-- parameter start -->

status

String

計算狀態。為下列其中之一：

- `ready`：計算已完成。數字為最新狀態。
- `unready`：我們尚未完成指定 `date` 的好友數量計算。請稍後再試。計算通常需要約一天。
- `out_of_service`：指定的 `date` 早於我們開始計算好友數量的起始日期（2016 年 11 月 1 日）。

<!-- parameter end -->
<!-- parameter start -->

followers

Number

截至指定 `date`，使用者首次將此 LINE 官方帳號加為好友的次數。即使使用者之後封鎖該帳號，或刪除其 LINE 帳號，此數字也不會減少。

如果 `status` 屬性不是 `ready`，此值為 `null`。

<!-- parameter end -->
<!-- parameter start -->

targetedReaches

Number

截至指定 `date`，該 LINE 官方帳號可透過依性別、年齡及／或地區進行目標投放（targeted）訊息所觸及的使用者數量。此數字僅包含在 LINE 或 LINE 服務中活躍，且人口統計屬性可信度高的使用者。

如果 `status` 屬性不是 `ready`，此值為 `null`。

<!-- parameter end -->
<!-- parameter start -->

blocks

Number

截至指定 `date`，封鎖該帳號的使用者數量。當使用者解除封鎖該帳號時，此數字會減少。

如果 `status` 屬性不是 `ready`，此值為 `null`。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// If the calculation has finished
{
  "status": "ready",
  "followers": 7620,
  "targetedReaches": 5848,
  "blocks": 237
}

// if the calculation hasn't finished yet
{
  "status": "unready",
  "followers": null,
  "targetedReaches": null,
  "blocks": null
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼以及一個錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 未指定日期或指定了無效的日期。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 區段中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you don't specify a date (400 Bad Request)
{
  "message": "date is required"
}

// If you specify an invalid date (400 Bad Request)
{
  "message": "Bad Request"
}
```

<!-- tab end -->

### Get friend demographics 

端點（Endpoint）: `GET` `https://api.line.me/v2/bot/insight/demographic`

取得該 LINE 官方帳號好友的好友人口統計資訊（friend demographic information）。要取得好友人口統計資訊，必須符合下列所有條件：

- 目標觸及人數（target reach）為 20 人或以上。
- 該 LINE 官方帳號由位於日本（JP）、泰國（TH）或台灣（TW）的使用者所建立。

<!-- note start -->

**非即時資料**

好友人口統計資訊需要約 3 天才會反映。因此，所能取得的資訊大約是 3 天前的資料。請注意，反映的時間點可能會有所不同。

<!-- note end -->

<!-- tip start -->

**關於好友人口統計資訊**

好友人口統計資訊是依據 LINE 使用者在 LINE Family 服務中登錄的性別、年齡、地區資訊及行為歷程，被歸類為「推定屬性（deemed attributes）」。推定屬性不包含行動電信業者及作業系統。

推定屬性是依據各種趨勢來分類，例如在 LINE 上購買及使用的貼圖、感興趣的內容，以及使用者成為好友的 LINE 官方帳號類型等。電話號碼、電子郵件地址、通訊錄及聊天內容等敏感資訊，並不會被納入作為分類依據的資訊中。

好友人口統計資訊的推估屬於統計性質，並不會識別特定個人。可能識別特定個人的資訊不會與第三方（例如廣告主）分享。

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/insight/demographic \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個帶有下列屬性的 JSON 物件：

<!-- parameter start -->

available

Boolean

- `true`：可取得好友人口統計資訊。
- `false`：無法取得好友人口統計資訊。請考慮下列原因：
  - 目標觸及人數少於 20 人。
  - 該 LINE 官方帳號並非由位於日本（JP）、泰國（TH）或台灣（TW）的使用者所建立。

回應中每個陣列（`genders`、`ages`、`areas`、`appTypes`、`subscriptionPeriods`）的各元素，只有在 `available` 的值為 `true` 時才會包含在回應中。

<!-- parameter end -->
<!-- parameter start -->

genders

Array

各性別所佔的百分比。如果無法取得好友人口統計資訊，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

genders\[].gender

String

依據使用者的性別回傳下列值：

- `male`
- `female`
- `unknown`

<!-- parameter end -->
<!-- parameter start -->

genders\[].percentage

Number

百分比

<!-- parameter end -->
<!-- parameter start -->

ages

Array

各年齡層所佔的百分比。如果無法取得好友人口統計資訊，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

ages\[].age

String

依據使用者的年齡回傳下列值：

<!-- note start -->

**當你使用泰國 LINE 官方帳號時**

當你取得泰國 LINE 官方帳號的人口統計資訊時，`ages[].age` 值為 `from0to14` 與 `from15to19` 的百分比不會包含在回應中。20 歲以下的使用者會被計入 `unknown`。

<!-- note end -->

- `from0to14`
- `from15to19`
- `from20to24`
- `from25to29`
- `from30to34`
- `from35to39`
- `from40to44`
- `from45to49`
- `from50`
  - 自 2024 年 9 月 5 日起，[你現在可以取得 50 至 70 歲之間好友的百分比](https://developers.line.biz/en/news/2024/09/05/age-percentage-subdivision/)。
- `from50to54`
- `from55to59`
- `from60to64`
- `from65to69`
- `from70`
- `unknown`

<!-- parameter end -->
<!-- parameter start -->

ages\[].percentage

Number

百分比

<!-- parameter end -->
<!-- parameter start -->

areas

Array

各地區所佔的百分比。如果無法取得好友人口統計資訊，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

areas\[].area

String

依據使用者的國家與地區回傳下列值： \
**JP**

- `北海道` (Hokkaido)
- `青森` (Aomori)
- `岩手` (Iwate)
- `宮城` (Miyagi)
- `秋田` (Akita)
- `山形` (Yamagata)
- `福島` (Fukushima)
- `茨城` (Ibaraki)
- `栃木` (Tochigi)
- `群馬` (Gunma)
- `埼玉` (Saitama)
- `千葉` (Chiba)
- `東京` (Tokyo)
- `神奈川` (Kanagawa)
- `新潟` (Niigata)
- `富山` (Toyama)
- `石川` (Ishikawa)
- `福井` (Fukui)
- `山梨` (Yamanashi)
- `長野` (Nagano)
- `岐阜` (Gifu)
- `静岡` (Shizuoka)
- `愛知` (Aichi)
- `三重` (Mie)
- `滋賀` (Shiga)
- `京都` (Kyoto)
- `大阪` (Osaka)
- `兵庫` (Hyogo)
- `奈良` (Nara)
- `和歌山` (Wakayama)
- `鳥取` (Tottori)
- `島根` (Shimane)
- `岡山` (Okayama)
- `広島` (Hiroshima)
- `山口` (Yamaguchi)
- `徳島` (Tokushima)
- `香川` (Kagawa)
- `愛媛` (Ehime)
- `高知` (Kochi)
- `福岡` (Fukuoka)
- `佐賀` (Saga)
- `長崎` (Nagasaki)
- `熊本` (Kumamoto)
- `大分` (Oita)
- `宮崎` (Miyazaki)
- `鹿児島` (Kagoshima)
- `沖縄` (Okinawa)
- `unknown`

**TW**

- `台北市` (Taipei City)
- `新北市` (New Taipei City)
- `桃園市` (Taoyuan City)
- `台中市` (Taichung)
- `台南市` (Tainan City)
- `高雄市` (Kaohsiung)
- `基隆市` (Keelung)
- `新竹市` (Hsinchu City)
- `嘉義市` (Chiayi City)
- `新竹縣` (Hisnchu County)
- `苗栗縣` (Miaoli County)
- `彰化縣` (Changhua County)
- `南投縣` (Nantou County)
- `雲林縣` (Yunlin County)
- `嘉義縣` (Chiayi County)
- `屏東縣` (Pingtung County)
- `宜蘭縣` (Yilan County)
- `花蓮縣` (Hualien County)
- `台東縣` (Taitung County)
- `澎湖縣` (Penghu County)
- `金門縣` (Kinmen County)
- `連江縣` (Lianjiang County)
- `unknown`

**TH**

- `Bangkok`
- `Pattaya`
- `Northern`
- `Central`
- `Southern`
- `Eastern`
- `NorthEastern`
- `Western`
- `unknown`

<!-- parameter end -->
<!-- parameter start -->

areas\[].percentage

Number

百分比

<!-- parameter end -->
<!-- parameter start -->

appTypes

Array

各作業系統（OS）所佔的百分比。如果無法取得好友人口統計資訊，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

appTypes\[].appType

String

依據使用者的作業系統回傳下列值：

- `ios`
- `android`
- `others`

<!-- parameter end -->
<!-- parameter start -->

appTypes\[].percentage

Number

百分比

<!-- parameter end -->
<!-- parameter start -->

subscriptionPeriods

Array

各好友關係期間（friendship duration）所佔的百分比。如果無法取得好友人口統計資訊，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

subscriptionPeriods\[].subscriptionPeriod

String

回傳下列好友關係期間的值。「好友關係期間」的定義為，自使用者將 LINE 官方帳號加為好友的隔天起算的時間長度。

- `within7days`：少於 7 天
- `within30days`：大於或等於 7 天但少於 30 天
- `within90days`：大於或等於 30 天但少於 90 天
- `within180days`：大於或等於 90 天但少於 180 天
- `within365days`：大於或等於 180 天但少於 365 天
- `over365days`：大於或等於 365 天
- `unknown`：未知

<!-- parameter end -->
<!-- parameter start -->

subscriptionPeriods\[].percentage

Number

對應各個 `subscriptionPeriod` 值的使用者百分比。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// If the friend demographic information isn't available because the target reach is lower than 20
{
  "available": false,
  "genders": [],
  "ages": [],
  "areas": [],
  "appTypes": [],
  "subscriptionPeriods": []
}

// If the friend demographic information is available because the target reach is 20 or higher
{
    "available": true,
    "genders": [
        {
            "gender": "unknown",
            "percentage": 37.6
        },
        {
            "gender": "male",
            "percentage": 31.8
        },
        {
            "gender": "female",
            "percentage": 30.6
        }
    ],
    "ages": [
        {
            "age": "unknown",
            "percentage": 37.6
        },
        {
            "age": "from50",
            "percentage": 17.3
        },
        ...
    ],
    "areas": [
        {
            "area": "unknown",
            "percentage": 42.9
        },
        {
            "area": "徳島",
            "percentage": 2.9
        },
        ...
    ],
    "appTypes": [
        {
            "appType": "ios",
            "percentage": 62.4
        },
        {
            "appType": "android",
            "percentage": 27.7
        },
        {
            "appType": "others",
            "percentage": 9.9
        }
    ],
    "subscriptionPeriods": [
        {
            "subscriptionPeriod": "over365days",
            "percentage": 96.4
        },
        {
            "subscriptionPeriod": "within365days",
            "percentage": 1.9
        },
        {
            "subscriptionPeriod": "within180days",
            "percentage": 1.2
        },
        {
            "subscriptionPeriod": "within90days",
            "percentage": 0.5
        },
        {
            "subscriptionPeriod": "within30days",
            "percentage": 0.1
        },
        {
            "subscriptionPeriod": "within7days",
            "percentage": 0
        }
    ]
}
```

<!-- tab end -->

#### Error response 

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 區段中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

### Get user interaction statistics 

端點（Endpoint）: `GET` `https://api.line.me/v2/bot/insight/message/event?requestId={requestId}`

回傳使用者如何與你 LINE 官方帳號所發送的 narrowcast 訊息或 broadcast 訊息互動的統計資料。

你可以取得每則訊息或每個泡泡（bubble）的統計資料。

![message and bubbles](https://developers.line.biz/media/messaging-api/get-message-event.png)

<!-- note start -->

**關於記錄的統計資料**

互動資料僅在訊息發送後的 14 天（1,209,600 秒）內更新。超過該時間後，互動資料就不再更新。

例如，如果你在 2021 年 2 月 1 日 15:00 發送訊息，互動資料會更新至 2021 年 2 月 15 日 15:00。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/insight/message/event?requestId=f70dd685-499a-4231-a441-f24b8d4fba21' \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

requestId

narrowcast 訊息或 broadcast 訊息的請求 ID（Request ID）。每個 Messaging API 請求都有一個請求 ID。可在[回應標頭（response headers）](https://developers.line.biz/en/reference/messaging-api/#response-headers)中找到它。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個帶有下列屬性的 JSON 物件：

<!-- note start -->

**Note**

統計資料可能含有部分誤差。

為保護使用者隱私，在下列情況下，與使用者互動相關的部分屬性值會顯示為 `null`：

- 屬性值小於 20
- 即使屬性值大於或等於 20，但實際產生該事件的使用者人數少於 20（例如，若 `messages[].mediaPlayed` 為 30，但 `messages[].uniqueMediaPlayed` 為 15，則兩者都會顯示為 `null`）

<!-- note end -->

<!-- parameter start -->

overview

Object

訊息統計資料摘要。

<!-- parameter end -->
<!-- parameter start -->

overview.requestId

String

請求 ID。

<!-- parameter end -->
<!-- parameter start -->

overview.timestamp

Number

訊息發送時間，以 UNIX 時間表示（單位為秒）。

<!-- parameter end -->
<!-- parameter start -->

overview.delivered

Number

已送達的訊息數量。此屬性會顯示小於 20 的值。不過，若所有訊息尚未發送完成，則為 null。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueImpression

Number

開啟該訊息（即至少顯示了 1 個泡泡）的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueClick

Number

開啟訊息中任一 URL 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueMediaPlayed

Number

開始播放訊息中任一影片或音訊的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueMediaPlayed100Percent

Number

完整播放訊息中任一影片或音訊的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages

Array

關於各個訊息泡泡的資訊陣列。如果無法取得統計資料，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

messages\[].seq

Number

泡泡的序號。

<!-- parameter end -->
<!-- parameter start -->

messages\[].impression

Number

泡泡被顯示的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed

Number

泡泡中音訊或影片開始播放的次數。此計數也包含影片被自動播放的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed25Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 25% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed50Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 50% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed75Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 75% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed100Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 100% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed

Number

開始播放泡泡中音訊或影片的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed25Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 25% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed50Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 50% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed75Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 75% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed100Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 100% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

clicks

Array

關於訊息中被開啟的 URL 的資訊陣列。如果訊息不含任何 URL，或無法取得統計資料，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].seq

Number

URL 的序號。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].url

String

URL。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].click

Number

該 URL 被開啟的次數。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].uniqueClick

Number

開啟該 URL 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].uniqueClickOfRequest

Number

透過訊息中任一連結開啟此 `url` 的使用者數量。如果一則訊息含有兩個指向相同 URL 的連結，且使用者開啟了這兩個連結，則只計算一次。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// If the statistic isn't available because the value of each property is lower than 20
{
  "overview": {
    "requestId": "a425a5cd-6510-43fe-95be-a27f222e5dc0",
    "timestamp": 1711684800,
    "delivered": 1,
    "uniqueImpression": null,
    "uniqueClick": null,
    "uniqueMediaPlayed": null,
    "uniqueMediaPlayed100Percent": null
  },
  "messages": [],
  "clicks": []
}

// If the statistic is available because the value of each property is 20 or higher
{
  "overview": {
    "requestId": "f70dd685-499a-4231-a441-f24b8d4fba21",
    "timestamp": 1568214000,
    "delivered": 320,
    "uniqueImpression": 82,
    "uniqueClick": 51,
    "uniqueMediaPlayed": null,
    "uniqueMediaPlayed100Percent": null
  },
  "messages": [
    {
      "seq": 1,
      "impression": 136,
      "mediaPlayed": null,
      "mediaPlayed25Percent": null,
      "mediaPlayed50Percent": null,
      "mediaPlayed75Percent": null,
      "mediaPlayed100Percent": null,
      "uniqueMediaPlayed": null,
      "uniqueMediaPlayed25Percent": null,
      "uniqueMediaPlayed50Percent": null,
      "uniqueMediaPlayed75Percent": null,
      "uniqueMediaPlayed100Percent": null
    }
  ],
  "clicks": [
    {
      "seq": 1,
      "url": "https://line.me/",
      "click": 41,
      "uniqueClick": 30,
      "uniqueClickOfRequest": 30
    },
    {
      "seq": 1,
      "url": "https://www.lycorp.co.jp/",
      "click": 59,
      "uniqueClick": 38,
      "uniqueClickOfRequest": 38
    }
  ]
}
```

<!-- tab end -->

#### Error response 

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 區段中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

### Get statistics per unit 

端點（Endpoint）: `GET` `https://api.line.me/v2/bot/insight/message/event/aggregation?customAggregationUnit={customAggregationUnit}&from={from}&to={to}`

你可以查看使用者如何與你 LINE 官方帳號所發送的 push 訊息及 multicast 訊息互動的「每單位（per-unit）」統計資料。

你可以針對每個單位，取得每則訊息及每個訊息泡泡為基礎的統計資料。

![message and bubbles](https://developers.line.biz/media/messaging-api/get-message-event.png)

如果你以相同的單位名稱發送訊息，無論訊息內容或訊息泡泡的數量與順序為何，統計資料都會被彙總在一起。

<!-- note start -->

**關於記錄的統計資料**

互動資料僅在訊息發送後的 14 天（1,209,600 秒）內更新。超過該時間後，互動資料就不再更新。

例如，如果你在 2021 年 2 月 1 日 15:00 發送訊息，互動資料會更新至 2021 年 2 月 15 日 15:00。

<!-- note end -->

<!-- tip start -->

**要取得每則訊息的統計資料**

使用此端點以取得每則 narrowcast 訊息或 broadcast 訊息的統計資料。

- [Get user interaction statistics](https://developers.line.biz/en/reference/messaging-api/#get-message-event)

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/insight/message/event/aggregation \
-H 'Authorization: Bearer {channel access token}' \
--data-urlencode 'customAggregationUnit=promotion_a' \
--data-urlencode 'from=20210301' \
--data-urlencode 'to=20210331' \
-G
```

<!-- tab end -->

#### Rate limit 

每小時 60 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

customAggregationUnit

String

發送訊息時所指定的彙總單位名稱。區分大小寫。例如，`Promotion_a` 與 `Promotion_A` 會被視為不同的單位名稱。

如需更多關於指派單位名稱的資訊，請參閱 Messaging API 文件中的 [Assign a unit name](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/#assign-names-to-units-when-sending-messages)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

from

String

彙總期間的開始日期。

- 格式：`yyyyMMdd`（例如 `20210301`）
- 時區：UTC+9

<!-- parameter end -->
<!-- parameter start (props: required) -->

to

String

彙總期間的結束日期。結束日期最多可指定到 30 天之後。例如，若開始日期為 `20210301`，則最晚的結束日期為 `20210331`。

- 格式：`yyyyMMdd`（例如 `20210301`）
- 時區：UTC+9

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及一個帶有下列資訊的 JSON 物件。

<!-- note start -->

**Note**

統計資料可能含有部分誤差。

為保護使用者隱私，在下列情況下，與使用者互動相關的部分屬性值會顯示為 `null`：

- 屬性值小於 20
- 即使屬性值大於或等於 20，但實際產生該事件的使用者人數少於 20（例如，若 `messages[].mediaPlayed` 為 30，但 `messages[].uniqueMediaPlayed` 為 15，則兩者都會顯示為 `null`）

<!-- note end -->

<!-- parameter start -->

overview

Object

與訊息相關的統計資料。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueImpression

Number

開啟該訊息（即至少顯示了 1 個泡泡）的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueClick

Number

開啟訊息中任一 URL 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueMediaPlayed

Number

開始播放訊息中任一影片或音訊的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

overview.uniqueMediaPlayed100Percent

Number

完整播放訊息中任一影片或音訊的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages

Array

關於各個訊息泡泡的資訊陣列。如果無法取得統計資料，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

messages\[].seq

Number

泡泡的序號。

<!-- parameter end -->
<!-- parameter start -->

messages\[].impression

Number

泡泡被顯示的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueImpression

Number

顯示了該泡泡的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed

Number

泡泡中音訊或影片開始播放的次數。此計數也包含影片被自動播放的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed25Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 25% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed50Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 50% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed75Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 75% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].mediaPlayed100Percent

Number

泡泡中音訊或影片開始播放並播放至總時長 100% 的次數。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed

Number

開始播放泡泡中音訊或影片的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed25Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 25% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed50Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 50% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed75Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 75% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

messages\[].uniqueMediaPlayed100Percent

Number

開始播放泡泡中音訊或影片並播放至總時長 100% 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

clicks

Array

關於訊息中被開啟的 URL 的資訊陣列。如果訊息不含任何 URL，或無法取得統計資料，則回傳空陣列。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].seq

Number

URL 的序號。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].url

String

URL。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].click

Number

泡泡中的 URL 被開啟的次數。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].uniqueClick

Number

開啟泡泡中 URL 的使用者數量。

<!-- parameter end -->
<!-- parameter start -->

clicks\[].uniqueClickOfRequest

Number

透過訊息中任一連結開啟此 `url` 的使用者數量。如果另一個訊息泡泡含有相同的 URL，且使用者開啟了這兩個連結，則只計算一次。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// If there is no statistic for aggregation period
{
  "overview": {
    "uniqueImpression": null,
    "uniqueClick": null,
    "uniqueMediaPlayed": null,
    "uniqueMediaPlayed100Percent": null
  },
  "messages": [],
  "clicks": []
}

// If there is a statistic for aggregation period
{
  "overview": {
    "uniqueImpression": 40,
    "uniqueClick": 30,
    "uniqueMediaPlayed": 25,
    "uniqueMediaPlayed100Percent": null
  },
  "messages": [
    {
      "seq": 1,
      "impression": 42,
      "uniqueImpression": 40,
      "mediaPlayed": 30,
      "mediaPlayed25Percent": null,
      "mediaPlayed50Percent": null,
      "mediaPlayed75Percent": null,
      "mediaPlayed100Percent": null,
      "uniqueMediaPlayed": 25,
      "uniqueMediaPlayed25Percent": null,
      "uniqueMediaPlayed50Percent": null,
      "uniqueMediaPlayed75Percent": null,
      "uniqueMediaPlayed100Percent": null
    }
  ],
  "clicks": [
    {
      "seq": 1,
      "url": "https://developers.line.biz/",
      "click": 35,
      "uniqueClick": 25,
      "uniqueClickOfRequest": null
    },
    {
      "seq": 1,
      "url": "https://api.line-status.info/",
      "click": 29,
      "uniqueClick": null,
      "uniqueClickOfRequest": null
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼以及一個錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法取得統計資料。請考慮下列原因：<ul><li>未指定單位名稱。</li><li>未指定彙總期間的日期。</li><li>指定了無效的彙總期間日期。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 區段中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you couldn't get the statistic (400 Bad Request)
{
  "message": null,
  "key": null,
  "stacktrace": null,
  "code": null
}
```

<!-- tab end -->
### Get the number of unit name types assigned during this month 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/message/aggregation/info`

你可以取得本月期間指派給訊息的單位名稱（unit name）類型數量。如需更多關於傳送訊息時可指派的單位名稱數量限制資訊，請參閱 Messaging API 文件中的 [Maximum number of unit name types](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/#limit-to-the-number-of-units)。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/message/aggregation/info \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及一個包含此資訊的 JSON 物件。

<!-- parameter start -->

numOfCustomAggregationUnits

Number

本月期間指派給訊息的單位名稱類型數量。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "numOfCustomAggregationUnits": 22
}
```

<!-- tab end -->

#### Error Response 

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

### Get a list of unit names assigned during this month 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/message/aggregation/list`

你可以取得本月期間指派給訊息的單位名稱不重複清單。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/message/aggregation/list \
-H 'Authorization: Bearer {channel access token}' \
--data-urlencode 'limit=30' \
-G
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

limit

String

每次請求最多可取得的單位名稱數量。預設值為 `100`。\
最大值：`100`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

start

String

[回應](https://developers.line.biz/en/reference/messaging-api/#get-a-list-of-unit-names-assigned-during-this-month-response) 所回傳 JSON 物件中 `next` 屬性所含的延續權杖（continuation token）值。如果無法在單一請求中取得所有單位名稱，請包含此參數以取得剩餘的陣列。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及一個包含此資訊的 JSON 物件。

<!-- parameter start -->

customAggregationUnits

Array of strings

代表單位名稱的字串陣列。此陣列不重複地包含本月期間指派給訊息的單位名稱。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

用以取得下一組單位名稱陣列的延續權杖。僅在原始請求中 `customAggregationUnits` 屬性還有未回傳的剩餘單位名稱時才會回傳。

延續權杖會在 24 小時（86,400 秒）後過期。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "customAggregationUnits": ["promotion_a", "promotion_b"],
  "next": "jxEWCEEP..."
}
```

<!-- tab end -->

#### Error Response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。請考慮以下原因：<ul><li>指定了無效的延續權杖。</li><li>為 `limit` 屬性指定了無效的值。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid continuation token, such as expired (400 Bad Request)
{
  "message": "Invalid start param"
}
```

<!-- tab end -->

## Coupon 

你可以管理要從你的 LINE 官方帳號（LINE Official Account）傳送給使用者的優惠券。

### Create a coupon 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/coupon`

建立一張優惠券。

僅建立優惠券並不會自動將其傳送給使用者。你需要將已建立的優惠券作為訊息傳送出去。如需更多資訊，請參閱 Messaging API 文件中的 [Steps to send coupons using the Messaging API](https://developers.line.biz/en/docs/messaging-api/send-coupons-to-users/#send-coupons-using-messaging-api)。

你最多可以建立 5,000 張有效的優惠券。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/coupon \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'
{
  "title": "Friends-only coupon",
  "description": "- To redeem your coupon, present this screen at checkout.\n- Redeemable once only, even if previously redeemed only unintentionally by the customer.\n- The validity period of this coupon may change or it may be canceled without notice.",
  "reward": {
    "type": "discount",
    "priceInfo": {
      "type": "fixed",
      "fixedAmount": 100
    }
  },
  "acquisitionCondition": {
    "type": "normal"
  },
  "startTimestamp": 0,
  "endTimestamp": 1924959599,
  "imageUrl": "https://developers.line.biz/media/messaging-api/coupon/sample-coupon-image-100-yen-off.jpg",
  "timezone": "ASIA_TOKYO",
  "visibility": "UNLISTED",
  "maxUseCountPerTicket": 1
}'
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

使用 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 建立優惠券不受此限制。

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

title

String

優惠券標題。\
最大長度：60

<!-- parameter end -->
<!-- parameter start (props: optional) -->

description

String

優惠券使用指南。設定優惠券的使用說明與注意事項。可以用 `\n` 指定換行。\
最大長度：1,000

<!-- parameter end -->
<!-- parameter start (props: required) -->

acquisitionCondition

Object

包含優惠券領取條件的物件。

<!-- parameter end -->
<!-- parameter start (props: required) -->

acquisitionCondition.type

String

優惠券領取條件類型。\
指定下列其中一個值：

- `normal`：無條件。所有使用者都可領取。
- `lottery`：抽獎。只有抽中的使用者才能領取。

具有「好友推薦」（friend referral）領取條件的優惠券無法透過 Messaging API 建立。這類優惠券只能從 LINE Official Account Manager 建立。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

acquisitionCondition.lotteryProbability

Number

以 1 到 99 的整數指定優惠券中獎機率（%）。\
舉例來說，若指定 50，中獎機率即為 50%。
當 `acquisitionCondition.type` 為 `lottery` 時為必填。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

acquisitionCondition.maxAcquireCount

Number

抽獎中獎者人數的上限。指定 1 到 999999 的整數。\
若無上限，請指定 `-1`。\
當 `acquisitionCondition.type` 為 `lottery` 時為必填。

<!-- parameter end -->
<!-- parameter start (props: required) -->

maxUseCountPerTicket

Number

優惠券可使用的次數。\
指定下列其中一個值：

- `1`：僅一次
- `-1`：無限制

<!-- parameter end -->
<!-- parameter start (props: required) -->

startTimestamp

Number

優惠券有效期間的開始日期與時間。\
以 UNIX 時間（單位為秒）指定。

<!-- parameter end -->
<!-- parameter start (props: required) -->

endTimestamp

Number

優惠券有效期間的結束日期與時間。\
以 UNIX 時間（單位為秒）指定。\
你不能指定早於當前日期與時間或早於開始日期與時間的日期與時間。

<!-- parameter end -->
<!-- parameter start (props: required) -->

timezone

String

作為有效期間基準所使用的時區。\
指定下列其中一個值：

- `ETC_GMT_MINUS_12`: (UTC-12:00) Etc/GMT-12
- `ETC_GMT_MINUS_11`: (UTC-11:00) Etc/GMT-11
- `PACIFIC_HONOLULU`: (UTC-10:00) Pacific/Honolulu
- `AMERICA_ANCHORAGE`: (UTC-09:00) America/Anchorage
- `AMERICA_LOS_ANGELES`: (UTC-08:00) America/Los_Angeles, Santa_Isabel
- `AMERICA_PHOENIX`: (UTC-07:00) America/Phoenix, Denver
- `AMERICA_CHICAGO`: (UTC-06:00) America/Chicago, Guatemala
- `AMERICA_NEW_YORK`: (UTC-05:00) America/New_York, Indiana/Indianapolis
- `AMERICA_CARACAS`: (UTC-04:30) America/Caracas
- `AMERICA_SANTIAGO`: (UTC-04:00) America/Santiago, Cuiaba
- `AMERICA_ST_JOHNS`: (UTC-03:30) America/St_Johns
- `AMERICA_SAO_PAULO`: (UTC-03:00) America/Sao_Paulo, Argentina/Buenos_Aires
- `ETC_GMT_MINUS_2`: (UTC-02:00) Etc/GMT-2
- `ATLANTIC_CAPE_VERDE`: (UTC-01:00) Atlantic/Cape_Verde, Azores
- `EUROPE_LONDON`: (UTC+00:00) Europe/London, Etc/GMT
- `EUROPE_PARIS`: (UTC+01:00) Europe/Paris, Berlin
- `EUROPE_ISTANBUL`: (UTC+02:00) Europe/Istanbul, Kiev
- `EUROPE_MOSCOW`: (UTC+03:00) Europe/Moscow, Minsk
- `ASIA_TEHRAN`: (UTC+03:30) Asia/Tehran
- `ASIA_TBILISI`: (UTC+04:00) Asia/Tbilisi, Yerevan
- `ASIA_KABUL`: (UTC+04:30) Asia/Kabul
- `ASIA_TASHKENT`: (UTC+05:00) Asia/Tashkent, Karachi
- `ASIA_COLOMBO`: (UTC+05:30) Asia/Colombo, Kolkata
- `ASIA_KATHMANDU`: (UTC+05:45) Asia/Kathmandu
- `ASIA_ALMATY`: (UTC+06:00) Asia/Almaty, Dhaka
- `ASIA_RANGOON`: (UTC+06:30) Asia/Rangoon
- `ASIA_BANGKOK`: (UTC+07:00) Asia/Bangkok, Jakarta
- `ASIA_TAIPEI`: (UTC+08:00) Asia/Taipei, Singapore
- `ASIA_TOKYO`: (UTC+09:00) Asia/Tokyo, Seoul
- `AUSTRALIA_DARWIN`: (UTC+09:30) Australia/Darwin, Adelaide
- `AUSTRALIA_SYDNEY`: (UTC+10:00) Australia/Sydney, Brisbane
- `ASIA_VLADIVOSTOK`: (UTC+11:00) Asia/Vladivostok, Pacific/Guadalcanal
- `ETC_GMT_PLUS_12`: (UTC+12:00) Etc/GMT+12
- `PACIFIC_TONGATAPU`: (UTC+13:00) Pacific/Tongatapu, Apia

<!-- parameter end -->
<!-- parameter start (props: required) -->

reward

Object

包含優惠券類型資訊的 [Reward 物件](https://developers.line.biz/en/reference/messaging-api/#create-coupon-reward-object)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

visibility

String

在 LY Corporation 服務中顯示優惠券。\
為下列其中一個值：

- `PUBLIC`：顯示。
- `UNLISTED`：不顯示。

如需更多資訊，請參閱 LINE for Business 中的 [Display coupon in LY Corporation services](https://www.lycbiz.com/jp/manual/OfficialAccountManager/coupons-service/)（僅提供日文版）。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageUrl

String

優惠券圖片的 URL。\
最大字元限制：2000\
通訊協定：HTTPS（TLS 1.2 或更新版本）\
圖片格式：JPEG 或 PNG\
最大檔案大小：10MB（建議 1MB 以下）

URL 應使用 UTF-8 進行百分比編碼（percent-encode）。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- note start -->

**之後變更該 URL 上的圖片不會更新優惠券圖片**

該 URL 上的圖片會在建立優惠券時被擷取並儲存在 LINE Platform 上。之後變更該 URL 上的圖片不會更新優惠券圖片。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

couponCode

String

開啟優惠券後所顯示的優惠券代碼。\
最大長度：16

<!-- parameter end -->
<!-- parameter start (props: optional) -->

barcodeImageUrl

String

開啟優惠券後所顯示的條碼圖片 URL。\
最大字元限制：2000\
通訊協定：HTTPS（TLS 1.2 或更新版本）\
圖片格式：JPEG 或 PNG\
最大檔案大小：10MB

URL 應使用 UTF-8 進行百分比編碼（percent-encode）。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- note start -->

**之後變更該 URL 上的圖片不會更新優惠券圖片**

該 URL 上的圖片會在建立優惠券時被擷取並儲存在 LINE Platform 上。之後變更該 URL 上的圖片不會更新優惠券圖片。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

usageCondition

String

優惠券使用條件。\
最大長度：100

<!-- parameter end -->

##### Reward object 

<!-- parameter start (props: required) -->

type

String

優惠券類型。\
指定下列其中一個值：

- `discount`：折扣
- `free`：免費
- `gift`：贈品
- `cashBack`：現金回饋
- `others`：其他

<!-- parameter end -->
<!-- parameter start (props: optional) -->

priceInfo

Object

包含折扣或現金回饋詳細資訊的物件。\
當 `type` 為 `discount` 與 `cashBack` 時為必填。

<!-- parameter end -->
<!-- parameter start (props: required) -->

priceInfo.type

String

優惠券折扣詳細資訊的類型。

當 `type` 為 `discount` 時，你可以指定下列其中一個值：

- `fixed`：顯示折扣金額
- `percentage`：顯示折扣百分比
- `explicit`：劃掉原價並顯示折扣後價格

當 `type` 為 `cashBack` 時，你可以指定下列其中一個值：

- `fixed`：顯示現金回饋金額
- `percentage`：顯示現金回饋百分比

<!-- parameter end -->
<!-- parameter start (props: optional) -->

priceInfo.fixedAmount

Number

以正整數指定折扣金額。\
當 `priceInfo.type` 為 `fixed` 時為必填。\
幣別單位會依 LINE 官方帳號（LINE Official Account）所屬的國家或地區自動設定。

- 台灣：TWD（新台幣）
- 泰國：THB（泰銖）
- 所有其他國家與地區：JPY（日圓）

<!-- parameter end -->
<!-- parameter start (props: optional) -->

priceInfo.percentage

Number

以 1 到 99 的整數指定折扣率（%）。\
舉例來說，若指定 50，折扣率即為 50%。\
當 `priceInfo.type` 為 `percentage` 時為必填。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

priceInfo.originalPrice

Number

以正整數指定折扣前的價格。\
當 `priceInfo.type` 為 `explicit` 時為必填。\
幣別單位會依 LINE 官方帳號（LINE Official Account）所屬的國家或地區自動設定。

- 台灣：TWD（新台幣）
- 泰國：THB（泰銖）
- 所有其他國家與地區：JPY（日圓）

<!-- parameter end -->
<!-- parameter start (props: optional) -->

priceInfo.priceAfterDiscount

Number

以正整數指定折扣後的價格。\
當 `priceInfo.type` 為 `explicit` 時為必填。\
幣別單位會依 LINE 官方帳號（LINE Official Account）所屬的國家或地區自動設定。

- 台灣：TWD（新台幣）
- 泰國：THB（泰銖）
- 所有其他國家與地區：JPY（日圓）

<!-- parameter end -->

_Reward object examples_

<!-- tab start `json` -->

```json
// 1,500 yen discount
{
  "type": "discount",
  "priceInfo": {
    "type": "fixed",
    "fixedAmount": 1500
  }
}

// 25% discount
{
  "type": "discount",
  "priceInfo": {
    "type": "percentage",
    "percentage": 25
  }
}

// Cross out the original price of 12,000 yen and display the discounted price of 9,500 yen
{
  "type": "discount",
  "priceInfo": {
    "type": "explicit",
    "originalPrice": 12000,
    "priceAfterDiscount": 9500
  }
}

// Free
{
  "type": "free"
}

// Gift
{
  "type": "gift"
}

// 100 yen cashback
{
  "type": "cashBack",
  "priceInfo": {
    "type": "fixed",
    "fixedAmount": 100
  }
}

// 30% cashback
{
  "type": "cashBack",
  "priceInfo": {
    "type": "percentage",
    "percentage": 30
  }
}

// Others
{
  "type": "others"
}
```

<!-- tab end -->

#### Response 

回傳狀態碼 `200` 以及一個包含下列屬性的 JSON 物件。

<!-- parameter start -->

couponId

String

優惠券 ID。在傳送優惠券訊息等情況時使用。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "couponId": "01JYNW8JMQVFBNWF1APF8Z3FS7"
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法建立優惠券。請考慮以下原因：<ul><li>指定了無效的優惠券類型。</li><li>已達到有效優惠券的數量上限（最多 5,000 張）。</li><li>在 reward 物件中指定了與 `priceInfo.type` 不相符的屬性。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// When the coupon title exceeds 60 characters
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Size must be between 1 and 60",
      "property": "title"
    }
  ]
}

// When an invalid coupon type is specified
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Must be one of the following values: [discount,free,gift,cashBack,others]",
      "property": "reward.type"
    }
  ]
}

// When the number of valid coupons exceeds the limit
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "You have too many coupons created.",
      "property": ""
    }
  ]
}

// When priceInfo.type is percentage in the reward object, but fixedAmount is specified
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Must not be specified",
      "property": "reward.priceInfo.fixedAmount"
    }
  ]
}
```

<!-- tab end -->

### Discontinue a coupon 

端點（Endpoint）：`PUT` `https://api.line.me/v2/bot/coupon/{couponId}/close`

停用指定的優惠券。

一旦優惠券被停用，已經以訊息形式收到該券的使用者將無法再領取，而已經領取該券的使用者也將無法再使用。

已停用的優惠券無法重新啟用。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X PUT https://api.line.me/v2/bot/coupon/01JYNW8JMQVFBNWF1APF8Z3FS7/close \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json'
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

使用 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 停用優惠券不受此限制。

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

couponId

String

要停用的優惠券 ID。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及一個空的 JSON 物件。

_Response example_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                                                 |
| ----- | ----------------------------------------------------------- |
| `410` | 指定了已停用優惠券的優惠券 ID。 |
| `404` | 指定的優惠券不存在。                         |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If the specified coupon is already discontinued (410 Gone)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "The coupon has already been closed.",
      "property": ""
    }
  ]
}

// If you specify a non-existent coupon ID (404 Not Found)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "coupon not found",
      "property": ""
    }
  ]
}
```

<!-- tab end -->

### Get a list of coupons 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/coupon`

取得優惠券清單，包含優惠券 ID 與優惠券標題。你也可以只取得有效的優惠券或只取得已停用的優惠券。

此優惠券清單同時包含透過 Messaging API 及 [LINE Official Account Manager](https://manager.line.biz/) 所建立的優惠券。你可以在 LINE Official Account Manager 中檢視相同的清單。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/coupon \
-H 'Authorization: Bearer {channel access token}'
-d 'limit=100' \
-d 'status=DRAFT,RUNNING' \
-G
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

使用 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 查看優惠券清單不受此限制。

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

limit

Number

單一請求中可取得的最大優惠券數量。預設值為 `20`。\
最大值：`100`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

start

String

[回應](https://developers.line.biz/en/reference/messaging-api/#get-coupons-list-response) 所回傳 JSON 物件中 `next` 屬性所含的延續權杖（continuation token）值。如果無法在單一請求中取得所有優惠券，請包含此參數以取得剩餘的優惠券。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

status

要回傳的優惠券狀態。若省略，則會包含所有狀態的優惠券。

- `DRAFT`：草稿儲存的優惠券。
- `RUNNING`：即將開始或有效的優惠券。
- `CLOSED`：已過期或已停用的優惠券。

如果你指定多個參數，會使用 OR 條件。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個包含下列屬性的 JSON 物件。

<!-- parameter start -->

items

Array of objects

代表優惠券的物件陣列。\
最多：`limit` 所指定的數量

<!-- parameter end -->
<!-- parameter start -->

items\[].couponId

String

優惠券 ID。

<!-- parameter end -->
<!-- parameter start -->

items\[].title

String

優惠券標題。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

用以取得下一組優惠券的延續權杖。僅在回應的 `items` 屬性中還有無法取得的優惠券時才會回傳此屬性。

延續權杖的有效期限為 24 小時（86,400 秒）。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
// When all coupons are retrieved
{
  "items": [
    {
      "couponId": "01JZMWQ9HMDW9ENJP4C167CXP8",
      "title": "Year-end and New Year coupon"
    },
    {
      "couponId": "01JZA9NPPFDJ3RFG8NA9DJ0NQT",
      "title": "Friends-only coupon"
    }
  ]
}

// When there are still coupons that couldn't be retrieved
{
  "next": "MTAwMDU3MjAxOjE3NTI1Njk5NDU2MjE6WXBPRHo1N3VjL3hPMkcxVEZPVGY1eW9YS3BqL2R2TGVEdit2V3J0ckczVT0=",
  "items": [
    {
      "couponId": "01JZMWQ9HMDW9ENJP4C167CXP8",
      "title": "Year-end and New Year coupon"
    },
    {
      "couponId": "01JZA9NPPFDJ3RFG8NA9DJ0NQT",
      "title": "Friends-only coupon"
    }
  ]
}

// When no matching coupons are found
{
  "items": []
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法取得優惠券清單。可能的原因包括：<ul><li>指定了無效的狀態。</li><li>要取得的優惠券最大數量超過 100。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// When an invalid status is specified (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Must be one of the following values: [DRAFT,RUNNING,CLOSED]",
      "property": "status"
    }
  ]
}

// When the maximum number of coupons to retrieve exceeds 100
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Must be less than or equal to 100",
      "property": "limit"
    }
  ]
}
```

<!-- tab end -->

### Get details of a coupon 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/coupon/{couponId}`

擷取指定優惠券的詳細資訊。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/coupon/01JYNW8JMQVFBNWF1APF8Z3FS7 \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

使用 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 查看優惠券詳細資訊不受此限制。

如需更多關於速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

couponId

String

要擷取詳細資訊的優惠券 ID。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個包含下列屬性的 JSON 物件。

<!-- parameter start -->

couponId

String

優惠券的優惠券 ID。

<!-- parameter end -->
<!-- parameter start -->

title

String

優惠券標題。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

description

String

優惠券使用指南。

<!-- parameter end -->
<!-- parameter start -->

acquisitionCondition

Object

包含優惠券領取條件的物件。

<!-- parameter end -->
<!-- parameter start -->

acquisitionCondition.type

String

優惠券領取條件類型。\
為下列其中一個值：

- `normal`：無條件。所有使用者都可領取。
- `lottery`：抽獎。只有抽中的使用者才能領取。
- `referral`：好友推薦。推薦該優惠券的使用者與接受推薦的使用者皆可領取。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

acquisitionCondition.lotteryProbability

Number

優惠券中獎機率（%），為 1 到 99 的整數。\
當 `acquisitionCondition.type` 為 `lottery` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

acquisitionCondition.maxAcquireCount

Number

中獎者人數上限，為 1 到 999999 的整數。\
若無上限，值為 `-1`。\
當 `acquisitionCondition.type` 為 `lottery` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start -->

maxUseCountPerTicket

Number

優惠券可使用的次數。\
為下列其中一個值：

- `1`：僅一次
- `-1`：無限制

<!-- parameter end -->
<!-- parameter start -->

maxTicketPerUser

Number

每位使用者可領取的優惠券數量。\
若 `acquisitionCondition.type` 為 `referral`，則此數量為 1 到 30 的整數。否則值為 `1`。

<!-- parameter end -->
<!-- parameter start -->

startTimestamp

Number

優惠券有效期間的開始日期與時間，以 UNIX 時間（單位為秒）表示。

<!-- parameter end -->
<!-- parameter start -->

endTimestamp

Number

優惠券有效期間的結束日期與時間，以 UNIX 時間（單位為秒）表示。

<!-- parameter end -->
<!-- parameter start -->

timezone

String

作為有效期間基準所使用的時區。\
為下列其中一個值：

- `ETC_GMT_MINUS_12`: (UTC-12:00) Etc/GMT-12
- `ETC_GMT_MINUS_11`: (UTC-11:00) Etc/GMT-11
- `PACIFIC_HONOLULU`: (UTC-10:00) Pacific/Honolulu
- `AMERICA_ANCHORAGE`: (UTC-09:00) America/Anchorage
- `AMERICA_LOS_ANGELES`: (UTC-08:00) America/Los_Angeles, Santa_Isabel
- `AMERICA_PHOENIX`: (UTC-07:00) America/Phoenix, Denver
- `AMERICA_CHICAGO`: (UTC-06:00) America/Chicago, Guatemala
- `AMERICA_NEW_YORK`: (UTC-05:00) America/New_York, Indiana/Indianapolis
- `AMERICA_CARACAS`: (UTC-04:30) America/Caracas
- `AMERICA_SANTIAGO`: (UTC-04:00) America/Santiago, Cuiaba
- `AMERICA_ST_JOHNS`: (UTC-03:30) America/St_Johns
- `AMERICA_SAO_PAULO`: (UTC-03:00) America/Sao_Paulo, Argentina/Buenos_Aires
- `ETC_GMT_MINUS_2`: (UTC-02:00) Etc/GMT-2
- `ATLANTIC_CAPE_VERDE`: (UTC-01:00) Atlantic/Cape_Verde, Azores
- `EUROPE_LONDON`: (UTC+00:00) Europe/London, Etc/GMT
- `EUROPE_PARIS`: (UTC+01:00) Europe/Paris, Berlin
- `EUROPE_ISTANBUL`: (UTC+02:00) Europe/Istanbul, Kiev
- `EUROPE_MOSCOW`: (UTC+03:00) Europe/Moscow, Minsk
- `ASIA_TEHRAN`: (UTC+03:30) Asia/Tehran
- `ASIA_TBILISI`: (UTC+04:00) Asia/Tbilisi, Yerevan
- `ASIA_KABUL`: (UTC+04:30) Asia/Kabul
- `ASIA_TASHKENT`: (UTC+05:00) Asia/Tashkent, Karachi
- `ASIA_COLOMBO`: (UTC+05:30) Asia/Colombo, Kolkata
- `ASIA_KATHMANDU`: (UTC+05:45) Asia/Kathmandu
- `ASIA_ALMATY`: (UTC+06:00) Asia/Almaty, Dhaka
- `ASIA_RANGOON`: (UTC+06:30) Asia/Rangoon
- `ASIA_BANGKOK`: (UTC+07:00) Asia/Bangkok, Jakarta
- `ASIA_TAIPEI`: (UTC+08:00) Asia/Taipei, Singapore
- `ASIA_TOKYO`: (UTC+09:00) Asia/Tokyo, Seoul
- `AUSTRALIA_DARWIN`: (UTC+09:30) Australia/Darwin, Adelaide
- `AUSTRALIA_SYDNEY`: (UTC+10:00) Australia/Sydney, Brisbane
- `ASIA_VLADIVOSTOK`: (UTC+11:00) Asia/Vladivostok, Pacific/Guadalcanal
- `ETC_GMT_PLUS_12`: (UTC+12:00) Etc/GMT+12
- `PACIFIC_TONGATAPU`: (UTC+13:00) Pacific/Tongatapu, Apia

<!-- parameter end -->
<!-- parameter start -->

reward

Object

包含優惠券類型資訊的 [Reward 物件](https://developers.line.biz/en/reference/messaging-api/#get-coupon-reward-object)。

<!-- parameter end -->
<!-- parameter start -->

visibility

String

在 LY Corporation 服務中顯示優惠券。\
為下列其中一個值：

- `PUBLIC`：顯示。
- `UNLISTED`：不顯示。

如需更多資訊，請參閱 LINE for Business 中的 [Display coupon in LY Corporation services](https://www.lycbiz.com/jp/manual/OfficialAccountManager/coupons-service/)（僅提供日文版）。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

imageUrl

String

優惠券圖片的 URL。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

couponCode

String

開啟優惠券後所顯示的優惠券代碼。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

barcodeImageUrl

String

開啟優惠券後所顯示的條碼圖片 URL。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

usageCondition

String

優惠券使用條件。

<!-- parameter end -->
<!-- parameter start -->

status

優惠券的狀態。

- `DRAFT`：草稿儲存的優惠券。
- `RUNNING`：即將開始或有效的優惠券。
- `CLOSED`：已過期或已停用的優惠券。

<!-- parameter end -->
<!-- parameter start -->

createdTimestamp

Number

優惠券的建立日期與時間，以 UNIX 時間（單位為秒）表示。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "couponId": "01K0B456W5Y6SBD3YH74YM6QE6",
  "title": "Friends-only coupon",
  "description": "- To redeem your coupon, present this screen at checkout.\n- Redeemable once only, even if previously redeemed only unintentionally by the customer.\n- The validity period of this coupon may change or it may be canceled without notice.",
  "acquisitionCondition": {
    "type": "lottery",
    "lotteryProbability": 50,
    "maxAcquireCount": -1
  },
  "startTimestamp": 1752678000,
  "endTimestamp": 1924959540,
  "timezone": "ASIA_TOKYO",
  "couponCode": "COUPONCODE123456",
  "maxUseCountPerTicket": 1,
  "maxTicketPerUser": 1,
  "visibility": "UNLISTED",
  "reward": {
    "type": "discount",
    "priceInfo": {
      "type": "fixed",
      "fixedAmount": 100,
      "currency": "JPY"
    }
  },
  "imageUrl": "https://oa-coupon.line-scdn-dev.net/0h9gbUqRVkZkhfLHhXMLYZHwdyaCosWGBAPFR7cD5tZidsTnofYDVfezt-ZAR3YER9OzRfK35XZwR6TH5uYDF2TnJ-cBNyfURpPRl2RSFSXQc0TiJhYCFiXiZ8XXk0",
  "usageCondition": "Usable for payments of 1,000 yen or more",
  "status": "RUNNING",
  "createdTimestamp": 1752720120
}
```

<!-- tab end -->

##### Reward object 

<!-- parameter start -->

type

String

優惠券類型。\
為下列其中一個值：

- `discount`：折扣
- `free`：免費
- `gift`：贈品
- `cashBack`：現金回饋
- `others`：其他

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

priceInfo

Object

包含折扣或現金回饋詳細資訊的物件。\
當 `type` 為 `discount` 與 `cashBack` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start -->

priceInfo.type

String

優惠券折扣詳細資訊的類型。

當 `type` 為 `discount` 時，為下列其中一個值：

- `fixed`：顯示折扣金額
- `percentage`：顯示折扣百分比
- `explicit`：劃掉原價並顯示折扣後價格

當 `type` 為 `cashBack` 時，為下列其中一個值：

- `fixed`：顯示現金回饋金額
- `percentage`：顯示現金回饋百分比

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

priceInfo.fixedAmount

Number

折扣金額。\
當 `priceInfo.type` 為 `fixed` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

priceInfo.percentage

Number

折扣率（%）。\
當 `priceInfo.type` 為 `percentage` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

priceInfo.originalPrice

Number

折扣前的價格。\
當 `priceInfo.type` 為 `explicit` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

priceInfo.priceAfterDiscount

Number

折扣後的價格。\
當 `priceInfo.type` 為 `explicit` 時包含此屬性。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

priceInfo.currency

Number

幣別單位。會依 LINE 官方帳號（LINE Official Account）所屬的國家或地區自動設定。\
當 `priceInfo.type` 為 `fixed` 或 `explicit` 時包含此屬性。

- `TWD`：新台幣（台灣）
- `THB`：泰銖（泰國）
- `JPY`：日圓（所有其他國家與地區）

<!-- parameter end -->

_Reward object examples_

<!-- tab start `json` -->

```json
// 1,500 yen discount
{
  "type": "discount",
  "priceInfo": {
    "type": "fixed",
    "fixedAmount": 1500,
    "currency": "JPY"
  }
}

// 25% discount
{
  "type": "discount",
  "priceInfo": {
    "type": "percentage",
    "percentage": 25
  }
}

// Cross out the original price of 12,000 yen and display the discounted price of 9,500 yen
{
  "type": "discount",
  "priceInfo": {
    "type": "explicit",
    "originalPrice": 12000,
    "priceAfterDiscount": 9500,
    "currency": "JPY"
  }
}

// Free
{
  "type": "free"
}

// Gift
{
  "type": "gift"
}

// 100 yen cashback
{
  "type": "cashBack",
  "priceInfo": {
    "type": "fixed",
    "fixedAmount": 100,
    "currency": "JPY"
  }
}

// 30% cashback
{
  "type": "cashBack",
  "priceInfo": {
    "type": "percentage",
    "percentage": 30
  }
}

// Others
{
  "type": "others"
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `404` | 指定的優惠券不存在。請考慮以下原因：<ul><li>指定了在其他頻道（channel）中建立的優惠券。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a non-existent coupon ID (404 Not Found)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "coupon not found",
      "property": ""
    }
  ]
}
```

<!-- tab end -->
## Users 

你可以取得已將你的 LINE 官方帳號加為好友的使用者資訊。

<!-- note start -->

**存取你自己的使用者 ID**

你可以在 [LINE Developers Console](https://developers.line.biz/console/) 上你的頻道（channel）的 **Basic settings** 分頁中存取你的使用者 ID。如需 LINE Developers Console 中各角色權限的詳細資訊，請參閱 [Managing roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/) 中的 [Channel roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel)。並沒有可用於取得你自己使用者 ID 的 API。

<!-- note end -->

### Get profile 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/profile/{userId}`

你可以取得符合下列兩項條件之一的使用者的個人檔案（profile）資訊：

- 已將你的 LINE 官方帳號加為好友的使用者
- 尚未將你的 LINE 官方帳號加為好友，但曾傳送訊息給你的 LINE 官方帳號的使用者（封鎖你的 LINE 官方帳號的使用者除外）

你只能取得主要個人檔案資訊。你無法取得使用者的[子個人檔案（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

<!-- note start -->

**Note**

你無法取得已封鎖你的 LINE 官方帳號的使用者的個人檔案資訊。

<!-- note end -->

<!-- tip start -->

**群組聊天成員與多人聊天成員的個人檔案資訊**

使用這些端點來取得群組聊天成員或多人聊天成員的個人檔案資訊。

- [Get group chat member profile](https://developers.line.biz/en/reference/messaging-api/#get-group-member-profile)
- [Get multi-person chat member profile](https://developers.line.biz/en/reference/messaging-api/#get-room-member-profile)

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/profile/{userId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

userId

在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)中回傳的使用者 ID。請勿使用 LINE 上找到的 LINE ID。

<!-- parameter end -->

#### Response 

當指定的使用者 ID 有效時，會回傳狀態碼 `200` 及包含下列資訊的 JSON 物件（object）。

<!-- parameter start -->

displayName

String

使用者的顯示名稱

<!-- parameter end -->
<!-- parameter start -->

userId

String

使用者 ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

language

String

使用者的語言，以 [BCP 47](https://www.rfc-editor.org/info/bcp47) 語言標籤表示。若使用者尚未同意 LY Corporation 隱私權政策，則不會包含在回應（response）中。\
例如英文為 `en`。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pictureUrl

String

個人檔案圖片 URL。「https」圖片 URL。若使用者沒有個人檔案圖片，則不會包含在回應中。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

statusMessage

String

使用者的狀態消息。若使用者沒有設定狀態消息，則不會包含在回應中。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "displayName": "LINE taro",
  "userId": "U4af4980629...",
  "language": "en",
  "pictureUrl": "https://profile.line-scdn.net/ch/v2/p/uf9da5ee2b...",
  "statusMessage": "Hello, LINE!"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的使用者 ID。 |
| `404` | 無法取得個人檔案資訊。可能的原因如下：<ul><li>目標使用者 ID 不存在。</li><li>使用者尚未同意提供其個人檔案資訊。</li><li>使用者尚未將目標 LINE 官方帳號加為好友。</li><li>使用者將目標 LINE 官方帳號加為好友後又予以封鎖。</li></ul>如需詳細資訊，請參閱 Messaging API 文件中的 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you couldn't get profile information (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get a list of users who added your LINE Official Account as a friend 

端點：`GET` `https://api.line.me/v2/bot/followers/ids`

<!-- note start -->

**Note**

此功能僅適用於認證帳號或[尊榮帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)。如需帳號類型的詳細資訊，請參閱 LINE for Business 上的 [Account Types of LINE Official Account](https://www.linebiz.com/jp-en/service/line-official-account/account-type/) 頁面。

<!-- note end -->

取得已將你的 LINE 官方帳號加為好友的使用者的 [User ID](https://developers.line.biz/en/glossary/#user-id) 清單。

若要取得所有使用者 ID，你需要重複發送請求，直到[回應](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids-response)中不再包含 `next` 屬性（property）為止。重複發送請求時，將回應中所包含的 `next` 屬性指定為下一次請求的 `start`。

#### Restrictions on user IDs that can be obtained 

下列使用者的 ID 不會包含在所取得的使用者 ID 清單中：

- 已刪除其 LINE 帳號的使用者。
- 將你的 LINE 官方帳號加為好友後又予以封鎖的使用者。
- 尚未同意提供其個人檔案資訊的使用者。如需詳細資訊，請參閱 Messaging API 文件中的 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。

因此，使用此端點取得的實際使用者 ID 數量，可能與你的 LINE 官方帳號商業檔案或 [LINE Official Account Manager](https://manager.line.biz/) 上顯示的好友數量不一致。

<!-- note start -->

**你可能無法使用所取得的使用者 ID**

即使你向以此端點取得的使用者 ID 傳送訊息，傳送也可能因使用者的行為而失敗。失敗的主要原因如下：

- 在取得使用者 ID 與你嘗試傳送訊息之間，使用者封鎖了目標 LINE 官方帳號。
- 使用者在將目標 LINE 官方帳號加為好友後[刪除了 LINE 帳號](https://guide.line.me/ja/account-and-settings/account-and-profile/line-account-delete.html)。

<!-- note end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/followers/ids \
-H 'Authorization: Bearer {channel access token}' \
-d 'limit=1000' \
-d 'start=yANU9IA...' \
-G
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

limit

Number

單一請求中可取得的使用者 ID 的最大數量。預設值為 `300`。\
最大值：`1000`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

start

String

[回應](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids-response)中所回傳的 JSON 物件的 `next` 屬性中找到的延續權杖（continuation token）的值。包含此參數即可取得下一個使用者 ID 陣列（array）。若你無法在單一請求中取得所有使用者 ID，請指定此參數以取得其餘的使用者 ID。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含下列屬性的 JSON 物件。

<!-- parameter start -->

userIds

Array of strings

由字串組成的陣列，表示已將 LINE 官方帳號加為好友的使用者的使用者 ID。由於[可取得的使用者 ID 限制](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids-obtainable-ids)，即使回傳了 `next` 屬性，`userIds` 屬性中的使用者 ID 數量也可能未達到 `limit` 所指定的最大數量。\
最大值：`limit` 所指定的數量

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

用於取得下一批使用者 ID 的延續權杖。僅在前一個請求的 `userIds` 屬性中尚有未回傳的剩餘使用者 ID 時才會回傳。

此延續權杖會在 24 小時（86,400 秒）後失效。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "userIds": ["U4af4980629...", "U0c229f96c4...", "U95afb1d4df..."],
  "next": "yANU9IA..."
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的延續權杖。 |
| `403` | 無權使用此端點。僅適用於認證帳號或[尊榮帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify an invalid continuation token, such as expired (400 Bad Request)
{
  "message": "Invalid start param"
}
```

<!-- tab end -->

## Membership 

你可以取得你的 LINE 官方帳號會員資格（membership）的相關資訊。如需詳細資訊，請參閱 Messaging API 文件中的 [Use membership features](https://developers.line.biz/en/docs/messaging-api/use-membership-features/)。

### Get a user's membership subscription status 

端點：`GET` `https://api.line.me/v2/bot/membership/subscription/{userId}`

你可以取得使用者所訂閱的會員資格的相關資訊。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/membership/subscription/{userId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

userId

你想查看其會員資格訂閱狀態的使用者的使用者 ID。

如需如何取得使用者 ID 的詳細資訊，請參閱 Messaging API 文件中的 [Get user IDs](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/)。

<!-- parameter end -->

#### Response 

若使用者已訂閱會員資格，則會回傳狀態碼 `200` 及包含下列資訊的 JSON 物件。

<!-- parameter start -->

subscriptions

Array

由會員資格組成的陣列。

<!-- parameter end -->
<!-- parameter start -->

membership

Object

包含會員方案資訊的物件。

<!-- parameter end -->
<!-- parameter start -->

membership.membershipId

Number

會員方案 ID。

<!-- parameter end -->
<!-- parameter start -->

membership.title

String

會員方案名稱。

<!-- parameter end -->
<!-- parameter start -->

membership.description

String

會員方案說明。

<!-- parameter end -->
<!-- parameter start -->

membership.benefits

Array of strings

會員方案福利清單。\
福利的最大數量：5

<!-- parameter end -->
<!-- parameter start -->

membership.price

Number

會員方案的每月費用。（例如 `1500.00`）

<!-- parameter end -->
<!-- parameter start -->

membership.currency

String

`membership.price` 的幣別。為下列其中之一：

- `JPY`：日圓
- `TWD`：新台幣
- `THB`：泰銖

<!-- parameter end -->
<!-- parameter start -->

user

Object

包含使用者會員資格訂閱資訊的物件。

<!-- parameter end -->
<!-- parameter start -->

user.membershipNo

Number

使用者在會員方案中的會員編號。

<!-- parameter end -->
<!-- parameter start -->

user.joinedTime

Number

使用者訂閱會員資格的 UNIX 時間（以秒為單位）。

<!-- parameter end -->
<!-- parameter start -->

user.nextBillingDate

String

會員方案的下次付款日期。

- 格式：`yyyy-MM-dd`（例如 `2024-02-08`）
- 時區：UTC+9

<!-- parameter end -->
<!-- parameter start -->

user.totalSubscriptionMonths

Number

使用者訂閱會員方案的期間（以月為單位）。若使用者先前取消後又重新訂閱同一個會員方案，則僅計算重新訂閱之後的期間。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "subscriptions": [
    {
      "membership": {
        "membershipId": 3189,
        "title": "Basic Plan",
        "description": "You will receive messages and photos every Saturday.",
        "benefits": ["Members Only Messages", "Members Only Photos"],
        "price": 500.00,
        "currency": "JPY"
      },
      "user": {
        "membershipNo": 1,
        "joinedTime": 1707214784,
        "nextBillingDate": "2024-02-08",
        "totalSubscriptionMonths": 1
      }
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的使用者 ID。 |
| `404` | 無法取得使用者所訂閱會員資格的相關資訊。可能的原因如下：<ul><li>使用者並未訂閱會員資格</li><li>目標使用者 ID 不存在</li></ul> |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The value for the 'userId' parameter is invalid"
}

// If user doesn't subscribe to membership (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get a list of users who have joined the membership 

端點：`GET` `https://api.line.me/v2/bot/membership/{membershipId}/users/ids`

你可以取得已加入你的 LINE 官方帳號會員資格的使用者的使用者 ID 清單。

#### Restrictions on user IDs that can be obtained 

即使使用者已加入會員資格，若符合下列任一條件，該使用者的使用者 ID 也不會包含在清單中：

- 使用者已刪除其 LINE 帳號。
- 使用者已封鎖你的 LINE 官方帳號。
- 使用者尚未將你的 LINE 官方帳號加為好友。
- 使用者尚未同意允許存取其個人檔案資訊。如需詳細資訊，請參閱 Messaging API 文件中的 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/membership/{membershipId}/users/ids \
-H 'Authorization: Bearer {channel access token}' \
-d 'limit={limit}' \
-d 'start={start}' \
-G
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

membershipId

會員資格 ID。

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

limit

Number

單一請求中可取得的使用者 ID 的最大數量。預設值為 `300`。\
最大值：`1000`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

start

延續權杖的值。此值包含在[回應](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids-response)中所回傳的 JSON 物件的 `next` 屬性中。若你無法在單一請求中取得所有使用者 ID，可指定此參數以取得其餘的陣列。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含下列屬性的 JSON 物件。

<!-- parameter start -->

userIds

Array of strings

由已加入會員資格的使用者的使用者 ID 所組成的陣列。即使回傳了 `next` 屬性，`userIds` 屬性中所包含的使用者 ID 數量也不一定會與 `limit` 查詢參數所指定的數量相同，因為可取得的使用者 ID 取決於使用者的狀態。如需詳細資訊，請參閱 [Restrictions on user IDs that can be obtained](https://developers.line.biz/en/reference/messaging-api/#get-membership-user-ids-restrictions)。\
最大值：`limit` 查詢參數所指定的數量

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

延續權杖。用於取得下一批使用者 ID 清單。僅在前一個回應的 `userIds` 屬性中尚有無法取得的使用者 ID 時才會回傳此屬性。

此延續權杖會在 24 小時（86,400 秒）後失效。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "userIds": ["U4af4980629...", "U0c229f96c4...", "U95afb1d4df..."],
  "next": "yANU9IA..."
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的延續權杖。</li><li>`limit` 查詢參數指定了無效的值。</li></ul> |
| `404` | `membershipId` path parameter 指定了不存在的會員資格 ID。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a membership ID that doesn't exist in the membershipId path parameter (404 Not Found)
{
  "message": "Membership ID is not found"
}
```

<!-- tab end -->

### Get membership plans being offered 

端點：`GET` `https://api.line.me/v2/bot/membership/list`

你可以取得目前透過你的 LINE 官方帳號會員資格提供的會員方案。

審查中的方案或已終止的方案不會包含在回應中。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/membership/list \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 200 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含下列屬性的 JSON 物件。

<!-- parameter start -->

memberships

Array

由提供中的會員方案所組成的陣列。\
方案的最大數量：5

<!-- parameter end -->
<!-- parameter start -->

memberships\[].membershipId

Number

會員方案 ID。

<!-- parameter end -->
<!-- parameter start -->

memberships\[].title

String

會員方案名稱。

<!-- parameter end -->
<!-- parameter start -->

memberships\[].description

String

會員方案說明。

<!-- parameter end -->
<!-- parameter start -->

memberships\[].benefits

Array of strings

會員方案福利清單。\
福利的最大數量：5

<!-- parameter end -->
<!-- parameter start -->

memberships\[].price

Number

會員方案的每月費用。（例如 `1500.00`）

<!-- parameter end -->
<!-- parameter start -->

memberships\[].currency

String

`memberships[].price` 的幣別。為下列其中之一：

- `JPY`：日圓
- `TWD`：新台幣
- `THB`：泰銖

<!-- parameter end -->
<!-- parameter start -->

memberships\[].memberCount

Number

訂閱該會員方案的成員數量。

<!-- parameter end -->
<!-- parameter start -->

memberships\[].memberLimit

Number

可訂閱的成員人數上限。若未設定上限，則為 `null`。

<!-- parameter end -->
<!-- parameter start -->

memberships\[].isInAppPurchase

Boolean

訂閱會員方案的使用者的付款方式。

- `true`：應用程式內購買
- `false`：瀏覽器付款

<!-- parameter end -->
<!-- parameter start -->

memberships\[].isPublished

Boolean

會員方案狀態。

- `true`：公開
- `false`：非公開（該方案已停止提供且不再公開，但仍提供福利）

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "memberships": [
    {
      "membershipId": 3189,
      "title": "Basic Plan",
      "description": "You will receive messages and photos every Saturday.",
      "benefits": ["Members Only Messages", "Members Only Photos"],
      "price": 500.00,
      "currency": "JPY",
      "memberCount": 1,
      "memberLimit": null,
      "isInAppPurchase": true,
      "isPublished": true
    },
    {
      "membershipId": 3213,
      "title": "Premium Plan",
      "description": "Invitation to a special party.",
      "benefits": ["Members Only Party"],
      "price": 1500.00,
      "currency": "JPY",
      "memberCount": 0,
      "memberLimit": null,
      "isInAppPurchase": false,
      "isPublished": true
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code  | Description                  |
| ----- | ---------------------------- |
| `404` | 沒有提供任何會員方案。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// No membership plan offered (404 Not Found)
{
  "message": "Membership plan not found"
}
```

<!-- tab end -->

## LINE Official Account (bot) 

你可以取得 LINE 官方帳號（bot）的基本資訊。

### Get LINE Official Account (bot) info 

端點：`GET` `https://api.line.me/v2/bot/info`

取得 LINE 官方帳號（bot）的基本資訊。

_Example request_

<!-- tab start `shell` -->

```sh
curl -X GET \
-H 'Authorization: Bearer {channel access token}' \
https://api.line.me/v2/bot/info
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含下列資訊的 JSON 物件。

<!-- parameter start -->

userId

String

LINE 官方帳號（bot）的使用者 ID。

<!-- parameter end -->
<!-- parameter start -->

basicId

String

LINE 官方帳號（bot）的 Basic ID。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

premiumId

String

LINE 官方帳號（bot）的 [Premium ID](https://developers.line.biz/en/glossary/#premium-id)。若未設定 premium ID，則不會包含在回應中。

<!-- parameter end -->
<!-- parameter start -->

displayName

String

LINE 官方帳號（bot）的顯示名稱。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pictureUrl

String

個人檔案圖片 URL。「https」圖片 URL。若 LINE 官方帳號（bot）沒有個人檔案圖片，則不會包含在回應中。

<!-- parameter end -->
<!-- parameter start -->

chatMode

String

在 [LINE Official Account Manager](https://manager.line.biz) 中設定的聊天設定。為下列其中之一：

- `chat`：聊天設定為「開啟」。
- `bot`：聊天設定為「關閉」。

<!-- parameter end -->
<!-- parameter start -->

markAsReadMode

String

訊息的自動已讀設定。若聊天設定為「關閉」，則回傳 `auto`。若聊天設定為「開啟」，則回傳 `manual`。

- `auto`：啟用自動已讀設定。
- `manual`：停用自動已讀設定。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "userId": "Ub9952f8...",
  "basicId": "@216ru...",
  "displayName": "Example name",
  "pictureUrl": "https://profile.line-scdn.net/0hbGgpkVAb...",
  "chatMode": "chat",
  "markAsReadMode": "manual"
}
```

<!-- tab end -->

#### Error response 

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

## Group chats 

你可以取得 LINE 官方帳號所屬的群組聊天及其成員的相關資訊。

### Get group chat summary 

端點：`GET` `https://api.line.me/v2/bot/group/{groupId}/summary`

取得 LINE 官方帳號為其成員的群組聊天的群組 ID、群組名稱及群組圖示 URL。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/group/{groupId}/summary \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

groupId

群組 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 source 物件中找到。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含這些屬性的 JSON 物件。

<!-- parameter start -->

groupId

String

群組 ID

<!-- parameter end -->
<!-- parameter start -->

groupName

String

群組名稱

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pictureUrl

String

群組圖示 URL。若使用者未設定群組個人檔案圖示，則不會包含在回應中。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "groupId": "Ca56f94637c...",
  "groupName": "Group name",
  "pictureUrl": "https://profile.line-scdn.net/abcdefghijklmn"
}
```

<!-- tab end -->

#### Error Response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的群組 ID。 |
| `404` | 指定了不存在的群組，或你的 LINE 官方帳號未參與的群組。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid group ID (400 Bad Request)
{
  "message": "The value for the 'groupId' parameter is invalid"
}

// If you specify a non-existent group or a group that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get number of users in a group chat 

端點：`GET` `https://api.line.me/v2/bot/group/{groupId}/members/count`

取得群組聊天中的使用者數量。即使使用者尚未將 LINE 官方帳號加為好友，或已封鎖 LINE 官方帳號，你仍可取得群組中的使用者數量。

回傳的數量不包含 LINE 官方帳號。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/group/{groupId}/members/count \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

groupId

群組 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 source 物件中找到。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含這些屬性的 JSON 物件。

<!-- parameter start -->

count

Number

群組聊天中的成員數量。回傳的數量不包含 LINE 官方帳號。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "count": 3
}
```

<!-- tab end -->

#### Error Response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的群組 ID。 |
| `404` | 指定了不存在的群組，或你的 LINE 官方帳號未參與的群組。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid group ID (400 Bad Request)
{
  "message": "The value for the 'groupId' parameter is invalid"
}

// If you specify a non-existent group or a group that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get group chat member user IDs 

端點：`GET` `https://api.line.me/v2/bot/group/{groupId}/members/ids`

<!-- note start -->

**Note**

此功能僅適用於認證帳號或[尊榮帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)。如需帳號類型的詳細資訊，請參閱 LINE for Business 上的 [Account Types of LINE Official Account](https://www.linebiz.com/jp-en/service/line-official-account/account-type/) 頁面。

<!-- note end -->

取得 LINE 官方帳號所在的群組聊天的成員的使用者 ID。這包含尚未將 LINE 官方帳號加為好友或已封鎖 LINE 官方帳號的使用者的使用者 ID。

<!-- tip start -->

**你也可以從 webhook 取得使用者 ID**

當使用者加入群組聊天或在群組聊天中傳送訊息時，會有 webhook 被傳送到 bot 伺服器。該 webhook 包含使用者 ID，因此你無需發送 API 請求即可取得使用者 ID。如需詳細資訊，請參閱 Messaging API 文件中的 [Get a user ID from webhook](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-user-ids-in-webhook)。

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/group/{groupId}/members/ids?start={continuationToken}' \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

groupId

群組 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

start

[回應](https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids-response)中所回傳的 JSON 物件的 `next` 屬性中找到的延續權杖的值。包含此參數即可取得群組成員的下一個使用者 ID 陣列。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含下列屬性的 JSON 物件。

<!-- parameter start -->

memberIds

Array of strings

群組聊天中成員的使用者 ID 清單。`memberIds` 中僅包含 LINE for iOS 與 LINE for Android 的使用者。如需詳細資訊，請參閱 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。\
最大值：100 個使用者 ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

用於取得群組聊天中成員的下一個使用者 ID 陣列的延續權杖。僅在原始請求的 `memberIds` 中尚有未回傳的剩餘使用者 ID 時才會回傳。

此延續權杖會在 24 小時（86,400 秒）後失效。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "memberIds": ["U4af4980629...", "U0c229f96c4...", "U95afb1d4df..."],
  "next": "jxEWCEEP..."
}
```

<!-- tab end -->

#### Error Response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的群組 ID。</li><li>`start` 屬性指定了無效的延續權杖。</li></ul> |
| `403` | 無權使用此端點。僅適用於認證帳號或[尊榮帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)。 |
| `404` | 指定了不存在的群組，或你的 LINE 官方帳號未參與的群組。 |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid group ID (400 Bad Request)
{
  "message": "The value for the 'groupId' parameter is invalid"
}

// If you specify an invalid continuation token, such as expired (400 Bad Request)
{
  "message": "Invalid start param"
}

// If you specify a non-existent group or a group that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get group chat member profile 

端點：`GET` `https://api.line.me/v2/bot/group/{groupId}/member/{userId}`

若已知群組成員的使用者 ID，則可取得 LINE 官方帳號所在的群組聊天的成員的個人檔案資訊。

<!-- tip start -->

**Tip**

無論使用者是否已將你的 LINE 官方帳號加為好友，或是否已封鎖你的 LINE 官方帳號，你都可以取得同一個群組聊天中使用者的個人檔案資訊。

<!-- tip end -->

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/group/{groupId}/member/{userId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

groupId

群組 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。

<!-- parameter end -->
<!-- parameter start (props: required) -->

userId

使用者 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。請勿使用 LINE 中使用的 LINE ID。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及包含下列資訊的 JSON 物件。

<!-- parameter start -->

displayName

String

顯示名稱

<!-- parameter end -->
<!-- parameter start -->

userId

String

使用者 ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pictureUrl

String

個人檔案圖片 URL。若使用者沒有個人檔案圖片，則不會包含在回應中。

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "displayName": "LINE taro",
  "userId": "U4af4980629...",
  "pictureUrl": "https://sprofile.line-scdn.net/0hHkIRkHJF..."
}
```

<!-- tab end -->

#### Error Response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。可能的原因如下：<ul><li>指定了無效的群組 ID。</li><li>指定了無效的使用者 ID。</li></ul> |
| `404` | 無法取得個人檔案資訊。可能的原因如下：<ul><li>指定了不存在的群組，或你的 LINE 官方帳號未參與的群組。</li><li>指定了不存在的使用者，或未加入群組的使用者。</li></ul> |

如需詳細資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid group ID (400 Bad Request)
{
  "message": "The value for the 'groupId' parameter is invalid"
}

// If you specify a non-existent group or user, or a group that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->
### Leave group chat 

端點（endpoint）：`POST` `https://api.line.me/v2/bot/group/{groupId}/leave`

退出[群組聊天](https://developers.line.biz/en/docs/messaging-api/group-chats/#group)。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/group/{groupId}/leave \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

groupId

群組 ID。可在[webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件（object）中找到。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error Response 

回傳以下 HTTP 狀態碼與錯誤回應（response）：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的群組 ID。 |
| `404` | 指定了不存在的群組，或你的 LINE 官方帳號未參與的群組。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid group ID (400 Bad Request)
{
  "message": "The value for the 'groupId' parameter is invalid"
}

// If you specify a non-existent group or a group that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

## Multi-person chats 

你可以取得 LINE 官方帳號所屬的多人聊天及其成員的相關資訊。

### Get number of users in a multi-person chat 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/room/{roomId}/members/count`

取得多人聊天中的使用者人數。即使使用者未將 LINE 官方帳號加為好友，或已封鎖該 LINE 官方帳號，你仍可取得多人聊天中的使用者人數。

回傳的數字不包含 LINE 官方帳號本身。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/room/{roomId}/members/count \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

roomId

聊天室 ID。可在[webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 source 物件中找到。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個帶有下列屬性（property）的 JSON 物件。

<!-- parameter start -->

count

Number

多人聊天中的成員人數。回傳的數字不包含 LINE 官方帳號本身。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "count": 3
}
```

<!-- tab end -->

#### Error Response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的聊天室 ID。 |
| `404` | 指定了不存在的多人聊天，或你的 LINE 官方帳號未參與的多人聊天。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid room ID (400 Bad Request)
{
  "message": "The value for the 'roomId' parameter is invalid"
}

// If you specify a non-existent multi-person chat or a multi-person chat that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get multi-person chat member user IDs 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/room/{roomId}/members/ids`

<!-- note start -->

**Note**

此功能僅供已驗證帳號或[進階帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)使用。如需更多有關帳號類型的資訊，請參閱 LINE for Business 上的 [Account Types of LINE Official Account](https://www.linebiz.com/jp-en/service/line-official-account/account-type/) 頁面。

<!-- note end -->

取得 LINE 官方帳號所在的多人聊天成員的使用者 ID。這包含尚未將 LINE 官方帳號加為好友，或已封鎖該 LINE 官方帳號的使用者的使用者 ID。

<!-- tip start -->

**你也可以從 webhook 取得使用者 ID**

當使用者加入多人聊天，或在多人聊天中傳送訊息時，會有 webhook 發送至 bot 伺服器。該 webhook 包含使用者 ID，因此你無需發出 API 請求即可取得使用者 ID。如需更多資訊，請參閱 Messaging API 文件中的 [Get a user ID from webhook](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-user-ids-in-webhook)。

<!-- tip end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/room/{roomId}/members/ids?start={continuationToken}' \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

roomId

聊天室 ID。可在[webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: optional) -->

start

[回應](https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids-response)所回傳的 JSON 物件中 `next` 屬性所含的延續權杖（continuation token）值。包含此參數（parameter）以取得群組成員的下一組使用者 ID 陣列（array）。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個帶有下列屬性的 JSON 物件。

<!-- parameter start -->

memberIds

Array of strings

多人聊天中成員的使用者 ID 清單。`memberIds` 僅包含 LINE for iOS 與 LINE for Android 的使用者。如需更多資訊，請參閱 [Consent on getting user profile information](https://developers.line.biz/en/docs/messaging-api/user-consent/)。\
上限：100 個使用者 ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

next

String

用於取得多人聊天中成員下一組使用者 ID 陣列的延續權杖。僅在原始請求的 `memberIds` 中尚有未回傳的使用者 ID 時才會回傳。

延續權杖會在 24 小時（86,400 秒）後過期。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "memberIds": ["U4af4980629...", "U0c229f96c4...", "U95afb1d4df..."],
  "next": "jxEWCEEP..."
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。請考慮以下原因：<ul><li>指定了無效的聊天室 ID。</li><li>`start` 屬性指定了無效的延續權杖。</li></ul> |
| `403` | 無權使用此端點。僅供已驗證帳號或[進階帳號](https://developers.line.biz/en/glossary/#premium-account)使用。 |
| `404` | 指定了不存在的多人聊天，或你的 LINE 官方帳號未參與的多人聊天。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid continuation token, such as expired (400 Bad Request)
{
  "message": "Invalid start param"
}
```

<!-- tab end -->

### Get multi-person chat member profile 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/room/{roomId}/member/{userId}`

若已知多人聊天成員的使用者 ID，則可取得 LINE 官方帳號所在多人聊天中該成員的個人檔案資訊。

<!-- tip start -->

**Tip**

無論使用者是否已將你的 LINE 官方帳號加為好友，或是否已封鎖你的 LINE 官方帳號，你都可以取得同一多人聊天中使用者的個人檔案資訊。

<!-- tip end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/room/{roomId}/member/{userId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

roomId

聊天室 ID。可在[webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。

<!-- parameter end -->
<!-- parameter start (props: required) -->

userId

使用者 ID。可在[webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。請勿使用 LINE 中所用的 LINE ID。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個帶有下列資訊的 JSON 物件。

<!-- parameter start -->

displayName

String

顯示名稱

<!-- parameter end -->
<!-- parameter start -->

userId

String

使用者 ID

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

pictureUrl

String

個人檔案圖片 URL。若使用者沒有個人檔案圖片，則回應中不會包含此項。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "displayName": "LINE taro",
  "userId": "U4af4980629...",
  "pictureUrl": "https://sprofile.line-scdn.net/0hHkIRkHJF..."
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 請求有問題。請考慮以下原因：<ul><li>指定了無效的聊天室 ID。</li><li>指定了無效的使用者 ID。</li></ul> |
| `404` | 無法取得個人檔案資訊。請考慮以下原因：<ul><li>指定了不存在的多人聊天，或你的 LINE 官方帳號未參與的多人聊天。</li><li>指定了不存在的使用者，或未加入多人聊天的使用者。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid room ID (400 Bad Request)
{
  "message": "The value for the 'roomId' parameter is invalid"
}

// If you specify a non-existent multi-person chat or user, or a multi-person chat that your LINE Official Account doesn't participate in (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Leave multi-person chat 

端點（endpoint）：`POST` `https://api.line.me/v2/bot/room/{roomId}/leave`

退出[多人聊天](https://developers.line.biz/en/docs/messaging-api/group-chats/#room)。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/room/{roomId}/leave \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

roomId

聊天室 ID。可在[webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

若你指定了你的 LINE 官方帳號未參與的多人聊天，同樣會回傳狀態碼 `200`。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error Response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                                    |
| ----- | ---------------------------------------------- |
| `400` | 指定了無效的聊天室 ID。               |
| `404` | 指定了不存在的多人聊天。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an invalid room ID (400 Bad Request)
{
  "message": "The value for the 'roomId' parameter is invalid"
}

// If you specify a non-existent multi-person chat (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

## Rich menu 

顯示於你的 LINE 官方帳號聊天畫面上的可自訂選單。如需更多資訊，請參閱 [Use rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)。

### Create rich menu 

端點（endpoint）：`POST` `https://api.line.me/v2/bot/richmenu`

建立 rich menu。

你必須[上傳 rich menu 圖片](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)，並[將 rich menu 設定為預設 rich menu](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu) 或[將 rich menu 連結至使用者](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)，rich menu 才會顯示。透過 Messaging API，每個 LINE 官方帳號最多可建立 1000 個 rich menu。

<!-- tip start -->

**建立 rich menu 之前**

另外也有一個用於[驗證 rich menu 物件](https://developers.line.biz/en/reference/messaging-api/#validate-rich-menu-object)的端點。

<!-- tip end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": false,
    "name": "Nice rich menu",
    "chatBarText": "Tap to open",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 2500,
          "height": 1686
        },
        "action": {
          "type": "postback",
          "data": "action=buy&itemid=123"
        }
      }
   ]
}'
```

<!-- tab end -->

#### Rate limit 

每小時 100 次請求

透過 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 建立與刪除 rich menu 不受此限制。

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

指定一個要顯示為 rich menu 的 [rich menu 物件](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)。

#### Response 

回傳狀態碼 `200` 與一個帶有下列資訊的 JSON 物件。

<!-- parameter start -->

richMenuId

String

rich menu 的 ID。在[上傳 rich menu 圖片](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)時使用。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "richMenuId": "{richMenuId}"
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法建立 rich menu。請考慮以下原因：<ul><li>指定了無效的 rich menu 物件。</li><li>已達到可建立的 rich menu 數量上限（最多 1000 個）。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a rich menu object that doesn't have a required JSON key for the rich menu object (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "must be specified",
      "property": "name"
    }
  ]
}

// If you specify an invalid scheme for a URI action (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "invalid uri",
      "property": "areas[0].action.uri"
    }
  ]
}
```

<!-- tab end -->

### Validate rich menu object 

端點（endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/validate`

驗證 rich menu 物件。

你可以驗證 [rich menu 物件](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)是否可作為[建立 rich menu](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu) 的有效請求主體（request body）。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/validate \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
      "width": 2500,
      "height": 1686
    },
    "selected": false,
    "name": "Nice rich menu",
    "chatBarText": "Tap to open",
    "areas": [
      {
        "bounds": {
          "x": 0,
          "y": 0,
          "width": 2500,
          "height": 1686
        },
        "action": {
          "type": "postback",
          "data": "action=buy&itemid=123"
        }
      }
   ]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

指定你想驗證的 [rich menu 物件](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)。

#### Response 

若請求主體可作為有效的 rich menu 物件，則回傳 HTTP 狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的 rich menu 物件。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a rich menu object that doesn't have a required JSON key for the rich menu object (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "must be specified",
      "property": "name"
    }
  ]
}

// If you specify an invalid scheme for a URI action (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "invalid uri",
      "property": "areas[0].action.uri"
    }
  ]
}
```

<!-- tab end -->

### Upload rich menu image 

端點（endpoint）：`POST` `https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 中傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

上傳並為 rich menu 設定圖片。

#### Requirements for rich menu image 

你可以使用符合以下規格的 rich menu 圖片：

- 圖片格式：JPEG 或 PNG
- 圖片寬度：800 至 2500 像素
- 圖片高度：250 像素以上
- 圖片長寬比（寬度 / 高度）：1.45 以上
- 最大檔案大小：1 MB

<!-- note start -->

**Note**

你無法替換已設定到 rich menu 的圖片。若要更新你的 rich menu 圖片，請建立新的 rich menu 物件並上傳另一張圖片。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: image/jpeg" \
-T image.jpg
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

`image/jpeg` 或 `image/png`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

richMenuId

要設定圖片的 rich menu 的 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法為 rich menu 設定圖片。請考慮以下原因：<ul><li>圖片不符合[要求](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image-requirements)。</li><li>rich menu 已設定圖片。</li></ul> |
| `404` | 指定了不存在的 rich menu。 |
| `415` | `Content-Type` 中指定了不支援的媒體格式（非 `image/jpeg` 與 `image/png`）。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify an image that doesn't meet the requirements (400 Bad Request)
{
  "message": "The image size is not allowed for richmenu"
}

// The image is already set to the rich menu (400 Bad Request)
{
  "message": "An image has already been uploaded to the richmenu"
}
```

<!-- tab end -->

### Download rich menu image 

端點（endpoint）：`GET` `https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content`

<!-- note start -->

**此網域名稱與其他端點不同**

此端點的網域名稱（`api-data.line.me`）用於在 Messaging API 的 LINE Platform 中傳送與接收大量資料。此網域名稱與其他端點（`api.line.me`）不同。

<!-- note end -->

下載與 rich menu 相關聯的圖片。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET "https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content" \
-H 'Authorization: Bearer {channel access token}' \
-o picture.jpg
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

richMenuId

要下載圖片的 rich menu 的 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與 rich menu 圖片的二進位資料。可如請求範例所示下載該圖片。

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `404` | 無法下載圖片。請考慮以下原因：<ul><li>指定了不存在的 rich menu。</li><li>rich menu 沒有設定圖片。</li></ul> |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If the rich menu doesn't exist (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get rich menu list 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/richmenu/list`

取得透過[建立 rich menu](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu) 所建立的所有 rich menu 的 rich menu 回應物件清單。

<!-- note start -->

**Note**

你無法取得透過 LINE Official Account Manager 建立的 rich menu。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/richmenu/list \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 10 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個帶有下列資訊的 JSON 物件。

<!-- parameter start -->

richmenus

Array

[rich menu 回應物件](https://developers.line.biz/en/reference/messaging-api/#rich-menu-response-object)的陣列

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "richmenus": [
    {
      "richMenuId": "{richMenuId}",
      "name": "Nice rich menu",
      "size": {
        "width": 2500,
        "height": 1686
      },
      "chatBarText": "Tap to open",
      "selected": false,
      "areas": [
        {
          "bounds": {
            "x": 0,
            "y": 0,
            "width": 2500,
            "height": 1686
          },
          "action": {
            "type": "postback",
            "data": "action=buy&itemid=123"
          }
        }
      ]
    }
  ]
}
```

<!-- tab end -->

#### Error response 

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

### Get rich menu 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/richmenu/{richMenuId}`

透過 rich menu ID 取得 rich menu。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/richmenu/{richMenuId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

richMenuId

rich menu 的 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個 [rich menu 回應物件](https://developers.line.biz/en/reference/messaging-api/#rich-menu-response-object)。

_回應範例_

<!-- tab start `json` -->

```json
{
  "richMenuId": "{richMenuId}",
  "name": "Nice rich menu",
  "size": {
    "width": 2500,
    "height": 1686
  },
  "chatBarText": "Tap to open",
  "selected": false,
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 2500,
        "height": 1686
      },
      "action": {
        "type": "postback",
        "data": "action=buy&itemid=123"
      }
    }
  ]
}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                            |
| ----- | -------------------------------------- |
| `404` | 指定了不存在的 rich menu。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a non-existent rich menu (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Delete rich menu 

端點（endpoint）：`DELETE` `https://api.line.me/v2/bot/richmenu/{richMenuId}`

刪除 rich menu。

<!-- note start -->

**rich menu 限制**

若你的 LINE 官方帳號透過 Messaging API 已達到 1,000 個 rich menu 的上限，則必須先刪除一個 rich menu，才能建立新的。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X DELETE https://api.line.me/v2/bot/richmenu/{richMenuId} \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每小時 100 次請求

透過 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager) 建立與刪除 rich menu 不受此限制。

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

richMenuId

rich menu 的 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                            |
| ----- | -------------------------------------- |
| `404` | 指定了不存在的 rich menu。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If you specify a non-existent rich menu (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Set default rich menu 

端點（endpoint）：`POST` `https://api.line.me/v2/bot/user/all/richmenu/{richMenuId}`

設定預設 rich menu。預設 rich menu 會顯示給所有開啟 LINE 官方帳號聊天畫面的使用者。若已設定預設 rich menu，呼叫此端點會以你請求中所指定的 rich menu 取代目前的預設 rich menu。

rich menu 會依以下優先順序（由高到低）顯示：

1. [透過 Messaging API 設定的個別使用者 rich menu](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)
1. 透過 Messaging API 設定的預設 rich menu
1. [透過 LINE Official Account Manager 設定的預設 rich menu](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-with-the-line-manager)

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/user/all/richmenu/{richMenuId} \
-H "Authorization: Bearer {channel access token}"
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

richMenuId

rich menu 的 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error Response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code  | Description                             |
| ----- | --------------------------------------- |
| `400` | rich menu 沒有設定圖片。 |
| `404` | 指定了不存在的 rich menu。  |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If there is no image set to the rich menu (400 Bad Request)
{
  "message": "must upload richmenu image before applying it to user",
  "details": []
}

// If you specify a non-existent rich menu (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Get default rich menu ID 

端點（endpoint）：`GET` `https://api.line.me/v2/bot/user/all/richmenu`

取得透過 Messaging API 設定的預設 rich menu 的 ID。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/user/all/richmenu \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個帶有下列資訊的 JSON 物件。

<!-- parameter start -->

richMenuId

String

rich menu 的 ID

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "richMenuId": "{richMenuId}"
}
```

<!-- tab end -->

#### Error Response 

回傳以下 HTTP 狀態碼與錯誤回應：

| Code | Description |
| --- | --- |
| `403` | 預設 rich menu 是由其他頻道（channel）所設定，例如 [LINE Official Account Manager](https://developers.line.biz/en/glossary/#line-oa-manager)。 |
| `404` | 尚未設定預設 rich menu。 |

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_錯誤回應範例_

<!-- tab start `json` -->

```json
// If the default rich menu is set by another channel (403 Forbidden)
{
  "message": "the richmenu is owned by another channel",
  "details": []
}

// If the default rich menu isn't set (404 Not Found)
{
  "message": "no default richmenu",
  "details": []
}
```

<!-- tab end -->

### Clear default rich menu 

端點（endpoint）：`DELETE` `https://api.line.me/v2/bot/user/all/richmenu`

清除透過 Messaging API 設定的預設 rich menu。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -v -X DELETE https://api.line.me/v2/bot/user/all/richmenu \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多有關速率限制的資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 與一個空的 JSON 物件。

_回應範例_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error Response 

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。
## Per-user rich menu 

你可以透過指定使用者 ID 與 rich menu ID，以每位使用者為單位設定 rich menu。詳情請參閱 Messaging API 文件中的 [Use per-user rich menus](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/)。

### Link rich menu to user 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId}`

將 rich menu 連結至某位使用者。同一時間只能將一個 rich menu 連結至一位使用者。如果使用者已連結了某個 rich menu，呼叫此端點會以你請求中指定的 rich menu 取代既有的 rich menu。

rich menu 會依下列優先順序顯示（由高至低）：

1. 透過 Messaging API 設定的 per-user rich menu
1. [透過 Messaging API 設定的預設 rich menu](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu)
1. [透過 LINE Official Account Manager 設定的預設 rich menu](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-with-the-line-manager)

#### Conditions for linking rich menu 

你可以將 rich menu 連結至已將你的 LINE Official Account 加為好友的使用者。

如果你嘗試將 rich menu 連結至下列使用者，會回傳狀態碼 `200`，但 rich menu 不會連結至該使用者：

- 已刪除其 LINE 帳號的使用者
- 已封鎖你的 LINE Official Account 的使用者
- 尚未將你的 LINE Official Account 加為好友的使用者
- 頻道（channel）中不存在的使用者 ID，例如從其他服務提供者（provider）底下的另一個頻道取得的 ID

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId} \
-H "Authorization: Bearer {channel access token}"
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

richMenuId

rich menu 的 ID

<!-- parameter end -->
<!-- parameter start (props: required) -->

userId

使用者 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件（object）中找到。請勿使用 LINE 中所用的 LINE ID。

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

回傳下列 HTTP 狀態碼及錯誤回應（response）：

| Code | Description |
| --- | --- |
| `400` | 無法連結 rich menu。可能的原因如下：<ul><li>指定了無效的使用者 ID。</li><li>rich menu 未設定任何圖片。</li></ul> |
| `404` | 指定了不存在的 rich menu。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

若回傳錯誤，rich menu 不會被解除連結。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The value for the 'userId' parameter is invalid"
}

// If you specify a non-existent rich menu (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Link rich menu to multiple users 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/bulk/link`

將 rich menu 連結至多位使用者。

rich menu 會依下列優先順序顯示（由高至低）：

1. 透過 Messaging API 設定的 per-user rich menu
1. [透過 Messaging API 設定的預設 rich menu](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu)
1. [透過 LINE Official Account Manager 設定的預設 rich menu](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-with-the-line-manager)

與[將 rich menu 連結至單一使用者](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)不同，此請求是在背景以非同步方式處理。通常會在幾秒內完成。

即使回傳狀態碼 `202`，rich menu 也可能未連結。若要確認請求是否處理成功，請[取得連結至使用者的 rich menu ID](https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-id-of-user)，並檢查 rich menu 是否確實連結至使用者。

若回傳[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#bulk-link-rich-menu-error-response)，rich menu 不會連結至任何使用者。

#### Conditions for linking rich menu 

你可以將 rich menu 連結至已將你的 LINE Official Account 加為好友的使用者。若回傳狀態碼 `202`，rich menu 會連結至請求中指定的使用者。

即使回傳狀態碼 `202`，下列使用者也可能因尚未與你的 LINE Official Account 成為好友而無法連結至 rich menu：

- 已刪除其 LINE 帳號的使用者
- 已封鎖你的 LINE Official Account 的使用者
- 尚未將你的 LINE Official Account 加為好友的使用者
- 頻道中不存在的使用者 ID，例如從其他服務提供者底下的另一個頻道取得的 ID

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/bulk/link \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
  "richMenuId":"{richMenuId}",
  "userIds":["{userId1}","{userId2}"]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

richMenuId

String

rich menu 的 ID

<!-- parameter end -->
<!-- parameter start (props: required) -->

userIds

Array of strings

使用者 ID 的陣列（array）。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。請勿使用 LINE 中所用的 LINE ID。\
上限：500 個使用者 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `202` 及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法連結 rich menu。可能的原因如下：<ul><li>指定了無效的使用者 ID。</li><li>指定了無效的 rich menu ID。</li><li>rich menu 未設定任何圖片。</li></ul> |
| `404` | 指定了不存在的 rich menu。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The property, 'userIds[0]', in the request body is invalid (line: -, column: -)"
}

// If you specify an invalid rich menu ID (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "invalid richMenuId",
      "property": "richMenuId"
    }
  ]
}

// If you specify a non-existent rich menu (404 Not Found)
{
    "message": "richmenu not found",
    "details": []
}
```

<!-- tab end -->

### Get rich menu ID of user 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/user/{userId}/richmenu`

取得連結至某位使用者的 rich menu 的 ID。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/user/{userId}/richmenu \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

userId

使用者 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。請勿使用 LINE 中所用的 LINE ID。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 及一個包含下列資訊的 JSON 物件。

<!-- parameter start -->

richMenuId

String

rich menu 的 ID

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "richMenuId": "{richMenuId}"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的使用者 ID。 |
| `404` | 無法取得 rich menu ID。可能的原因如下：<ul><li>該使用者未連結至任何 rich menu。</li><li>指定了不存在的使用者。</li><li>該使用者尚未將目標 LINE Official Account 加為好友。</li></ul> |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The value for the 'userId' parameter is invalid"
}

// If you specify the user to whom the rich menu isn't linked (404 Not Found)
{
  "message": "the user has no richmenu",
  "details": []
}
```

<!-- tab end -->

### Unlink rich menu from user 

端點（Endpoint）：`DELETE` `https://api.line.me/v2/bot/user/{userId}/richmenu`

移除連結至指定使用者的 per-user rich menu 的 API。

#### Conditions for unlinking rich menu 

你可以從已將你的 LINE Official Account 加為好友的使用者解除 rich menu 的連結。

如果你嘗試從下列使用者解除 rich menu 的連結，會回傳狀態碼 `200`，但 rich menu 不會從該使用者解除連結：

- 已刪除其 LINE 帳號的使用者
- 已封鎖你的 LINE Official Account 的使用者
- 尚未將你的 LINE Official Account 加為好友的使用者
- 頻道中不存在的使用者 ID，例如從其他服務提供者底下的另一個頻道取得的 ID

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X DELETE https://api.line.me/v2/bot/user/{userId}/richmenu \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

userId

使用者 ID。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。請勿使用 LINE 中所用的 LINE ID。

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

回傳下列 HTTP 狀態碼及錯誤回應：

| Code  | Description                      |
| ----- | -------------------------------- |
| `400` | 指定了無效的使用者 ID。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The value for the 'userId' parameter is invalid"
}
```

<!-- tab end -->

### Unlink rich menus from multiple users 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/bulk/unlink`

從多位使用者解除 rich menu 的連結。

與[從單一使用者解除 rich menu 連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)不同，此請求是在背景以非同步方式處理。通常會在幾秒內完成。

即使回傳狀態碼 `202`，rich menu 也可能未解除連結。若要確認請求是否處理成功，請[取得連結至使用者的 rich menu ID](https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-id-of-user)，並檢查已解除連結的 rich menu 是否確實未連結至使用者。

若回傳[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#bulk-unlink-rich-menu-error-response)，rich menu 不會從任何使用者解除連結。

#### Conditions for unlinking rich menu 

你可以從已將你的 LINE Official Account 加為好友的使用者解除 rich menu 的連結。若回傳狀態碼 `202`，rich menu 會從請求中指定的使用者解除連結。

即使回傳狀態碼 `202`，下列使用者也可能因尚未與你的 LINE Official Account 成為好友而無法從 rich menu 解除連結：

- 已刪除其 LINE 帳號的使用者
- 已封鎖你的 LINE Official Account 的使用者
- 尚未將你的 LINE Official Account 加為好友的使用者
- 頻道中不存在的使用者 ID，例如從其他服務提供者底下的另一個頻道取得的 ID

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/bulk/unlink \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
  "userIds":["{userId1}","{userId2}"]
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

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

userIds

Array of strings

使用者 ID 的陣列。可在 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的 `source` 物件中找到。請勿使用 LINE 中所用的 LINE ID。\
上限：500 個使用者 ID

<!-- parameter end -->

#### Response 

回傳狀態碼 `202` 及一個空的 JSON 物件。

_Example response_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code  | Description                      |
| ----- | -------------------------------- |
| `400` | 指定了無效的使用者 ID。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify an invalid user ID (400 Bad Request)
{
  "message": "The property, 'userIds[0]', in the request body is invalid (line: -, column: -)"
}
```

<!-- tab end -->

### Replace or unlink the linked rich menus in batches 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/batch`

你可以使用此端點，對透過如[將 rich menu 連結至使用者](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)等端點連結至使用者的 rich menu 進行批次控制。可用的操作如下：

1. 將連結至特定 rich menu 的所有使用者的 rich menu，替換為另一個 rich menu。
1. 解除連結至特定 rich menu 的所有使用者的 rich menu。
1. 解除所有連結至 rich menu 的使用者的 rich menu。

你也可以在[請求主體（request body）](https://developers.line.biz/en/reference/messaging-api/#batch-control-rich-menus-of-users-request-body)的 `operations` 屬性（property）中指定多個 rich menu 批次操作。若你指定多個 rich menu 批次操作，每個批次操作會針對每位使用者獨立且平行地處理。你所指定的批次操作彼此不會互相影響。

例如，若你在 `operations` 屬性中指定下列陣列，請求前連結至 rich menu A 的使用者其 rich menu 會被替換為 B，而請求前連結至 rich menu B 的使用者其 rich menu 會被替換為 C。請求前連結至 rich menu A 的使用者其 rich menu 不會被替換為 C，因為批次操作彼此不會互相影響。

```json
[
  {
    "type": "link",
    "from": "{ID of rich menu A}",
    "to": "{ID of rich menu B}"
  },
  {
    "type": "link",
    "from": "{ID of rich menu B}",
    "to": "{ID of rich menu C}"
  }
]
```

rich menu 的批次操作會在背景以非同步方式處理。你可以使用[取得 rich menu 批次控制的狀態](https://developers.line.biz/en/reference/messaging-api/#get-batch-control-rich-menus-progress-status)端點來查詢處理狀態。

#### How to avoid unintended operations when retrying 

透過使用 `resumeRequestKey` 屬性，你可以安全地重試。

在下列情況中，若你在重試時未使用 `resumeRequestKey` 屬性，rich menu 可能會被替換為非預期的內容。

- 由於逾時或 LINE Platform 的內部伺服器錯誤，你不確定請求是否已被接受
- 你[取得 rich menu 批次操作進度狀態](https://developers.line.biz/en/reference/messaging-api/#get-batch-control-rich-menus-progress-status)後，回應的 `phase` 屬性為 `failed`

即使在這些情況下，若你在第一次請求時在 `resumeRequestKey` 屬性中指定任意的金鑰，使用相同金鑰再次傳送請求時，僅會針對尚未完成處理的使用者繼續處理。

`resumeRequestKey` 屬性會在 14 天（336 小時）後過期。若已過期，該請求會被視為新的請求。

_Example of a request to replace a rich menu and unlink a rich menu_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/batch \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
  "operations": [
    {
      "type": "link",
      "from": "{rich menu ID before replacement}",
      "to": "{rich menu ID after replacement}"
    },
    {
      "type": "unlink",
      "from": "{rich menu ID to unlink}"
    }
  ],
  "resumeRequestKey": "{an arbitrary key string matching the regular expression pattern [0-9a-zA-Z\-_]{1,100}}"
}'
```

<!-- tab end -->

_Example of a request to unlink a linked rich menu from all users_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/batch \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
  "operations": [
    {
      "type": "unlinkAll"
    }
  ],
  "resumeRequestKey": "{an arbitrary key string matching the regular expression pattern [0-9a-zA-Z\-_]{1,100}}"
}'
```

<!-- tab end -->

#### Rate limit 

每小時 3 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

<!-- tip start -->

**你可以事先驗證請求主體**

另外還有[驗證 rich menu 批次控制請求](https://developers.line.biz/en/reference/messaging-api/#validate-batch-control-rich-menus-request)端點，可用於事先驗證請求主體。

透過使用驗證端點，你可以事先確認你的請求不會導致錯誤，且不受此端點速率限制的約束。

<!-- tip end -->

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

operations

Array of [Rich menu operation object](https://developers.line.biz/en/reference/messaging-api/#batch-control-rich-menus-of-users-operations)

指定 rich menu 的批次操作。\
上限：1,000 個物件

<!-- parameter end -->
<!-- parameter start (props: optional) -->

resumeRequestKey

String

用於重試的金鑰。金鑰值為符合正規表示式模式 `[0-9a-zA-Z\-_]{1,100}` 的字串。

<!-- parameter end -->

##### Rich menu operation object 

rich menu 操作物件（Rich menu operation object）代表對連結至使用者的 rich menu 進行的批次操作。

<!-- parameter start (props: required) -->

type

String

對連結至使用者的 rich menu 進行的操作。為下列其中之一：

- `link`：針對所有連結至 `from` 屬性所指定 rich menu 的使用者，將其 rich menu 替換為 `to` 屬性所指定的 rich menu。
- `unlink`：解除所有連結至 `from` 屬性所指定 rich menu 的使用者的 rich menu。
- `unlinkAll`：解除所有連結至 rich menu 的使用者的 rich menu。

若你指定 `unlinkAll`，則 `operations` 屬性中不能包含 `unlinkAll` 以外的 `type`。

<!-- parameter end -->
<!-- parameter start (props: annotation="Required if type is link or unlink") -->

from

String

rich menu 的 ID。

指定替換前的 rich menu ID 或要解除連結的 rich menu ID。

若你在 `operations` 屬性中指定多個操作，不能在多個 `from` 屬性中指定相同的 rich menu ID。

<!-- parameter end -->
<!-- parameter start (props: annotation="Required if type is link") -->

to

String

rich menu 的 ID。

指定要被替換成的 rich menu ID。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個空的 JSON 物件。

rich menu 的批次操作會在背景以非同步方式處理。你可以使用[取得 rich menu 批次控制的狀態](https://developers.line.biz/en/reference/messaging-api/#get-batch-control-rich-menus-progress-status)端點來查詢處理狀態。

_Response example_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法控制 rich menu。可能的原因如下：<ul><li>指定了無效的 rich menu ID。</li><li>你想替換成的 rich menu 沒有圖片。</li><li>在 `operations` 屬性中指定了超過 1000 個操作。</li><li>同時在 `type` 屬性中指定了 `unlinkAll` 與其他類型。</li><li>在多個 `from` 屬性中指定了相同的 rich menu ID。</li></ul> |
| `404` | 指定了不存在的 rich menu。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

若回傳錯誤回應，rich menu 不會連結至任何使用者。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify an invalid rich menu ID (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "invalid richMenuId",
      "property": "operations[0].from"
    }
  ]
}

// If you specify the ID of the same rich menu in multiple from properties (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "from richmenu (richmenu-6fc298...) is duplicated",
      "property": "operations[].from"
    }
  ]
}

// If you specify unlinkAll and other types to the type property in the request at the same time (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "'unlinkAll' type can't be combined with other type",
      "property": "operations[].type"
    }
  ]
}
```

<!-- tab end -->

### Get the status of rich menu batch control 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/richmenu/progress/batch`

取得[批次替換或解除已連結 rich menu](https://developers.line.biz/en/reference/messaging-api/#batch-control-rich-menus-of-users)的狀態。

超過 `acceptedTime` 中所顯示時間戳記的 14 天（336 小時）後，你將無法再取得狀態。

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X GET 'https://api.line.me/v2/bot/richmenu/progress/batch?requestId={request_id}' \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}'
```

<!-- tab end -->

#### Rate limit 

每小時 100 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

requestId

用於批次控制連結至使用者的 rich menu 的請求 ID。每個 Messaging API 請求都有一個請求 ID。可在[回應標頭（response headers）](https://developers.line.biz/en/reference/messaging-api/#response-headers)中找到。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個包含下列資訊的 JSON 物件。

<!-- parameter start -->

phase

String

目前的狀態。為下列其中之一：

- `ongoing`：rich menu 批次控制正在進行中。
- `succeeded`：rich menu 批次控制已完成。
- `failed`：rich menu 批次控制失敗。這表示有一位或多位使用者的 rich menu 無法被控制。也可能有部分使用者的操作已成功完成。

<!-- parameter end -->
<!-- parameter start -->

acceptedTime

String

批次控制 rich menu 之請求被接受的時間（以毫秒計）。

- 格式：[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)（例如 `2020-12-03T10:15:30.121Z`）
- 時區：UTC

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

completedTime

String

rich menu 批次控制完成的時間（以毫秒計）。當 `phase` 屬性為 `succeeded` 或 `failed` 時回傳。

- 格式：[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)（例如 `2020-12-03T10:15:30.121Z`）
- 時區：UTC

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "phase": "succeeded",
  "acceptedTime": "2023-06-26T07:37:21.083Z",
  "completedTime": "2023-06-26T09:12:12.197Z"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 指定了無效的請求 ID。 |
| `404` | 無法取得狀態。可能的原因如下：<ul><li>指定了不存在的請求 ID。</li><li>取得狀態的期限已過期。</li></ul> |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Example error response_

<!-- tab start `json` -->

```json
// If you specify a non-existent request ID (404 Not Found)
{
  "message": "Not found"
}
```

<!-- tab end -->

### Validate a request of rich menu batch control 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/validate/batch`

驗證[批次替換或解除已連結 rich menu](https://developers.line.biz/en/reference/messaging-api/#batch-control-rich-menus-of-users)端點的請求主體。

你可以使用此端點偵測下列錯誤，這些錯誤與你實際批次替換或解除已連結 rich menu 時相同：

- 若你指定不存在的 rich menu
- 若你指定沒有圖片的 rich menu
- 若你在 `operations` 屬性中指定多個操作且操作有誤
  - 當 `operations` 屬性中指定超過 1,000 個陣列時
  - 當 `type` 屬性同時為 `unlinkAll` 與其他 `type` 時
  - 當多個 `from` 屬性中指定了相同的 rich menu ID 時
- 若你在 `resumeRequestKey` 屬性中指定無效的字串

_Example request_

<!-- tab start `shell` -->

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/validate/batch \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: application/json" \
-d '{
  "operations": [
    {
      "type": "link",
      "from": "{rich menu ID before replacing}",
      "to": "{rich menu ID after replacing}"
    },
    {
      "type": "unlink",
      "from": "{rich menu ID to unlink}"
    }
  ],
  "resumeRequestKey": "{an arbitrary key string matching the regular expression pattern [0-9a-zA-Z\-_]{1,100}}"
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

operations

Array of [Rich menu operation object](https://developers.line.biz/en/reference/messaging-api/#batch-control-rich-menus-of-users-operations)

定義對 rich menu 進行的批次操作。\
上限：1,000 個物件

<!-- parameter end -->
<!-- parameter start (props: optional) -->

resumeRequestKey

String

用於重試的金鑰。金鑰值為符合正規表示式模式 `[0-9a-zA-Z\-_]{1,100}` 的字串。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個空的 JSON 物件。

_Response example_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法控制 rich menu。可能的原因如下：<ul><li>指定了無效的 rich menu ID。</li><li>你想替換成的 rich menu 沒有圖片。</li><li>在 `operations` 屬性中指定了超過 1000 個操作。</li><li>同時在 `type` 屬性中指定了 `unlinkAll` 與其他類型。</li><li>在多個 `from` 屬性中指定了相同的 rich menu ID。</li></ul> |
| `404` | 指定了不存在的 rich menu。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify a rich menu with no images (400 Bad Request)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "'to' richmenu (richmenu-0c757d...) must have image but it doesn't",
      "property": "operations[0].to"
    }
  ]
}

// If you specify a non-existent rich menu ID (404 Not Found)
{
  "message": "The request body has 1 error(s)",
  "details": [
    {
      "message": "Richmenu (richmenu-d3385e...) is not found",
      "property": "operations[0].to"
    }
  ]
}
```

<!-- tab end -->

## Rich menu alias 

你可以使用 [rich menu alias](https://developers.line.biz/en/glossary/#rich-menu-alias) 與 [rich menu switch action](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action) 提供使用者可切換分頁的 rich menu。詳情請參閱 Messaging API 文件中的 [Switch between tabs on rich menus](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/)。

### Create rich menu alias 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/alias`

建立 rich menu alias。

若要建立 rich menu alias，請務必事先完成下列工作。詳情請參閱 Messaging API 文件中的 [Switch between tabs on rich menus](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/)。

- [建立 rich menu](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu)
- [上傳 rich menu 圖片](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)

使用 Messaging API，每個 LINE Official Account 最多可建立 1000 個 rich menu alias。

_Request example_

<!-- tab start `shell` -->

```sh
# Example of creating rich menu alias A
curl -v -X POST https://api.line.me/v2/bot/richmenu/alias \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "richMenuAliasId": "richmenu-alias-a",
    "richMenuId": "richmenu-862e6ad6c267d2ddf3f42bc78554f6a4"
}'

# Example of creating rich menu alias B
curl -v -X POST https://api.line.me/v2/bot/richmenu/alias \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "richMenuAliasId":"richmenu-alias-b",
    "richMenuId":"richmenu-88c05ef6921ae53f8b58a25f3a65faf7"
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

richMenuAliasId

String

rich menu alias ID，可以是任意 ID，在每個頻道中須為唯一。

- 字元數上限：32
- 支援的字元類型：半形英數字（`a-z`、`0-9`）、底線（`_`）與連字號（`-`）

<!-- parameter end -->
<!-- parameter start (props: required) -->

richMenuId

String

要與此 rich menu alias 關聯的 rich menu ID。

<!-- note start -->

**關於可關聯的 rich menu**

rich menu alias 只能與在同一個頻道中建立的 rich menu 關聯。

<!-- note end -->

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個空的 JSON 物件。

_Response example_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法建立 rich menu alias。可能的原因如下：<ul><li>指定了不存在的 rich menu 或未設定圖片的 rich menu。</li><li>指定了無效的 rich menu alias ID。</li><li>指定了無效的 rich menu ID。</li><li>已達到可建立的 rich menu alias 數量上限。</li><li>指定了與既有 rich menu alias 相同的 ID。</li></ul> |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify a rich menu that doesn't exist or a rich menu ID without a set image (400 Bad Request)
{
    "message": "richmenu not found",
    "details": []
}

// If you specify an invalid rich menu ID (400 Bad Request)
{
    "message": "The request body has 1 error(s)",
    "details": [
        {
            "message": "invalid richMenuId",
            "property": "richMenuId"
        }
    ]
}

// If you specify the same rich menu alias ID as an existing rich menu alias (400 Bad Request)
{
    "message": "conflict richmenu alias id",
    "details": []
}
```

<!-- tab end -->

### Delete rich menu alias 

端點（Endpoint）：`DELETE` `https://api.line.me/v2/bot/richmenu/alias/{richMenuAliasId}`

刪除 rich menu alias。

<!-- note start -->

**關於 rich menu alias 數量上限**

使用 Messaging API，每個 LINE Official Account 最多可建立 1,000 個 rich menu alias。一旦達到此上限，你必須先刪除既有的 rich menu alias 才能建立新的 rich menu alias。

<!-- note end -->

_Request example_

<!-- tab start `shell` -->

```sh
# Example of deleting rich menu alias A
curl -v -X DELETE https://api.line.me/v2/bot/richmenu/alias/richmenu-alias-a \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每小時 100 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameter 

<!-- parameter start (props: required) -->

richMenuAliasId

你想刪除的 rich menu alias ID。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個空的 JSON 物件。

_Response example_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code  | Description                                  |
| ----- | -------------------------------------------- |
| `400` | 指定了無效的 rich menu alias ID。  |
| `404` | 指定了不存在的 rich menu alias。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify a rich menu alias that doesn't exist (404 Not Found)
{
  "message": "richmenu alias not found",
  "details": []
}
```

<!-- tab end -->

### Update rich menu alias 

端點（Endpoint）：`POST` `https://api.line.me/v2/bot/richmenu/alias/{richMenuAliasId}`

更新 rich menu alias。你可以指定既有的 rich menu alias，以修改其關聯的 rich menu。

<!-- note start -->

**更新何時會反映？**

由於快取資料的關係，rich menu alias 的更新可能不會立即反映。

<!-- note end -->

_Request example_

<!-- tab start `shell` -->

```sh
# Example of when you want to update rich menu alias A
curl -v -X POST https://api.line.me/v2/bot/richmenu/alias/richmenu-alias-a \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "richMenuId": "richmenu-862e6ad6c267d2ddf3f42bc78554f6a4"
}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Path parameter 

<!-- parameter start (props: required) -->

richMenuAliasId

你想更新的 rich menu alias ID。

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

richMenuId

String

要與此 rich menu alias 關聯的 rich menu ID

<!-- note start -->

**關於可關聯的 rich menu**

rich menu alias 只能與在同一個頻道中建立的 rich menu 關聯。

<!-- note end -->

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個空的 JSON 物件。

_Response example_

<!-- tab start `json` -->

```json
{}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code | Description |
| --- | --- |
| `400` | 無法更新 rich menu alias。可能的原因如下：<ul><li>指定了不存在的 rich menu 或未設定圖片的 rich menu。</li><li>指定了無效的 rich menu alias ID。</li><li>指定了無效的 rich menu ID。</li></ul> |
| `404` | 指定了不存在的 rich menu alias。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify a rich menu that doesn't exist or a rich menu ID without a set image (400 Bad Request)
{
    "message": "richmenu not found",
    "details": []
}

// If you specify an invalid rich menu ID (400 Bad Request)
{
    "message": "The request body has 1 error(s)",
    "details": [
        {
            "message": "invalid richMenuId",
            "property": "richMenuId"
        }
    ]
}
```

<!-- tab end -->

### Get rich menu alias information 

端點（Endpoint）：`GET` `https://api.line.me/v2/bot/richmenu/alias/{richMenuAliasId}`

指定 rich menu alias ID 以取得該 rich menu alias 的資訊。

_Request example_

<!-- tab start `shell` -->

```sh
# Example of when you want to get the information of rich menu alias A
curl -v -X GET https://api.line.me/v2/bot/richmenu/alias/richmenu-alias-a \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需速率限制的詳細資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request header

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameter 

<!-- parameter start (props: required) -->

richMenuAliasId

你想取得資訊的 rich menu alias ID。

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼及一個空的 JSON 物件。

<!-- parameter start -->

richMenuAliasId

String

rich menu alias ID。

<!-- parameter end -->
<!-- parameter start -->

richMenuId

String

與此 rich menu alias 關聯的 rich menu ID。

<!-- parameter end -->

_Response example_

<!-- tab start `json` -->

```json
{
  "richMenuAliasId": "richmenu-alias-a",
  "richMenuId": "richmenu-88c05ef6921ae53f8b58a25f3a65faf7"
}
```

<!-- tab end -->

#### Error response 

回傳下列 HTTP 狀態碼及錯誤回應：

| Code  | Description                                  |
| ----- | -------------------------------------------- |
| `400` | 指定了無效的 rich menu alias ID。  |
| `404` | 指定了不存在的 rich menu alias。 |

如需更多資訊，請參閱[共通規格（Common specifications）](https://developers.line.biz/en/reference/messaging-api/#common-specifications)章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

_Error response example_

<!-- tab start `json` -->

```json
// If you specify a rich menu alias that doesn't exist (404 Not Found)
{
  "message": "richmenu alias not found",
  "details": []
}
```

<!-- tab end -->
### Get list of rich menu alias 

Endpoint: `GET` `https://api.line.me/v2/bot/richmenu/alias/list`

取得 rich menu alias 清單。

_Request example_

<!-- tab start `shell` -->

```sh
curl -v -X GET https://api.line.me/v2/bot/richmenu/alias/list \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Rate limit 

每秒 2,000 次請求

如需更多速率限制（rate limit）的相關資訊，請參閱 [Rate limits](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

#### Request header 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Response 

回傳 `200` HTTP 狀態碼以及一個包含下列值的 JSON 物件（object）。

<!-- parameter start -->

aliases\[].richMenuAliasId

String

Rich menu alias ID。

<!-- parameter end -->
<!-- parameter start -->

aliases\[].richMenuId

String

與該 rich menu alias 相關聯的 rich menu ID。

<!-- parameter end -->

_Response example_

<!-- tab start `json` -->

```json
// If you have 2 rich menu aliases
{
    "aliases": [
        {
            "richMenuAliasId": "richmenu-alias-a",
            "richMenuId": "richmenu-862e6ad6c267d2ddf3f42bc78554f6a4"
        },
        {
            "richMenuAliasId": "richmenu-alias-b",
            "richMenuId": "richmenu-88c05ef6921ae53f8b58a25f3a65faf7"
        }
    ]
}

// If you have 0 rich menu alias
{
    "aliases": []
}
```

<!-- tab end -->

#### Error response 

如需更多資訊，請參閱 [Common specifications](https://developers.line.biz/en/reference/messaging-api/#common-specifications) 章節中的 [Status codes](https://developers.line.biz/en/reference/messaging-api/#status-codes) 與 [Error responses](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

## Account link 

你可以將 provider（企業與開發者）所提供的服務帳號與 LINE 使用者的帳號進行連結。

### Issue link token 

Endpoint: `POST` `https://api.line.me/v2/bot/user/{userId}/linkToken`

核發用於 [account link](https://developers.line.biz/en/docs/messaging-api/linking-accounts/) 功能的 link token。

_Example request_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/v2/bot/user/{userId}/linkToken \
-H 'Authorization: Bearer {channel access token}'
```

<!-- tab end -->

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`

<!-- parameter end -->

#### Path parameters 

<!-- parameter start (props: required) -->

userId

要連結的 LINE 帳號的使用者 ID。可在 [account link event](https://developers.line.biz/en/reference/messaging-api/#account-link-event) 物件的 `source` 物件中找到。請勿使用 LINE 中所使用的 LINE ID。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及一個包含下列值的 JSON 物件。

<!-- parameter start -->

linkToken

String

Link token。Link token 的有效期間為 10 分鐘，且只能使用一次。

<!-- note start -->

**Note**

有效期間可能在不另行通知的情況下變更。

<!-- note end -->

<!-- parameter end -->

_Example response_

<!-- tab start `json` -->

```json
{
  "linkToken": "NMZTNuVrPTqlr2IF8Bnymkb7rXfYv5EY"
}
```

<!-- tab end -->

## Message objects 

包含你所要傳送訊息內容的 JSON 物件。

<!-- tip start -->

**驗證 message objects**

透過下列端點（endpoint），你可以驗證 message objects：

- [Validate message objects of a reply message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-reply-message)
- [Validate message objects of a push message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-push-message)
- [Validate message objects of a multicast message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-multicast-message)
- [Validate message objects of a narrowcast message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-narrowcast-message)
- [Validate message objects of a broadcast message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-broadcast-message)

<!-- tip end -->

### Common properties for messages 

下列屬性（property）可在所有的 message objects 中指定。

#### Quick reply 

這些屬性用於 quick reply 功能。如需更多資訊，請參閱 [Use quick replies](https://developers.line.biz/en/docs/messaging-api/using-quick-reply/)。

<!-- parameter start (props: optional) -->

quickReply

Object

[items object](https://developers.line.biz/en/reference/messaging-api/#items-object)

<!-- parameter end -->

如果使用者收到多個 [message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)，則會顯示最後一個 message object 的 `quickReply` 屬性。

##### items object 

這是一個包含 [quick reply 按鈕](https://developers.line.biz/en/reference/messaging-api/#quick-reply-button-object) 的容器。

<!-- parameter start (props: required) -->

items

Array of objects

[Quick reply button objects](https://developers.line.biz/en/reference/messaging-api/#quick-reply-button-object)。\
上限：13 個物件

<!-- parameter end -->

_Example items object_

<!-- tab start `json` -->

```json
"quickReply": {
  "items": [
    {
      "type": "action",
      "action": {
        "type": "cameraRoll",
        "label": "Send photo"
      }
    },
    {
      "type": "action",
      "action": {
        "type": "camera",
        "label": "Open camera"
      }
    }
  ]
}
```

<!-- tab end -->

##### Quick reply button object 

這是一個以按鈕形式顯示的 quick reply 選項。

<!-- parameter start (props: required) -->

type

String

`action`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageUrl

String

顯示在按鈕開頭的圖示 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
圖片格式：PNG\
長寬比：1:1（寬 : 高）\
檔案大小上限：1 MB

圖片大小沒有限制。\
如果 `action` 屬性為 [camera action](https://developers.line.biz/en/reference/messaging-api/#camera-action)、[camera roll action](https://developers.line.biz/en/reference/messaging-api/#camera-roll-action) 或 [location action](https://developers.line.biz/en/reference/messaging-api/#location-action)，且未設定 `imageUrl` 屬性，則會顯示預設圖示。

URL 應使用 UTF-8 進行百分比編碼（percent-encode）。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

action

Object

點選此按鈕時所執行的動作。指定一個 [action object](https://developers.line.biz/en/reference/messaging-api/#action-objects)。以下為可用動作的清單：

- [Postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)
- [Message action](https://developers.line.biz/en/reference/messaging-api/#message-action)
- [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)
- [Datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)
- [Camera action](https://developers.line.biz/en/reference/messaging-api/#camera-action)
- [Camera roll action](https://developers.line.biz/en/reference/messaging-api/#camera-roll-action)
- [Location action](https://developers.line.biz/en/reference/messaging-api/#location-action)
- [Clipboard action](https://developers.line.biz/en/reference/messaging-api/#clipboard-action)

<!-- parameter end -->

如果不支援 quick reply 功能的 LINE 版本收到含有 quick reply 按鈕的訊息，則只會顯示訊息。

#### Customize icon and display name 

從 LINE 官方帳號傳送訊息時，你可以在 [Message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中指定 `sender.name` 與 `sender.iconUrl` 屬性。

<!-- parameter start (props: optional) -->

sender.name

String

顯示名稱。某些字詞（例如 `LINE`）可能無法使用。\
字元數上限：20

<!-- parameter end -->
<!-- parameter start (props: optional) -->

sender.iconUrl

String

傳送訊息時用來顯示為圖示的圖片 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
圖片格式：PNG\
長寬比：1:1（寬 : 高）\
檔案大小上限：1 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->

_自訂圖示與顯示名稱的文字訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "text",
  "text": "Hello, I am Cony!!",
  "sender": {
    "name": "Cony",
    "iconUrl": "https://line.me/conyprof"
  }
}
```

<!-- tab end -->

### Text message 

<!-- note start -->

**emoji 的字元數與索引位置**

設定於屬性中的文字裡，emoji 的字元數與索引位置必須是以 UTF-16 編碼時的 code unit 數量與位置。對於某些字元，例如使用 surrogate pair 的字元以及可用 UTF-16 表示的 emoji，請將它們計算為多個字元而非一個。

如需更多資訊，請參閱 Messaging API 文件中的 [Character counting in a text](https://developers.line.biz/en/docs/messaging-api/text-character-count/)。

<!-- note end -->

<!-- parameter start (props: required) -->

type

String

`text`

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

訊息文字。你可以包含下列 emoji：

- LINE emoji。使用 `$` 字元作為佔位符（placeholder），並在 `emojis` 屬性中指定你想使用的 LINE emoji 的 `product ID` 與 `emoji ID`。如需更多資訊，請參閱 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。
- Unicode emoji

字元數上限：5000

<!-- warning start -->

**「LINE original unicode emojis」已於 2022 年 3 月 31 日停止提供**

請改用搭配 `emojis` 屬性的「LINE Emoji」，而非「LINE original unicode emojis」。

如需更多資訊，請參閱 2022 年 4 月 1 日的消息 [「LINE original unicode emojis」of the Messaging API has been discontinued as of March 31, 2022](https://developers.line.biz/en/news/2022/04/01/line-original-unicode-emojis-has-been-discontinued/) 以及 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- warning end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

emojis

Array of LINE emoji objects

一個或多個 LINE emoji。\
上限：20 個 LINE emoji

<!-- parameter end -->
<!-- parameter start (props: optional) -->

emojis.index

Number

`text` 中代表 LINE emoji 佔位符的 `$` 的索引位置，第一個字元位於位置 `0`。詳情請參閱文字訊息範例。

<!-- note start -->

**Note**

如果你指定的位置與 `$` 的位置不符，API 會回傳 HTTP `400 Bad request`。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

emojis.productId

String

一組 LINE emoji 的 Product ID。如需更多 product ID 的相關資訊，請參閱 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

emojis.emojiId

String

Emoji ID。如需更多可透過 Messaging API 傳送的 LINE emoji 的 emoji ID 相關資訊，請參閱 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

quoteToken

String

你想引用的訊息的 quote token。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->

_文字訊息範例_

<!-- tab start `json` -->

```json
{
    "type": "text",
    "text": "Hello, world"
}
```

<!-- tab end -->

_含有 LINE emoji 的文字訊息範例_

<!-- tab start `json` -->

```json
{
    "type": "text",
    "text": "$ LINE emoji $",
    "emojis": [
      {
        "index": 0,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "001"
      },
      {
        "index": 13,
        "productId": "5ac1bfd5040ab15980c9b435",
        "emojiId": "002"
      }
    ]
}
```

<!-- tab end -->

_引用過往訊息的文字訊息範例_

<!-- tab start `json` -->

```json
{
    "type": "text",
    "text": "Yes, you can.",
    "quoteToken": "yHAz4Ua2wx7..."
}
```

<!-- tab end -->

### Text message (v2) 

與 [text message](https://developers.line.biz/en/reference/messaging-api/#text-message) 不同，text message (v2) 可以將以 `{` 和 `}` 括住的字串替換為 mention 與 emoji。

<!-- parameter start (props: required) -->

type

String

`textV2`

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

訊息文字。

你可以使用 `substitution` 屬性，將以 `{` 和 `}` 括住的字串替換為 mention 或 emoji。如果你想將 `{` 和 `}` 作為字串使用，請以 `{{` 和 `}}` 進行跳脫（escape）。此外，使用 `{` 和 `}` 時請注意下列事項：

- `{` 和 `}` 必須成對使用。
- 以 `{` 和 `}` 括住的字串的替換內容必須使用 `substitution` 屬性指定。

字元數上限：5000

<!-- parameter end -->
<!-- parameter start (props: optional) -->

substitution

Object

一個物件，用來指定 `text` 屬性中以 `{` 和 `}` 括住部分的替換內容。

可用於物件鍵（key）的字元為半形英數字元（`0-9a-zA-Z`）與底線（`_`）。此外，鍵的最大長度為 20 個字元。

你可以為物件值指定 [mention objects](https://developers.line.biz/en/reference/messaging-api/#text-message-v2-mention-object) 或 [emoji objects](https://developers.line.biz/en/reference/messaging-api/#text-message-v2-emoji-object)。

物件數量上限：100

<!-- parameter end -->
<!-- parameter start (props: optional) -->

quoteToken

String

你想引用的訊息的 quote token。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->

_含有 mention 與 emoji 的 text message (v2) 範例_

<!-- tab start `json` -->

```json
{
  "type": "textV2",
  "text": "Welcome, {user1}! {laugh}\n{everyone} There is a newcomer!",
  "substitution": {
    "user1": {
      "type": "mention",
      "mentionee": {
        "type": "user",
        "userId": "U49585cd0d5..."
      }
    },
    "laugh": {
      "type": "emoji",
      "productId": "5a8555cfe6256cc92ea23c2a",
      "emojiId": "002"
    },
    "everyone": {
      "type": "mention",
      "mentionee": {
        "type": "all"
      }
    }
  }
}
```

<!-- tab end -->

#### Mention object 

指定要在文字中替換的 mention 內容。使用 mention objects 時請注意下列事項：

1. Mention objects 只能用於 [reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message) 或 [push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message)。
1. 訊息的目的地必須是 [群組聊天室](https://developers.line.biz/en/docs/messaging-api/group-chats/#group) 或 [多人聊天室](https://developers.line.biz/en/docs/messaging-api/group-chats/#room)。
1. 傳送訊息的 LINE 官方帳號必須是該訊息所要傳送至的群組聊天室或多人聊天室的成員。
1. 所有被提及的使用者都必須是該訊息所要傳送至的群組聊天室或多人聊天室的成員。
1. 單一訊息中最多可替換 20 個 mention。

上述第 2 至 4 點無法透過 [Validate message objects of a reply message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-reply-message) 或 [Validate message objects of a push message](https://developers.line.biz/en/reference/messaging-api/#validate-message-objects-of-push-message) 端點進行驗證。

<!-- parameter start (props: required) -->

type

String

`mention`

<!-- parameter end -->
<!-- parameter start (props: required) -->

mentionee

Object

要提及的物件。指定 [user object](https://developers.line.biz/en/reference/messaging-api/#text-message-v2-mentionee-user) 或 [all-mention object](https://developers.line.biz/en/reference/messaging-api/#text-message-v2-mentionee-all) 其中之一。

<!-- parameter end -->

##### User object 

<!-- parameter start (props: required) -->

type

String

`user`

<!-- parameter end -->
<!-- parameter start (props: required) -->

userId

String

要提及的使用者的 user ID。你無法指定 LINE Bot 的 user ID。

<!-- parameter end -->

##### All-mention object 

<!-- parameter start (props: required) -->

type

String

`all`

<!-- parameter end -->

#### Emoji object 

指定要在文字中替換的 emoji 內容。單一訊息中最多可替換 20 個 emoji。

<!-- parameter start (props: required) -->

type

String

`emoji`

<!-- parameter end -->
<!-- parameter start (props: required) -->

productId

String

一組 LINE emoji 的 Product ID。如需更多 product ID 的相關資訊，請參閱 Messaging API 文件中的 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

emojiId

String

Emoji ID。如需更多可透過 Messaging API 傳送的 LINE emoji 的 emoji ID 相關資訊，請參閱 Messaging API 文件中的 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

<!-- parameter end -->

### Sticker message 

<!-- parameter start (props: required) -->

type

String

`sticker`

<!-- parameter end -->
<!-- parameter start (props: required) -->

packageId

String

一組貼圖的 Package ID。如需 package ID 的相關資訊，請參閱 [Stickers](https://developers.line.biz/en/docs/messaging-api/sticker-list/)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

stickerId

String

Sticker ID。如需可透過 Messaging API 傳送的貼圖的 sticker ID 清單，請參閱 [Stickers](https://developers.line.biz/en/docs/messaging-api/sticker-list/)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

quoteToken

String

你想引用的訊息的 quote token。如需更多資訊，請參閱 Messaging API 文件中的 [Get quote tokens](https://developers.line.biz/en/docs/messaging-api/get-quote-tokens/)。

<!-- parameter end -->

_貼圖訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "sticker",
  "packageId": "446",
  "stickerId": "1988"
}
```

<!-- tab end -->

_引用過往訊息的貼圖訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "sticker",
  "packageId": "789",
  "stickerId": "10855",
  "quoteToken": "yHAz4Ua2wx7..."
}
```

<!-- tab end -->

### Image message 

<!-- parameter start (props: required) -->

type

String

`image`

<!-- parameter end -->
<!-- parameter start (props: required) -->

originalContentUrl

String

圖片檔案 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
圖片格式：JPEG 或 PNG\
檔案大小上限：10 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

previewImageUrl

String

預覽圖片 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
圖片格式：JPEG 或 PNG\
檔案大小上限：1 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

視使用者裝置的狀況而定，`originalContentUrl` 屬性的圖片可能會被用作預覽圖片。

<!-- parameter end -->

_圖片訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "image",
  "originalContentUrl": "https://example.com/original.jpg",
  "previewImageUrl": "https://example.com/preview.jpg"
}
```

<!-- tab end -->

### Video message 

<!-- note start -->

**如果影片無法正常播放**

即使含有影片的訊息成功傳送，影片仍可能無法在使用者裝置上正常播放。如需更多資訊，請參閱 FAQ 中的 [Why can't I play a video that I sent as a message?](https://developers.line.biz/en/faq/#why-cant-i-play-a-video-i-sent)。

<!-- note end -->

<!-- note start -->

**影片長寬比**

- 在某些環境中播放時，過寬或過高的影片可能會被裁切。
- `originalContentUrl` 指定的影片與 `previewImageUrl` 指定的預覽圖片的長寬比應相同。如果長寬比不同，預覽圖片會出現在影片後方。

![LINE 聊天室中的影片訊息。長寬比為 1:1 的預覽圖片顯示在長寬比為 16:9 的影片後方。](https://developers.line.biz/media/messaging-api/messages/image-overlapping-en.png)

<!-- note end -->

<!-- parameter start (props: required) -->

type

String

`video`

<!-- parameter end -->
<!-- parameter start (props: required) -->

originalContentUrl

String

影片檔案 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
影片格式：mp4\
檔案大小上限：200 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

previewImageUrl

String

預覽圖片 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
圖片格式：JPEG 或 PNG\
檔案大小上限：1 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

trackingId

String

當 [Video viewing complete event](https://developers.line.biz/en/reference/messaging-api/#video-viewing-complete) 發生時用來辨識影片的 ID。如果你傳送加上 `trackingId` 的影片訊息，當使用者看完影片時就會發生 video viewing complete event。

你可以在多個訊息中使用相同的 ID。

- 字元數上限：100
- 支援的字元類型：半形英數字元（`a-z`、`A-Z`、`0-9`）與符號（`-.=,+*()%$&;:@{}!?<>[]`）

<!-- note start -->

**Note**

你無法在傳送至群組聊天室或多人聊天室的訊息中使用 `trackingId` 屬性。

<!-- note end -->

<!-- parameter end -->

_影片訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "video",
  "originalContentUrl": "https://example.com/original.mp4",
  "previewImageUrl": "https://example.com/preview.jpg",
  "trackingId": "track-id"
}
```

<!-- tab end -->

### Audio message 

<!-- parameter start (props: required) -->

type

String

`audio`

<!-- parameter end -->
<!-- parameter start (props: required) -->

originalContentUrl

String

音訊檔案 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
音訊格式：mp3 或 m4a\
檔案大小上限：200 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

duration

Number

音訊檔案的長度（毫秒）

<!-- parameter end -->

_音訊訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "audio",
  "originalContentUrl": "https://example.com/original.m4a",
  "duration": 60000
}
```

<!-- tab end -->

### Location message 

<!-- parameter start (props: required) -->

type

String

`location`

<!-- parameter end -->
<!-- parameter start (props: required) -->

title

String

標題\
字元數上限：100

<!-- parameter end -->
<!-- parameter start (props: required) -->

address

String

地址\
字元數上限：100

<!-- parameter end -->
<!-- parameter start (props: required) -->

latitude

Decimal

緯度

<!-- parameter end -->
<!-- parameter start (props: required) -->

longitude

Decimal

經度

<!-- parameter end -->

_位置訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "location",
  "title": "my location",
  "address": "1-3 Kioicho, Chiyoda-ku, Tokyo, 102-8282, Japan",
  "latitude": 35.67966,
  "longitude": 139.73669
}
```

<!-- tab end -->

### Coupon message 

Coupon message 是透過指定 coupon ID 將優惠券傳送給使用者的訊息。

<!-- parameter start (props: required) -->

type

String

`coupon`

<!-- parameter end -->
<!-- parameter start (props: required) -->

couponId

String

Coupon ID。\
你可以在 [建立優惠券](https://developers.line.biz/en/reference/messaging-api/#create-coupon) 時的 [回應](https://developers.line.biz/en/reference/messaging-api/#create-coupon-response) 中取得 coupon ID（`couponId`）。你也可以在 [取得優惠券清單](https://developers.line.biz/en/reference/messaging-api/#get-coupons-list) 的端點中查看 coupon ID。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

deliveryTag

String

優惠券顯示路徑的名稱。\
字元數上限：30\
支援的字元類型：半形英數字元（`a-z`、`A-Z`、`0-9`）與底線（`_`）

如果你未指定 `deliveryTag`，路徑會顯示為 `Unknown`。如需更多資訊，請參閱 LINE for Business 中的 [Insight - Coupons](https://www.lycbiz.com/jp/manual/OfficialAccountManager/insight_coupon/)（僅提供日文版）。

<!-- parameter end -->

_優惠券訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "coupon",
  "couponId": "01JYNW8JMQVFBNWF1APF8Z3FS7",
  "deliveryTag": "2025_winter_campaign"
}
```

<!-- tab end -->

### Imagemap message 

Imagemap message 是由一張具有多個可點選區域的圖片所構成的訊息。你可以為整張圖片指定一個可點選區域，或是在圖片的不同分割區域上設定不同的可點選區域。

你也可以在圖片上播放影片，並在影片結束後顯示一個帶有超連結的標籤。

<!-- note start -->

**如果影片無法正常播放**

即使含有影片的訊息成功傳送，影片仍可能無法在使用者裝置上正常播放。如需更多資訊，請參閱 FAQ 中的 [Why can't I play a video that I sent as a message?](https://developers.line.biz/en/faq/#why-cant-i-play-a-video-i-sent)。

<!-- note end -->

<!-- note start -->

**影片長寬比**

`originalContentUrl` 指定的影片與 `previewImageUrl` 指定的預覽圖片的長寬比應相同。如果長寬比不同，預覽圖片會出現在影片後方。

![LINE 聊天室中的影片訊息。長寬比為 1:1 的預覽圖片顯示在長寬比為 16:9 的影片後方。](https://developers.line.biz/media/messaging-api/messages/image-overlapping-en.png)

<!-- note end -->

<!-- parameter start (props: required) -->

type

String

`imagemap`

<!-- parameter end -->
<!-- parameter start (props: required) -->

baseUrl

String

圖片基礎 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
如需更多關於 imagemap message 中支援圖片的相關資訊，請參閱 [How to configure an image](https://developers.line.biz/en/reference/messaging-api/#base-url)。

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

altText

String

替代文字。當使用者收到訊息時，它會在裝置的通知或聊天清單中作為圖片的替代而顯示。\
你可以包含 Unicode emoji。\
字元數上限：1500

<!-- parameter end -->
<!-- parameter start (props: required) -->

baseSize.width

Number

基礎圖片的寬度（像素）。設為 1040。

<!-- parameter end -->
<!-- parameter start (props: required) -->

baseSize.height

Number

基礎圖片的高度。設為對應寬度 1040 像素的高度。

<!-- parameter end -->
<!-- parameter start (props: annotation="*1") -->

video.originalContentUrl

String

影片檔案 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
影片格式：mp4\
檔案大小上限：200 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- note start -->

**Note**

在某些環境中播放時，過寬或過高的影片可能會被裁切。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: annotation="*1") -->

video.previewImageUrl

String

預覽圖片 URL（字元數上限：2000）\
通訊協定：HTTPS（TLS 1.2 以上）\
圖片格式：JPEG 或 PNG\
檔案大小上限：1 MB

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: annotation="*1") -->

video.area.x

Number

影片區域相對於 imagemap 區域左緣的水平位置。值必須為 `0` 或更高。

<!-- parameter end -->
<!-- parameter start (props: annotation="*1") -->

video.area.y

Number

影片區域相對於 imagemap 區域上緣的垂直位置。值必須為 `0` 或更高。

<!-- parameter end -->
<!-- parameter start (props: annotation="*1") -->

video.area.width

Number

影片區域的寬度

<!-- parameter end -->
<!-- parameter start (props: annotation="*1") -->

video.area.height

Number

影片區域的高度

<!-- parameter end -->
<!-- parameter start (props: annotation="*2") -->

video.externalLink.linkUri

String

網頁 URL。當影片後方顯示的標籤被點選時呼叫。\
字元數上限：1000\
可用的 scheme 為 `http`、`https`、`line` 與 `tel`。如需更多關於 LINE URL scheme 的相關資訊，請參閱 [Use LINE features with the LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/)。

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: annotation="*2") -->

video.externalLink.label

String

標籤。在影片結束後顯示。\
字元數上限：30

<!-- parameter end -->
<!-- parameter start (props: required) -->

actions

Array of [imagemap action objects](https://developers.line.biz/en/reference/messaging-api/#imagemap-action-objects)

點選時的動作\
上限：50

<!-- parameter end -->

*1 如果你在 imagemap 上設定要播放影片，則此屬性為必填。\
*2 如果你在 imagemap 上設定要播放影片並在影片結束後顯示標籤，則此屬性為必填。

_含有兩個可點選區域的 imagemap message 範例_

<!-- tab start `json` -->

```json
{
  "type": "imagemap",
  "baseUrl": "https://example.com/bot/images/rm001",
  "altText": "This is an imagemap",
  "baseSize": {
    "width": 1040,
    "height": 1040
  },
  "video": {
    "originalContentUrl": "https://example.com/video.mp4",
    "previewImageUrl": "https://example.com/video_preview.jpg",
    "area": {
      "x": 0,
      "y": 0,
      "width": 1040,
      "height": 585
    },
    "externalLink": {
      "linkUri": "https://example.com/see_more.html",
      "label": "See More"
    }
  },
  "actions": [
    {
      "type": "uri",
      "linkUri": "https://example.com/",
      "area": {
        "x": 0,
        "y": 586,
        "width": 520,
        "height": 454
      }
    },
    {
      "type": "message",
      "text": "Hello",
      "area": {
        "x": 520,
        "y": 586,
        "width": 520,
        "height": 454
      }
    }
  ]
}
```

<!-- tab end -->

#### How to configure an image 

用於 imagemap message 的圖片必須符合下列需求：

- 圖片格式：JPEG 或 PNG
- 圖片寬度：240px、300px、460px、700px、1040px
- 檔案大小上限：10 MB

<!-- tip start -->

**使用透明 PNG**

你可以在 imagemap message 中使用透明 PNG。

<!-- tip end -->

請使圖片可透過 `baseUrl/{image width}` 的 URL 格式以 5 種不同尺寸存取。LINE 之後會根據裝置以適當的解析度下載圖片。

例如，如果我們的基礎 URL 為 `https://example.com/images/cats`，則寬度為 700px 的圖片 URL 會是 `https://example.com/images/cats/700`。為確認所有圖片皆能正常顯示，請存取這些圖片 URL。

| 圖片寬度 | 範例 URL                                    |
| ----------- | ------------------------------------------- |
| 240px       | `https://example.com/bot/images/rm001/240`  |
| 300px       | `https://example.com/bot/images/rm001/300`  |
| 460px       | `https://example.com/bot/images/rm001/460`  |
| 700px       | `https://example.com/bot/images/rm001/700`  |
| 1040px      | `https://example.com/bot/images/rm001/1040` |

<!-- note start -->

**從 URL 中排除圖片副檔名**

請勿在圖片檔名中包含副檔名。如果 URL 含有圖片檔案副檔名（例如 `https://example.com/bot/images/rm001/700.png`），圖片將不會在 imagemap message 中顯示。

<!-- note end -->

#### Imagemap action objects 

指定 imagemap 動作與可點選區域的物件。當某個區域被點選時，會針對每種動作類型觸發下列動作：

- `uri`：使用者會被重新導向至指定的 URI。
- `message`：傳送指定的訊息。
- `clipboard`：將指定的字串複製到使用者裝置的剪貼簿。

##### Imagemap URI action object 

<!-- parameter start (props: required) -->

type

String

`uri`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

label

String

動作的標籤。當用戶端裝置啟用無障礙功能時會被朗讀。\
字元數上限：100

<!-- parameter end -->
<!-- parameter start (props: required) -->

linkUri

String

網頁 URL\
字元數上限：1000\
可用的 scheme 為 `http`、`https`、`line` 與 `tel`。如需更多關於 LINE URL scheme 的相關資訊，請參閱 [Use LINE features with the LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/)。

URL 應使用 UTF-8 進行百分比編碼。如需更多資訊，請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

area

[Imagemap area object](https://developers.line.biz/en/reference/messaging-api/#imagemap-area-object)

定義的可點選區域

<!-- parameter end -->

_Imagemap URI action object 範例_

<!-- tab start `json` -->

```json
{
  "type": "uri",
  "label": "https://example.com/",
  "linkUri": "https://example.com/",
  "area": {
    "x": 0,
    "y": 0,
    "width": 520,
    "height": 1040
  }
}
```

<!-- tab end -->

##### Imagemap message action object 

<!-- parameter start (props: required) -->

type

String

`message`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

label

String

動作的標籤。當用戶端裝置啟用無障礙功能時會被朗讀。\
字元數上限：100

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

要傳送的訊息\
字元數上限：400

<!-- parameter end -->
<!-- parameter start (props: required) -->

area

[Imagemap area object](https://developers.line.biz/en/reference/messaging-api/#imagemap-area-object)

定義的可點選區域

<!-- parameter end -->

_Imagemap message action object 範例_

<!-- tab start `json` -->

```json
{
  "type": "message",
  "label": "hello",
  "text": "hello",
  "area": {
    "x": 520,
    "y": 0,
    "width": 520,
    "height": 1040
  }
}
```

<!-- tab end -->

##### Imagemap clipboard action object 

此功能適用於 iOS 或 Android 的 LINE 版本 `14.0.0` 以上。

<!-- parameter start (props: required) -->

type

String

`clipboard`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

label

String

動作的標籤。當用戶端裝置啟用無障礙功能時會被朗讀。 \
字元數上限：100

<!-- parameter end -->
<!-- parameter start (props: required) -->

clipboardText

String

複製到剪貼簿的文字

- 字元數上限：1000

<!-- parameter end -->
<!-- parameter start (props: required) -->

area

[Imagemap area object](https://developers.line.biz/en/reference/messaging-api/#imagemap-area-object)

定義的可點選區域

<!-- parameter end -->

_Imagemap clipboard action object 範例_

<!-- tab start `json` -->

```json
{
  "type": "clipboard",
  "label": "Copy",
  "clipboardText": "3B48740B",
  "area": {
    "x": 520,
    "y": 0,
    "width": 520,
    "height": 1040
  }
}
```

<!-- tab end -->

###### Imagemap area object 

定義可點選區域的大小。以左上角作為區域的原點。請根據 `baseSize.width` 屬性與 `baseSize.height` 屬性設定這些屬性。

<!-- parameter start (props: required) -->

x

Number

相對於區域左緣的水平位置。值必須為 `0` 或更高。

<!-- parameter end -->
<!-- parameter start (props: required) -->

y

Number

相對於區域上緣的垂直位置。值必須為 `0` 或更高。

<!-- parameter end -->
<!-- parameter start (props: required) -->

width

Number

可點選區域的寬度

<!-- parameter end -->
<!-- parameter start (props: required) -->

height

Number

可點選區域的高度

<!-- parameter end -->

_Imagemap area object 範例_

<!-- tab start `json` -->

```json
{
  "x": 520,
  "y": 0,
  "width": 520,
  "height": 1040
}
```

<!-- tab end -->
### Template messages 

範本訊息（Template messages）是具有預先定義版面配置的訊息，您可以自訂內容。詳情請參閱[範本訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)。

可使用以下範本類型：

- [Buttons](https://developers.line.biz/en/reference/messaging-api/#buttons)
- [Confirm](https://developers.line.biz/en/reference/messaging-api/#confirm)
- [Carousel](https://developers.line.biz/en/reference/messaging-api/#carousel)
- [Image carousel](https://developers.line.biz/en/reference/messaging-api/#image-carousel)

如果您想傳送版面配置更彈性的訊息，請使用 [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)。

#### Common properties of template message objects 

以下屬性（property）為所有範本訊息物件（object）共通。

<!-- parameter start (props: required) -->

type

String

`template`

<!-- parameter end -->
<!-- parameter start (props: required) -->

altText

String

替代文字。當使用者收到訊息時，此文字會顯示在裝置的通知、聊天列表，以及[引用訊息](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-quote-messages)中，作為範本訊息的替代內容。\
您可以加入 Unicode emoji。\
最大字元數限制：1500

<!-- parameter end -->
<!-- parameter start (props: required) -->

template

Object

[Buttons](https://developers.line.biz/en/reference/messaging-api/#buttons)、[Confirm](https://developers.line.biz/en/reference/messaging-api/#confirm)、[Carousel](https://developers.line.biz/en/reference/messaging-api/#carousel) 或 [Image Carousel](https://developers.line.biz/en/reference/messaging-api/#image-carousel) 物件。

<!-- parameter end -->

#### Buttons template 

具有圖片、標題、文字以及多個動作按鈕的範本。

<!-- parameter start (props: required) -->

type

String

`buttons`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

thumbnailImageUrl

String

圖片 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
圖片格式：JPEG 或 PNG\
最大寬度：1024px\
最大檔案大小：10 MB

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- tip start -->

**建議的檔案大小**

為避免訊息顯示延遲，請將個別圖片檔案的大小保持較小（建議 1 MB 以下）。

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageAspectRatio

String

圖片的長寬比。以下其中一種：

- `rectangle`：1.51:1
- `square`：1:1

預設值：`rectangle`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageSize

String

圖片的大小。以下其中一種：

- `cover`：圖片填滿整個圖片區域。未能容納於區域內的圖片部分不會顯示。
- `contain`：整張圖片顯示於圖片區域中。在直式圖片的左右兩側未使用區域，以及橫式圖片的上下方區域會顯示背景。

預設值：`cover`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageBackgroundColor

String

圖片的背景顏色。請指定 RGB 顏色值。預設值：`#FFFFFF`（白色）

<!-- parameter end -->
<!-- parameter start (props: optional) -->

title

String

標題\
最大字元數限制：40

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

訊息文字\
最大字元數限制：160（無圖片或標題時）\
最大字元數限制：60（含圖片或標題的訊息）

<!-- parameter end -->
<!-- parameter start (props: optional) -->

defaultAction

[Action object](https://developers.line.biz/en/reference/messaging-api/#action-objects)

點按圖片、標題或文字區域時執行的動作。

<!-- parameter end -->
<!-- parameter start (props: required) -->

actions

Array of [action objects](https://developers.line.biz/en/reference/messaging-api/#action-objects)

點按時執行的動作\
最大物件數：4

<!-- parameter end -->

_Buttons 範本訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "template",
  "altText": "This is a buttons template",
  "template": {
    "type": "buttons",
    "thumbnailImageUrl": "https://example.com/bot/images/image.jpg",
    "imageAspectRatio": "rectangle",
    "imageSize": "cover",
    "imageBackgroundColor": "#FFFFFF",
    "title": "Menu",
    "text": "Please select",
    "defaultAction": {
      "type": "uri",
      "label": "View detail",
      "uri": "http://example.com/page/123"
    },
    "actions": [
      {
        "type": "postback",
        "label": "Buy",
        "data": "action=buy&itemid=123"
      },
      {
        "type": "postback",
        "label": "Add to cart",
        "data": "action=add&itemid=123"
      },
      {
        "type": "uri",
        "label": "View detail",
        "uri": "http://example.com/page/123"
      }
    ]
  }
}
```

<!-- tab end -->

#### Confirm template 

具有兩個動作按鈕的範本。

<!-- parameter start (props: required) -->

type

String

`confirm`

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

訊息文字\
最大字元數限制：240

<!-- parameter end -->
<!-- parameter start (props: required) -->

actions

Array of [action objects](https://developers.line.biz/en/reference/messaging-api/#action-objects)

點按時執行的動作\
為這 2 個按鈕設定 2 個動作

<!-- parameter end -->

_Confirm 範本訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "template",
  "altText": "this is a confirm template",
  "template": {
    "type": "confirm",
    "text": "Are you sure?",
    "actions": [
      {
        "type": "message",
        "label": "Yes",
        "text": "yes"
      },
      {
        "type": "message",
        "label": "No",
        "text": "no"
      }
    ]
  }
}
```

<!-- tab end -->

#### Carousel template 

具有多個欄位的範本，可像旋轉木馬（carousel）一樣輪播。水平捲動時欄位會依序顯示。

<!-- parameter start (props: required) -->

type

String

`carousel`

<!-- parameter end -->
<!-- parameter start (props: required) -->

columns

Array of [column objects](https://developers.line.biz/en/reference/messaging-api/#column-object-for-carousel)

欄位陣列（array）\
最大欄位數：10

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageAspectRatio

String

圖片的長寬比。以下其中一種：

- `rectangle`：1.51:1
- `square`：1:1

適用於所有欄位。預設值：`rectangle`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageSize

String

圖片的大小。以下其中一種：

- `cover`：圖片填滿整個圖片區域。未能容納於區域內的圖片部分不會顯示。
- `contain`：整張圖片顯示於圖片區域中。在直式圖片的左右兩側未使用區域，以及橫式圖片的上下方區域會顯示背景。

適用於所有欄位。預設值：`cover`。

<!-- parameter end -->

_Carousel 範本訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "template",
  "altText": "this is a carousel template",
  "template": {
    "type": "carousel",
    "columns": [
      {
        "thumbnailImageUrl": "https://example.com/bot/images/item1.jpg",
        "imageBackgroundColor": "#FFFFFF",
        "title": "this is menu",
        "text": "description",
        "defaultAction": {
          "type": "uri",
          "label": "View detail",
          "uri": "http://example.com/page/123"
        },
        "actions": [
          {
            "type": "postback",
            "label": "Buy",
            "data": "action=buy&itemid=111"
          },
          {
            "type": "postback",
            "label": "Add to cart",
            "data": "action=add&itemid=111"
          },
          {
            "type": "uri",
            "label": "View detail",
            "uri": "http://example.com/page/111"
          }
        ]
      },
      {
        "thumbnailImageUrl": "https://example.com/bot/images/item2.jpg",
        "imageBackgroundColor": "#000000",
        "title": "this is menu",
        "text": "description",
        "defaultAction": {
          "type": "uri",
          "label": "View detail",
          "uri": "http://example.com/page/222"
        },
        "actions": [
          {
            "type": "postback",
            "label": "Buy",
            "data": "action=buy&itemid=222"
          },
          {
            "type": "postback",
            "label": "Add to cart",
            "data": "action=add&itemid=222"
          },
          {
            "type": "uri",
            "label": "View detail",
            "uri": "http://example.com/page/222"
          }
        ]
      }
    ],
    "imageAspectRatio": "rectangle",
    "imageSize": "cover"
  }
}
```

<!-- tab end -->

##### Column object for carousel 

<!-- parameter start (props: optional) -->

thumbnailImageUrl

String

圖片 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
圖片格式：JPEG 或 PNG\
長寬比：1.51:1（寬 : 高）\
最大寬度：1024px\
最大檔案大小：10 MB

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- tip start -->

**建議的檔案大小**

為避免訊息顯示延遲，請將個別圖片檔案的大小保持較小（建議 1 MB 以下）。

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

imageBackgroundColor

String

圖片的背景顏色。請指定 RGB 顏色值。預設值為 `#FFFFFF`（白色）。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

title

String

標題\
最大字元數限制：40

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

訊息文字\
最大字元數限制：120（無圖片或標題時）\
最大字元數限制：60（含圖片或標題的訊息）

<!-- parameter end -->
<!-- parameter start (props: optional) -->

defaultAction

[Action object](https://developers.line.biz/en/reference/messaging-api/#action-objects)

點按圖片、標題或文字區域時執行的動作。

<!-- parameter end -->
<!-- parameter start (props: required) -->

actions

Array of [action objects](https://developers.line.biz/en/reference/messaging-api/#action-objects)

點按時執行的動作\
最大物件數：3

<!-- parameter end -->

<!-- note start -->

**Note**

請讓所有欄位的動作數量保持一致。如果某個欄位使用了圖片或標題，請確保所有其他欄位也比照辦理。

<!-- note end -->

#### Image carousel template 

具有多張圖片的範本，可像旋轉木馬（carousel）一樣輪播。水平捲動時圖片會依序顯示。

<!-- parameter start (props: required) -->

type

String

`image_carousel`

<!-- parameter end -->
<!-- parameter start (props: required) -->

columns

Array of [column objects](https://developers.line.biz/en/reference/messaging-api/#column-object-for-image-carousel)

欄位陣列（array）\
最大欄位數：10

<!-- parameter end -->

_Image carousel 範本訊息範例_

<!-- tab start `json` -->

```json
{
  "type": "template",
  "altText": "this is a image carousel template",
  "template": {
    "type": "image_carousel",
    "columns": [
      {
        "imageUrl": "https://example.com/bot/images/item1.jpg",
        "action": {
          "type": "postback",
          "label": "Buy",
          "data": "action=buy&itemid=111"
        }
      },
      {
        "imageUrl": "https://example.com/bot/images/item2.jpg",
        "action": {
          "type": "message",
          "label": "Yes",
          "text": "yes"
        }
      },
      {
        "imageUrl": "https://example.com/bot/images/item3.jpg",
        "action": {
          "type": "uri",
          "label": "View detail",
          "uri": "http://example.com/page/222"
        }
      }
    ]
  }
}
```

<!-- tab end -->

##### Column object for image carousel 

<!-- parameter start (props: required) -->

imageUrl

String

圖片 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
圖片格式：JPEG 或 PNG\
長寬比：1:1（寬 : 高）\
最大寬度：1024px\
最大檔案大小：10 MB

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- tip start -->

**建議的檔案大小**

為避免訊息顯示延遲，請將個別圖片檔案的大小保持較小（建議 1 MB 以下）。

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start (props: required) -->

action

[Action object](https://developers.line.biz/en/reference/messaging-api/#action-objects)

點按圖片時執行的動作

<!-- parameter end -->

### Flex Message 

Flex Message 是具有可自訂版面配置的訊息。您可以依據 [CSS Flexible Box（CSS Flexbox）](https://www.w3.org/TR/css-flexbox-1/)的規格自由自訂版面配置。詳情請參閱 Messaging API 文件中的[傳送 Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)。

- [Container](https://developers.line.biz/en/reference/messaging-api/#container)
  - [Bubble](https://developers.line.biz/en/reference/messaging-api/#bubble)
  - [Carousel](https://developers.line.biz/en/reference/messaging-api/#f-carousel)
- [Component](https://developers.line.biz/en/reference/messaging-api/#flex-component)
  - [Box](https://developers.line.biz/en/reference/messaging-api/#box)
  - [Button](https://developers.line.biz/en/reference/messaging-api/#button)
  - [Image](https://developers.line.biz/en/reference/messaging-api/#f-image)
  - [Video](https://developers.line.biz/en/reference/messaging-api/#f-video)
  - [Icon](https://developers.line.biz/en/reference/messaging-api/#icon)
  - [Text](https://developers.line.biz/en/reference/messaging-api/#f-text)
  - [Span](https://developers.line.biz/en/reference/messaging-api/#span)
  - [Separator](https://developers.line.biz/en/reference/messaging-api/#separator)
  - [Filler](https://developers.line.biz/en/reference/messaging-api/#filler)（已棄用）

<!-- parameter start (props: required) -->

type

String

`flex`

<!-- parameter end -->
<!-- parameter start (props: required) -->

altText

String

替代文字。當使用者收到訊息時，此文字會顯示在裝置的通知、對話列表，以及[引用訊息](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-quote-messages)中，作為 Flex Message 的替代內容。\
您可以加入 Unicode emoji。\
最大字元數限制：1500

<!-- parameter end -->
<!-- parameter start (props: required) -->

contents

Object

Flex Message [容器（container）](https://developers.line.biz/en/reference/messaging-api/#container)

<!-- parameter end -->

_Flex Message 範例_

<!-- tab start `json` -->

```json
{
  "type": "flex",
  "altText": "this is a flex message",
  "contents": {
    "type": "bubble",
    "body": {
      "type": "box",
      "layout": "vertical",
      "contents": [
        {
          "type": "text",
          "text": "hello"
        },
        {
          "type": "text",
          "text": "world"
        }
      ]
    }
  }
}
```

<!-- tab end -->

#### Operating environment 

所有 LINE 版本皆支援 Flex Message。但以下列出的功能並非所有 LINE 版本皆支援：

| Feature | LINE for iOS<br>LINE for Android | LINE for PC<br />(macOS, Windows) |
| --- | :-: | :-: |
| <ul><li>[box](https://developers.line.biz/en/reference/messaging-api/#box) 的 `maxWidth` 屬性</li><li>[box](https://developers.line.biz/en/reference/messaging-api/#box) 的 `maxHeight` 屬性</li><li>[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 的 `lineSpacing` 屬性</li><li>[Video](https://developers.line.biz/en/reference/messaging-api/#f-video) \*1</li></ul> | 11.22.0 或以上 | 7.7.0 或以上 |
| <ul><li>[bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 的 `size` 屬性中的 `deca` 與 `hecto` 值 \*2</li><li>[button](https://developers.line.biz/en/reference/messaging-api/#button)、[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 與 [icon](https://developers.line.biz/en/reference/messaging-api/#icon) 的 `scaling` 屬性</li></ul> | 13.6.0 或以上 | 7.17.0 或以上 |

\*1 為了讓 Flex Message 中的影片元件在不支援影片元件的版本上正確呈現，請指定 `altContent` 屬性。屆時會改為顯示您在此屬性中指定的圖片。

\*2 如果 LINE 的版本低於支援 `deca` 與 `hecto` 的版本，bubble 的大小將會以 `kilo` 顯示。

#### Container 

Container 是 Flex Message 的頂層構成元素。可使用的容器類型有：

- [Bubble](https://developers.line.biz/en/reference/messaging-api/#bubble)
- [Carousel](https://developers.line.biz/en/reference/messaging-api/#f-carousel)

關於容器的 JSON 範例與用法，請參閱 API 文件中的 [Flex Message 元素](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)。

##### Bubble 

Bubble 是僅包含一個訊息泡泡的容器。它可以包含四個區塊：header、hero、body 與 footer。關於各區塊的使用方式，請參閱 API 文件中的 [Block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)。

定義 bubble 的 JSON 資料最大大小為 30 KB。

<!-- parameter start (props: required) -->

type

String

`bubble`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

String

bubble 的大小。您可以指定以下其中一個值：`nano`、`micro`、`deca`、`hecto`、`kilo`、`mega` 或 `giga`。預設值為 `mega`。

`deca` 與 `hecto` 在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：13.6.0 或以上
- LINE for macOS 與 Windows：7.17.0 或以上

如果 LINE 的版本低於支援 `deca` 與 `hecto` 的版本，bubble 的大小將會以 `kilo` 顯示。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

direction

String

文字方向性以及水平 box 中元件的放置方向。請指定以下其中一個值：

- `ltr`：文字為從左至右的水平書寫，元件由左至右放置
- `rtl`：文字為從右至左的水平書寫，元件由右至左放置

預設值為 `ltr`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

header

Object

Header 區塊。請指定一個 [Box](https://developers.line.biz/en/reference/messaging-api/#box)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

hero

Object

Hero 區塊。請指定 [box](https://developers.line.biz/en/reference/messaging-api/#box)、[image](https://developers.line.biz/en/reference/messaging-api/#f-image) 或 [video](https://developers.line.biz/en/reference/messaging-api/#f-video)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

body

Object

Body 區塊。請指定一個 [Box](https://developers.line.biz/en/reference/messaging-api/#box)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

footer

Object

Footer 區塊。請指定一個 [Box](https://developers.line.biz/en/reference/messaging-api/#box)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

styles

Object

各區塊的樣式。請指定一個 [bubble 樣式](https://developers.line.biz/en/reference/messaging-api/#bubble-style)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

action

Object

點按此圖片時執行的動作。請指定一個[動作物件（action object）](https://developers.line.biz/en/reference/messaging-api/#action-objects)。

<!-- parameter end -->

_Bubble 範例_

<!-- tab start `json` -->

```json
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Header text"
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://example.com/flex/images/image.jpg"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Body text"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Footer text"
      }
    ]
  },
  "styles": {
    "comment": "See the example of a bubble style object"
  }
}
```

<!-- tab end -->

##### Objects for the block style 

使用以下兩種物件來定義 bubble 中各區塊的樣式。

_bubble 樣式與 block 樣式的範例_

<!-- tab start `json` -->

```json
  "styles": {
    "header": {
      "backgroundColor": "#00ffff"
    },
    "hero": {
      "separator": true,
      "separatorColor": "#000000"
    },
    "footer": {
      "backgroundColor": "#00ffff",
      "separator": true,
      "separatorColor": "#000000"
    }
  }
```

<!-- tab end -->

###### Bubble style 

<!-- parameter start (props: optional) -->

header

Object

Header 區塊。請指定一個 [block 樣式](https://developers.line.biz/en/reference/messaging-api/#block-style)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

hero

Object

Hero 區塊。請指定一個 [block 樣式](https://developers.line.biz/en/reference/messaging-api/#block-style)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

body

Object

Body 區塊。請指定一個 [block 樣式](https://developers.line.biz/en/reference/messaging-api/#block-style)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

footer

Object

Footer 區塊。請指定一個 [block 樣式](https://developers.line.biz/en/reference/messaging-api/#block-style)。

<!-- parameter end -->

###### Block style 

<!-- parameter start (props: optional) -->

backgroundColor

String

區塊的背景顏色。請使用十六進位顏色碼。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

separator

Boolean

設為 `true` 時，會在區塊上方放置一條分隔線。預設值為 `false`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

separatorColor

String

分隔線的顏色。請使用十六進位顏色碼。

<!-- parameter end -->

<!-- note start -->

**Note**

您無法在第一個區塊上方放置分隔線。

<!-- note end -->

##### Carousel 

Carousel 是包含多個 bubble 的容器。您可以左右捲動來瀏覽 carousel 中的 bubble。

定義 carousel 的 JSON 資料最大大小為 50 KB。

<!-- parameter start (props: required) -->

type

String

`carousel`

<!-- parameter end -->
<!-- parameter start (props: required) -->

contents

Array of objects

carousel 中的 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble)。最多：12 個 bubble

<!-- parameter end -->

<!-- note start -->

**Bubble 的寬度**

carousel 不能包含寬度（`size` 屬性）不同的 bubble。carousel 中的每個 bubble 應具有相同的寬度。

<!-- note end -->

<!-- tip start -->

**Bubble 的高度**

每個 bubble 的 body 會延展以對齊 carousel 中最高的 bubble。但沒有 body 的 bubble 高度不會改變。

<!-- tip end -->

_Carousel 範例_

<!-- tab start `json` -->

```json
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "First bubble"
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "Second bubble"
          }
        ]
      }
    }
  ]
}
```

<!-- tab end -->

#### Component 

Component 是構成區塊的單位。可使用的元件有：

- [Box](https://developers.line.biz/en/reference/messaging-api/#box)
- [Button](https://developers.line.biz/en/reference/messaging-api/#button)
- [Image](https://developers.line.biz/en/reference/messaging-api/#f-image)
- [Video](https://developers.line.biz/en/reference/messaging-api/#f-video)
- [Icon](https://developers.line.biz/en/reference/messaging-api/#icon)
- [Text](https://developers.line.biz/en/reference/messaging-api/#f-text)
- [Span](https://developers.line.biz/en/reference/messaging-api/#span)
- [Separator](https://developers.line.biz/en/reference/messaging-api/#separator)
- [Filler](https://developers.line.biz/en/reference/messaging-api/#filler)（已棄用）

關於各元件的 JSON 範例與用法，請參閱 Messaging API 文件中的 [Flex Message 元素](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)與 [Flex Message 版面配置](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)。

##### Box 

此元件定義水平或垂直的版面配置方向，並將多個元件集合在一起。任何元件都可以被包含在內，包括 box 本身。您也可以在 box 中包含 box。

<!-- parameter start (props: required) -->

type

String

`box`

<!-- parameter end -->
<!-- parameter start (props: required) -->

layout

String

此 box 中元件的版面配置樣式。詳情請參閱 API 文件中的 [Box 元件方向](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-component-orientation)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

contents

Array of objects

此 box 中的元件。可使用的元件類型如下：

- 當 `layout` 屬性為 `horizontal` 或 `vertical` 時：[box](https://developers.line.biz/en/reference/messaging-api/#box)、[button](https://developers.line.biz/en/reference/messaging-api/#button)、[image](https://developers.line.biz/en/reference/messaging-api/#f-image)、[text](https://developers.line.biz/en/reference/messaging-api/#f-text)、[separator](https://developers.line.biz/en/reference/messaging-api/#separator) 與 [filler](https://developers.line.biz/en/reference/messaging-api/#filler)
- 當 `layout` 屬性為 `baseline` 時：[icon](https://developers.line.biz/en/reference/messaging-api/#icon)、[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 與 [filler](https://developers.line.biz/en/reference/messaging-api/#filler)

元件會依照陣列中指定的相同順序呈現。您也可以指定一個空陣列。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

backgroundColor

String

區塊的背景顏色。除了 RGB 顏色外，也可以設定 alpha 通道（透明度）。請使用十六進位顏色碼（例如 #RRGGBBAA）。預設值為 `#00000000`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

borderColor

String

box 邊框的顏色。請使用十六進位顏色碼。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

borderWidth

String

box 邊框的寬度。您可以指定以像素為單位的值，或是 `none`、`light`、`normal`、`medium`、`semi-bold` 或 `bold` 其中一種。`none` 表示不繪製邊框；其他的值依寬度遞增順序列出。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

cornerRadius

String

邊框圓角化時的半徑。您可以指定以像素為單位的值，或是 `none`、`xs`、`sm`、`md`、`lg`、`xl` 或 `xxl` 其中一種。`none` 不會將角圓角化，其他的值則依列出順序遞增半徑。預設值為 `none`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

width

String

box 的寬度。其值應以像素為單位或以父元素寬度的百分比指定。詳情請參閱 Messaging API 文件中的 [Box 寬度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-width)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

maxWidth

String

box 的最大寬度。其值應以像素為單位或以父元素寬度的百分比指定。詳情請參閱 Messaging API 文件中的 [Box 的最大寬度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-width)。

此屬性在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：11.22.0 或以上
- LINE for macOS 與 Windows：7.7.0 或以上

<!-- parameter end -->
<!-- parameter start (props: optional) -->

height

String

box 的高度。其值應以像素為單位或以父元素高度的百分比指定。詳情請參閱 Messaging API 文件中的 [Box 高度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-height)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

maxHeight

String

box 的最大高度。其值應以像素為單位或以父元素高度的百分比指定。詳情請參閱 Messaging API 文件中的 [Box 的最大高度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-height)。

此屬性在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：11.22.0 或以上
- LINE for macOS 與 Windows：7.7.0 或以上

<!-- parameter end -->
<!-- parameter start (props: optional) -->

flex

Number

此元件的寬度或高度在父 box 中所占的比例。詳情請參閱 Messaging API 文件中的[元件大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

spacing

String

此 box 中各元件之間的最小間距。預設值為 `none`。詳情請參閱 Messaging API 文件中的 [box 的 `spacing` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#spacing-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

margin

String

在父容器中放置此元件之前要包含的最小空間量。詳情請參閱 Messaging API 文件中的[元件的 `margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

paddingAll

String

此 box 邊框與子元素之間的留白空間。詳情請參閱 Messaging API 文件中的[以 box padding 定位子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

paddingTop

String

此 box 上端邊框與子元素上端之間的留白空間。詳情請參閱 Messaging API 文件中的[以 box padding 定位子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

paddingBottom

String

此 box 下端邊框與子元素下端之間的留白空間。詳情請參閱 Messaging API 文件中的[以 box padding 定位子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

paddingStart

String

- 如果 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 中的文字方向性為 LTR：此 box 左端邊框與子元素左端之間的留白空間。
- 如果 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 中的文字方向性為 RTL：此 box 右端邊框與子元素右端之間的留白空間。

詳情請參閱 Messaging API 文件中的[以 box padding 定位子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

paddingEnd

String

- 如果 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 中的文字方向性為 LTR：此 box 右端邊框與子元素右端之間的留白空間。
- 如果 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 中的文字方向性為 RTL：此 box 左端邊框與子元素左端之間的留白空間。

詳情請參閱 Messaging API 文件中的[以 box padding 定位子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

position

String

放置此 box 的參考位置。請指定以下其中一個值：

- `relative`：以前一個 box 作為參考。
- `absolute`：以父元素的左上角作為參考。

預設值為 `relative`。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetTop

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetBottom

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetStart

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetEnd

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

action

Object

點按此圖片時執行的動作。請指定一個[動作物件（action object）](https://developers.line.biz/en/reference/messaging-api/#action-objects)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

justifyContent

String

子元素如何沿父元素的主軸對齊。如果父元素是水平 box，則僅在其子元素的 `flex` 屬性設為 0 時才生效。詳情請參閱 Messaging API 文件中的[利用留白空間排列子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#justify-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

alignItems

String

子元素如何沿父元素的交叉軸對齊。詳情請參閱 Messaging API 文件中的[利用留白空間排列子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#justify-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

background.type

String

使用的背景類型。請指定以下這些值：

- `linearGradient`：線性漸層。詳情請參閱 Messaging API 文件中的[線性漸層背景](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#linear-gradient-bg)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

background.angle

String

線性漸層移動的角度。請使用整數值如 `90deg`（90 度）或小數如 `23.5deg`（23.5 度），於半開區間 [0, 360) 內指定角度。線性漸層的方向會隨著角度增加而順時針旋轉。當值為 `0deg` 時，漸層從底部開始、頂部結束；當值為 `45deg` 時，漸層從左下角開始、右上角結束；當值為 `90deg` 時，漸層從左側開始、右側結束；當值為 `180deg` 時，漸層從頂部開始、底部結束。詳情請參閱 Messaging API 文件中的[線性漸層的角度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#linear-gradient-bg-angle)。

當 `background.type` 為 `linearGradient` 時，此為必填。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

background.startColor

String

漸層起點的顏色。請使用 `#RRGGBB` 或 `#RRGGBBAA` 格式的十六進位顏色碼。

當 `background.type` 為 `linearGradient` 時，此為必填。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

background.endColor

String

漸層終點的顏色。請使用 `#RRGGBB` 或 `#RRGGBBAA` 格式的十六進位顏色碼。

當 `background.type` 為 `linearGradient` 時，此為必填。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

background.centerColor

String

漸層中間的顏色。請使用 `#RRGGBB` 或 `#RRGGBBAA` 格式的十六進位顏色碼。指定 `background.centerColor` 屬性的值可建立具有三種顏色的漸層。詳情請參閱 Messaging API 文件中的[線性漸層的中間色停駐點](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#linear-gradient-bg-center-color)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

background.centerPosition

String

中間色停駐點的位置。請指定介於 `0%`（起點）與 `100%`（終點）之間的整數或小數值。預設為 `50%`。詳情請參閱 Messaging API 文件中的[線性漸層的中間色停駐點](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#linear-gradient-bg-center-color)。

<!-- parameter end -->

_Box 範例_

<!-- tab start `json` -->

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "url": "https://example.com/flex/images/image.jpg"
      },
      {
        "type": "separator"
      },
      {
        "type": "text",
        "text": "Text in the box"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "width": "30px",
        "height": "30px",
        "background": {
          "type": "linearGradient",
          "angle": "90deg",
          "startColor": "#FFFF00",
          "endColor": "#0080ff"
        }
      }
    ],
    "height": "400px",
    "justifyContent": "space-evenly",
    "alignItems": "center"
  }
}
```

<!-- tab end -->

##### Button 

此元件呈現一個按鈕。您可以設定當使用者點按按鈕時要執行的[動作](https://developers.line.biz/en/docs/messaging-api/actions/)。

<!-- parameter start (props: required) -->

type

String

`button`

<!-- parameter end -->
<!-- parameter start (props: required) -->

action

Object

點按此按鈕時執行的動作。請指定一個[動作物件（action object）](https://developers.line.biz/en/reference/messaging-api/#action-objects)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

flex

Number

此元件的寬度或高度在父元素中所使用的比例。預設情況下，水平 box 的元件其 `flex` 屬性設為 `1`。預設情況下，垂直 box 的元件其 `flex` 屬性設為 `0`。詳情請參閱 Messaging API 文件中的[元件大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

margin

String

在父容器中放置此元件之前要包含的最小空間量。詳情請參閱 Messaging API 文件中的[元件的 `margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

position

String

`offsetTop`、`offsetBottom`、`offsetStart` 與 `offsetEnd` 的參考。請指定以下其中一個值：

- `relative`：以前一個 box 作為參考。
- `absolute`：以父元素的左上角作為參考。

預設值為 `relative`。詳情請參閱 API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetTop

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetBottom

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetStart

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetEnd

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

height

String

按鈕的高度。您可以指定 `sm` 或 `md`。預設值為 `md`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

style

String

按鈕的樣式。請指定以下其中一個值：

- `primary`：深色按鈕的樣式
- `secondary`：淺色按鈕的樣式
- `link`：HTML 連結樣式

預設值為 `link`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

color

String

當 `style` 屬性為 `link` 時為文字顏色。當 `style` 屬性為 `primary` 或 `secondary` 時為背景顏色。請使用十六進位顏色碼。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

gravity

String

垂直方向的對齊樣式。詳情請參閱 Messaging API 文件中的[垂直對齊文字、圖片或按鈕](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#gravity-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

adjustMode

String

調整文字字型大小的方法。請指定此值：

- `shrink-to-fit`：自動縮小字型大小以符合元件寬度。此屬性採取「盡力而為（best-effort）」的方式，在某些平台上可能運作方式不同——或完全不運作！詳情請參閱 Messaging API 文件中的[自動縮小字型以符合](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#adjusts-fontsize-to-fit)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

scaling

Boolean

如果您將 `scaling` 屬性設為 `true`，文字的字型大小將會根據 LINE app 的字型大小設定自動縮放。預設值為 `false`。詳情請參閱 Messaging API 文件中的[根據字型大小設定縮放尺寸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#size-scaling)。

此屬性在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：13.6.0 或以上
- LINE for macOS 與 Windows：7.17.0 或以上

<!-- parameter end -->

_Button 範例_

<!-- tab start `json` -->

```json
{
  "type": "button",
  "action": {
    "type": "uri",
    "label": "Tap me",
    "uri": "https://example.com"
  },
  "style": "primary",
  "color": "#0000ff"
}
```

<!-- tab end -->

##### Image 

此元件呈現一張圖片。

<!-- parameter start (props: required) -->

type

String

`image`

<!-- parameter end -->
<!-- parameter start (props: required) -->

url

String

圖片 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
圖片格式：JPEG 或 PNG\
最大圖片尺寸：1024 x 1024 像素\
最大檔案大小：10 MB（當 `animated` 屬性為 `true` 時為 300 KB）

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- tip start -->

**建議的檔案大小**

為避免訊息顯示延遲，請將個別圖片檔案的大小保持較小（建議 1 MB 以下）。

<!-- tip end -->

<!-- parameter end -->
<!-- parameter start (props: optional) -->

flex

Number

此元件的寬度或高度在父 box 中所占的比例。詳情請參閱 Messaging API 文件中的[元件大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

margin

String

在父容器中放置此元件之前要包含的最小空間量。詳情請參閱 Messaging API 文件中的[元件的 `margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

position

String

`offsetTop`、`offsetBottom`、`offsetStart` 與 `offsetEnd` 的參考。請指定以下其中一個值：

- `relative`：以前一個 box 作為參考。
- `absolute`：以父元素的左上角作為參考。

預設值為 `relative`。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetTop

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetBottom

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetStart

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetEnd

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

align

String

水平方向的對齊樣式。詳情請參閱 Messaging API 文件中的[水平對齊文字或圖片](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#align-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

gravity

String

垂直方向的對齊樣式。詳情請參閱 Messaging API 文件中的[垂直方向的對齊](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#gravity-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

String

圖片的最大寬度。預設為 `md`。詳情請參閱 Messaging API 文件中的[圖片大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#image-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

aspectRatio

String

圖片的長寬比。`{width}:{height}` 格式。請於 1 至 100000 的範圍內指定 `{width}` 與 `{height}` 的值。但是，您不能將 `{height}` 設為超過 `{width}` 值三倍的值。預設值為 `1:1`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

aspectMode

String

當圖片的長寬比與 `aspectRatio` 屬性指定的長寬比不符時，圖片的顯示樣式。詳情請參閱[關於繪圖區域](https://developers.line.biz/en/reference/messaging-api/#drawing-area)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

backgroundColor

String

圖片的背景顏色。請使用十六進位顏色碼。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

action

Object

點按此圖片時執行的動作。請指定一個[動作物件（action object）](https://developers.line.biz/en/reference/messaging-api/#action-objects)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

animated

Boolean

當此值為 `true` 時，會播放動態圖片（APNG）。在單一訊息中，您最多可以為 10 張圖片指定 `true` 值。您無法傳送超過此限制的訊息。預設為 `false`。大於 300 KB 的動態圖片不會被播放。

<!-- parameter end -->

<!-- tip start -->

**如何建立動態圖片**

使用 APNG 編輯器建立動態圖片。在建立 APNG 檔案時，請參考與建立動態貼圖相關的資訊。詳情請參閱 LINE Creators Market 中動態貼圖的[製作準則](https://creator.line.me/en/guideline/animationsticker/)。

<!-- tip end -->

<!-- note start -->

**如果我的動態圖片無法播放怎麼辦？**

如果圖片有顯示但沒有播放動畫，請檢查以下項目：

- 您是否將 `animated` 屬性的值設為 `true`？
- 圖片檔案大小是否小於或等於 300 KB？

在某些情況下，動畫可能因接收訊息的 LINE app 設定而無法播放。請同時檢查以下項目：

- LINE app 設定中是否啟用了 `Auto-play GIFs`（自動播放 GIF）？

動畫會依據 APNG 中 `acTL` 區塊（chunk）的 `num_plays` 欄位所指定的次數重複播放。您也可以指定值為 0 以無限重複播放動畫。

<!-- note end -->

_Image 範例_

<!-- tab start `json` -->

```json
{
  "type": "image",
  "url": "https://example.com/flex/images/image.jpg",
  "size": "full",
  "aspectRatio": "1.91:1"
}
```

<!-- tab end -->

###### About the drawing area 

以 `size` 屬性指定圖片的最大寬度，並以 `aspectRatio` 屬性指定圖片的長寬比（寬高比）。由 `size` 與 `aspectRatio` 屬性決定的矩形區域稱為**繪圖區域（drawing area）**。圖片會在此繪圖區域中呈現。

- 如果 `flex` 屬性指定的圖片寬度大於由 [`size` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-size)計算出的寬度，則繪圖區域的寬度會縮小至元件的寬度。
- 如果圖片的長寬比與 `aspectRatio` 屬性指定的長寬比不符，圖片會依據 `aspectMode` 屬性顯示。預設值為 `fit`。
  - 如果 `aspectMode` 的值為 `cover`：圖片填滿整個繪圖區域。未能容納於繪圖區域內的圖片部分不會顯示。
  - 如果 `aspectMode` 的值為 `fit`：整張圖片顯示於繪圖區域中。在直式圖片的左右兩側未使用區域，以及橫式圖片的上下方區域會顯示背景。

##### Video 

此元件呈現一段影片。

影片元件在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：11.22.0 或以上
- LINE for macOS 與 Windows：7.7.0 或以上

如果 LINE 的版本低於支援影片的版本，則會顯示指定為 altContent 屬性值的元件。

<!-- note start -->

**如果影片無法正常播放**

即使包含影片的訊息成功傳送，影片在使用者的裝置上也可能無法正常播放。詳情請參閱 FAQ 中的[為什麼我無法播放我以訊息傳送的影片？](https://developers.line.biz/en/faq/#why-cant-i-play-a-video-i-sent)。

<!-- note end -->

<!-- note start -->

**影片的長寬比**

在某些環境中播放時，過寬或過高的影片可能會被裁切。

此外，`url` 屬性中指定的影片長寬比應與以下兩個長寬比相同。如果這些長寬比不同，可能會導致非預期的版面配置：

- `aspectRatio` 屬性指定的長寬比
- `previewUrl` 屬性指定的預覽圖片的長寬比

![一個 LINE 聊天室中的影片。在長寬比為 16:9 的影片後方顯示了一張長寬比為 1:1 的預覽圖片。](https://developers.line.biz/media/messaging-api/messages/image-overlapping-en.png)

<!-- note end -->

<!-- note start -->

**影片元件的使用條件**

要使用影片元件，必須滿足以下條件：

- 影片元件直接指定於 hero [區塊](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)下
- bubble 的 `size` 屬性值指定為 `kilo`、`mega` 或 `giga`
- 該 bubble 不是 carousel 的子元素

<!-- note end -->

<!-- parameter start (props: required) -->

type

String

`video`

<!-- parameter end -->
<!-- parameter start (props: required) -->

url

String

影片檔案 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
影片格式：mp4\
最大檔案大小：200 MB

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

previewUrl

String

預覽圖片 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
圖片格式：JPEG 或 PNG\
最大檔案大小：1 MB

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

altContent

component

替代內容。當使用者裝置使用的 LINE 版本不支援影片元件時，畫面上會顯示替代內容。請指定一個 [box](https://developers.line.biz/en/reference/messaging-api/#box) 或 [image](https://developers.line.biz/en/reference/messaging-api/#f-image)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

aspectRatio

String

影片的長寬比。`{width}:{height}` 格式。請於 1 至 100000 的範圍內指定 `{width}` 與 `{height}` 的值。但是，您不能將 `{height}` 設為超過 `{width}` 值三倍的值。預設值為 `1:1`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

action

Object

[URI 動作](https://developers.line.biz/en/reference/messaging-api/#uri-action)。詳情請參閱 Messaging API 文件中的 [URI 動作](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#uri-action)。

<!-- parameter end -->

_Video 範例_

<!-- tab start `json` -->

```json
{
  "type": "bubble",
  "size": "mega",
  "hero": {
    "type": "video",
    "url": "https://example.com/video.mp4",
    "previewUrl": "https://example.com/video_preview.jpg",
    "altContent": {
      "type": "image",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "url": "https://example.com/image.jpg"
    },
    "aspectRatio": "20:13"
  }
}
```

<!-- tab end -->

##### Icon 

此元件呈現一個用於裝飾相鄰文字的圖示。您只能在 [baseline box](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#baseline-box) 中使用此元件。

<!-- parameter start (props: required) -->

type

String

`icon`

<!-- parameter end -->
<!-- parameter start (props: required) -->

url

String

圖片 URL（最大字元數限制：2000）\
通訊協定：HTTPS（TLS 1.2 或以上）\
圖片格式：JPEG 或 PNG\
最大圖片尺寸：1024 x 1024 像素\
最大檔案大小：1 MB

URL 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱[關於在請求主體屬性中指定的 URL 編碼](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

margin

String

在父容器中放置此元件之前要包含的最小空間量。詳情請參閱 Messaging API 文件中的[元件的 `margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

position

String

`offsetTop`、`offsetBottom`、`offsetStart` 與 `offsetEnd` 的參考。請指定以下其中一個值：

- `relative`：以前一個 box 作為參考。
- `absolute`：以父元素的左上角作為參考。

預設值為 `relative`。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetTop

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetBottom

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetStart

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetEnd

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

String

圖示寬度的最大尺寸。預設為 `md`。詳情請參閱 Messaging API 文件中的 [Icon、text 與 span 的大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#other-component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

scaling

Boolean

如果您將 `scaling` 屬性設為 `true`，圖示大小將會根據 LINE app 的字型大小設定自動縮放。預設值為 `false`。詳情請參閱 Messaging API 文件中的[根據字型大小設定縮放尺寸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#size-scaling)。

此屬性在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：13.6.0 或以上
- LINE for macOS 與 Windows：7.17.0 或以上

<!-- parameter end -->
<!-- parameter start (props: optional) -->

aspectRatio

String

圖示的長寬比。`{width}:{height}` 格式。`{width}` 與 `{height}` 的值必須在 1–100000 的範圍內。`{height}` 不能超過 `{width}` 值的三倍。預設值為 `1:1`。

<!-- parameter end -->

圖示的 `flex` 屬性固定為 `0`。

_Icon 範例_

<!-- tab start `json` -->

```json
{
  "type": "icon",
  "url": "https://example.com/icon/png/caution.png",
  "size": "lg",
  "aspectRatio": "1.91:1"
}
```

<!-- tab end -->

##### Text 

此元件呈現一段文字字串。您可以指定字型顏色、大小與粗細。

<!-- parameter start (props: required) -->

type

String

`text`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

text

String

文字。請務必設定 `text` 屬性或 `contents` 屬性其中之一。如果您設定了 `contents` 屬性，則會忽略 `text`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

contents

Array of objects

[span](https://developers.line.biz/en/reference/messaging-api/#span) 陣列（array）。請務必設定 `text` 屬性或 `contents` 屬性其中之一。如果您設定了 `contents` 屬性，則會忽略 `text`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

adjustMode

String

調整文字字型大小的方法。請指定此值：

- `shrink-to-fit`：自動縮小字型大小以符合元件寬度。此屬性採取「盡力而為（best-effort）」的方式，在某些平台上可能運作方式不同——或完全不運作！詳情請參閱 Messaging API 文件中的[自動縮小字型以符合](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#adjusts-fontsize-to-fit)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

flex

Number

此元件的寬度或高度在父 box 中所占的比例。詳情請參閱 Messaging API 文件中的[元件大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

margin

String

在父容器中放置此元件之前要包含的最小空間量。詳情請參閱 Messaging API 文件中的[元件的 `margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

position

String

`offsetTop`、`offsetBottom`、`offsetStart` 與 `offsetEnd` 的參考。請指定以下其中一個值：

- `relative`：以前一個 box 作為參考。
- `absolute`：以父元素的左上角作為參考。

預設值為 `relative`。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetTop

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetBottom

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetStart

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

offsetEnd

String

Offset。詳情請參閱 Messaging API 文件中的 [Offset](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

String

字型大小。預設為 `md`。詳情請參閱 Messaging API 文件中的 [Icon、text 與 span 的大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#other-component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

scaling

Boolean

如果您將 `scaling` 屬性設為 `true`，文字的字型大小將會根據 LINE app 的字型大小設定自動縮放。預設值為 `false`。詳情請參閱 Messaging API 文件中的[根據字型大小設定縮放尺寸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#size-scaling)。

如果此屬性為 `true`，由 `contents` 屬性設定的 [span](https://developers.line.biz/en/reference/messaging-api/#span) 中的文字字型大小也會自動縮放。

此屬性在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：13.6.0 或以上
- LINE for macOS 與 Windows：7.17.0 或以上

<!-- parameter end -->
<!-- parameter start (props: optional) -->

align

String

水平方向的對齊樣式。詳情請參閱 Messaging API 文件中的[水平對齊文字或圖片](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#align-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

gravity

String

垂直方向的對齊樣式。預設值為 `top`。詳情請參閱 Messaging API 文件中的[垂直方向的對齊](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#gravity-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

wrap

Boolean

設為 `true` 時可換行文字。預設值為 `false`。如果設為 `true`，您可以使用換行字元（`\n`）來開始新的一行。詳情請參閱 Messaging API 文件中的[文字換行](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text-wrap)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

lineSpacing

String

換行文字中的行距。請指定以 px 結尾的正整數或小數。`lineSpacing` 屬性不適用於起始行的上方與最後一行的下方。詳情請參閱 Messaging API 文件中的[增加文字的行距](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text-line-spacing)。

此屬性在以下 LINE 版本上受支援：

- LINE for iOS 與 Android：11.22.0 或以上
- LINE for macOS 與 Windows：7.7.0 或以上

<!-- parameter end -->
<!-- parameter start (props: optional) -->

maxLines

Number

最大行數。如果文字超過指定的行數，最後一行會以省略號（…）結尾。如果設為 `0`，則顯示完整文字。預設值為 `0`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

weight

String

字型粗細。您可以指定以下其中一個值：`regular` 或 `bold`。指定 `bold` 會使字型變粗。預設值為 `regular`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

color

String

字型顏色。請使用十六進位顏色碼。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

action

Object

點按此圖片時執行的動作。請指定一個[動作物件（action object）](https://developers.line.biz/en/reference/messaging-api/#action-objects)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

style

String

文字的樣式。請指定以下這些值之一：

- `normal`：正常
- `italic`：斜體

預設值為 `normal`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

decoration

String

文字的裝飾。請指定以下這些值之一：

- `none`：無裝飾
- `underline`：底線
- `line-through`：刪除線

預設值為 `none`。

<!-- parameter end -->

_Text 範例_

<!-- tab start `json` -->

```json
{
  "type": "text",
  "text": "Hello, World!",
  "size": "xl",
  "weight": "bold",
  "color": "#0000ff"
}
```

<!-- tab end -->

##### Span 

此元件以不同樣式呈現多段文字字串。您可以指定每段文字的顏色、大小、粗細與裝飾。Span 會設定於 [text](https://developers.line.biz/en/reference/messaging-api/#text) 的 `contents` 屬性中。

<!-- parameter start (props: required) -->

type

String

`span`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

text

String

文字。如果父 text 的 `wrap` 屬性設為 `true`，您可以使用換行字元（`\n`）來開始新的一行。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

color

String

字型顏色。請使用十六進位顏色碼。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

size

String

字型大小。詳情請參閱 Messaging API 文件中的 [Icon、text 與 span 的大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#other-component-size)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

weight

String

字型粗細。您可以指定以下其中一個值：`regular` 或 `bold`。指定 `bold` 會使字型變粗。預設值為 `regular`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

style

String

文字的樣式。請指定以下這些值之一：

- `normal`：正常
- `italic`：斜體

預設值為 `normal`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

decoration

String

文字的裝飾。請指定以下這些值之一：

- `none`：無裝飾
- `underline`：底線
- `line-through`：刪除線

預設值為 `none`。

<!-- note start -->

**Note**

[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 的 `decoration` 屬性所設定的裝飾，無法被 span 的 `decoration` 屬性覆寫。

<!-- note end -->

<!-- parameter end -->

_Span 範例_

<!-- tab start `json` -->

```json
{
  "type": "span",
  "text": "蛙",
  "size": "xxl",
  "weight": "bold",
  "style": "italic",
  "color": "#4f8f00"
}
```

<!-- tab end -->

##### Separator 

此元件在 [box](https://developers.line.biz/en/reference/messaging-api/#box) 內呈現一條分隔線。如果包含在水平版面配置的 box 中，會繪製一條垂直線。同樣地，如果包含在垂直版面配置的 box 中，會繪製一條水平線。

<!-- parameter start (props: required) -->

type

String

`separator`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

margin

String

在父容器中放置此元件之前要包含的最小空間量。詳情請參閱 Messaging API 文件中的[元件的 `margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

color

String

分隔線的顏色。請使用十六進位顏色碼。

<!-- parameter end -->

_Separator 範例_

<!-- tab start `json` -->

```json
{
  "type": "separator",
  "color": "#000000"
}
```

<!-- tab end -->

##### Filler 

<!-- warning start -->

**Filler 已棄用**

若要新增空間，請改用各元件的屬性而非新增 filler。詳情請參閱 Messaging API 文件中的[元件位置](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-position)。

<!-- warning end -->

此元件呈現一個空白空間。您可以在 [box](https://developers.line.biz/en/reference/messaging-api/#box) 內的各元件之間、之前或之後放置一個空間。

<!-- parameter start (props: required) -->

type

String

`filler`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

flex

Number

此元件的寬度或高度在父 box 中所占的比例。詳情請參閱 Messaging API 文件中的[元件大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-size)。

<!-- parameter end -->

父元素的 `spacing` 屬性對 filler 會被忽略。

_Filler 範例_

<!-- tab start `json` -->

```json
{
  "type": "filler"
}
```

<!-- tab end -->
## Action objects 

這些是當使用者點擊訊息中的按鈕或圖片時，您的機器人可採取的動作類型。

- [Postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)
- [Message action](https://developers.line.biz/en/reference/messaging-api/#message-action)
- [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)
- [Datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)
- [Camera action](https://developers.line.biz/en/reference/messaging-api/#camera-action)
- [Camera roll action](https://developers.line.biz/en/reference/messaging-api/#camera-roll-action)
- [Location action](https://developers.line.biz/en/reference/messaging-api/#location-action)
- [Richmenu Switch Action](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)
- [Clipboard action](https://developers.line.biz/en/reference/messaging-api/#clipboard-action)

### Postback action 

當與此動作相關聯的控制項被點擊時，會透過 Webhook 回傳一個 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event)，其中包含 `data` 屬性（property）中所指定的字串。

<!-- parameter start (props: required) -->

type

String

`postback`

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

label

String

此動作的標籤。其規格取決於該動作設定在哪一個物件（object）上。詳情請參閱 [Specifications of the label](https://developers.line.biz/en/reference/messaging-api/#action-object-label-spec)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

data

String

透過 Webhook 在 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 的 `postback.data` 屬性中回傳的字串\
最大字元限制：300

<!-- parameter end -->
<!-- parameter start (props: optional) -->

displayText

String

當動作被執行時，顯示在 LINE 聊天畫面上、作為使用者送出之訊息的文字。\
最大字元限制：300\
`displayText` 與 `text` 屬性不可同時使用。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

text

String

【已棄用】當動作被執行時，顯示在 LINE 聊天畫面上、作為使用者送出之訊息的文字。會透過 Webhook 從伺服器回傳。此屬性不應與快速回覆按鈕一起使用。\
最大字元限制：300\
`displayText` 與 `text` 屬性不可同時使用。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

inputOption

String

依使用者動作而定，例如 rich menu 的顯示方式。請指定下列其中一個值：

- `closeRichMenu`：關閉 rich menu
- `openRichMenu`：開啟 rich menu
- `openKeyboard`：開啟鍵盤
- `openVoice`：開啟語音訊息輸入模式

此屬性適用於 iOS 或 Android 上 LINE 版本 `12.6.0` 或更新版本。

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

fillInText

String

當鍵盤開啟時，預先填入輸入欄位的字串。僅在 `inputOption` 屬性設為 `openKeyboard` 時有效。字串可以用換行字元（`\n`）斷行。\
最大字元限制：300

此屬性適用於 iOS 或 Android 上 LINE 版本 `12.6.0` 或更新版本。

<!-- parameter end -->

#### Specifications of the label 

下列動作的 `label` 屬性，會依該動作所設定的物件而有不同的規格：

- [Postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)
- [Message action](https://developers.line.biz/en/reference/messaging-api/#message-action)
- [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)
- [Datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)
- [Clipboard action](https://developers.line.biz/en/reference/messaging-api/#clipboard-action)

上述列出之動作的標籤規格如下。對於上述以外的動作之標籤規格，請參閱各動作的規格說明。

<table>
  <thead>
    <tr>
      <th colspan="2">Object</th>
      <th>Required</th>
      <th>Max character limit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"><a href="#template-messages">Template messages</a></td>
      <td>Image carousel</td>
      <td>Optional</td>
      <td>12</td>
    </tr>
    <tr>
      <td>Other than image carousel</td>
      <td>Required</td>
      <td>20</td>
    </tr>
    <tr>
      <td colspan="2"><a href="#rich-menu-object">Rich menu</a> *1</td>
      <td>Optional</td>
      <td>20</td>
    </tr>
    <tr>
      <td colspan="2"><a href="#quick-reply-button-object">Quick reply button</a></td>
      <td>Required</td>
      <td>20</td>
    </tr>
    <tr>
      <td rowspan="2"><a href="#flex-message">Flex Message</a></td>
      <td>Button</td>
      <td>Required</td>
      <td>40</td>
    </tr>
    <tr>
      <td>Other than button *2</td>
      <td>Optional</td>
      <td>40</td>
    </tr>
  </tbody>
</table>

\*1 當用戶端裝置啟用無障礙功能時會被朗讀出來。

\*2 所指定的標籤不會被顯示。

_postback action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "postback",
  "label": "Buy",
  "data": "action=buy&itemid=111",
  "displayText": "Buy",
  "inputOption": "openKeyboard",
  "fillInText": "---\nName: \nPhone: \nBirthday: \n---"
}
```

<!-- tab end -->

### Message action 

當與此動作相關聯的控制項被點擊時，`text` 屬性中的字串會以使用者訊息的形式被送出。

<!-- parameter start (props: required) -->

type

String

`message`

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

label

String

此動作的標籤。其規格取決於該動作設定在哪一個物件上。詳情請參閱 [Specifications of the label](https://developers.line.biz/en/reference/messaging-api/#action-object-label-spec)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

text

String

執行動作時送出的文字\
最大字元限制：300

<!-- parameter end -->

_message action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "message",
  "label": "Yes",
  "text": "Yes"
}
```

<!-- tab end -->

### URI action 

當與此動作相關聯的控制項被點擊時，`uri` 屬性中指定的 URI 會在 LINE 的內建瀏覽器中開啟。

<!-- parameter start (props: required) -->

type

String

`uri`

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

label

String

此動作的標籤。其規格取決於該動作設定在哪一個物件上。詳情請參閱 [Specifications of the label](https://developers.line.biz/en/reference/messaging-api/#action-object-label-spec)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

uri

String

執行動作時開啟的 URI（最大字元限制：1000）\
可用的 scheme 為 `http`、`https`、`line` 與 `tel`。關於 LINE URL scheme 的更多資訊，請參閱 [Use LINE features with the LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/)。

URI 應使用 UTF-8 進行百分比編碼（percent-encoded）。詳情請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

altUri.desktop

String

執行動作時，在 macOS 版與 Windows 版 LINE 上開啟的 URI（最大字元限制：1000）\
若設定了 `altUri.desktop` 屬性，則在 macOS 版與 Windows 版 LINE 上會忽略 `uri` 屬性。\
可用的 scheme 為 `http`、`https`、`line` 與 `tel`。關於 LINE URL scheme 的更多資訊，請參閱 [Use LINE features with the LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/)。

URI 應使用 UTF-8 進行百分比編碼。詳情請參閱 [About the encoding of a URL specified in a request body property](https://developers.line.biz/en/reference/messaging-api/#url-encoding)。

<!-- note start -->

**Note**

在 Flex Messages 中設定 URI actions 時支援 `altUri.desktop`，但在快速回覆中無法使用。

<!-- note end -->

<!-- parameter end -->

_URI action 物件範例_

<!-- tab start `json` -->

```json
// Example of opening a specified URL in LINE's in-app browser
{
    "type": "uri",
    "label": "Menu",
    "uri": "https://example.com/menu"
}

// Example of opening different URLs for smartphone and desktop versions of LINE
{
   "type":"uri",
   "label":"View details",
   "uri":"http://example.com/page/222",
   "altUri": {
      "desktop" : "http://example.com/pc/page/222"
   }
}

// Example of opening a call app by specifying a phone number
{
    "type": "uri",
    "label": "Phone order",
    "uri": "tel:09001234567"
}

// Example of sharing LINE Official Account through LINE URL scheme
{
    "type": "uri",
    "label": "Recommend to friends",
    "uri": "https://line.me/R/nv/recommendOA/%40linedevelopers"
}
```

<!-- tab end -->

### Datetime picker action 

當與此動作相關聯的控制項被點擊時，會透過 Webhook 回傳一個 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event)，其中包含使用者從日期與時間選擇對話框中所選的日期與時間。datetime picker action 不支援時區。

<!-- parameter start (props: required) -->

type

String

`datetimepicker`

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

label

String

此動作的標籤。其規格取決於該動作設定在哪一個物件上。詳情請參閱 [Specifications of the label](https://developers.line.biz/en/reference/messaging-api/#action-object-label-spec)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

data

String

透過 Webhook 在 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 的 `postback.data` 屬性中回傳的字串\
最大字元限制：300

<!-- parameter end -->
<!-- parameter start (props: required) -->

mode

String

動作模式\
`date`：選擇日期\
`time`：選擇時間\
`datetime`：選擇日期與時間

<!-- parameter end -->
<!-- parameter start (props: optional) -->

initial

String

日期或時間的初始值

<!-- parameter end -->
<!-- parameter start (props: optional) -->

max

String

可選擇的最大日期或時間值。必須大於 `min` 值。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

min

String

可選擇的最小日期或時間值。必須小於 `max` 值。

<!-- parameter end -->

_datetime picker action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "datetimepicker",
  "label": "Select date",
  "data": "storeId=12345",
  "mode": "datetime",
  "initial": "2017-12-25t00:00",
  "max": "2018-01-24t23:59",
  "min": "2017-12-25t00:00"
}
```

<!-- tab end -->

#### Date and time format 

`initial`、`max` 與 `min` 值的日期與時間格式如下所示。`full-date`、`time-hour` 與 `time-minute` 格式遵循 [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) 協定。

| Mode | Format | Example |
| --- | --- | --- |
| date | `full-date`<br />Max: 2100-12-31<br />Min: 1900-01-01 | 2017-06-18 |
| time | `time-hour`:`time-minute`<br />Max: 23:59<br />Min: 00:00 | 00:00<br />06:15<br />23:59 |
| datetime | `full-date`T`time-hour`:`time-minute` or `full-date`t`time-hour`:`time-minute`<br />Max: 2100-12-31T23:59<br />Min: 1900-01-01T00:00 | 2017-06-18T06:15<br />2017-06-18t06:15 |

### Camera action 

此動作只能搭配快速回覆按鈕設定。當與此動作相關聯的按鈕被點擊時，會開啟 LINE 中的相機畫面。

<!-- parameter start (props: required) -->

type

String

`camera`

<!-- parameter end -->
<!-- parameter start (props: required) -->

label

String

此動作的標籤\
最大字元限制：20

<!-- parameter end -->

_camera action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "camera",
  "label": "Camera"
}
```

<!-- tab end -->

### Camera roll action 

此動作只能搭配快速回覆按鈕設定。當與此動作相關聯的按鈕被點擊時，會開啟 LINE 中的相簿畫面。

<!-- parameter start (props: required) -->

type

String

`cameraRoll`

<!-- parameter end -->
<!-- parameter start (props: required) -->

label

String

此動作的標籤\
最大字元限制：20

<!-- parameter end -->

_camera roll action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "cameraRoll",
  "label": "Camera roll"
}
```

<!-- tab end -->

### Location action 

此動作只能搭配快速回覆按鈕設定。當與此動作相關聯的按鈕被點擊時，會開啟 LINE 中的位置畫面。

<!-- parameter start (props: required) -->

type

String

`location`

<!-- parameter end -->
<!-- parameter start (props: required) -->

label

String

此動作的標籤\
最大字元限制：20

<!-- parameter end -->

_location action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "location",
  "label": "Location"
}
```

<!-- tab end -->

### Rich menu switch action 

此動作只能搭配 rich menu 設定。它無法用於 Flex Messages 或快速回覆。當您點擊與此動作相關聯的 rich menu 時，可以在多個 rich menu 之間切換，並透過 Webhook 回傳一個 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event)，其中包含使用者所選的 rich menu alias ID。詳情請參閱 Messaging API 文件中的 [Switch between tabs on rich menus](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/)。

<!-- parameter start (props: required) -->

type

String

`richmenuswitch`

<!-- parameter end -->
<!-- parameter start (props: optional) -->

label

String

動作標籤。對 rich menu 而言為選填。當使用者裝置的無障礙功能啟用時會被朗讀。

- 最大字元限制：20

<!-- parameter end -->
<!-- parameter start (props: required) -->

richMenuAliasId

String

要切換至的 rich menu alias ID。

<!-- parameter end -->
<!-- parameter start (props: required) -->

data

String

透過 Webhook 由 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 的 `postback.data` 屬性回傳的字串

- 最大字元限制：300

<!-- parameter end -->

_rich menu switch action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "richmenuswitch",
  "richMenuAliasId": "richmenu-alias-b",
  "data": "richmenu-changed-to-b"
}
```

<!-- tab end -->

### Clipboard action 

當使用者點擊與此動作相關聯的控制項時，`clipboardText` 屬性中指定的文字會被複製到裝置的剪貼簿。

此功能適用於 iOS 或 Android 上 LINE 版本 `14.0.0` 或更新版本。

<!-- parameter start (props: required) -->

type

String

`clipboard`

<!-- parameter end -->
<!-- parameter start (props: annotation="See description") -->

label

String

此動作的標籤。其規格取決於該動作設定在哪一個物件上。詳情請參閱 [Specifications of the label](https://developers.line.biz/en/reference/messaging-api/#action-object-label-spec)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

clipboardText

String

複製到剪貼簿的文字

- 最大字元限制：1000

<!-- parameter end -->

_clipboard action 物件範例_

<!-- tab start `json` -->

```json
{
  "type": "clipboard",
  "label": "Copy",
  "clipboardText": "3B48740B"
}
```

<!-- tab end -->

## Rich menu structure 

Rich menu 由下列任一物件組成。

- 不含 rich menu ID 的 [Rich menu object](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)。當您 [create a rich menu](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu) 時使用此物件。
- 含 rich menu ID 的 [Rich menu response object](https://developers.line.biz/en/reference/messaging-api/#rich-menu-response-object)。當您 [get a rich menu](https://developers.line.biz/en/reference/messaging-api/#get-rich-menu) 或 [get a list of rich menus](https://developers.line.biz/en/reference/messaging-api/#get-rich-menu-list) 時會回傳此物件。

[Area objects](https://developers.line.biz/en/reference/messaging-api/#area-object) 與 [action objects](https://developers.line.biz/en/reference/messaging-api/#action-objects) 都包含在這些物件中。

### Rich menu object 

<!-- tip start -->

**檢查 rich menu 物件是否有效**

若您想檢查 rich menu 物件是否有效，可以使用 [Validate rich menu object](https://developers.line.biz/en/reference/messaging-api/#validate-rich-menu-object) 端點（endpoint）。

<!-- tip end -->

<!-- parameter start (props: required) -->

size

Object

[`size` object](https://developers.line.biz/en/reference/messaging-api/#size-object)，內含顯示在聊天中之 rich menu 的寬度與高度。rich menu 圖片的寬度必須介於 800px 與 2500px 之間。高度必須至少為 250px。然而，長寬比（寬 / 高）必須至少為 1.45。

<!-- parameter end -->
<!-- parameter start (props: required) -->

selected

Boolean

`true` 表示預設顯示該 rich menu。否則為 `false`。

<!-- parameter end -->
<!-- parameter start (props: required) -->

name

String

rich menu 的名稱。此值可用於協助管理您的 rich menu，且不會顯示給使用者。\
最大字元限制：300

<!-- parameter end -->
<!-- parameter start (props: required) -->

chatBarText

String

顯示在聊天列（chat bar）中的文字\
最大字元限制：14

<!-- parameter end -->
<!-- parameter start (props: required) -->

areas

Array

[area objects](https://developers.line.biz/en/reference/messaging-api/#area-object) 的陣列（array），用於定義可點擊區域的座標與大小\
最多：20 個 area object

<!-- parameter end -->

_rich menu 物件範例_

<!-- tab start `json` -->

```json
{
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": false,
  "name": "Nice rich menu",
  "chatBarText": "Tap to open",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 2500,
        "height": 1686
      },
      "action": {
        "type": "postback",
        "data": "action=buy&itemid=123"
      }
    }
  ]
}
```

<!-- tab end -->

### Rich menu response object 

<!-- parameter start -->

richMenuId

String

rich menu 的 ID

<!-- parameter end -->
<!-- parameter start -->

size

Object

[`size` object](https://developers.line.biz/en/reference/messaging-api/#size-object)，內含顯示在聊天中之 rich menu 的寬度與高度。rich menu 圖片的寬度必須介於 800px 與 2500px 之間。高度必須至少為 250px。然而，長寬比（寬 / 高）必須至少為 1.45。

<!-- parameter end -->
<!-- parameter start -->

selected

Boolean

`true` 表示預設顯示該 rich menu。否則為 `false`。

<!-- parameter end -->
<!-- parameter start -->

name

String

rich menu 的名稱。此值可用於協助管理您的 rich menu，且不會顯示給使用者。\
最大字元限制：300

<!-- parameter end -->
<!-- parameter start -->

chatBarText

String

顯示在聊天列中的文字\
最大字元限制：14

<!-- parameter end -->
<!-- parameter start -->

areas

Array

[area objects](https://developers.line.biz/en/reference/messaging-api/#area-object) 的陣列，用於定義可點擊區域的座標與大小\
最多：20 個 area object

<!-- parameter end -->

_rich menu response 物件範例_

<!-- tab start `json` -->

```json
{
  "richMenuId": "{richMenuId}",
  "size": {
    "width": 2500,
    "height": 1686
  },
  "selected": false,
  "name": "Nice rich menu",
  "chatBarText": "Tap to open",
  "areas": [
    {
      "bounds": {
        "x": 0,
        "y": 0,
        "width": 2500,
        "height": 1686
      },
      "action": {
        "type": "postback",
        "label": "Buy",
        "data": "action=buy&itemid=123"
      }
    }
  ]
}
```

<!-- tab end -->

#### `size` object 

<!-- parameter start (props: required) -->

width

Number

rich menu 的寬度。rich menu 圖片的寬度必須介於 `800` 與 `2500` 之間。然而，長寬比（寬 / 高）必須至少為 1.45。

<!-- parameter end -->
<!-- parameter start (props: required) -->

height

Number

rich menu 的高度。高度必須至少為 `250`。然而，長寬比（寬 / 高）必須至少為 1.45。

<!-- parameter end -->

_size 物件範例_

<!-- tab start `json` -->

```json
{
  "width": 2500,
  "height": 1686
}
```

<!-- tab end -->

#### Area object 

<!-- parameter start (props: required) -->

bounds

Object

以像素描述該區域邊界的物件。請參閱 [`bounds` object](https://developers.line.biz/en/reference/messaging-api/#bounds-object)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

action

Object

點擊該區域時執行的動作。請參閱 [action objects](https://developers.line.biz/en/reference/messaging-api/#action-objects)。

<!-- parameter end -->

_area 物件範例_

<!-- tab start `json` -->

```json
{
  "bounds": {
    "x": 0,
    "y": 0,
    "width": 2500,
    "height": 1686
  },
  "action": {
    "type": "postback",
    "label": "Buy",
    "data": "action=buy&itemid=123"
  }
}
```

<!-- tab end -->

##### `bounds` object 

<!-- parameter start (props: required) -->

x

Number

可點擊區域左上角相對於圖片左緣的水平位置。值必須為 `0` 或更大。

<!-- parameter end -->
<!-- parameter start (props: required) -->

y

Number

可點擊區域左上角相對於圖片左緣的垂直位置。值必須為 `0` 或更大。

<!-- parameter end -->
<!-- parameter start (props: required) -->

width

Number

可點擊區域的寬度。

<!-- parameter end -->
<!-- parameter start (props: required) -->

height

Number

可點擊區域的高度。

<!-- parameter end -->

_bounds 物件範例_

<!-- tab start `json` -->

```json
{
  "x": 0,
  "y": 0,
  "width": 2500,
  "height": 1686
}
```

<!-- tab end -->
