# 重試失敗的 API 請求（Retry failed API requests）

您的訊息可能無法送達，這種情況下您會收到 5xx 錯誤或請求逾時。但即使您收到這類錯誤，您的訊息仍有可能已經送達。因此，若您因為錯誤而再次送出相同的請求，收件者可能會收到兩次相同的訊息，如下圖所示：

![](https://developers.line.biz/media/messaging-api/retry-api-request/retry-api-request-bad-en.svg)

為了避免送出兩次相同的訊息，請使用重試金鑰（retry key，`X-Line-Retry-Key`）。若您指定了重試金鑰，無論您發出多少次請求，該請求都只會被執行一次。一旦請求被接受，後續重試的請求都會被封鎖，您將會收到狀態碼 `409`。

因此，我們建議您在進行重試時使用重試金鑰，以防止同一個 API 請求被重複執行。

![](https://developers.line.biz/media/messaging-api/retry-api-request/retry-api-request-good-en.svg)

<!-- note start -->

**Note**

`X-Line-Retry-Key` 可讓您安全地重試 API 請求而不會重複傳送訊息，但它並不保證訊息能夠可靠地送達。只要 API 請求曾經被 LINE Platform 接受過一次（HTTP 狀態碼 200），即使因為使用者已封鎖 LINE 官方帳號而導致訊息無法正確送達，也無法再重試相同的請求。

<!-- note end -->

## Flow of retrying API requests 

若要使用支援重試金鑰的 API，請依照下圖所示的流程發出您的請求：

![Retry API Request Flowchart](https://developers.line.biz/media/messaging-api/retry-api-request/retry-key-flowchart-en.png)

### Specify the retry key always 

當您使用支援重試金鑰的 API 傳送訊息時，請務必在請求標頭（request header）中指定重試金鑰 `X-Line-Retry-Key`。重試金鑰應為以您自選的方法所產生的十六進位 UUID。

<!-- note start -->

**Specify the retry key in the first API request**

未帶有 `X-Line-Retry-Key` 的 API 請求永遠無法重試。請務必在第一次發出請求時就加上該金鑰。

<!-- note end -->

支援重試的 API 如下：

| Sending methods | API reference |
| --- | --- |
| Push messages | [Send push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message) |
| Multicast messages | [Send multicast message](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message) |
| Narrowcast messages | [Send narrowcast message](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message) |
| Broadcast messages | [Send broadcast message](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message) |

<!-- note start -->

**Retry only with supported APIs**

若您在上述未列出的 API 的請求標頭中指定 `X-Line-Retry-Key`，您的請求將會被拒絕，並收到狀態碼 `400`。

<!-- note end -->

以下是一個帶有重試金鑰（`123e4567-e89b-12d3-a456-426614174000`）來傳送 push message 的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {CHANNEL_ACCESS_TOKEN}' \
-H 'X-Line-Retry-Key: 123e4567-e89b-12d3-a456-426614174000' \
-d '{
  "messages": [
    {
      "type": "text",
      "text": "Hello, user"
    }
  ]
}'
```

### Retry API requests by status code 

請依照您所收到的狀態碼來判斷是否要重試 API 請求：

| Status code | Description | Retry or not |
| --- | --- | --- |
| 500 Internal Server Error | 內部伺服器錯誤 | ✅ 重試。您的下一次請求可能會成功。 |
| Timeout | 請求因網路故障或其他原因而失敗。 | ✅ 重試。您的下一次請求可能會成功。 |
| 2xx | API 請求已被接受。 | ❌ 不要重試。不會接受額外的重試。 |
| 409 Conflict | 已有一個使用相同重試金鑰的 API 請求被接受。 | ❌ 不要重試。重試的請求已被接受。 |
| 4xx | 請求有問題 | ❌ 不要重試。重試不會改變結果。 |

<!-- note start -->

**Note**

- 重試金鑰在第一次請求後的 24 小時內有效。請將您的服務設計為在 24 小時內重試請求。
- 請讓您重試的請求與原始請求相同。不要更改內容或收件者。若您做了更改卻使用相同的重試金鑰，重試可能不會如您預期般運作。

<!-- note end -->

<!-- tip start -->

**Interval between retries**

- 帶有重試金鑰的重試會被計為一次 API 請求，因此頻繁重試可能會導致達到 API 速率限制（API rate limit）。
- 為了在伺服器或網路發生故障時維持較低的負載，我們建議您採用[指數退避（exponential backoff）](https://en.wikipedia.org/wiki/Exponential_backoff)來維持重試間隔。

<!-- tip end -->

#### Retry responses 

您重試的 API 請求所收到的回應會有所不同，取決於該 API 請求是否已被接受。

<!-- tip start -->

**Different request ID is issued**

若多個使用相同重試金鑰的請求被執行，每個請求都會取得不同的 request ID。

<!-- tip end -->

##### Response to an accepted request 

對於成功的重試請求，您會收到與正常被接受的請求相同的回應。以下是一個範例：

```sh
HTTP/1.1 200 OK
x-line-request-id: 123e4567-e89b-12d3-a456-426655440001
```

##### Response to retrying an accepted request 

若您重試一個 LINE Platform 已回傳狀態碼 `2xx` 的 API 請求，您將會收到狀態碼 `409`。該回應會回傳成功請求的 ID，即 `x-line-accepted-request-id`。

```sh
HTTP/1.1 409 Conflict
x-line-request-id: 123e4567-e89b-12d3-a456-426655440002
x-line-accepted-request-id: 123e4567-e89b-12d3-a456-426655440001

{
  "message": "The retry key is already accepted"
}
```

此外，在 push message 的情況下，會回傳一個包含與 API 請求被接受時相同的 `sentMessages.id` 與 `sentMessages.quoteToken` 的 JSON 物件。

```sh
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

## Related pages 

如需更多關於進行重試的資訊，請參閱 Messaging API reference 中的 [Retrying an API request](https://developers.line.biz/en/reference/messaging-api/#retry-api-request)。
