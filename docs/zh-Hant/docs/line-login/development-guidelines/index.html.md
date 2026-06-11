# LINE Login 開發指引（LINE Login development guidelines）

當您使用 LINE Login 開發 web 應用程式時，請遵循以下開發指引。

**禁止事項**

- [禁止對 LINE Platform 發送大量請求](https://developers.line.biz/en/docs/line-login/development-guidelines/#prohibiting-mass-requests-to-line-platform)

**必要事項**

- [當使用者從您的應用程式取消註冊時，請解除應用程式的授權](https://developers.line.biz/en/docs/line-login/development-guidelines/#deauthorize)

**建議事項**

- [儲存記錄檔](https://developers.line.biz/en/docs/line-login/development-guidelines/#save-logs)

<!-- note start -->

**注意**

LINE Login 開發的基本規則是依據 [Terms and Policies](https://developers.line.biz/en/terms-and-policies/) 中所述的內容。

<!-- note end -->

## Prohibited matters 

### Prohibiting mass requests to the LINE Platform 

請勿為了負載測試（load testing）的目的，向 LINE Platform 發送大量的[授權請求（authorization request）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)或 [LINE Login API](https://developers.line.biz/en/reference/line-login/) 請求。若要對 web 應用程式進行負載測試，請準備一個不會對 LINE Platform 產生大量請求的測試環境。

<!-- note start -->

**注意**

若超過速率限制（rate limit），將會回傳 `429 Too Many Requests` 並發生錯誤。

<!-- note end -->

## Required matters 

### Deauthorize your app when a user unregisters from your app 

當使用者從整合了 LINE Login 的應用程式（網站、智慧型手機應用程式等）取消註冊，或當使用者終止您的應用程式與 LINE 應用程式之間的連結時，您必須執行以下事項：

1. 必須代表使用者，使用[解除使用者已授予權限的應用程式之授權](https://developers.line.biz/en/reference/line-login/#deauthorize)端點（endpoint），解除使用者授予給已授權應用程式的權限。
1. 請在相關功能附近，或在使用者於註冊或授權時所同意的條款與條件中，依如下方式說明當使用者從您的應用程式取消註冊或終止您的應用程式與 LINE 應用程式之間的連結時會發生什麼事。
   - 例如：若您取消訂閱本服務，LY Corporation 將會收到您已取消訂閱的通知，且本服務與 LINE 應用程式之間的連結將會被終止。
   - 例如：若您執行此操作，LY Corporation 將會收到通知，且本服務與 LINE 應用程式之間的連結將會被終止。

以下使用情境需要進行解除授權（deauthorization）。

![Steps from linking your account to deauthorize app](https://developers.line.biz/media/line-login/development-guidelines/deauthorize-your-app-en.png)

當使用者以其 LINE 帳號登入整合了 LINE Login 的應用程式，並在頻道（channel）同意畫面上[授權該應用程式](https://developers.line.biz/en/docs/line-login/integrate-line-login/#authorization-process)時，該目標應用程式會出現在 LINE 應用程式的 **設定** > **帳號** > **已授權的應用程式** 中。請解除應用程式的授權，以避免在使用者從您的應用程式取消註冊後，權限仍維持在已授權的狀態。

如需更多關於使用者如何解除其授予給應用程式之權限的相關資訊，請參閱 LINE Login 文件中的 [Managing authorized apps](https://developers.line.biz/en/docs/line-login/managing-authorized-apps/)。

## Recommended matters 

### Saving logs 

我們建議將[授權請求（Authorization request）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)與 [LINE Login API](https://developers.line.biz/en/reference/line-login/) 請求的記錄檔儲存一段時間，以便當問題發生時，開發者本身能夠順利地調查問題的原因與影響範圍。

#### Authorization request logs 

我們建議在發出[授權請求（Authorization request）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)時，將以下資訊儲存為記錄檔。

- 發出授權請求的時間
- 授權請求的參數

更具體地說，請使用以下格式將其儲存於記錄檔中。

| 發出授權請求的時間 | 授權請求的參數 |
| --- | --- |
| Mon, 16 Jul 2021 10:20:10 GMT | `https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=xxxxxxxxxx...` |

#### Authorization code or error response 

我們建議在透過[授權請求（Authorization request）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)收到[授權碼（Authorization code）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code)或[錯誤回應（Error response）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-an-error-response)時，將以下資訊儲存為記錄檔。

- 收到授權碼或錯誤回應的時間
- 請求方法（Request method）
- 授權碼或錯誤回應的記錄

更具體地說，請使用以下格式將其儲存於記錄檔中。

| 收到回應的時間 | 請求方法 | 授權碼或錯誤回應的記錄 |
| --- | --- | --- |
| Mon, 16 Jul 2021 10:20:20 GMT | GET | `/callback?code=Zfl2WjsWcn2XBBWApcty&state=n5B9b9FR2BWjloDzEskZMmGysITRTYpjLkM6oD5qfmA` |

#### Time logs for LINE Login API request 

我們建議在發出 [LINE Login API](https://developers.line.biz/en/reference/line-login/) 請求時，將以下資訊儲存為記錄檔。

- [回應標頭（Response headers）](https://developers.line.biz/en/reference/line-login/#response-headers)的請求 ID（`x-line-request-id`）
- 發出 API 請求的時間
- 請求方法（Request method）
- API 端點（endpoint）
- LINE Platform 回傳的[狀態碼（Status codes）](https://developers.line.biz/en/reference/line-login/#status-codes)

更具體地說，請使用以下格式將其儲存於記錄檔中。

| 請求 ID（`x-line-request-id`） | 發出 API 請求的時間 | 請求方法 | API 端點 | 狀態碼 |
| --- | --- | --- | --- | --- |
| 8d48c8577e739b9c | Mon, 16 Jul 2021 10:20:22 GMT | POST | `https://api.line.me/oauth2/v2.1/token` | 200 |

<!-- tip start -->

**建議保留於記錄檔中、且會有所助益的額外資訊**

依照您所執行的 web 應用程式之需求，除了上述資訊之外，也可以儲存以下資訊，以便在問題發生時進行調查。

- LINE Login API 請求主體（request body）
- API 請求後 LINE Platform 回傳的回應主體（Response body）

<!-- tip end -->

<!-- note start -->

**我們不提供記錄檔**

即使收到詢問，我們也不會提供授權請求的記錄檔或 LINE Login API 請求的記錄檔等。記錄檔應由使用 LINE Login 開發 web 應用程式的開發者自行儲存。

<!-- note end -->
