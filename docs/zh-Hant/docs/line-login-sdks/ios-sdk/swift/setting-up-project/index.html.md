# 設定您的專案

本主題說明如何將 LINE SDK for iOS Swift 整合至您的 iOS 專案，並套用必要的設定。

為了讓您的 app 與最新的 iOS 版本相容並充分運用其功能，我們強烈建議您遵循本安裝指南，並使用最新版本的 LINE SDK for iOS Swift。

## Prerequisites 

若要建置與使用 LINE SDK for iOS Swift，您需要：

- 一個 [provider](https://developers.line.biz/en/glossary/#provider) 與一個 LINE Login 頻道（channel）。您可以在 LINE Developers Console 中[同時建立兩者](https://developers.line.biz/console/register/line-login/channel/)。
- iOS 13.0 或更新版本作為部署目標（deployment target）
- Xcode 14.1 或更新版本

<!-- tip start -->

**將 iOS 13.0 之前的版本作為部署目標的支援**

如果您想支援 iOS 13.0 之前的版本作為部署目標，請使用較舊版本的 LINE SDK for iOS Swift。詳情請參閱 [Releases](https://github.com/line/line-sdk-ios-swift/releases)。

<!-- tip end -->

您可以將 LINE SDK for iOS Swift 與 Swift 或 Objective-C 程式碼搭配使用。本指南假設您使用 Swift 程式碼來實作 LINE SDK for iOS Swift。若要使用 Objective-C 程式碼整合 LINE SDK for iOS Swift，請參閱 [Using the SDK with Objective-C](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/using-objc/)。

## Installation 

LINE SDK for iOS Swift 與先前的 LINE SDK for iOS Objective-C 版本不相容。如果您正在升級 LINE SDK 的版本，請在進行升級前先參閱 [Upgrading the SDK](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/migration-guide/)。

### CocoaPods 

如果您不熟悉 CocoaPods，請參閱 [CocoaPods Getting Started Guide](https://guides.cocoapods.org/using/getting-started.html)。在透過 CocoaPods 將 LINE SDK for iOS Swift 整合至您的 app 之前，您的機器上需要先安裝 CocoaPods gem。

1. 當您的 Podfile 準備好後，將下方的 pod 指令加入您的 target：

    ```ruby
    platform :ios, '13.0'
    use_frameworks!

    target '<Your App Target Name>' do
        pod 'LineSDKSwift', '~> 5.0'
    end
    ```

1. 執行以下指令：

    ```bash
    $ pod install
    ```

LINE SDK for iOS Swift 將會被下載並整合至您的 Xcode workspace 中。

### Carthage 

[Carthage](https://github.com/Carthage/Carthage) 是一個去中心化的相依性管理工具，它會建置您的相依套件並提供二進位框架（binary frameworks）。

1. 若要安裝 Carthage 工具，請使用 [Homebrew](https://brew.sh/)。

    ```bash
    $ brew update
    $ brew install carthage
    ```

1. 若要使用 Carthage 將 LINE SDK for iOS Swift 整合至您的 Xcode 專案，請在您的 Cartfile 中指定 SDK 的 GitHub 儲存庫，如下所示：

    ```
    github "line/line-sdk-ios-swift" ~> 5.0
    ```

1. 執行以下指令以建置 LINE SDK for iOS Swift：

    ```
    $ carthage update line-sdk-ios-swift
    ```

現在您可以依照後續章節所述的步驟，將已建置的 `LineSDK.framework` 檔案加入您的 Xcode 專案。

#### Linking the `LineSDK.framework` file to your Xcode project 

將 `LineSDK.framework` 檔案從 `Carthage/Build/iOS` 資料夾拖放至您應用程式 target 的「General」設定分頁中的「Linked Frameworks and Libraries」區段。

![LINE SDK Framework file being moved from Finder to the Linked Frameworks and Libraries section in your app target.](https://developers.line.biz/media/ios-sdk-swift/install-link.png)

#### Copying the `LineSDK.framework` file during the build phase 

1. 點選您應用程式 target 的「Build Phases」設定分頁中的 **+** 圖示，並選擇 **New Run Script Phase**。建立一個內容如下的 run script：

    ```
    /usr/local/bin/carthage copy-frameworks
    ```

1. 在「Input Files」區段下加入 `LineSDK.framework` 檔案的路徑：

    ```
    $(SRCROOT)/Carthage/Build/iOS/LineSDK.framework
    ```

1. 在「Output Files」區段下加入 `LineSDK.framework` 檔案的路徑：

    ```
    $(BUILT_PRODUCTS_DIR)/$(FRAMEWORKS_FOLDER_PATH)/LineSDK.framework
    ```

run script 看起來應該像這樣：

![Run script section expanded to show Shell, Input Files, Input File Lists, and Output Files.](https://developers.line.biz/media/ios-sdk-swift/install-carthage-copy.png)

## Linking your app to your channel 

將您的 app 連結至 LINE Login 頻道需要一些設定。在 [LINE Developers Console](https://developers.line.biz/console/) 中，前往您的 LINE Login 頻道設定，並在 **LINE Login** 分頁中填寫以下欄位：

- **iOS bundle ID：** 您 app 的 Bundle 識別碼，可在 Xcode 專案設定的「General」分頁中找到。必須為小寫。例如 `com.example.app`。您可以透過在每一行各輸入一個識別碼來指定多個 Bundle 識別碼。
- **iOS universal link：** 輸入為您 app 設定的 universal link。關於如何使用 universal link 處理登入流程的更多資訊，請參閱 [Using universal links](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/universal-links-support/)。

![LINE Login iOS bundle ID and universal link settings.](https://developers.line.biz/media/line-login/integrate-login-ios/ios-app-settings.png)

## Configuring the `Info.plist` file 

在 Xcode 中，對您 app 的 `Info.plist` 檔案按右鍵並選擇 **Open As** > **Source Code**。在最後一個 `</dict>` 標籤之前插入以下程式碼片段：

```xml
<key>CFBundleURLTypes</key>
<array>
    <dict>
        <key>CFBundleTypeRole</key>
        <string>Editor</string>
        <key>CFBundleURLSchemes</key>
        <array>
            <!-- Specify URL scheme to use when returning from LINE to your app. -->
            <string>line3rdp.$(PRODUCT_BUNDLE_IDENTIFIER)</string>
        </array>
    </dict>
</array>
<key>LSApplicationQueriesSchemes</key>
<array>
    <!-- Specify URL scheme to use when launching LINE from your app. -->
    <string>lineauth2</string>
</array>
```

此程式碼片段會加入以下設定：

Key | Description
--- | -----------
CFBundleURLSchemes | 使用 `line3rdp.$(PRODUCT_BUNDLE_IDENTIFIER)` 來定義開啟您 app 所需的 URL scheme。iOS 會儲存此 URL scheme 以供日後參考。LINE Login 會在 LINE Platform 回傳登入結果後，使用此 scheme 開啟您的 app。<br /> 注意：URL scheme `lineauth2` 已用於啟動 LINE。請勿在 CFBundleURLSchemes 中使用此 scheme。
LSApplicationQueriesSchemes | 指定 `lineauth2` 以允許從您的 app 啟動 LINE。app 會在登入流程中啟動 LINE。
