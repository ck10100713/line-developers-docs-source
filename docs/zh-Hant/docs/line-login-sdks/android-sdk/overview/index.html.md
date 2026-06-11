# LINE SDK for Android 總覽（LINE SDK for Android overview）

LINE SDK for Android 提供一套現代化的方式來實作 LINE Platform API。本 SDK 所包含的功能將協助你開發出具有吸引力且個人化使用者體驗的 Android 應用程式。

## Features 

LINE SDK for Android 提供下列功能。

### User authentication 

此功能讓使用者能以自己的 LINE 帳號登入你的服務。在 LINE SDK for Android 的協助下，將 LINE Login 整合到你的應用程式中變得前所未有地簡單。如果使用者已在自己的 Android 裝置上登入 LINE，他們便能自動登入你的應用程式，無須輸入 LINE 登入憑證。這為使用者提供了絕佳的方式，讓他們無須經過註冊流程即可開始使用你的應用程式。

### Utilizing user data with OpenID support 

使用者授權後，你可以取得該使用者的 LINE 個人檔案。你無須自行建立使用者系統，即可運用使用者註冊於 LINE 的資訊。

LINE SDK 支援 [OpenID Connect](https://openid.net/developers/how-connect-works/) 1.0 規格。當你取得存取權杖（access token）時，可以一併取得包含使用者 LINE 個人檔案的 ID 權杖（ID token）。

### API calls 

使用 LINE SDK 所包含的方法，可取得使用者個人檔案資訊、登出使用者，以及管理存取權杖。

## Open-source SDK 

LINE SDK for Android 是一個開放原始碼專案。請造訪 [我們的程式碼儲存庫](https://github.com/line/line-sdk-android) 以查看所提供的程式碼與範例。

## Using the LINE SDK 

請依照下列步驟，將 LINE SDK 用於你的 Android 應用程式。

1. 建立一個頻道（channel）。

   如需更多資訊，請參閱 LINE Login 文件中的 [Getting started with LINE Login](https://developers.line.biz/en/docs/line-login/getting-started/)。

2. 使用 LINE SDK 為你的 Android 應用程式加入 LINE Login 支援。

   如需更多資訊，請參閱 [Integrating LINE Login with your Android app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/)。

   若要進一步了解如何使用加入好友選項，請參閱 [Enabling the add friend option with the SDK](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/)。

3. 使用 LINE Login。

   若要進一步了解如何在你的應用程式中使用 LINE Login，請參閱 [Managing users](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/) 與 [LINE SDK for Android reference](https://developers.line.biz/en/reference/android-sdk/)。

   若要進一步了解如何在你的伺服器上使用 LINE Login，請參閱 [Managing access tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/) 與 [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

### Trying the sample app 

你可以透過我們的入門應用程式（starter app）了解 LINE Login 的運作方式。如需更多資訊，請參閱 [Trying the sample app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/try-line-login/)。

## What's in this guide 

本指南說明如何將 LINE SDK 整合到你的應用程式中，並從你的應用程式使用 SDK 中可用的 API 功能。請參閱下表，了解本指南所討論主題的總覽。

| Title | Content |
| --- | --- |
| [LINE SDK for Android overview](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/overview/) | SDK 功能以及使用 SDK 的高階步驟。 |
| [Trying the sample app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/try-line-login/) | 如何執行我們的範例應用程式。 |
| [Integrating LINE Login with your Android app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/) | 如何將 LINE SDK 整合到你的專案中，並運用 LINE Login 來提升應用程式的使用者體驗。 |
| [Enabling the add friend option with the SDK](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/) | 如何向使用者顯示將 LINE 官方帳號加為好友的選項，並取得 LINE 官方帳號與使用者之間的好友關係狀態。 |
| [Managing users](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/) | 如何取得使用者個人檔案、使用 ID 權杖取得使用者資料，以及登出使用者。 |
| [Managing access tokens](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/) | 如何重新整理及驗證存取權杖，並取得目前的存取權杖。 |
| [Handling errors](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/handling-errors/) | SDK 回傳的錯誤。 |
| [LINE SDK v5 for Android reference](https://developers.line.biz/en/reference/android-sdk/) | SDK 中可用的介面與類別的詳細資訊。 |

## Other resources 

| Title | Content |
| --- | --- |
| [Release notes for LINE SDK for Android](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/release-notes/) | SDK 變更紀錄。 |
| [LINE API SDKs](https://developers.line.biz/en/docs/downloads/) | LINE SDK 的下載連結。 |
