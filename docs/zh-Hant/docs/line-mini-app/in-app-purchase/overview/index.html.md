# 應用程式內購買總覽（In-app purchase overview）

本頁說明 LINE MINI App 應用程式內購買（in-app purchase）功能的總覽。

應用程式內購買是一套讓使用者可以在[已驗證的 MINI App（verified MINI Apps）](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#verified-mini-app)內購買數位內容的系統。

這是一項選用功能，若要使用，你必須透過 [LINE Developers Console](https://developers.line.biz/console/) 提出申請並獲得核准。有關如何申請的詳細資訊，請參閱[申請使用應用程式內購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/request-iap-review/)。

## What is in-app purchase 

應用程式內購買是一套讓使用者可以在已驗證的 MINI App 內購買由 LINE MINI App 所提供之數位內容的系統。

目前僅提供可消耗型（consumable）數位內容供購買。

應用程式內購買具有以下特性：

- 使用 App Store 與 Google Play 的付款機制。
- 由 LINE Platform 提供付款驗證與通知功能。
- 使用 LIFF SDK 實作用戶端。
- 透過 Webhook 進行伺服器端整合。

有關實作的詳細資訊，請參閱[整合應用程式內購買功能](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/)。

## Flow to start using in-app purchase 

開始使用應用程式內購買的流程如下。詳細資訊請參閱各份文件。

| 步驟 | 詳細說明 |
| --- | --- |
| 步驟 1：[申請使用應用程式內購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/request-iap-review/) | 在 [LINE Developers Console](https://developers.line.biz/console/) 上你的 LINE MINI App 頻道的 **In-app purchase** 分頁中申請使用。申請時，請正確輸入所有資訊，包括公司名稱。<br>只有已驗證的 LINE MINI App 才能向使用者提供應用程式內購買。不過，即使是未驗證的 MINI App 也可以申請使用應用程式內購買。 |
| 步驟 2：[設定應用程式內購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/) | 當你的應用程式內購買使用申請狀態變為「Approved」後，請在 **In-app purchase** 分頁內的 **In-app purchase settings** 分頁中，註冊用於測試付款的 Webhook URL 與測試人員（testers）。 |
| 步驟 3：將[應用程式內購買整合](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/)至你用於開發（Developing）的 LINE MINI App 頻道，並[執行測試付款](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#test-payment-guide) | 在你用於開發（Developing）的 LINE MINI App 頻道上整合應用程式內購買功能，並執行測試付款。 |
| 步驟 4：[申請驗證審查](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/) | 在 LINE Developers Console 的 **Review request** 分頁中申請審查，以便發布為已驗證的 MINI App。申請時，請開啟 **Review request** 分頁中的 **Release the in-app purchase feature** 切換按鈕。<br>若你是將應用程式內購買整合到一個已發布為已驗證 MINI App 的應用程式中，則需要再次接受審查。 |
| 步驟 5：發布含應用程式內購買的 LINE MINI App | 當步驟 4 的驗證審查獲得核准後，你就可以發布含應用程式內購買的 LINE MINI App。<br />若它原本已是已驗證的 MINI App，則程序有所不同。詳細資訊請參閱[提交 LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)。 |

## System architecture 

應用程式內購買由以下元件組成：

| 元件 | 角色 |
| --- | --- |
| LINE MINI App | 接收使用者動作並啟動購買交易。 |
| LINE MINI App server | 預約購買、接收 Webhook，並管理購買結果。 |
| LINE Platform | 驗證商店付款並傳送 Webhook 事件。 |
| App store | 執行實際的付款交易。<ul><li>iOS：App Store</li><li>Android：Google Play</li></ul> |

## Conditions 

使用應用程式內購買的條件與要求如下。

### In-app purchase use conditions 

該 LINE MINI App 必須在 LINE MINI App 頻道上將「Region to provide the service」與「Company or owner's country or region」皆設定為「Japan」。

### In-app purchase requirements 

- 該 LINE MINI App 為已驗證的 MINI App（\*）
- 該 LINE MINI App 的 LIFF SDK 版本為 2.26.0 或更新版本
- 該 LINE MINI App 在 LIFF 瀏覽器中開啟
- 使用者已在其 LINE 帳號中註冊日本電話號碼
- 使用者的 LINE 版本為 15.6.0 或更新版本

\* 未驗證的 MINI App 僅能在用於開發（Developing）與審查（Review）的 LINE MINI App 上運作。

## Available items and prices 

可透過應用程式內購買購買的項目，已預先定義於 LINE Platform 上。

項目價格以日圓定義。

當向使用者顯示可透過應用程式內購買購買的項目時，你必須以使用者所使用之應用程式商店所在地區的當地貨幣顯示價格，以避免降低使用者體驗。

符合使用者所使用之應用程式商店所在地區的當地化價格，可使用 [`liff.iap.getPlatformProducts()`](https://developers.line.biz/en/reference/line-mini-app/#get-platform-products) 方法取得。使用此方法可將你的 LINE MINI App 中顯示的價格與付款時應用程式商店所顯示的價格之間的差異降到最低。

## In-app purchase cancellation 

LY Corporation 不支援取消使用應用程式內購買完成的付款。對於不當使用或誤付款的情況，請查看 App Store 或 Google Play 等各應用程式商店的最新退款政策，並指示使用者直接申請退款。

- [Request a refund for apps or content that you bought from Apple](https://support.apple.com/en-us/118223)
- [Learn about Google Play refund policies](https://support.google.com/googleplay/answer/2479637?hl=en)

## Example process flow 

基本應用程式內購買處理流程的範例。

![](https://developers.line.biz/media/line-mini-app/in-app-purchase/flow.png)

- 1～5：[確認環境是否與應用程式內購買相容](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#check-the-environment)
- 6～9：[取得可購買項目的清單](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#get-item-information)並向使用者顯示
- 10～13：[取得使用者對使用應用程式內購買的同意](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#get-user-consent)
- 14～21：從你的 LINE MINI App server [預約購買](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#reserve-payment)
- 22～30：在應用程式商店（App Store、Google Play）[啟動購買交易](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#start-transaction)
- 31～36：[接收 Webhook、確認購買完成，並授予項目](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#receive-webhook)
