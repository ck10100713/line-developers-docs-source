# 設定你的專案（Setting up your project）

LINE SDK for Unity 提供在 iOS 或 Android 平台上使用 LINE SDK 的介面。若要在 Unity Editor 中使用 LINE SDK 並將其匯出至各平台，你的開發環境需要具備一些條件。

## Unity requirements 

- Unity 2020.3.15 或更新版本，並已安裝 iOS 與 Android 模組
- 有效的 Unity Personal、Unity Plus 或 Unity Pro 訂閱

## Installation on iOS 

若要在 iOS 上整合 LINE SDK for Unity，你需要：

- 將 iOS 13.0 或更高版本設為部署目標（deployment target）
- Xcode 14.1 或更高版本

在 iOS 上，LINE SDK for Unity 作為 LINE SDK for iOS Swift 的包裝層（wrapper）運作。當你將專案匯出至 Xcode 時，它會加入所需的函式庫。

## Installation on Android 

你必須安裝 Android SDK，因為 Unity 會使用它來將你的專案建置至 Android 平台。如果你先前已[設定 Unity 進行 Android 開發](https://docs.unity3d.com/Manual/android-sdksetup.html)，那麼你已經擁有 Android SDK。
