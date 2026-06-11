# LIFF 瀏覽器與外部瀏覽器的差異（The differences between the LIFF browser and external browser）

<!-- tip start -->

**LIFF 瀏覽器規格**

如需更多資訊，請參閱 [LIFF browser specifications](https://developers.line.biz/en/docs/liff/overview/#liff-browser-spec)。

<!-- tip end -->

[LIFF 瀏覽器（LIFF browser）](https://developers.line.biz/en/glossary/#liff-browser)不支援[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)所支援的部分網頁技術。LIFF 瀏覽器不支援的網頁技術包含下列項目：

| Web technology | Description |
| --- | --- |
| [theme-color Meta Tag](https://caniuse.com/meta-theme-color) | 用來指定使用者介面顏色的功能 |
| [Download attribute](https://caniuse.com/download) | 讓超連結用於下載資源（而非導覽至該資源）的功能 |
| [Add to home screen (A2HS)](https://caniuse.com/sr_web-app-manifest) | <p>讓使用者可將網頁應用程式新增至自己裝置主畫面的功能。</p><p>在 LINE MINI App 中，可透過[multi-tab view](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#multi-tab-view)中的 **Add to Home**，或使用 [`liff.createShortcutOnHomeScreen()`](https://developers.line.biz/en/reference/liff/#create-shortcut-on-home-screen) 方法，將 LINE MINI App 的捷徑新增至使用者裝置的主畫面。如需更多資訊，請參閱 LINE MINI App 文件中的 [Add a shortcut to your LINE MINI App to the home screen of the user's device](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)。</p> |
| [Service Workers](https://caniuse.com/serviceworkers) | 讓網頁應用程式可支援離線運作、背景同步、推播通知等的功能 |

上述列出的網頁技術，未來可能會由 LIFF 瀏覽器支援。

至於 LIFF 瀏覽器是否支援上述以外的網頁技術，則依照 [WKWebView](https://developer.apple.com/documentation/webkit/wkwebview) 與 [Android WebView](https://developer.android.com/reference/android/webkit/WebView) 的規格而定。如需更多資訊，請參閱 [Can I use...](https://caniuse.com/)。
