# 試用範例 app（Trying the starter app）

iOS 版的 LINE Login 範例 app 可讓你快速了解 [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) 在 iOS app 上的運作方式。

## Prerequisites 

若要建置並執行範例 app，你需要：

- Xcode 14.1 或更新版本。

## Trying the starter app with the predefined sample channel 

若要使用我們的範例頻道（channel）試用範例 app，請依照以下步驟操作。

1. 複製（clone）[LINE SDK for iOS Swift open-source repository](https://github.com/line/line-sdk-ios-swift)。

    ```sh
    $ git clone https://github.com/line/line-sdk-ios-swift.git
    ```

1. 開啟 `LineSDK.xcworkspace` 檔案。
1. 建置 `LineSDKSample` 專案。範例 app 會在模擬器（Simulator）中啟動。

### Trying the starter app with your own channel 

你也可以將範例 app 連結到自己的頻道。如果你還沒有頻道，可以在 LINE Developers Console 中[建立一個](https://developers.line.biz/console/register/line-login/channel/)。這也需要選擇或建立一個[服務提供者（provider）](https://developers.line.biz/en/glossary/#provider)。

建立頻道後，請在專案中進行以下變更，將範例 app 連結到該頻道：

- 在 LINE Developers Console 中，依照[將你的 app 連結到頻道](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/setting-up-project/#linking-app-to-channel)的說明設定你的頻道。
- 將 app bundle ID 修改為你的頻道中所設定的 ID。
- 在 `Config.xcconfig` 檔案中，將 `LINE_CHANNEL_ID` 的值改為你的頻道 ID。

## Running the starter app 

使用 iOS 裝置或模擬器執行範例 app。首次登入時，你必須同意讓 app 存取你的個人檔案資訊。

點選 **Log in with LINE** 按鈕，即可使用 app 對 app 登入（app-to-app login）方式登入。

如果裝置上已安裝 LINE 且你已登入，你就能自動登入範例 app，無須輸入 LINE 帳號憑證。否則，系統會要求你透過裝置的瀏覽器登入。在這種情況下，你需要輸入 LINE 帳號憑證。

### Trying out the features available on the LINE SDK 

登入 app 後，你可以點選選單項目來試用以下 LINE SDK 的功能。

以下功能適用於一般使用者。

- 將使用者登出
- 取得使用者個人檔案
- 驗證存取權杖（access token）
- 取得與頻道連結的 LINE 官方帳號與使用者之間的好友狀態（friendship status）

畫面中的其他功能僅供特定使用者使用。
