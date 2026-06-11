# LINE Profile+

<!-- note start -->

**使用選用功能需提出申請**

只有已提交所需申請、位於日本的企業使用者，才能使用本文件所述的功能。若要透過 LINE Login、LIFF App 或 LINE MINI App 使用登錄於 LINE Profile+ 的資訊，請聯絡您的業務代表或[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。對於 LINE MINI App，此功能僅適用於已驗證的 MINI App。

<!-- note end -->

LINE Profile+ 是用於管理 LINE 使用者個人檔案資訊的服務。使用者登錄於 LINE Profile+ 的資訊與一般的[個人檔案資訊（profile information）](https://developers.line.biz/en/glossary/#profile-information)不同，且只有經過申請流程的企業使用者才能取得。

<!-- table of contents -->

## Differences between profile information and LINE Profile+ 

如需 LINE 個人檔案資訊與 LINE Profile+ 之間差異的詳細資訊，請參閱 LINE Platform 基礎中的[取得使用者個人檔案資訊](https://developers.line.biz/en/docs/basics/user-profile/)。

- [什麼是使用者個人檔案資訊](https://developers.line.biz/en/docs/basics/user-profile/#what-is-profile)
- [LINE Profile+](https://developers.line.biz/en/docs/basics/user-profile/#what-is-line-profile-plus)

## Get user data registered with LINE Profile+ 

您可以使用 LIFF App 或 LINE MINI App，或是將 LINE Login 整合到您自己的 Web App 中，來取得登錄於 LINE Profile+ 的資訊。

請依照下列步驟指定您想要取得的資訊範圍（scope），並取得包含 LINE Profile+ 資訊的 ID token 之 payload。

| 步驟 | [透過 LIFF App 或 LINE MINI App](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#liff-mini) | [透過 LINE Login](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#line-login) |
| --- | --- | --- |
| 1. 指定 scope | [在 LINE Developers Console 上指定 scope](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#liff-specify-scope) | [為授權 URL 指定 scope](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#line-login-specify-scope) |
| 2. 取得 ID token payload | [透過 liff.getDecodedIDToken() 取得 ID token payload](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#liff-get-id-token) | [驗證發行存取權杖時取得的 ID token，以取得 ID token payload](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#line-login-get-id-token) |
| 3. 取得 LINE Profile+ 資訊 | [從 ID token payload 取得 LINE Profile+ 資訊](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#liff-get-profile-plus) | [從 ID token payload 取得 LINE Profile+ 資訊](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#line-login-get-profile-plus) |

### Via LIFF App or LINE MINI App 

若要透過 LIFF App 或 LINE MINI App 取得登錄於 LINE Profile+ 的資訊，請在 [LINE Developers Console](https://developers.line.biz/console/) 上設定您想要取得的資訊 [scope](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#scope)，接著取得 ID token payload，即可取得目前已登入使用者的 LINE Profile+ 資訊。

#### 1. Specify scopes on LINE Developers Console 

請事先指定您想要取得的資訊 scope。在 [LINE Developers Console](https://developers.line.biz/console/) 上選取目標頻道（channel），然後在 LINE MINI App 頻道的 **Web app settings** 分頁下的 **Scope** 區塊，或是 LINE Login 頻道的 **LIFF** 分頁中，勾選您想要使用的 scope。

如需透過 LINE Profile+ 可取得的 scope 的詳細資訊，請參閱 [LINE Profile+ scopes](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#scope)。

![profile plus scope](https://developers.line.biz/media/partner-docs/profile_plus_scopes_en.png)

<!-- note start -->

**同時指定 openid**

若要取得登錄於 LINE Profile+ 的資訊，需要 ID token。請同時指定 `openid`，以一併請求取得 ID token 的權限。

<!-- note end -->

#### 2. Get ID token payload via liff.getDecodedIDToken() 

當您執行 LIFF SDK 的 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 方法時，可以取得已解碼的 ID token payload，其中包含 LIFF App 或 LINE MINI App 目前已登入使用者的 LINE Profile+ 資訊。

取得 ID token payload 的範例程式碼：

```javascript
liff.init(() => {
  const idToken = liff.getDecodedIDToken();
  console.log(idToken); // print decoded idToken object
});
```

#### 3. Get LINE Profile+ information from ID token payload 

驗證從步驟 2 取得的 ID token payload 中的 LINE Profile+ 資訊。

LINE Profile+ 資訊範例：

```json
"given_name": "LINE",
"middle_name": "L",
"family_name": "Taro",
"gender": "male",
"birthdate": "1990-01-01",
"phone_number": "+81901111....",
"address": {
    "postal_code": "1028282",
    "region": "Tokyo",
    "locality": "Kioicho, Chiyoda-ku",
    "street_address": "1-3",
    "country": "JP"
}
```

如需 ID token 中所含 LINE Profile+ 資訊的詳細資訊，請參閱 [LINE Profile+ information included in ID token](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#id-token)。

### Via LINE Login 

您可以將 LINE Login v2.1 整合到您的 Web App 中，並使用 [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) 來取得登錄於 LINE Profile+ 的資訊。

本頁僅包含使用 LINE Profile+ 的補充資訊。如需如何整合 LINE Login v2.1 的詳細資訊，請參閱[將 LINE Login 整合到您的 Web App](https://developers.line.biz/en/docs/line-login/integrate-line-login/)。

<!-- note start -->

**備註**

LINE Profile+ 不相容於 LINE Login v2.0 或更早的版本。

<!-- note end -->

#### 1. Specify scopes for authorization URL 

請為授權 URL 的 `scope` 參數指定專用的 scope。

如需透過 LINE Profile+ 可取得的 scope 的詳細資訊，請參閱 [LINE Profile+ scopes](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#scope)。

以下是帶有查詢參數的授權 URL 範例：

```sh
https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%3Fkey%3Dvalue&state=123abc&scope=openid%20profile%20real_name%20gender%20birthdate%20phone%20address&bot_prompt=normal&nonce=0987654asd
```

<!-- note start -->

**同時指定 openid**

若要取得登錄於 LINE Profile+ 的資訊，需要 ID token。請同時指定 `openid`，以一併請求取得 ID token 的權限。

<!-- note end -->

如需使用者存取授權 URL 後的操作詳細資訊，請參閱[驗證流程（Authentication process）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#authentication-process)。

#### 2. Validate ID token obtained when issuing access token to get ID token payload 

登錄於 LINE Profile+ 的資訊包含在 [ID token](https://developers.line.biz/en/docs/line-login/verify-id-token/#id-tokens) 中。在[發行存取權杖](https://developers.line.biz/en/docs/line-login/integrate-line-login/#get-access-token)時，ID token 會包含在回應中。

請求範例：

```sh
curl -v -X POST https://api.line.me/oauth2/v2.1/token \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'grant_type=authorization_code' \
-d 'code=b5fd32eacc791df' \
--data-urlencode 'redirect_uri=https://example.com/auth?key=value' \
-d 'client_id=12345' \
-d 'client_secret=d6524edacc8742aeedf98f'
```

透過[發行存取權杖（Issue access token）](https://developers.line.biz/en/reference/line-login/#issue-access-token)取得的 ID token 是以 Base64 格式編碼（例如 `eyJhbGciOiJIUzI1NiJ9...`）。您可以執行[驗證 ID token（Verify ID token）](https://developers.line.biz/en/reference/line-login/#verify-id-token)，取得以 JSON 格式解碼的 ID token payload。

請求範例：

```sh
curl -v -X POST 'https://api.line.me/oauth2/v2.1/verify' \
 -d 'id_token=eyJraWQiOiIxNmUwNGQ0ZTU2NzgzYTc5MmRjYjQ2ODRkOD...' \
 -d 'client_id=1234567890'
```

#### 3. Get LINE Profile+ information from ID token payload 

驗證從步驟 2 取得的 ID token payload 中的 LINE Profile+ 資訊。

LINE Profile+ 資訊範例：

```json
"given_name": "LINE",
"middle_name": "L",
"family_name": "Taro",
"gender": "male",
"birthdate": "1990-01-01",
"phone_number": "+81901111....",
"address": {
    "postal_code": "1028282",
    "region": "Tokyo",
    "locality": "Kioicho, Chiyoda-ku",
    "street_address": "1-3",
    "country": "JP"
}
```

如需 ID token 中所含 LINE Profile+ 資訊的詳細資訊，請參閱 [LINE Profile+ information included in ID token](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#id-token)。

## LINE Profile+ scopes 

以下是您可透過 LINE Profile+ 取得的資訊 scope：

- `real_name`：取得使用者所登錄之「name（姓名）」的權限
- `gender`：取得使用者所登錄之「gender（性別）」的權限
- `birthdate`：取得使用者所登錄之「birthdate（生日）」的權限
- `phone`：取得使用者所登錄之「phone number（電話號碼）」的權限
- `address`：取得使用者所登錄之「address（地址）」的權限

<!-- note start -->

**備註**

必須事先申請要使用的 scope。

<!-- note end -->

## LINE Profile+ information included in ID token 

您透過 LIFF App、LINE MINI App 或 LINE Login 取得的 ID token，其 payload 中包含所指定 LINE Profile+ scope 的資訊。

#### Payload 

使用 LINE Profile+ 時，會在 ID token 中新增下列屬性。

| 屬性 | 型別 | 說明 | 需要授權的 scope |
| --- | --- | --- | --- |
| `given_name` | String | 名字 | `real_name` |
| `given_name_pronunciation` | String | 名字的假名 | `real_name` |
| `middle_name` | String | 中間名 | `real_name` |
| `family_name` | String | 姓氏 | `real_name` |
| `family_name_pronunciation` | String | 姓氏的假名，為片假名。 | `real_name` |
| `gender` | String | 「male」、「female」或使用者所輸入的值 | `gender` |
| `birthdate` | String | 生日。格式遵循 [RFC3339 protocol](https://www.ietf.org/rfc/rfc3339.txt)。 | `birthdate` |
| `phone_number` | String | 電話號碼。格式遵循 [E.164](https://developers.line.biz/en/glossary/#e164)。 | `phone` |
| `address` | Object | [Address object](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/#address-object) | `address` |

##### Address object 

您最多可在 LINE Profile+ 中登錄 10 筆地址。對於 ID token，您只能取得一筆最近更新或使用的地址。

| 欄位 | 型別 | 說明 |
| --- | --- | --- |
| `postal_code` | String | 郵遞區號。為不含連字號的單位元組數字。此為選填欄位，因此在某些情況下可能會留白。 |
| `region` | String | 州或省 |
| `locality` | String | 城市 |
| `street_address` | String | 在「Street」與「Other」欄位中輸入的值。「Street」與「Other」之間以換行碼（`/n`）分隔。此為選填欄位，因此在某些情況下可能會留白。 |
| `country` | String | 國家名稱。表示方式依循 ISO 3166-1 alpha-2。 |

#### Payload example 

```json
{
  "iss": "https://access.line.me",
  "sub": "U272cada9c6f4c0c933b0713bc2f90f68",
  "aud": "1234567890",
  "exp": 1513142487,
  "iat": 1513138887,
  "name": "LINE taro",
  "picture": "https://profile.line-scdn.net/0h8pWWElvzZ19qLk3ywQYYCFZraTIdAGEXEhx9ak56MDxDHiUIVEEsPBspMG1EGSEPAk4uP01t0m5G",
  "given_name": "LINE",
  "middle_name": "L",
  "family_name": "Taro",
  "gender": "male",
  "birthdate": "1990-01-01",
  "phone_number": "+81901111....",
  "address": {
    "postal_code": "1028282",
    "region": "Tokyo",
    "locality": "Kioicho, Chiyoda-ku",
    "street_address": "1-3",
    "country": "JP"
  }
}
```
