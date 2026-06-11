# 試用範例應用程式

Android 版 LINE Login 範例應用程式讓你快速了解 [LINE Login](https://developers.line.biz/en/docs/line-login/overview/) 在 Android 應用程式上的運作方式。

## Prerequisites 

若要建置並執行範例應用程式，你需要：

- 已安裝 [Android Studio](https://developer.android.com/studio)

## Trying the sample app 

若要使用我們的範例頻道（channel）試用範例應用程式，請依照下列步驟進行。

1. 複製（clone）[LINE SDK for Android open-source repository](https://github.com/line/line-sdk-android)。

    ```sh
    $ git clone https://github.com/line/line-sdk-android.git
    ```

1. 在 Android Studio 中開啟 LINE SDK 專案。
1. 建置專案，並使用 Android 裝置或 Android 模擬器執行應用程式。

<!-- tip start -->

**Tip**

範例應用程式已經定義了自己的範例頻道 ID，其值為 `1620019587`，你不需要再次設定。

<!-- tip end -->

## Running the sample app 

使用 Android 裝置或 Android 模擬器執行範例應用程式。當你第一次登入時，必須同意讓應用程式存取你的個人檔案資訊。

![LINE SDK Sample App Main screen](https://developers.line.biz/media/line-login/try-line-login/line-sdk-sample-app-home-screen.jpg)

### Using the "Log in with LINE" button 

點選綠色的 **Log in with LINE** 按鈕，以使用 app-to-app 登入。這是 LINE SDK 內建的登入按鈕。

如果裝置上已安裝 LINE 且你已登入，你將能自動登入範例應用程式，而不需要輸入你的 LINE 認證資訊。否則，系統會要求你使用裝置的瀏覽器登入。在這種情況下，你需要輸入你的 LINE 認證資訊。

### Using the "login" button 

如果你目前尚未登入，**login** 按鈕將可使用。
點選 **login** 按鈕，將會觸發 LINE app-to-app 登入流程。
登入方式與流程就如同 SDK 內建的登入按鈕，但它提供了一些可調整的選項，例如 `Scopes`。
你可以參考 LINE SDK 所提供的 `LineLoginApi` 類別中的 `getLoginIntent` 方法。

<!-- note start -->

**Note**

它預設使用的 Scopes 為 `PROFILE` 與 `OPENID_CONNECT`。

<!-- note end -->

### Using the "web login" button 

如果你目前尚未登入，**web login** 按鈕將可使用。
點選 **web login** 按鈕，將會由瀏覽器開啟 LINE 登入網頁。

### Using the "logout" button 

在你登入之後，**logout** 按鈕將可使用。
點選 **logout** 按鈕以將目前的使用者登出。

詳情請參閱[將使用者登出](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#logout)。

### Trying out the features available on the LINE SDK 

![LINE SDK Sample App Api List screen](https://developers.line.biz/media/line-login/try-line-login/line-sdk-sample-app-api-list-screen.jpg)

當你登入應用程式後，你可以點選 **API List Page** 按鈕來試用 LINE SDK 的下列功能。

- [取得使用者個人檔案](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#get-profile)
- [取得目前的存取權杖](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/#get-current-token)
- [重新整理存取權杖](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/#refresh-token)
- [驗證存取權杖](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-access-tokens/#verify-access-token)
- [使用 LINE Login 取得好友關係狀態](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/#use-line-login-api)

點選每個 SDK API 按鈕後，你可以從頁面上半部檢視回應內容。
