# 將 LINE MINI App 的捷徑加到使用者裝置的主畫面

<!-- tip start -->

**此功能僅適用於已驗證的 MINI App**

此功能僅適用於已驗證的 MINI App。對於未驗證的 MINI App，你可以在 Developing 用的內部頻道上測試此功能，但無法在 Published 用的內部頻道上使用此功能。

<!-- tip end -->

使用者可以將你的 LINE MINI App 捷徑加到使用者裝置的主畫面。

從[動作按鈕（action button）](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)開啟下拉式選單後點選 **Add to Home** 選項，或使用 [`liff.createShortcutOnHomeScreen()`](https://developers.line.biz/en/reference/liff/#create-shortcut-on-home-screen) 方法，即會顯示新增捷徑畫面。使用者可依照畫面上的指示，將你的 LINE MINI App 捷徑加到使用者裝置的主畫面。這讓使用者能直接從裝置的主畫面存取你的 LINE MINI App。

**在 Android 裝置上的顯示**

<!-- note start -->

**在某些 Android 裝置上，現有的捷徑可能會被移除**

在某些 Android 裝置上，如果使用者從 LINE 應用程式的**設定** > **應用程式圖示**變更圖示，現有的捷徑可能會被移除。詳情請參閱 LINE 服務中心的 [\[Android\] 變更 LINE 應用程式圖示後，LINE 捷徑出現問題時的處理方式](https://help.line.me/line/smartphone/pc?lang=ja&contentId=200000315)（僅提供日文）。

<!-- note end -->

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-android-en.png)
![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/shortcut-android.png)

**在 iOS 裝置上的顯示**

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-ios-en.png)
![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/shortcut-ios-en.png)

針對使用者經常使用的服務（例如會員卡與行動點餐）運用此功能，可以提升使用者體驗。

## Operating conditions 

如果使用者裝置的作業系統為 iOS，**Add to Home** 與 `liff.createShortcutOnHomeScreen()` 方法可運作的條件如下。如果在不支援運作的環境中點選 **Add to Home** 或執行 `liff.createShortcutOnHomeScreen()` 方法，將會顯示錯誤頁面。

| 預設瀏覽器 | iOS 版本 | 是否可運作 |
| --- | --- | --- |
| Safari | 所有版本 | 可運作 |
| Chrome | 16.4 或更新版本 | 可運作 |
| Safari 與 Chrome 以外的瀏覽器 | 16.4 或更新版本 | 不保證可運作 |
| Safari 以外的瀏覽器 | 早於 16.4 | 無法運作 |

例如，如果你在早於 iOS 16.4 的 Chrome 上執行 `liff.createShortcutOnHomeScreen()` 方法，將會顯示以下錯誤頁面：

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-ios-error-en.png)
