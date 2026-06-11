# 開始使用 LINE Login（Getting started with LINE Login）

本頁說明如何透過部署一個簡單的入門網頁應用程式（starter web app）來開始使用 LINE Login。這個網頁應用程式能讓使用者用他們的 LINE 帳號登入。你可以使用使用者登入時所核發的存取權杖（access token）來取得使用者的個人資料。

完成本頁的所有步驟後，你會更深入地了解 LINE Login 的運作方式，以及如何將它整合進你的網頁應用程式。

<!-- tip start -->

**iOS／Android／Unity 入門應用程式**

我們也針對特定平台提供入門應用程式：

- [試用入門應用程式 - iOS Swift](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/try-line-login/)
- [試用範例應用程式 - Android](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/try-line-login/)
- [試用入門應用程式 - Unity](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/try-line-login/)

<!-- tip end -->

## Before you begin 

在你能使用 LINE Login 入門應用程式之前，你需要準備以下項目：

| 需求 | 說明 |
| --- | --- |
| LINE 帳號 | LINE 應用程式的帳號。你需要一個 LINE 帳號才能試用這個入門應用程式。若要建立 LINE 帳號，請[下載](https://line.me/) iOS 版或 Android 版的 LINE 並註冊。如需更多關於建立新 LINE 帳號的資訊，請參閱 LINE 使用者指南中的[建立新帳號](https://guide.line.me/ja/signup-and-migration/line-signup.html)（僅提供日文版）。 |
| Provider | Provider 是一個概念，用來描述提供應用程式的個人或組織。請在 [LINE Developers Console](https://developers.line.biz/console/) 上建立 provider。每位 LINE 使用者在每個 provider 下都會有不同的使用者 ID。 |
| LINE Login 頻道（channel） | 頻道（channel）構成你的應用程式與 LINE Platform 之間的連結。請在 provider 內建立頻道。你需要為每個應用程式建立一個頻道。請在 [LINE Developers Console](https://developers.line.biz/console/register/line-login/channel/) 上建立 LINE Login 頻道。<br/>注意事項：<ul><li>如果你從未登入過 LINE Developers Console，系統會先要求你註冊為開發者。<ul><li>建立 LINE Login 頻道的步驟說明於 [Step 1：建立你的 LINE Login 頻道](https://developers.line.biz/en/docs/line-login/getting-started/#step-1-create-channel)。</li></ul></li><li>建立要用於入門應用程式的 LINE Login 頻道時，請務必在 **App types** 下選擇 **Web app**。</li></ul> |
| Heroku 帳號 | [Heroku](https://www.heroku.com/) 是一項為網頁應用程式提供託管服務的服務。將入門應用程式部署到 Heroku，代表你不需要擁有自己的伺服器。 |
| Heroku CLI | 使用某些 Heroku 功能時需要 [Heroku 命令列介面（CLI）](https://devcenter.heroku.com/articles/heroku-cli)。 |

<!-- note start -->

**Heroku 的免費方案已停止**

Heroku 的免費方案已於 2022 年 11 月 27 日停止。如果你想免費試用這個入門應用程式，請使用其他平台。如需更多資訊，請參閱 [Heroku's Next Chapter](https://www.heroku.com/blog/next-chapter/)。

<!-- note end -->

## Step 1: Create your LINE Login channel 

讓我們從建立 LINE Login 頻道開始。

[頻道（channel）](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)是你的應用程式連接到 LINE Platform 的通道。請在 [LINE Developers Console](https://developers.line.biz/console/register/line-login/channel/) 上為你的每個網頁應用程式建立一個 LINE Login 頻道。

1. 登入 [LINE Developers Console](https://developers.line.biz/console/)。
2. 選擇一個 provider，並從 **Channels** 分頁中選擇 **LINE Login**。
3. 在這些欄位中輸入必要的資訊以建立頻道：

| 項目 | 必填？ | 說明 | 對使用者顯示的位置 |
| --- | --- | --- | --- |
| **Channel type** | ✅ | 頻道類型。選擇 LINE Login 以建立你的 LINE Login 頻道。 | - |
| **Provider** | ✅ | 頻道的 [provider](https://developers.line.biz/en/docs/line-developers-console/overview/#provider) | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **Region to provide the service** | ✅ | 你想提供 LINE Login 服務的地區。為以下其中之一：<br><ul><li>日本</li><li>泰國</li><li>台灣</li><li>印尼</li></ul>\*如果你想在多個地區提供服務，請為每個地區建立一個頻道。 | - |
| **Company or owner's country or region** | ✅ | 管理該頻道的公司或所有者的國家或地區 | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **Channel icon** | ❌ | 頻道的圖示 | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **Channel name** | ✅ | 頻道的名稱 <br>\*頻道名稱不能包含「LINE」或類似的字串。 | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **Channel description** | ✅ | 頻道的說明 | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **App types** | ✅ | 你打算整合 LINE Login 的應用程式類型。為以下其中之一：<br><ul><li>Web app</li><li>Mobile app</li></ul>\*在部署入門應用程式的範例中，請選擇 **Web app**。 | - |
| **Email address** | ✅ | 接收關於頻道重要更新的電子郵件地址 | - |
| **Privacy policy URL** | 參閱說明 | 應用程式隱私權政策的 URL。如果你的 provider 是[認證 provider（certified provider）](https://developers.line.biz/en/docs/line-developers-console/overview/#certified-provider)則為必填。 | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **Terms of use URL** | ❌ | 應用程式使用條款的 URL | 啟動 LINE Login 或 LIFF App 時的權限同意畫面 |
| **LINE Developers Agreement** | ✅ | 閱讀並同意 [LINE Developers Agreement](https://terms2.line.me/LINE_Developers_Agreement?lang=en)。 | - |
| **LY Corporation Privacy Policy** | 參閱說明 | 僅在你於 **Region to provide the service** 選擇泰國時為必填。閱讀並確認 [LY Corporation Privacy Policy](https://line.me/th/terms/policy/)。 | - |

### Precautions for channel and provider linkage 

一旦你建立了頻道，之後就無法將該頻道移動到其他 provider。

當你開發一個將 LINE Login 頻道與 Messaging API 頻道連結的服務時，請在同一個 provider 內建立這兩個頻道。

使用開發者所提供服務的 LINE 使用者，在每個 provider 下都會獲得不同的使用者 ID。使用者 ID 無法用於跨不同 provider 下的頻道來識別同一位使用者。

![](https://developers.line.biz/media/line-developers-console/different-user-ids.png)

<!-- warning start -->

**建立頻道時需特別留意的情況**

例如，以下情況需要特別留意：

- 頻道與 provider 由個人或公司管理。
- 在同一個 provider 下建立彼此不相關的服務或公司的頻道。
- 在由提供頻道管理工具等服務的服務（公司）所管理的 provider 下建立頻道。

在這些情況下，由於日後無法在 provider 之間移動頻道，以及使用者在不同 provider 下會獲得不同使用者 ID 的事實，未來可能會產生問題。在考量相關風險後，請在適當的 provider 下建立頻道。

<!-- warning end -->

<!-- tip start -->

**provider 與頻道管理的最佳實務**

有一個頁面以具體範例說明如何管理 provider 與頻道的管理員角色，以及你應該在哪個 provider 下建立頻道。

如需更多資訊，請參閱 LINE Developers Console 文件中的 [Best practices for provider and channel management](https://developers.line.biz/en/docs/line-developers-console/best-practices-for-provider-and-channel-management/)。

<!-- tip end -->

## Step 2: Deploy the starter app 

接下來，使用在 Step 1 建立的頻道之頻道 ID（channel ID）與頻道密鑰（channel secret），將入門應用程式部署到 Heroku。請依照以下步驟操作：

1. 前往 GitHub 上的 [line-login-starter](https://github.com/line/line-login-starter) 儲存庫。
2. 在 [README](https://github.com/line/line-login-starter) 中，點選 **Deploy to Heroku**。
3. 在 Heroku 的「Create New App」頁面填寫必要的資訊：
   - Heroku app name <br/>必須是唯一的。建議：<code v-pre>line-login-starter-{YYYYMMDD}</code>
   - Region
   - Config Variables
     - 採用以下格式的 Callback URL：`https://{Heroku app name}.herokuapp.com/auth`
     - Channel ID（可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到）
     - Channel secret（可在 [LINE Developers Console](https://developers.line.biz/console/) 中找到）
4. 選擇 **Deploy app** 並確認你的應用程式已成功部署。

## Step 3: Check the channel settings and enter the callback URL

為了在網頁應用程式中使用 LINE Login 頻道，必須正確設定 **App Type** 與 **Callback URL**。

1. 從 [LINE Developers Console](https://developers.line.biz/console/) 中，選擇你在 Step 1 建立的頻道。
2. 點選 **Basic settings** 分頁，並確認 **App types** 下顯示的是 **Web app**。
3. 點選 **LINE Login** 分頁，並輸入來自 Heroku 的 **Callback URL**（`https://{Heroku app name}.herokuapp.com/auth`）。

### LINE Login's basic settings 

**Basic settings** 分頁包含關於你頻道的基本資訊。以下是你會看到的資訊：

| 項目 | 說明 |
| --- | --- |
| **Channel ID** | 頻道的唯一識別碼 |
| **Region to provide the service** | 你想提供 LINE Login 服務的地區。你只能在建立新頻道時設定地區。 |
| **Company or owner's country or region** | 管理該頻道的公司或所有者的國家或地區 |
| **Channel icon** | 頻道的圖示 |
| **Channel name** | 頻道的名稱 |
| **Channel description** | 頻道的說明 |
| **Email address** | 接收關於頻道重要更新的電子郵件地址 |
| **Privacy policy URL** | 應用程式隱私權政策的 URL |
| **Terms of use URL** | 應用程式使用條款的 URL |
| **App types** | 你打算整合 LINE Login 的應用程式類型 |
| **Permissions** | 此頻道可存取的使用者資料類型 |
| **Channel secret** | 一個唯一的密鑰，你可用它授予應用程式存取你頻道的權限 |
| **Assertion Signing Key** | 與你的 assertion signing key 配對相關聯的 UUID |
| **Your user ID** | 你 LINE 帳號的使用者 ID |
| **Linked LINE Official Account** | 連結到此頻道的 LINE 官方帳號（LINE Official Account）。你只能連結來自同一個 provider 的 LINE 官方帳號。 |
| **Localization** | 你可以新增其他語言，為你的頻道提供多語言支援。 |
| **Email address permission** | 申請使用 OpenID Connect 來請求使用者電子郵件的權限。 |
| **Delete** | 刪除此頻道。 |

## Step 4: Try the app 

1. 瀏覽你應用程式的 URL（`https://{Heroku app name}.herokuapp.com`）。你應該會看到以下畫面：

   ![LINE Login starter app login](https://developers.line.biz/media/line-login/getting-started/line-login-starter-app-login.png)

2. 點選 **Log in**。

   你將被重新導向到我們的標準登入頁面。該 URL 以 `https://access.line.me/oauth2/v2.1/` 開頭，並包含許多查詢參數。若要了解它們的意義，請閱讀[將 LINE Login 整合進你的網頁應用程式](https://developers.line.biz/en/docs/line-login/integrate-line-login/)。

3. 登入 LINE 並同意授予應用程式所需的權限。

當你成功使用 LINE 憑證登入後，應用程式會顯示你的 LINE 使用者個人資料圖片、顯示名稱與狀態消息。（如果你使用的是 iOS 或 Android 裝置且已登入 LINE，你將會自動登入。）

### Try out the other features of the starter app 

登入應用程式後，你可以選擇以下按鈕來試用此應用程式的其他功能：

- 驗證使用者存取權杖
- 重新整理使用者存取權杖
- 撤銷（revoke）存取權杖（登出）

### Check logs 

使用 [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) 查看你應用程式的日誌。

1. 從命令列登入 Heroku。

   ```sh
   $ heroku login
   ```

1. 查看日誌。

   ```sh
   $ heroku logs --app {Heroku app name} --tail
   ```

## Step 5: Customize your app 

你可以將入門應用程式下載到你的本機電腦，以便自行測試與修改。接著，你可以將應用程式部署到你選擇的網頁伺服器。在此，我們將說明如何對你在 Step 1 建立的 Heroku 應用程式進行修改並部署。

請確認你已安裝以下項目：

- JDK 1.8 或更新版本
- Maven™ 3.0 或更新版本
- Git™

1. 複製（clone）[line-login-starter](https://github.com/line/line-login-starter) GitHub 儲存庫。

   ```sh
   git clone https://github.com/line/line-login-starter.git
   ```

1. 使用 `cd` 進入 `line-login-starter`。
1. 為你的本機儲存庫新增 Heroku 的遠端（remote）。

   ```sh
   $ heroku git:remote -a {Heroku app name}
   ```

1. 進行編輯並提交（commit）變更（選用）。

   ```sh
   $ git add .
   $ git commit -m "First commit"
   ```

1. 將變更推送（push）到 Heroku master。

   ```sh
   $ git push heroku master
   ```

## Step 6: Publish your channel (optional) 

LINE Login 頻道建立時的狀態為「Developing」。在此狀態下，只有具備 Admin 或 Tester 角色的使用者（請參閱[管理角色](https://developers.line.biz/en/docs/line-developers-console/managing-roles/)）才能使用該 LINE Login 頻道。如果你想讓其他使用者存取你的應用程式，你必須將應用程式的狀態變更為「Published」。若要這麼做，請在 [LINE Developers Console](https://developers.line.biz/console/) 上開啟你的 LINE Login 頻道，並點選頁面頂端的 **Developing** 狀態。

如果你目前的頻道僅供測試用途，你可以維持原狀不變。但若要讓任何未來的應用程式可供使用者使用，你需要發布與其連結的頻道。請注意，一旦你將狀態變更為「Published」，就無法再將它改回「Developing」。

### How to test with a LINE Login channel with the "Developing" status 

當你使用狀態為「Developing」的 LINE Login 頻道進行測試時，被賦予在該頻道測試角色的開發者帳號，必須連結到一個 LINE 帳號。透過將 LINE 帳號連結到與你開發者帳號相關聯的 Business ID，你就能將你的 LINE 帳號連結到你的開發者帳號。

開發者帳號永遠以一對一的方式連結到 Business ID。然而，將 Business ID 連結到你的 LINE 帳號則是選用的。因此，可能會有你的 Business ID 與 LINE 帳號未連結的情況。當你測試 LINE Login 時，請確認你的 Business ID 已連結到你的 LINE 帳號。

當你測試 LINE Login 時，你需要使用連結到你開發者帳號的 LINE 帳號來登入。請注意，你無法使用為 Business ID 所註冊的電子郵件地址與密碼來登入。

如需更多關於將 Business ID 與 LINE 帳號連結的資訊，請參閱 LINE Developers Console 文件中的 [Link your Business ID with your LINE account](https://developers.line.biz/en/docs/line-developers-console/login-account/#link-business-account-with-line-account)。

## Next steps 

- [將 LINE Login 整合進你的網頁應用程式](https://developers.line.biz/en/docs/line-login/integrate-line-login/)
- [將 LINE Login 整合進你的 iOS 應用程式](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/)
- [將 LINE Login 整合進你的 Android 應用程式](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/)
- [將 LINE Login 整合進你的 Unity 遊戲](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/integrate-line-login/)
