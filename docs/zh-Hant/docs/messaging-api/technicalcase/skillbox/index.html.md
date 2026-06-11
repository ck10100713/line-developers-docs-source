# SkillBox 技術案例研究：LINE 通知大幅提升員工敬業度問卷的使用率，即使是沒有電子郵件信箱的員工也能參與

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁呈現採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時所提供的資訊。

<!-- tip end -->

![HRCOM Co.](https://developers.line.biz/media/messaging-api/technicalcase/skillbox/en/skillbox-logo.png)

**HRCOM Co. Ltd.**

我們是提升員工敬業度的專家，協助推動員工敬業度問卷的實施，包括問卷設計、分析報告製作，以及改善措施的提案與應用。我們同時提供「SkillBox」這項提升敬業度的解決方案，例如解決內部溝通問題。

## SkillBox, a praise-based mentor system 

SkillBox 是一套以讚美為基礎的導師制度，能輕鬆提升敬業度。比較低敬業度與高敬業度的組織時，可發現低敬業度的組織缺乏對員工的鼓勵，而高敬業度的組織則經常提供支持性的回饋，例如「做得好！」、「有什麼遇到困難的地方嗎？」以及「繼續加油！」SkillBox 自然地營造出一種情境，讓新進員工與資深員工每週只需花 1 至 2 分鐘互動，就能頻繁地彼此給予正向回饋，進而提升敬業度。

具體來說，新進員工每週會進行一次自我檢視，針對預先設定的行動清單中的每個項目選擇「已完成」或「未完成」。自我檢視畫面也包含一個選填的自由文字欄位，讓新進員工分享自己的努力或尋求建議，藉此向其導師回報目前的狀態。導師可以用貼圖或留言對檢視內容做出回應，透過這些互動輕鬆地以導師身分提供必要的後續關懷。

透過 SkillBox，我們希望解決年輕員工早期離職的課題。超過 30% 的大學畢業生在進入公司三年內離職，（\*1）許多組織將年輕員工的離職視為嚴重問題。導師計畫是解決這項課題的方法之一，已有 48% 的企業採用，而其中 70% 的企業表示這類計畫具有成效。（\*2）然而，在許多情況下，導師（通常是資深員工）因定期會談及其他任務而承擔的負擔相當沉重。因此，這類計畫有時會在各團隊的自行決定下淪為形式。透過運用 SkillBox，企業可以將導師的負擔降到最低，並確保導師制度正常運作，進一步降低離職率。

\*1：[厚生勞動省：「新畢業生的就業狀況（2020 年 3 月畢業生）」](https://www.mhlw.go.jp/content/11805001/001158687.pdf)

\*2：[HR Research Institute：「員工培育調查：新進員工訓練」－調查結果報告（2020）](https://hr-souken.jp/research/2550/)

### Image 

![service-image](https://developers.line.biz/media/messaging-api/technicalcase/skillbox/en/skillbox-ui-img.png)

## System overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/skillbox/en/skillbox-system.png)

### Technical architecture of AWS-based projects 

我們選擇 Amazon Web Services（AWS）作為本專案的核心系統基礎架構。後端方面，我們使用 Python 這個能輕鬆整合機器學習模型的程式語言。專案框架則採用 Flask，這是一個能在 ECS 與 Lambda 上順暢運行的輕量級框架。此外，我們建置了一個以 CloudFront 與 S3 運行 Vue.js 的前端環境，以及一個使用 ECS 與 Flask 的後端環境。資料庫使用 Amazon Aurora。ECS 負責處理來自 LINE API 的回呼（callback），而 AWS Lambda 則透過 LINE API 為使用者執行排程通知處理。我們使用 GitHub Actions 進行持續整合（CI），並使用 AWS CodePipeline 進行持續交付（CD）。由於本專案中 LINE 專門用於通知用途，因此我們使用 LINE WORKS 與 Messaging API。

### Building response habits and contributing to lower turnover 

SkillBox 現在連員工沒有公司電子郵件信箱的企業也開始採用。透過 LINE API 整合（LINE WORKS 與 Messaging API）導入 SkillBox 的企業，對其簡單易用給予了高度好評。例如，有一個實際案例是在日本各地經營美容診所的 Olive Spa。該公司先前是以紙本日報的方式來支援新進員工，而 SkillBox 作為這種做法的便利進化版本，廣受好評。關於使用個人智慧型手機，該公司表示：「開始運作時完全沒有任何問題，職場也順利接受了」，並表示：「我們真切地感受到它有助於防止員工離職」。（\*4）

\*4：[SkillBox 案例研究：Olive Spa Co., Ltd.](https://www.skillbox.jp/eduken/interview006)

### Future prospects for SkillBox feature improvements 

我們計劃持續改善 SkillBox，使其隨著時間推移變得更便於使用並帶來更大成效。我們在內部強調的一項原則是，系統必須讓使用者覺得有趣。這包括系統的功能面向，例如透過遊戲化（gamification）融入遊戲般的元素，也包括營運面的考量，例如如何以自然、低壓力的方式鼓勵養成回應的習慣。因此，我們認為持續重新思考回應請求通知的傳送方式，以及使用哪些裝置來提交回應，是相當重要的。在這方面，進一步精進我們與 LINE 的 API 整合，可能會帶來更多機會。舉例來說，未來的構想包括讓使用者能直接透過 LINE Official Account 在 SkillBox 上提交回應，或讓使用者能直接在官方帳號上閱讀 SkillBox 中的留言。雖然這些目前仍處於概念階段，但我們的目標是持續推進讓 SkillBox 對使用者更加便利的各項措施。

### Requests for the LINE API 

LINE API 提供了豐富完整的文件，讓我們得以順利地實作。雖然目前通知是透過 LINE 傳送，使用者則在網頁上輸入回應，但我們也曾考慮讓使用者能直接在 LINE 內進行回應。然而，對於需要多重選擇或多項輸入的表單而言，取消或編輯已提交回應的流程往往會變得複雜，因此我們決定不採取這種做法。我們在通知處理上也使用了 LINE WORKS API。在某些情況下，錯誤訊息提供的資訊有限，使我們難以判斷錯誤的確切原因或將其縮小至單一因素。

### A message for those developing new services 

我們已營運使用 LINE API 的服務超過兩年。至今我們極少遇到通訊錯誤或其他問題，這項服務也證明了它比我們同時期使用的其他類似第三方服務更為穩定一致。

---

## Related Links 

- [HRCOM Co. Ltd.](https://hrcom.co.jp/)
- [SkillBox](https://www.skillbox.jp/)
