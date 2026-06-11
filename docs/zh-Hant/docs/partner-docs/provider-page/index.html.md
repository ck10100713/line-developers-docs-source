# Provider page（提供者頁面）

<!-- note start -->

**使用選用功能需要提出申請**

只有已提交必要申請的企業用戶，才能使用本文件所述的功能。若要在您的 LINE 官方帳號（LINE Official Account）上使用這些功能，請聯絡您的業務代表，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## Overview 

提供者頁面（provider page）是一份清單，列出[Provider](https://developers.line.biz/en/glossary/#provider)在 LINE Platform 上所提供的各項服務。提供者可以在提供者頁面上展示他們所提供的服務，例如 LINE 官方帳號（Messaging API）、LINE MINI App 與 LINE Login。

![provider page sample](https://developers.line.biz/media/partner-docs/provider-page-en.png)

## Provider page settings 

只有認證提供者（certified provider）才能設定並發布提供者頁面。如需更多關於認證提供者的資訊，請參閱 [Certified provider](https://developers.line.biz/en/docs/line-developers-console/overview/#certified-provider)。

您可以從 [LINE Developers Console](https://developers.line.biz/console/) 上的 **Provider page** 分頁設定您的提供者頁面。只有在您獲授權使用提供者頁面功能時，才會顯示 **Provider page** 分頁。

在 **Provider Page** 分頁中，註冊您的隱私權政策 URL，並新增您想要在提供者頁面上顯示的服務。每個提供者頁面最多可以新增 100 項服務。如果隱私權政策 URL 尚未註冊，已註冊的服務將不會顯示在提供者頁面上。

<!-- tip start -->

**關於可新增至提供者頁面的 LINE 官方帳號**

可新增至提供者頁面的 LINE 官方帳號，僅限已認證帳號或[premium accounts](https://developers.line.biz/en/glossary/#premium-account)（進階帳號）。如需更多關於帳號類型的資訊，請參閱 LINE for Business 上的 [Account Types of LINE Official Account](https://www.linebiz.com/jp-en/service/line-official-account/account-type/) 頁面。

<!-- tip end -->

![provider page settings screen](https://developers.line.biz/media/partner-docs/provider-page-settings-en.png)

### Set the order in which services are displayed on the provider page 

從 [LINE Developers Console](https://developers.line.biz/console/) 上的 **Provider page** 分頁，將各項服務向上或向下拖放，即可反映它們在提供者頁面上顯示的順序。

您無法變更服務類別的順序：LINE 官方帳號、LINE MINI App 與 LINE Login。您只能變更各類別底下服務的顯示順序。

### Provider page URL 

您可以在 [LINE Developers Console](https://developers.line.biz/console/) 上的 **Provider page** 分頁找到您提供者頁面的 URL（`https://provider.line.me/{ProviderID}`）。

## Sharing the your provider page URL with users 

當您將提供者頁面的 URL 分享給用戶時，將會向用戶顯示所提供的提供者服務清單。

- **LINE 官方帳號**：在圖文選單（rich menu）中，或在被加為好友後所傳送的第一則訊息中，分享提供者頁面的連結。
- **LINE MINI App**：當用戶點按 LINE MINI App 中的[action button](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)（動作按鈕）時，會顯示一個標示為 **About the service** 的項目，讓他們可以檢視提供者頁面。
- **LINE Login**：在您已設定 LINE Login 按鈕的頁面上分享提供者頁面的連結。

## Cautions on the common use of user IDs 

原則上，[LINE user data policy](https://terms2.line.me/LINE_Developers_user_data_policy?lang=ja) 禁止在 LINE Platform 上提供多項服務的提供者，將從各個服務取得的 LINE 用戶資料進行串連與共用。不過，在發布提供者頁面之後，若符合以下[Terms and conditions of use](https://developers.line.biz/en/docs/partner-docs/provider-page/#terms-and-conditions-of-use)，則允許提供者串連 LINE 用戶資料並共同使用。

請注意，提供者作為 LINE 用戶資料的取得方，是依照相關法律與法規、並以不對用戶造成負面影響的方式，自行承擔風險使用這些資訊。

### Terms and conditions of use 

作為提供者，對於每項共同使用 LINE 用戶資料的服務，您都必須向用戶提供提供者頁面的連結，並告知用戶各項服務是由同一個提供者所提供。

在 Messaging API 頻道（channel）的情況下，請遵守以下事項。

- LINE 官方帳號的簽約公司與提供者必須為同一者，且兩家公司之間的關係不得對用戶造成誤導。

請注意，若您不遵守上述規則，或被發現以不當方式營運您的 LINE 帳號，LY Corporation 可能會建議您採取改正措施，或禁止您使用 LINE 用戶資料。
