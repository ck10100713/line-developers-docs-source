# 將 LINE Login（v2.0）整合至你的網頁應用程式（Integrating LINE Login (v2.0) with your web app）

<!-- warning start -->

**LINE Login v2.0 已淘汰**

本頁包含的是 LINE Login 舊版本 v2.0 的文件。LINE Login v2.0 已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)，其[終止服務（end-of-life）](https://developers.line.biz/en/glossary/#end-of-life)日期尚未確定，因此我們建議你使用目前的版本（LINE Login v2.1）。在終止服務公告與實際終止服務之間，會有一段緩衝期。如需更多資訊，請參閱 [LINE Login versions](https://developers.line.biz/en/docs/line-login/overview/#versions)。

<!-- warning end -->

本頁說明如何將 LINE Login 整合至你的網頁應用程式。如果你還沒有可整合 LINE Login 的應用程式，可以使用範例應用程式。請參閱 [Getting started with LINE Login](https://developers.line.biz/en/docs/line-login/getting-started/)。

## Login flow 

網頁應用程式的 LINE Login 流程（網頁登入）是以 [OAuth 2.0 授權碼流程（authorization code flow）](https://datatracker.ietf.org/doc/html/rfc6749)為基礎。

網頁登入流程的概觀如下所示。網頁應用程式必須實作流程圖中與自身相關的所有登入流程環節。

![Web login flow](https://developers.line.biz/media/line-login/web-login-flow.svg)

## Creating a channel 

[建立一個 LINE Login 頻道（channel）](https://developers.line.biz/en/docs/line-login/getting-started/#step-1-create-channel)，並將其設定為可搭配網頁應用程式使用。

- [設定回呼 URL（callback URL）](https://developers.line.biz/en/docs/line-login/integrate-line-login-v2/#setting-callback-url)

### Setting a callback URL 

在使用者通過驗證並授權你的網頁應用程式之後，授權碼（authorization code）與 `state` 會被傳送至回呼 URL。

請在 [LINE Developers Console](https://developers.line.biz/console/) 中頻道設定的 **LINE Login** 分頁設定回呼 URL。

每個頻道可以設定一個以上的回呼 URL。

![Redirect settings](https://developers.line.biz/media/line-login/integrate-login-web/redirect-settings.png)

<!-- note start -->

**存取電子郵件地址的權限**

你無法取得使用 LINE Login v2.0 登入你應用程式的使用者的電子郵件地址。

<!-- note end -->

## Authenticating users and making authorization requests 

啟動以 LINE Platform 驗證使用者並授權你應用程式的程序。

當使用者點擊 LINE Login 按鈕時，將使用者重新導向至授權 URL。

<!-- tip start -->

**Tip**

- 在你的網頁應用程式中加入 LINE Login 按鈕時，請遵循 [LINE Login button design guidelines](https://developers.line.biz/en/docs/line-login/login-button/)。
- 你也可以直接連結到授權 URL，而不顯示 LINE Login 按鈕。
- 使用者的驗證憑證不會傳送至你的網頁應用程式。

<!-- tip end -->

授權 URL 範例：

```
https://access.line.me/dialog/oauth/weblogin?response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth&state=123abc
```

你可以將下列查詢參數傳遞給授權 URL。

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `response_type` | String | Required  | `code` |
| `client_id` | String | Required  | LINE Login 頻道 ID。你可以在 [LINE Developers Console](https://developers.line.biz/console/) 中找到它。 |
| `redirect_uri` | String | Required  | 已在 [LINE Developers Console](https://developers.line.biz/console/) 註冊的回呼 URL |
| `state` | String | Required  | 用來防止[跨站請求偽造（cross-site request forgery）](https://wikipedia.org/wiki/Cross-site_request_forgery)的唯一英數字串。**你的網頁應用程式應為每個登入工作階段產生一個隨機值。**此值不可為 URL 編碼字串。 |

### User authentication and authorization 

<!-- tip start -->

**使用者驗證與授權由 LINE Platform 直接處理**

支援 LINE Login 的網頁應用程式不需要自行實作授權程序。

<!-- tip end -->

在被重新導向至授權 URL 之後，使用者會以其 LINE 驗證憑證登入，並決定是否授予你的網頁應用程式所請求的存取權限。

同意畫面範例：

![Consent screen](https://developers.line.biz/media/line-login/integrate-login-web/consent-screen.png)

## Receiving the authorization code or error response with a web app 

使用者完成驗證與授權程序後，會被重新導向至回呼 URL。

如果使用者已授予你的應用程式存取權限，會回傳一組授權碼。

如果使用者*未*授予你的應用程式存取權限，則會回傳錯誤回應。

### Receiving the authorization code 

使用者通過驗證並完成授權步驟後，會帶著下列查詢參數被重新導向至回呼 URL。

| Parameter | Type | Description |
| --- | --- | --- |
| `code` | String | 用來取得存取權杖（access token）的授權碼。有效期為 10 分鐘。此授權碼只能使用一次。 |
| `state` | String | 用來防止[跨站請求偽造（cross-site request forgery）](https://wikipedia.org/wiki/Cross-site_request_forgery)的唯一英數字串。請驗證此值是否與傳遞給授權 URL 的 `state` 參數值相符。 |

重新導向目標 URL 範例：

```
https://example.com/callback?code=b5fd32eacc791df&state=123abc
```

### Receiving an error response 

如果使用者拒絕授予你應用程式所請求的權限，會帶著下列查詢參數被重新導向至回呼 URL：

| Parameter | Type | Description |
| --- | --- | --- |
| `error_description` | String | `The+user+has+denied+the+approval` <br>**注意：**此參數不會出現在 iOS 與 Android 應用程式的內建瀏覽器（in-app browser）中。我們目前正在處理這個問題。 |
| `errorMessage` | String | `DISALLOWED` |
| `errorCode` | Number | `417` |
| `state` | String | 授權 URL 中所包含的 `state` 參數。你可以使用此值來判斷哪個程序被拒絕。 |
| `error` | String | `access_denied` |

重新導向目標 URL 範例：

```
https://example.com/callback?error_description=The+user+has+denied+the+approval&errorMessage=DISALLOWED&errorCode=417&state=123abc&error=access_denied
```

## Getting an access token with a web app 

如果你從 LINE Platform 連同授權碼一起收到的 `state` 參數，與你在[驗證使用者並提出授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login-v2/#making-an-authorization-request)時所指定的 `state` 參數相符，你就可以取得存取權杖。

請求範例：

```sh
curl -v -X POST https://api.line.me/v2/oauth/accessToken \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=b5fd32eacc791df' \
-d 'redirect_uri=https%3A%2F%2Fexample.com%2Fauth' \
-d 'client_id=12345' \
-d 'client_secret=d6524edacc8742aeedf98f'
```

回應範例：

```json
{
  "access_token": "bNl4YEFPI/hjFWhTqexp4MuEw5YPs7qhr6dJDXKwNPuLka...",
  "expires_in": 2591977,
  "refresh_token": "8iFFRdyxNVNLWYeteMMJ",
  "scope": "P",
  "token_type": "Bearer"
}
```

如需更多資訊，請參閱 LINE Login v2.0 API 參考文件中的 [Issuing access tokens](https://developers.line.biz/en/reference/line-login-v2/#issue-access-token)。

## Next steps 

取得存取權杖後，你可以用它來執行下列操作：

- [Managing access tokens (LINE Login v2.0)](https://developers.line.biz/en/docs/line-login/managing-access-tokens-v2/)
- [Managing users (LINE Login v2.0)](https://developers.line.biz/en/docs/line-login/managing-users-v2/)
