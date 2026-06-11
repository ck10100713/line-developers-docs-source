# 店家預約示範（Store reservation demo）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

你可以運用 LINE MINI App 進行預約，例如美髮沙龍與餐廳的預約。

為了避免使用者忘記預約，當預約時間接近時，LINE MINI App 可以透過 LINE 訊息發送提醒。此外，若符合相關條件，從 LINE MINI App 取得的 user ID 不僅可用於發送預約通知，也可用於發送促銷活動等推播訊息。

\* 你必須取得使用者的同意，才能蒐集並運用與其 LINE 帳號連結的行為資料。

<!-- table of contents -->

## View the demo 

啟動智慧型手機上的 LINE 並掃描此 QR code，即可檢視示範。

![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-en-qr-img.webp)

<!-- note start -->

**示範應用程式取得的資料**

使用示範應用程式之前，請注意此應用程式將存取你的 LINE 帳號個人檔案資訊，包括你的顯示名稱與 user ID。你的 user ID 會儲存在伺服器上，但這些資料每天都會被刪除。

<!-- note end -->

## How to use 

\* 畫面設計可能因版本不同而有所差異。

| | | | |
| --- | --- | --- | --- |
|![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-en-image1.webp)|![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-en-image2.webp)|![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-en-image3.webp)|![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-en-image4.webp)|
| 1.掃描 QR code | 2.授權所需的權限 | 3.指定日期與時間進行預約 | 4.提醒通知 |

<!-- tip start -->

**重點**

1. 無須下載應用程式或註冊成為會員
2. 透過提醒通知協助使用者記得預約
3. 根據使用者預約應用程式的操作與到店紀錄發送訊息

<!-- tip end -->

## Benefits 

### End user benefits 

#### 1. No need to download the app or register as a member 

LINE MINI App 不需要在智慧型手機上下載或安裝，也不需要輸入個人資訊，因此你可以立即進行預約。

#### 2. Prevent users from forgetting with reminder notifications 

在你到店前，系統會將服務訊息以提醒通知的形式發送到你的聊天室。你可以自由選擇通知日期。即使忙於工作或私人生活，你也不會忘記預約日期。

### Service provider benefits 

#### 1. Help users remember reservations with reminder notifications 

為了避免使用者忘記到店，可以在使用者到店當天、到店前一天或其他希望的日子，透過 LINE 訊息提醒使用者。

#### 2. Deliver messages based on the operation and store visit history of the user's reservation app 

你可以將預約應用程式的操作與到店紀錄連結到 user ID 來記錄這些資訊。你可以運用這些紀錄，透過 LINE 向使用者發送有用的資訊，作為促銷手段，例如提高回訪率。

## System and sequence diagram of the demo application 

下圖顯示示範應用程式如何使用 LINE API。

\* 圖中包含未在示範應用程式中實作的功能。

### Hair salon 

**系統圖**

![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-system-diagram-en.webp)

- 使用其他服務的系統圖
  - [使用 AWS 的系統圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-system-diagram-aws-en.webp)
  - [使用 Azure 的系統圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-system-diagram-azure-en.webp)

**順序圖**

![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-sequence-diagram-en.webp)

- 使用其他服務的順序圖
  - [使用 AWS 的順序圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-sequence-diagram-aws_en.webp)
  - [使用 Azure 的順序圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-sequence-diagram-azure_en.webp)

### Restaurant 

**系統圖**

![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-2-system-diagram-en.webp)

- 使用其他服務的系統圖
  - [使用 AWS 的系統圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-2-system-diagram-aws-en.webp)
  - [使用 Azure 的系統圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-2-system-diagram-azure_en.webp)

**順序圖**

![](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-2-sequence-diagram-en.webp)

- 使用其他服務的順序圖
  - [使用 AWS 的順序圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-2-sequence-diagram-aws_en.webp)
  - [使用 Azure 的順序圖](https://developers.line.biz/media/line-mini-app/demo/reservation-demo/reserve-2-sequence-diagram-azure_en.webp)

## Related links 

- [Messaging API 文件](https://developers.line.biz/en/docs/messaging-api/)
- [LINE MINI App 文件](https://developers.line.biz/en/docs/line-mini-app/)
