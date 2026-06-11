# 管理存取權杖（LINE Login v2.0）（Managing access tokens (LINE Login v2.0)）

<!-- warning start -->

**LINE Login v2.0 已淘汰**

本頁面所包含的是舊版 LINE Login（v2.0）的文件。LINE Login v2.0 已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)，其[終止服務（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)日期尚未確定，因此我們建議您改用目前的版本（LINE Login v2.1）。在終止服務公告與實際終止服務之間，會有一定的緩衝期。詳情請參閱 [LINE Login versions](https://developers.line.biz/en/docs/line-login/overview/#versions)。

<!-- warning end -->

透過 LINE Login API 所管理的存取權杖（access token），可驗證應用程式是否已獲授權，得以存取儲存在 LINE Platform 上的使用者資料（例如使用者 ID、顯示名稱、個人檔案圖片及狀態消息）。

本主題說明如何使用 [LINE Login v2.0](https://developers.line.biz/en/docs/line-login/overview/#versions) 端點（endpoint）來管理存取權杖。

## Get the user's access token 

當使用者驗證完成後，LINE Platform 會回傳一組存取權杖。

此時，您可以假定該應用程式已具備存取使用者資料的權限。

如需深入瞭解，請參閱：

**LINE Login：**

- [Integrating LINE Login (v2.0) with your web app](https://developers.line.biz/en/docs/line-login/integrate-line-login-v2/)

<!-- note start -->

**存取權杖的有效期間**

存取權杖在簽發後 30 天內有效。任何包含存取權杖的回應，也會在 `expires_in` 屬性中包含該權杖到期前的剩餘秒數。

<!-- note end -->

### Refresh tokens 

當使用者驗證完成後，系統會連同存取權杖一併回傳一組刷新權杖（refresh token）。

當存取權杖到期時，您可以使用刷新權杖來取得一組新的存取權杖。如需深入瞭解，請參閱 LINE Login v2.0 API 參考資料中的 [Refresh access token](https://developers.line.biz/en/reference/line-login-v2/#refresh-access-token)。

<!-- note start -->

**刷新權杖的有效期間**

刷新權杖自其對應的存取權杖簽發起，最長有效 90 天。

若刷新權杖到期，您必須提示使用者重新登入，以產生新的存取權杖。

<!-- note end -->

## Verify access tokens 

在自己的伺服器上使用任何從應用程式或外部伺服器收到的存取權杖之前，請先驗證該存取權杖。

如需深入瞭解，請參閱 LINE Login v2.0 API 參考資料中的 [Verify access token validity](https://developers.line.biz/en/reference/line-login-v2/#verify-access-token)。

<!-- note start -->

**驗證存取權杖後您需要檢查的額外條件**

當 LINE Login API 成功驗證存取權杖後，其回應會包含一個 `client_id` 屬性（頻道 ID）以及一個 `expires_in` 屬性（權杖到期前的剩餘時間）。在使用該存取權杖之前，請確認這些屬性符合下列條件。

| Property     | Criteria                                                |
| ------------ | ------------------------------------------------------- |
| `client_id`  | 與您的應用程式連結的 LINE Login 頻道（channel）的頻道 ID |
| `expires_in` | 正值                                                    |

<!-- note end -->
