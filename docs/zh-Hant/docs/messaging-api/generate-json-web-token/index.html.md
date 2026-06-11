# 簽發頻道存取權杖 v2.1（Issue channel access token v2.1）

LINE Platform 上提供[四種類型的頻道存取權杖（channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#channel-access-token-types)。其中，頻道存取權杖 v2.1 與無狀態（stateless）頻道存取權杖可以使用 JSON Web Token（JWT）來產生。

本頁說明如何指定 assertion 簽署金鑰、如何從簽署金鑰產生 JWT，以及如何使用所產生的 JWT 簽發頻道存取權杖，並以頻道存取權杖 v2.1 為對象。

## Process of issuing a channel access token v2.1 

簽發頻道存取權杖 v2.1 的流程如下圖所示。此圖顯示以下三個步驟：

- [建立 assertion 簽署金鑰](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#create-an-assertion-signing-key)（圖中的步驟 1）
- [產生 JWT](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#generate-jwt)（圖中的步驟 6）
- [簽發頻道存取權杖 v2.1](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#issue_a_channel_access_token_v2_1)（圖中的步驟 7）

![](https://developers.line.biz/media/messaging-api/channel-access-token/channel-access-token-issue-flow-en.svg)

<!-- tip start -->

**頻道存取權杖 v2.1 規格**

簽發頻道存取權杖 v2.1 的驗證方式遵循 [Using JWTs as Authorization Grants (RFC 7523)](https://datatracker.ietf.org/doc/html/rfc7523#section-2.1)。這是 [OAuth Assertion Framework (RFC 7521)](https://datatracker.ietf.org/doc/html/rfc7521#section-4.1) 中，使用 [JSON Web Token (RFC 7519)](https://datatracker.ietf.org/doc/html/rfc7519) 的 Assertion Framework。

<!-- tip end -->

## Create an assertion signing key 

簽發 assertion 簽署金鑰可分為以下兩個步驟：

- [1. 產生 assertion 簽署金鑰的金鑰對](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#generate-a-key-pair-for-the-assertion-signing-key)
- [2. 註冊公開金鑰並取得 `kid`](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#register-public-key-and-get-kid)

### 1. Generate a key pair for the assertion signing key 

要建立 JWT，您必須先建立一組 assertion 簽署金鑰對（私鑰、公鑰）。

#### Assertion signing key specification 

您可以使用符合以下條件的 [JSON Web Key (RFC7517)](https://datatracker.ietf.org/doc/html/rfc7517) 作為 JWT 的 assertion 簽署金鑰。

- 金鑰必須是 RSA 公開金鑰。（將 `kty` 屬性設為 `RSA`）
- RSA 金鑰長度必須為 2048 位元。
- 使用 RS256（搭配 SHA256 的 RSASSA-PKCS1-v1_5）作為簽署演算法。（將 `alg` 屬性設為 `RS256`）
- 載明此公開金鑰用於簽署。（依下表的說明設定 `use` 或 `key_ops`）。

因此，assertion 簽署金鑰的公開金鑰必須包含以下屬性：

| 屬性 | 說明 |
| --- | --- |
| `kty` | 金鑰所使用的加密演算法系列。設為 `RSA`。 |
| `alg` | 金鑰所使用的演算法。設為 `RS256`。 |
| `use`<sup>\*1</sup> | 金鑰的用途。設為 `sig`。 |
| `key_ops`<sup>\*1</sup> | 金鑰要執行的操作。僅設為 `["verify"]`。 |
| `e` | 用於還原公開金鑰的絕對值 |
| `n` | 用於還原公開金鑰的加密索引 |

\*1 請指定 `use` 或 `key_ops` 其中之一。

<!-- note start -->

**註冊公開金鑰前的確認事項**

請確認您要註冊的公開金鑰沒有 `kid` 屬性。如果 assertion 簽署金鑰的公開金鑰帶有 `kid` 屬性，將會發生錯誤。這是因為 `kid` 只會在您於 LINE Developers Console 註冊公開金鑰時簽發。

<!-- note end -->

您可以選擇根據已公開的規格自行撰寫程式來產生 assertion 簽署金鑰對，但使用符合規格的函式庫會讓產生金鑰更為輕鬆。

以下是產生 assertion 簽署金鑰的步驟範例：

- [使用 jwx（Go 語言函式庫）建立金鑰對](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#use-go-lang)
- [使用 JWCrypto（Python 函式庫）建立金鑰對](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#use-python)
- [使用瀏覽器建立金鑰對](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#use-browser)

#### Create a key pair with jwx (Go language library) 

您可以使用 [jwx 命令列工具](https://github.com/lestrrat-go/jwx/tree/develop/v2/cmd/jwx)產生金鑰對。此命令列工具是 [jwx](https://github.com/lestrrat-go/jwx) 的一部分，jwx 是一套用於 JWT 實作的開放原始碼 Go 語言函式庫。如果您尚未建置 Go 語言開發環境，請從 [Go 語言官方網站](https://go.dev/doc/install)下載 Go。

要簽發 assertion 簽署金鑰：

##### 1. Install the jwx command line tool 

使用以下指令安裝 jwx 命令列工具。

```sh
$ git clone https://github.com/lestrrat-go/jwx.git
$ cd jwx
$ make jwx
```

安裝完成後，您會看到 jwx 命令列工具安裝的路徑。

```
// Example of installed path display
Installed jwx in {installed path}
```

您應該設定路徑，以便能夠執行後續步驟中的指令。

##### 2. Generate private key and public key 

使用以下指令建立私鑰。

```sh
$ jwx jwk generate --type RSA --keysize 2048 --template '{"alg":"RS256","use":"sig"}' > private.key
```

使用該私鑰建立公鑰。

```sh
$ jwx jwk format --public-key private.key > public.key
```

如果成功，便會產生一組私鑰與公鑰：

**私鑰範例**

```json
{
  "alg": "RS256",
  "d": "JeSJWnvZ......",
  "dp": "gBDRXGg7......",
  "dq": "MjFJ4xM9......",
  "e": "AQ......",
  "kty": "RSA",
  "n": "pTS2jGso......",
  "p": "xQibzkW6......",
  "q": "1qWtyQ9s......",
  "qi": "sdVGblc......",
  "use": "sig"
}
```

**公鑰範例**

```json
{
  "alg": "RS256",
  "e": "AQ......",
  "kty": "RSA",
  "n": "pTS2jGso......",
  "use": "sig"
}
```

#### Create a key pair with JWCrypto (Python library) 

您可以使用開放原始碼的 Python 函式庫 [JWCrypto](https://github.com/latchset/jwcrypto) 來建立金鑰對以實作 JWT。要使用 JWCrypto，您的電腦需安裝 Python 3 與 pip。如果您沒有 Python 3，請從 [Python 官方網站](https://www.python.org/downloads/)下載適合您作業系統的安裝程式並進行安裝。安裝 Python 3 時會一併安裝 pip。如果您已有 Python 3 但沒有 pip，請參閱 [pip 文件](https://pip.pypa.io/en/stable/installation/)進行安裝。

要簽發 assertion 簽署金鑰：

##### 1. Install JWCrypto 

使用以下指令安裝 JWCrypto。

```python
$ pip install jwcrypto
```

##### 2. Write code to create private and public keys 

建立一個 Python 檔案，透過將 `kty` 指定為 `RSA`、`alg` 指定為 `RS256`、`use` 指定為 `sig`、`size` 指定為 `2048`，來產生私鑰與公鑰，如下所示。

```python
from jwcrypto import jwk
import json
key = jwk.JWK.generate(kty='RSA', alg='RS256', use='sig', size=2048)

private_key = key.export_private()
public_key = key.export_public()

print("=== private key ===\n"+json.dumps(json.loads(private_key),indent=2))
print("=== public key ===\n"+json.dumps(json.loads(public_key),indent=2))
```

以您想要的任何檔名儲存此 Python 檔案。本例中的檔名為 `app.py`。

在儲存該 Python 檔案的同一個目錄中，使用以下指令依據私鑰產生公鑰。

```sh
$ python app.py
```

如果成功，便會在標準輸出中產生一組私鑰與公鑰：

**私鑰範例**

```json
{
  "alg": "RS256",
  "d": "zKh7iwIIPXXFKYQS...",
  "dp": "u1qKg_43UeuGpZFI...",
  "dq": "69AzYgpcg0ckypUrv...",
  "e": "AQ..",
  "kty": "RSA",
  "n": "_RzHf7cgG_i6Pdo_...",
  "p": "_20iRavoSrMIwWuRPxo...",
  "q": "_a5QodMBbEriAgztXvHi...",
  "qi": "JozdjTtK57IFLeVAB...",
  "use": "sig"
}
```

**公鑰範例**

```json
{
  "alg": "RS256",
  "e": "AQAB",
  "kty": "RSA",
  "n": "_RzHf7cgG_i6Pdo...",
  "use": "sig"
}
```

#### Generate a key pair with a browser 

如果您的瀏覽器支援 [Web Crypto API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API)，您可以使用 [`SubtleCrypto.generateKey()`](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto/generateKey) 方法來產生私鑰與公鑰。如果您使用 Google Chrome，請在 Chrome 開發者工具的主控台（console）中輸入並執行以下程式碼。

```javascript
(async () => {
  const pair = await crypto.subtle.generateKey(
    {
      name: "RSASSA-PKCS1-v1_5",
      modulusLength: 2048,
      publicExponent: new Uint8Array([1, 0, 1]),
      hash: "SHA-256",
    },
    true,
    ["sign", "verify"],
  );

  console.log("=== private key ===");
  console.log(
    JSON.stringify(
      await crypto.subtle.exportKey("jwk", pair.privateKey),
      null,
      "  ",
    ),
  );

  console.log("=== public key ===");
  console.log(
    JSON.stringify(
      await crypto.subtle.exportKey("jwk", pair.publicKey),
      null,
      "  ",
    ),
  );
})();
```

如果成功，便會產生一組私鑰與公鑰。

**私鑰範例**

```json
{
  "alg": "RS256",
  "d": "GaDzOmc4......",
  "dp": "WAByrYmh......",
  "dq": "WLwjYun0......",
  "e": "AQ......",
  "ext": true,
  "key_ops": [
    "sign"
  ],
  "kty": "RSA",
  "n": "vsbOUoFA......",
  "p": "5QJitCu9......",
  "q": "1ULfGui5......",
  "qi": "2cK4apee......"
}
```

**公鑰範例**

```json
{
  "alg": "RS256",
  "e": "AQ......",
  "ext": true,
  "key_ops": [
    "verify"
  ],
  "kty": "RSA",
  "n": "vsbOUoFA......"
}
```

### 2. Register public key and get `kid` 

產生金鑰對後，請在 [LINE Developers Console](https://developers.line.biz/console/) 註冊公開金鑰，以換取 `kid`。要註冊您的公開金鑰，請前往主控台並開啟您頻道（channel）的頻道設定。點選 **Basic settings** 分頁，接著點選 assertion 簽署金鑰旁的 **Register a public key** 按鈕。輸入公開金鑰並以 **Register** 按鈕完成註冊。

如果公開金鑰成功註冊，您便會換取到 `kid`。

## Generate a JWT 

JWT 是一個字串，包含 header、payload 與 signature，這三者皆為必要。要產生 JWT，您可以使用任何 [JWT 函式庫](https://www.jwt.io/libraries)，或使用您的 assertion 簽署金鑰從頭撰寫自己的程式碼。

### Header 

header 必須包含以下屬性：

| 屬性 | 類型 | 說明 |
| --- | --- | --- |
| `alg` | String | 用於產生 JWT 的演算法。將值設為 `"RS256"` |
| `typ` | String | 權杖的類型。將值設為 `"JWT"`。 |
| `kid` | String | 金鑰 ID。將值設為在 [2. 註冊公開金鑰並取得 `kid`](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#register-public-key-and-get-kid) 中換取到的 `kid` 屬性。 |

以下是解碼後的 header 範例：

```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "536e453c-aa93-4449-8e90-add2608783c6"
}
```

### Payload 

payload 必須包含以下屬性：

| 屬性 | 類型 | 說明 |
| --- | --- | --- |
| `iss` | String | 頻道 ID。您可以從 [LINE Developers Console](https://developers.line.biz/console/) 取得您的頻道 ID。此屬性的值必須與 `sub` 相同。 |
| `sub` | String | 頻道 ID。您可以從 [LINE Developers Console](https://developers.line.biz/console/) 取得您的頻道 ID。此屬性的值必須與 `iss` 相同。 |
| `aud` | String | 將值設為 `https://api.line.me/`。 |
| `exp` | Number | JWT 的到期時間，以 UNIX 時間（秒）表示。JWT assertion 的最長有效期間為 30 分鐘。 |
| `token_exp` | Number | 頻道存取權杖的有效期間，以秒為單位。頻道存取權杖的最長有效期間為 30 天。 |

以下是解碼後的 payload 範例：

```json
{
  "iss": "1234567890",
  "sub": "1234567890",
  "aud": "https://api.line.me/",
  "exp": 1559702522,
  "token_exp": 86400
}
```

### Signature 

您需要對 header 與 payload 進行簽署以產生 JWT。請了解如何使用 [node-jose](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#jwt-use-nodejs)（Node.js 函式庫）或 [PyJWT](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#jwt-use-python)（Python 函式庫）建立 signature，並使用其結果產生 JWT。

#### Generate a JWT with node-jose (Node.js library) 

要使用 Node.js 函式庫 node-jose 建立 signature 並產生 JWT，請確認您已安裝 [Node.js](https://nodejs.org/en) 與 [node-jose](https://github.com/cisco/node-jose#installing)。

以下範例程式碼使用 node-jose 以**私鑰**進行簽署以產生 JWT。要使用此程式碼產生您自己的 JWT，請先將 `privateKey` 的值改為您 assertion 簽署金鑰的私鑰。同時也將 `header` 與 `payload` 改為您自己的值，然後執行程式碼。請務必以您的**私鑰**進行簽署，以證明內容未遭竄改。關於用法的詳細資訊，請參閱 [node-jose](https://github.com/cisco/node-jose#installing)。

```javascript
let jose = require("node-jose");

let privateKey = `
{
    "p": "4h8yEw4q9VkzhXMgXZsIZVkEuZ49EmtWYk9zs0hPTa24ejjRMA6KTYh_va0GlaChO9t0MVQVuduznt-OFZyRAinr4svU4MKD2A3gTHJJCxs0xICva8rkHXqxfPwXngpb5L_xFURbXcSTzMcKckWuOpyPznAgY4XsZxw0t7ewj9E",
    "kty": "RSA",
    "q": "pVhBdRN5K3MEiZzU4__TsrtSBJDD_stu60m73iIvsHIrvK3Dmfl-J1zhsyOvi3NH9mVXpUimBwP8nTe-BlVM71G7_EotFHeKH1zTmBlx6AOngmrc40W2Hd__OZW0NfC_xOTvI_Ea2BNGoGtcrIGVFLTivJ4y9wAVOKA058zJ0ls",
    "d": "ObzE_-TROJazDm-ry-8TKRBMGzwcwTK6lMFSk7n-Xp6h7cDauSdRRYnZivC1lh5plVG3I9aUmPTRbVk7nrPqOlp4WWKQ27lyLd5IogbArpXgnBSkp9Zy0lWzvOsI3gHNnYuehyksHB53FIK93t838JfDQoXUUzalNoNwAGfkTNZxT4GIXGMGzNck2Z_urOATMf8-wdad-u4a5IB2KfHugwH2kw-Zig7fbdcN4_DeKWpuigdesa48Yj_hRJRws-mVFp-xHlGJehumnM_v8FLD85ap8L1hwvBqdJQeurcLXYzZbtdp9a5GpJI7gzOTMoEdxIKlEIIbaOKv4rkkztdhoQ",
    "e": "AQAB",
    "use": "sig",
    "kid": "536e453c-aa93-4449-8e90-add2608783c6",
    "qi": "XQ2puK9LT5yimyJXlXb4nHEBzPGe3sYbaZW_gMK4iHuM8cseImwLNP8ZIeGaNx5X_hZ6ZOzkjtYJjY85fvaWa2UDGdGlEw3ZO-Nk0Qu_exBrqZgZAsua75TjpJRw01Yd1TNBx5MYuvhltJLsjW-uSjcE-rZoO74FEe9pYYeQjI4",
    "dp": "Qq_wlK4Y_ULRbwoFAZY3Y6xdOGDyofwF_fhwpu8sdDxHq8QV7ZZcM4GOKuJcjsRQyNZv7hxeS_H_h1tnC_igy4KRjtGOdrrnJ1DwVZte72eWqF1LXv73R7pnnfS7AmELuOriruL6Dy1qaXpKGmlyeNazkq5-3tsgXUh0Q7po2AE",
    "alg": "RS256",
    "dq": "Wj1ovDT8lLIZb-Ggby9YotuJT-SSk6UDzHZZikquLGajaD6N2qNILsOKivKXBEzOobN9uj-EHaAXZtbdZyd27cZ2CqORJvJ299b5xLFecXpNGeio1YFee7-c1BjYWfgjMZqgycT1GairizINSjkO3FY8ySSuPBBXhKgrN7eVDrE",
    "n": "kgwP0NPaoAwhSh9iLlRaT7FSRbNsl6T5-j-bB3xAT1UbsxOJ9v06S3_54bpYlEAkjlrO-i1vmSzfSVnqFXnjWThWRvPmBDth3Ka7hQm9UXjiAvTzYxXGFjyhALqa_-DQCtdrqIhi8E4hAuSu--kGgnFKg3G-21KJuqnVzsXrClGkxbmVufx0MJjJxr1YGfkTMG8i0dovS9tnkioDAkt1knupiYk5ir_WiNy4T-70T5s3ktC5_4Uz10hS-rWeUxiihzG8G7ceg84-Kt5jKP_AgUnel-ksRyfgSJCYC9nHyz913a3ALj3Dzt7TBaxwAjlxESrdNz5RE9DNDZfPmNWRSw"
  }
`;

let header = {
  alg: "RS256",
  typ: "JWT",
  kid: "536e453c-aa93-4449-8e90-add2608783c6",
};

let payload = {
  iss: "1234567890",
  sub: "1234567890",
  aud: "https://api.line.me/",
  exp: Math.floor(new Date().getTime() / 1000) + 60 * 30,
  token_exp: 60 * 60 * 24 * 30,
};

jose.JWS.createSign(
  { format: "compact", fields: header },
  JSON.parse(privateKey),
)
  .update(JSON.stringify(payload))
  .final()
  .then((result) => {
    console.log(result);
  });
```

使用您在 header 中指定的演算法，對 Base64url 編碼的 header、Base64url 編碼的 claim set 與私鑰（例如 rsa_private.pem 檔案）進行簽署。Base64url 編碼的結果即為您的 JWT。以下是 JWT 的範例。

```sh
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjJjNjU4NWYzLThkZGQtNDZjNC05YmUyLWI1NGE3MGFhOTRlYSJ9.eyJpc3MiOiIxNjUzOTQ3MTcyIiwic3ViIjoiMTY1Mzk0NzE3MiIsImF1ZCI6Imh0dHBzOi8vYXBpLmxpbmUubWUvIiwiZXhwIjoiMTU4NTIwMDA2MiIsInRva2VuX2V4cCI6IjI1OTIwMDAifQ.UVG6PAEub-OPbZ3nJuVxRRPjY6Sz_eIHJV9DTTAHCR79YsG4yWvoa9AeIctibb6IJQKgTEV7mF7LsUDmXldEDqYwyEmKs38zj_995Ntc9SYBFphHpr09NqfMoqMphwKqms2NOnqgcHreFs27d9Q0Qv8Rtv2t7SB2cVO__KrsjzYNs3miTvDdkqYLXFo5fXwuzNtHOCAJomd6bhMR8Yd1-vJmtMCBPK4hmA98w8fG_NhcyLbw-B9AuxQ6z92zXiRhNyPlK_3ce2T7HtgUluJ4xJl4xdLJ_C6hvTAqtQxmSiJKzbjUiANF6hVBTomU8vkaIjEKjnlT1uPMihfrsA3pzQ
```

#### Generate a JWT with PyJWT (Python library) 

要使用 PyJWT 建立 signature 並產生 JWT，您需要安裝 [Python](https://www.python.org/downloads/) 與 [PyJWT](https://github.com/jpadilla/pyjwt)。

以下範例程式碼使用 PyJWT 以**私鑰**進行簽署以產生 JWT。要使用此程式碼產生您自己的 JWT，請先將 `privateKey` 的值改為您 assertion 簽署金鑰的私鑰。同時也將 `headers` 中的 `kid` 與 `payload` 改為您自己的值，然後執行程式碼。請務必以您的**私鑰**進行簽署，以證明內容未遭竄改。關於用法的詳細資訊，請參閱 [PyJWT](https://github.com/jpadilla/pyjwt#installing)。

```python
import jwt
from jwt.algorithms import RSAAlgorithm
import time

privateKey = {
  "alg": "RS256",
  "d": "dcA-LXLBRecBQbW7a8LKAriFJhnpXzwu2uNoVF_8-QmGVzI5682FWh_CWhl_B6J0fpmA-d7_EP0WCB3AGhxlyTP6ROoYJo7nygb_KMLREM7n64LFGbvNtw4jk7dmISXl_JuEX6CG09BBx4GLh9AGHSaK4v9B-dDvrNZlAo2mIjISHNcAPENbOl_XIOmZpJd56znjjc1gGKaYGbIm8unxHnPhL66IVYGRu8gxKfG6JUP7o370-VDfFOeaAR0HshTycP6M41jcDSjL6z9-J-Sh0zSZXqGS4u82TNtmwtRTzVwd0w30KQ0TTROTiNsz5apVHjpMvmAxRlbvcW41xIq8sQ",
  "dp": "PAWBMzwnwgc-yixarV30gemH6Wk15HfSUYpR4wJZUHemGx_LE5GXdnKoyy8G9DAl6XMpm7YVH8cPXgXYNh-JlAggvzUeH5A7KAV4ZPTNak4CI844GSbYIu_dPBcVAg0O6sxQWugYpPbPnMDpE7qf4KilSSVG3JKqEMxkYySjZZE",
  "dq": "LBA_q2YYnglCL41-1b3BmzCm-hs7Q-N__otDWO01I03VYnzU-vEQmxy6Fzrh2Y4Fgwp6D8iScu42AOyhE-T-qDNbAsCB0iZeFqm84g6VQAfDbknjIUZtcGvQgzy-zlrl253_QdyJvl2b44KT1hfoF0tDNA1rhOy7WlBM__rH0Pc",
  "e": "AQAB",
  "kty": "RSA",
  "n": "x2glWJ7baQV4vdElnAXA5yu8yFk4LpszkHW3Ey-BKGT3kGVLy3Jk3OvkwjBFOglXWeyTWe_rJkMYkBKuon5syZVjrjb24CmViAXGr6d6IvrYWj8IGZ6ElVABfnjGgZMVywmBb7hIh2p8QR0L8UJEuWjBU5nlwkMBpvnY2HXAVhvir8CN7WRj_GBMxxgg7wSuW1tV-7Qf44grMqJ0Je7zjflS4-TpI8Ox3nhamn0d7NIdQ3jNdTP7IZF61IvETgb_6NdFnfsN-aifJC-Ea3ZwhVcEGJ5z3MMoKSoChJmkJMiV9CldqGRnEDWwBugZHeEtn71eGVE3DAXAzrf525YHYQ",
  "p": "7eH8LAzNkITH6t7CWU5tPAmQlGQPkby66Yfq52tSZ43pQRz0CdtDYCQnGoBXvHzAHhzH4MjmNLOSGVimZK_dIRg5lJaPvVe6hgQ3pYud5WzPWsnQTsC7agQ2rfQglyFUtjwd1gWBIY4gwHj4BYG6Up3g0TlX1sf_juZxcLhkOsc",
  "q": "1pf-Pj2ZPL1nGqVcMVH_hfziIOBtjxc5vMGyHwTaLAA9y2xKfe_SRU8kUK2q5ZykJ8wMckR9Pduuyn-vp4q2FANVSN69G01pUKM2ppkgXuil2S3REmzniGdajZjkpWKaZ6z1tJ_xSv9ghx06Dbro8n___KnpBq6afb022anRxJc",
  "qi": "6L6SgH_pkyqq1Tb6QXPAGmtqVZT58Ljf3QTw6Tx5OdZ9NNvDReHHb64MgbUMLhLzGMeXGqDI5j0WLhtXv4ddCKWkF7OeKLUNuRP7yLpyYMazn8TEOjKHsgLAklenxcSgYaoO_wULh1mze1_ZO2PJNgvkIx_Xzr0XDUAqUp4W0jk",
  "use": "sig"
}

headers = {
    "alg": "RS256",
    "typ": "JWT",
    "kid": "9869e446-3489-4516-a83f-ec9214ad94d0"
}

payload = {
  "iss": "1234567890",
  "sub": "1234567890",
  "aud": "https://api.line.me/",
  "exp":int(time.time())+(60 * 30),
  "token_exp": 60 * 60 * 24 * 30
}

key = RSAAlgorithm.from_jwk(privateKey)

JWT = jwt.encode(payload, key, algorithm="RS256", headers=headers, json_encoder=None)
print(JWT)
```

使用您在 header 中指定的演算法，對 Base64url 編碼的 header、Base64url 編碼的 claim set 與私鑰進行簽署。Base64url 編碼的結果即為您的 JWT。以下是 JWT 的範例。

```sh
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6Ijk4NjllNDQ2LTM0ODktNDUxNi1hODNmLWVjOTIxNGFkOTRkMCJ9.eyJpc3MiOiIxMjM0NTY3ODkwIiwic3ViIjoiMTIzNDU2Nzg5MCIsImF1ZCI6Imh0dHBzOi8vYXBpLmxpbmUubWUvIiwiZXhwIjoxNjIzOTk1NTk5LCJ0b2tlbl9leHAiOjI1OTIwMDB9.Zf32xTqgUHSYw2C2Mlmunqz_AtkaqvGh0msx9XJMX6QYLPT4m4QYF3PsER-zfbhbByNT4rH09JEMRP7bzcNMQ8l4n_WXwTyLkNciZYzF-sTiVHiZu4ucJm4_l8ni5NaqOVEntsCp1wQi8-VLjaMpQlQ7crCdouEMFFeyVwgERfH8ui6UZaJeIlJKRZTnO6iYvKYuLyUsqzowfwZo0hcnnZIXKnjZ81ukjH3_78EHXOD5ivovAT7CtmBoglm3Bvsi0N6PlEONLhHqpCleaYTXRmCykxDLP600JRvi5TYApaN-8n2Bo3FskXJLuxquWLP-LTfMDlkakmfEfcQCiz7daQ
```

## Issue a channel access token v2.1 

您可以使用您所[產生](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/#generate-jwt)的 JWT assertion 來[簽發頻道存取權杖 v2.1](https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token-v2-1)。

<!-- note start -->

**使用金鑰 ID 管理頻道存取權杖 v2.1**

- 當您請求頻道存取權杖 v2.1 時，所取得的回應是一組頻道存取權杖與唯一的金鑰 ID（`key_id`）。為了妥善管理頻道存取權杖，請安全地儲存這組頻道存取權杖與金鑰 ID。
- 金鑰 ID 是於 2020 年 6 月 22 日加入 Messaging API 的識別碼。如果您的應用程式使用沒有金鑰 ID 的頻道存取權杖 v2.1，我們建議您重新簽發頻道存取權杖 v2.1，並安全地儲存這組權杖與金鑰 ID。如果您重新簽發頻道存取權杖，請務必更新您的 bot 以使用新的權杖。

<!-- note end -->

取得頻道存取權杖 v2.1 的流程如下：

![](https://developers.line.biz/media/messaging-api/channel-access-token/using_keyID_procedure_01.png)

1. 使用您所產生的 JWT 執行 [Issue channel access token v2.1](https://developers.line.biz/en/reference/messaging-api/#issue-channel-access-token-v2-1) 端點以簽發頻道存取權杖。
2. LINE Platform 回傳一組頻道存取權杖與金鑰 ID 給您。
3. 將這組頻道存取權杖與金鑰 ID 儲存在資料庫或其他地方。

### Revoke channel access token v2.1 

如果您的頻道存取權杖有效，您可以[撤銷頻道存取權杖 v2.1](https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token-v2-1)。

<!-- note start -->

**驗證頻道存取權杖的有效性**

您可以使用無效的頻道存取權杖執行 [Revoke channel access token v2.1](https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token-v2-1) 端點而不會得到錯誤。您可以使用 [Get all valid channel access token key IDs v2.1](https://developers.line.biz/en/reference/messaging-api/#get-all-valid-channel-access-token-key-ids-v2-1) 端點取得有效頻道存取權杖的金鑰 ID。您可以將取得的金鑰 ID 與儲存在資料庫等處的頻道存取權杖與金鑰 ID 配對進行比對，以辨識出有效的存取權杖。

<!-- note end -->

撤銷頻道存取權杖 v2.1 的流程如下：

![](https://developers.line.biz/media/messaging-api/channel-access-token/using_keyID_procedure_02.png)

1. 從您所儲存的 assertion 簽署金鑰重新產生 JWT。
2. 使用該 JWT 執行 [Get all valid channel access token key IDs v2.1](https://developers.line.biz/en/reference/messaging-api/#get-all-valid-channel-access-token-key-ids-v2-1) 端點。
3. LINE Platform 回傳有效頻道存取權杖的金鑰 ID。
4. 對照您資料庫中的金鑰 ID。
5. 檢查您是否有與所回傳的任一金鑰 ID 相符的頻道存取權杖與金鑰 ID 配對。
6. 取得已驗證的頻道存取權杖。
7. 使用該頻道存取權杖執行 [Revoke channel access token v2.1](https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token-v2-1) 端點。
8. LINE Platform 撤銷該頻道存取權杖。
