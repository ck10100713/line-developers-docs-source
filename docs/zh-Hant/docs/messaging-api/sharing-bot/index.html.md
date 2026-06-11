# 為你的 LINE 官方帳號增加好友

當你建立好 LINE 官方帳號後，接下來就是宣傳你的 LINE 官方帳號並增加好友。了解如何讓使用者接觸到你的 LINE 官方帳號：

- [使用 QR code](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#use-qr-code)
- [分享你 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)
- [使用加入好友按鈕或連結](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#use-the-add-friend-button-or-link)
- [鼓勵使用者向 LINE 上的好友推薦你的 LINE 官方帳號](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#encourage-users-to-recommend-your-bot-to-friends-on-line)
- [在 LINE Login 時提示使用者將你的 LINE 官方帳號加為好友](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#prompt-users-to-add-your-line-official-account-at-line-login)

## Use QR code 

在你的網站上或以印刷品形式分享 LINE 官方帳號的 QR code。使用者只需掃描你的 QR code，即可將你的 LINE 官方帳號加為好友。你可以從 [LINE Developers Console](https://developers.line.biz/console/) 或 [LINE Official Account Manager](https://manager.line.biz/) 取得 QR code。

在 LINE Developers Console 中，點選你頻道設定的 **Messaging API** 分頁。

![](https://developers.line.biz/media/messaging-api/sharing-bot/qr-code-console-en.png)

在 LINE Official Account Manager 中，點選 **Home** > **Gain friends** > **"Add friend" tools** > **Create an "Add friend" QR code**。你可以複製 HTML 片段並將程式碼貼到你的網站上，以顯示 QR code。

![](https://developers.line.biz/media/messaging-api/sharing-bot/qr-code-oa-manager-en.png)

## Share the LINE ID of your LINE Official Account 

讓使用者知道你 LINE 官方帳號的 LINE ID，使用者就能在 LINE 上搜尋你的 LINE 官方帳號並將其加為好友。你可以從 [LINE Official Account Manager](https://manager.line.biz/) 的頁首找到你 LINE 官方帳號的 LINE ID。以小老鼠符號（@）為前綴的文字就是你 LINE 官方帳號的 LINE ID。

此外，你也可以購買付費 ID（premium ID），建立一個更容易讓使用者記住的自訂 LINE ID。有關付費 ID 的更多資訊，請參閱 LINE for Business 中的 [Subscription plan](https://www.lycbiz.com/jp/service/line-official-account/plan/)（僅提供日文）。

![](https://developers.line.biz/media/messaging-api/sharing-bot/oa-manager-line-id.png)

## Use the Add Friend button or link 

在你的應用程式或網站上加入按鈕或連結後，使用者只要在裝置上輕觸一下，就能將你的 LINE 官方帳號加為好友。你可以加入以下按鈕或連結：

- [由 LINE Social Plugins 提供的加入好友按鈕](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#add-friend-button-by-line-social-plugins)
- [由 LINE Official Account Manager 提供的加入好友按鈕](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#add-friend-button-by-the-line-manager)
- [個人檔案頁面的 LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#line-url-scheme-for-profile-page)

### Add Friend button by LINE Social Plugins 

LINE Social Plugins 會產生一段[加入好友按鈕](https://developers.line.biz/en/docs/line-social-plugins/install-guide/using-add-friend-buttons/)的程式碼。你只需將程式碼複製並貼到你的應用程式或網站上即可加入這個按鈕。此按鈕提供多種語言版本。你也可以顯示你 LINE 官方帳號的好友數量，並加入連結至你 LINE 官方帳號首頁的連結。

若要使用 LINE Social Plugins 產生的**加入好友**按鈕，請參閱 [Create button](https://developers.line.biz/en/docs/line-social-plugins/install-guide/using-add-friend-buttons/#create-button) 的說明。

![](https://developers.line.biz/media/messaging-api/sharing-bot/add-friend-button-types.png)

### Add friend button by LINE Official Account Manager 

[LINE Official Account Manager](https://manager.line.biz/) 會產生一段**加入好友**按鈕的程式碼。點選 **Home** > **Gain Friends** > **"Add friend" tools** > **Create a button**。將 HTML 程式碼複製並貼到你的網站上，即可顯示按鈕。

![](https://developers.line.biz/media/messaging-api/sharing-bot/add-friend-button-oa-manager-en.png)

### LINE URL scheme for profile page 

你可以從你的網頁應用程式或原生應用程式，使用這個 LINE URL scheme 提示使用者將你的 LINE 官方帳號加為好友。當在 LINE for iOS 或 LINE for Android 中輕觸此 LINE URL scheme 時，會開啟你 LINE 官方帳號的商家個人檔案頁面。

- https://line.me/R/ti/p/`{Percent-encoded LINE ID}`&nbsp;

例如，[`https://line.me/R/ti/p/%40linedevelopers`](https://line.me/R/ti/p/%40linedevelopers) 會顯示 LINE Developers 的 LINE 官方帳號商家個人檔案頁面。有關 LINE URL scheme 的更多資訊，請參閱 [Sharing a LINE Official Account](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#sharing-line-official-account)。

![](https://developers.line.biz/media/messaging-api/sharing-bot/add-line-developers-oa-en.png)

## Encourage users to recommend your LINE Official Account to friends on LINE 

如果使用者已經將你的 LINE 官方帳號加為好友，你可以使用這個 LINE URL scheme 鼓勵使用者向他們在 LINE 上的好友推薦你的 LINE 官方帳號。

- https://line.me/R/nv/recommendOA/`{LINE ID with @}`&nbsp;

例如，在[圖文選單（rich menu）](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)或[範本訊息（template messages）](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)的 [URI action object](https://developers.line.biz/en/reference/messaging-api/#uri-action) 中指定此 LINE URL scheme。有關此 LINE URL scheme 的更多資訊，請參閱 [Sharing a LINE Official Account](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#sharing-line-official-account)。

![](https://developers.line.biz/media/messaging-api/sharing-bot/recommend-line-developers-rich-menu.png)

## Prompt users to add your LINE Official Account as a friend at LINE Login 

如果你在網頁應用程式或原生應用程式中使用 [LINE Login](https://developers.line.biz/en/docs/line-login/overview/)，你可以將 LINE 官方帳號連結至你的 LINE Login 頻道，在登入過程中提示使用者將你的 LINE 官方帳號加為好友。你可以選擇在同意畫面中加入選項，或在使用者同意後另外開啟「加入 LINE 官方帳號」畫面。

有關如何將你的 LINE 官方帳號連結至 LINE Login 頻道的說明，請參閱 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。

![If bot_prompt=normal, the option to add a friend is displayed on the consent screen. If bot_prompt=aggressive, the option to add a friend is displayed after the user has consented.](https://developers.line.biz/media/line-login/link-a-bot/bot-prompt-en.png)

## Learn more 

- [Use LINE features with the LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/)
- [Messaging API reference](https://developers.line.biz/en/reference/messaging-api/)
- [LINE Social Plugins](https://developers.line.biz/en/docs/line-social-plugins/)
- [LINE Official Account Manager](https://manager.line.biz/)
