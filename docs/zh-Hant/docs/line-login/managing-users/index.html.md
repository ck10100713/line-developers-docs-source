# 管理使用者（Managing users）

本主題說明如何管理透過 LINE Login API 登入的使用者。

## Getting user profiles 

你可以取得已透過[存取權杖（access token）](https://developers.line.biz/en/docs/line-login/managing-access-tokens/)識別之使用者的個人檔案資訊。個人檔案資訊包含使用者的 ID、顯示名稱、個人檔案圖片以及狀態消息。

<!-- note start -->

**檢查你的存取權杖（access token）scope**

你需要具有 `profile` scope 的存取權杖才能取得使用者的個人檔案資訊。若要瞭解詳情，請參閱[驗證使用者並提出授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)以及 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)。

<!-- note end -->

請求範例：

```sh
curl -v -X GET https://api.line.me/v2/profile \
-H 'Authorization: Bearer {access token}'
```

回應範例：

```json
{
  "userId":"U4af4980629...",
  "displayName":"Brown",
  "pictureUrl":"https://profile.line-scdn.net/abcdefghijklmn",
  "statusMessage":"Hello, LINE!"
}
```

若要瞭解詳情，請參閱 LINE Login v2.1 API 參考文件中的 [Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile)。

<!-- tip start -->

**為服務識別使用者**

請透過使用者的[使用者 ID（user ID）](https://developers.line.biz/en/glossary/#user-id)來識別使用者。使用者 ID 無法變更。

使用者可以隨時設定新的顯示名稱、個人檔案圖片與狀態消息。

你無法用這些資訊來識別使用者。

<!-- tip end -->

<!-- tip start -->

**使用 ID 權杖（ID token）識別使用者**

你可以使用與存取權杖一併取得的 ID 權杖（ID token），來取得使用者的個人檔案資訊與電子郵件位址。

若要瞭解詳情，請參閱 LINE Login v2.1 API 參考文件中的 [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token)。

<!-- tip end -->

## Logging out users 

為了打造更好的使用者體驗，我們建議提供讓使用者登出你應用程式的方式。

當使用者已從你的應用程式登出後，請撤銷（revoke）其[存取權杖（access token）](https://developers.line.biz/en/docs/line-login/managing-access-tokens/)，並刪除你應用程式中該使用者的所有資料。

撤銷存取權杖的請求範例：

```sh
curl -v -X POST 'https://api.line.me/oauth2/v2.1/revoke' \
-H "Content-Type:application/x-www-form-urlencoded" \
-d "client_id={channel id}&client_secret={channel secret}&access_token={access token}"
```

若要瞭解詳情，請參閱 LINE Login v2.1 API 參考文件中的 [Revoke access tokens](https://developers.line.biz/en/reference/line-login/#revoke-access-token)。
