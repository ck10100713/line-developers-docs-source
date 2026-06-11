# LINE SDK for iOS 版本資訊

<!-- note start -->

**5.0.0 以後版本的版本資訊已移至 GitHub 儲存庫**

LINE SDK for iOS 5.0.0 以後版本的版本資訊，已可在 GitHub 儲存庫上查看。詳情請參閱 [Releases](https://github.com/line/line-sdk-ios-swift/releases)。

<!-- note end -->

November 20, 2018

## LINE SDK 5.0.0 for iOS released

LINE SDK 5.0.0 for iOS 已發布。關於安裝與使用說明，請參閱 [LINE SDK for iOS guide](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/)。

#### Changes

##### LINE Login v2.1 and Social API v2.1 are supported

當使用者透過 LINE Login 登入您的應用程式時，您可以將要授予應用程式的權限設定為 scope。透過設定 scope，您可以在取得存取權杖（access token）時一併取得 ID 權杖（ID token）。這些權杖會依照您在登入請求中設定的 scope 包含使用者資料。

您可以為登入您應用程式的使用者顯示「將您的 bot 加為好友」的選項。您可以透過登入回應與 Social API 取得使用者與您 bot 之間的好友關係狀態。

##### New SDK version in Swift

LINE SDK for iOS Swift 以 Swift 開發，為實作 LINE API 提供了現代化的方式。LINE SDK 5.0.0 for iOS Objective-C 是我們 Objective-C SDK 的最後一個版本。

##### Open-source SDK

LINE SDK for iOS Swift 已開源。請造訪[我們的儲存庫](https://github.com/line/line-sdk-ios-swift)查看提供的程式碼與範例。

##### Detailed reference

現在您可以存取以原始碼為基礎的詳細參考文件。詳情請參閱以下內容：

- [LINE SDK for iOS Swift reference](https://developers.line.biz/en/reference/ios-sdk-swift/)
- [LINE SDK for iOS Objective-C reference](https://developers.line.biz/en/reference/ios-sdk-objc/)

April 13, 2018

## LINE SDK 4.1.1 for iOS released

LINE SDK 4.1.1 for iOS 已發布。您可以從以下頁面下載此 SDK。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了 `LineSDKLogin` 物件在登出後仍於快取中保留存取權杖的問題。

January 29, 2018

## LINE SDK 4.1.0 for iOS released

LINE SDK 4.1.0 for iOS 已發布。您可以從以下頁面下載此 SDK。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 網頁登入流程現在改用 Safari View Controller，而非外部瀏覽器。

March 22, 2017

##  LINE SDK for iOS CocoaPod released

我們已在 CocoaPods 上發布 LINE SDK for iOS。現在您可以使用 CocoaPods 為您的 Objective-C 與 Swift 專案下載 LINE SDK for iOS。

關於如何使用 CocoaPods 下載此 SDK，請參閱以下連結。

- 使用 [CocoaPods](https://cocoapods.org/) 下載

January 27, 2017

## LINE SDK 4.0.1 for iOS released

LINE SDK 4.0.1 for iOS 已發布。您可以從以下頁面下載此 SDK。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了使用 Web Login 時造成驗證錯誤的問題。

December 13, 2016

## Change to requirement on whitelisting LINE domains

將 LINE 網域加入白名單已不再是使用 LINE SDK for iOS 的必要條件。因此，原本位於 Settings for iOS 9 or later 章節中關於將 LINE 網域加入白名單的說明文件已被移除。

October 7, 2016

## The LINE SDK 3.2.1 for iOS released

LINE SDK for iOS 已更新至 3.2.1 版本。您可以從以下頁面的 LINE SDK 封存中下載：

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- `LineAdapter+Login.framework` 與 `LineAdapterUI.framework` 已合併至 `LineAdapter.framework`。
- 變更了 swift 的定義。

此外，LINE SDK 起始應用程式（starter application）已修訂以相容於此版本的 SDK。您可以從下方的 GitHub 儲存庫複製（clone）或下載。

- [https://github.com/line/line-sdk-starter-ios](https://github.com/line/line-sdk-starter-ios)
