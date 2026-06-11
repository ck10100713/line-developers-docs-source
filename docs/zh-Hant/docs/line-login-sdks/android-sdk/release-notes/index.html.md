# LINE SDK for Android 版本資訊（Release notes for LINE SDK for Android）

<!-- note start -->

**5.0.0 以上版本的版本資訊已移至 GitHub 儲存庫**

LINE SDK for Android 5.0.0 以上版本的版本資訊已移至 GitHub 儲存庫。詳情請參閱 [Releases](https://github.com/line/line-sdk-android/releases)。

<!-- note end -->

2018 年 11 月 30 日

## LINE SDK 4.0.10 for Android released

LINE SDK 4.0.10 for Android 已發布。關於下載 LINE SDK 的詳情，請參閱以下說明。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了在裝置上的 LINE 失效後，以 LINE Login 進行驗證時找不到 activity 的問題。

我們將持續提供改善，讓您能更輕鬆地進行開發。

2018 年 11 月 20 日

## LINE SDK 5.0.0 for Android released

LINE SDK 5.0.0 for Android 已發布。關於安裝與使用說明，請參閱 [LINE SDK for Android guide](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/)。

#### Changes

##### LINE Login v2.1 and Social API v2.1 are supported

當使用者透過 LINE Login 登入您的應用程式時，您可以將要授予應用程式的權限設定為 scope。透過設定 scope，您可以在取得存取權杖（access token）的同時取得 ID token。這些 token 會依照您在登入請求中所設定的 scope，包含相對應的使用者資料。

您可以向登入您應用程式的使用者顯示加入您的 bot 為好友的選項。您可以透過登入回應與 Social API 取得使用者與您的 bot 之間的好友狀態。

##### Open-source SDK

從 5.0.0 版起，LINE SDK for Android 已開源。請造訪[我們的儲存庫](https://github.com/line/line-sdk-android)查看所提供的程式碼與範例。

##### Detailed reference

現在您可以存取以原始碼為基礎的詳細參考文件。詳情請參閱 [LINE SDK for Android reference](https://developers.line.biz/en/reference/android-sdk/)。

2018 年 3 月 12 日

## LINE SDK 4.0.8 for Android released

LINE SDK 4.0.8 for Android 已發布。關於下載 LINE SDK 的詳情，請參閱以下說明。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了使用者在 LINE 首次開啟之前嘗試登入時，會出現無限載入指示器的問題。

我們將持續提供改善，讓您能更輕鬆地進行開發。

2018 年 2 月 6 日

## LINE SDK 4.0.7 for Android released

LINE SDK 4.0.7 for Android 已發布。關於下載 LINE SDK 的詳情，請參閱以下說明。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了使用者以 home 鍵離開 LINE 後，在 LINE 尚未完成驗證程序前就開啟 SDK 應用程式時發生的當機問題。

我們將持續提供改善，讓您能更輕鬆地進行開發。

2017 年 9 月 29 日

## LINE SDK 4.0.6 for Android released

LINE SDK 4.0.6 for Android 已發布。關於下載 LINE SDK 的詳情，請參閱以下說明。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了當 LINE 的密碼輸入畫面顯示在螢幕上時，使用者按下返回鍵會出現無限載入指示器的問題。

我們將持續提供改善，讓您能更輕鬆地進行開發。

2017 年 6 月 2 日

## LINE SDK 4.0.5 for Android released

LINE SDK 4.0.5 for Android 已發布。關於下載 LINE SDK 的詳情，請參閱以下說明。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了使用 `appcompat` 25.0.0 以上版本時，以登入 intent 呼叫 `startActivityForActivity` 會發生執行階段錯誤的問題。

2017 年 4 月 26 日

## LINE SDK 4.0.4 for Android released

LINE SDK 4.0.4 for Android 已發布。關於下載 LINE SDK 的詳情，請參閱以下說明。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 對 SDK 的驗證邏輯做了小幅變更，以修正在 app-to-app 登入期間 `onActivityResult` 不會被執行的問題。
- 修正了 4.0.2 版中的已知問題：使用者首次以 app-to-app 登入應用程式時，`onActivityResult` 會回傳「CANCEL」結果。

2017 年 4 月 10 日

## LINE SDK 4.0.2 for Android released

LINE SDK 4.0.2 for Android 已發布。您可以從以下頁面下載 SDK。

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了在 Android 4.x 裝置上瀏覽器登入會以 INTERNAL_ERROR 失敗的問題。

已知問題：

- 在 Android 4.x 裝置上，使用者首次以 app-to-app 登入應用程式時，onActivityResult 會回傳「CANCEL」結果。不過，使用者在第二次嘗試時即可成功登入。此問題是由 LINE 的問題所造成，將在未來的更新中解決。

2016 年 10 月 14 日

## LINE SDK 3.1.21 for Android released

LINE SDK for Android 已更新至 3.1.21 版。您可以從以下頁面的 LINE SDK 封存檔下載：

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 更新以避免建置警告。

2016 年 10 月 11 日

## LINE SDK 3.1.20 for Android released

LINE SDK for Android 已更新至 3.1.20 版。您可以從以下頁面的 LINE SDK 封存檔下載：

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 更新為以 Java 1.7 建置以維持相容性。

2016 年 3 月 15 日

## LINE SDK 3.1.19 for Android version released

LINE SDK for Android 已更新至 3.1.19 版。您可以從以下頁面的 LINE SDK 封存檔下載：

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 修正了使用者再次嘗試登入時的登入錯誤問題

2016 年 3 月 9 日

## LINE SDK 3.1.18 for Android released

LINE SDK for Android 已更新至 3.1.18 版。您可以從以下頁面的 LINE SDK 封存檔下載：

- [Download LINE SDK](https://developers.line.biz/en/docs/downloads/)

變更內容：

- 新增對 64 位元架構的支援
- 在登入方法中新增 locale 屬性
- 修正了部分錯誤
