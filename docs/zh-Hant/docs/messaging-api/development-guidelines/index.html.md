# Messaging API 開發指南（Messaging API development guidelines）

在開始開發機器人之前，請先了解使用 Messaging API 開發機器人時有哪些建議事項與禁止事項。

**禁止事項**

- [不要對 LINE Platform 發送大量請求](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-mass-requests-to-line-platform)
- [不要透過 LINE Platform 進行負載測試](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-line-platform-load-tests)
- [不要對同一位使用者發送大量訊息](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-mass-transmissions-to-same-user)
- [不要對無效的使用者 ID 發送請求](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-requests-for-non-existent-user-ids)
- [不要嘗試識別使用者屬性](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-identify-users-attribute)
- [不要以 IP 位址限制存取](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-ip-address-restrictions)

**建議事項**

- [收到收回（unsend）事件時的建議處理方式](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#webhook-unsend-message)
- [接收 webhook 時，建議驗證 webhook 簽章](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#verify-webhook-signature)
- [建議以「不破壞相容性的功能新增」為前提進行實作](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#assume-non-breaking-changes)
- [保存日誌](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#save-logs)

<!-- note start -->

**Note**

機器人開發的基本規則是以[條款與政策（terms and policies）](https://developers.line.biz/en/terms-and-policies/)為依據。

<!-- note end -->

## Prohibited matters 

### Don't send mass requests to the LINE Platform 

不要為了負載測試或操作測試而對 LINE Platform 發送大量請求。在所有情況下，請務必將請求數量控制在指定的[速率限制（rate limits）](https://developers.line.biz/en/reference/messaging-api/#rate-limits)以內。若發送的請求超過速率限制，將會收到 `429 Too Many Requests` 錯誤。

<!-- note start -->

**速率限制內的操作測試**

即使遵守速率限制，也不要高頻率地發送以下這類請求：

- 重複建立與刪除[受眾（audiences）](https://developers.line.biz/en/docs/messaging-api/using-audience/#create-audience)，但實際上並未用於發送 narrowcast 訊息
- 重複發送並未使用 Messaging API 功能的請求

<!-- note end -->

### Don't do load testing through the LINE Platform 

LINE Platform 並未提供用於對機器人伺服器進行負載測試的服務。請勿透過 LINE Platform 發送大量訊息來對你的機器人伺服器進行負載測試。請另外準備一個專門用於對機器人伺服器進行負載測試的環境。

### Don't send mass messages to the same user 

在所有情況下，請勿對同一位使用者發送過多的訊息。

### Don't send requests to invalid user IDs 

請勿對不存在的[使用者 ID（user ID）](https://developers.line.biz/en/glossary/#user-id)發送請求。

### Don't try to identify user attributes 

請勿嘗試識別特定使用者 ID 的使用者[屬性（attributes）](https://developers.line.biz/en/reference/messaging-api/#narrowcast-demographic-filter)。此外，也不要為了識別使用者屬性而使用[管理受眾（Managing Audience）](https://developers.line.biz/en/reference/messaging-api/#manage-audience-group) API 或發送 [narrowcast 訊息](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)。

### Don't restrict access by IP address 

在接收 webhook 的機器人伺服器上，請勿以 LINE Platform 的 IP 位址來限制發送 webhook 請求的存取。請改用[簽章驗證（signature validation）](https://developers.line.biz/en/reference/messaging-api/#signature-validation)來拒絕來自未授權來源的請求，而非以 IP 位址進行存取控制。這是因為我們不會公開 LINE Platform 的 IP 位址，而且 IP 位址可能會在不另行通知的情況下變更。

## Recommended matters 

### Recommended processing on receipt of unsend event 

當使用者收回（unsend）已發送的訊息時，會有一個[收回事件（unsend event）](https://developers.line.biz/en/reference/messaging-api/#unsend-event)被發送至機器人伺服器。

收到收回事件時，我們建議服務提供者尊重使用者收回已發送訊息的意圖，並以最謹慎的態度妥善處理該訊息，使該目標訊息在日後無法被檢視或使用。

詳情請參閱[收到收回事件時的處理方式（Processing on receipt of unsend event）](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#webhook-unsend-message)。

### Recommended verification of webhook signature when receiving webhooks 

當機器人伺服器收到 webhook 事件時，建議機器人伺服器在處理 [webhook 事件物件（webhook event objects）](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)之前，先驗證請求標頭中所包含的簽章。此驗證步驟很重要，可用以確認該 webhook 確實來自 LINE Platform，且在傳輸過程中未遭竄改。

詳情請參閱[驗證 webhook 簽章（Verify webhook signature）](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/)。

### Recommendation for implementation assuming non-breaking feature additions 

在 Messaging API 中，可能會進行不破壞相容性的功能新增。這些變更的目的是在不破壞既有功能的前提下擴充 API。因此，以下類型的變更可能會在不事先通知的情況下進行：

- 新增端點（endpoint）
- 在 API 請求中新增選用的參數、欄位與標頭
- 在 API 回應中新增欄位與標頭
- 在 webhook 事件物件中新增屬性
- 變更 API 回應與 webhook 事件物件中屬性的順序
- 新增列舉值（例如：新增 [webhook 事件物件（webhook event object）](https://developers.line.biz/en/reference/messaging-api/#common-properties)中 `type` 屬性的值）
- 資料元素之間是否包含空格或換行

請將你的機器人伺服器實作成即使遇到這些不破壞相容性的功能新增，也能正常運作而不會發生任何問題。

### Save logs 

我們建議你將所發送的 [Messaging API 請求](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#messaging-api-logs)與所接收的 [webhook](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#webhook-logs)的日誌保存一段時間。這些日誌有助於你在調查問題原因時使用。

<!-- tip start -->

**值得保存於日誌中的有用資料**

除了本節所建議要記錄的基本資訊之外，以下這些資料也可能對你有所幫助。請依據你的機器人需求，考慮是否保存這些資料：

- 你所呼叫的 Messaging API 的請求主體參數
- LINE Platform 針對該 API 呼叫所回傳的回應主體
- 當 webhook 由 LINE Platform 發送時，[請求標頭（request header）](https://developers.line.biz/en/reference/messaging-api/#request-headers)中的簽章（`x-line-signature`）
- LINE Platform 所發送的 [webhook 事件物件（Webhook event object）](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)

<!-- tip end -->

<!-- note start -->

**我們不提供日誌**

即使你提出詢問，我們也不會提供 Messaging API 請求或 LINE Platform 所發送 webhook 的日誌。保存日誌是你的責任。

<!-- note end -->

#### Save logs for Messaging API requests 

當你向 Messaging API 發送請求時，我們建議你記錄以下資訊：

- [回應標頭（Response header）](https://developers.line.biz/en/reference/messaging-api/#response-headers)中的請求 ID（`x-line-request-id`）
- 發送該 API 請求的時間
- 該請求的 HTTP 方法
- 所呼叫的 API 端點
- LINE Platform 所回傳的[狀態碼（Status code）](https://developers.line.biz/en/reference/messaging-api/#status-codes)

請以如下格式將各項資料保存於日誌檔中：

| 請求 ID（`x-line-request-id`） | API 請求的時間 | HTTP 方法 | API 端點 | 狀態碼 |
| --- | --- | --- | --- | --- |
| 8e36bade-c5d6-4d00-9e69-72244675a9a1 | Mon, 05 Jul 2021 08:14:35 GMT | POST | `https://api.line.me/v2/bot/message/push` | 200 |

#### Save logs for webhooks received 

當你的機器人伺服器從 LINE Platform 收到 [webhook](https://developers.line.biz/en/reference/messaging-api/#webhooks) 時，我們建議你記錄以下資訊：

- webhook 發送方的 IP 位址
- 收到該 webhook 的時間
- HTTP 方法
- 請求路徑
- 機器人伺服器針對所收到的 webhook 在[回應（response）](https://developers.line.biz/en/reference/messaging-api/#response)中所回傳的狀態碼

請以如下格式將各項資料保存於日誌檔中：

| 發送方 IP 位址 | 收到 webhook 的時間 | HTTP 方法 | 請求路徑 | 狀態碼 |
| --- | --- | --- | --- | --- |
| 203.0.113.1 | Mon, 05 Jul 2021 08:10:00 GMT | POST | `/linebot/webhook` | 200 |
