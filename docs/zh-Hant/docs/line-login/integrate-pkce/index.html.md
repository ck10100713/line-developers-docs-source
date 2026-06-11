# LINE Login 的 PKCE 支援（PKCE support for LINE Login）

## What is PKCE? 

PKCE（Proof Key for Code Exchange）是一項在 [RFC7636](https://datatracker.ietf.org/doc/html/rfc7636) 中定義的 OAuth2.0 擴充規格，目的是對抗授權碼攔截攻擊（authorization code interception attack）。

未使用 PKCE 的 OAuth2.0 授權流程存在弱點：若惡意應用程式以某種方式取得了包含授權碼（authorization code）的自訂 URI，使用者專屬的存取權杖（access token）便可能遭竊。透過在整合 LINE Login 的 Web 應用程式中實作 PKCE 授權流程，您可以進一步提升 LINE Login v2.1 的安全性，並防止授權碼攔截攻擊。

## Benefits of implementing PKCE for LINE Login 

針對授權碼攔截攻擊，使用 LINE Login 的 Web 應用程式是否實作 PKCE，會有不同的行為表現。我們建議實作 PKCE，讓您的 Web 應用程式更安全。

<table>
  <thead>
    <tr>
      <th>Without PKCE implemented</th>
      <th>With PKCE implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>若惡意應用程式以某種方式取得了包含授權碼的回呼 URL，便可能竊取存取權杖。<br><img style="padding-top:1em; width:1200px" alt="Authorization code interception attack when PKCE isn't implemented" src="/media/line-login/new-user-login-without-pkce-en.svg" class="bg-border mt-3"></img></td>
      <td>即使惡意應用程式竊取了重新導向（redirection）期間傳遞的資訊，仍可透過比對唯一的 <code>code_challenge</code> 來防止存取權杖遭竊。<br><img style="padding:1em; width:1200px" alt="Authorization code interception attack when PKCE is implemented" src="/media/line-login/new-user-login-with-pkce-en.svg" class="bg-border mt-3"></img></td>
    </tr>
  </tbody>
</table>

<!-- tip start -->

**實作 PKCE 的另一項好處**

若您從 [Yahoo! JAPAN 應用程式](https://promo-mobile.yahoo.co.jp/yjapp/) 存取整合了已實作 PKCE 的 LINE Login 的 Web 應用程式，便可啟用[自動登入（auto login）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)功能，讓您略過使用電子郵件地址與密碼的登入流程。

![Auto login from the Yahoo! JAPAN app](https://developers.line.biz/media/line-login/yja-to-line-login-en.png)

<!-- tip end -->

## Implement PKCE for LINE Login 

若要為 LINE Login 實作 PKCE，除了執行[將 LINE Login 整合至您的 Web 應用程式](https://developers.line.biz/en/docs/line-login/integrate-line-login/)的流程外，還請依照以下四個步驟進行。

![How to implement PKCE](https://developers.line.biz/media/line-login/new-user-login-pkce-workflow-en.svg)

1. [產生 `code_verifier`。](https://developers.line.biz/en/docs/line-login/integrate-pkce/#generate-code-verifier)
2. [根據步驟 1 產生的 `code_verifier` 來產生 `code_challenge`。](https://developers.line.biz/en/docs/line-login/integrate-pkce/#generate-code-challenge)
3. [將步驟 2 產生的 `code_challenge` 與 `code_challenge_method` 加入查詢參數，並將使用者重新導向至該授權 URL。](https://developers.line.biz/en/docs/line-login/integrate-pkce/#add-to-authentication-url)
4. [將步驟 1 產生的 `code_verifier` 加入「Issue access token」API 端點的請求主體（request body）中並執行。](https://developers.line.biz/en/docs/line-login/integrate-pkce/#execute-issuing-access-token)

<!-- tip start -->

**支援 PKCE 的新參數**

為了支援 PKCE，下列參數已新增至 LINE Login 的「Authorization URL」與「Issue access token」API 端點中。

- `code_verifier`
- `code_challenge`
- `code_challenge_method`

關於各參數的詳細資訊，請參閱下方各步驟的詳細說明。

<!-- tip end -->

### 1. Generate `code_verifier` 

在 Web 應用程式端，當使用者執行 LINE Login 時，會產生一個唯一的 `code_verifier`。`code_verifier` 的規格以 [RFC7636](https://datatracker.ietf.org/doc/html/rfc7636) 為基礎。

**參數**

| Parameter | Specs | Example |
| --- | --- | --- |
| <code style="word-break: normal">code_verifier</code> | **可用字元類型**：由半形英數字（`a`-`z`、`A`-`Z`、`0`-`9`）與符號（`-._~`）組成的隨機字串<br>**字元數**：43 至 128 個字元 | wJKN8qz5t8SSI9lMFhBB6qwNkQBkuPZoCxzRhwLRUo1 |

**範例程式碼**

以下是使用 Node.js 產生 `code_verifier` 的範例程式碼：

``` js
// randomAlphaNumericString() is supported to be a function that generates and returns a random string consisting of
// available characters (half-width alphanumeric characters and symbols) for the integer specified in the argument (43 to 128).
const code_verifier = randomAlphaNumericString(43);
```

### 2. Generate `code_challenge` 

您可以將產生的 `code_verifier` 以 SHA256 進行雜湊處理，再以 Base64URL 格式編碼，即可產生 `code_challenge`。

**參數**

| Parameter | Specs | Example |
| --- | --- | --- |
| <code style="word-break: normal">code_challenge</code> | 將 `code_verifier` 以 SHA256 雜湊並以 Base64URL 格式編碼後的值 | BSCQwo_m8Wf0fpjmwkIKmPAJ1A7tiuRSNDnXzODS7QI |

<!-- note start -->

**URL 查詢參數的格式**

`code_challenge` 的值必須從一般的 Base64 格式字串中刪除或替換部分字元，才能作為 URL 查詢參數使用。詳細資訊請參閱 RFC 4648 的 [5. Base 64 Encoding with URL and Filename Safe Alphabet](https://datatracker.ietf.org/doc/html/rfc4648#section-5)。

- 移除填充字元（補齊用的 `=`）
- 將 `+` 替換為 `-`
- 將 `/` 替換為 `_`

| Base64 format example | Deletion and replacement for `code_challenge` example |
| --- | --- |
| BSCQwo_m8Wf0fpjmwk<b style="color:red">+</b>KmPAJ1A<b style="color:red">/</b>tiuRSNDnXzODS7<b style="color:red">==</b> | BSCQwo_m8Wf0fpjmwk<b style="color:red">-</b>KmPAJ1A<b style="color:red">_</b>tiuRSNDnXzODS7 |

<!-- note end -->

**範例程式碼**

以下是使用 Node.js 產生 `code_challenge` 的範例程式碼：

``` js
// This sample code uses the Node.js "crypto" module.
// See: https://nodejs.org/api/crypto.html#crypto_crypto
const crypto = require("crypto");

// Encode BASE64 format into BASE64URL format.
function base64UrlEncode(str) {
    return str
        .replace(/\+/g, '-')
        .replace(/\//g, '_')
        .replace(/=/g, '');
}

// Hash code_verifier with SHA256 and encode it into BASE64URL format to generate code_challenge.
const code_challenge = base64UrlEncode(crypto
    .createHash('sha256')
    .update(code_verifier)
    .digest('base64'));
```

### 3. Add `code_challenge` and` code_challenge_method` in the query parameters of the authorization URL 

在一般 LINE Login 授權 URL 的查詢參數中，加入 `code_challenge` 與 `code_challenge_method`。

**參數**

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| `code_challenge` | String | Optional | 於[步驟 2](https://developers.line.biz/en/docs/line-login/integrate-pkce/#generate-code-challenge) 產生的 `code_challenge`。預設值為 `null`。若未指定值，則該請求不支援 PKCE。 |
| <code style="word-break: normal">code_challenge_method</code> | String | Optional | `S256`（代表雜湊函式 `SHA256`。）<br><br>注意：[RFC7636「Client Creates the Code Challenge」](https://datatracker.ietf.org/doc/html/rfc7636#section-4.2) 除了 `S256` 之外，也定義了 `plain`（不做任何轉換）作為產生 `code_challenge` 的方法，但基於安全考量，LINE Login 僅支援 `S256`。 |

**授權 URL 範例**

```sh
https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%3Fkey%3Dvalue&state=12345abcde&scope=profile%20openid&nonce=09876xyz
&code_challenge={The value of code_challenge calculated in step 2}&code_challenge_method=S256
```

關於授權 URL 的其他查詢參數的詳細資訊，請參閱[驗證使用者並提出授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)。
### 4. Issue an access token by specifying `code_verifier` in the request body 

在 [Issue access token](https://developers.line.biz/en/reference/line-login/#issue-access-token) API 端點的請求主體中加入 `code_verifier` 並執行。

**請求主體（Request body）**

<!-- parameter start (props: optional) -->
code_verifier
String

於[步驟 1](https://developers.line.biz/en/docs/line-login/integrate-pkce/#generate-code-verifier) 產生的 `code_verifier`。<br>（例如：`wJKN8qz5t8SSI9lMFhBB6qwNkQBkuPZoCxzRhwLRUo1`）

<!-- parameter end -->

**請求範例**

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=1234567890abcde' \
--data-urlencode 'redirect_uri=https://example.com/auth?key=value' \
-d 'client_id=1234567890' \
-d 'client_secret=1234567890abcdefghij1234567890ab' \
-d 'code_verifier={The code_verifier generated in step 1}'
```

關於「Issue access token」API 端點的詳細資訊，請參閱 LINE Login v2.1 API 參考文件中的 [Issue access token](https://developers.line.biz/en/reference/line-login/#issue-access-token)。
