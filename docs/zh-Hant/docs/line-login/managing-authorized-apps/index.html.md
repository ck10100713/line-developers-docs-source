# 管理已授權的應用程式（Managing authorized apps）

使用者在使用 LINE Login 頻道（channel）時，必須同意提供其資訊，例如 [User ID](https://developers.line.biz/en/glossary/#user-id)。同意之後，使用者可以隨時檢視同意條款，或撤銷（revoke）同意。

1. 在你的 LINE App 中，依序點選 **設定** > **帳號** > **已授權的應用程式**。<br> 系統會顯示「已授權的應用程式」設定畫面。
2. 點選你想要取消授權的應用程式。<br> 系統會顯示已授權應用程式畫面。<br> ![Authorized app](https://developers.line.biz/media/line-login/managing-authorized-apps/authorized-app-en.png)<br> 若要檢視同意條款，請點選「檢視權限」。<br> 若要撤銷同意，請點選「解除連結」。

## When user revokes consent 

當使用者撤銷同意後，存取權杖（access token）與更新權杖（refresh token）會立即失效，並對使用者與服務提供者造成以下影響：

| 對象 | 說明 |
| --- | --- |
| 使用者 | <ul><li>當你嘗試在已撤銷同意的應用程式上使用 LINE Login 時，會再次顯示同意畫面。</li><li>在取得同意之前，將禁止使用 LINE Login。</li></ul> |
| 服務提供者 | <ul><li>即使你使用已取得的存取權杖，也無法取得 user ID 或個人資料資訊。</li><li>由於更新權杖已無法使用，存取權杖也無法更新。</li><li>在使用者再次同意並使用 LINE Login 之前，你將無法取得 user ID 或個人資料資訊。</li></ul> |

<!-- note start -->

**尊重使用者撤銷同意的決定**

每位 LINE 使用者在不同服務提供者下都有不同的 user ID。即使使用者撤銷同意後再次同意，其 user ID 也不會改變。這表示與特定 user ID 相關聯的資訊，即使在使用者撤銷同意之後仍可能持續被使用。

然而，請尊重使用者撤銷同意的決定，並在驗證存取權杖之後再重新取得使用者的資訊。

若存取權杖已失效，請採取以下措施：

- 若存取權杖過期而失效，請使用更新權杖來更新存取權杖。
- 然而，若使用者撤銷同意，則存取權杖與更新權杖都將無法使用。

你必須依照 [LINE User Data Policy](https://terms2.line.me/LINE_Developers_user_data_policy?lang=en) 正確處理使用者的資訊。未遵守 LINE User Data Policy 將導致服務終止。

<!-- note end -->
