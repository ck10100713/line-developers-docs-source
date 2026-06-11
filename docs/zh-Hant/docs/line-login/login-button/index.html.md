# LINE Login 按鈕設計指南（LINE Login button design guidelines）

新增 LINE Login 按鈕，讓使用者可以透過 [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) 登入您的應用程式。

![LINE Login button image](https://developers.line.biz/media/line-login/login-button/login-button-en.png)

LINE Login 按鈕由以下元件組成：LINE 圖示、LINE 圖示對話框，以及 LINE Login 按鈕文字。

使用 LINE Login 按鈕前，請務必閱讀並同意 [Usage Guidelines for the LINE Login Button](https://terms2.line.me/LINE_Developers_Guidelines_for_Login_Button)。當您下載以下 LINE Login 按鈕範本時，即視為您已同意這份指南。

[Download the LINE Login button template](https://vos.line-scdn.net/line-developers/docs/media/line-login/login-button/LINE_Login_Button_Image.zip)

<br>該檔案包含多組不同解析度的圖片，可用於 web、iOS 或 Android 應用程式。您可使用 PSD 檔案，以不同語言新增自訂的登入文字。

## Design guidelines 

新增 LINE Login 按鈕到您的應用程式時，請遵循以下設計指南。

### Size 

只要圖片符合以下條件，您就可以依據顯示按鈕的裝置，放大或縮小 LINE Login 按鈕的尺寸。

- LINE 圖示的長寬比不會改變。
- LINE 圖示維持清晰可見。

### Color 

LINE Login 按鈕只能使用以下顏色。

| Item | Color |
| :--- | :--- |
| Base color | ![base color](https://developers.line.biz/media/line-login/login-button/06c755.png)#06C755 |
| Hover | ![base color](https://developers.line.biz/media/line-login/login-button/06c755.png)#06C755 + ![hover color](https://developers.line.biz/media/line-login/login-button/000000-10-per.png)#000000 (opacity: 10%) |
| Press | ![base color](https://developers.line.biz/media/line-login/login-button/06c755.png)#06C755 + ![press color](https://developers.line.biz/media/line-login/login-button/000000-30-per.png)#000000 (opacity: 30%) |
| Disabled | ![white color](https://developers.line.biz/media/line-login/login-button/ffffff.png)#FFFFFF |
| Font/logo color (other than disabled) | ![logo white color](https://developers.line.biz/media/line-login/login-button/ffffff.png)#FFFFFF |
| Font/logo color (only disabled) | ![logo grey color](https://developers.line.biz/media/line-login/login-button/1e1e1e-20-per.png)#1E1E1E (opacity: 20%) |
| Vertical line color (other than disabled) | ![line color for other than disabled](https://developers.line.biz/media/line-login/login-button/000000-8-per.png)#000000 (opacity: 8%) |
| Vertical line color (only disabled) | ![line color for only disabled](https://developers.line.biz/media/line-login/login-button/e5e5e5-60-per.png)#E5E5E5 (opacity: 60%) |
| Border color (only disabled) | ![border color](https://developers.line.biz/media/line-login/login-button/e5e5e5-60-per.png)#E5E5E5 (opacity: 60%) |

<!-- note start -->

**注意透明度色層的疊放順序**

對於帶透明度的顏色，請留意您將其疊放的色層。舉例來說，以 hover 按鈕上的垂直線為例，請將 hover（`#000000 (opacity: 30%)`）疊放在基本色層（`#06C755`）之上，接著再將垂直線（`#000000 (opacity: 8%)`）與文字／logo（`#FFFFFF`）疊放在更上層。

![Layers of LINE login buttons](https://developers.line.biz/media/line-login/login-button/login-button-color-layer-order-en.png)

關於各色層的擺放方式，詳情請參閱下圖。

<!-- note end -->

![LINE Login button color](https://developers.line.biz/media/line-login/login-button/login-button-color-en.png)

### Text 

建議的 LINE Login 按鈕文字為「Log in with LINE」。各種語言的建議用語清單可參考下表。

如果您決定使用自訂的按鈕文字，請務必遵循以下指南：

- 不可換行
- 文字清楚向使用者表明此按鈕是用於以 LINE 登入該應用程式

您也可以單獨使用 LINE 圖示、不搭配任何按鈕文字，作為 LINE Login 按鈕。

|Language|Login button text (long)|Login button text (short)|
|--- |--- |--- |
|en|Log in with LINE|Log in|
|ja|LINEでログイン|ログイン|
|ko|LINE으로 로그인|로그인|
|de|Mit LINE anmelden|Anmelden|
|es|Iniciar sesión con LINE|Iniciar sesión|
|fr|Connexion avec LINE|Se connecter|
|id|Masuk dengan LINE|Masuk|
|it|Login con LINE|Login|
|ms|Log masuk dengan LINE|Log Masuk|
|pt-BR|Login com o LINE|Login|
|pt-PT|Iniciar sessão com o LINE|Iniciar sessão|
|ru|Войти в LINE|Войти|
|th|ล็อกอินด้วย LINE|ล็อกอิน|
|tr|LINE ile oturum açın|Oturum Aç|
|ar|تسجيل دخول باستخدام LINE|تسجيل دخول|
|vi|Đăng nhập với LINE|Đăng nhập|
|zh-CN|用LINE帐号登录|登录|
|zh-TW|與LINE連動|連動|

### Font 

按鈕文字的字型必須清晰易讀。各圖片尺寸的建議字型大小已包含在 PSD 檔案中。

### Padding 

登入按鈕文字左右兩側內距（padding）的寬度，必須等於或大於 LINE 圖示對話框的寬度。此寬度在下圖中定義為 X。

登入按鈕文字上下內距的建議高度為 X/2。請務必使用能維持此內距的字型大小。

![LINE Login button padding](https://developers.line.biz/media/line-login/login-button/login-button-padding-en.png)

### Isolation zone 

隔離區（isolation zone）是 LINE Login 按鈕周圍不可放置任何元素的空間。隔離區的寬度必須等於或大於 LINE 圖示對話框的左側內距。此寬度在下圖中定義為「A」。除了維持隔離區之外，也請避免在隔離區附近放置文字或圖形，因為這可能會降低 LINE Login 按鈕的成效。

![LINE Login button isolation zone](https://developers.line.biz/media/line-login/login-button/login-button-isolation-zone.png)

### Common mistakes to avoid 

- 使用非指定的顏色
- 使用過時的 LINE 圖示
- 使用其他圖示或經過修改的圖示，而非使用 LINE 圖示
