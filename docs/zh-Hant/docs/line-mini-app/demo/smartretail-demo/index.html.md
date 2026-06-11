# 購物體驗範例

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

善用智慧型手機這項離終端使用者最近的裝置，為零售業者推動 DX（Digital Transformation，數位轉型）。尤其是提供結合線上與線下的顧客體驗（OMO：Online Merges with Offline，線上與線下融合），預期將成為新的零售標準。過去顧客體驗主要侷限於店內體驗，但現在不再僅限於店內，而是能高度設計成從進店前到進店後的無縫顧客體驗，為終端使用者帶來顯著的好處。

透過使用 LINE MINI App，您可以用單一個 LINE 完成以下所有的價值提供。透過 LINE 官方帳號（LINE Official Account）與 LINE MINI App 取得的使用者行為資料，可以儲存在服務供應商準備的 CRM 中，實現為每位終端使用者量身打造、最精緻且無縫的顧客體驗。

- 在進店前透過 LINE Ads、LINE 官方帳號、LINE Flyers 以及獨特的預約系統提供特別優惠
- 透過智慧型手機結帳、數位會員卡，以及查看購買紀錄（收據）的功能，改善購物體驗
- 透過 LINE 官方帳號進行購買後的溝通

此外，藉由將 [GS1 標準的 2D 條碼](https://www.gs1jp.org/standard/industry/2d-in-retail/)（僅提供日文版）整合進智慧型手機收銀機，您可以創造全新的購物體驗並實現店鋪 DX。

<!-- table of contents -->

## OMO concept powered by LINE 

在由 LINE 驅動的全新數位時代購物體驗（OMO）中，會從進店前到購買後提供一致的旅程。在進店前，會透過 LINE Ads、LINE 官方帳號與 LINE Flyers 提供資訊，而店內促銷則使用 LINE POP Media 與數位看板進行。在購買時，透過智慧型手機自助結帳、以 LINE 為基礎的活動報名以及電子商務網站簡化流程，接著再透過 LINE 官方帳號進行購買後的互動。如此便能打造出整合線上與線下接觸點的無縫購物體驗。

![](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-image-data-en.webp)

## View the smartphone register demo 

- [讓我們透過範例網站，體驗使用 LINE MINI App 的實際購物旅程。](https://lineapiusecase.com/en/omo/index.html)

## Benefits 

### End user benefits 

#### 1. No need to download the app or deal with a complicated enrollment process 

無需經過繁複的註冊流程即可使用零售業者提供的服務。您可以立即享受卓越的顧客體驗。

#### 2. Complete everything from getting store deals to making payments on LINE 

您可以使用 LINE flyer 在進店前取得特別優惠的資訊。您也可以在 LINE 上完成付款，省去收銀台壅塞時排隊的需要。這有助於防止感染，並大幅縮短購物時間。

#### 3. Seamless access to all services, including membership cards 

您可以發行數位會員卡，並在 LINE 上收到數位購買憑證（收據）。您也可以在 LINE 上取得並使用會員優惠與點數。您甚至可以將 LINE 當作自助結帳系統，輕鬆查看購買紀錄，讓終端使用者免於繁瑣的會員卡與收據管理。

### Service provider benefits 

#### 1. No complicated procedures are required and people can easily start using the service 

使用者不僅只要掃描 QR code 就能開始使用系統，如果不願意的話，也無需輸入姓名與地址。由於開始使用服務的門檻降低，使用者採用系統的可能性很高。

#### 2. Communicate with end users offline and online 

舉例來說，您可以透過 LINE 官方帳號發送活動資訊，並發放為每位終端使用者量身打造的優惠券。此外，由於 LINE 官方帳號能即時對終端使用者發送通知，您可以依據商品的銷售狀況吸引顧客上門。

#### 3. It can reduce congestion in front of the cash register, prevent infections, and save money 

由於終端使用者可以使用智慧型手機付款，無需導入自助結帳系統，並可減少收銀員人數，從而節省成本。此外，藉由減少在收銀台等候的人數，系統也有助於防止感染。

## System and sequence diagram of the demo application 

此圖顯示範例 App 如何使用 LINE API。

\* 此圖包含範例 App 中尚未實作的功能。

**系統圖**

![](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-system-diagram-en.webp)

- 使用其他服務的系統圖
  - [使用 AWS 的系統圖](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-system-diagram-aws-en.webp)
  - [使用 Azure 的系統圖](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-system-diagram-azure-en.webp)

**序列圖**

![](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-sequence-diagram-en.webp)

- 使用其他服務的序列圖
  - [使用 AWS 的序列圖](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-sequence-diagram-aws_en.webp)
  - [使用 Azure 的序列圖](https://developers.line.biz/media/line-mini-app/demo/smartretail-demo/smartretail-sequence-diagram-azure-en.webp)

## Related links 

- [Messaging API 文件](https://developers.line.biz/en/docs/messaging-api/)
- [LINE MINI App 文件](https://developers.line.biz/en/docs/line-mini-app/)
