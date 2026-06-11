# LINE MINI App 開發準則（LINE MINI App development guidelines）

使用 LIFF 開發網頁應用程式時，請遵循下列開發準則。

- [Prohibiting mass requests to the LINE Platform](https://developers.line.biz/en/docs/line-mini-app/development-guidelines/#prohibiting-mass-requests-to-line-platform)
- [Saving logs](https://developers.line.biz/en/docs/line-mini-app/development-guidelines/#save-logs)
- [Deauthorize your app when a user unregisters from your app](https://developers.line.biz/en/docs/line-mini-app/development-guidelines/#deauthorize)

LINE MINI App 使用的是 LIFF 提供的系統。因此，請遵循 LIFF 文件中的 [LIFF app development guidelines](https://developers.line.biz/en/docs/liff/development-guidelines/)。

<!-- note start -->

**Note**

LINE MINI App 開發的基本規則是以 [Terms and Policies](https://developers.line.biz/en/terms-and-policies/) 中所述的內容為依據。

<!-- note end -->

## Prohibiting mass requests to the LINE Platform 

請勿透過 [LIFF scheme](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-a-liff-app)（`https://miniapp.line.me/{liffId}`）過度存取 LINE MINI App，也不要為了負載測試（load testing）而向 [LIFF API](https://developers.line.biz/en/reference/liff/) 或 [Service message API](https://developers.line.biz/en/reference/line-mini-app/) 發送大量請求。若要對 LINE MINI App 進行負載測試，請準備一個不會對 LINE Platform 產生大量請求的測試環境。

<!-- note start -->

**Note**

若超過速率限制（rate limit），將會回傳 `429 Too Many Requests` 並發生錯誤。

<!-- note end -->

## Saving logs 

我們建議將 [Service message API](https://developers.line.biz/en/reference/line-mini-app/) 請求的記錄保存一段時間，以便開發者本身在問題發生時能順利調查其原因與影響範圍。

### Service message API request logs 

在向 [Service message API](https://developers.line.biz/en/reference/line-mini-app/) 發送請求時，除了回應中所包含的[服務通知權杖（service notification token）](https://developers.line.biz/en/reference/line-mini-app/#issue-notification-token-response) `notificationToken` 之外，我們建議將下列資訊也保存在記錄中。

- 發出 API 請求的時間
- 請求方法（request method）
- API 端點（endpoint）
- LINE Platform 回傳的[狀態碼（status codes）](https://developers.line.biz/en/reference/line-mini-app/)

更具體地說，請以下列格式保存在記錄檔中。

| 發出 API 請求的時間 | 請求方法 | API 端點 | 狀態碼 |
| --- | --- | --- | --- |
| Mon, 16 Jul 2021 10:20:23 GMT | POST | `https://api.line.me/message/v3/notifier/send?target=service` | 200 |

<!-- tip start -->

**建議保留在記錄中的其他有用資訊**

視您所執行的 LINE MINI App 的需求而定，除了上述資訊之外，還可以保存下列資訊，以便在問題發生時進行調查。

- Service message API 請求主體（request body）
- API 請求後 LINE Platform 回傳的回應主體（response body），服務通知權杖 `notificationToken` 以外的部分

<!-- tip end -->

<!-- note start -->

**我們不提供記錄**

即使收到詢問，我們也不會提供 service message API 請求等的記錄。記錄應由開發 LINE MINI App 的開發者本身保存。

<!-- note end -->

## Deauthorize your app when a user unregisters from your app 

當使用者取消註冊您的 LINE MINI App，或當使用者終止您的應用程式與 LINE app 之間的連結時，您必須執行下列事項：

1. 必須代表使用者，透過[撤銷使用者已授權的應用程式（Deauthorize your app to which the user has granted permissions）](https://developers.line.biz/en/reference/line-login/#deauthorize)端點，撤銷（deauthorize）使用者已授予該已授權應用程式的權限。
1. 請在功能附近，或在使用者於註冊或授權時所同意的條款與條件中，如下所述地寫明當使用者取消註冊您的應用程式或終止您的應用程式與 LINE app 之間的連結時會發生什麼事。
   - 例如：若您取消訂閱本服務，LY Corporation 將會收到您已取消訂閱的通知，且本服務與 LINE app 之間的連結將被終止。
   - 例如：若您執行此操作，LY Corporation 將會收到通知，且本服務與 LINE app 之間的連結將被終止。

下列使用情境需要撤銷授權。

![Steps from linking your account to deauthorize app](https://developers.line.biz/media/line-login/development-guidelines/deauthorize-your-app-en.png)

當使用者登入將 LINE Login 與其 LINE 帳號整合的應用程式，並在頻道同意畫面上[授權該應用程式（authorize the app）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#authorization-process)時，目標應用程式將會出現在 LINE app 的 **Settings** > **Account** > **Authorized apps** 中。請撤銷該應用程式的授權，以免在使用者取消註冊您的應用程式後權限仍維持授權狀態。

有關使用者如何撤銷其已授予應用程式的權限的詳細資訊，請參閱 LINE Login 文件中的 [Managing authorized apps](https://developers.line.biz/en/docs/line-login/managing-authorized-apps/)。
