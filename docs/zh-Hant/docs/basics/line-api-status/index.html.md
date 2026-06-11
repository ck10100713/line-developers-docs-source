# 確認 LINE Platform 的可用性（LINE API Status）

LY Corporation 提供 [LINE API Status](https://api.line-status.info/)，可用來確認 LINE Platform 的可用性與服務中斷狀態。

<!-- table of contents -->

## What is LINE API Status 

LINE API Status 是一個可讓你確認 LINE Platform 可用性與服務中斷狀態的網站。可用性與服務中斷狀態資訊以英文提供。

<!-- note start -->

**關於 LINE API Status 上的資訊**

LY Corporation 會透過 LINE API Status 提供服務中斷狀態的資訊，但這並不保證資訊即時、準確或完整。我們會持續透過 LINE Developers 網站上的 [News](https://developers.line.biz/en/news/tags/outage-report/) 向你說明服務中斷的詳情，例如原因與影響範圍。

<!-- note end -->

- [LINE API Status](https://api.line-status.info/)<br>![](https://developers.line.biz/media/basics/line-api-status.png)

### Provision of ATOM and RSS feeds 

LINE API Status 提供 ATOM 與 RSS feed。你可以在 LINE API Status 上點擊 **SUBSCRIBE TO UPDATES** 來取得 ATOM 或 RSS feed。

![](https://developers.line.biz/media/news/line_api_status_rss_feed.png)

### Display when operation is stable 

當沒有服務中斷且運作穩定時，會顯示 `All Systems Operational`。

![](https://developers.line.biz/media/news/line_api_status_operational.png)

### Display when outage occurs 

當發生服務中斷時，會針對發生中斷的服務以及中斷的發生情形顯示以下內容：

![](https://developers.line.biz/media/news/line_api_status_outage.png)

服務中斷狀態也會透過此彈出視窗顯示在 [LINE Developers 網站](https://developers.line.biz/)上。

![](https://developers.line.biz/media/news/line_api_status_outage_popup.png)

## Services covered by LINE API Status 

LINE API Status 涵蓋以下服務：

- Messaging API
  - API
  - Webhook
- LINE Developers
  - LINE Developers 網站
  - LINE Developers Console
- LIFF
- LINE Login

目前，LINE API Status 不涵蓋 LINE 應用程式以及上述以外的服務。

## Accessing LINE API Status 

你可以從 LINE Developers 網站頁首的 **More** 選單或頁尾存取 LINE API Status。

![](https://developers.line.biz/media/basics/line-api-status-from-header-en.png)

![](https://developers.line.biz/media/basics/line-api-status-from-footer-en.png)
