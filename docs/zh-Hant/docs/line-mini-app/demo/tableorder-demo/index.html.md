# 桌邊點餐示範（Table order demo）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

使用者可以透過 LINE MINI App，在店內外完成從預先點餐到付款（含外送）的所有流程。

透過將 LINE MINI App 與 LINE 官方帳號連動，使用者在使用服務的過程中，便可以無縫地為 LINE 官方帳號招募好友。此外，藉由運用透過 LINE MINI App 取得的使用者資料，還能達成更有效率的推廣活動。（\* 僅限於在同一個 provider 內提供時。）

\* 您必須取得使用者的同意，才能收集並運用與其 LINE 帳號連結的行為資料。

<!-- table of contents -->

## View the demo 

您可以在智慧型手機上啟動 LINE 並掃描此 QR code 來查看示範。

![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-en-qr-img.webp)

<!-- note start -->

**示範 App 所取得的資料**

請注意，示範 App 將會存取您的 LINE 帳號個人檔案資訊，包括您的顯示名稱與使用者 ID。您的使用者 ID 會儲存在伺服器上，但這些資料會每天刪除。付款將從本示範 App 所準備的 LINE Pay 餘額中扣除，不會實際選擇付款方式或進行付款。

請在了解上述各點的前提下使用本服務。

<!-- note end -->

## How to use 

\* 畫面設計可能因您的版本而有所不同。

| | | | |
| --- | --- | --- | --- |
|![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-en-image1.webp)|![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-en-image2.webp)|![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-en-image3.webp)|![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-en-image4.webp)|
| 1.掃描 QR code | 2.授權所需的權限 | 3.選擇商品並下單 | 4.結帳 |

<!-- tip start -->

**重點**

1. 用智慧型手機即可完成從點餐到結帳的所有流程，減少與店員的接觸，有助於防止傳染
2. 多人可以分別點餐並各自付款
3. 導入 App 可降低人力、人事成本與終端機租賃成本
4. 與終端使用者進行線上溝通
5. 透過桌邊點餐 App，依使用者的操作與到店紀錄發送訊息

<!-- tip end -->

## Benefits 

### End user benefits 

#### 1. Complete everything from ordering to checkout with a smartphone, which reduces contact with store clerks and helps prevent infections 

您可以透過掃描桌上的 QR code 來啟動 LINE MINI App。如果您在座位上使用 LINE MINI App 下單並完成結帳，就不需要面對面接觸，有助於防疫。

#### 2. Multiple people can order and pay separately 

當您和一大群人一起到餐廳用餐時，桌邊點餐 App 也很實用。店家通常每桌只配置一台終端機，但這種情況下一次只能由一個人操作。透過桌邊點餐 App，每個人都可以同時用自己的智慧型手機點餐。此外，每個人還可以分別結帳，省去分攤帳單的麻煩。

### Service provider benefits 

#### 1. Reduce labor, labor costs, and terminal leasing costs by introducing an app 

減輕員工處理點餐與付款的負擔，並提升工作效率。同時也能減少面對面接觸的需求，有助於防止傳染病。此外，如果您想使用專用平板電腦導入桌邊點餐，就需要支付點餐終端機的租賃費用。透過桌邊點餐 App，會以使用者的智慧型手機取代點餐終端機，因此無需支付點餐終端機的租賃費用。

#### 2. You can also provide customer support by handling user inquiries 

您可以在第一個驗證畫面上提示使用者將 LINE 官方帳號加為好友。針對將 LINE 官方帳號加為好友的使用者，您可以發送推播訊息（例如促銷活動），並在日後接受詢問。

#### 3. Deliver messages based on the user's operation and store visit history with the table order app 

您可以透過將桌邊點餐 App 與使用者 ID 連結，記錄該 App 的操作與到店紀錄。在符合條件的情況下，您可以根據這些紀錄，透過 LINE 向使用者發送實用資訊，作為提升回訪率等促銷措施。

\* 您必須取得使用者的同意，才能收集並運用與其 LINE 帳號連結的行為資料。

## System and sequence diagram of the demo application 

此圖顯示示範 App 如何使用 LINE API。

\* 圖中包含示範 App 尚未實作的功能。

**系統圖**

![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-system-diagram-en.webp)

- 使用其他服務的系統圖
  - [使用 AWS 的系統圖](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-system-diagram-aws-en.webp)
  - [使用 Azure 的系統圖](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-system-diagram-azure-en.webp)

**序列圖**

![](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-sequence-diagram-en.webp)

- 使用其他服務的序列圖
  - [使用 AWS 的序列圖](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-sequence-diagram-aws-en.webp)
  - [使用 Azure 的序列圖](https://developers.line.biz/media/line-mini-app/demo/tableorder-demo/tableorder-sequence-diagram-azure-en.webp)

## Related links 

- [Messaging API documentation](https://developers.line.biz/en/docs/messaging-api/)
- [LINE MINI App documentation](https://developers.line.biz/en/docs/line-mini-app/)
