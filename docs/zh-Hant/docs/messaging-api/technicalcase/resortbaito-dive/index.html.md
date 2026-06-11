# 提升臨時人員滿意度的「Resort Baito Dive」開發案例研究（A case study on the development of \"Resort Baito Dive\" to enhance temporary staff satisfaction）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![Dive Inc.](https://developers.line.biz/media/messaging-api/technicalcase/resortbaito-dive/en/resortbaito-dive-logo.png)

**Dive Inc.**

Dive Inc. 是一家新創公司，核心業務是為觀光設施提供人力派遣服務，主要透過「resort baito」（短期度假打工）。我們致力於解決觀光產業所面臨的嚴重勞動力短缺問題。我們的服務網站每年註冊使用者超過 40,000 人，LINE 好友數已突破 150,000。透過創造連結勞動者與在地社群的就業機會，我們致力於地方振興與觀光產業的成長。

## Service overview and issues to address 

在 Dive Inc.，我們的度假打工人力派遣服務「Resort Baito Dive」使用 LINE Official Account。透過 LINE Official Account，臨時人員每天與業務代表及客戶支援進行溝通。這些互動涵蓋廣泛的主題，從派遣期間的日常疑慮到求職諮詢都包含在內。在旺季月份，每月發送的訊息數量約達 63,000 則。我們致力於用心處理每一次互動，因此獲得了臨時人員高度正面的回饋。

### Image 

![service-image](https://developers.line.biz/media/messaging-api/technicalcase/resortbaito-dive/en/resortbaito-dive-ui-img.png)

![service-cms-image](https://developers.line.biz/media/messaging-api/technicalcase/resortbaito-dive/en/resortbaito-dive-ui-img-2.png)

## System Overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/resortbaito-dive/en/resortbaito-dive-system.png)

### Technologies that support Resort Baito Dive and their impacts 

我們的基礎設施建立在 AWS 上。前端使用 CloudFront 與 S3 提供服務，後端 API 則使用 ALB（Application Load Balancer）與 ECS on Fargate 建構。

接收使用者聊天訊息的 Webhook，採用 API Gateway 與 SQS（Simple Queue Service）組合設計，後續處理則由 Lambda 負責。這套架構確保能可靠地接收使用者訊息。我們在資料庫採用 Aurora Serverless v2，透過自動化資源配置提升維運效率。此外，這些基礎設施配置以 AWS CDK 作為程式碼來管理，部署則透過 GitHub Actions 自動化。在開發語言方面，前端、後端與基礎設施一致採用 TypeScript，以降低工程師的認知負擔。這套統一的做法讓系統得以高效且高品質地運作。

發布之後，從上一個營業日結束到下一個營業日開始之間所收到的聊天訊息，其回覆已能在上午完成，而此前這項工作會延續到下午。此外，搜尋功能的強化將每天進行數次、用於例行檢查是否有漏回聊天訊息所需的時間，從每次約一小時縮短到約 30 分鐘，使維運效率獲得大幅改善。

### Future outlook for Resort Baito Dive 

隨著聊天資料如今已在公司內部累積，我們計畫將這些資料運用於分析用途，以進一步提升使用者滿意度。

### Requests for the LINE API 

由於用於取得群組聊天與多人聊天成員 user ID 的 API 僅能由已驗證帳號執行，我們在使用開發帳號進行測試時遇到了困難。我們希望，若能透過專為測試目的設立的特別申請流程，讓未驗證帳號也能使用此 API，將不勝感激。

- [Get group chat member user IDs](https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids)

- [Get multi-person chat member user IDs](https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids)

### A message for those developing new services 

當你需要確實接收使用者訊息（例如聊天訊息）時，一個有效的做法是將透過 Webhook 收到的訊息放入佇列（queue）。以這種方式將訊息接收與處理分離，可以打造出具可擴展性的架構。

---

## Related Links 

- [Dive Inc.](https://resortbaito-dive.com/)
- [Development Company: Classmethod, Inc.](https://classmethod.jp/)
