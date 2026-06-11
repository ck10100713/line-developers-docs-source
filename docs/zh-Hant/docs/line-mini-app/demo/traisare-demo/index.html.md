# 行動體驗示範（Mobile experience demo）

<!-- tip start -->

**關於本頁面**

本頁面包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

只要將 MaaS Tech Japan 的整合式行動數據平台 [TraISARE](https://traisare.maas.co.jp/)（僅提供日文版）與 LINE 結合，便能提供個人化的行動體驗。

從終端使用者的角度來看，這讓使用者可以購買遊覽票券、取得交通即時資訊，並依據使用紀錄獲得個人化推薦與優惠券——這一切都能在 LINE 這個使用者每天都會用到的 App 上便利地完成。

對服務提供者而言，整合並分析交通、人流與行為數據，有助於提出兼顧使用模式與壅塞程度的最佳化交通方案，引導使用者改變行為。

我們的目標是透過 LINE 降低導入 MaaS（Mobility as a Service，行動即服務）的門檻，並運用 TraISARE 的各種行動數據，以量身打造的方式提升使用者體驗。這正是我們對個人化行動體驗的願景。

<!-- table of contents -->

## View the demo 

- [在示範網站上，透過 LINE MINI App 體驗真實的行動旅程吧。](https://lineapiusecase.com/en/traisare/index.html)

## Benefits 

### End user benefits 

#### 1. No app downloads or complicated registration required 

使用 LINE MINI App，不需要下載專屬 App，也不必輸入個人資訊——即可立即開始使用 MaaS。

#### 2. Receive useful information tailored to your situation while on the go 

依據交通票券的使用情形，取得與旅程相關的實用資訊與專屬優惠券。

#### 3. Travel comfortably without worrying about delays or crowding 

即時接收大眾運輸的誤點與壅塞熱點資訊，讓你不必自行搜尋資訊，就能盡情享受出遊。

### Service provider benefits 

#### 1. Easily implement a PDCA cycle for MaaS initiatives 

透過 LINE MINI App 以及 TraISARE 數據平台與儀表板，你可以減輕提供專屬 MaaS App、以及建置數據累積與成效驗證基礎設施的負擔，進而輕鬆落實 PDCA 循環。

#### 2. Promote behavioral change to avoid congestion and encourage service use 

發放優惠券協助使用者避開壅塞區域，並依據行為預測發送資訊，以促使使用者改變行動。此外，還能分析累積的數據，追蹤優惠券發送後使用者的移動與停留時間。

#### 3. Provide more convenient and comfortable travel through integrated transportation information 

TraISARE 能與外部服務整合，取得交通與壅塞數據。此外，透過 LINE 即時提供資訊有助於提升服務品質，並可望延長使用者在特定區域的停留時間。

## System and sequence diagram of the demo application 

下圖說明示範 App 如何使用 LINE API。

\* 此圖包含示範 App 中尚未實作的功能。

**系統圖（System diagram）**

![](https://developers.line.biz/media/line-mini-app/demo/traisare-demo/traisare-system-diagram-en.png)

**循序圖（Sequence diagram）**

![](https://developers.line.biz/media/line-mini-app/demo/traisare-demo/traisare-sequence-diagram-en.png)

## Related links 

- [Messaging API documentation](https://developers.line.biz/en/docs/messaging-api/)
- [LINE MINI App documentation](https://developers.line.biz/en/docs/line-mini-app/)
