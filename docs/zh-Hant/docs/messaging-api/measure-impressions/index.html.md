# 評估曝光數（Measure impressions）

在 Messaging API 中，統計資料涵蓋了各種使用者行為的資訊。本頁將聚焦於其中的曝光數（impression）。

- [Aggregation environment](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#environment-for-aggregation)
- [Endpoints for obtaining statistics](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#endpoints-for-statistics)
- [What is an impression?](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#what-is-impression)
- [Impression measurement logic](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#impression-logic)
- [Usage precautions](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#precautions)

## Aggregation environment 

包含曝光數在內的統計資料，是以 iOS 與 Android 版的 LINE app 為基準進行彙整。

在 PC 版或 Chrome 版 LINE 上瀏覽的訊息，不會計入統計資料。

## Endpoints for obtaining statistics 

你可以使用以下端點（endpoint）來取得使用者如何與你所傳送訊息互動的統計資料：

- [Get user interaction statistics](https://developers.line.biz/en/reference/messaging-api/#get-message-event)
- [Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit)

## What is an impression? 

在 Messaging API 中，曝光數（impression）指的是使用者進入聊天室並瀏覽由 LINE 官方帳號（LINE Official Account）所傳送的訊息。曝光有時也會被稱為訊息開啟（message opens）。

### Impression types 

曝光分為兩種類型：不重複曝光數（unique impression）與曝光數（impression）。本文件中所述的[曝光評估邏輯](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#impression-logic)同時適用於這兩種類型。不過請注意，兩者的計算次數有所不同。

透過[取得統計資料的端點](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#endpoints-for-statistics)可取得的曝光數如下：

| Property | 曝光類型 | 說明 |
| --- | --- | --- |
| `overview.uniqueImpression` \*1 | 不重複曝光數 | 開啟該訊息的使用者人數。顯示至少一則 bubble 的人數。<br>每則訊息對每位使用者只計算一次。 |
| `messages[].uniqueImpression` \*2 | 不重複曝光數 | 顯示該 bubble 的使用者人數。<br>每則 bubble 對每位使用者只計算一次。 |
| `messages[].impression` \*1 | 曝光數 | 該 bubble 被顯示的次數。<br>若符合條件，每則 bubble 對每位使用者可能會被計算多次。 |

\*1 [Get user interaction statistics](https://developers.line.biz/en/reference/messaging-api/#get-message-event) 與 [Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit) 端點回應中包含曝光數值的屬性。

\*2 [Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit) 端點回應中包含曝光數值的屬性。

#### Message and bubble concept 

一則[訊息（message）](https://developers.line.biz/en/docs/messaging-api/sending-messages/)由一個或多個[訊息物件（message object）](https://developers.line.biz/en/reference/messaging-api/#message-objects)組成。你可以在單一請求中傳送最多五個訊息物件。

在 Messaging API 中，bubble 指的是單一個訊息物件。訊息物件包含貼圖訊息物件、圖片訊息物件等多種類型。它們在視覺上是否呈現為對話泡泡的形狀並不重要。

下圖示範了一則由三個 bubble 組成的訊息範例。雖然 bubble 2 與 bubble 3 在外觀上與 bubble 1 的文字訊息物件並不具有相同的對話泡泡形狀，但在曝光評估中，每一個都會被視為 bubble。

![](https://developers.line.biz/media/messaging-api/measure-impressions/message-and-bubbles-en.png)

當這則訊息被傳送，且使用者開啟聊天室進行瀏覽時，所顯示的單一 bubble 會觸發 `overview.uniqueImpression` 的計算。`messages[].uniqueImpression` 與 `messages[].impression` 則會針對每一個 bubble 分別計算。

詳情請參閱 Messaging API 參考資料中的 [Get user interaction statistics](https://developers.line.biz/en/reference/messaging-api/#get-message-event) 與 [Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit)。

### Actions that aren't counted as impressions 

只有當使用者進入聊天室並瀏覽由 LINE 官方帳號所傳送的訊息時，才會計算曝光數。

不過，若使用者執行下列其中一種能在不進入聊天室的情況下將訊息標示為已讀的操作，則不會計入曝光數。

| OS | 操作 |
| --- | --- |
| Android | <ul><li>在聊天清單中長按你想標示為已讀的聊天室，然後從出現的選單中選擇 <b>標示為已讀</b>，即可批次將它們標示為已讀。</li><li>從聊天清單頂端的選項選單中選擇 <b>全部標示為已讀</b>，即可將所有聊天室標示為已讀。</li></ul> |
| iOS | <ul><li>在聊天清單中向左滑動某個聊天，並從選單中選擇 <b>已讀</b>，即可批次將其標示為已讀。</li><li>點按漢堡選單，開啟聊天清單編輯畫面，選取多個聊天，然後點按 <b>已讀</b>，即可一次將多個聊天標示為已讀。</li></ul> |

## Impression measurement logic 

本節說明曝光數的具體評估邏輯。

- [Display message bubbles at 100%](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#must-show-all-messages)
- [Duplicate counting doesn't occur when scrolling](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#no-duplicate-by-scrolling)
- [About carousel messages](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#carousel-message)

### Display message bubbles at 100% 

當使用者進入聊天室並瀏覽由 LINE 官方帳號所傳送的訊息時，會計算曝光數。此時，訊息的 bubble 必須在畫面上 100% 可見。

以下是 100% 可見與非 100% 可見的 bubble 範例。

| 說明 | 圖片 |
| --- | --- |
| 此區域的 bubble 為 100% 可見。 | ![green](https://developers.line.biz/media/messaging-api/measure-impressions/100per-area.png) |
| 此區域的 bubble 並非 100% 可見。 | ![red](https://developers.line.biz/media/messaging-api/measure-impressions/not-100per-area.png) |

| 顯示 | 說明 | 圖片 |
| --- | --- | --- |
| ✅️ 100% 可見 | 顯示在綠色區域中的 bubble 完整可見，因此會被計算為一次曝光。 | ![The entire bubble is displayed](https://developers.line.biz/media/messaging-api/measure-impressions/impression-100per.png) |
| ❌️ 非 100% 可見 | 顯示在紅色區域中的 bubble 與圖文選單（rich menu）重疊，並非完整可見，因此不會被計算為曝光。 | ![The entire bubble isn't displayed because it overlaps with the rich menu](https://developers.line.biz/media/messaging-api/measure-impressions/impression-not-100per-richmenu.png) |
| ❌️ 非 100% 可見 | 紅色區域中的 bubble 與[服務選單列（service menu bar）](https://www.lycbiz.com/jp/manual/OfficialAccountManager/servicemenubar/)重疊，並非完整可見，因此不會被計算為曝光。 | ![The entire bubble isn't displayed because it overlaps with the service menu bar](https://developers.line.biz/media/messaging-api/measure-impressions/impression-not-100per-service-menu-ber.png) |
| ❌️ 非 100% 可見 | 紅色區域中的 bubble 太高，無法完整容納於聊天視窗內，因此並非完整可見，所以不會被計算為曝光。 | ![The message is too tall to fit entirely within the bubble](https://developers.line.biz/media/messaging-api/measure-impressions/impression-not-100per-too-long.png) |

<!-- tip start -->

**當整個 bubble 無法一次顯示時的曝光計算**

「100% 顯示」指的是在使用者離開聊天室之前的某個時間點，目標 bubble 的頂端與底端邊緣都曾在使用者的視窗中可見。

即使整個 bubble 無法如前述範例般一次顯示完全，只要透過捲動或關閉圖文選單，使被遮蔽 bubble 的頂端與底端邊緣都變為可見，就會被視為 100% 顯示，並記錄該次曝光。

<!-- tip end -->

### Duplicate counting doesn't occur when scrolling 

一旦記錄了一次曝光，只要使用者停留在同一個聊天室內，即使他們捲動回去多次顯示同一則訊息，也不會再次計算。

不過，若使用者返回聊天清單後再重新進入聊天室並瀏覽 100% 的訊息，則會被計算為一次新的曝光。

不重複曝光數對每位使用者只計算一次，因此即使使用者重新進入聊天室，數值也不會增加。

### About carousel messages 

若你使用 Flex Message 傳送採用[輪播（carousel）](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#carousel)的訊息，即使使用者水平捲動以顯示輪播內容，曝光數也不會被多次計算。

對於使用輪播的訊息，當 bubble 的所有邊緣（頂端、底端、左側與右側）都被顯示時，曝光數會計算一次。

![](https://developers.line.biz/media/messaging-api/measure-impressions/carousel-100per-scroll.png)

## Usage precautions 

在評估曝光數時，請注意以下幾點：

- [Make sure that it's within the measurement period](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#ensure-measurement-period)
- [Avoid making the message too tall](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#avoid-too-tall-messages)
- [Avoid interfering with the rich menus or the service menu bar](https://developers.line.biz/en/docs/messaging-api/measure-impressions/#avoid-interference)

### Make sure that it's within the measurement period 

包含曝光數在內的統計資料，自訊息傳送起僅會收集 14 天（1,209,600 秒）。在此之後便不再更新。使用 [Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit) 端點時，由於你可以指定彙整期間，因此請務必確認所指定的日期落在評估期間之內。

### Avoid making the message too tall 

若你傳送極為冗長（過高）的訊息，整則訊息可能無法在聊天室中完整顯示，曝光數也可能無法如預期般被計算。請將訊息調整為適當的長度。

### Avoid interfering with the rich menus or the service menu bar 

若你的 LINE 官方帳號使用了[圖文選單（rich menu）](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/)，bubble 在聊天室中可能會與其重疊，導致整個 bubble 無法完整可見。因此，曝光數可能無法如預期般被計算。

此外，若你使用顯示於聊天室頂端的[服務選單列（service menu bar）](https://www.lycbiz.com/jp/manual/OfficialAccountManager/servicemenubar/)，也可能發生類似的問題。

請調整訊息的長度與圖文選單的尺寸，以避免這些問題。
