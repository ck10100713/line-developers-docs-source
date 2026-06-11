# 將 LINE Login 整合到你的 Unity 遊戲中

在你[設定好專案](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/project-setup/)後，你就可以開始將 LINE SDK for Unity 匯入到你既有的 Unity 遊戲中，並運用 LINE Login 來改善你的應用程式使用者體驗。

## Getting the SDK 

### Download from GitHub 

若要取得最新版的 LINE SDK for Unity，請從我們的 [GitHub Releases page](https://github.com/line/line-sdk-unity/releases) 下載 `.unitypackage` 檔案。

### Import into your project 

<!-- note start -->

**Note**

在你將 LINE SDK for Unity 匯入專案之前，請先備份你的專案，並／或將其儲存在版本控制系統中。

<!-- note end -->

開啟你的 Unity 專案後，雙擊下載的 `.unitypackage` 檔案。匯入套件中的所有內容，如下圖所示：

![Import Unity package](https://developers.line.biz/media/unity-sdk/importing.png)

## Add LineSDK prefab to your scene 

匯入套件後，在你的 **Project** 面板中，你會在 `Assets/LineSDK/` 底下找到一個 **LineSDK** prefab。將它拖曳到你想要加入 LINE Login 的場景的 **Hierarchy** 面板中：

![Add LineSDK prefab](https://developers.line.biz/media/unity-sdk/adding-prefab.png)

接著，點選場景中的 LineSDK GameObject，並將 **Channel ID** 欄位更新為你的 LINE Login 頻道 ID：

![Set Channel ID](https://developers.line.biz/media/unity-sdk/setting-channel-id.png)

你可以在 [LINE Developers Console](https://developers.line.biz/console/) 中找到你的 LINE Login 頻道 ID。如果你還沒有頻道，請在 LINE Developers Console 中[建立一個](https://developers.line.biz/console/register/line-login/channel/)。你還需要選擇或建立一個 [provider](https://developers.line.biz/en/glossary/#provider)。

## Update player settings 

在你繼續實作 LINE Login 或在遊戲中使用 LINE API 之前，請依照以下步驟確認你的專案 player 設定正確無誤。

### Settings for Android export 

1. 選擇 **File > Build Settings**。
1. 點選 **Player Settings**。
1. 將 **Company Name** 和 **Product Name** 設定為與 LINE Developers Console 中頻道設定（**LINE Login** 分頁）裡 **Package names** 相同的值。
1. 選擇 ![Android settings tab](https://developers.line.biz/media/unity-sdk/android-settings-tab.png) > **Other Settings**。
1. 將 **Package Name** 設定為與 LINE Developers Console 中頻道的 **LINE Login** 分頁裡 **Package names** 相同的值。
1. 將 **Minimum API Level** 至少設定為 **API level 19**。
1. 在 **Publishing Settings** 底下，啟用 **Custom Gradle Template**。

### Settings for iOS export 

1. 選擇 **File > Build Settings**。
1. 點選 **Player Settings**。
1. 選擇 ![iPhone, iPod Touch and iPad settings tab](https://developers.line.biz/media/unity-sdk/ios-settings-tab.png) > **Other Settings**。
1. 將 **Bundle Identifier** 設定為與 LINE Developers Console 中頻道的 **LINE Login** 分頁裡 **iOS bundle ID** 相同的值。
1. 將 **Target minimum iOS Version** 至少設定為 `11.0`。

如需更多關於 LINE SDK for Unity iOS 所使用的相依性管理工具的資訊，請參閱[設定你的專案](https://developers.line.biz/en/docs/line-login-sdks/unity-sdk/project-setup/)。

## Implement login with LINE 

現在，你可以在 LineSDK（GameObject）所在的場景中實作 LINE Login。例如：

```csharp
using Line.LineSDK;

public class MyController : MonoBehaviour {
    public void LoginButtonClicked() {
        var scopes = new string[] {"profile", "openid"};
        LineSDK.Instance.Login(scopes, result => {
            result.Match(
                value => {
                    Debug.Log("Login OK. User display name: " + value.UserProfile.DisplayName);
                },
                error => {
                    Debug.Log("Login failed, reason: " + error.Message);
                }
            );
        });
    }
}
```

LINE SDK for Unity 目前僅支援 iOS 和 Android。如果你在 Unity Editor 的 play 模式下執行，它一定會回傳錯誤。若要測試，你需要將場景匯出到 iOS 或 Android 裝置上。
