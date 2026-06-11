# 活動體驗示範

<!-- tip start -->

**關於本頁**

本頁內容是從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當時的資訊。

<!-- tip end -->

透過將 LINE 與多模式路徑搜尋服務 [mixway API](https://mixway.ekispert.net/lp/api)（僅提供日文版）結合，您可以為演唱會、慶典、煙火大會等活動的參加者打造更聰明的活動體驗。

從終端使用者的角度來看，參加一場活動似乎是單一的流程。但實際上，它由多個較小的步驟組成——例如預約活動（購買票券）、查詢前往會場的路徑、安排交通方式，以及出席活動（出示票券等）。在此之前，每個流程都需要各自專屬的應用程式，這意味著使用者必須為每一個建立並管理各自獨立的帳號。

透過將所有這些流程整合到單一 LINE MINI App，並集中到一個帳號，您可以消除使用者在參加活動時所面臨的小障礙。這就是我們所說的更聰明的活動體驗。

<!-- table of contents -->

## View the demo 

這款示範應用程式讓您體驗參加活動的全新方式，模擬「與朋友一起去看煙火大會」的情境。您可以在智慧型手機上啟動 LINE 並掃描此 QR code 來觀看示範。

![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-qr-demo-en.webp)

<!-- note start -->

**示範應用程式所取得的資料**

在使用示範應用程式之前，請注意該應用程式會存取您的 LINE 帳號個人資料資訊，包括您的顯示名稱與使用者 ID。您的使用者 ID 會儲存在伺服器上，但這些資料每天會被刪除。

<!-- note end -->

## How to use the demo app 

\* 畫面設計可能會因您的版本而有所不同。

| | | | |
| --- | --- | --- | --- |
|![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-image1-en.png)|![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-image2-en.png)|![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-image3-en.png)|![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-image4-en.png)|
| 1.初始化應用程式 | 2.活動票券購買流程 | 3.搜尋並選擇路徑 | 4.發送通知 |

<!-- tip start -->

**重點**

1. 在 LINE 內完成所有必要的活動參加流程。
2. 在 LINE 中傳遞關於活動行程與交通延誤的通知。
3. 支援將活動專屬巴士（例如需求型交通）等專有交通方式納入考量的路徑搜尋。
4. 便於開發結合大眾運輸與需求型交通的路徑搜尋。
5. 不需要繁複的手續，讓使用者可以輕鬆開始。
6. 預期能提升活動會場的安全性並減少壅塞。

<!-- tip end -->

## Benefits 

### End user benefits 

#### 1. Completes all necessary event participation processes within LINE 

預約、付款、查詢前往會場的路徑、安排交通方式，以及出示票券，全都在熟悉的 LINE 應用程式中完成。這消除了為每個流程使用各自專屬應用程式、建立並管理專屬帳號或列印票券的麻煩。

#### 2. Delivers notifications in LINE about event schedules and transportation delays 

活動行程與已預約交通方式的延誤資訊，會在 LINE 應用程式中傳遞（推播通知）。使用者不必擔心忘記活動，或是在不熟悉的地區錯過交通中斷的資訊。

#### 3. Enables route searching that considers proprietary transportation such as event-specific buses (e.g. demand mobility) 

使用者可以搜尋包含需求型交通、臨時巴士或僅在活動當天運行、且通常不在一般路徑搜尋應用程式涵蓋範圍內的臨時共享單車的路徑。由於搜尋會將需求型交通的運行時間納入考量，使用者可以制定更詳細的行程。

### Service provider benefits 

#### 1. Facilitates easy development of route searches that combine public transportation with demand mobility 

透過使用 mixway API（一款適用於 MaaS 的多路徑搜尋 API），您可以實現結合大眾運輸與步行、駕車、共享單車、需求型交通等的多模式導航。

#### 2. Requires no complicated procedures, allowing users to start easily 

由於終端使用者可以透過熟悉的 LINE 應用程式處理預約、付款、路徑搜尋與票券出示，參加活動的門檻因此降低。您可以直接透過 LINE 提供全新的活動體驗。

#### 3. Expected to enhance safety and reduce congestion at event venues 

大型活動經常在會場與周邊地區面臨壅塞問題。透過 LINE 掌握參加人數，並支援他們往返活動的交通，您可以提供更安全、更順暢的活動體驗。

## System and sequence diagram of the demo application 

此圖顯示示範應用程式如何使用 LINE API。

\* 此圖包含示範應用程式中未實作的功能。

**系統圖**

![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-system-diagram-en.png)

- 使用其他服務的系統圖
  - [使用 AWS 的系統圖](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-system-diagram-aws-en.png)
  - [使用 Azure 的系統圖](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-system-diagram-azure-en.png)

**序列圖**

![](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-sequence-diagram-en.png)

- 使用其他服務的序列圖
  - [使用 AWS 的序列圖](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-sequence-diagram-aws-en.png)
  - [使用 Azure 的序列圖](https://developers.line.biz/media/line-mini-app/demo/mixwayapi-demo/maas-mixwayapi-sequence-diagram-azure-en.png)

## Related links 

- [Messaging API 說明文件](https://developers.line.biz/en/docs/messaging-api/)
- [LINE MINI App 說明文件](https://developers.line.biz/en/docs/line-mini-app/)
