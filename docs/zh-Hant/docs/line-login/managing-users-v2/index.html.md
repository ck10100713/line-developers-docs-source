# 管理使用者（LINE Login v2.0）

<!-- warning start -->

**LINE Login v2.0 已被棄用**

本頁面包含舊版 LINE Login（v2.0）的說明文件。LINE Login v2.0 已被[棄用（deprecated）](https://developers.line.biz/en/glossary/#deprecated)，[終止服務（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)的日期尚待確定，因此我們建議您改用目前的版本（LINE Login v2.1）。在公告終止服務與實際終止服務之間，會有一定的緩衝期間。詳情請參閱 [LINE Login versions](https://developers.line.biz/en/docs/line-login/overview/#versions)。

<!-- warning end -->

本主題說明如何使用 [LINE Login v2.0](https://developers.line.biz/en/docs/line-login/overview/#versions) 端點（endpoint），來管理透過 LINE Login API 登入的使用者。

## Get user profiles 

您可以取得已透過[存取權杖（access token）](https://developers.line.biz/en/docs/line-login/managing-access-tokens/)識別的使用者個人資料。個人資料包含使用者的 ID、顯示名稱、個人檔案圖片，以及狀態消息。

LINE Login v2.0 與 v2.1 取得使用者個人資料的方法相同。如需深入了解，請參閱 [Getting user profiles](https://developers.line.biz/en/docs/line-login/managing-users/#get-profile)。

## Log out users 

<!-- note start -->

**Note**

本文件為 LINE Login v2.0（LINE Login 的舊版本）的說明文件。

如要了解如何使用最新版本 LINE Login v2.1 來執行此操作，請參閱 [Logging out users](https://developers.line.biz/en/docs/line-login/managing-users/#logout)。

<!-- note end -->

為了打造更好的使用者體驗，我們建議您提供讓使用者登出應用程式的方式。

當使用者登出您的應用程式後，請撤銷（revoke）其[存取權杖（access token）](https://developers.line.biz/en/docs/line-login/managing-access-tokens-v2/)，並刪除應用程式中所有的使用者資料。

撤銷存取權杖的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/oauth/revoke \
-H 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'refresh_token={refresh token}'
```

如需深入了解，請參閱 LINE Login v2.0 API 參考資料中的 [Revoke access token](https://developers.line.biz/en/reference/line-login-v2/#revoke-access-token)。
