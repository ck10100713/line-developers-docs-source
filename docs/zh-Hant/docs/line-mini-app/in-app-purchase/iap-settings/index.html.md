# 設定應用程式內購買（Set up in-app purchase）

本頁說明在你的[應用程式內購買使用申請](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/request-iap-review/)獲得核准後，需要設定的項目。

在 LINE MINI App 頻道的 **In-app purchase** 分頁中，你可以[註冊 webhook URL](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/#register-webhook-url)以及[註冊測試人員](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/#register-testers)以進行測試付款。

![](https://developers.line.biz/media/line-mini-app/in-app-purchase/iap-settings-tab-en.png)

<!-- tip start -->

**如果未顯示 In-app purchase settings 分頁**

如果 **In-app purchase** 分頁中沒有出現 **In-app purchase settings** 分頁，表示你的應用程式內購買使用申請尚未獲得核准。

當「Workflow in progress」區塊中的狀態變更為「Approved」後，**In-app purchase settings** 分頁才會顯示出來。請等待你的申請獲得核准。

<!-- tip end -->

## Register the webhook URL 

LINE MINI App 中的應用程式內購買會使用 webhook，在伺服器端即時接收付款狀態的變更（例如付款完成或退款）。

你也可以為 Developing 與 Published 設定相同的 webhook URL。

### Register the webhook URL for the developing 

請依照下列步驟註冊用於開發階段的 webhook URL。當你使用具有測試人員權限的帳號進行測試付款時，付款通知會傳送至開發階段的 webhook URL。

1. 在 LINE Developers Console 中，選擇 **In-app purchase** 分頁，然後選擇 **In-app purchase settings** 分頁。
1. 在 **Webhook URL for developing** 輸入欄位中，輸入要接收通知的伺服器 URL。該 URL 必須以 `https://` 開頭。
1. 點擊 **Update** 按鈕。

### Register the webhook URL for published 

請依照下列步驟設定用於正式發布的 webhook URL：

1. 在 LINE Developers Console 中，選擇 **In-app purchase** 分頁，然後選擇 **In-app purchase settings** 分頁。
1. 在 **Webhook URL for published** 輸入欄位中，輸入要接收通知的伺服器 URL。該 URL 必須以 `https://` 開頭。
1. 點擊 **Update** 按鈕。

## Use the test payment feature 

在將應用程式內購買功能整合到 LINE MINI App 時，你可以使用測試付款功能。測試付款可在 Developing 狀態的 LINE MINI App 頻道中進行。

當具有測試人員權限的帳號在 Developing 頻道中執行付款流程時，系統會將其視為測試付款，讓你能夠在不實際產生帳單的情況下測試付款流程。

若要使用測試付款功能，你需要具備該 LINE MINI App 頻道的測試人員權限。

### Tester permissions for the test payment feature 

測試付款功能的測試人員權限，最多可授予 20 個具有該 LINE MINI App 頻道 Admin 角色或 Tester 角色的帳號。

測試人員權限的有效期間為 30 天。

如需實際測試方法的詳細資訊，請參閱[測試付款指南](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#test-payment-guide)。

#### Register testers 

為測試付款功能註冊測試人員的步驟如下：

1. 在 LINE Developers Console 中，選擇目標 LINE MINI App 頻道。
1. 選擇 **In-app purchase** 分頁，然後點擊 **In-app purchase settings**。
1. 在「Tester permission for the test payment feature」區塊的 **Select a tester** 下拉式清單中，選擇你要註冊的帳號。該下拉式清單會顯示已在 LINE MINI App 頻道 **Roles** 分頁中新增的帳號。
1. 點擊 **Enable** 按鈕。

註冊完成後，清單中會顯示該帳號的名稱、電子郵件地址與到期日。

#### Manage tester permissions 

你可以對已註冊的測試人員執行下列操作：

- 延長權限：點擊清單中的 **Extend** 按鈕，將到期日更新為從該時間點起算的 30 天後。
- 停用權限：點擊清單中的 **Disable** 按鈕，立即禁止該帳號進行測試付款。

如果某測試人員的權限已過期，你可以在 **Select a tester** 下拉式清單中選擇該帳號並再次啟用，以重新啟用其權限。
