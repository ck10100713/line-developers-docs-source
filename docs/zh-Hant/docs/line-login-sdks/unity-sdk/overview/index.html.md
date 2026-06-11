# LINE SDK for Unity 總覽（LINE SDK for Unity overview）

LINE SDK for Unity 提供了一種現代化的方式來實作 LINE Platform API。此 SDK 所包含的功能將協助你開發具備吸引力且個人化使用者體驗的 Unity 遊戲。

## Features 

LINE SDK for Unity 是 [LINE SDK for iOS Swift](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/) 與 [LINE SDK for Android](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/) 的封裝（wrapper）。它在執行於 iOS 或 Android 上的 Unity 遊戲中提供以下功能。

### User authentication 

此功能可讓使用者以其 LINE 帳號登入你的 Unity 遊戲。在 LINE SDK for Unity 的協助下，將 LINE Login 整合到你的應用程式中變得前所未有地容易。如果使用者已在其 Android 裝置上登入 LINE，他們將自動登入你的應用程式，而無須輸入 LINE 登入憑證。這為使用者提供了一個絕佳的方式，讓他們無須經歷註冊流程即可開始使用你的應用程式。

### Utilizing user data with OpenID support 

一旦使用者授權後，你就可以取得他們的 LINE 個人檔案。你可以運用使用者在 LINE 中註冊的資訊，而無須建置你自己的使用者系統。

LINE SDK 支援 [OpenID Connect](https://openid.net/developers/how-connect-works/) 1.0 規格。當你取得存取權杖（access token）時，可以取得包含使用者 LINE 個人檔案的 ID 權杖（ID token）。

### API calls 

使用 LINE SDK 所包含的方法來取得使用者個人檔案資訊、登出使用者，以及管理存取權杖。

## Open-sourced SDK 

LINE SDK for Unity 是一個開源專案。請造訪[我們的儲存庫](https://github.com/line/line-sdk-unity)來查看所提供的程式碼與範例。

## Using the SDK 

若要在你的 Unity 遊戲中使用 LINE SDK，請依照以下步驟操作。

1. 建立一個頻道（channel）。如需更多資訊，請參閱 LINE Login 文件中的 [Getting started with LINE Login](https://developers.line.biz/en/docs/line-login/getting-started/)。
2. 使用 SDK 為你的 Unity 遊戲加入 LINE Login 支援。如需更多資訊，請參閱 [Integrating LINE Login with your Unity game](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/integrate-line-login/)。
3. 透過 SDK 從你的應用程式發出 API 呼叫，或透過 LINE Login API 從伺服器端程式碼發出 API 呼叫。如需更多資訊，請參閱 [LINE SDK for Unity API reference](https://developers.line.biz/en/reference/unity-sdk/) 與 [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

### Trying the starter app 

你可以使用我們的入門應用程式（starter app）來瞭解 LINE Login 的運作方式。請參閱 [Trying the starter app](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/try-line-login/)。

## What's in this guide 

本指南說明如何將 LINE SDK 整合到你的 Unity 遊戲中，並從你的應用程式使用 SDK 中提供的 API 功能。下表列出本指南中的主題及其內容。

| Title | Content |
| --- | --- |
| [LINE SDK for Unity overview](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/overview/) | SDK 功能與使用 SDK 的高階步驟。 |
| [Setting up project](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/project-setup/) | 整合 LINE SDK for Unity 所需的先決條件與環境。 |
| [Trying the starter app](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/try-line-login/) | 如何執行我們的入門應用程式。 |
| [Integrating LINE Login with your Unity game](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/integrate-line-login/) | 如何將 LINE SDK 整合到你的專案中，並運用 LINE Login 來提升應用程式的使用者體驗。 |
| [Using LINE SDK for other APIs and result handling](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/using-sdk/) | LINE SDK for Unity 的用法與其他細節。 |
| [LINE SDK for Unity reference](https://developers.line.biz/en/reference/unity-sdk/) | SDK 中可用介面與類別的詳細資訊。 |

## Other resources 

| Title | Content |
| --- | --- |
| [Release notes for LINE SDK for Unity](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/release-notes/) | SDK 的變更記錄。 |
