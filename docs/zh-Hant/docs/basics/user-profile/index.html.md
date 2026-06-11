# 取得使用者個人檔案資訊

透過 [Messaging API](https://developers.line.biz/en/docs/messaging-api/overview/)、[LINE Login](https://developers.line.biz/en/docs/line-login/overview/)、[LINE Front-end Framework（LIFF）](https://developers.line.biz/en/docs/liff/overview/) 以及 [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/)，你都可以取得使用者的個人檔案資訊。

可取得的個人檔案資訊類型，取決於你所使用的取得方式。此外，有些個人檔案資訊（例如使用者的電子郵件地址與通訊地址）需要另外提出申請或簽訂合約才能取得。

本頁將說明使用者個人檔案資訊的類型，以及如何取得這些資訊。

<!-- table of contents -->

## What is user profile information 

使用者可在 LINE 應用程式的 **設定（Settings）** > **個人檔案（Profile）** 中設定自己的個人檔案資訊，例如姓名與大頭貼。關於可在 **個人檔案** 中設定的資訊，詳情請參閱 LINE 服務中心的 [Your profile](https://help.line.me/line/smartphone/pc?lang=en&contentId=20000134)。

![Users can set their profile information in the LINE app](https://developers.line.biz/media/basics/my-profile-en.png)

除了這個 **個人檔案** 之外，還有以下幾種個人檔案資訊類型：

- [Common Profile](https://developers.line.biz/en/docs/basics/user-profile/#what-is-common-profile)
- [LINE Profile+](https://developers.line.biz/en/docs/basics/user-profile/#what-is-line-profile-plus)

### Common Profile 

Common Profile 是使用者透過整合自己在 LINE 應用程式或 Yahoo! JAPAN 所註冊的個人檔案資訊而建立的個人檔案。使用者可在 Account Center 中設定自己的 Common Profile。

![Users can set their Common Profile in the Account Center](https://developers.line.biz/media/basics/quick-fill-ja.png)

關於 Common Profile 的資訊，請參閱 LINE 使用者指南中的 [Set Common Profile to use Quick-fill](https://guide.line.me/ja/services/quick-fill.html)（僅提供日文版）。

### LINE Profile+ 

除了一般的個人檔案資訊之外，使用者還可在 LINE 應用程式中前往 **設定（Settings）** > **個人檔案（Profile）** > **LINE Profile+**，註冊通訊地址與電話號碼等額外資訊。

![Users can set additional profile information with LINE Profile+.](https://developers.line.biz/media/basics/profile-plus-en.png)

透過 **LINE Profile+**，使用者可以設定以下資訊：

- 姓名（姓、名、中間名、名字發音等）
- 性別
- 生日（使用者在 **設定** > **個人檔案** > **生日** 中註冊的資訊也會顯示在 LINE Profile+ 中）
- 電話號碼（使用者在 **設定** > **帳號** > **電話號碼** 中註冊的資訊也會顯示在 LINE Profile+ 中）
- 電子郵件地址（使用者在 **設定** > **帳號** > **電子郵件地址** 中註冊的資訊也會顯示在 LINE Profile+ 中）
- 通訊地址（郵遞區號、州/省、城市、街道地址等）

透過在 LINE Profile+ 中註冊這些資訊，使用者在使用 LINE 家族應用程式或外部服務時，便可避免手動輸入通訊地址、電話號碼等資料。詳情請參閱 LINE 服務中心「Your profile」一節中的 [LINE Profile+](https://help.line.me/line/smartphone/pc?lang=ja&contentId=20000134)（僅提供日文版）。

關於如何運用註冊於 LINE Profile+ 的個人檔案資訊，詳情請參閱企業客戶選用功能文件中的 [LINE Profile+](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/)。

## How to get profile information 

在 LINE Platform 上，你可以使用以下方式取得使用者個人檔案資訊：

- 方式 1：從 Messaging API 的 [Get profile](https://developers.line.biz/en/reference/messaging-api/#get-profile) 端點取得
- 方式 2：從 LINE Login 的 [Get user information](https://developers.line.biz/en/reference/line-login/#userinfo) 端點取得
- 方式 3：從 LINE Login 的 [Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile) 端點取得
- 方式 4：從 LINE Login 之 ID 權杖的 [payload](https://developers.line.biz/en/docs/line-login/verify-id-token/#payload) 取得
- 方式 5：從 LIFF 的 [liff.getProfile()](https://developers.line.biz/en/reference/liff/#get-profile) 方法取得
- 方式 6：使用 LIFF 的 [liff.getDecodedIDToken()](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 方法，從其 [payload](https://developers.line.biz/en/docs/line-login/verify-id-token/#payload) 取得
- 方式 7：使用 LINE MINI App 的 [Common Profile Quick-fill](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/) 功能取得

方式 1 至 6 可讓你從 LINE 個人檔案與 LINE Profile+ 取得資訊。方式 7 則可讓你從 Common Profile 取得資訊。

你只能取得主要的個人檔案資訊，無法取得使用者的[子個人檔案（subprofile）](https://developers.line.biz/en/glossary/#subprofile)。

關於使用各種方式可取得的個人檔案資訊類型，詳情請參閱[可取得的個人檔案資訊類型](https://developers.line.biz/en/docs/basics/user-profile/#profile-information-types)。

## Types of profile information that can be obtained 

可取得的個人檔案資訊類型，取決於你所使用的取得方式。

下表列出使用[如何取得個人檔案資訊](https://developers.line.biz/en/docs/basics/user-profile/#how-to-get-profile)中所說明的方式 1 至 7 可取得的個人檔案資訊類型。

| 個人檔案資訊 | 方式 1</br>Messaging API 的</br>[Get profile](https://developers.line.biz/en/reference/messaging-api/#get-profile)</br>端點 | 方式 2</br>LINE Login 的</br>[Get user information](https://developers.line.biz/en/reference/line-login/#userinfo)</br>端點 | 方式 3</br>LINE Login 的</br>[Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile)</br>端點 | 方式 4</br>LINE Login 之 ID 權杖的</br>[Payload](https://developers.line.biz/en/docs/line-login/verify-id-token/#payload) | 方式 5</br>[liff.getProfile()](https://developers.line.biz/en/reference/liff/#get-profile) | 方式 6</br>[liff.getDecodedIDToken()](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 的</br>[Payload](https://developers.line.biz/en/docs/line-login/verify-id-token/#payload) | 方式 7</br>LINE MINI App 的</br>[Common Profile Quick-fill](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 使用者 ID | ✅ (`userId`) | ✅ (`sub`) | ✅ (`userId`) | ✅ (`sub`) | ✅ (`userId`) | ✅ (`sub`) | ❌ |
| 顯示名稱 | ✅ (`displayName`) | ✅ (`name`) | ✅ (`displayName`) | ✅ (`name`) | ✅ (`displayName`) | ✅ (`name`) | ❌ |
| 大頭貼 | ✅ (`pictureUrl`) | ✅ (`picture`) | ✅ (`pictureUrl`) | ✅ (`picture`) | ✅ (`pictureUrl`) | ✅ (`picture`) | ❌ |
| 狀態訊息 | ✅ (`statusMessage`) | ❌ | ✅ (`statusMessage`) | ❌ | ✅ (`statusMessage`) | ❌ | ❌ |
| 語言 | ✅ (`language`) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| 電子郵件地址 | ❌ | ❌ | ❌ | ✅ (`email`) | ❌ | ✅ (`email`) | ✅ (`email`) |
| 姓名 | ❌ | ❌ | ❌ | ✅ (`given_name`、`family_name` 等) | ❌ | ✅ (`given_name`、`family_name` 等) | ✅ (`given-name`、`family-name` 等) |
| 性別 | ❌ | ❌ | ❌ | ✅ (`gender`) | ❌ | ✅ (`gender`) | ✅ (`sex-enum`) |
| 生日 | ❌ | ❌ | ❌ | ✅ (`birthdate`) | ❌ | ✅ (`birthdate`) | ✅ (`bday-year`、`bday-month` 等) |
| 通訊地址 | ❌ | ❌ | ❌ | ✅ (`address`) | ❌ | ✅ (`address`) | ✅ (`address-level1`、`address-level2` 等) |
| 電話號碼 | ❌ | ❌ | ❌ | ✅ (`phone_number`) | ❌ | ✅ (`phone_number`) | ✅ (`tel`) |

若要使用方式 4 與方式 6 取得電子郵件地址，你必須請求存取使用者電子郵件地址的權限。詳情請參閱 LINE Login 文件中的[請求存取使用者電子郵件地址的權限](https://developers.line.biz/en/docs/line-login/integrate-line-login/#applying-for-email-permission)。

此外，若要使用方式 4 與方式 6 取得姓名、性別、生日、通訊地址與電話號碼，你必須申請 LINE Profile+，這是一項供企業使用者選用的功能。關於 LINE Profile+ 的詳情，請參閱企業客戶選用功能文件中的 [LINE Profile+](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/)。

若要使用方式 7 取得個人檔案資訊，你必須申請使用 Quick-fill 功能。關於申請使用 Quick-fill 的詳情，請參閱 LINE MINI App 文件中的 [Common Profile Quick-fill 概觀](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/)。
