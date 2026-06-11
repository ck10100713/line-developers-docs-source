# 整合應用程式內購買（in-app purchase）功能

本頁說明如何將應用程式內購買（in-app purchase）功能整合至您的 LINE MINI App。

## Preparation 

在開始實作前，請先確認以下事項：

- 您的 LINE MINI App 已以已驗證 MINI App（verified MINI App）形式發布，或者若為未驗證 MINI App（unverified MINI App），則 Developing 用的頻道（channel）可供使用。
- 您[使用應用程式內購買功能的申請](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/request-iap-review/)已獲核准。
- 您的 LINE MINI App 已備妥伺服器。
- 已備妥 Webhook 端點（endpoint）（webhook URL）。（\*）

\* 請在您使用應用程式內購買的申請獲核准後，於 [LINE Developers Console](https://developers.line.biz/console/) 上註冊 webhook URL。有關註冊方式的詳細資訊，請參閱 [Register the webhook URL](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/#register-webhook-url)。

## Implementation flow 

請依以下流程整合應用程式內購買：

1. [確認您的環境是否相容於應用程式內購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#check-the-environment)
1. [取得可購買項目的相關資訊](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#get-item-information)
1. [取得使用者對應用程式內購買的同意](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#get-user-consent)
1. [從您的 LINE MINI App 伺服器預約購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#reserve-payment)
1. [在商店啟動購買交易](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#start-transaction)
1. [接收 webhook 並處理購買完成](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#receive-webhook)

### 1. Check if your environment is compatible with in-app purchase 

呼叫 [`liff.isApiAvailable()`](https://developers.line.biz/en/reference/liff/#is-api-available) 方法，以判斷您的環境是否支援應用程式內購買。

```javascript
liff.isApiAvailable("iap");
```

若使用者使用的是外部瀏覽器，或使用者所用的 LINE app 版本不支援應用程式內購買，請停用該 LINE MINI App 或隱藏購買流程。

即使您透過 `liff.isApiAvailable()` 方法確認環境支援應用程式內購買，但若無法在「[3. 取得使用者對應用程式內購買的同意](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#get-user-consent)」中取得使用者同意，或之後同意遭撤銷，則仍無法使用應用程式內購買。

### 2. Get information about purchasable items 

取得並向使用者顯示可購買項目的相關資訊。

可透過應用程式內購買購買的項目，是由 LY Corporation 以日圓為基準預先定義的。在向使用者顯示可透過應用程式內購買購買的項目時，請使用依使用者所用 app 商店所在地區在地化（localized）後的價格與幣值，以避免損害使用者體驗。

在這些預先定義的項目中，您的 LINE MINI App 所支援的項目可依使用應用程式內購買之服務供應商的政策來決定。請呼叫 [`liff.iap.getPlatformProducts()`](https://developers.line.biz/en/reference/line-mini-app/#get-platform-products) 方法，以取得這些項目在地化後的價格、幣別與項目名稱。

```javascript
const productIds = ["iap_ln_002", "iap_ln_003"];
await liff.iap.getPlatformProducts({ productIds });
```

範例：

```json
{
  "iap_ln_002": {
    "currency": "JPY",
    "price": 100,
    "productName": "LINE Purchase 100"
  },
  "iap_ln_003": {
    "currency": "JPY",
    "price": 150,
    "productName": "LINE Purchase 150"
  }
}
```

### 3. Obtain user consent for in-app purchase 

請使用 [`liff.iap.requestConsentAgreement()`](https://developers.line.biz/en/reference/line-mini-app/#request-consent-agreement) 方法，取得使用者對「[Terms of Use: LINE In-App Purchase System](https://terms.line.me/line_iap_tou_1?lang=en)」的同意。

```javascript
await liff.iap.requestConsentAgreement();
```

此程序須以每位使用者為單位完成一次，而非以每個 LINE MINI App 為單位。若使用者已在其他 LINE MINI App 同意使用應用程式內購買，則不需要再次同意。若目前執行中的 LINE MINI App 已取得同意，同樣不需要再次同意。

不過，若「Terms of Use: LINE In-App Purchase System」有更新，使用者可能需要再次提供同意。尚未提供同意的使用者無法預約或啟動購買。因此，在開始應用程式內購買時，您應一律呼叫 `liff.iap.requestConsentAgreement()` 方法，以確認最新的同意狀態。

當執行 `liff.iap.requestConsentAgreement()` 方法時，若使用者尚未完成同意且需要新的同意，此時便會顯示同意畫面。為避免因顯示同意畫面而造成使用者流失，建議您在適當的時機請求同意。

### 4. Reserve a purchase from your LINE MINI App server 

在於 app 商店（App Store、Google Play）啟動購買交易之前，請使用「[Reserve purchase](https://developers.line.biz/en/reference/line-mini-app/#reserve-purchase)」端點，從您的 LINE MINI App 伺服器預約購買。

請在適當的時機從您的 LINE MINI App 伺服器進行購買預約，例如當使用者在您的 LINE MINI App 中點擊某項目的購買按鈕時。

取得購買預約所需的附加參數：

- 認證時的存取權杖（access token），請指定由 [`liff.getAccessToken()`](https://developers.line.biz/en/reference/liff/#get-access-token) 方法所取得的值。
- `clientIp` 請指定從您的 LINE MINI App 伺服器取得的使用者 IP 位址。
- `clientOs` 請指定由 [`liff.getOS()`](https://developers.line.biz/en/reference/liff/#get-os) 方法所取得的值。

<!-- note start -->

**存取權杖的有效期間（Access token validity period）**

存取權杖自發行後有效 12 小時。不過，即使在此有效期間（validity period）內，存取權杖仍可能因使用者的操作而遭撤銷（revoke）。因此，請留意您取得存取權杖的時機。

- 當使用者關閉 LINE MINI App 時，存取權杖可能遭撤銷。詳細資訊請參閱 LIFF 文件中的 [Behavior when closing the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#behavior-when-closing-liff-app)。
- 當啟用「[Channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#what-is-channel-consent-simplification)」功能時，從驗證畫面授予額外權限會刷新存取權杖，並撤銷先前發行的存取權杖。詳細資訊請參閱 [Request permissions other than the `openid` scope on the verification screen](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

<!-- note end -->

此時，購買尚未完成。例如，即使購買預約成功，若使用者之後離開 LINE MINI App 或在 app 商店中取消購買交易，實際的購買仍不會完成。

可從購買預約時的回應取得的訂單 ID（`orderId` 值），也會作為參數包含在付款完成時 LINE Platform 所傳送的 webhook 中。請將 `orderId` 值記錄於日誌或儲存空間中，因為在向 LY Corporation 洽詢或進行調查時將會需要它。

此外，請記錄回應中所包含的 `x-line-request-id` 標頭（header）的值，並連同 `orderId` 值與我們聯絡。

### 5. Start the purchase transaction at the store 

完成購買預約後，請從您的 LINE MINI App 啟動 [app 商店付款](https://developers.line.biz/en/reference/line-mini-app/#create-payment)。

```javascript
await liff.iap.createPayment({
  productId,
  orderId,
});
```

當購買交易成功時，LINE Platform 會與商店核對，以驗證付款是否正確完成。當付款經驗證為正確時，LINE Platform 會將購買完成的 webhook 事件通知至 webhook 端點。有關將被通知之 webhook 事件的詳細資訊，請參閱 LINE MINI App API 參考文件中的 [Purchase complete event](https://developers.line.biz/en/reference/line-mini-app/#purchase-complete-event)。

若購買被取消或購買交易失敗，將會擲出例外（exception）。請視需要實作錯誤處理。

```javascript
try {
  await liff.iap.createPayment({
    productId,
    orderId,
  });
} catch (e) {
  // e => { code: "CANCELED", message: "Transaction was canceled." }
  console.error({
    code: e.code,
    message: e.message,
  });
}
```

### 6. Receive webhook and process purchase completion 

當您收到 LINE Platform 所通知的[購買完成](https://developers.line.biz/en/reference/line-mini-app/#purchase-complete-event) webhook 事件時，請在您的 LINE MINI App 伺服器上檢查內容，並將項目授予使用者。如何將項目授予使用者的具體實作方式，取決於所開發 LINE MINI App 的實作。

由於 webhook 事件的特性，同一事件可能因網路或應用程式錯誤而被通知多次。此外，即使 LINE MINI App 伺服器正確接收了某個特定的購買完成事件，若 LINE Platform 無法確認該事件已被接收，同一事件仍可能被重新通知。

每筆使用者購買都會被指派一個於[購買預約](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#reserve-payment)時發行的唯一 `orderId`。請使用 `orderId` 來判斷該交易是否已經處理過。此外，每筆購買僅授予項目一次。

請務必一律以 webhook 事件為依據來判斷購買是否完成。

#### Verify the webhook signature 

為防止偽造的請求，在接收 webhook 時請使用 `x-line-signature` 請求標頭驗證簽章。詳細資訊請參閱 [Verify the webhook signature](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/#verify-webhook-signature)。

#### Response to webhook 

LINE Platform 不會驗證 LINE MINI App 伺服器回應的內容，因此伺服器可回傳任意 payload。

不過，若伺服器成功接收 webhook，則必須回傳 2xx 範圍內的狀態碼。

若回傳任何其他狀態碼（例如 3xx、4xx、5xx），LINE Platform 會將該請求視為失敗，並嘗試重新傳送 webhook。重新傳送會在 30 分鐘內進行多次。

#### Get webhook event history 

您可以使用「[Get webhook event history](https://developers.line.biz/en/reference/line-mini-app/#webhook-events-history)」端點，擷取先前所傳送的 webhook 事件歷史。

若您需要對接收失敗的 webhook 事件進行復原（recovery），請使用此端點。

詳細資訊請參閱 LINE MINI App API 參考文件中的 [Get webhook event history](https://developers.line.biz/en/reference/line-mini-app/#webhook-events-history)。

## Test payment guide 

在將應用程式內購買功能整合至您的 LINE MINI App 後，便可在 LINE MINI App 的 Developing 用頻道中使用測試付款（test payments）。透過測試付款，您可以在 LINE MINI App 上驗證一連串的操作，例如購買項目與[查看購買歷史](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#purchase-history)。

當具備測試者（tester）權限的帳號在 Developing 頻道中執行付款流程時，系統會將其視為測試付款，讓您可以在不實際執行扣款的情況下測試付款流程。

執行測試付款的使用者必須符合以下所有條件：

- 擁有[相關 LINE MINI App 頻道的 Admin 或 Tester 角色](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#channel-permission)
- 擁有[測試付款功能的測試者權限](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#tester-permission)

### LINE MINI App channel roles 

若要使用 LINE MINI App 的測試付款功能，您需要該 LINE MINI App 頻道的 Admin 角色或 Tester 角色。請在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Role settings** 分頁中設定權限。

有關角色設定方式的詳細資訊，請參閱 LINE Developers Console 文件中的 [Adding developers, editing roles, and deleting developers on channel](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#role-settings-for-channel)。

請注意，只有具備頻道 Admin 角色的開發人員才能新增或編輯頻道角色。有關各角色差異的詳細資訊，請參閱 LINE Developers Console 文件中的 [LINE MINI App channel](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel-line-mini-app)。

### Tester permissions for the test payment feature 

測試付款功能的測試者權限，可授予具備相關 LINE MINI App 頻道 Admin 角色或 Tester 角色的開發人員。請在 LINE Developers Console 上 **In-app purchase** 分頁內的 **In-app purchase setup** 分頁中設定測試者權限。

有關權限設定方式的詳細資訊，請參閱 [Register testers](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/#register-testers)。

### Test payment procedure

透過測試付款，您可以在不處理實際付款的情況下驗證行為。

測試程序如下：

1. 在相關的 LINE MINI App 頻道中[註冊測試者](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/#register-testers)。
1. 將 Developing 用 LINE MINI App 的 LIFF URL 分享給測試者。LIFF URL 可於 LINE Developers Console 的 **Web app settings** 分頁中確認。
1. 測試者從指定的 LIFF URL 啟動 LINE MINI App 並執行付款。

## Production operation checklist 

在正式環境（production）中營運應用程式內購買服務時，請檢查以下事項。

### User notification on successful payment 

當付款完成時，LY Corporation 會從 LINE 官方帳號「LINEアプリ内課金お知らせ」（日文，意即 LINE In-App Purchase Notification）向進行購買的使用者自動傳送一則訊息。因此，開發人員端不需要採取任何額外動作。

使用者無法封鎖此帳號或變更通知設定。不過，在極少數情況下，通知可能會因使用者的使用環境或伺服器狀況而無法送達，敬請見諒。

### How users check purchase history 

使用者可以透過開啟 LINE app「設定」畫面中的 **In-app purchases**，或透過 LINE 官方帳號「LINEアプリ内課金お知らせ」所傳送的訊息，來查看應用程式內購買歷史。可確認最長一年內的購買歷史。

在下方顯示的「In-App Purchases」畫面中，紅框區段內的值反映的是[申請使用應用程式內購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/request-iap-review/)時、[購買預約請求](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#reserve-payment)時，或使用者於商店購買時的實際價格與幣別。

![](https://developers.line.biz/media/line-mini-app/in-app-purchase/purchase-history-en.png)

| 編號 | 詳細說明 |
| --- | --- |
| 1 | 原樣顯示購買預約時所指定的項目名稱（[`shopProductName`](https://developers.line.biz/en/reference/line-mini-app/#reserve-purchase-request-body)）。請設定適當的值，讓使用者能辨識自己所購買的項目。 |
| 2 | 顯示 LY Corporation 使用應用程式內購買之服務的名稱，以及使用應用程式內購買之服務供應商的服務名稱。請注意，服務供應商的服務名稱目前尚未提供多語言版本。<br><ul><li>當語言設定為日文時：`LINEミニアプリ <服務供應商的服務名稱>`</li><li>其他情況：`LINE MINI App <服務供應商的服務名稱>`</li></ul> |
| 3 | 顯示與 app 商店相關的資訊，包括付款使用的是哪個 app 商店（App Store 或 Google Play），以及在該 app 商店中註冊的項目名稱。 |
| 4 | 顯示付款時間，即在商店處理付款後 LINE Platform 確認付款的時間。 |
| 5 | 顯示付款當下的幣別與價格。在 app 商店付款流程中，會依使用者所用 app 商店所在地區換算幣別，並顯示實際支付的幣別與價格。 |
