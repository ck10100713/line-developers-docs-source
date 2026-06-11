# 應用程式內購買開發指南（In-app purchase development guidelines）

本頁說明在 LINE MINI App 中使用應用程式內購買功能時的規格限制、設計考量，以及建議的實作方式。

使用應用程式內購買功能時，請遵循下列開發指南。此外，也請務必參閱 [LINE MINI App 開發指南](https://developers.line.biz/en/docs/line-mini-app/development-guidelines/)。

**禁止事項**

- [請勿以 IP 位址限制存取](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#prohibit-ip-address-restriction)

**必要事項**

- [驗證存取權杖的有效性](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#verify-access-token)

**建議事項**

- [驗證 webhook 簽章](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#verify-webhook-signature)
- [排除重複](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#eliminate-duplicates)
- [實作適當的錯誤處理](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#error-handling)
- [請勿重複傳送付款通知](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#payment-notifications)

## Prohibited matters 

### Don't restrict access by IP address 

在接收 webhook 的伺服器上，請勿根據傳送 webhook 請求的 LINE Platform 之 IP 位址來限制存取。LINE Platform 的 IP 位址並未公開，且可能在未事先通知的情況下變更。請改用[簽章驗證](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#verify-webhook-signature)來拒絕來自未經授權來源的請求，而非以 IP 位址進行存取控制。

## Required matters 

### Verify access token validity 

進行購買預約時，請使用[驗證存取權杖的有效性](https://developers.line.biz/en/reference/line-login/#verify-access-token)端點，在 LINE MINI App 的伺服器端驗證存取權杖（access token）的有效性、頻道 ID（channel ID）以及存取權杖的有效期間（validity period）。

## Recommended matters 

### Implement with non-breaking changes in mind 

在 LINE MINI App 應用程式內購買中，可能會進行不破壞相容性（non-breaking）的功能新增。這些變更的目的是在不破壞現有功能的前提下擴充 API。因此，下列類型的變更可能會在未事先通知的情況下進行：

- 新增端點（endpoint）
- 在 API 請求中新增選用的參數、欄位與標頭
- 在 API 回應中新增欄位與標頭
- 新增列舉值（enum value）
- 在 webhook 事件物件中新增屬性
- 變更 API 回應與 webhook 事件物件中屬性的順序
- 資料元素之間是否存在空白或換行

請將你的伺服器實作成即使遇到這些不破壞相容性的功能新增，也能正常運作。

### Verify the webhook signature 

為了防止偽造的請求，請使用 `x-line-signature` 請求標頭來驗證簽章。

- 以頻道密鑰（channel secret）作為密鑰，使用 HMAC-SHA256 演算法計算請求主體的摘要（digest）。
- 將摘要以 Base64 編碼，並檢查其是否與 `x-line-signature` 請求標頭中所含的簽章相符。

以 Java 進行簽章驗證的範例

```java
class WebhookProcessor {
    void verify(String httpRequestBody) { // Request body string
        String channelSecret = '...'; // Channel secret string
        SecretKeySpec key = new SecretKeySpec(channelSecret.getBytes(), "HmacSHA256");
        Mac mac = Mac.getInstance("HmacSHA256");
        mac.init(key);

        byte[] source = httpRequestBody.getBytes("UTF-8");
        String signature = Base64.encodeBase64String(mac.doFinal(source));
        // Compare x-line-signature request header string and the signature
    }
}
```

如需 webhook 簽章驗證的詳細資訊，請參閱 Messaging API 文件中的[驗證 Webhook 簽章](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/)。

### Eliminate duplicates 

由於網路狀況的關係，同一個 webhook 事件可能會被傳送多次。請使用訂單 ID（`orderId`）來確保不會針對單一購買重複授予商品。此外，若使用者在應用程式商店中取消付款，也請確保取消處理不會被執行多次。

### Implement proper error handling 

購買預約並不保證付款一定會完成。若發生網路錯誤或其他問題，請採取適當的處置，例如重試請求或提示使用者再試一次。

### Don't send duplicate payment notifications 

當購買完成時，系統會自動從 LINE 官方帳號「LINE In-App Purchase Notifications（日文為 LINEアプリ内課金お知らせ）」向使用者傳送訊息。同樣地，若使用者在應用程式商店中取消付款，系統也會自動向使用者傳送訊息。

如果在此之外還從另一個 LINE 官方帳號傳送付款通知，使用者就會多次收到同類型的通知。為了避免降低使用者體驗，請勿傳送重複的通知。
