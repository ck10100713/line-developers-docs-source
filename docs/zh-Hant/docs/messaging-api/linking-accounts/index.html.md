# 使用者帳號連結（User account linking）

身為服務供應商，您可以讓您的服務使用者**安全地**將其 LINE 帳號連結至您服務的帳號。要連結帳號，使用者必須將您的 LINE 官方帳號（LINE Official Account）加為好友。引導使用者將其 LINE 帳號連結至您的服務帳號後，您便能在 LINE 上運用來自您服務的使用者資料。藉由這些使用者資料，您可以讓使用者在您的 LINE 官方帳號上獲得更豐富的體驗。

當使用者將其 LINE 帳號連結至您的服務帳號後，您就能運用您的 LINE 官方帳號來造福使用者。舉例來說，如果您的服務是一個購物網站，您可以：

- 當使用者在您的購物網站完成購買時，透過您的 LINE 官方帳號傳送 LINE 訊息給該使用者。
- 讓使用者在與您 LINE 官方帳號的聊天中下訂單。

您可以透過 LINE Login 來連結帳號，但這樣您就需要有一個 LINE Login 頻道（channel）。使用 Messaging API，您無需 LINE Login 頻道即可連結帳號。

## Account linking sequence 

將使用者的 LINE 帳號連結至您服務帳號的流程如下：

![](https://developers.line.biz/media/messaging-api/linking-accounts/sequence.png)

1. 您的 bot 伺服器以使用者的 LINE user ID 呼叫核發連結權杖（link token）的 API。
1. LINE Platform 核發並回傳連結權杖給您的 bot 伺服器。
1. 您的 bot 伺服器呼叫 Messaging API，傳送連結用 URL 給使用者。
1. LINE Platform 將連結用 URL 傳送給使用者。
1. 使用者存取該連結用 URL。
1. 您的 Web 伺服器送出您服務的登入頁面。
1. 使用者輸入其在您服務的登入憑證。
1. 您的 Web 伺服器取得使用者在您服務的 user ID，並使用該 ID 產生一個 nonce（僅使用一次的數值）。
1. 您的 Web 伺服器將使用者重新導向至帳號連結端點（account-linking endpoint）。
1. 使用者存取該帳號連結端點。
1. LINE Platform 傳送一個包含 LINE user ID 與 nonce 的 webhook 事件給您的 bot 伺服器。
1. 您的 bot 伺服器使用該 nonce 取得使用者在您服務的 user ID。

您也可以自行實作帳號連結，而不仰賴 Messaging API。然而，您的使用者可能因帳號連結而面臨安全性問題，因此若您選擇自行實作，請務必留意。舉例來說，攻擊者可能傳送一個 URL 給使用者，藉此將攻擊者的 LINE 帳號連結至使用者的服務帳號。Messaging API 能保護使用者免於此類攻擊。Messaging API 會檢查發起核發連結用 URL 的使用者，是否為要連結之 LINE 帳號的真正擁有者。

## Linking accounts 

要將您服務的使用者帳號與 LINE 的使用者帳號連結，請依照下列指示進行：

### 1. Issue a link token 

您需要一個連結權杖（link token）才能連結使用者的 LINE 帳號與您的服務帳號。要[核發連結權杖](https://developers.line.biz/en/reference/messaging-api/#issue-link-token)，請向 `/bot/user/{userId}/linkToken` 端點傳送 HTTP POST 請求。

```sh
curl -X POST https://api.line.me/v2/bot/user/{userId}/linkToken \
-H 'Authorization: Bearer {channel access token}'
```

若請求成功，該端點會回傳狀態碼 `200` 及一個連結權杖。此權杖僅供一次性使用，且有效期間為 10 分鐘。

```sh
{
  "linkToken": "NMZTNuVrPTqlr2IF8Bnymkb7rXfYv5EY"
}
```

### 2. Send the linking URL to the user 

您的 bot 伺服器會傳送一個供使用者連結帳號的 URL。舉例來說，此連結用 URL 可指定在[範本訊息（template message）](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)的 [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action) 物件中。在此連結用 URL 中，加上一個帶有步驟 1 連結權杖的查詢參數。

以下是一個傳送帶有連結用 URL 訊息給使用者的請求範例。

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": "{user id}",
    "messages": [{
        "type": "template",
        "altText": "Account Link",
        "template": {
            "type": "buttons",
            "text": "Account Link",
            "actions": [{
                "type": "uri",
                "label": "Account Link",
                "uri": "http://example.com/link?linkToken=xxx"
            }]
        }
    }]
}'
```

### 3. Get the user's ID of your service 

當使用者存取該 URL 時，向使用者顯示您服務的登入頁面。當使用者登入您的服務時，您便能取得使用者在您服務的 user ID。

### 4. Generate a nonce and redirect the user to the LINE Platform 

使用步驟 3 取得的 user ID 產生一個 nonce。此 nonce 必須：

- 是一個僅供單次使用且難以預測的字串。為了安全起見，請勿使用可預測的值，例如您服務中所使用的 user ID。
- 長度介於 10 至 255 個字元之間。

在為 nonce 產生隨機值時，請考量以下建議：

- 使用安全的亂數產生器來產生 nonce。
- 讓 nonce 至少有 128 位元（16 位元組）長。
- 將 nonce 以 Base64 編碼。

產生 nonce 後，將該 nonce 與您服務的 user ID 連結，並儲存這些資訊。接著將使用者重新導向至下方 URL。

```sh
https://access.line.me/dialog/bot/accountLink?linkToken={link token}&nonce={nonce}
```

當使用者存取此端點時，LINE Platform 會檢查該使用者是否即為連結權杖所核發的對象使用者。根據驗證結果，LINE Platform 會有如下不同的處理方式。

- 使用者驗證成功：LINE Platform 會傳送一個[帳號連結事件（account link event）](https://developers.line.biz/en/reference/messaging-api/#account-link-event)給您的 bot 伺服器。該事件的 `result` 屬性值為 `ok`。
- 使用者驗證失敗：LINE Platform 會傳送一個[帳號連結事件](https://developers.line.biz/en/reference/messaging-api/#account-link-event)給您的 bot 伺服器。該事件的 `result` 屬性值為 `failed`。
- 連結權杖無效：若連結權杖已過期或先前已被使用，LINE Platform 不會傳送任何 webhook 事件，並會向使用者顯示錯誤。

### 5. Linking accounts 

若步驟 4 的使用者驗證成功，請連結使用者的帳號。帳號連結事件物件包含使用者的 LINE user ID 與 nonce。使用此 nonce 取得您稍早連結並儲存的、使用者在您服務的 user ID。當您將使用者在您服務的 user ID 連結至使用者的 LINE user ID 時，帳號連結即完成。

## Unlinking accounts 

若使用者已將其 LINE 帳號連結至您的服務帳號，您必須允許使用者解除帳號連結：

- 您必須讓使用者隨時都能解除帳號連結。
- 您必須在連結帳號的當下告知使用者，他們可以解除帳號連結。

舉例來說，Messaging API 讓您能依使用者自訂[圖文選單（rich menus）](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/)。您可以對尚未連結帳號的使用者顯示連結帳號的選單；同樣地，您也可以對已連結帳號的使用者顯示解除帳號連結的選單。

## Learn more 

- [Messaging API reference](https://developers.line.biz/en/reference/messaging-api/)
- [New customer experiences enabled by ID integration using the LINE API (LINE DATA SOLUTION)](https://data.linebiz.com/contents/column/line_api)（僅提供日文版）
