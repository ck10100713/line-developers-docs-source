# 從 ID 權杖取得個人資料（Get profile information from ID tokens）

LINE Platform 會發行符合 [OpenID Connect](https://openid.net/developers/how-connect-works/) 規範的 ID 權杖（ID token），讓你能安全地從 LINE Platform 取得使用者的[個人資料（profile information）](https://developers.line.biz/en/glossary/#profile-information)（使用者 ID、顯示名稱、大頭貼、電子郵件地址）。

如果你擁有 LINE Profile+ 權限，還能安全地取得在 [LINE Profile+](https://developers.line.biz/en/glossary/#line-profile-plus) 註冊的資料（姓名、性別、生日、電話號碼、地址）。詳情請參閱 [Get user data registered with LINE Profile+](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#getting-profile-plus)。

<!-- table of contents -->

## Get an ID token 

你也可以在[取得存取權杖（access token）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#get-access-token)時取得 ID 權杖。

<!-- tip start -->

**你也可以透過 LIFF app 取得 ID 權杖。**

你也可以使用 [liff.getIDToken()](https://developers.line.biz/en/reference/liff/#get-id-token) 來取得 ID 權杖。

<!-- tip end -->

## About ID tokens 

ID 權杖是包含使用者資訊的 JSON Web Token（JWT）。ID 權杖由 [header](https://developers.line.biz/en/docs/line-login/verify-id-token/#header)、[payload](https://developers.line.biz/en/docs/line-login/verify-id-token/#payload) 與 [signature](https://developers.line.biz/en/docs/line-login/verify-id-token/#signature) 組成，各部分以句點（.）字元分隔。每個部分都是經過 base64url 編碼的值。詳情請參閱 [JWT](https://datatracker.ietf.org/doc/html/rfc7519) 規範。

為了確保你的 app 安全，你應該一律使用簽章（signature）驗證 ID 權杖。除非 ID 權杖是直接從 LINE Platform 取得，否則請在伺服器端驗證 ID 權杖。

要驗證 ID 權杖，請撰寫驗證程式碼，或使用 [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token) 端點（endpoint）。關於使用該端點驗證 ID 權杖的詳情，請參閱 [Get profile information from an ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#get-profile-info-from-id-token)。

### Header 

以下是 header 中包含的值。

| Property | Type | Description |
| --- | --- | --- |
| `alg` | String | ID 權杖的簽章演算法。對於原生 app、LINE SDK 或 LIFF app，會回傳 `ES256`（使用 P-256 與 SHA-256 的 ECDSA）；對於網頁登入，則會回傳 `HS256`（使用 SHA-256 的 HMAC）。 |
| `type` | String | Payload 格式。會回傳 `JWT`。 |
| `kid` | String | 公開金鑰 ID。僅在 `alg` 的值為 `ES256` 時才會包含在 header 中。關於 `kid` 屬性的詳情，請參閱 [JSON Web Key (JWK) document](https://datatracker.ietf.org/doc/html/rfc7517#section-4.5)。 |

以下是解碼後的 header 部分範例。

當 `alg` 為 `HS256` 時：

```json
{
  "typ": "JWT",
  "alg": "HS256"
}
```

當 `alg` 為 `ES256` 時：

```json
{
  "typ": "JWT",
  "alg": "ES256",
  "kid": "a2a459aec5b65fa..."
}
```

### Payload 

使用者的資訊位於 payload 部分。你只能取得主要的個人資料，無法取得使用者的[子個人資料（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

| Property | Type | Description |
| --- | --- | --- |
| `iss` | String | `https://access.line.me`。產生 ID 權杖的 URL。 |
| `sub` | String | 產生此 ID 權杖所對應的使用者 ID |
| `aud` | String | 頻道 ID |
| `exp` | Number | ID 權杖的到期時間，以 UNIX 時間表示（單位為秒）。 |
| `iat` | Number | ID 權杖產生的時間，以 UNIX 時間表示（單位為秒）。 |
| `auth_time` | Number | 使用者通過驗證的時間，以 UNIX 時間表示（單位為秒）。若授權請求中未指定 `max_age` 參數，則不會包含此值。 |
| `nonce` | String | 在授權 URL 中指定的 `nonce` 值。若授權請求中未指定 `nonce` 值，則不會包含此值。 |
| `amr` | Array of strings | 使用者所使用的驗證方法清單。在特定條件下不會包含在 payload 中。<br />包含以下一個或多個值：<ul><li>`pwd`：以電子郵件與密碼登入</li><li>`lineautologin`：LINE 自動登入（包含透過 LINE SDK）</li><li>`lineqr`：以 QR code 登入</li><li>`linesso`：以單一登入（single sign-on）登入</li><li>`mfa`：以雙重驗證（two-factor authentication）登入</li></ul> 關於使用者驗證的詳情，請參閱 [User authentication](https://developers.line.biz/en/docs/line-login/integrate-line-login/#authentication-process)。此外，關於雙重驗證的詳情，請參閱 [Require two-factor authentication](https://developers.line.biz/en/docs/line-login/overview/#two-factor-authentication)。 |
| `name` | String | 使用者的顯示名稱。若授權請求中未指定 `profile` scope，則不會包含此值。 |
| `picture` | String | 使用者的大頭貼圖片 URL。若授權請求中未指定 `profile` scope，則不會包含此值。 |
| `email` | String | 使用者的電子郵件地址。若授權請求中未指定 `email` scope，則不會包含此值。 |

以下是解碼後的 payload 部分範例。

```json
{
  "iss": "https://access.line.me",
  "sub": "U1234567890abcdef1234567890abcdef ",
  "aud": "1234567890",
  "exp": 1504169092,
  "iat": 1504263657,
  "nonce": "0987654asdf",
  "amr": ["pwd"],
  "name": "Taro Line",
  "picture": "https://sample_line.me/aBcdefg123456"
}
```

### Signature 

簽章是將以句點字元分隔、經 base64url 編碼的 header 與 payload 字串進行雜湊運算後的值，用來防止 ID 權杖遭竄改。

雜湊演算法由 header 中的 `alg` 屬性指定。驗證 ID 權杖所需的金鑰會因雜湊簽章所使用的演算法不同而有所差異。

| Algorithm | Key for verification |
| --- | --- |
| `ES256`（使用 P-256 與 SHA-256 的 ECDSA） | [JSON Web Key (JWK) document URL](https://api.line.me/oauth2/v2.1/certs) 中包含 header 內 `kid` 屬性的元素 |
| `HS256`（使用 SHA-256 的 HMAC） | [頻道密鑰（channel secret）](https://developers.line.biz/en/glossary/#channel-secret) |

關於 ID 權杖驗證的詳情，請參閱 OpenID Connect Core 1.0 的 [ID Token Validation](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation)。

關於 OpenID provider 的資訊，請參閱 [OpenID Provider Configuration Document](https://access.line.me/.well-known/openid-configuration)。

## Get profile information from an ID token 

在使用 ID 權杖中所含的資訊時，請撰寫驗證程式碼，或使用 LINE Login 的 [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token) 端點來驗證 ID 權杖。

如果你使用 Verify ID Token 端點，只要將你連同存取權杖一起取得的 ID 權杖以及 LINE Login 頻道 ID 傳送至我們的專用 API 端點，即可驗證 ID 權杖並取得對應使用者的個人資料與電子郵件地址。

請求範例：

```sh
curl -v -X POST 'https://api.line.me/oauth2/v2.1/verify' \
 -d 'id_token=eyJraWQiOiIxNmUwNGQ0ZTU2NzgzYTc5MmRjYjQ2ODRkOD...' \
 -d 'client_id=1234567890'
```

回應範例：

```json
{
  "iss": "https://access.line.me",
  "sub": "U1234567890abcdef1234567890abcdef",
  "aud": "1234567890",
  "exp": 1504169092,
  "iat": 1504263657,
  "nonce": "0987654asdf",
  "amr": ["pwd"],
  "name": "Taro Line",
  "picture": "https://sample_line.me/aBcdefg123456",
  "email": "taro.line@example.com"
}
```

詳情請參閱 LINE Login API 參考文件中的 [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token)。
