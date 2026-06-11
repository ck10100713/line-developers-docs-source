# 使用 universal link

你可以運用 Apple 的 [universal links](https://developer.apple.com/library/archive/documentation/General/Conceptual/AppSearch/UniversalLinks.html) 功能來提升 app 的安全性，該功能可在 app 之間安全地傳遞資訊。若你設定了 universal link，LINE 會優先嘗試以 universal link 開啟你的 app。如果 universal link 無效，LINE 會退而改用以你的 iOS bundle ID 為基礎的 URL（請參閱[將你的 app 連結至頻道](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/#linking-app-to-channel)）。

<!-- note start -->

**建議使用 universal link**

雖然 universal link 並非必要，但我們建議使用，以使你的 app 更安全。

<!-- note end -->

若要讓使用者能以 universal link 開啟你的 app，請依照下列步驟操作：

1. [在你的 app 與伺服器之間建立關聯。](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/universal-links-support/#ul-s1)
1. [在 LINE Developers Console 上設定 universal link。](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/universal-links-support/#ul-s2)
1. [以 universal link 呼叫 `LoginManager.setup` 方法。](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/universal-links-support/#ul-s3)
1. [在你的 app 被 universal link 開啟後處理登入結果。](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/universal-links-support/#ul-s4)

## 1. Create an association between your app and your server 

關於此步驟，請參閱 Apple 的 [Allowing Apps and Websites to Link to Your Content](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content)。

請完成以下作業：

- 建立一個 `apple-app-site-association` 檔案，其中包含關於你的 app 可處理之 URL 的 JSON 資料，並將其放置於你的 HTTPS 伺服器上。
- 為你的 app 新增 Associated Domains entitlement。

本節假設你使用 `https://yourdomain.com/line-auth/` 作為處理 LINE 授權回應的 universal link。

請在 `apple-app-site-association` 檔案的 `paths` 欄位中加入 `/line-auth/*`。一個有效的 Apple App Site Association 檔案範例如下：

```json
{
    "applinks": {
        "apps": [],
        "details": [
            {
                "appID": "YOUR_TEAM_ID.com.yourcompany.yourapp",
                "paths": [ "/line-auth/*" ]
            }
        ]
    }
}
```

請注意，你只能在實體 iOS 裝置上測試 universal link。你需要正確設定你的 app ID 與描述檔（profile）。如果你的 universal link 無法運作，請參閱 Apple 開發者網站上的 [Troubleshooting Universal Links](https://developer.apple.com/library/archive/qa/qa1916/_index.html)。在繼續進行後續步驟之前，請先確保你的 universal link 能正常運作。

## 2. Set up a universal link on the LINE Developers Console 

關於操作程序，請參閱[將你的 app 連結至頻道](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/#linking-app-to-channel)。在此範例中，我們將其設定為 `https://yourdomain.com/line-auth/`。

## 3. Call the `LoginManager.setup` method with the universal link 

當你呼叫 `LoginManager.setup` 方法時，請將 universal link 傳遞給 LINE SDK for iOS Swift。這可讓 LINE Login 驗證該連結是否已在 LINE Developers Console 與你的 app 上都正確設定，以防止 universal link 遭到濫用。在下方範例中，universal link 為 `https://yourdomain.com/line-auth/`。

```swift
let link = URL(string: "https://yourdomain.com/line-auth/")
LoginManager.shared.setup(channelID: "YOUR_CHANNEL_ID", universalLinkURL: link)
```

關於呼叫 `LoginManager.setup` 方法的更多資訊，請參閱[將 LINE Login 整合至你的 iOS app](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/integrate-line-login/)。

## 4. Handle the login result after your app is opened by the universal link 

若要處理從 LINE Platform 回傳的驗證結果，請將收到的 URL 傳遞給 `LoginManager` 的 `application(_:open:options:)` 方法。這代表你需要修改你的 app delegate 類別或 scene delegate 類別，取決於你的專案是否支援多視窗（這是 [iOS 13 推出的功能](https://developer.apple.com/documentation/uikit/scenes)）。

### Modify app delegate 

iOS 12 及更早版本會藉由呼叫你的 `UIApplicationDelegate` 物件來開啟 URL。如果你的 app delegate 類別包含 `application(_:continue:restorationHandler:)` delegate 方法，請在其中加入以下幾行程式碼。如果不存在，請先建立它，再加入這些程式碼：

```swift
func application(
    _ app: UIApplication,
    continue userActivity: NSUserActivity,
    restorationHandler: @escaping ([UIUserActivityRestoring]?) -> Void) -> Bool
{
    if LoginManager.shared.application(app, open: userActivity.webpageURL) {
        return true
    }
    // Your other code to handle universal links and/or user activities.
}
```

### Modify scene delegates 

預設情況下，iOS 13 或更新版本會嘗試藉由呼叫 `UISceneDelegate` 物件來開啟 URL。

如果你以 Xcode 11 或更新版本建立專案，預設情況下它會包含一個 `SceneDelegate.swift` 檔案，且你的 `Info.plist` 檔案會包含一個 `UIApplicationSceneManifest` 項目。

如果你的 app 支援多視窗，請將以下幾行程式碼加入你想使用的任何 scene delegate 類別中：

```swift
// SceneDelegate.swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
    _ = LoginManager.shared.application(.shared, open: URLContexts.first?.url)
}
```

<!-- note start -->

**如果你不支援多視窗**

如果你的 app 不支援多視窗，iOS 會呼叫你的 `UIApplicationDelegate` 物件來開啟 URL。請改為修改你的 app delegate 類別。

<!-- note end -->

現在 LINE 可以使用 universal link 開啟你的 app，且你的 app 能夠處理登入結果。
