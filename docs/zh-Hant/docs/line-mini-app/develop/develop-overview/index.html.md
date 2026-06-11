# 開始使用

在您直接著手開發 LINE MINI App 之前，建議您仔細閱讀以下內容：

- Discover LINE MINI App
  - [LINE MINI App specifications](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)
- Design
  - [LINE MINI App icon specifications and guidelines](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/)
  - [Safe area for landscape mode](https://developers.line.biz/en/docs/line-mini-app/design/landscape/)
  - [Loading icon](https://developers.line.biz/en/docs/line-mini-app/design/loading-icon/)
- Develop
  - [Performance guidelines](https://developers.line.biz/en/docs/line-mini-app/develop/performance-guidelines/)
- Submit Application
  - [Submit Application for Review](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)
  - [LINE MINI App policy](https://terms2.line.me/LINE_MINI_App?lang=en)

## Create a LINE MINI App Channel 

任何符合 [LINE MINI App Policy](https://terms2.line.me/LINE_MINI_App?lang=en) 規範的授權客戶，都可以建立 LINE MINI App 頻道（channel）。

[頻道（Channel）](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)是將您的應用程式連接到 LINE Platform 的溝通管道。請在 LINE Developers Console 上為每個 LINE MINI App 建立一個 LINE MINI App 頻道。

1. 存取 [LINE Developers Console](https://developers.line.biz/console/) 並選擇一個 provider。

2. 依序點選 **Channels** > **Create a new channel** > **LINE MINI App**。

   ![LINE MINI App channel](https://developers.line.biz/media/line-mini-app/line-mini-app-channel-en.png)

3. 輸入以下項目的資訊以建立 LINE MINI App 頻道。

   | Item | Required? | Description | Location displayed to users |
   | --- | --- | --- | --- |
   | **Channel type** | ✅ | 頻道類型。選擇 LINE MINI App 以建立您的 LINE MINI App 頻道。 | - |
   | **Provider** | ✅ | 頻道的 [provider](https://developers.line.biz/en/docs/line-developers-console/overview/#provider) | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
   | **Region to provide the service** | ✅ | 您想提供 LINE MINI App 的地區。以下其中之一：<br><ul><li>Japan</li><li>Thailand</li><li>Taiwan</li></ul>\*如果您想在多個地區提供 LINE MINI App，請為每個地區建立一個頻道。 | - |
   | **Channel icon** | ❌ | 頻道的圖示。如需圖示尺寸與設計的詳細資訊，請參閱 [LINE MINI App icon specifications and guidelines](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/)。 | <ul><li>啟動 LINE MINI App 時的權限同意畫面</li><li>當您使用[操作按鈕（action button）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#built-in-share-settings)分享 LINE MINI App 頁面時的目標聊天室</li><li>[多分頁檢視（Multi-tab view）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#multi-tab-view-settings)</li><li>[服務訊息（Service message）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#template-elements)的頁尾區段</li><li>[探索 LINE MINI App（主頁分頁、搜尋功能等）](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#access-line-mini-app-methods-for-users)</li><li>[新增捷徑畫面（Add Shortcut screen）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#add-shortcut-screen)</li></ul> |
   | **Channel name** | ✅ | 頻道的名稱<br>\*頻道名稱不可包含「LINE」或類似字串。 | <ul><li>啟動 LINE MINI App 時的權限同意畫面</li><li>當您使用[操作按鈕（action button）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#built-in-share-settings)分享 LINE MINI App 頁面時的目標聊天室</li><li>[多分頁檢視（Multi-tab view）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#multi-tab-view-settings)</li><li>[服務訊息（Service message）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/#template-elements)的頁尾區段</li><li>[探索 LINE MINI App（主頁分頁、搜尋功能等）](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#access-line-mini-app-methods-for-users)</li><li>[新增捷徑畫面（Add Shortcut screen）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#add-shortcut-screen)</li></ul> |
   | **Channel description** | ✅ | 頻道的描述。如果負責開發 LINE MINI App 的公司與提供服務的公司不同，請告知使用者。如需詳細資訊，請參閱 [LINE MINI App Policy](https://terms2.line.me/LINE_MINI_App?lang=en) 中的 Company information。 | 啟動 LINE MINI App 時的權限同意畫面 |
   | **Email address** | ✅ | 用於接收頻道重要更新的電子郵件地址 | - |
   | **Privacy policy URL** | ✅ \* | 應用程式的隱私權政策 URL | 啟動 LINE MINI App 時的權限同意畫面 |
   | **Terms of use URL** | ❌ | 應用程式的使用條款 URL | 啟動 LINE MINI App 時的權限同意畫面 |
   | **LINE Developers Agreement** | ✅ | 閱讀並同意 LINE Developers Agreement。 | - |
   | **LINE MINI App Platform Agreemeent** | ✅ | 閱讀並同意 LINE MINI App Platform Agreement。 | - |
   | **LINE MINI App Policy** | ✅ | 閱讀並同意 LINE MINI App Policy。 | - |
   | **Service company's country or region** | ✅ | 聲明並保證提供 LINE MINI App 的地區與服務公司所在的國家或地區相同。 | 啟動 LINE MINI App 時的權限同意畫面 |
   | **LY Corporation Privacy Policy** | 見描述 | 僅在您於 **Region to provide the service** 選擇 Thailand 時為必填。閱讀並確認 [LY Corporation Privacy Policy](https://line.me/th/terms/policy/)。 | - |

   \* 僅對於認證 provider（certified provider），建立 LINE MINI App 頻道時必須輸入隱私權政策 URL。

4. 請務必閱讀以「By creating a LINE MINI App and agreeing to the terms and conditions herein, I hereby warrant and represent that I have the full authority to execute and bind my company to the terms hereof.」開頭的內容，並勾選方塊以表示您保證並聲明擁有上述權限。
5. 點選 **Create**。
6. 請務必閱讀「Regarding Consent to Usage of the Information」，若您同意則點選 **Accept**。

   上述流程將會為 LINE MINI App 建立一個頻道，並可作為未驗證的 MINI App（unverified MINI App）使用。

   如需更多關於變更您已建立的 LINE MINI App 頻道設定的資訊，請參閱 [When settings on the LINE Developers Console are reflected](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#timing-of-settings-reflection)。

<!-- note start -->

**如果您無法建立 LINE MINI App 頻道**

如果您無法建立 LINE MINI App 頻道，請將您用來登入 [LINE Developers Console](https://developers.line.biz/console/) 的 Business ID 連結到您的 LINE 帳號。如需詳細資訊，請參閱 LINE Developers Console 文件中的 [Link your Business ID with your LINE account](https://developers.line.biz/en/docs/line-developers-console/login-account/#link-business-account-with-line-account)。

<!-- note end -->

### Privacy policy URL settings 

如果負責開發 LINE MINI App 的公司與服務提供者不同，您將需要設定 **Channel description** 與 **Privacy policy URL** 才能通過審查。如需詳細資訊，請參閱 [LINE MINI App Policy](https://terms2.line.me/LINE_MINI_App?lang=en) 中的「Company information」。

建立 LINE MINI App 頻道時，如果您是認證 provider（certified provider），即可設定 **Privacy policy URL**。但如果您不是，則無法設定。在這種情況下，請先建立 LINE MINI App 頻道，然後再編輯 **Privacy policy URL**。

### Precautions for channel and provider linkage 

一旦您建立了頻道，之後就無法將該頻道移動到另一個 provider。

使用開發者所提供服務的 LINE 使用者，會在每個 provider 下被賦予一個不同的使用者 ID。使用者 ID 無法用來在不同 provider 下的各頻道之間識別出同一位使用者。

![](https://developers.line.biz/media/line-developers-console/different-user-ids.png)

<!-- warning start -->

**建立頻道時需要特別注意的情況**

舉例來說，以下情況需要特別注意：

- 頻道與 provider 由個人或公司管理。
- 在同一個 provider 下建立彼此無關的服務或公司的頻道。
- 在由提供頻道管理工具等服務的公司（service company）所管理的 provider 下建立頻道。

在這些情況下，由於之後無法在 provider 之間移動頻道，以及使用者在不同 provider 下會被賦予不同的使用者 ID，未來可能會產生問題。請在審慎考量相關風險後，於適當的 provider 下建立頻道。

<!-- warning end -->

<!-- tip start -->

**provider 與頻道管理的最佳實務**

有一個頁面以具體範例說明如何管理 provider 與頻道的管理員角色，以及您應該在哪個 provider 下建立頻道。

如需詳細資訊，請參閱 LINE Developers Console 文件中的 [Best practices for provider and channel management](https://developers.line.biz/en/docs/line-developers-console/best-practices-for-provider-and-channel-management/)。

<!-- tip end -->

## Develop a LINE MINI App 

一旦您建立了 LINE MINI App 頻道，就可以開始開發 LINE MINI App。可以將開發 LINE MINI App 想成是使用 [LIFF](https://developers.line.biz/en/docs/liff/overview/)，但需搭配本指南所說明的額外要求與限制。

如需詳細資訊，請參閱 [LINE MINI App specifications](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)。

### Internal structure of a LINE MINI App channel 

從 LINE Developers Console 的 **Channels** 分頁來看，LINE MINI App 顯示為單一頻道，但在內部則由以下三個頻道（以下稱「內部頻道（internal channels）」）所組成：

| Internal channels | Description |
| --- | --- |
| LINE MINI App channel in Developing | 用於開發的 LINE MINI App 頻道。頻道狀態永遠為「Developing」。 |
| LINE MINI App channel in Review | 用於 LY Corporation 審查的 LINE MINI App 頻道。頻道狀態永遠為「Developing」。 |
| LINE MINI App channel in Published | 已發布並提供給使用者使用的 LINE MINI App 頻道。頻道狀態永遠為「Publishing」。 |

如需更多關於內部頻道的資訊，請參閱 [LINE Developers Console Guide for LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/)。

### Using APIs 

開發 LINE MINI App 時，有兩種類型的 API 可供您使用：LIFF API 與 [Service Message API](https://developers.line.biz/en/reference/line-mini-app/)。LIFF API 是從您的 LINE MINI App 呼叫，而 Service Message API 則是從您服務的伺服器端呼叫。如需更多關於使用 LIFF API 的資訊，請參閱 [LIFF documentation](https://developers.line.biz/en/docs/liff/overview/)。

舉例來說，要[實作自訂操作按鈕（custom action button）](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/)，您需要從您的 LINE MINI App 呼叫 LIFF API。但要傳送[服務訊息（service messages）](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)，您則需要從您的伺服器呼叫 Service Message API。

<!-- tip start -->

**LIFF API 持續在改進中**

為了提升使用者體驗，LIFF API 持續新增功能並改進既有功能。

<!-- tip end -->

## Use basic authentication to restrict access to your LINE MINI App before it is released 

基本驗證（basic authentication）適用於狀態為「Not yet reviewed」或「Reviewing」的 LINE MINI App。您可以使用基本驗證來限制對尚未發布的 LINE MINI App 的存取。

### How to use basic authentication 

在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Web app settings** 分頁中，於 **Developing** 或 **Review** 的 **Endpoint URL** 指定帶有基本驗證的 URL。接著在 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中開啟 LINE MINI App，就會出現一個對話框，提示您輸入使用者名稱與密碼。

![Basic authentication screen](https://developers.line.biz/media/line-mini-app/basic-auth.png)

### Conditions for basic authentication 

當滿足以下所有條件時，即可使用基本驗證：

- 您的 LINE MINI App 狀態為「Not yet reviewed」或「Reviewing」。
- LINE MINI App 在 [LIFF Browser](https://developers.line.biz/en/glossary/#liff-browser) 中開啟。

基本驗證不適用於 LIFF App，以及狀態為「Reflected」的 LINE MINI App。此外，您無法使用摘要驗證（digest authentication）。

<!-- tip start -->

**即使滿足條件，基本驗證仍無法使用時**

在 LIFF-to-LIFF 轉換之後的 LINE MINI App 中，基本驗證無法使用。如需詳細資訊，請參閱 LIFF 文件中的 [Opening a LIFF app from another LIFF app (LIFF-to-LIFF transition)](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff)。

<!-- tip end -->

如需更多關於 LIFF browser 上基本驗證規格的資訊，請參閱 LIFF 文件中的 [LIFF browser specifications](https://developers.line.biz/en/docs/liff/overview/#liff-browser-spec)。

### Notes on using basic authentication 

基本驗證是一種用於簡易存取限制的驗證方法，LINE MINI App 的開發者在使用前應自行評估並判斷基本驗證是否符合其安全需求。

新增此功能並不代表建議使用基本驗證，也不保證基於基本驗證的存取限制具備安全性。

## Our recommendations for development 

請以幫助使用者輕鬆且快速地存取您核心功能的方式來開發您的 LINE MINI App。以下是我們的幾項建議：

- 使用 HTML5 [Geolocation API](https://www.w3.org/TR/geolocation/) 來定位使用者。
- 善用可透過 LIFF API 取得的使用者 LINE 個人檔案資訊。舉例來說，在餐廳訂位時自動帶入使用者的 LINE 個人檔案資訊，可讓使用者免於每次新增訂位時都要重新輸入個人資料。
- 最佳化您 LINE MINI App 的效能，為您的 LINE MINI App 使用者提供更好的使用者體驗。如需詳細資訊，請參閱 [Performance guidelines](https://developers.line.biz/en/docs/line-mini-app/develop/performance-guidelines/)。

## Request LINE MINI App review 

當您建立 LINE MINI App 頻道時，該 LINE MINI App 為未驗證的 MINI App（unverified MINI App），部分功能會受到限制。若要讓已開發的 LINE MINI App 成為已驗證的 MINI App（verified MINI App），就必須接受 LY Corporation 的驗證審查（verification review）。

請注意，如果提供服務的地區為 Taiwan 或 Thailand，只有隸屬於認證 provider（certified provider）的 LINE MINI App 頻道才能申請驗證審查。

如需詳細資訊，請參閱 [Submitting LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)。
