# 傳送服務訊息（service messages）

<!-- tip start -->

**此功能僅適用於已驗證的 MINI App**

此功能僅適用於已驗證的 MINI App。對於未驗證的 MINI App，你可以在 Developing 的內部頻道（channel）上測試此功能，但無法在 Published 的內部頻道上使用此功能。

<!-- tip end -->

服務訊息（service messages）是 LINE MINI App 的一項功能，可讓你針對使用者在 LINE MINI App 上的特定動作，以回應或確認的形式通知使用者其應知道的資訊。舉例來說，如果使用者在 LINE MINI App 上預約了餐廳或住宿，針對單一預約動作，你最多可以傳送 5 則服務訊息，例如預約完成通知或前一天的提醒。

![LINE MINI App Notice](https://developers.line.biz/media/line-mini-app/mini-service-messages-en.png)

<!-- note start -->

**傳送服務訊息的條件**

你只能以針對使用者在 LINE MINI App 上動作的確認或回應形式來傳送服務訊息。禁止傳送廣告與活動通知，包括折扣、購物回饋、新產品、折扣優惠券或促銷等資訊。如需更多關於服務訊息條件的資訊，請參閱 [Conditions for service messages](https://developers.line.biz/en/docs/line-mini-app/service/service-operation/#conditions-for-service-messages)。

<!-- note end -->

## Chat room where service messages are displayed 

從 LINE MINI App 傳送的服務訊息，無論 LINE MINI App 的類型為何，都會顯示在為各個提供 LINE MINI App 的地區所決定的聊天室中。

| Japan | Thailand | Taiwan |
| :-: | :-: | :-: |
| LINEミニアプリ お知らせ | LINE MINI App Notice | LINE MINI App 通知 |
| ![LINEミニアプリ お知らせ](https://developers.line.biz/media/line-mini-app/mini_service_notifier_jp.png) | ![LINE MINI App Notice](https://developers.line.biz/media/line-mini-app/mini_service_notifier_th.png) | ![LINE MINI App 通知](https://developers.line.biz/media/line-mini-app/mini_service_notifier_tw.png) |

## Types of service messages that can be sent 

你可以使用提供的範本（templates）來傳送服務訊息。這些範本依類別整理，例如店家預約、排隊管理與配送通知，並提供六種語言：日文、英文、繁體中文、泰文、印尼文與韓文。你可以在 [LINE Developers Console](https://developers.line.biz/console/) 中檢視這些範本。

![You can check service message templates in the console](https://developers.line.biz/media/line-mini-app/service-message-template-en.png)

## Preview service messages 

在 [LINE Developers Console](https://developers.line.biz/console/) 中選取 LINE MINI App 頻道，接著在 **Service message template** 分頁中點擊 **Add**，以顯示「Add service message template」畫面。

在此畫面中，你可以透過選取範本並編輯 JSON 來預覽訊息並傳送測試訊息。測試訊息會傳送至目前登入 LINE Developers Console 的使用者其 LINE 開發者帳號所關聯的 LINE 帳號。

![Changes to JSON are reflected in the preview](https://developers.line.biz/media/line-mini-app/preview-service-message-en.png)

## Flow of sending a service message 

若要傳送服務訊息，你需要一個服務訊息範本與一個服務通知權杖（service notification token）。請依照下列步驟傳送：

1. 在 LINE Developers Console 中，將[服務訊息範本新增](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#service-message-templates)至 LINE MINI App 頻道。
2. 根據使用者在 LINE MINI App 上的動作，[發行服務通知權杖並傳送服務訊息](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#sending-service-messages-for-the-first-time)。
3. 使用步驟 2 所發行的新服務通知權杖來[傳送後續的服務訊息](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#sending-subsequent-service-messages)，例如提醒訊息。

<!-- note start -->

**你需要通過審查**

步驟 1 中新增至 LINE MINI App 頻道的服務訊息範本，必須通過 LY Corporation 的審查，才能搭配 [Sending service messages API](https://developers.line.biz/en/reference/line-mini-app/#send-service-message) 使用。

<!-- note end -->

## Adding service message templates to the channel 

從 LY Corporation 提供的範本中，選取一個要搭配 [Service Message API](https://developers.line.biz/en/reference/line-mini-app/#service-messages) 使用的範本，並將其新增至 LINE MINI App 頻道。每個 LINE MINI App 頻道最多可設定 20 個服務訊息範本。

範本依類別提供，你可以在 [LINE Developers Console](https://developers.line.biz/console/) 中找到它們。你也可以傳送測試訊息至自己的 LINE 帳號，以檢視服務訊息的預覽。若要將服務訊息範本新增至頻道，請依照下列步驟操作：

1. 在 [LINE Developers Console](https://developers.line.biz/console/) 中，選取要新增範本的 LINE MINI App 頻道，並點擊 **Service message template** 分頁。

<!-- note start -->

**Note**

1. 你可以在開發頻道的同時準備正式範本（official template）。<br />

- **在此期間，你可以：**
  - 新增範本
  - 檢視所有範本的清單
  - 檢視範本詳細資訊
  - 編輯範本的 `use case`
  - 刪除範本
  - 傳送可在模擬器中使用的測試訊息

2. 當審查進行中時，正式範本的使用會受到一些限制。

- **在此期間，你仍然可以：**
  - 檢視所有範本的清單
  - 傳送可在模擬器中使用的測試訊息
  - 檢視範本詳細資訊
- **然而在此階段，你「無法」：**
  - 新增範本
  - 編輯範本的 `use case`
  - 刪除範本

3. 一旦頻道發布後，你就可以在已發布的頻道上使用正式範本（與 #1 的準備階段適用相同的條件）。

當你的頻道正在審查中時，你無法新增範本。在你的頻道通過審查之前，你只能傳送可在模擬器中使用的測試訊息。不過，審查程序不會影響過去已成功新增的既有範本。

<!-- note end -->

2. 點擊 [**Add**]。

3. 設定下列項目：

   | Item | Description |
   | --- | --- |
   | Select template | 選取要搭配 Service Message API 使用的範本。 |
   | Template detail | 將顯示所選範本的詳細資訊。執行[傳送服務訊息的 API](https://developers.line.biz/en/reference/line-mini-app/#send-service-message) 時，請將 [**Template name for API use**] 中所顯示的字串（`{template name}_{BCP 47 language tag}`）指定為 `templateName`。 |
   | Preview | 將顯示測試訊息的預覽。當你從 [**Send test message**] 點擊 [**Send**] 時，測試訊息會傳送至登入 LINE Developers Console 的 LINE 帳號。 |
   | Send test message | 輸入指定範本變數與值配對的 JSON 物件。[**Preview**] 會隨你的輸入而更新。<ul><li>[**Copy**]：將 JSON 物件複製到剪貼簿。</li><li>[**Reset**]：捨棄對 JSON 物件的編輯。</li><li>[**Send**]：將測試訊息傳送至登入 LINE Developers Console 的 LINE 帳號。</li></ul> |
   | Use Case | 輸入範本確切的使用情境（use case）。 |

   <!-- note start -->

   **Note**

   如果你以偏離在 [**Use Case**] 中所輸入說明的方式使用範本，我們可能會禁止你使用該範本。

   <!-- note end -->

4. 點擊 [**Add**]。

   返回服務訊息範本清單。

   審查狀態會顯示在所新增範本的 [**Published status**] 中。

   | Published status | Description |
   | --- | --- |
   | DEVELOPING | 開發中（尚未提出審查請求）。此功能僅可從已準備好發布的頻道，[傳送服務訊息](https://developers.line.biz/en/reference/line-mini-app/#send-service-message)給在 LINE MINI App 頻道上具有 Admin 或 Tester 權限的開發者。 |
   | PUBLISHING | 已通過審查。用於從正式（production）頻道[傳送服務訊息](https://developers.line.biz/en/reference/line-mini-app/#send-service-message)給 LINE MINI App 頻道的使用者。 |

### Template elements 

一則服務訊息由 (A) title、(B) detail、(C) button 與 (D) footer 組成。請根據使用情境組合這些區塊來建立範本。選擇最符合你服務訊息目的的範本。

![](https://developers.line.biz/media/line-mini-app/mini_servicenotifier_layout.png)

| Label | Section | Description |
| --- | --- | --- |
| A | Title | title 區塊由下列元素組成。<ul><li>Title (A-1)</li><li>Subtitle (A-2)</li></ul> |
| B | Detail | detail 區塊依範本類型有兩種不同的版面配置：<ul><li>「detailed」：需要一個鍵（key）。鍵的最大數量取決於你所選取的範本。如需更多關於字元計算的資訊，請參閱 [Maximum number of characters for each element](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#maximum-number-of-characters)。<br />![](https://developers.line.biz/media/line-mini-app/mini_detail_detailed.png)</li><li>「simple」：你最多可以選取一個鍵。如需更多關於字元計算的資訊，請參閱 [Maximum number of characters for each element](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#maximum-number-of-characters)。<br />![](https://developers.line.biz/media/line-mini-app/mini_detail_simple.png)</li></ul> |
| C | Button | 你可以使用的按鈕數量依範本而異。此外，只有設定了 URL 的按鈕才會顯示。請將你 LINE MINI App 頁面的[永久連結（Permanent link）](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)指定為 URL。<ul><li>第一個按鈕為必填，並會顯示為訊息中的第一個連結。</li><li>第二個（及之後的）按鈕為選填，並會根據你所選取的範本而預先定義。</li></ul> |
| D | Footer | 會顯示在 **Basic settings** 分頁中於 **Channel icon** 所設定的圖示，以及於 **Channel Name** 所設定的頻道名稱。當使用者點選 footer 時，會顯示你的 LINE MINI App 首頁。 |

<!-- note start -->

**當你的 LINE MINI App 狀態不是「Reflected」時的 footer**

如果你的 LINE MINI App 狀態為「Not yet reviewed」或「Reviewing」，則會顯示 LINE 圖示與文字「Service Message」，而非原本的 footer。一旦狀態變更為「Reflected」，就會顯示你所設定的 LINE MINI App 圖示與 LINE MINI App 名稱。

<!-- note end -->

### Maximum number of characters for each element 

在 detail 區塊中，「detailed」與「simple」各有每個鍵值的建議字元數與最大字元數（soft limit 與 hard limit）。

| Item         | Recommended number of characters | Soft limit | Hard limit |
| ------------ | -------------------------------- | ---------- | ---------- |
| **detailed** | 10                               | 36         | 50         |
| **simple**   | 32                               | 100        | 150        |

我們建議將每個鍵的值限制在建議字元數以內。如果超過建議字元數，超出可顯示區域的字元會被省略號（`...`）取代，或是無法傳送該服務訊息。

| Number of characters | How the text is displayed |
| --- | --- |
| 建議字元數以內 | 所有文字都會顯示 |
| 大於建議字元數，且在 soft limit 以內 | 超出可顯示區域的字元「可能」被省略號（`...`）取代 |
| 大於 soft limit，且在 hard limit 以內 | 超出可顯示區域的字元會被省略號（`...`）取代 |
| 大於 hard limit | 因發生錯誤而無法傳送服務訊息 |

鍵值的字元數是以[字素叢集（grapheme cluster）](https://unicode.org/reports/tr29/)為單位計算，而非以 UTF-16 碼元為單位。如需更多關於文字字元計算的資訊，請參閱 Messaging API 文件中的 [Character counting in a text](https://developers.line.biz/en/docs/messaging-api/text-character-count/)。

## Sending service messages for the first time 

以下是在使用者動作後，第一次從 LINE MINI App 傳送服務訊息的步驟：

這是一張圖示說明，展示如何使用頻道存取權杖（channel access token）以及透過 [liff.getAccessToken()](https://developers.line.biz/en/reference/liff/#get-access-token) 取得的存取權杖（以下稱「LIFF access token」），來發行服務通知權杖以傳送服務訊息。在此圖中，頻道存取權杖使用的是[無狀態頻道存取權杖（stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)。

<!-- note start -->

**建議使用無狀態頻道存取權杖**

[長期頻道存取權杖（long-lived channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)與[由使用者指定有效期間的頻道存取權杖（Channel Access Token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)無法用於 LINE MINI App 頻道。

開發 LINE MINI App 時，可以使用[無狀態頻道存取權杖（stateless channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)或[短期頻道存取權杖（short-lived channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)。在這兩者之中，建議使用無狀態頻道存取權杖。無狀態頻道存取權杖的發行次數沒有限制，因此應用程式無須管理權杖的生命週期。

<!-- note end -->

![relationship of tokens](https://developers.line.biz/media/line-mini-app/mini-illust-01-en.png)

1. 通知時，在 LINE MINI App 中呼叫 [liff.getAccessToken()](https://developers.line.biz/en/reference/liff/#get-access-token) 以取得 LIFF access token。

1. 將步驟 1 取得的 LIFF access token 傳送至伺服器。

1. 取得[頻道存取權杖（channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/)。

1. [發行服務通知權杖](https://developers.line.biz/en/reference/line-mini-app/#issue-notification-token)。

   會使用步驟 3 取得的頻道存取權杖與步驟 1 取得的 LIFF access token。

   ```java
   final OkHttpClient notifierApiClient = new OkHttpClient().newBuilder().build();
   final MediaType mediaType = MediaType.parse("application/json");
   final RequestBody notificationTokenRequestBody = RequestBody.create(mediaType, "{'liffAccessToken': 'eyJhbGciOiJIUzI1NiJ9…​'");
   final Request notificationTokenRequest = new Request.Builder()
     .url(BASE_URL + "/notifier/token")
     .method("POST", notificationTokenRequestBody)
     .addHeader("Content-Type", "application/json")
     .addHeader("Authorization", "Bearer eyJhbGciOiJIUzI1NiJ9...")
     .build();
   final NotificationTokenResponse response = notifierApiClient.newCall(request).execute();
   String notificationToken = notificationTokenResponse.getNotificationToken();
   int tokenRemainingCount = notificationTokenResponse.getRemainingCount();
   ```

   <!-- note start -->

   **LIFF access token 的有效期間**

   LIFF access token 在發行後 12 小時內有效。然而，即使在此有效期間內，LIFF access token 仍可能因使用者的動作而被撤銷（revoke）。因此，請留意取得 LIFF access token 的時機。
   - 當使用者關閉 LINE MINI App 時，LIFF access token 可能會被撤銷。如需更多資訊，請參閱 LIFF 文件中的 [Behavior when closing the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#behavior-when-closing-liff-app)。
   - 當啟用「[Channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#what-is-channel-consent-simplification)」功能時，從驗證畫面授予額外權限會重新整理 LIFF access token，並撤銷先前所發行的 LIFF access token。如需更多資訊，請參閱 [Request permissions other than the `openid` scope on the verification screen](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

   <!-- note end -->

1. 第一次[傳送服務訊息](https://developers.line.biz/en/reference/line-mini-app/#send-service-message)。

   使用步驟 4 取得的服務通知權杖。傳送服務訊息後，請[儲存回應中所包含的服務通知權杖](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#save-service-notification-token)。

   如果你使用的範本含有範本變數，請在 `params` 中指定鍵值配對。如果你未為必填元素指定範本變數，將會回傳錯誤。

   `params` 範例：

   ```json
   {
     ...
     "params": {
       // params sample to be updated
       "variable-name": "value",
       "button_uri_1": "detailView?userId=1234&purchaseID=5678"
     }
     ...
   }
   ```

   ```java
   final RequestBody notificationRequestBody = RequestBody.create(mediaType,"{
     'templateName': 'reservation_confirmation_en',
     'notificationToken': '34c11a03-b726-49e3-8ce0-949387a9…​',
     'params': {
       'template-field-name': 'field-value',
       'template-field-name': 'field-value',
     }}");
   final Request notificationRequest = new Request.Builder()
     .url(BASE_URL + "/notifier/send?target=service")
     .method("POST", notificationRequestBody)
     .addHeader("Content-Type", "application/json")
     .addHeader("Authorization", "Bearer W1TeHCgfH2Liwa...")
     .build();
   final NotificationResponse notificationResponse = notifierApiClient.newCall(request).execute();
   notificationToken = notificationResponse.getNotificationToken();
   tokenRemainingCount = notificationResponse.getRemainingCount();
   ```

服務通知權杖在發行後 1 年（31,536,000 秒）失效。舉例來說，在有效期間內，針對使用者的單一預約動作，最多可以從 LINE MINI App 傳送 5 則服務訊息。如需更多關於傳送後續服務訊息的資訊，請參閱 [Sending subsequent service messages](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#sending-subsequent-service-messages)。

![AOA flow 2](https://developers.line.biz/media/line-mini-app/mini-illust-03-en.png)

## Sending subsequent service messages 

當你針對同一個使用者動作傳送後續的服務訊息時，請使用你上次[傳送服務訊息](https://developers.line.biz/en/reference/line-mini-app/#send-service-message)時回應中所包含的服務通知權杖。即使是傳送後續的服務訊息，也請[儲存回應中所包含的服務通知權杖](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#save-service-notification-token)。

傳送後續的服務訊息時，請勿重複使用傳送第一則服務訊息時所用的頻道存取權杖與 LIFF access token 來發行服務通知權杖。

```java
...
JsonObject subsequentMessage = Json.createObjectBuilder()
  .add("notificationToken", notificationToken)
  .add("templateName", templateName)
  .add("params", templateData)
  .build();
...

if (tokenRemainingCount < 0)
{
  notificationRequestBody = RequestBody.create(mediaType, subsequentMessage.toString());
  notificationRequest = new Request.Builder()
        .url(BASE_URL + "/notifier/send?target=service")
        .method("POST", notificationRequestBody)
        .addHeader("Content-Type", mediaType.toString())
        .addHeader("Authorization", "Bearer W1TeHCgfH2Liwa...")
        .build();
  notificationResponse =
        notifierApiClient.newCall(notificationRequest).execute();
  notificationToken = notificationResponse.getNotificationToken();
  tokenRemainingCount = notificationResponse.getRemainingCount();
}
```

## Save the service notification token included in the response 

傳送服務訊息後，請保留回應中所包含的已更新服務通知權杖（`notificationToken`）。此服務通知權杖將用於針對同一個使用者動作傳送後續的服務訊息。

只要權杖尚未失效，你針對同一個使用者動作可傳送服務訊息的次數，與回應中所包含的 `remainingCount` 相同。每個使用者動作都可以透過回應中所包含的工作階段 ID（`sessionId`）來識別。
