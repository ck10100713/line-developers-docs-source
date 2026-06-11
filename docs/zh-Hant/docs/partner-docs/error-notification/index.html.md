# 錯誤通知（Error notification）

<!-- note start -->

**使用選用功能需提出申請**

只有已提交必要申請的企業用戶才能使用本文件所述的功能。若要在您的 LINE 官方帳號（LINE Official Account）使用這些功能，請聯絡您的業務負責人，或聯絡[我們的業務夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## Summary 

當用戶將您的 LINE 官方帳號加為好友，或向您的 LINE 官方帳號傳送訊息時，LINE Platform 會將 Webhook 事件傳送到 [LINE Developers Console](https://developers.line.biz/console/) 中「Webhook URL」所指定的 URL（bot 伺服器）。

如果 bot 伺服器沒有回應這個 Webhook 事件請求，或回傳了狀態碼 `2xx` 以外的回應，頻道管理員就會收到一封通知電子郵件，告知錯誤的發生。這個選項稱為「錯誤通知（error notification）」功能。

![當 bot 伺服器回傳錯誤時，您將會收到通知電子郵件](https://developers.line.biz/media/partner-docs/normal-error-notification-en.jpg)

## Notification email 

本主題說明錯誤通知功能所寄送的電子郵件。

### Email recipients 

通知電子郵件將寄送到下列電子郵件地址：

- 目標頻道（channel）的 **Basic settings** 頁面上所註冊的電子郵件地址
- 對目標頻道具有 Admin 角色的用戶所註冊的電子郵件地址

### Email types 

通知電子郵件可分為下列類型：

- [當 LINE Platform 偵測到錯誤時](https://developers.line.biz/en/docs/partner-docs/error-notification/#detected-error)
- [當 LINE Platform 停止 Webhook 重新投遞時](https://developers.line.biz/en/docs/partner-docs/error-notification/#webhook-redelivery-stopped)（僅在已啟用 Webhook 重新投遞時）

#### When the LINE Platform detected an error 

當 LINE Platform 偵測到發生錯誤時，將寄送下列電子郵件。電子郵件的內容與錯誤訊息可能會在未經通知的情況下變更。

| | |
| --- | --- |
| Subject | Messaging API: Your bot server returned no response or an error - `<Channel name>` |
| Main text | LINE Platform sent a webhook, but your bot server did not respond or returned an error.<br/>Check the reason and details for the error and your bot server's configuration. Then make any necessary changes so that it can receive webhooks properly. |
| Error details | 錯誤原因以及發生的日期與時間會依各情況分別說明。詳情請參閱 [Email content](https://developers.line.biz/en/docs/partner-docs/error-notification/#content)。 |

<!-- tip start -->

**您也可以在 LINE Developers Console 中查看錯誤資訊**

您也可以在 [LINE Developers Console](https://developers.line.biz/console/) 中查看您在通知電子郵件中收到的錯誤資訊。詳情請參閱 [LINE Developers Console 中的「Webhook errors」分頁](https://developers.line.biz/en/docs/partner-docs/error-notification/#line-developers-console)。

<!-- tip end -->

#### When the LINE Platform stopped webhook redelivery 

如果您在 Messaging API 頻道設定中[啟用了 Webhook 重新投遞](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#enable-webhook-redelivery)，LINE Platform 會重新投遞您的 bot 伺服器未能成功接收的 Webhook。

接著，如果 bot 伺服器在經過一段時間後仍未回應，LINE Platform 會停止重新投遞該 Webhook，並寄送下列電子郵件。電子郵件的主旨與內容可能會在未經通知的情況下變更。

| | |
| --- | --- |
| Subject | Messaging API: Webhook redelivery stopped - `<Channel name>` |
| Main text | The LINE Platform tried to send the webhook for the event(s), but stopped redelivery due to no response from your bot server.<br>Please visit the LINE Developers site for details. |
| Error details | 錯誤原因以及發生的日期與時間會依各情況分別說明。詳情請參閱 [Email content](https://developers.line.biz/en/docs/partner-docs/error-notification/#content)。 |

關於 Webhook 重新投遞的詳細資訊，請參閱[重新投遞未能成功接收的 Webhook](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-redelivery)。

### Notification email sample 

![sample mail](https://developers.line.biz/media/partner-docs/error-notification-email-sample.png)

### Email content 

以下是電子郵件的內容。

| Item | Description |
| --- | --- |
| Channel ID | 目標頻道 ID。 |
| Channel name | 目標頻道名稱。 |
| Reason for error  | 錯誤原因的概要。詳細資訊請參閱 Messaging API 文件中的[查看錯誤原因](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#check-error-reason)。 |
| Detail for error | 錯誤原因的細節。詳細資訊請參閱 Messaging API 文件中的[查看錯誤細節](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#check-detail-for-error)。 |
| Error count | 錯誤發生的次數。 |
| Time detected | 錯誤發生的時間。 |

## How to resolve a notification message 

假設您收到的錯誤通知內容與[通知電子郵件範例](https://developers.line.biz/en/docs/partner-docs/error-notification/#sample-mail)相同。由於錯誤原因是 `error_status_code`、錯誤細節是 `500`，因此根據[查看錯誤原因](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#check-error-reason)，您可以推斷 bot 伺服器以 HTTP 狀態碼 `500` 回應了該 Webhook 請求。

在這種情況下，bot 伺服器可能無法正確處理它所接收到的 Webhook 事件。請檢查 bot 伺服器的 Webhook 事件處理紀錄（log），以調查問題的成因。

<!-- note start -->

**關於錯誤調查**

LY Corporation 不提供針對個別錯誤的調查或確認。錯誤的原因應由管理該頻道或 bot 伺服器的開發者直接處理。

<!-- note end -->

## "Webhook errors" tab in the LINE Developers Console 

您也可以在 [LINE Developers Console](https://developers.line.biz/console/) 上 Messaging API 頻道的 **Webhook errors** 分頁中，查看通知電子郵件中所收到的錯誤資訊。

**Webhook errors** 分頁只會在已於 **Messaging API** 分頁啟用 **Error statistics aggregation** 的頻道顯示。詳細資訊請參閱[啟用錯誤統計](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#enable-error-statistics)。

![Error statistics aggregation](https://developers.line.biz/media/messaging-api/receiving-messages/error-statistics-en.png)
