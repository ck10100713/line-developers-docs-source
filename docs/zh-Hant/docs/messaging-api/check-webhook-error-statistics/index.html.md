# 查看 webhook 錯誤原因與統計資料

Messaging API 提供一項功能，可在傳送 webhook 時查看錯誤原因與統計資料。當 webhook 因 bot 伺服器發生問題等而未被接收時，這項功能有助於了解 webhook 的傳送狀況。

![當 bot 伺服器回傳錯誤時顯示的錯誤統計資料](https://developers.line.biz/media/messaging-api/receiving-messages/webhook-error-en.jpg)

## Enable error statistics 

錯誤統計資料的顯示功能預設為停用。若要顯示錯誤統計資料，請從 [LINE Developers Console](https://developers.line.biz/console/) 執行以下步驟：

1. 開啟你想顯示錯誤統計資料的頻道（channel）設定畫面。
1. 點擊 **Messaging API** 分頁。
1. 開啟 **Use webhook**。
1. 開啟 **Error statistics aggregation**。

開啟 **Error statistics aggregation** 後，點擊 **Webhook errors** 分頁即可查看統計資料。錯誤僅會在 **Error statistics aggregation** 開啟期間進行彙整。停用期間的資料不會被回溯顯示。所顯示錯誤的日期與時間使用的時區為 UTC+9。你也可以點擊 **Download TSV file** 以 TSV 格式下載過去的錯誤資訊。

![Error statistics aggregation](https://developers.line.biz/media/messaging-api/receiving-messages/error-statistics-en.png)

<!-- tip start -->

**錯誤統計資料不包含用於驗證 webhook URL 的請求**

錯誤統計資料只會顯示實際嘗試傳送的 webhook。無論成功或失敗，錯誤統計資料都不會包含用於[驗證 webhook URL](https://developers.line.biz/en/docs/messaging-api/verify-webhook-url/) 的請求。

<!-- tip end -->

## Check the reason for errors 

錯誤統計資料提供錯誤的原因與詳細資訊。原因共有四種類型。

| 錯誤原因 | 摘要 |
| --- | --- |
| `could_not_connect` | LINE Platform 嘗試將 webhook 傳送至 bot 伺服器，但無法成功連線到 bot 伺服器。詳情請參閱[原因為 could_not_connect](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-could-not-connect) 章節。 |
| `request_timeout` | LINE Platform 將 webhook 傳送至 bot 伺服器，但 bot 伺服器未在 2 秒內回傳回應。詳情請參閱[原因為 request_timeout](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-request-timeout) 章節。 |
| `error_status_code` | LINE Platform 將 webhook 傳送至 bot 伺服器，但 bot 伺服器回傳的回應不是 `20x` 範圍內的 HTTP 狀態碼。詳情請參閱[原因為 error_status_code](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-status-code) 章節。 |
| `unclassified` | 發生了無法歸類於上述類別的未知錯誤。詳情請參閱[原因為 unclassified](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-unclassified) 章節。 |

## Check the detail for errors 

各原因的詳細資訊如下：

- [原因為 could_not_connect](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-could-not-connect)
- [原因為 request_timeout](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-request-timeout)
- [原因為 error_status_code](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-status-code)
- [原因為 unclassified](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#reason-unclassified)

### The reason is `could_not_connect` 

若 LINE Platform 嘗試將 webhook 傳送至 bot 伺服器，但無法成功連線到 bot 伺服器，原因會是 `could_not_connect`。在此情況下的詳細資訊如下。

| 錯誤詳細資訊 | 摘要 |
| --- | --- |
| `Connection failed` | 連線到 bot 伺服器失敗。 |
| `Connection failed (received GOAWAY)` | 連線到 bot 伺服器時遭拒絕。 |
| `Connection failed (session closed)` | 與 bot 伺服器的連線意外中斷。 |
| `Connection timeout` | 在特定時間內未完成與 bot 伺服器的連線。 |
| `DNS Query timeout` | 已對 webhook URL 進行名稱解析，但無法在特定時間內完成名稱解析。 |
| `Invalid URL syntax` | 指定了無效的 webhook URL（例如違反 RFC）。 |
| `Session protocol negotiation failure` | 已連線到 bot 伺服器，但協定協商失敗。 |
| `No SSL/TLS record` | bot 伺服器的回應未經 SSL/TLS 加密。 |
| `TLS handshake failure` | 已連線到 bot 伺服器，但 TLS handshake 失敗。請檢查 bot 伺服器是否支援 [webhook 來源的 SSL/TLS 規格](https://developers.line.biz/en/docs/messaging-api/ssl-tls-spec-of-the-webhook-source/)。 |
| `Unknown host` | 找不到 Webhook URL 中指定的主機。 |

### The reason is `request_timeout` 

若 webhook 從 LINE Platform 傳送至 bot 伺服器，但 LINE Platform 未收到回應，或傳送在中途失敗，原因會是 `request_timeout`。在此情況下的詳細資訊如下。請注意，webhook 仍有可能已被 bot 伺服器成功接收。

| 錯誤詳細資訊 | 摘要 |
| --- | --- |
| `Request timeout` | Webhook 已傳送至 bot 伺服器，但在特定時間內未回傳回應。 |

### The reason is `error_status_code` 

若原因為 `error_status_code`，詳細資訊中會包含 HTTP 狀態碼。

### The reason is `unclassified` 

若發生無法歸類的錯誤，原因會是 `unclassified`。在此情況下的詳細資訊如下。

| 錯誤詳細資訊 | 摘要 |
| --- | --- |
| `Session closed unexpectedly` | 已將 webhook 傳送至 bot 伺服器，但連線意外關閉。 |
| `Stream closed unexpectedly` | 已將 webhook 傳送至 bot 伺服器，但 stream 意外關閉。 |
| `Unclassified webhook dispatch error` | 發生了無法歸類且非預期的錯誤。 |

## Enable webhook redelivery to prepare for errors 

事先啟用 webhook 重新傳送功能後，若你的 bot 伺服器接收 webhook 失敗而發生錯誤，webhook 會重新傳送至你的 bot 伺服器。詳情請參閱[重新傳送接收失敗的 webhook](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-redelivery)。
