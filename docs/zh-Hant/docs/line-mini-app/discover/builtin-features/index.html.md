# 內建功能（Built-in features）

LINE MINI App 內建了以下功能：

<!-- table of contents -->

## Action button 

預設情況下，動作按鈕（action button）會顯示在 LINE MINI App 每個頁面都提供的共用[頁首（header）](https://developers.line.biz/en/docs/line-mini-app/discover/ui-components/#header)上。

![](https://developers.line.biz/media/line-mini-app/discover/mini-header-action-button-en.png)

當你點按動作按鈕時，會依你的 LINE app 版本顯示如下功能。動作按鈕的圖示會因你的 LINE 版本而有所不同。

| LINE app 版本                              | 可用功能          |
| ----------------------------------------- | ----------------- |
| 26.7.0 或更新版本                          | 下拉式選單        |
| 15.12.0 或更新版本，且早於 26.7.0          | 多分頁檢視        |
| 早於 15.12.0                               | 選項              |

<!-- tip start -->

**Tip**

- 你可以實作[自訂動作按鈕（custom action button）](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#custom-action-button)，並以你選擇的格式放置在任何你想要的位置。
- 我們正在開發新功能，例如不需關閉 LINE MINI App 就能在多個聊天室之間來回切換的能力。
- 你無法在 LINE MINI App 上隱藏動作按鈕。此外，無法為加入 LINE MINI App 頻道（channel）的 LIFF app 設定 **Module mode**。

<!-- tip end -->

### Dropdown menu 

在 LINE 26.7.0 或更新版本中，點按動作按鈕會顯示以下下拉式選單。

![](https://developers.line.biz/media/line-mini-app/discover/mini-header-action-button-tap-en.png)

| 項目 | 說明 |
| --- | --- |
| **All tabs** | 顯示[多分頁檢視（multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)。 |
| **Refresh** | 重新整理畫面上目前的頁面。 |
| **Minimize browser** | 將 LIFF 瀏覽器最小化。此功能僅能用於已驗證的 MINI App。詳情請參閱 LIFF 文件中的[最小化 LIFF 瀏覽器（Minimizing LIFF browser）](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/)。 |
| **Share** | 以 LINE 訊息形式分享目前頁面的 LIFF URL 或永久連結。如果目前頁面不是以 LINE MINI App 的端點（endpoint）URL 開頭，則會改為分享 LINE MINI App 的 LIFF URL。分享訊息包含以下元素：<ul><li>URL：目前頁面的永久連結。</li><li>標題：在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Web app settings** 分頁中 **LIFF app name** 所輸入的 LIFF app 名稱。</li><li>說明：自動設定的文字</li><li>圖片：在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Channel Basic settings** 分頁中登錄為 **Channel icon** 的圖片</li></ul> |
| **Add to Home** | 會顯示加入目前頁面捷徑的「Add Shortcut」畫面。如果目前頁面不是以 LINE MINI App 的端點 URL 開頭，將會發生錯誤。適用於 LINE 14.3.0 或更新版本中的已驗證 MINI App。詳情請參閱[將 LINE MINI App 的捷徑加入使用者裝置的主畫面](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)。 |
| **Favorites** | <p>將目前的 LINE MINI App 加入使用者的我的最愛。此功能僅在滿足以下所有條件時才能使用：</p><p><ul><li>該 LINE MINI App 為[已驗證的 MINI App（verified MINI App）](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#verified-mini-app)。</li><li>使用者位於日本。</li><li>使用者的 LINE 版本為 15.18.0 或更新版本。</li></ul></p><p>已加入使用者我的最愛的 LINE MINI App 可在 LINE app 的 MINI 分頁中檢視。</p> |
| **Permission settings** | <p>開啟權限設定畫面。權限設定畫面可讓使用者檢視並變更目前開啟的 LINE MINI App 的相機與麥克風權限。適用於 LINE 14.6.0 或更新版本。</p><p>如果使用者變更了權限，除非在 LINE MINI App 上重新載入頁面，否則變更可能不會反映。</p> |
| **About the service** | 顯示[供應商頁面（Provider page）](https://developers.line.biz/en/docs/partner-docs/provider-page/)。此功能僅能用於已驗證的 MINI App。 |
| **Report** | <p>在外部瀏覽器中開啟 LINE app 詢問表單。此功能僅在滿足以下所有條件時才能使用：</p><ul><li>LINE MINI App 頻道的 **Basic settings** 分頁中的 **Region to provide the service** 設定為「Japan」。</li><li>使用者的 LINE 版本為 15.6.0 或更新版本。</li></ul> |

<!-- note start -->

**Note**

若要分享目前頁面，使用者需要在正式支援 LINE MINI App 的 LINE 版本上點按動作按鈕。若 LINE 版本低於[支援的版本](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/#supported-platforms-and-versions)，無論正在分享的是哪個頁面，頁首中的動作按鈕都將一律導向 LINE MINI App 的首頁。

<!-- note end -->

### Multi-tab view 

多分頁檢視會顯示你最近使用的服務。最近使用的服務區段包含使用者開啟過的 LINE MINI App 與 LIFF app，依最近使用的順序顯示，最多 50 個項目。使用者可利用使用紀錄重新開啟 LINE MINI App 與 LIFF app。

詳情請參閱 LIFF 文件中的[多分頁檢視（Multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)。

![](https://developers.line.biz/media/line-mini-app/discover/mini-multi-tab-view-en.png)

## Channel consent simplification 

LIFF app 若要取得使用者資訊或傳送訊息給使用者，使用者必須在首次存取該 LIFF app 時於頻道同意畫面上同意對應的權限。

在 LINE MINI App 中，透過「Channel consent simplification」（頻道同意簡化）功能，使用者只需同意簡化一次。在那之後，當使用者首次存取另一個 LINE MINI App 時，將會跳過頻道同意畫面，讓他們可以立即開始使用該 LINE MINI App。

詳情請參閱 [LINE MINI App 授權流程](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/)。
