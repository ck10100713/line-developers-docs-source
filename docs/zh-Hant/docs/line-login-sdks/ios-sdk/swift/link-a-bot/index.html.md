# 使用 SDK 啟用加入好友選項（Enabling the add friend option with the SDK）

當使用者登入您的應用程式時，您可以顯示將 LINE 官方帳號加入為好友的選項。這稱為**加入好友選項（add friend option）**。開發者可以指定要被加入為好友的 LINE 官方帳號。

在開始進行設定之前，請參閱 LINE Login 文件中的[登入時將 LINE 官方帳號加入為好友（加入好友選項）](https://developers.line.biz/en/docs/line-login/link-a-bot/)，以了解加入好友選項以及以下細節：

- 在 LINE Developers Console 上將 LINE 官方帳號與您的頻道（channel）連結
- 傳送至 LINE Platform 的 bot prompt 參數及其行為
- 從 LINE Platform 回傳的好友關係狀態旗標及其意義

本主題說明如何透過 LINE SDK 啟用這些與加入好友選項相關的功能：

- [在登入請求中設定 bot prompt 參數](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/link-a-bot/#bot_prompt)
- [檢查使用者與 LINE 官方帳號之間的好友關係狀態](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/link-a-bot/#get_friendship)

## Setting the bot prompt parameter in the login request 

以下範例程式碼示範如何在登入請求中將 `.botPromptNormal` 或 `.botPromptAggressive` 設定為 bot prompt 參數：

```swift
// Includes an option to add a LINE Official Account as a friend in the consent screen.
var parameters = LoginManager.Parameters()
parameters.botPromptStyle = .normal
LoginManager.shared.login(permissions: [.profile], parameters: parameters) {
    // ...
}

// Opens a new screen to add the LINE Official Account as a friend after the user agrees to the permissions in the consent screen.
parameters.botPromptStyle = .aggressive
LoginManager.shared.login(permissions: [.profile], parameters: parameters) {
    // ...
}
```

如需更多關於參數值的資訊，請參閱 LINE SDK for iOS Swift reference 中的 [LoginManager.Parameters](https://developers.line.biz/en/reference/ios-sdk-swift/Classes/LoginManager/Parameters.html) 與 [LoginManager.BotPrompt](https://developers.line.biz/en/reference/ios-sdk-swift/Classes/LoginManager/BotPrompt.html)。

## Checking the friendship status between the user and the LINE Official Account 

您可以使用以下方法檢查使用者與 LINE 官方帳號之間的好友關係狀態。

- [檢查登入回應中的 `friendshipStatusChanged` 屬性](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/link-a-bot/#use-friendship_status_changed)：此方法會檢查登入期間好友關係狀態是否已變更。
- [使用 LINE Login 取得好友關係狀態](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/link-a-bot/#use-line-login-api)：此方法會取得使用者與 LINE 官方帳號之間的好友關係狀態。

### Check the `friendshipStatusChanged` property in the login response 

成功登入後，`LoginResult` 物件的 `friendshipStatusChanged` 屬性會包含一個布林值，用以表示好友關係狀態是否已變更。

必須符合以下條件才能取得好友關係狀態旗標：

- 在登入請求中指定了 bot prompt 選項。
- 向使用者顯示了包含將您的 LINE 官方帳號加入為好友選項的同意畫面。

以下範例程式碼示範如何取得 `friendshipStatusChanged` 屬性。

```swift
var parameters = LoginManager.Parameters()
parameters.botPromptStyle = .normal
LoginManager.shared.login(permissions: [.profile], parameters: parameters) {
    result in
    switch result {
    case .success(let value):
        print(value.friendshipStatusChanged)
    case .failure(let error):
        print(error)
    }
}
```

如需更多關於 `friendshipStatusChanged` 屬性的資訊，請參閱 LINE SDK for iOS Swift reference 中的 [friendshipStatusChanged](https://developers.line.biz/en/reference/ios-sdk-swift/Structs/LoginResult.html#/s:7LineSDK11LoginResultV23friendshipStatusChangedSbSgvp)。

### Use LINE Login to get friendship status 

在使用者登入您的應用程式且已回傳存取權杖（access token）後，呼叫 `getBotFriendshipStatus` 方法。

```swift
API.getBotFriendshipStatus { result in
    switch result {
    case .success(let value): print(value.friendFlag)
    case .failure(let error): print(error)
    }
}
```

如需更多關於回傳值的資訊，請參閱 LINE SDK for iOS Swift reference 中的 [getBotFriendshipStatus](https://developers.line.biz/en/reference/ios-sdk-swift/Enums/API.html#/s:7LineSDK3APIO22getBotFriendshipStatus13callbackQueue17completionHandleryAA08CallbackI0O_ys6ResultOyAA03GetefG7RequestV8ResponseVAA0A8SDKErrorOGctFZ)。
