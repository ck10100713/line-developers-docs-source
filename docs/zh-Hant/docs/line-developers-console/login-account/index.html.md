# 登入 LINE Developers Console（Log in to the LINE Developers Console）

若要登入 [LINE Developers Console](https://developers.line.biz/console/)，您需要 [Business ID](https://help2.line.me/business_id/web/?lang=en&contentId=20011264) 與開發者帳號（developer account）。

本頁說明如何登入 LINE Developers Console、建立開發者帳號，以及將您的 Business ID 與 LINE 帳號連結。

## Log in to the LINE Developers Console 

若要登入 LINE Developers Console，請點擊 [LINE Developers 網站](https://developers.line.biz/) 右上角的 **[Log in to Console](https://developers.line.biz/console/)** 按鈕。

![Click Log in to Console](https://developers.line.biz/media/line-developers-console/login-account-02-en.png)

接著會顯示 Business ID 登入畫面。請選擇您的登入方式並登入。您可以使用下列任一種帳號登入 Business ID：

- [LINE account](https://developers.line.biz/en/docs/line-developers-console/login-account/#line-account)
- [Business account](https://developers.line.biz/en/docs/line-developers-console/login-account/#business-account)
- [Yahoo! JAPAN ID](https://developers.line.biz/en/docs/line-developers-console/login-account/#yahoo-japan-id)（僅限日本提供）

如需更多關於各登入方式差異的資訊，請參閱說明中心的 [Business ID login methods](https://help2.line.me/business_id/web/?lang=en&contentId=20011265)。

![](https://developers.line.biz/media/line-developers-console/login-account-01-en.png)

### Log in with LINE account 

使用 LINE 帳號登入 Business ID 時，可採用下列方式登入：

- **自動登入（Auto login）**：在已安裝 LINE 的智慧型手機上免操作即可登入。
- **電子郵件登入（Email address log in）**：使用為您的 LINE 帳號註冊的電子郵件地址與密碼登入。
- **QR code 登入（QR code log in）**：使用智慧型手機 LINE App 的 QR code 讀取器掃描所顯示的 QR code 來登入。
- **單一登入（Single Sign On, SSO）**：在顯示「Continue as」的確認畫面上點擊登入按鈕來登入。

<!-- tip start -->

**使用 LINE 帳號登入時會啟用兩階段驗證（Two-factor authentication）**

當您使用 LINE 帳號登入時會啟用兩階段驗證。當您在電腦的瀏覽器上使用電子郵件地址登入時，必須輸入 LINE 帳號的電子郵件地址與密碼，接著再輸入智慧型手機 LINE App 上顯示的驗證碼。

![Two-factor authentication flow](https://developers.line.biz/media/news/login-flow-with-2fa-en.png)

一旦執行過兩階段驗證，用來登入的瀏覽器在一年內將不會再要求進行兩階段驗證。此外，若您已透過兩階段驗證登入過 [LINE Official Account Manager](https://manager.line.biz/)，則使用相同帳號登入 LINE Developers Console 時將不會被要求登入。

<!-- tip end -->

### Log in with business account 

使用 business account 登入 Business ID 時，請使用為您的 Business ID 註冊的電子郵件地址與密碼。

### Log in with Yahoo! JAPAN ID 

使用 Yahoo! JAPAN ID 登入 Business ID 時，您必須將 Yahoo! JAPAN ID 連結至 [Yahoo! JAPAN Business ID](https://support.yahoo-net.jp/PccBizmanager/s/article/H000011271)（僅提供日文）。

請注意，使用 Yahoo! JAPAN ID 登入 Business ID 僅限日本提供。

如需更多關於如何使用 Yahoo! JAPAN ID 登入的資訊，請參閱 Yahoo! JAPAN ID 指南中的 [What are the available login methods?](https://id.yahoo.co.jp/login/login_methods.html)（僅提供日文）。

## Create a developer account (only on first login) 

當您第一次使用 LINE 帳號或 business account 登入 [LINE Developers Console](https://developers.line.biz/console/) 時，請建立開發者帳號。輸入 **Developer name**（開發者名稱）與 **Your email**（您的電子郵件）。仔細閱讀並同意 [LINE Developers Agreement](https://terms2.line.me/LINE_Developers_Agreement?lang=en)，然後點擊 **Create my account**。此步驟僅在第一次登入時才需要。

![Developer account creation screen](https://developers.line.biz/media/line-developers-console/developer-registration-01-en.png)

開發者帳號建立完成後，會顯示一個畫面表示開發者帳號已建立完成。

![Developer account creation completion screen](https://developers.line.biz/media/line-developers-console/developer-registration-02-en.png)

## Account relationships 

您需要開發者帳號才能使用 LINE Developers Console。此外，開發者帳號一律與 Business ID 以一對一的方式連結。當您第一次登入 LINE Developers Console 並[建立開發者帳號](https://developers.line.biz/en/docs/line-developers-console/login-account/#register-as-developer)時，您的 Business ID 與開發者帳號就會自動連結。

<!-- note start -->

**將開發者帳號連結至 Business ID 的注意事項**

- 如果您刪除與開發者帳號連結的 Business ID，您將無法再登入您的開發者帳號
- 與開發者帳號連結的 Business ID 之後無法變更

<!-- note end -->

開發者帳號與 LINE 帳號是透過 Business ID 連結的。當您將 LINE 帳號連結至已與開發者帳號連結的 Business ID 時，即可將您的 LINE 帳號連結至開發者帳號。如需更多關於如何連結帳號的資訊，請參閱[將您的 Business ID 與 LINE 帳號連結](https://developers.line.biz/en/docs/line-developers-console/login-account/#link-business-account-with-line-account)。

開發者帳號、Business ID 與 LINE 帳號之間的關係如下：

|  | Developer account | Business ID | LINE account |
| --- | --- | --- | --- |
| Developer account | — | 一對一連結（\*） | 透過 Business ID 連結（一對一） |
| Business ID | 一對一連結（\*） | — | 可一對一連結 |
| LINE account | 透過 Business ID 連結（一對一） | 可一對一連結 | — |

\* 當您[建立開發者帳號](https://developers.line.biz/en/docs/line-developers-console/login-account/#register-as-developer)時，您的 Business ID 會自動連結至您的開發者帳號。

<!-- tip start -->

**關於各帳號的電子郵件地址**

為您的開發者帳號、Business ID 與 LINE 帳號註冊的名稱與電子郵件地址是分開管理的。因此，註冊在各帳號的電子郵件地址可能不同。

<!-- tip end -->

### Account relationships when creating a new Business ID 

當您第一次登入 LINE Developers Console 並建立新的 Business ID 時，您 LINE 帳號的連結行為會依您是使用 LINE 帳號或 business account（電子郵件地址與密碼）建立 Business ID 而有所不同。所使用的帳號類型與開發者帳號和 LINE 帳號之間連結關係如下：

| Account type | LINE account linked to developer account |
| --- | --- |
| LINE account | 用來建立 Business ID 的 LINE 帳號 |
| Business account<br>（電子郵件地址與密碼） | 無（\*） |

\* 您可以隨時將 LINE 帳號連結至使用 business account 建立的 Business ID。如需更多資訊，請參閱[將您的 Business ID 與 LINE 帳號連結](https://developers.line.biz/en/docs/line-developers-console/login-account/#link-business-account-with-line-account)。

## Link your Business ID with your LINE account 

每個 LINE 帳號只能連結一個 Business ID。您無法將多個 Business ID 連結至單一 LINE 帳號。

請依照下列步驟將您的 Business ID 與 LINE 帳號連結：

1. 登入 [LINE Developers Console](https://developers.line.biz/console/)
1. 點擊畫面右上角的圖示

   ![Click the icon in the top-right corner of the screen](https://developers.line.biz/media/line-developers-console/linking-line-account-click-user-icon-en.png)

1. 點擊帳號資訊，接著開啟個人資料畫面

   ![Click account information](https://developers.line.biz/media/line-developers-console/linking-line-account-click-account-en.png)

1. 點擊 **Go to Business ID Profile** 按鈕，前往您的 Business ID 個人資料

   ![Click the Go to Business ID profile](https://developers.line.biz/media/line-developers-console/linking-line-account-click-business-id-en.png)

1. 在 LINE account 區段中點擊「Unlinked」旁的連結圖示

   ![Link to LINE account](https://developers.line.biz/media/line-developers-console/linking-line-account-click-link-icon-en.png)

1. 登入您想要與 Business ID 連結的 LINE 帳號
1. 一旦 LINE 帳號登入完成，該 LINE 帳號就會與 Business ID 連結

<!-- note start -->

**連結 LINE 帳號時若顯示「This LINE account is already in use.」訊息**

您想要連結至 Business ID 的 LINE 帳號不得連結至任何其他 Business ID。如果您嘗試將 Business ID 連結至先前已連結至任何其他 Business ID 的 LINE 帳號，您將會看到「This LINE account is already in use」的訊息，並且無法連結這些帳號。

![Link to LINE account](https://developers.line.biz/media/line-developers-console/login-account-04-en.png)

<!-- note end -->

<!-- tip start -->

**將開發者帳號與 LINE 帳號連結**

開發者帳號與 LINE 帳號是透過 Business ID 連結的。當您將 LINE 帳號連結至已與開發者帳號連結的 Business ID 時，即可將您的 LINE 帳號連結至開發者帳號。

<!-- tip end -->

## Unlink your LINE account from your Business ID 

若要將您的 LINE 帳號從 Business ID 解除連結，您必須為您的 Business ID 註冊電子郵件地址與密碼（business account）。當您將 LINE 帳號從 Business ID 解除連結時，您的開發者帳號與 LINE 帳號之間的連結也會一併失效。

請依照下列步驟將 LINE 帳號從您的 Business ID 解除連結：

1. 使用您想要解除連結 LINE 帳號的 Business ID 登入 [LINE Developers Console](https://developers.line.biz/console/)
1. 點擊畫面右上角的圖示

   ![Click the icon in the top-right corner of the screen](https://developers.line.biz/media/line-developers-console/linking-line-account-click-user-icon-en.png)

1. 點擊帳號資訊，接著開啟個人資料畫面

   ![Click account information](https://developers.line.biz/media/line-developers-console/linking-line-account-click-account-en.png)

1. 點擊 **Go to Business ID Profile** 按鈕，前往您的 Business ID 個人資料

   ![Click the Go to Business ID Profile](https://developers.line.biz/media/line-developers-console/linking-line-account-click-business-id-en.png)

1. 在 LINE account 區段中點擊刪除圖示
   - 如果您尚未為 Business ID 註冊電子郵件地址與密碼（business account），則不會顯示刪除圖示。請點擊電子郵件地址區段的編輯圖示，並註冊您的電子郵件地址與密碼。

   ![Unlink LINE account](https://developers.line.biz/media/line-developers-console/unlink-business-account-with-line-account-en.png)

1. 在確認畫面上點擊 **Delete**

   ![Click Delete on the confirmation screen](https://developers.line.biz/media/line-developers-console/unlink-business-account-click-delete-en.png)

1. Business ID 與 LINE 帳號即解除連結

## Available features 

您可以建立的頻道（channel）類型取決於登入 LINE Developers Console 的開發者帳號是否與 LINE 帳號連結。

依據您所使用的開發者帳號被指派的角色（role），您可使用的功能會有所限制。如需更多資訊，請參閱 [Managing roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/)。

依據開發者帳號與 LINE 帳號的連結狀態，可使用的頻道類型如下：

| Link status | LINE Login | Blockchain Service | LINE MINI App |
| --- | --- | --- | --- |
| 已與 LINE 帳號連結的開發者帳號 | ✅ | ✅ | ✅ |
| 未與 LINE 帳號連結的開發者帳號 | ✅ | ❌ | ✅ |

Messaging API 頻道可透過建立 LINE 官方帳號（LINE Official Accounts）來建立。如需更多資訊，請參閱 Messaging API 文件中的 [Get started with the Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/)。
