# 在 LIFF app 與伺服器中使用使用者資料（Using user data in LIFF apps and servers）

當使用者在 LIFF 瀏覽器中啟動 LIFF app，或是使用者透過 `liff.init()` 方法登入並在外部瀏覽器中啟動 LIFF app 時，LIFF app 可以取得使用者的個人資料（user ID、顯示名稱、個人資料圖片以及電子郵件地址）。

如果你的 LIFF app 沒有妥善處理這些使用者資料，將會容易遭受冒用（spoofing）以及其他類型的攻擊。

本頁說明如何在 LIFF app 或伺服器中，安全地使用開啟 LIFF app 的使用者資訊。

## Use user data on server 

若要在伺服器上使用使用者資料，請從 LIFF app 將 ID token 或 access token 傳送到伺服器。伺服器可以將 LIFF app 傳送過來的 token 傳送到 LINE Platform，藉此安全地取得使用者的個人資料。

- [Send user ID token to get user data](https://developers.line.biz/en/docs/liff/using-user-profile/#sending-id-token)
- [Send access token to get user data](https://developers.line.biz/en/docs/liff/using-user-profile/#sending-access-token)

<!-- warning start -->

**請勿將使用者資訊傳送到伺服器**

請勿從 LIFF app 將透過 `liff.getDecodedIDToken()` 與 `liff.getProfile()` 取得的使用者個人資料明細傳送到伺服器。

<!-- warning end -->

<!-- tip start -->

**Tip**

LIFF SDK 會驗證從 LINE Platform 取得的 ID token 與 access token。你可以信任透過 `liff.getIDToken()` 與 `liff.getAccessToken()` 取得的 token。

<!-- tip end -->

### Send user ID token to get user data 

當你將透過 [`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token) 取得的 ID token 傳送到伺服器時，伺服器會驗證該 ID token，並可使用 [POST /oauth2/v2.1/verify](https://developers.line.biz/en/reference/line-login/#verify-id-token) 來安全地取得使用者的個人資料資訊。

![Interactive SVG](https://developers.line.biz/media/liff/send-user-profile-via-id-token.svg)

### Send access token to get user data 

當你將透過 [`liff.getAccessToken()`](https://developers.line.biz/en/reference/liff/#get-access-token) 取得的 access token 傳送到伺服器時，伺服器會驗證該 token 的有效性（[GET /oauth2/v2.1/verify](https://developers.line.biz/en/reference/line-login/#verify-access-token)），並且也會驗證 access token 的頻道 ID 與有效期間（validity period），如此一來伺服器便可安全地取得使用者的個人資料資訊（[GET /v2/profile](https://developers.line.biz/en/reference/line-login/#get-user-profile)）。

當[使用者關閉 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#behavior-when-closing-liff-app) 時，即使 access token 尚未過期，也會被撤銷（revoke）。

![Interactive SVG](https://developers.line.biz/media/liff/send-user-profile-via-access-token.svg)

## Use user data in LIFF app 

使用透過 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 或 [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 取得的使用者個人資料資訊。

![Interactive SVG](https://developers.line.biz/media/liff/use-user-profile-on-liff-app.svg)

<!-- warning start -->

**請勿將使用者資訊傳送到伺服器**

請勿從 LIFF app 將透過 `liff.getDecodedIDToken()` 與 `liff.getProfile()` 取得的使用者個人資料明細傳送到伺服器。

<!-- warning end -->
