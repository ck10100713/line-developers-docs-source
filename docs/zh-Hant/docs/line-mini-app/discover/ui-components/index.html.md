# LINE MINI App UI 元件（LINE MINI App UI components）

LINE MINI App 頁面由（A）標頭（Header）與（B）主體（Body）組成

![](https://developers.line.biz/media/line-mini-app/mini_concept.png)

## Header 

LINE MINI App 標頭使用平台原生（platform-native）元件，並由 LINE 自動產生。

標頭由以下元件組成：

![](https://developers.line.biz/media/line-mini-app/discover/mini_uicomp_header.png)

| Number | Component | Description |
| --- | --- | --- |
| 1 | Service Name | 在 LINE MINI App 頁面的 `<title>` 中指定。會顯示其中的元素。你無法設定字型。 |
| - | Subtext | 在未經驗證（unverified）的 MINI App 中，該頁面的網域（domain）會顯示在 Service Name 下方。在已驗證（verified）的 MINI App 中，LINE MINI App 名稱與已驗證徽章（verified badge）會顯示在 Service Name 下方。 |
| 2 | Action button | 當你點擊動作按鈕（action button）時，會顯示你所使用的 LINE app 版本可用的功能。詳情請參閱 [Action button](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)。 |
| 3 | Minimize Button / Close Button | 顯示最小化按鈕（minimize button）還是關閉按鈕（close button），取決於 LINE MINI App 的類型與 LINE 版本。<table><thead><tr><th>Type of LINE MINI App</th><th>LINE version</th><th>Button displayed</th></tr></thead><tbody><tr><td rowspan="2">Verified MINI App</td><td><ul><li>LINE for iOS version 14.15.1 - 26.6.x</li><li>LINE for Android version 15.0.0 - 26.6.x</li></ul></td><td>Minimize button</td></tr><tr><td>Versions other than the above</td><td>Close button</td></tr><tr><td>Unverified MINI App</td><td>All versions</td><td>Close button</td></tr></tbody></table>點擊關閉按鈕會關閉 LINE MINI App。點擊最小化按鈕會將 LINE MINI App 最小化。如需有關最小化的詳細資訊，請參閱 LIFF 文件中的 [Minimizing LIFF browser](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/)。 |
| 4 | Return Button | 顯示上一頁。 |
| 5 | Loading Bar | 顯示目前頁面的載入狀態。 |

## Body 

主體使用 WebView。開發各項服務時，請善用 HTML5 與 LIFF。

如需有關 LINE MINI App 開發規格的詳細資訊，請參閱 [LINE MINI App specifications](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)。
