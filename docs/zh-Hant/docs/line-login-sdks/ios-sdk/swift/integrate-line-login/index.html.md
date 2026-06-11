# 將 LINE Login 整合至你的 iOS app

當你[安裝 SDK](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/) 並設定好專案後，就可以開始運用 LINE Login 來改善你的 app 的使用者體驗。

## Setting up the LineSDK framework and your channel ID 

為了處理透過登入動作所產生的結果，請在 `AppDelegate.swift` 檔案中設定 LINE SDK for iOS Swift。

### 1. Import the LineSDK framework 

在 `AppDelegate.swift` 檔案的最上方，如下方所示 import `LineSDK` framework：

```swift
// AppDelegate.swift
import LineSDK
```

若要在你的 app 中的其他檔案使用此 SDK，也請在那些檔案中 import 此 SDK。

### 2. Call the `LoginManager.setup` method 

請在你的 app 啟動後，如下方所示立即呼叫 `LoginManager.setup` 方法：

```swift
func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?) -> Bool {
    // Add this to your "didFinishLaunching" delegate method.
    LoginManager.shared.setup(channelID: "YOUR_CHANNEL_ID", universalLinkURL: nil)

    return true
}
```

<!-- note start -->

**Note**

請務必在你存取 LINE SDK for iOS Swift 的其他屬性或呼叫其他方法**之前**，先呼叫 `setup` 方法。

<!-- note end -->

#### Using a universal link 

如果你在 LINE Developers Console 中設定了 universal link，請在呼叫 `setup` 方法時帶入 `universalLinkURL` 參數。這會讓 LINE 透過 universal link 開啟你的 app，藉此確保登入流程的安全性。

關於如何使用 universal link 處理登入流程的更多資訊，請參閱 [Using universal links](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/universal-links-support/)。

### 3. Handle app opening 

為了處理由 LINE Platform 回傳的認證結果，請將收到的 URL 傳給 `LoginManager` 的 `application(_:open:options:)` 方法。這表示你需要修改你的 app delegate class，或是你的 scene delegate classes，取決於你的專案是否支援多視窗（multiple windows，這是 [iOS 13 引進](https://developer.apple.com/documentation/uikit/scenes)的功能）。

#### Modify app delegate 

iOS 12 及更早版本會透過呼叫你的 `UIApplicationDelegate` 物件來開啟 URL。因此，請在你的 app delegate class 的 `application(_:open:options:)` delegate 方法中加入下列程式碼：

```swift
// AppDelegate.swift
func application(_ app: UIApplication, open url: URL, options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    return LoginManager.shared.application(app, open: url)
}
```

#### Modify scene delegates 

預設情況下，iOS 13 及之後的版本會嘗試透過呼叫 `UISceneDelegate` 物件來開啟 URL。

如果你是用 Xcode 11 或之後的版本建立專案，預設它會包含一個 `SceneDelegate.swift` 檔案，且你的 `Info.plist` 檔案會包含 `UIApplicationSceneManifest` 項目。請在你想使用的任何 scene delegate class 中加入下列程式碼：

如果你的 app 支援多視窗，請在你想使用的任何 scene delegate class 中加入下列程式碼：

```swift
// SceneDelegate.swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    _ = LoginManager.shared.application(.shared, open: URLContexts.first?.url)
}
```

<!-- note start -->

**If you're not supporting multiple windows**

如果你的 app 不支援多視窗，iOS 會呼叫你的 `UIApplicationDelegate` 物件來開啟 URL。請改為修改你的 app delegate class。

<!-- note end -->

## Performing a login process 

為了讓使用者登入你的 iOS app，你可以建立一個 LINE 品牌的登入按鈕，引導使用者完成認證與授權流程。

新增登入按鈕有 2 種方式：

- [使用 LINE SDK 內建的登入按鈕](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/#use-button)
- [使用你自己的程式碼](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/#use-code)

### Use the LINE SDK's built-in login button 

LINE SDK for iOS Swift 提供了一個預先定義好的登入按鈕。SDK 中的 `LoginButton` class 是 `UIButton` class 的子類別，並遵循 [LINE Login button design guidelines](https://developers.line.biz/en/docs/line-login/login-button/) 中建議的樣式。你可以如下方所示，在你的 app 的使用者介面中加入一個登入按鈕，提供使用者快速登入的方式：

```swift
// In your view controller
override func viewDidLoad() {
    super.viewDidLoad()

    // Create Login Button.
    let loginButton = LoginButton()
    loginButton.delegate = self

    // Configuration for permissions and presenting.
    loginButton.permissions = [.profile]
    loginButton.presentingViewController = self

    // Add button to view and layout it.
    view.addSubview(loginButton)
    loginButton.translatesAutoresizingMaskIntoConstraints = false
    loginButton.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
    loginButton.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
}
```

當你的使用者點選登入按鈕時，系統會以適當的登入流程對使用者進行認證：如果使用者的裝置上已安裝 LINE，你的 app 會向 LINE 取得使用者的 LINE 憑證以進行認證。否則，使用者會被重新導向到瀏覽器上的 LINE Login 對話框，並被要求輸入其 LINE 憑證。

為了接收登入狀態，請如下方所示實作 `LoginButtonDelegate` protocol 中的相關 delegate 方法：

```swift
extension LoginViewController: LoginButtonDelegate {
    func loginButton(_ button: LoginButton, didSucceedLogin loginResult: LoginResult) {
        hideIndicator()
        print("Login Succeeded.")
    }

    func loginButton(_ button: LoginButton, didFailLogin error: LineSDKError) {
        hideIndicator()
        print("Error: \(error)")
    }

    func loginButtonDidStartLogin(_ button: LoginButton) {
        showIndicator()
        print("Login Started.")
    }
}
```

當登入流程結束時，其中一個 delegate 方法會帶著登入結果被呼叫。

### Use your own code 

除了使用預設的登入按鈕之外，你也可以用自己的程式碼自訂使用者介面與登入流程。

若要執行登入流程，請呼叫 `LoginManager.login` 方法並帶入適當的參數。通常登入流程會發生在 view controller 中，如下方所示：

```swift
// LoginViewController.swift

import LineSDK

class LoginViewController: UIViewController {
    override func viewDidLoad() {
        //...
    }

    func login() {
        LoginManager.shared.login(permissions: [.profile], in: self) {
            result in
            switch result {
            case .success(let loginResult):
                print(loginResult.accessToken.value)
                // Do other things you need with the login result
            case .failure(let error):
                print(error)
            }
        }
    }
}
```

當使用者完成登入流程後，completion handler 會帶著 `result` 引數被呼叫。對登入結果進行 switch 即可存取登入詳細資訊。

如果登入成功，LINE Platform 會回傳一個包含常見登入資訊的 `LoginResult` 物件。請使用 `LoginManager.shared.isAuthorized` 方法來存取登入狀態。

如果在登入流程中發生錯誤，LINE SDK 會回傳 `.failure` 的 `result` 引數，以及相關的 `LineSDKError` enumeration 成員。關於如何從 SDK 取得錯誤細節並妥善處理，請參閱 [Handling errors](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/error-handling/)。

關於如何設計你的登入介面，請參閱 [LINE Login button design guidelines](https://developers.line.biz/en/docs/line-login/login-button/)，你也可以在該頁面下載 LINE Login 按鈕圖片。

## Handling the login result 

### Token permissions 

雖然你可以在呼叫 `LoginManager.login` 方法時，指定任何你希望使用者授予你的 app 的權限，但你的頻道（channel）可能並未具備對應的權限。在這種情況下，`LoginResult` 物件的 `permissions` 屬性會與你在授權請求中所指定的不同。

若要檢查與存取權杖（access token）關聯的已授權權限，請取得 `permissions` 屬性。例如，可使用下方程式碼檢查權杖中是否包含 `.profile` 權限：

```swift
case .success(let loginResult):
    let profileEnabled = loginResult.permissions.contains(.profile)
```

不具備適當權限的 API 呼叫會失敗。更多資訊請參閱 [Handling errors](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/error-handling/)。

### User profile 

如果你在授權請求中指定了 profile 權限，登入結果就會包含一個 `UserProfile` 物件。你可以如下方所示，透過存取使用者個人檔案資訊來建構你自己的使用者系統：

```swift
LoginManager.shared.login(permissions: [.profile], in: self) {
    result in
    switch result {
    case .success(let loginResult):
        if let profile = loginResult.userProfile {
            print("User ID: \(profile.userID)")
            print("User Display Name: \(profile.displayName)")
            print("User Icon: \(String(describing: profile.pictureURL))")
        }
    case .failure(let error):
        print(error)
    }
}
```

使用者 ID 僅在單一 provider 內是唯一的。同一位 LINE 使用者在不同的 provider 之下會有不同的使用者 ID。請避免使用使用者 ID 來跨不同 provider 識別使用者。

### Using user data on your server 

<!-- warning start -->

**User impersonation**

當 `UserProfile` 物件中的使用者 ID 或其他資訊是由用戶端傳送至你的後端伺服器時，請不要信任這些資料。惡意的用戶端可能會傳送任意的使用者 ID 或經竄改的資訊到你的伺服器，藉此假冒（impersonate）某位使用者。

正確做法是，用戶端應該傳送一個存取權杖給伺服器，而伺服器應該使用該權杖來取得使用者資料。

<!-- warning end -->

通常，後端伺服器會根據使用者 ID、顯示名稱或其他 LINE 帳號屬性來驗證使用者的身分。請不要將這些資訊以純文字形式從 app 傳送到後端，而是傳送儲存在 app 中的存取權杖。接著，使用該存取權杖來安全地傳送與接收資料。你的後端伺服器可以向 LINE Platform 驗證該存取權杖，然後取得使用者的詳細資料。

存取權杖可以從 `LoginResult` 物件取得。以下是一個範例：

```swift
LoginManager.shared.login(permissions: [.profile], in: self) {
    result in
    switch result {
    case .success(let loginResult):
        let token = loginResult.accessToken.value
        // Send `token` to your server.
    case .failure(let error):
        print(error)
```

關於要從你的後端呼叫哪些 API，請參閱下列頁面了解更多：

- [Verify access token validity](https://developers.line.biz/en/reference/line-login/#verify-access-token)
- [Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile)
