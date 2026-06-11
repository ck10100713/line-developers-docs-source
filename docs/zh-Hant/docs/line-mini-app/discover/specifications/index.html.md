# LINE MINI App 規格（LINE MINI App specifications）

本頁說明開發 LINE MINI App 的相關規格。

<!-- table of contents -->

## HTML5 Support 

開發 LINE MINI App 時，您幾乎可以使用任何 [HTML5](https://html.spec.whatwg.org/) 規格。例如，您可以使用 [Geolocation API](https://www.w3.org/TR/geolocation/) 來取得使用者的位置資訊，並為使用者提供鄰近店家的資訊。大多數與 HTML5 相容的地圖 API 都可以使用，包括 Google Maps API。

![](https://developers.line.biz/media/line-mini-app/mini_map_api.png)

### Support Media Formats 

LINE MINI App 也支援 HTML5 所支援的媒體格式。請參閱以下 HTML5 規格：

- [img element](https://html.spec.whatwg.org/multipage/embedded-content.html#the-img-element)
- [Media element](https://html.spec.whatwg.org/multipage/media.html)

### HTML5 Support in the browser 

以下網站可協助您了解外部瀏覽器對 HTML5 的支援情況：

- [https://caniuse.com](https://caniuse.com/)

## Supported Platforms and Versions 

LINE MINI App 是使用 [LIFF](https://developers.line.biz/en/docs/liff/overview/) 開發的。因此，LINE MINI App 支援的 OS 版本與 LINE 版本，是以 LIFF 的[建議運作環境](https://developers.line.biz/en/docs/liff/overview/#operating-environment)為基準。

<!-- note start -->

**Note**

支援的版本可能會在未事先通知的情況下變更。

<!-- note end -->

### Opening LINE MINI App in an external browser 

<!-- tip start -->

**自 2025 年 10 月起，LINE MINI App 可在外部瀏覽器中使用**

使用者在外部瀏覽器中開啟 LINE MINI App 時所顯示的畫面已變更。詳情請參閱 2025 年 9 月 26 日的最新消息：[2025 年 10 月 1 日起，所有 LINE MINI App 使用者均可在網頁瀏覽器中使用服務](https://developers.line.biz/en/news/2025/09/26/mini-app-browser/)。

<!-- tip end -->

當未使用 LINE 的使用者，或在[深層連結（deep links）](https://en.wikipedia.org/wiki/Mobile_deep_linking)無法運作情況下的 LINE 使用者，在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟 LINE MINI App 時，會顯示如下圖所示的頁面，並引導使用者使用 LINE 的智慧型手機 App（[LIFF 瀏覽器（LIFF browser）](https://developers.line.biz/en/glossary/#liff-browser)）開啟 LINE MINI App。在該頁面上點選 [**Open in web browser**]，會在網頁瀏覽器中顯示 LIFF 端點 URL 頁面。

![](https://developers.line.biz/media/line-mini-app/landing-page-en.png)

## Supported LIFF Versions 

LINE MINI App 是使用 [LIFF](https://developers.line.biz/en/docs/liff/overview/) 開發的。LINE MINI App 可使用的 LIFF SDK 最低版本為 v2.1。

LINE MINI App 允許使用 LIFF v2.1.x 所提供的所有 LIFF API。
