# Common Profile Quick-fill 總覽（Overview of Common Profile Quick-fill）

<!-- tip start -->

**僅限已驗證的 MINI App 可使用**

若要使用 Common Profile Quick-fill，您的 LINE MINI App 必須通過驗證，且您必須申請使用 Quick-fill。詳情請參閱 [Steps for using Quick-fill](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process)。

<!-- tip end -->

## What is Common Profile Quick-fill 

Quick-fill 是一項功能，使用者只要在 LINE MINI App 上輕觸 **Auto-fill（自動填入）** 按鈕，即可自動填入所需的個人資料資訊。您可以在 LINE MINI App 中輕鬆使用使用者於 Account Center 設定的 Common Profile 資訊。

![](https://developers.line.biz/media/line-mini-app/quick-fill/quick-fill-3-steps.png)

將 Quick-fill 整合到您的 LINE MINI App 後，使用者只要輕觸一下，就能自動輸入地址或電話號碼。例如在餐廳訂位或於網路商店下訂單時，使用者就能省去手動輸入資訊的麻煩。

本頁說明如何將 Quick-fill 整合到您的 LINE MINI App。

關於如何在 LINE MINI App 上使用 Quick-fill 的資訊，請參閱 LINE 使用者指南中的 [Set Common Profile to use Quick-fill](https://guide.line.me/ja/services/quick-fill.html)（僅提供日文版）。

### Languages that support Quick-fill 

Quick-fill 目前僅支援日文。因此，無論 LINE app 的語言設定為何，Quick-fill 畫面都會以日文顯示。

## Steps for using Quick-fill 

若要使用 Quick-fill，您的 LINE MINI App 必須通過驗證，且您必須申請使用 Quick-fill。請依照以下步驟進行：

- [Step 1. Prepare a verified MINI App](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-1)
- [Step 2. Apply to use Quick-fill and develop](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-2)

### Step 1. Prepare a verified MINI App 

Quick-fill 僅在已驗證的 MINI App 中可用。因此，您必須先準備一個已驗證的 MINI App 才能整合 Quick-fill。詳情請參閱 [Process from LINE MINI App development to release](https://developers.line.biz/en/docs/line-mini-app/quickstart/#overall-process)。

### Step 2. Apply to use Quick-fill and develop 

準備好已驗證的 MINI App 後，下一步就是申請並開發 Quick-fill。請依照以下步驟進行：

- [Step 2-1. Apply for Quick-fill and obtain approval](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-2-1)
- [Step 2-2. Specify the Quick-fill scope in the LINE Developers Console](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-2-2)
- [Step 2-3. Integrate Quick-fill](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-2-3)
- [Step 2-4. Request review of the LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-2-4)

#### Step 2-1. Apply for Quick-fill and obtain approval 

若要使用 Quick-fill，請先填寫使用申請表，並透過申請表單提交。若同一服務供應商要一次為多個 LINE MINI App 提出申請，可使用多筆申請用的申請表。

- [[Single application] Usage application form (Excel file)](https://workers-hub.ent.box.com/s/06w8vzqxfwx2e031oq2q9ztj7ca8p7h8)（僅提供日文版）
- [[Multiple applications] Usage application form (Excel file)](https://workers-hub.ent.box.com/s/xrwjm892d1uxsiblptfgoj07r0v5zwbp)（僅提供日文版）

填寫完使用申請表後，請透過以下表單提交您的申請。我們會透過電子郵件通知您申請的受理狀況以及審核結果。

[Application form](https://form-business.yahoo.co.jp/claris/enqueteForm?inquiry_type=miniapp-quick-fill)（僅提供日文版）

#### Step 2-2. Specify the scope of Quick-fill in the LINE Developers Console 

當您的 Quick-fill 使用申請被受理後，請指定您想使用的資訊範圍（scope）。在 [LINE Developers Console](https://developers.line.biz/console/) 中選擇目標 LINE MINI App 頻道，然後在 **Web app settings** 分頁的 **Scope** 區段中，勾選您想使用的 scope 核取方塊。

若要為已驗證的 MINI App 指定 scope，您必須在 **Review request** 分頁中點選 **Search enable** 按鈕，以啟用該 LINE MINI App 的搜尋功能。

![](https://developers.line.biz/media/line-mini-app/quick-fill/quick-fill-scope-ja.png)

關於 Quick-fill 可使用的 scope 類型詳情，請參閱 [Types of scope that can be selected in the LINE Developers Console](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#scope)。

<!-- tip start -->

**同時啟用 Quick-fill 與 Channel consent simplification 時的行為**

若您同時啟用 Quick-fill 與 [Channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/)，使用者將無法在 Verification 畫面上停用 Common Profile 的切換按鈕。我們計劃日後修正此行為。關於 Verification 畫面的詳情，請參閱 [Request permissions other than the `openid` scope on the verification screen](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

<!-- tip end -->

#### Step 2-3. Integrate Quick-fill 

指定 scope 後，請將 Quick-fill 整合到您的 LINE MINI App。關於開發的詳情，請參閱 [Integrate Quick-fill with the LIFF Plugin](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#use-liff-plugin)。

開發整合 Quick-fill 的 LINE MINI App 時，請遵循以下指引：

- [Common Profile Quick-fill design regulations](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/)
- [LINE MINI App development guidelines](https://developers.line.biz/en/docs/line-mini-app/development-guidelines/)
- [LIFF app development guidelines](https://developers.line.biz/en/docs/liff/development-guidelines/)
- [LINE Login development guidelines](https://developers.line.biz/en/docs/line-login/development-guidelines/)

#### Step 2-4. Request review of the LINE MINI App 

整合 Quick-fill 後，請透過 LINE MINI App 頻道中的 **Review request** 分頁提交您的 LINE MINI App 進行審核。一旦您的 LINE MINI App 通過審核，您就能將變更套用至已發布的 LINE MINI App。

## Integrate Quick-fill with the LIFF Plugin 

若要開發 Quick-fill，您必須使用 LIFF SDK 與 [LIFF plugin](https://developers.line.biz/en/docs/liff/liff-plugin/)。關於 LIFF plugin 可搭配運作的 LIFF SDK 版本資訊，請參閱 [LIFF SDK version](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#liff-sdk-version)。

您可以透過以下兩種方式之一，將 LIFF SDK 整合到您的 LINE MINI App：

- [Specify a CDN path to integrate Quick-fill](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#specify-cdn-path)
- [Use the npm package to integrate Quick-fill](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#use-npm-package)

將 LIFF SDK 整合到您的 LINE MINI App 後，您可以如下所示，將 Quick-fill LIFF plugin 傳遞給 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法，以啟用 Quick-fill LIFF plugin：

```javascript
liff.use(new LiffCommonProfilePlugin());
await liff.init({ liffId: "xxx" });

const { data, error } = await liff.$commonProfile.get();
liff.$commonProfile.fill(data);
```

`$commonProfile` 屬性會被加入 `liff` 物件中，並可使用以下 Quick-fill client API：

- [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile)
- [`liff.$commonProfile.getDummy()`](https://developers.line.biz/en/reference/line-mini-app/#get-dummy-common-profile)
- [`liff.$commonProfile.fill()`](https://developers.line.biz/en/reference/line-mini-app/#fill-common-profile)

### Specify a CDN path to integrate Quick-fill 

當您指定 CDN 路徑時，透過 `script` 標籤載入套件，`liffCommonProfile` 屬性會被加入 window 物件中。將存在於 `liffCommonProfile` 內的 `LiffCommonProfilePlugin` 類別的實例作為引數傳遞給 `liff.use()`。

```html
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <script src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>
    <script src="https://static.line-scdn.net/5/liff-common-profile/edge/production/1.0.0/index.umd.cjs"></script>
    <title>LIFF App</title>
  </head>
  <body>

    <script type="module" src="/index.js"></script>
  </body>
</html>
```

```js
liff.use(new liffCommonProfile.LiffCommonProfilePlugin());

const { data, error } = await liff.$commonProfile.get();
liff.$commonProfile.fill(data);
```

詳情請參閱 LIFF 文件中的 [Specify the CDN path](https://developers.line.biz/en/docs/liff/developing-liff-apps/#specify-cdn-path)。

### Use the npm package to integrate Quick-fill 

當您使用 npm 套件時，請從套件中匯入 `LiffCommonProfilePlugin` 類別，並將其實例作為引數傳遞給 `liff.use()`。

```sh
$ npm install @line/liff-common-profile-plugin
```

```js
import liff from "@line/liff";
import { LiffCommonProfilePlugin } from "@line/liff-common-profile-plugin";
liff.use(new LiffCommonProfilePlugin());

const { data, error } = await liff.$commonProfile.get();
liff.$commonProfile.fill(data);
```

詳情請參閱 LIFF 文件中的 [Use the npm package](https://developers.line.biz/en/docs/liff/developing-liff-apps/#use-npm-package)。

## Quick-fill operating environment 

Quick-fill 僅在使用者使用 LINE for iOS 或 LINE for Android 時運作。

以下是您系統上 Quick-fill 的運作環境：

- [LIFF SDK version](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#liff-sdk-version)
- [Node.js version](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#nodejs-version)

LINE MINI App 使用 [LINE Front-end Framework (LIFF)](https://developers.line.biz/en/docs/liff/overview/)。關於 Quick-fill 的建議環境詳情，請參閱 LIFF 文件中的 [Recommended operating environment](https://developers.line.biz/en/docs/liff/overview/#operating-environment) 區段。

<!-- note start -->

**保證 LIFF app 可運作的轉址目的地**

LIFF app 僅在 URL 與端點（endpoint）URL 完全相同（例如 `https://example.com/path`），或位於端點 URL 之下層（例如 `https://example.com/path/to/lower?key1=value1#URL-fragment`）時才會運作。若您將 LIFF app 轉址至上述以外的位置，則不保證 LIFF app 能正常運作。

<!-- note end -->

### LIFF SDK version 

由於 Quick-fill 的開發會使用 LIFF plugin，請使用 LIFF SDK v2.19.0 或更新版本。關於 LIFF plugin 的詳情，請參閱 LIFF 文件中的 [LIFF plugin](https://developers.line.biz/en/docs/liff/liff-plugin/)。

### Node.js version 

當您使用 npm 安裝 LIFF SDK 時，請使用 Node.js 18.15.0 或更新版本。請注意，當您使用指定 CDN 路徑的方式使用 LIFF SDK 時，並不需要 Node.js。

關於將 LIFF SDK 整合到您 LIFF app 的詳情，請參閱 LIFF 文件中的 [Integrating the LIFF SDK with the LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk)。

## Types of scope that can be selected in the LINE Developers Console 

您可以在 LINE Developers Console 中選擇以下類型的 Quick-fill scope。

| Scope | 說明 |
| --- | --- |
| `commonprofile.name` | 取得使用者已註冊姓名的權限 |
| `commonprofile.email` | 取得使用者已註冊電子郵件地址的權限 |
| `commonprofile.address` | 取得使用者已註冊地址的權限 |
| `commonprofile.gender` | 取得使用者已註冊性別的權限 |
| `commonprofile.birthday` | 取得使用者已註冊生日的權限 |
| `commonprofile.phone` | 取得使用者已註冊電話號碼的權限 |

若這些 scope 未顯示在 LINE Developers Console 上，請參閱 [Step 2-1. Apply for Quick-fill and obtain approval](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process-step-2-1)。

使用者無法在 [channel consent screen](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings) 上選擇並允許部分 scope。他們只能將這些 scope 以「Account Center 中的管理資訊（Common Profile）」整批一併允許或不允許。

## The `scopes` parameters that can be specified and its return value 

可為 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 與 [`liff.$commonProfile.getDummy()`](https://developers.line.biz/en/reference/line-mini-app/#get-dummy-common-profile) 指定的 `scopes` 參數及其各自的回傳值如下：

| Number | `scopes` | 說明 | 資料類型 | 最大字元數<br/>(半形) | 最大字元數<br/>(平假名與漢字) | 回傳值說明 |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `family-name` | 姓 | string | 100 | 50 |  |
| 2 | `given-name` | 名 | string | 100 | 50 |  |
| 3 | `family-name-kana` | 姓（讀音） | string | 100 | 50 |  |
| 4 | `given-name-kana` | 名（讀音） | string | 100 | 50 |  |
| 5 | `sex-enum` | 性別 | number | 1（固定長度） | N/A | <ul><li>`0`：男性</li><li>`1`：女性</li><li>`2`：其他</li><li>`3`：不回答</li></ul> |
| 6 | `bday-day` | 生日（日） | number | 2 | N/A |  |
| 7 | `bday-month` | 生日（月） | number | 2 | N/A |  |
| 8 | `bday-year` | 生日（年） | number | 4 | N/A |  |
| 9 | `tel` | 電話號碼 | string | 200 | N/A |  |
| 10 | `email` | 電子郵件地址 | string | 200 | N/A |  |
| 11 | `postal-code` | 郵遞區號 | string | 47 | N/A |  |
| 12 | `address-level1` | 地址 1 | string | 53 | 53 |  |
| 13 | `address-level2` | 地址 2 | string | 53 | 53 |  |
| 14 | `address-level3` | 地址 3 | string | 100 | 69 |  |
| 15 | `address-level4` | 地址 4 | string | 100 | 69 |  |

Account Center 的 Common Profile 是結合 LINE 與 Yahoo! JAPAN 所註冊的個人資料而建立的。若使用者未使用 Account Center，則會自動填入來自 LINE 的個人資料資訊。

## Dummy data for Common Profile that can be obtained 

您可以使用 [`liff.$commonProfile.getDummy()`](https://developers.line.biz/en/reference/line-mini-app/#get-dummy-common-profile) 取得 Common Profile 的虛擬資料（dummy data）。您可以透過 `caseId` 從提供的 10 種類型中指定要取得的虛擬資料。

| `caseId` | `family-name`  | `given-name`  | `family-name-kana`  | `given-name-kana`  | `sex-enum` | `bday-day` | `bday-month` | `bday-year` | `tel`  | `email`  | `postal-code`  | `address-level1`  | `address-level2`  | `address-level3`  | `address-level4` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 見本田 | 見本夫 | ダミータ | ダミーオ | 0 | 12 | 3 | 1998 | 09001234567 | dummy_39@yahoo.co.jp | 1020094 | 東京都 | 千代田区 | 紀尾井町1-2 | 東京ガーデンテラス紀尾井町 |
| 2 |  |  |  |  | 1 | 12 | 3 | 1998 | 09001234567 | dummy_39@yahoo.co.jp | N5X 1N7 | 東京都 |  | 紀尾井町1-2 | 東京ガーデンテラス紀尾井町 |
| 3 | 見本田 |  | ダミータ |  | 2 |  |  |  | 09001234567 | dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dummy_39dumm@yahoo.co.jp | 102-0094 | 東京都 | 千代田区 |  | 東京ガーデンテラス紀尾井町 |
| 4 |  | 見本夫 |  | ダミーオ | 3 | 12 | 3 | 1998 | 0901234567 | dummy_39@yahoo.co.jp | 1077 AA2 15000N5X 1N7107715000X 1077 AA2 15000N5X 1N71 | 東京都 | 千代田区 | 紀尾井町1-2 |  |
| 5 | Daimta | Damio | ダミータ | ダミーオ | 0 | 12 | 3 | 1998 | 09001234567 |  | 1020094 | Tokyo | Chiyoda-ku | Kioi-cho,1-2 | Tokyo Garden terrace Kioi-cho, |
| 6 | 1234 | 4321 | ダミータ | ダミーオ | 1 |  |  | 1998 | 090-1234-5678 | dummy_39@yahoo.co.jp |  | ﾄｳｷｮｳﾄ | ﾁﾖﾀﾞｸ | ｷｵｲﾁｮｳ1-2 | ﾄｳｷｮｳｶﾞｰﾃﾞﾝﾃﾗｽｷｵｲﾁｮｳ |
| 7 | ﾀﾞﾐｰﾀ | ﾀﾞﾐｵ | ダミータ | ダミーオ | 2 |  | 3 |  | 09001234567090012345670900123456709001234567090012345670900123456709001234567090012345670900123456709001234567090012345670900123456709001234567090012345670900123456709001234567090012345670900123456709 | dummy_39@yahoo.co.jp | 1020094 |  |  |  |  |
| 8 | ダミ！？ | ダミ夫@ | ダミータ | ダミーオ | 3 | 12 |  | 1998 | 09001234567 | dummy_39@yahoo.co.jp | 1020094 | 🍀 | 🍀🍀 | 🍀🍀🍀 | 🍀🍀🍀🍀 |
| 9 | 🐶🐶🐶 | ダミ💚 | ダミータ | ダミーオ | 0 | 12 | 3 | 1998 |  | dummy_39@yahoo.co.jp | 102-0094 | 東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都東京都 | 千代田区千代田区千代田区千代田区千代田区千代田区千代田区千代田区千代田区千代田区千代田区千代田区千代田区千 | 紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2紀尾井町1-2 | 東京ガーデンテラス紀尾井町東京ガーデンテラス紀尾井町東京ガーデンテラス紀尾井町東京ガーデンテラス紀尾井町東京ガーデンテラス紀尾井町東京ガーデンテラス紀尾井町東京ガーデンテラス紀尾井町 |
| 10 | ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田ダミー田 | ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫ダミー夫 | ダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータダミータ | ダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオダミーオ | 1 | 12 | 3 | 1998 | 09001234567 | dummy_39@yahoo.co.jp | N5X 1N7 |  | 千代田区 | 紀尾井町1-2 | 東京ガーデンテラス紀尾井町 |

## Options for getting Common Profile information 

當您使用 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 取得 Common Profile 資訊時，您可以為每個 scope 指定以下選項。這些選項預設皆設為 `true`，因此若要停用它們，請指定 `false`。

| 屬性 | 預設值 | 說明 | 可指定的 scope |
| --- | --- | --- | --- |
| `excludeEmojis` | true | 是否從字串中移除表情符號（emoji）。 | <ul><li>`given-name`</li><li>`family-name`</li></ul> |
| `excludeNonJp` | true | 是否排除 12 位數以上的電話號碼。若為 `true`，當電話號碼為 12 位數以上時，會回傳空字串與錯誤資訊。 | <ul><li>`tel`</li></ul> |
| `digitsOnly` | true | 是否排除非數字的郵遞區號。若為 `true`，當郵遞區號含有數字以外的字元時，會回傳空字串與錯誤資訊。 | <ul><li>`postal-code`</li></ul> |

## API reference 

關於 Quick-fill 所使用的 client API 詳情，請參閱 LINE MINI App API reference 中的 [Common Profile Quick-fill](https://developers.line.biz/en/reference/line-mini-app/#quick-fill)。
