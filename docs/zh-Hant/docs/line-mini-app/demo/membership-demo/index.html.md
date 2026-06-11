# 會員卡示範（Membership card demo）

<!-- tip start -->

**關於本頁**

本頁內容是從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）移轉至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

你可以使用 LINE MINI App，在 LINE 上為自己的服務提供會員卡。

舉例來說，在超市、藥妝店、服飾店等實體店面提供會員卡的公司，也能轉換為線上會員卡。這能建立一條光靠實體會員卡無法達成的使用者溝通管道。具體而言，你可以運用透過 LINE MINI App 取得的使用者 ID，發送如促銷活動之類的推播訊息。

\* 你必須取得使用者的同意，才能蒐集並運用與其 LINE 帳號連結的行為資料。

<!-- table of contents -->

## View the demo 

啟動智慧型手機上的 LINE 並掃描此 QR code，即可檢視示範。

![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-en-qr-img.webp)

<!-- note start -->

**示範 App 會取得的資料**

在使用示範 App 之前，請注意此 App 會存取你的 LINE 帳號個人檔案資訊，包括你的顯示名稱與使用者 ID。你的使用者 ID 將儲存於伺服器上，但此資料每日會被刪除。

<!-- note end -->

## How to use the demo app 

\* 畫面設計可能因版本而有所不同。

| | | | |
| --- | --- | --- | --- |
|![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-en-image1.webp)|![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-en-image2.webp)|![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-en-image3.webp)|![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-en-image4.webp)|
| 1.掃描 QR code | 2.授權所需的權限 | 3.發行會員卡 | 4.電子收據 |

<!-- tip start -->

**重點**

1. 不再需要實體會員卡
2. 無需交付實體卡片，減少實體接觸
3. 無需輸入任何個人資訊即可立即發行會員卡
4. 可依據與線上會員卡連結的活動紀錄發送訊息

<!-- tip end -->

## Benefits 

### End-user benefits 

#### 1. No more need for physical membership cards 

線上會員卡不像實體會員卡那樣會塞滿你的錢包。你只要在店內掃描 QR code，就能輕鬆發行會員卡。你也只需開啟 LINE 即可出示線上會員卡。

#### 2. No physical cards to deliver, reducing physical contact 

會員卡可顯示於 LINE App 上，省去交付實體卡片的需求。這有助於減少接觸機會，進而協助預防傳染。

### Service provider benefits 

#### 1. Membership cards can be issued immediately without entering any personal information 

一般而言，發行會員卡時需要姓名、地址等個人資訊以辨識個人身分。然而，使用 LINE MINI App 的線上會員卡可與使用者在 LINE 上已登錄的資訊連結。換句話說，由於無需向使用者取得個人資訊，因此可以安全地發行會員卡，而不必為了防止個人資訊外洩而付出不必要的成本。

#### 2. Messages can be delivered based on the activity history associated with the online membership card 

你可以將行為紀錄與使用者 ID 連結來加以記錄。若符合條件，你可以運用這些紀錄，透過 LINE 向使用者發送有用的資訊作為促銷措施，例如提高回購率。

## System and sequence diagram of the demo application 

此圖顯示示範 App 如何使用 LINE API。

\* 此圖包含了示範 App 中尚未實作的功能。

**系統圖（System diagram）**

![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-system-diagram-en.webp)

- 使用其他服務的系統圖
  - [使用 AWS 的系統圖](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-system-diagram-aws-en.webp)
  - [使用 Azure 的系統圖](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-system-diagram-azure-en.webp)

**序列圖（Sequence diagram）**

![](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-sequence-diagram-en.webp)

- 使用其他服務的序列圖
  - [使用 AWS 的序列圖](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-sequence-diagram-aws_en.webp)
  - [使用 Azure 的序列圖](https://developers.line.biz/media/line-mini-app/demo/membership-demo/membership-sequence-diagram-azure_en.webp)

## Related links 

- [Messaging API documentation](https://developers.line.biz/en/docs/messaging-api/)
- [LINE MINI App documentation](https://developers.line.biz/en/docs/line-mini-app/)
