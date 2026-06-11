# LINE MINI App 圖示規格與準則（LINE MINI App icon specifications and guidelines）

LINE MINI App 圖示會用於多個位置，包括頻道（channel）同意畫面、Home 分頁、LINE 訊息以及服務訊息（service message）。本頁提供建立圖示時應遵循的準則，以及如何上傳圖示影像的說明。

- [LINE MINI App 圖示的主要顯示位置](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/#main-locations)
- [準則](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/#guidelines)
- [如何上傳圖示影像](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/#how-to-upload)

## The main locations for the LINE MINI App icon 

LINE MINI App 圖示的主要顯示位置如下：

- [頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)
- [Home 分頁](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#home-tab)
- [LINE 訊息](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/#line-message)
- [服務訊息](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)

![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/channel-consent-screen-en.png)
![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/home-tab-en.png)
![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/line-message-en.png)
![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/service-messages-en.png)

## Guidelines 

以下是設計 LINE MINI App 圖示時應遵循的準則。圖示可能會顯示得很小，尤其是在行動裝置上。請設計能讓使用者在任何位置都能清楚辨識的圖示。

- [禁止事項](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/#prohibited-matters)
- [必要事項](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/#required-matters)
- [建議事項](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/#recommended-matters)

### Prohibited matters 

#### Use of the LINE MINI App logo 

請勿在你的標誌中包含下方所示的 LINE MINI App 標誌：

| Japanese | English |
| --- | --- |
| ![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/mini-icon-guideline-mini-logo-ja.png) | ![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/mini-icon-guideline-mini-logo-en.png) |

### Required matters 

#### Icon size 

圖示的背景區域（BG SIZE）應為 130x130px。

![](https://developers.line.biz/media/line-mini-app/mini_icon_background.png)

#### Logo size 

標誌的最小尺寸（LOGO SIZE）必須為 54x54px，最大尺寸必須為 90x90px。建議尺寸介於 54×54px 與 76×76px 之間。

![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/mini-icon-guideline-size-en.png)

### Recommended matters 

#### Logo design 

為了隨時維持標誌的可見性與品質，標誌應設計為獨立的圖示或文字標誌（wordmark）。

![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/mini-icon-guideline-design.png)

<!-- tip start -->

**使用 PSD 格式的範本檔案建立圖示（選用）**

我們提供可用於建立圖示的 PSD 範本檔案。使用此範本檔案可設定圖示的外框（outline）。設定外框後，當圖示放置在 LINE app 中與圖示同色的背景前方時，會更容易辨識。在建立圖示之前，請先下載以下範本檔案（PSD 格式）。

[下載範本檔案（PSD 格式）](https://vos.line-scdn.net/line-developers/docs/media/line-mini/icon_template_file.psd)

依範本檔案建立圖示時，請根據背景顏色指定外框顏色。此時，建議在範本檔案中選擇一種背景顏色類型。此外，在儲存前請隱藏範本檔案中未使用的圖層。

![](https://developers.line.biz/media/line-mini-app/mini_icon_guideline_color.png)

| Background color                  | Outline color   | Outline opacity |
| --------------------------------- | --------------- | --------------- |
| White (#FFFFFF)                   | Black (#000000) | 12%             |
| Black (#000000)<br>Dark (#181818) | White (#FFFFFF) | 8%              |
| Other color                       | Black (#000000) | 8%              |

<!-- tip end -->

## How to upload an image for the icon 

請在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Basic settings** 分頁中的 **Channel icon** 上傳圖示影像。圖示僅能使用 PNG 與 JPEG 這兩種檔案格式。

上傳的圖示影像會自動裁切，且圖示背景會變為透明。請確認標誌能放入預覽影像中的綠色方框內。

![](https://developers.line.biz/media/line-mini-app/line-mini-app-icon/mini-icon-form-en.png)
