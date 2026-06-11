# 試用入門範例 App（Trying the starter app）

Unity 版的 LINE Login 入門範例 App 讓你可以快速了解 [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) 在 Unity 遊戲中的運作方式。

## Prerequisites 

在建置並執行入門範例 App 之前，請先依照[設定你的專案](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/project-setup/)指南，正確設定你的 Unity、iOS 及 Android 環境。

## Trying the starter app with the predefined sample channel 

若要使用我們的範例頻道（channel）來試用入門範例 App，請依照下列步驟操作：

1. 複製（clone）[LINE SDK for Unity 開源儲存庫](https://github.com/line/line-sdk-unity)。

    ```sh
    $ git clone https://github.com/line/line-sdk-unity.git
    ```

1. 在 Unity 中，開啟 `LINE_SDK_Unity` 資料夾內的專案。
1. 將 `Assets/LineSDK/Demo/Scenes/Main` 底下的場景建置並匯出為 iOS 或 Android。
1. 將匯出的專案／二進位檔安裝到你的裝置上。

<!-- note start -->

**Note**

你可能需要修改憑證才能將範例 App 安裝到 iOS 裝置上。如果你沒有憑證，可以前往 **Player Settings > Settings for iOS > Other Settings**，將 **Target SDK** 設為 **Simulator SDK**，然後在 iOS 模擬器上執行範例 App。

<!-- note end -->

### Trying the starter app with your own channel 

你也可以將入門範例 App 連結到你自己的頻道（channel）。如果你還沒有頻道，請[立即建立一個](https://developers.line.biz/console/register/line-login/channel/)。你還需要選擇或建立一個 [provider](https://developers.line.biz/en/glossary/#provider)。

若要將入門範例 App 連結到你的頻道，請在你的 Unity 專案中進行下列變更：

1. 選擇 **File** > **Build Settings**。
1. 點擊 **Player Settings**。
1. 選擇 ![iPhone, iPod Touch and iPad settings tab](https://developers.line.biz/media/unity-sdk/ios-settings-tab.png) > **Other Settings**，並將 **Bundle Identifier** 設為與 LINE Developers Console 中你的 LINE Login 頻道 **LINE Login** 分頁裡 **iOS bundle ID** 相同的值。

    ![Bundle Identifier](https://developers.line.biz/media/unity-sdk/bundle-identifier-settings.png)

1. 在接下來的兩個欄位中，設為與 LINE Developers Console 中你的 LINE Login 頻道 **LINE Login** 分頁裡 Android **Package Name** 相同的值。
    - **Product Name**
    - ![Android settings tab](https://developers.line.biz/media/unity-sdk/android-settings-tab.png) > **Other Settings** > **Package Name**

    ![Package Name](https://developers.line.biz/media/unity-sdk/package-name-settings.png)

1. 從主頁面中，選擇 **LineSDK** 物件。
1. 在 **Line SDK (Script)** 底下的 **Channel ID** 欄位中，輸入你的 LINE Login 頻道 ID。

    ![Channel ID](https://developers.line.biz/media/unity-sdk/channel-id-settings.png)

## Running the starter app 

使用 iOS／Android 裝置或模擬器執行入門範例 App。首次登入時，你必須同意讓 App 存取你的個人檔案資訊。

點擊 **Log in with LINE**，即可使用 app-to-app 登入。

如果裝置上已安裝 LINE 且你已登入，你就能自動登入入門範例 App，無需輸入你的 LINE 憑證。否則，系統會要求你透過瀏覽器登入。在後者的情況下，你需要輸入你的 LINE 憑證。

### Trying out the features available on the LINE SDK 

當你登入 App 後，可以點擊選單項目來試用 LINE SDK 的下列功能。

一般使用者可使用的功能：

- 登出使用者
- 取得使用者個人檔案
- 驗證存取權杖（access token）
- 取得連結至該頻道的 LINE 官方帳號與使用者之間的好友關係狀態

其他顯示的功能僅供限定使用者使用。
