# 搭配 Objective-C 程式碼使用 SDK（Using the SDK with Objective-C code）

## Overview 

雖然 LINE SDK for iOS Swift 是以純 Swift 撰寫的，但你仍然可以在 Objective-C 專案中使用它。有兩種做法可以達成此目的。

## Option 1: Make a mixed-language project 

如果你對 Swift 以及 Swift／Objective-C 互通性有一些經驗，我們建議你將 LINE SDK for iOS Swift 直接整合進你的 Objective-C 專案，並使用 Swift 來呼叫 LINE SDK 的 API。

任何既有的 Objective-C 專案都可以轉換成混合 Objective-C 與 Swift 的多語言專案。你可以在多語言專案中加入與 LINE SDK for iOS Swift 互動的 Swift 檔案。

若要在 Objective-C 中使用來自 Swift 檔案的必要宣告，請以 `@objc` 或 `@objcMembers` 屬性將它們公開。如需這些屬性的詳細資訊，請參閱 Swift.org 的 [Attributes](https://docs.swift.org/swift-book/ReferenceManual/Attributes.html#ID592)。

當你將 Swift 檔案匯入專案時，Xcode 會自動產生一個橋接標頭檔（bridging header），以便將這些檔案公開給 Objective-C 程式碼。如需橋接標頭檔的詳細資訊，請參閱 Apple 的 [Importing Swift into Objective-C](https://developer.apple.com/documentation/swift/importing-swift-into-objective-c)。

若要瞭解如何讓 Swift 類別可在 Objective-C 專案中使用，我們也推薦以下文章：

- [Jen Sipila](https://jen-sip.medium.com/) 撰寫的 [Setting up Swift and Objective-C Interoperability](https://medium.com/ios-os-x-development/swift-and-objective-c-interoperability-2add8e6d6887)：尤其可參考「Make a Swift Class available to Objective-C Files」一節。
- Apple 撰寫的 [Migrating Your Objective-C Code to Swift](https://developer.apple.com/documentation/swift/migrating-your-objective-c-code-to-swift)：這篇文章能幫助你瞭解整個流程。

## Option 2: Use the Objective-C wrapper 

若要使用 Objective-C 程式碼與 LINE SDK for iOS Swift 互動，請使用 LINE SDK for iOS Swift 所提供的 Objective-C wrapper。與選項 1 不同的是，你需要將額外的 Objective-C wrapper 框架加入專案。本節將說明 Objective-C wrapper 的基本概念、安裝方式以及常見用法。

LINE SDK for iOS Swift 僅與 Swift 程式碼相容。Objective-C wrapper 是建構在核心 SDK 之上，使其能與 Objective-C 程式碼相容，並提供 LINE SDK for iOS Swift 大部分的核心功能。由於 Objective-C 規格與 Swift 並非完全相容，因此有些功能在 Objective-C wrapper 中無法使用。

為了避免與原始 SDK 的名稱發生潛在衝突，型別名稱與大部分的 SDK 元件都會加上「LineSDK」前綴。此 wrapper 也需要額外的設定步驟。

請記住，此 wrapper 只是使用 LINE SDK for iOS Swift 的暫時方法。我們建議你將專案遷移至 Swift，以便存取 LINE SDK for iOS Swift 的完整功能。

### Installation 

#### Prerequisites 

若要建置並透過 Objective-C wrapper 使用 LINE SDK for iOS Swift，你需要：

- iOS 11.0 以上版本作為部署目標（deployment target）。
- Xcode 10 以上版本。

#### CocoaPods 

如果你不熟悉 CocoaPods，請參閱 [CocoaPods Getting Started Guide](https://guides.cocoapods.org/using/getting-started.html)。在透過 CocoaPods 將 LINE SDK for iOS Swift 整合進你的應用程式之前，你的機器上需要先安裝 CocoaPods gem。

1. 準備好 Podfile 後，將下列 pod 指令加入你的 target：

    ```ruby
    platform :ios, '11.0'
    use_frameworks!

    target '<Your App Target Name>' do
        pod 'LineSDKSwift/ObjC', '~> 5.0'
    end
    ```

1. 執行下列指令：

    ```bash
    $ pod install
    ```

1. LINE SDK for iOS Swift 將會被下載並整合進你的 Xcode workspace。

##### Importing the SDK 

加入 `@import LineSDK;`，將搭配 Objective-C wrapper 的 LINE SDK for iOS Swift 匯入你的 Objective-C 專案，如下所示：

```objective-c
#import "ViewController.h"
@import LineSDK;

@implementation ViewController
// ...
@end
```

#### Carthage 

[Carthage](https://github.com/Carthage/Carthage) 是一個去中心化的相依套件管理工具，它會建置你的相依套件並提供二進位框架（binary frameworks）給你。

1. 若要安裝 Carthage 工具，請使用 [Homebrew](https://brew.sh/)。

    ```bash
    $ brew update
    $ brew install carthage
    ```

1. 若要使用 Carthage 將 LINE SDK for iOS Swift 整合進你的 Xcode 專案，請在你的 Cartfile 中指定該 SDK 的 GitHub 儲存庫，如下所示：

    ```
    github "line/line-sdk-ios-swift" ~> 5.0
    ```

1. 執行下列指令來建置 LINE SDK for iOS Swift：

    ```
    $ carthage update line-sdk-ios-swift
    ```

現在，你可以依照後續各節所述的步驟，將建置完成的 `LineSDK.framework` 與 `LineSDKObjC.framework` 檔案加入你的 Xcode 專案。

##### Linking the framework files to your Xcode project 

將 `LineSDK.framework` 與 `LineSDKObjC.framework` 檔案從 `Carthage/Build/iOS` 資料夾拖放到你的應用程式 target「Build Phases」設定分頁中的「Link Binary With Libraries」區段。

##### Copying the framework files during the build phase 

1. 點選你的應用程式 target「Build Phases」設定分頁中的 **+** 圖示，並選擇 **New Run Script Phase**。建立一個內容如下的執行指令稿（run script）：

    ```
    /usr/local/bin/carthage copy-frameworks
    ```

1. 在「Input Files」區段下加入框架檔案的路徑：

    ```
    $(SRCROOT)/Carthage/Build/iOS/LineSDK.framework
    $(SRCROOT)/Carthage/Build/iOS/LineSDKObjC.framework
    ```

1. 在「Output Files」區段下加入框架檔案的路徑：

    ```
    $(BUILT_PRODUCTS_DIR)/$(FRAMEWORKS_FOLDER_PATH)/LineSDK.framework
    $(BUILT_PRODUCTS_DIR)/$(FRAMEWORKS_FOLDER_PATH)/LineSDKObjC.framework
    ```

「Build Phases」分頁應如下所示：

![iOS SDK Swift ObjC Link Build Phases tab, showing the Link Binary with Libraries, Copy Bundle Resources, and Run Script sub tabs.](https://developers.line.biz/media/ios-sdk-swift/install-carthage-objc.png)

##### Enabling the "Always Embed Swift Standard Libraries" option 

在「Build Settings」設定分頁中，將「Always Embed Swift Standard Libraries」（`ALWAYS_EMBED_SWIFT_STANDARD_LIBRARIES`）選項設為「YES」，以便將 Swift 標準函式庫納入你最終的應用程式套件（app bundle）中。

##### Importing the SDK 

加入 `@import LineSDKObjC;`，將搭配 Objective-C wrapper 的 LINE SDK for iOS Swift 匯入你的 Objective-C 專案，如下所示：

```objective-c
#import "ViewController.h"
@import LineSDKObjC;

@implementation ViewController
// ...
@end
```

### Naming conventions 

使用 Objective-C wrapper 時，型別名稱與大部分的 SDK 元件都會加上「LineSDK」前綴。以下程式碼範例示範如何在 Objective-C 中處理常見的工作：

#### Logging in users with multiple permissions 

```objective-c
NSSet *permissions = [NSSet setWithObjects:
                          [LineSDKLoginPermission profile],
                          [LineSDKLoginPermission openID],
                          nil];
[[LineSDKLoginManager sharedManager]
    loginWithPermissions:permissions
        inViewController:self
              parameters:nil
       completionHandler:^(LineSDKLoginResult *result, NSError *error) {
           if (result) {
               NSLog(@"User Name: %@", result.userProfile.displayName);
           } else {
               NSLog(@"Error: %@", error);
           }
       }
 ];
```

#### Getting user profiles 

```objective-c
[LineSDKAPI getProfileWithCompletionHandler:
    ^(LineSDKUserProfile * _Nullable profile, NSError * _Nullable error)
{
    if (profile) {
        NSLog(@"User Name: %@", profile.displayName);
    } else {
        NSLog(@"Error: %@", error);
    }
}];
```

### Handling errors with the Objective-C wrapper 

為了確保與 Objective-C 慣例相容，Objective-C wrapper 會擲出 `NSError` 物件。下列程式碼會檢查錯誤是否與 LINE SDK 相關。

```objective-c
NSError *error = // ... An error from LINE SDK ObjC Wrapper
if ([error.domain isEqualToString:[LineSDKErrorConstant errorDomain]]) {
    // SDK Error
}
```

由 wrapper 擲出的所有錯誤，其 `code` 與 `userInfo` 屬性都與原始 LINE SDK for iOS Swift 所擲出的相同。你可以利用它們找出錯誤的原因。

```objective-c
if (error.code == 2004) {
    // invalidHTTPStatusAPIError
    NSNumber *statusCode = error.userInfo[[LineSDKErrorConstant userInfoKeyStatusCode]];
    if ([statusCode integerValue] == 403) {
        // Permission granting issue. Ask for authorization with enough permission again.
    }
}
```

若要瞭解如何辨識並處理錯誤，請參閱 [Handling errors](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/error-handling/)。
