# LIFF browser 與 LINE 應用程式內建瀏覽器的差異（The differences between LIFF browser and LINE's in-app browser）

當你在 LINE 應用程式中開啟 LIFF app 時，LIFF app 會在 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 或 [LINE's in-app browser](https://developers.line.biz/en/glossary/#line-iab)（LINE 應用程式內建瀏覽器）中開啟。LIFF browser 與 LINE's in-app browser 是不同的瀏覽器，部分 LIFF app 功能僅在 LIFF browser 中可用。

本頁說明如何辨識瀏覽器是 LIFF browser 還是 LINE's in-app browser，以及兩者在可用功能上的差異。

<!-- table of contents -->

## LIFF browser 

專為 LIFF app 設計的瀏覽器。當你以下列方式開啟 LIFF app 時，LIFF app 會在 LIFF browser 中開啟：

- 在 LINE 應用程式的聊天室中點選 [LIFF URL](https://developers.line.biz/en/glossary/#liff-url)。
- 在外部瀏覽器中點選 LIFF URL。

## LINE's in-app browser 

專為在 LINE 應用程式內使用而設計的瀏覽器。當你以下列方式開啟 LIFF app 時，LIFF app 會在 LINE's in-app browser 中開啟：

- 在 LINE 應用程式的聊天室中點選 LIFF app 的端點（endpoint）URL。

請注意，在 LIFF 中，LINE's in-app browser 會被視為一種外部瀏覽器。例如，若你在 LINE's in-app browser 中執行 [`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) 方法，回傳值中 `type` 屬性的值會是 `external`（外部瀏覽器）。

## Identify whether a browser is the LIFF browser or LINE's in-app browser 

有兩種方法可辨識執行 LIFF app 的瀏覽器是 LIFF browser 還是 LINE's in-app browser：

- [從使用者介面辨識](https://developers.line.biz/en/docs/liff/differences-between-liff-browser-and-line-in-app-browser/#identify-from-ui)
- [使用 `liff.isInClient()` 方法辨識](https://developers.line.biz/en/docs/liff/differences-between-liff-browser-and-line-in-app-browser/#identify-using-liff-is-in-client)

### Identify from the user interface 

LIFF browser 與 LINE's in-app browser 的頁首（header）與頁尾（footer）介面不同。因此，你可以透過檢查開啟 LIFF app 的瀏覽器使用者介面，來辨識該瀏覽器是 LIFF browser 還是 LINE's in-app browser。

| LIFF browser | LINE's in-app browser |
| --- | --- |
| ![](https://developers.line.biz/media/liff/differences-between-liff-browser-and-line-in-app-browser/liff-browser.png)<ul><li>頁首<ul><li>最小化按鈕<b>不存在</b></li><li>動作按鈕<b>存在</b>（\*）</li></ul></li><li>頁尾<b>不存在</b></li></ul> | ![](https://developers.line.biz/media/liff/differences-between-liff-browser-and-line-in-app-browser/line-in-app-browser.png)<ul><li>頁首<ul><li>最小化按鈕<b>存在</b></li><li>動作按鈕<b>不存在</b></li></ul></li><li>頁尾<b>存在</b></li></ul> |

\* 動作按鈕不會在模組模式（module mode）中顯示。詳情請參閱[將 LIFF app 新增至你的頻道](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)。

### Identify using the `liff.isInClient()` method 

你可以使用 `liff.isInClient()` 方法辨識瀏覽器是否為 LIFF browser。詳情請參閱 LIFF API 參考文件中的 [liff.isInClient()](https://developers.line.biz/en/reference/liff/#is-in-client)。

## The differences in features available between the LIFF browser and LINE's in-app browser 

LIFF browser 與 LINE's in-app browser 之間可用功能的差異如下：

| Feature | LIFF browser | LINE's in-app browser |
| --- | --- | --- |
| 指定[檢視畫面大小（view size）](https://developers.line.biz/en/docs/liff/overview/#screen-size) | ✅ | ❌ |
| [動作按鈕（Action button）](https://developers.line.biz/en/docs/liff/overview/#action-button) | ✅ | ❌ |
| [多分頁檢視（Multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view) | ✅ | ❌ |
| [2D code 讀取器（2D code reader）](https://developers.line.biz/en/docs/liff/developing-liff-apps/#opening-two-dimensional-code-reader) | ✅ | ❌ |
| [傳送訊息至聊天室](https://developers.line.biz/en/docs/liff/developing-liff-apps/#sending-messages) | ✅ | ❌ |
| [Share target picker](https://developers.line.biz/en/docs/liff/developing-liff-apps/#share-target-picker) | ✅ | ❌ |
| [導向非 LIFF app 的外部網站時顯示彈出視窗](https://developers.line.biz/en/docs/liff/developing-liff-apps/#transition-to-external-site) | ✅ | ❌ |
| [LIFF-to-LIFF 轉換](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff) | ✅ | ❌ |

✅：可用<br>❌：不可用
