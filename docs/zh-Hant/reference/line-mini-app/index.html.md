# LINE MINI App API 參考文件（LINE MINI App API reference）

## Service Messages 

<!-- tip start -->

**此功能僅供已驗證的 MINI App 使用**

此功能僅供已驗證的 MINI App 使用。對於未驗證的 MINI App，你可以在開發用（Developing）的內部頻道上測試此功能，但無法在已發布（Published）的內部頻道上使用此功能。

<!-- tip end -->

Service Message API 讓你能從你的服務向 LINE MINI App 使用者傳送服務訊息（service message）。

傳送服務訊息需要服務通知權杖（service notification token）以及一個[範本（template）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#service-message-templates)。

- [發行服務通知權杖](https://developers.line.biz/en/reference/line-mini-app/#issue-notification-token)
- [傳送服務訊息](https://developers.line.biz/en/reference/line-mini-app/#send-service-message)

### Issuing a service notification token 

發行服務通知權杖。服務通知權杖用於向關聯的使用者傳送服務訊息。

服務通知權杖具有以下特性：

- 服務通知權杖在發行後 1 年（31,536,000 秒）後到期。在仍有效期間內，最多可傳送 5 則服務訊息。
- 每次使用服務通知權杖時，除非權杖已到期或不再有剩餘的訊息傳送次數，否則權杖值都會更新。如果你計畫向使用者連續傳送服務訊息，請保留更新後的服務通知權杖。

<!-- warning start -->

**請勿使用單一存取權杖發行多個服務通知權杖**

不允許重複使用由 [`liff.getAccessToken()`](https://developers.line.biz/en/reference/liff/#get-access-token) 取得的存取權杖（LIFF 存取權杖）來發行多個服務通知權杖。

每個 LIFF 存取權杖只能發行一個服務通知權杖。

<!-- warning end -->

<!-- note start -->

**注意**

每個服務通知權杖都與一位使用者關聯。你無法使用與某位使用者關聯的服務通知權杖向其他使用者傳送服務訊息。

<!-- note end -->

_請求範例_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/message/v3/notifier/token \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer W1TeHCgfH2Liwa...' \
-d '{
    "liffAccessToken": "eyJhbGciOiJIUzI1NiJ9..."
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/message/v3/notifier/token`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
如需更多資訊，請參閱 LINE Platform 基礎中的[頻道存取權杖（Channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/)。

<!-- parameter end -->

<!-- note start -->

**建議使用無狀態頻道存取權杖**

[長效期頻道存取權杖（Long-lived channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)和[可由使用者指定有效期間的頻道存取權杖（Channel Access Token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)無法用於 LINE MINI App 頻道。

開發 LINE MINI App 時，可使用[無狀態頻道存取權杖（stateless channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)或[短效期頻道存取權杖（short-lived channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)。在這兩者之中建議使用無狀態頻道存取權杖。無狀態頻道存取權杖的發行次數沒有限制，因此應用程式無需管理權杖的生命週期。

<!-- note end -->

#### Request body 

<!-- parameter start (props: required) -->

liffAccessToken

String

由 [`liff.getAccessToken()`](https://developers.line.biz/en/reference/liff/#get-access-token) 取得的使用者存取權杖（LIFF 存取權杖）。

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

notificationToken

String

服務通知權杖

<!-- parameter end -->
<!-- parameter start -->

expiresIn

Number

服務通知權杖到期前剩餘的時間（以秒為單位）。服務通知權杖在發行後 1 年（31,536,000 秒）後到期。

<!-- parameter end -->
<!-- parameter start -->

remainingCount

Number

使用所發行的服務通知權杖可傳送服務訊息的次數

<!-- parameter end -->
<!-- parameter start -->

sessionId

String

工作階段 ID（session ID）。如需更多資訊，請參閱[傳送服務訊息](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "notificationToken": "34c11a03-b726-49e3-8ce0-949387a9..",
  "expiresIn": 31536000,
  "remainingCount": 5,
  "sessionId": "xD06...."
}
```

<!-- tab end -->

#### Error response 

回傳以下其中一種狀態碼與錯誤訊息。

| Status code | Description |
| --- | --- |
| 400 Bad request | 此狀態碼代表以下其中一種情況：<ul><li>請求主體有問題。</li><li>`liffAccessToken` 屬性中指定的 LIFF 存取權杖在短時間內被多次用於請求發行服務通知權杖。</li></ul> |
| 401 Unauthorized | 此狀態碼代表以下其中一種或兩種情況：<ul><li>未指定有效的頻道存取權杖。</li><li>未指定有效的 LIFF 存取權杖。</li><ul><li>當[使用者關閉 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#behavior-when-closing-liff-app) 時，即使 LIFF 存取權杖尚未到期，也會被撤銷。</li></ul></ul> |
| 403 Forbidden | 此頻道未獲授權發行服務訊息。 |
| 500 Internal Server Error | 內部伺服器發生錯誤 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
{
  "message": "[liffAccessToken] must not be blank"
}
```

<!-- tab end -->

### Sending service messages 

向服務通知權杖中指定的使用者傳送服務訊息。

一旦傳送服務訊息，除非權杖已到期或不再有剩餘的訊息傳送次數，否則權杖值都會更新。如果你計畫向使用者連續傳送服務訊息，請保留更新後的服務通知權杖。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/message/v3/notifier/send?target=service \
-H 'Authorization: Bearer W1TeHCgfH2Liwa...' \
-H 'Content-Type: application/json' \
-d '{
    "templateName": "thankyou_msg_en",
    "params": {
        "date": "2020-04-23",
        "username": "Brown & Cony"
    },
    "notificationToken": "34c11a03-b726-49e3-8ce0-949387a9.."
}'
```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/message/v3/notifier/send`

#### Request headers 

<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->
<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
如需更多資訊，請參閱 LINE Platform 基礎中的[頻道存取權杖（Channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/)。

<!-- parameter end -->

<!-- note start -->

**建議使用無狀態頻道存取權杖**

[長效期頻道存取權杖（Long-lived channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)和[可由使用者指定有效期間的頻道存取權杖（Channel Access Token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)無法用於 LINE MINI App 頻道。

開發 LINE MINI App 時，可使用[無狀態頻道存取權杖（stateless channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)或[短效期頻道存取權杖（short-lived channel access tokens）](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)。在這兩者之中建議使用無狀態頻道存取權杖。無狀態頻道存取權杖的發行次數沒有限制，因此應用程式無需管理權杖的生命週期。

<!-- note end -->

#### Query parameters 

<!-- parameter start (props: required) -->

target

`service`

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

templateName

String

已新增並將用於服務訊息的範本名稱。你可以在 LINE Developers Console 中查看範本名稱。如需更多資訊，請參閱[可傳送的服務訊息類型](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#types-of-service-messages-that-can-be-sent)。\
請搭配 BCP 47 語言標籤後綴一起使用。\
格式：`{template name}_{BCP 47 language tag}`\
字元數上限：30

<!-- note start -->

**注意**

服務訊息支援的語言與語言標籤如下。

- 日文：`ja`
- 英文：`en`
- 中文（繁體）：`zh-TW`
- 泰文：`th`
- 印尼文：`id`
- 韓文：`ko`

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: required) -->

params

object

用於指定每個範本變數與值配對的 JSON 物件。\
如果範本沒有範本變數，請指定一個空的 JSON 物件（`{ }`）。\
範本變數是為每個範本各自定義的。如果某個範本變數屬於必填元素，請務必指定該範本變數與值配對。\
如需更多資訊，請參閱[將服務訊息範本新增至頻道](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#service-message-templates)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

notificationToken

String

服務通知權杖

<!-- parameter end -->

#### Response 

回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

notificationToken

String

更新後的服務通知權杖。使用此服務通知權杖來連續傳送服務訊息。

<!-- parameter end -->
<!-- parameter start -->

expiresIn

Number

更新後的服務通知權杖到期前剩餘的時間（以秒為單位）

<!-- parameter end -->
<!-- parameter start -->

remainingCount

Number

使用更新後的服務通知權杖可連續傳送服務訊息的次數。

<!-- parameter end -->
<!-- parameter start -->

sessionId

String

工作階段 ID（session ID）。如需更多資訊，請參閱[傳送服務訊息](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)。

<!-- parameter end -->

<!-- note start -->

**注意**

如果 `expiresIn` 與 `remainingCount` 的值皆為 `0`，代表服務訊息已傳送，但服務通知權杖無法更新。

<!-- note end -->

_回應範例_

<!-- tab start `json` -->

```json
// Request was successful,
// renewed service notification
// token issued
{
  "notificationToken": "c9884874-bf6a-4241-8999-2767241c...",
  "expiresIn": 31535906,
  "remainingCount": 3,
  "sessionId": "xD06...."
}

// Request was successful,
// the service message
// was sent, but the LINE Platform
// cannot renew the token
{
  "expiresIn": 0,
  "remainingCount": 0
}
```

<!-- tab end -->

#### Error response 

回傳以下其中一種狀態碼與錯誤訊息。

| Status code | Description |
| --- | --- |
| 400 Bad request | 此狀態碼代表以下其中一種情況：<ul><li>請求主體有問題。</li><li>服務訊息的目標收件者不存在。</li></ul> |
| 401 Unauthorized | 此狀態碼代表以下其中一種或兩種情況：<ul><li>未指定有效的頻道存取權杖。</li><li>未指定有效的服務通知權杖。</li></ul> |
| 403 Forbidden | 此狀態碼代表以下其中一種情況：<ul><li>此頻道未獲授權傳送服務訊息。</li><li>找不到指定的範本。</li></ul> |

_錯誤回應範例_

<!-- tab start `json` -->

```json
{
  "message": "Invalid notifier token"
}
```

<!-- tab end -->

## Common Profile Quick-fill 

<!-- tip start -->

**僅供已驗證的 MINI App 使用**

若要使用 Common Profile Quick-fill，你的 LINE MINI App 必須已通過驗證，且你必須申請使用 Quick-fill。如需更多資訊，請參閱[使用 Quick-fill 的步驟](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process)。

<!-- tip end -->

Quick-fill 是一項功能，使用者只要在 LINE MINI App 上輕觸 **Auto-fill** 按鈕，即可自動填入所需的個人資料資訊。你可以輕鬆在 LINE MINI App 中使用使用者於 Account Center 設定的 Common Profile 資訊。如需更多資訊，請參閱 [Common Profile Quick-fill 概觀](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/)。

### liff.$commonProfile.get() 

取得使用者於 Account Center 設定的 Common Profile 中的資訊。

當你執行 `liff.$commonProfile.get()` 方法時，會出現一個用於確認使用者個人資料的對話框（modal）。使用者在所顯示的對話框中確認個人資料後，即可輕觸 **Auto-fill**，個人資料資訊便會自動填入。

對話框顯示範例：

![](https://developers.line.biz/media/line-mini-app/quick-fill/quick-fill-modal-screen.png)

_範例_

<!-- tab start `javascript` -->

```javascript
const { data, error } = await liff.$commonProfile.get(
  ["family-name", "given-name", "email", "tel", "postal-code"],
  {
    formatOptions: {
      givenName: {
        excludeEmojis: false,
      },
      tel: {
        excludeNonJp: false,
      },
      postalCode: {
        digitsOnly: false,
      },
    },
  },
);
console.log(data);
console.log(error);
```

<!-- tab end -->

#### Syntax 

```javascript
liff.$commonProfile.get(scopes, options);
```

#### Arguments 

<!-- parameter start (props: required) -->

scopes

Array of strings

指定你想取得的 Common Profile 的範圍（scope）。

如需 `scopes` 可指定的值的相關資訊，請參閱[可指定的 `scopes` 參數及其回傳值](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#common-profile-scope)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

options

Object

取得 Common Profile 資訊的選項

<!-- parameter end -->
<!-- parameter start (props: optional) -->

options.formatOptions

Object

與資訊格式相關的選項。請為 `scopes` 屬性中指定的每個範圍指定一個 [`formatOptions` 物件](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile-format-options)。

請以駝峰式命名（camel case）格式將你想設定選項的範圍指定為鍵（key）。例如，當範圍為 `given-name` 時，鍵為 `givenName`。

<!-- parameter end -->

#### `formatOptions` object 

<!-- parameter start (props: optional) -->

excludeEmojis

Boolean

是否從字串中移除表情符號（emoji）。預設為 `true`。此選項只能在以下範圍中指定：

- givenName
- familyName

<!-- parameter end -->
<!-- parameter start (props: optional) -->

excludeNonJp

Boolean

是否排除 12 位數或以上的電話號碼。預設為 `true`。如果為 `true`，當電話號碼為 12 位數或以上時，會回傳空字串與錯誤資訊。此選項只能在以下範圍中指定：

- tel

<!-- parameter end -->
<!-- parameter start (props: optional) -->

digitsOnly

Boolean

是否排除包含非數字字元的郵遞區號。預設為 `true`。如果為 `true`，當郵遞區號包含數字以外的字元時，會回傳空字串與錯誤資訊。此選項只能在以下範圍中指定：

- postalCode

<!-- parameter end -->

_範例_

<!-- tab start `javascript` -->

```javascript
{
  givenName: {
    excludeEmojis: false,
  },
  tel: {
    excludeNonJp: false,
  },
  postalCode: {
    digitsOnly: false,
  },
}
```

<!-- tab end -->

#### Return value 

回傳 `{ data: Partial<CommonProfile>, error: Partial<CommonProfileError>}` 類型的 `Promise` 物件。

當 `Promise` 解析（resolve）時，包含使用者 Common Profile 資訊、類型為 `Partial<CommonProfile>` 的物件會傳遞至 `data` 屬性，而包含錯誤資訊、類型為 `Partial<CommonProfileError>` 的物件會傳遞至 `error` 屬性。

在以下情況中，`data` 的屬性會是 `undefined` 或 `null`：

- 屬性值變為 `undefined` 的情況
  - 如果目標項目未在 `scopes` 參數中指定
  - 如果目標項目已在 `scopes` 參數中指定，但使用者未授權該項目的權限
- 屬性值變為 `null` 的情況
  - 如果使用者尚未在 Common Profile 中為目標項目設定值
  - 如果在 Common Profile 中擷取目標項目時發生錯誤

如需依照所指定的 `scopes` 可取得的屬性值的相關資訊，請參閱[可指定的 `scopes` 參數及其回傳值](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#common-profile-scope)。

_`Partial<CommonProfile>` 類型物件的範例_

<!-- tab start `json` -->

```javascript
{
  "family-name": "Yamada",
  "given-name": "Taro",
  "email": "sample@example.com",
  "tel": "09001234567",
  "postal-code": "1020094"
}
```

<!-- tab end -->

_`Partial<CommonProfileError>` 類型物件的範例_

<!-- tab start `json` -->

```javascript
{
  "tel": ["Phone number has 12 or more digits"],
  "postal-code": ["Postal code contains non-numeric characters"]
}
```

<!-- tab end -->

#### Error response 

當 `Promise` 被拒絕（reject）時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

_未正確安裝外掛程式即呼叫 API 的範例_

<!-- tab start `javascript` -->

```javascript
new Error(
  "LiffCommonProfilePlugin isn't installed properly. Did you call liff.use(new LiffCommonProfilePlugin()) before using it?"
);
```

<!-- tab end -->

_在 LIFF 瀏覽器以外的瀏覽器呼叫 API 的範例_

<!-- tab start `javascript` -->

```javascript
new Error("liff.$commonProfile API is available only in LIFF browser.");
```

<!-- tab end -->

### liff.$commonProfile.getDummy() 

取得 Common Profile 的虛擬資料（dummy data）。共有 10 種虛擬資料可用，你可以使用 `caseId` 指定要取得的虛擬資料。

當你執行 `liff.$commonProfile.getDummy()` 方法時，會出現一個用於確認虛擬個人資料的對話框。你可以輕觸 **Auto-fill** 來取得 Common Profile 的虛擬資料。

對話框顯示範例：

![](https://developers.line.biz/media/line-mini-app/quick-fill/quick-fill-dummy-modal-screen.png)

_範例_

<!-- tab start `javascript` -->

```javascript
const { data, error } = await liff.$commonProfile.getDummy(
  ["family-name", "given-name", "email", "tel", "postal-code"],
  {
    formatOptions: {
      givenName: {
        excludeEmojis: false,
      },
      tel: {
        excludeNonJp: false,
      },
      postalCode: {
        digitsOnly: false,
      },
    },
  },
  1,
);
console.log(data);
console.log(error);
```

<!-- tab end -->

#### Syntax 

```javascript
liff.$commonProfile.getDummy(scopes, options, caseId);
```

#### Arguments 

<!-- parameter start (props: required) -->

scopes

Array of strings

指定你想取得的 Common Profile 的範圍。

如需 `scopes` 可指定的值的相關資訊，請參閱[可指定的 `scopes` 參數及其回傳值](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#common-profile-scope)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

options

Object

取得 Common Profile 資訊的選項

<!-- parameter end -->
<!-- parameter start (props: optional) -->

options.formatOptions

Object

與資訊格式相關的選項。請為 `scopes` 屬性中指定的每個範圍指定一個 [`formatOptions` 物件](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile-format-options)。

請以駝峰式命名（camel case）格式將你想設定選項的範圍指定為鍵（key）。例如，當範圍為 `given-name` 時，鍵為 `givenName`。

<!-- parameter end -->
<!-- parameter start (props: required) -->

caseId

number

指定你想取得的虛擬資料的 ID。可使用 ID 從 `1` 到 `10` 的虛擬資料。

如需各 `caseId` 對應虛擬資料的相關資訊，請參閱[可取得的 Common Profile 虛擬資料](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#get-dummy-common-profile)。

<!-- parameter end -->

#### Return value 

回傳 `{ data: Partial<CommonProfile>, error: Partial<CommonProfileError>}` 類型的 `Promise` 物件。

當 `Promise` 解析時，包含 Common Profile 虛擬資料、類型為 `Partial<CommonProfile>` 的物件會傳遞至 `data` 屬性，而包含錯誤資訊、類型為 `Partial<CommonProfileError>` 的物件會傳遞至 `error` 屬性。

在以下情況中，`data` 的屬性會是 `undefined` 或 `null`：

- 屬性值變為 `undefined` 的情況
  - 如果目標項目未在 `scopes` 參數中指定
- 屬性值變為 `null` 的情況
  - 如果虛擬資料沒有目標項目的值

如需依照所指定的 ID 可取得的虛擬資料的相關資訊，請參閱[可取得的 Common Profile 虛擬資料](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#get-dummy-common-profile)。

_`Partial<CommonProfile>` 類型物件的範例_

<!-- tab start `json` -->

```javascript
{
  "family-name": "見本田",
  "given-name": "見本夫",
  "family-name-kana": "ダミータ",
  "given-name-kana": "ダミーオ",
  "sex-enum": 0,
  "bday-day": 12,
  "bday-month": 3,
  "bday-year": 1998,
  "tel": "09001234567",
  "email": "dummy_39@yahoo.co.jp",
  "postal-code": "1020094",
  "address-level1": "東京都",
  "address-level2": "千代田区",
  "address-level3": "紀尾井町1-2",
  "address-level4": "東京ガーデンテラス紀尾井町"
}
```

<!-- tab end -->

_`Partial<CommonProfileError>` 類型物件的範例_

<!-- tab start `json` -->

```javascript
{
  "tel": ["Phone number has 12 or more digits"],
  "postal-code": ["Postal code contains non-numeric characters"]
}
```

<!-- tab end -->

##### Error response 

當 `Promise` 被拒絕時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-errors)。

_未正確安裝外掛程式即呼叫 API 的範例_

<!-- tab start `javascript` -->

```javascript
new Error(
  "LiffCommonProfilePlugin isn't installed properly. Did you call liff.use(new LiffCommonProfilePlugin()) before using it?"
);
```

<!-- tab end -->

_在 LIFF 瀏覽器以外的瀏覽器呼叫 API 的範例_

<!-- tab start `javascript` -->

```javascript
new Error("liff.$commonProfile API is available only in LIFF browser.");
```

<!-- tab end -->

### liff.$commonProfile.fill() 

使用你已取得的 Common Profile 資訊自動填入表單。`data-liff-autocomplete` 屬性用於將各個人資料資訊連結至表單。

<!-- tip start -->

**自動填入與範圍不符的情況**

使用 `liff.$commonProfile.fill()` 進行的自動輸入，是透過表單的 `data-liff-autocomplete` 屬性執行的。此時，表單 `data-liff-autocomplete` 屬性中指定的值必須與所取得的個人資料資訊的範圍（`family-name`、`tel`、`bday-year` 等）相符。

例如，如果你想在擷取出生年份（`bday-year`）、出生月份（`bday-month`）與出生日期（`bday-day`）資訊後，將其處理成如 `20110623` 的格式再自動填入表單，你可以使用 `document.getElementById().value` 或 `document.querySelector().value`，而非 `liff.$commonProfile.fill()`。

<!-- tip end -->

_依原樣自動填入姓氏、電話號碼和性別的範例_

<!-- tab start `javascript` -->

```javascript
// HTML
<input type="text" data-liff-autocomplete="family-name" />
<input type="tel" data-liff-autocomplete="tel" />
<select data-liff-autocomplete="sex-enum">
  <option value="0">男性</option>
  <option value="1">女性</option>
  <option value="2">回答なし</option>
  <option value="3">その他</option>
</select>

// JavaScript
const { data, error } = await liff.$commonProfile.get([
  "family-name",
  "tel",
  "sex-enum",
]);

liff.$commonProfile.fill(data);
```

<!-- tab end -->

_將部分已取得的 Common Profile 資訊以稍微不同的格式自動填入的範例_

<!-- tab start `javascript` -->

```javascript
// HTML
<input type="text" data-liff-autocomplete="bday-year" />
<input type="text" data-liff-autocomplete="bday-month" />
<input type="text" data-liff-autocomplete="bday-day" />

// JavaScript
const { data, error } = await liff.$commonProfile.get([
  "bday-year",
  "bday-month",
  "bday-day",
]);

const year = data["bday-year"];
const month = data["bday-month"];
const day = data["bday-day"];

// If the month or day is one digit, pad with 0s to
const formattedMonth = month.toString().padStart(2, '0');
const formattedDay = day.toString().padStart(2, '0');

// Automatically fills the value after processing
liff.$commonProfile.fill({
  "bday-year": year,
  "bday-month": formattedMonth,
  "bday-day": formattedDay,
});
```

<!-- tab end -->

#### Syntax 

```javascript
liff.$commonProfile.fill(profile);
```

#### Arguments 

<!-- parameter start (props: required) -->

profile

Partial\<CommonProfile\>

以 `Partial<CommonProfile>` 類型指定要自動填入表單的個人資料資訊。

如需可指定的 `scopes` 的相關資訊，請參閱[可指定的 `scopes` 參數及其回傳值](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#common-profile-scope)。

<!-- parameter end -->

#### Return value 

無

## In-app purchase (Client) 

<!-- tip start -->

**使用應用程式內購買功能需先申請**

若要使用應用程式內購買（in-app purchase）功能，你必須申請使用。如需更多資訊，請參閱 LINE MINI App 文件中的[應用程式內購買概觀](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)。

<!-- tip end -->

### liff.iap.getPlatformProducts() 

取得可透過應用程式內購買購買的項目清單。

_範例_

<!-- tab start `javascript` -->

```javascript
const productIds = ["iap_ln_002", "iap_ln_003"];
liff.iap
  .getPlatformProducts({ productIds })
  .then((products) => {
    console.log(products);
  })
  .catch((err) => {
    console.error(err);
  });
```

<!-- tab end -->

#### Syntax 

```javascript
liff.iap.getPlatformProducts({ productIds });
```

#### Arguments 

<!-- parameter start (props: required) -->

productIds

Array of strings

你想擷取的項目的[商品 ID（product ID）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-product-id/)陣列

<!-- parameter end -->

#### Return value 

回傳一個 `Promise` 物件。當 `Promise` 物件解析時，會傳遞一個以商品 ID 為鍵、並具有以下屬性的物件：

<!-- parameter start -->

currency

String

ISO 4217 格式的貨幣代碼。會以本地化為使用者所使用的應用程式商店所在地區的貨幣回傳。

<!-- parameter end -->
<!-- parameter start -->

price

Number

項目的價格。會以本地化為使用者所使用的應用程式商店所在地區的貨幣回傳。

<!-- parameter end -->
<!-- parameter start -->

productName

String

項目的名稱。會以本地化為使用者所使用的應用程式商店所在地區的表示形式回傳。

<!-- parameter end -->

_回傳值範例_

<!-- tab start `json` -->

```json
{
  "iap_ln_002": {
    "currency": "JPY",
    "price": 100,
    "productName": "LINE Purchase 100"
  }
}
```

<!-- tab end -->

#### Error response 

當 `Promise` 被拒絕時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-error-object)。

可能發生的錯誤包括以下：

| Error message | Description |
| --- | --- |
| Need access_token for api call, Please login first | 使用者尚未登入。 |
| In-App Purchase is not allowed in external browser | 此方法是在外部瀏覽器中執行的。 |
| In-App Purchase is not allowed in this LIFF app | 使用者執行的 LINE MINI App 不支援應用程式內購買。 |

### liff.iap.requestConsentAgreement() 

請求使用者同意「[LINE 應用程式內購買系統使用條款（Terms of Use: LINE In-App Purchase System）](https://terms.line.me/line_iap_tou_1?lang=en)」。

如果使用者尚未同意「LINE 應用程式內購買系統使用條款」，或需要重新取得同意時，會顯示同意畫面。

<!-- tip start -->

**請務必檢查最新的同意狀態**

如果「[LINE 應用程式內購買系統使用條款](https://terms.line.me/line_iap_tou_1?lang=en)」更新，將需要重新取得同意。在開始應用程式內購買之前，請務必呼叫此方法以檢查最新的同意狀態。

<!-- tip end -->

#### Syntax 

```javascript
await liff.iap.requestConsentAgreement();
```

#### Arguments 

無

#### Return value 

回傳一個 `Promise` 物件。

- 如果使用者同意，則解析。
- 如果使用者不同意，或因網路問題、使用者裝置上的問題或 LINE Platform 的內部錯誤導致操作失敗，則以錯誤物件拒絕。

#### Error response 

當 `Promise` 被拒絕時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-error-object)。

可能發生的錯誤包括以下：

| Error message | Description |
| --- | --- |
| The user did not agree to the terms. | 使用者未同意「[LINE 應用程式內購買系統使用條款](https://terms.line.me/line_iap_tou_1?lang=en)」。 |
| Need access_token for api call, Please login first | 使用者尚未登入。 |
| In-App Purchase is not allowed in external browser | 此方法是在外部瀏覽器中執行的。 |
| In-App Purchase is not allowed in this LIFF app | 使用者執行的 LINE MINI App 不支援應用程式內購買。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
{
  "code": "TERMS_AGREEMENT_ERROR",
  "message": "The user did not agree to the terms."
}
```

<!-- tab end -->

### liff.iap.createPayment() 

啟動應用程式商店（App Store、Google Play）的付款確認畫面，並開始購買交易。

#### Syntax 

```javascript
liff.iap.createPayment({ productId, orderId });
```

#### Arguments 

<!-- parameter start (props: required) -->

productId

String

預先定義的[商品 ID（product ID）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-product-id/)

<!-- parameter end -->

<!-- parameter start (props: required) -->

orderId

String

從「[預約購買（Reserve purchase）](https://developers.line.biz/en/reference/line-mini-app/#reserve-purchase)」端點取得的訂單 ID

<!-- parameter end -->

#### Return value 

回傳一個 `Promise<void>` 物件。

- 如果購買成功完成，則解析。
- 如果購買被取消，或因網路問題、使用者裝置上的問題或 LINE Platform 的內部錯誤導致操作失敗，則以錯誤物件拒絕。

#### Error response 

當 `Promise` 被拒絕時，會傳遞 [`LiffError`](https://developers.line.biz/en/reference/liff/#liff-error-object)。

可能發生的錯誤包括以下：

| Error message | Description |
| --- | --- |
| Need access_token for api call, Please login first | 使用者尚未登入。 |
| In-App Purchase is not allowed in external browser | 此方法是在外部瀏覽器中執行的。 |
| In-App Purchase is not allowed in this LIFF app | 使用者執行的 LINE MINI App 不支援應用程式內購買。 |

## In-app purchase (Server) 

<!-- tip start -->

**使用應用程式內購買功能需先申請**

若要使用應用程式內購買功能，你必須申請使用。如需更多資訊，請參閱 LINE MINI App 文件中的[應用程式內購買概觀](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)。

<!-- tip end -->

### Response headers 

應用程式內購買的回應包含以下 HTTP 標頭。請將其儲存至記錄檔，以便日後向 LY Corporation 詢問時參考。

| Response header   | Description                                        |
| ----------------- | -------------------------------------------------- |
| x-line-request-id | 請求 ID。為每個請求所發行的 ID。 |

### Error response 

當 HTTP 狀態碼為 4xx 或 5xx 時，會回傳包含以下 JSON 資料的回應主體：

<!-- parameter start (props: required) -->

errorCode

String

錯誤代碼

<!-- parameter end -->
<!-- parameter start (props: required) -->

message

String

錯誤訊息

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

details

array

錯誤詳細資訊

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

details\[].message

String

詳細訊息

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

details\[].property

String

發生錯誤的位置

<!-- parameter end -->

_錯誤回應範例_

當 HTTP 狀態碼為 4xx 時

<!-- tab start `json` -->

```json
{
  "errorCode": "VALIDATION_ERROR",
  "message": "Request validation failed.",
  "details": [
    {
      "message": "'clientOs' must be 'android' or 'ios'. Actually received: 'INVALID'",
      "property": "clientOs"
    }
  ]
}
```

<!-- tab end -->

當 HTTP 狀態碼為 5xx 時

<!-- tab start `json` -->

```json
{
  "errorCode": "INTERNAL_SERVER_ERROR",
  "message": "An internal server error occurred."
}
```

<!-- tab end -->

### Reserve purchase 

在開始應用程式商店付款之前預約購買。

[回應](https://developers.line.biz/en/reference/line-mini-app/#reserve-purchase-response)中包含的訂單 ID（`orderId`）也會包含在[購買完成事件（purchase complete event）](https://developers.line.biz/en/reference/line-mini-app/#purchase-complete-event)中。向 LY Corporation 詢問與調查時需要訂單 ID，因此請務必儲存。

此外，預約成功並不保證購買完成，因此請依據購買完成事件來授予項目。

_請求範例_

<!-- tab start `shell` -->

```sh
curl -X POST https://api.line.me/iap/v1/product/reserve \
-H "Authorization: Bearer {UserAccessToken}" \
-H "Content-Type: application/json" \
-d '{
"clientIp": "192.168.1.1",
"clientOs": "android",
"productId": "iap_ln_002",
"shopProductName": "Premium Package"
}'

```

<!-- tab end -->

#### HTTP request 

`POST https://api.line.me/iap/v1/product/reserve`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{user access token}`

目前使用者的存取權杖。可使用 [`liff.getAccessToken()`](https://developers.line.biz/en/reference/liff/#get-access-token) 方法取得。

<!-- parameter end -->
<!-- parameter start (props: required) -->

Content-Type

application/json

<!-- parameter end -->

#### Request body 

<!-- parameter start (props: required) -->

clientIp

String

從伺服器取得的使用者裝置 IP 位址。請以 IPv4 或 IPv6 格式指定。

<!-- parameter end -->
<!-- parameter start (props: required) -->

clientOs

String

從 [`liff.getOS()`](https://developers.line.biz/en/reference/liff/#get-os) 方法取得的值。為 `ios` 或 `android`。

<!-- parameter end -->
<!-- parameter start (props: required) -->

productId

String

要購買項目的[商品 ID（product ID）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-product-id/)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

shopProductName

String

顯示在購買記錄中的項目名稱。

不可使用表情符號與符號。請設定適當的值，讓使用者能辨識他們所購買的項目。

字元數上限：20（UTF-16）

<!-- parameter end -->

#### Response 

回傳包含狀態碼 `200` 以及以下資訊的 JSON 物件：

<!-- parameter start -->

orderId

String

訂單 ID。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{ "orderId": "T2025020710000002126002" }
```

<!-- tab end -->

#### Error response 

如需錯誤回應格式的更多資訊，請參閱[錯誤回應](https://developers.line.biz/en/reference/line-mini-app/#iap-error-responses)。

除了一般錯誤外，可能發生的錯誤包括以下：

| Error code | Description |
| --- | --- |
| VALIDATION_ERROR | 未符合請求限制。例如，傳遞給 `clientOs` 的值不是 `ios` 或 `android`。 |
| WEBHOOK_URL_IS_NOT_SET | 未設定用於接收付款完成通知的 webhook URL。 |
| PRODUCT_ID_NOT_FOUND | 所請求的[商品 ID（product ID）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-product-id/)不存在。 |
| BLOCKED_USER | 此使用者已被 LINE Platform 判定為詐欺使用者。與此使用者相關的請求無法被處理。 |
| INTERNAL_SERVER_ERROR | LINE Platform 發生暫時性問題。對於可重試的端點，請使用指數退避（exponential backoff）或類似方法重試。 |
| TERMS_AGREEMENT_ERROR | 當此使用者在「[取得使用者對應用程式內購買的同意](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/implement-in-app-purchase/#get-user-consent)」中尚未同意最新的條款與條件時發生。 |

_錯誤回應範例_

<!-- tab start `json` -->

```json
{
  "errorCode": "VALIDATION_ERROR",
  "message": "Request validation failed.",
  "details": [
    {
      "message": "'clientOs' must be 'android' or 'ios'. Actually received: 'INVALID'",
      "property": "clientOs"
    }
  ]
}
```

<!-- tab end -->

### Get webhook event history 

取得 LINE Platform 傳送的 webhook 事件記錄。你可以使用基於游標的分頁（cursor-based pagination）一次擷取最多 100 個事件。

排序順序是依照 LINE Platform 開始傳送 webhook 事件的日期與時間升冪排列。

你只能擷取過去 7 天內傳送的 webhook 事件。目前僅提供[購買完成事件（purchase complete events）](https://developers.line.biz/en/reference/line-mini-app/#purchase-complete-event)，未來將支援[退款事件（refund events）](https://developers.line.biz/en/reference/line-mini-app/#refund-event)。

_請求範例_

<!-- tab start `shell` -->

```sh
curl "https://api.line.me/iap/v1/webhook/events?startEpochSeconds=1747330438&endEpochSeconds=1747708454&pageSize=10" \
  -H "Authorization: Bearer {ChannelAccessToken}"

```

<!-- tab end -->

#### HTTP request 

`GET https://api.line.me/iap/v1/webhook/events`

#### Request headers 

<!-- parameter start (props: required) -->

Authorization

Bearer `{channel access token}`\
如需更多資訊，請參閱 LINE Platform 基礎中的[頻道存取權杖（Channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/)。

<!-- parameter end -->

#### Query parameters 

<!-- parameter start (props: required) -->

startEpochSeconds

Number

指定你想擷取 webhook 事件記錄的期間起始日期與時間。指定的日期與時間會包含在擷取目標內。請指定過去 7 天內的 UNIX 時間（以秒為單位）。

<!-- parameter end -->
<!-- parameter start (props: required) -->

endEpochSeconds

Number

指定你想擷取 webhook 事件記錄的期間結束日期與時間。指定的日期與時間會包含在擷取目標內。請指定過去 7 天內的 UNIX 時間（以秒為單位）。

<!-- parameter end -->
<!-- parameter start -->

cursor

String

webhook 事件頁面的游標（cursor）。\
請勿在第一次請求中指定此參數。從第二次及後續請求開始，你可以指定前一次請求回應中包含的 `nextCursor` 值，以擷取後續的 webhook 事件。

<!-- parameter end -->
<!-- parameter start (props: required) -->

pageSize

Number

每頁的 webhook 事件數量。<br> <ul><li>最小值：1</li><li>最大值：100</li></ul>

<!-- parameter end -->
<!-- parameter start -->

status

String

你想擷取的 webhook 事件狀態。請指定以下其中之一：

- `SUCCESS`：擷取成功接收的 webhook 事件記錄。
- `FAILED`：擷取接收失敗的 webhook 事件記錄。

如果未指定，則無論接收成功或失敗，皆會擷取所有 webhook 事件的記錄。

<!-- parameter end -->

<!-- note start -->

**分頁期間請勿變更 cursor 以外的參數**

在分頁期間，請在不變更 `cursor` 以外參數的情況下發出請求。如果你想變更參數，請從第一頁重新開始。

<!-- note end -->

#### Response 

成功時，回傳狀態碼 `200` 以及包含以下資訊的 JSON 物件。

<!-- parameter start -->

events

Array

webhook 事件清單。

<!-- parameter end -->
<!-- parameter start -->

events\[].transactionType

String

一律回傳 `PRODUCT`。

<!-- parameter end -->
<!-- parameter start -->

events[].event

Object

[Webhook 事件物件](https://developers.line.biz/en/reference/line-mini-app/#purchase-complete-payload)。

<!-- parameter end -->
<!-- parameter start (props: annotation="Not always included") -->

nextCursor

String

下一頁的游標。\
如果下一頁不存在，則值為 `null`。

<!-- parameter end -->

_回應範例_

<!-- tab start `json` -->

```json
{
  "events": [
    {
      "transactionType": "PRODUCT",
      "event": {
        "type": "purchaseComplete",
        "orderId": "T2025020710000002126002",
        "productId": "iap_ln_002",
        "userId": "U91FC5A...",
        "purchaseTimestamp": 1738672496,
        "channelId": "12345..."
      }
    }
  ],
  "nextCursor": "MTY3NjU0"
}
```

<!-- tab end -->

#### Error responses 

如需錯誤回應格式的更多資訊，請參閱[錯誤回應](https://developers.line.biz/en/reference/line-mini-app/#iap-error-responses)。

除了一般錯誤外，可能發生的錯誤包括以下：

| Error code | Description |
| --- | --- |
| VALIDATION_ERROR | 未符合請求限制。例如，傳遞給 `status` 的值不是 `SUCCESS` 或 `FAILED`。 |
| INTERNAL_SERVER_ERROR | LINE Platform 發生暫時性問題。對於允許重試的端點，請使用指數退避（exponential backoff）或類似方法重試。 |

## In-app purchase webhook event object 

<!-- tip start -->

**使用應用程式內購買功能需先申請**

若要使用應用程式內購買功能，你必須申請使用。如需更多資訊，請參閱 LINE MINI App 文件中的[應用程式內購買概觀](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)。

<!-- tip end -->

### Verify signature 

當你的 LINE MINI App 伺服器收到 webhook 請求時，請在處理 webhook 事件之前先驗證請求標頭中包含的簽章（signature）。此驗證步驟很重要，可用於確認 webhook 來自 LINE Platform，且在傳輸過程中未遭竄改。

如需更多資訊，請參閱 Messaging API 文件中的[驗證 webhook 簽章](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/)。

### Purchase complete event 

當使用者在應用程式商店（App Store、Google Play）購買已預約的項目，且付款由 LY Corporation 結算時，會發生此事件。webhook payload 包含所購買項目的相關資訊。

#### Webhook payload 

<!-- parameter start -->

type

String

webhook 事件的類型。\
指定為 `purchaseComplete`。

<!-- parameter end -->
<!-- parameter start -->

orderId

String

使用者所購買訂單的 ID。包含在「[預約購買（Reserve purchase）](https://developers.line.biz/en/reference/line-mini-app/#reserve-purchase)」端點的回應中。

<!-- parameter end -->
<!-- parameter start -->

productId

String

使用者所購買項目的商品 ID（[`productId`](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-product-id/)）。

<!-- parameter end -->
<!-- parameter start -->

userId

String

進行購買的使用者的使用者 ID。

<!-- parameter end -->
<!-- parameter start -->

purchaseTimestamp

number

在 LINE Platform 上完成付款的時間。單位為 UNIX 時間（以秒為單位）。

此時間並非使用者實際完成付款的時間。

<!-- parameter end -->
<!-- parameter start -->

channelId

String

LINE MINI App 頻道的頻道 ID。

<!-- parameter end -->

_範例_

<!-- tab start `json` -->

```json
{
  "type": "purchaseComplete",
  "orderId": "T2025020710000002126002",
  "productId": "iap_ln_002",
  "userId": "U91FC5A...",
  "purchaseTimestamp": 1738672496,
  "channelId": "12345..."
}
```

<!-- tab end -->

### Refund event 

當使用者在應用程式商店（App Store、Google Play）購買的項目獲得退款時，會發生此事件。此事件包含被退款項目的相關資訊。

#### Webhook payload 

<!-- parameter start -->

type

String

webhook 事件的類型。\
指定為 `refundComplete`。

<!-- parameter end -->
<!-- parameter start -->

orderId

String

被使用者退款的訂單 ID。包含在[預約購買（Reserve purchase）](https://developers.line.biz/en/reference/line-mini-app/#reserve-purchase)端點的回應中。

<!-- parameter end -->
<!-- parameter start -->

productId

String

被使用者退款項目的商品 ID（[`productId`](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-product-id/)）。

<!-- parameter end -->
<!-- parameter start -->

userId

String

請求退款的使用者的使用者 ID。

<!-- parameter end -->
<!-- parameter start -->

purchaseTimestamp

number

被退款項目的購買時間。單位為 UNIX 時間（以秒為單位）。

與[購買完成事件（purchase complete event）](https://developers.line.biz/en/reference/line-mini-app/#purchase-complete-event)的 `purchaseTimestamp` 相符。此時間並非使用者實際完成退款的時間。

<!-- parameter end -->
<!-- parameter start -->

channelId

String

LINE MINI App 頻道的頻道 ID。

<!-- parameter end -->

_範例_

<!-- tab start `json` -->

```json
{
  "type": "refundComplete",
  "orderId": "T2025020710000002126002",
  "productId": "iap_ln_002",
  "userId": "U91FC5A...",
  "purchaseTimestamp": 1738672496,
  "channelId": "12345..."
}
```

<!-- tab end -->
