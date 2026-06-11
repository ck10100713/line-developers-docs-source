# LINE SDK for iOS Swift 總覽（LINE SDK for iOS Swift overview）

LINE SDK for iOS Swift 以 Swift 開發，提供一套現代化的方式來實作 LINE Platform API。本 SDK 所包含的功能，將協助你開發出具有吸引力且個人化使用者體驗的 iOS app。

## Features 

LINE SDK for iOS Swift 提供以下功能。

### User authentication 

這項功能可讓使用者以其 LINE 帳號登入你的 app 或服務。在 LINE SDK for iOS Swift 的協助下，將 LINE Login 整合進你的 app 從未如此簡單。若使用者已在其 iOS 裝置上登入 LINE，他們將自動登入你的 app，無須輸入 LINE 的登入憑證。這為使用者提供了一個絕佳的方式來開始使用你的 app，而不必經歷註冊流程。

### Utilizing user data with OpenID support 

一旦使用者完成授權，你就能取得使用者的 LINE 個人檔案。你無須自行建置使用者系統，即可運用使用者在 LINE 中所註冊的資訊。

LINE SDK 支援 [OpenID Connect](https://openid.net/developers/how-connect-works/) 1.0 規格。當你取得存取權杖（access token）時，可以取得包含使用者 LINE 個人檔案的 ID 權杖（ID token）。

### API calls 

使用 LINE SDK 所包含的方法，來取得使用者個人檔案資訊、將使用者登出，以及管理存取權杖。

## Open-source SDK 

LINE SDK for iOS Swift 是一個開放原始碼專案。請造訪[我們的儲存庫](https://github.com/line/line-sdk-ios-swift)，查看我們提供給你使用的程式碼與範例。

## Using the LINE SDK 

若要在你的 iOS app 中使用 LINE SDK，請依照以下步驟操作。

1. 建立一個頻道（channel）。

   詳情請參閱 LINE Login 文件中的 [Getting started with LINE Login](https://developers.line.biz/en/docs/line-login/getting-started/)。

2. 使用 LINE SDK 將 LINE Login 支援加入你的 iOS app。

   詳情請參閱 [Setting up your project](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/) 與 [Integrating LINE Login with your iOS app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/)。

3. 使用 LINE Login。

   若要進一步了解如何在你的 app 中使用 LINE Login，請參閱 [Managing users](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/) 與 [LINE SDK for iOS Swift reference](https://developers.line.biz/en/reference/ios-sdk-swift/)。

   若要進一步了解如何在你的伺服器上使用 LINE Login，請參閱 [Managing access tokens](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-access-tokens/) 與 [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

### Trying the starter app 

你可以使用我們的 starter app 來了解 LINE Login 的運作方式。請參閱 [Trying the starter app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/try-line-login/)。

## What's in this guide 

本指南說明如何將 LINE SDK 整合進你的 app，並從你的 app 使用 SDK 中可用的 API 功能。本指南所討論的主題概觀請參閱下表。

| 標題 | 內容 |
| --- | --- |
| [LINE SDK for iOS Swift overview](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/overview/) | SDK 的功能，以及使用 SDK 的概略步驟。 |
| [Trying the starter app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/try-line-login/) | 如何執行我們的 starter app。 |
| [Setting up your project](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/) | 如何將 LINE SDK 整合進你的專案。 |
| [Integrating LINE Login with your iOS app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/) | 如何運用 LINE Login 來改善你的 app 使用者體驗。 |
| [Enabling the add friend option with the SDK](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/link-a-bot/) | 如何向使用者顯示加入 LINE 官方帳號為好友的選項，並取得 LINE 官方帳號與使用者之間的好友關係狀態。 |
| [Managing users](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-users/) | 如何取得使用者個人檔案、使用 ID 權杖取得使用者資料，以及將使用者登出。 |
| [Managing access tokens](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/managing-access-tokens/) | 如何重新整理與驗證存取權杖，以及取得目前的存取權杖。 |
| [Handling errors](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/error-handling/) | 如何處理 SDK 所回傳的錯誤。 |
| [Using the SDK with Objective-C code](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/using-objc/) | 如何將 LINE SDK for iOS Swift 整合進你的 Objective-C 專案。 |
| [Upgrading the SDK](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/migration-guide/) | 如何從 LINE SDK v4.1 for iOS 升級至 LINE SDK v5 for iOS Swift。 |
| [LINE SDK v5 for iOS Swift reference](https://developers.line.biz/en/reference/ios-sdk-swift/) | SDK 中可用的協定（protocol）與類別（class）的詳細資訊。 |

## Other resources 

| 標題 | 內容 |
| --- | --- |
| [Release notes for LINE SDK for iOS](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/release-notes/) | SDK 變更紀錄。 |
| [LINE API SDKs](https://developers.line.biz/en/docs/downloads/) | 下載 LINE SDK 的連結。 |
