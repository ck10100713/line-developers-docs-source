# LINE Login 安全檢查清單（LINE Login security checklist）

在開發使用 LINE Login 的應用程式時，你必須為第三方可能發起的攻擊做好準備，並在沒有任何安全漏洞的情況下實作登入功能。

我們提供一份檢查清單，以確保在將 LINE Login 整合到你的應用程式時不存在任何安全漏洞。請在發布前使用此檢查清單來驗證你的應用程式。

我們也建議你確認 LINE DEVELOPER DAY 2020 的議程「[Implementing safe and secure LINE Login](https://linedevday.linecorp.com/2020/en/sessions/7159/)」。

<!-- tip start -->

**請在理解檢查清單目的的前提下，務必建立安全的系統**

此檢查清單收錄了使用 LINE Login 時需要特別注意的重點摘錄。符合檢查清單的內容並不保證安全。請在充分理解風險的前提下，務必建立安全的系統。

<!-- tip end -->

<!-- table of contents -->

## Checklist for query parameters passed to the authorization URL 

以下檢查清單適用於在啟動認證與授權流程時，傳遞給授權 URL（authorization URL）的查詢參數（query parameter）。關於授權 URL 的詳細資訊，請參閱[Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)。

<!-- tip start -->

**Callback URL**

**Callback URL** 指的是 [LINE Developers Console](https://developers.line.biz/console/) 中 LINE Login 頻道（channel）**LINE Login tab** 上的 **Callback URL**。關於如何設定 **Callback URL** 的詳細資訊，請參閱[Getting started with LINE Login](https://developers.line.biz/en/docs/line-login/getting-started/)。

<!-- tip end -->

| 檢查內容 | 相關頁面 |
| --- | --- |
| 在 `redirect_uri` 中指定的 URL 結構（URL schema）是否為 HTTPS？（除非有特定理由不指定為 HTTPS。） | <ul><li>[RFC6749 3.1.2.1.](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2.1)</li></ul> |
| 你是否理解作為 `redirect_uri` 的有效 URL 是以下其中一種 URL？<ul><li>與 **Callback URL** 中註冊的 URL 完全相符的 URL</li><li>在 **Callback URL** 中註冊的 URL 上加入選用查詢參數後的 URL</li></ul> | <ul><li>[RFC6749 3.1.2.](https://datatracker.ietf.org/doc/html/rfc6749#section-3.1.2)</li><li>[Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)</li></ul> |
| 在 **Callback URL** 中註冊的 URL 所接收的查詢參數裡，是否存在會接收任意 URL 並進行轉址的查詢參數？如果存在這類參數，你是否已驗證不存在開放轉址（Open Redirector）漏洞？ | <ul><li>[RFC6749 10.15](https://datatracker.ietf.org/doc/html/rfc6749#section-10.15)</li></ul> |
| `state` 中指定的值是否以加密安全且不可預測的方式（例如 SecureRandom）隨機產生且具唯一性，並以第三方無法預測的方式產生？ | <ul><li>[RFC6749 10.12.](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12)</li><li>[Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)</li></ul> |
| 為 `state` 指定的值是否儲存在第三方無法存取的位置，例如以下位置？<ul><li>伺服器的工作階段（session）資訊</li><li>受同源政策（same-origin policy）保護的 Cookie 等</li></ul> | <ul><li>[RFC6749 10.12.](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12)</li></ul> |
| 即使是同一位使用者嘗試登入，每次嘗試登入時是否都為 `state` 指定不同的值？ | <ul><li>[RFC6749 10.12.](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12)</li></ul> |

## Checklist for query parameters returned to the callback URL 

以下檢查清單適用於回傳至 callback URL 的查詢參數。關於回傳至 callback URL 的查詢參數的詳細資訊，請參閱[Receiving the authorization response or error response with a web app](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code-or-error-response-with-a-web-app)。

| 檢查內容 | 相關頁面 |
| --- | --- |
| 你是否確認 `state` 的值與認證 URL 中指定的 `state` 相符？ | <ul><li>[RFC6749 10.12.](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12)</li><li>[Receiving the authorization response or error response with a web app](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code-or-error-response-with-a-web-app)</li></ul> |

## Checklist for issuing the access token 

以下檢查清單適用於使用 [LINE Login API](https://developers.line.biz/en/reference/line-login/) 核發存取權杖（access token）。關於核發存取權杖的詳細資訊，請參閱[Issue access token](https://developers.line.biz/en/reference/line-login/#issue-access-token)與[Managing authorized apps](https://developers.line.biz/en/docs/line-login/managing-access-tokens/)。

| 檢查內容 | 相關頁面 |
| --- | --- |
| 你是否理解在 `client_secret` 中指定的頻道密鑰（channel secret）是機密資訊，不可讓第三方得知？ | <ul><li>[OpenID Connect 1.0 16.19](https://openid.net/specs/openid-connect-core-1_0.html#rfc.section.16.19)</li></ul> |

## Checklist for using ID tokens and access tokens 

以下檢查清單適用於使用 LINE Platform 所核發的 ID 權杖（ID token）與存取權杖。關於核發 ID 權杖與存取權杖的詳細資訊，請參閱[Get profile information from ID tokens](https://developers.line.biz/en/docs/line-login/verify-id-token/)與[Managing authorized apps](https://developers.line.biz/en/docs/line-login/managing-access-tokens/)。

| 檢查內容 | 相關頁面 |
| --- | --- |
| 你是否已驗證 ID 權杖與存取權杖？ | <ul><li>[Verify access token validity](https://developers.line.biz/en/reference/line-login/#verify-access-token)</li><li>[Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token)</li></ul> |
| 在成功驗證存取權杖之後，你是否已確認 `client_id` 與 `expires_in` 屬性的值符合以下條件？<ul><li>`client_id`：與連結至原生應用程式的 LINE Login 頻道的頻道 ID 相同的值</li><li>`expires_in`：正值</li></ul> | <ul><li>[Using access tokens to register new users](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-access-tokens)</li></ul> |

## Checklist for sending ID tokens and access tokens to the backend server for processing 

以下檢查清單適用於使用 LINE Platform 取得的使用者資訊來進行使用者註冊與登入。關於安全的使用者註冊與登入流程的概念的詳細資訊，請參閱[Creating a secure login process between your app and server](https://developers.line.biz/en/docs/line-login/secure-login-process/)。

| 檢查內容 | 相關頁面 |
| --- | --- |
| 你是否將原始（raw）的 ID 權杖或存取權杖從用戶端傳送至後端伺服器，而非傳送使用者 ID 或其他資訊？<br>\* 在使用驗證 ID 權杖與存取權杖的 API 之後，後端伺服器即可取得使用者 ID 與其他資訊。 | <ul><li>[Using access tokens to register new users](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-access-tokens)</li><li>[Verify access token validity](https://developers.line.biz/en/reference/line-login/#verify-access-token)</li><li>[Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token)</li></ul> |
| 你是否已驗證從用戶端傳送至後端伺服器的 ID 權杖與存取權杖？ | <ul><li>[Using access tokens to register new users](https://developers.line.biz/en/docs/line-login/secure-login-process/#using-access-tokens)</li></ul> |
