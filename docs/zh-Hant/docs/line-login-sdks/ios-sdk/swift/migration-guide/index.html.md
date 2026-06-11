# 升級 SDK

## Upgrading to the latest SDK 

5.0.0 是 LINE SDK for iOS Swift 的第一個版本。此版本與[舊版 Objective-C 版本](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/deprecated/objective-c-v41/overview/)不相容。若您要升級至 LINE SDK for iOS Swift，需要變更部分程式碼。

<!-- note start -->

**Note**

全新的 LINE SDK for iOS Swift 是為 Swift 專案所設計。不過，您仍然可以在 Objective-C 程式碼中使用這個新版 SDK。若要了解如何在 Objective-C 程式碼中使用此 SDK，請參閱[在 Objective-C 程式碼中使用 SDK](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/using-objc/)。

<!-- note end -->

無論您使用的是哪一種語言的舊版本，升級 SDK 時，建議移除所有與舊版 SDK 相關的程式碼行，並依照[設定您的專案](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/)中的步驟執行全新安裝。不過，如果您想要在目前的實作基礎上進行變更，以下是一些通用步驟：

1. 從您的程式碼庫中移除舊的 `LineSDK.framework` 檔案。
    - 如果您使用如 CocoaPods 和 Carthage 等套件管理工具，請從套件定義檔（Podfile 或 Cartfile）中移除「LineSDK」項目。接著執行全新安裝，以移除專案中對 `LineSDK.framework` 檔案的參照。
    - 如果您使用下載的二進位檔，只需將其從專案中移除即可。

1. 清理您的 `Info.plist` 檔案。您可以安全地從檔案中移除 `LineSDKConfig` 項目，因為已不再需要此項目。

1. 安裝 LINE SDK for iOS Swift。詳細步驟請參閱[設定您的專案](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/)。

1. 在 `AppDelegate` 檔案中設定頻道 ID 與 callback 處理。

    在 app 啟動後隨即呼叫 `LoginManager.setup` 方法，如下所示：

    ```swift
    func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
        // Add this to your "didFinishLaunching" delegate method.
        LoginManager.shared.setup(channelID: "YOUR_CHANNEL_ID", universalLinkURL: nil)

        return true
    }
    ```

    更新開啟 URL 的處理，如下所示：

    ```swift
    func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
        return LoginManager.shared.application(app, open: url, options: options)
    }
    ```

## Updating your code to use the latest SDK 

接下來您已準備好更新所有其他的程式碼行，以便使用最新的 LINE SDK。以下章節將說明一些常見的範例。

本章節並未涵蓋所有的 SDK 功能。不過，由於 LINE SDK 遵循類似的慣例，您可以輕鬆地在其中找到對應的型別。請更新您的程式碼以使用最新的 LINE SDK，讓您的專案能夠順利編譯。

我們提供一個與最新版 LINE SDK for iOS Swift 相容的範例 app。請參閱我們的[開放原始碼儲存庫](https://github.com/line/line-sdk-ios-swift)，以了解基本的整合方法與用法。

<!-- note start -->

**透過 LINE 將使用者登入您的 app**

**由 LINE SDK 4.x 版本所核發的存取權杖（access token）無法用於 5.x 版本。**如果您升級 LINE SDK，所有使用者都必須重新登入，您的 app 才能存取 LINE Platform。

<!-- note end -->

#### Previous 

```swift
// First set the delegate to the current object
LineSDKLogin.sharedInstance().delegate = self
LineSDKLogin.sharedInstance().start()

// MARK: LineSDKLoginDelegate

func didLogin(_ login: LineSDKLogin, credential: LineSDKCredential?, profile: LineSDKProfile?, error: Error?) {

    if let error = error {
        print("LINE Login Failed with Error: \(error.localizedDescription) ")
        return
    }

    print("LINE Login Succeeded")
}
```

#### Now 

```swift
LoginManager.shared.login(permissions: [.profile]) {
    result in
    switch result {
    case .success(let loginResult):
        print("User name: \(loginResult.userProfile?.displayName ?? "nil")")
    case .failure(let error):
        print("Error: \(error)")
    }
}
```

### Getting user profiles 

#### Previous 

```swift
var apiClient: LineSDKAPI
apiClient = LineSDKAPI(configuration: LineSDKConfiguration.defaultConfig())

apiClient.getProfile(queue: .main) {
    (profile, error) in

    if let error = error {
        print("Error getting profile \(error.localizedDescription)")
    }

    print(profile?.displayName ?? "none")
    print(profile?.pictureURL ?? "none")
    print(profile?.statusMessage ?? "none")
    print(profile?.userID ?? "none")
}
```

#### Now 

```swift
API.getProfile { result in
    switch result {
    case .success(let profile):
        print("User name: \(profile.displayName)")
    case .failure(let error):
        print("Error: \(error)")
    }
}
```

### Logging out users 

#### Previous 

```swift
var apiClient: LineSDKAPI
apiClient = LineSDKAPI(configuration: LineSDKConfiguration.defaultConfig())

apiClient.logout(queue: .main) {
    (success, error) in

    if success {
        print("Logout Succeeded")
    }
    else {
        print("Logout Failed \(error?.localizedDescription as String?)")
    }
}
```

#### Now 

```swift
LoginManager.shared.logout { result in
    switch result {
    case .success:            print("Logout Succeeded")
    case .failure(let error): print("Logout Failed: \(error)")
    }
}
```

### Getting the current access token 

#### Previous 

```swift
var apiClient: LineSDKAPI
apiClient = LineSDKAPI(configuration: LineSDKConfiguration.defaultConfig())

let myToken = apiClient.currentAccessToken()
```

#### Now 

```swift
let token = AccessTokenStore.shared.current?.value
```

### Verifying access tokens 

#### Previous 

```swift
var apiClient: LineSDKAPI
apiClient = LineSDKAPI(configuration: LineSDKConfiguration.defaultConfig())

apiClient.verifyToken(queue: .main) {
    (result, error) in

    if let error = error {
        print("Token is Invalid: \(error.localizedDescription)")
        return
    }

    guard let result = result, let permissions = result.permissions else {
        print("Response result is null")
        return
    }
    print("Token is Valid")
}
```

#### Now 

```swift
API.Auth.verifyAccessToken { result in
    switch result {
    case .success: print("Token is valid.")
    case .failure(let error): print("Error: \(error)")
    }
}
```
