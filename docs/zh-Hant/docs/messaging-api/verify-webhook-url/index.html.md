# 驗證 Webhook URL（Verify webhook URL）

如果你正在使用 Messaging API 的 Webhook，建議你使用下列其中一種方法，來驗證 LINE Platform 是否能與 Webhook URL（bot 伺服器）通訊。

- [驗證方法 1：使用 Webhook URL 驗證端點進行驗證](https://developers.line.biz/en/docs/messaging-api/verify-webhook-url/#verify-method-01)
- [驗證方法 2：使用 LINE Developers Console 中 Webhook URL 的「Verify」按鈕](https://developers.line.biz/en/docs/messaging-api/verify-webhook-url/#verify-method-02)

<!-- tip start -->

**針對通訊請求回傳狀態碼 200**

LINE Platform 會向 Webhook URL（bot 伺服器）發送一個不包含 Webhook 事件的 HTTP POST 請求，以確認通訊狀況。請將你的 bot 伺服器設計為回傳狀態碼 `200`。

不包含 Webhook 事件的 HTTP POST 請求範例：

```json
{
  "destination": "xxxxxxxxxx",
  "events": []
}
```

<!-- tip end -->

如果在驗證 Webhook URL 之後，bot 伺服器仍未收到 Webhook，請[調查 Webhook 接收失敗的原因](https://developers.line.biz/en/docs/messaging-api/verify-webhook-url/#investigate-webhook-reception-failure)。

## Verification method 1: Verify with the endpoint for webhook URL validation 

使用 Webhook URL 測試端點來驗證通訊狀況。

- [測試 Webhook 端點](https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint)

## Verification method 2: Use the webhook URL's "Verify" button in the LINE Developers Console 

在 [LINE Developers Console](https://developers.line.biz/console/) 中，點擊 Webhook URL 的 **Verify** 按鈕來進行驗證。

![send target](https://developers.line.biz/media/news/webhook-url-verify-button.png)

## Investigate the cause of webhook reception failure 

如果在驗證 Webhook URL 之後，bot 伺服器仍未收到 Webhook，請使用下列方法來調查 Webhook 接收失敗的原因：

- 檢查測試 Webhook URL 端點所回傳的[回應](https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint-response)或[錯誤回應](https://developers.line.biz/en/reference/messaging-api/#test-webhook-endpoint-error-response)
- [檢查 Webhook 錯誤原因與統計資料](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/)
- 檢查 [Webhook 來源的 SSL/TLS 規格](https://developers.line.biz/en/docs/messaging-api/ssl-tls-spec-of-the-webhook-source/)
