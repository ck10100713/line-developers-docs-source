# 排隊管理解決方案如何透過 LINE MINI App 擴展規模：「matoca」與「yoboca」的開發案例

<!-- tip start -->

**關於本頁面**

本頁面包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁面呈現採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時所提供的資訊。

<!-- tip end -->

![BraveTechnology inc.](https://developers.line.biz/media/line-mini-app/technicalcase/bravetechnology/en/bravetechnology_logo.webp)

**BraveTechnology inc.**

排隊等候是每個人都會經歷的事。在 BraveTechnology，我們的使命是透過 LINE MINI App 提供候位與通知服務，減輕排隊所帶來的壓力。

## The service provider’s thoughts on developing the system 

我們提供服務，以實現為每個人減輕等候壓力的使命。

大多數人都不喜歡等待，無論是出乎意料的長時間等候，還是即使已經預約卻仍要延遲。另一方面，商家也面臨著讓顧客久候的壓力，以及可能對周邊區域造成困擾的壓力。在 COVID-19 疫情期間，由於人們試圖避免「三密」（密閉空間、人潮聚集的場所，以及近距離接觸的環境），這種壓力更是加劇。

為了解決這些問題，我們提供兩項服務：用於候位管理的「matoca」與用於取貨通知的「yoboca」。透過 matoca，使用者無須親自站著排隊即可保留排隊位置，並會在輪到自己時透過 LINE 收到通知。在從購買到取貨之間需要等候的情境中，yoboca 會在訂單備妥可供取貨時發送 LINE 通知。有了這些服務，使用者在被叫號之前可以自由地在咖啡廳放鬆或去辦其他事情，有助於減輕等候的壓力。

日常生活中有無數等待的時刻，每一個都帶來各自的壓力。我們將持續努力，運用 LINE 來減輕這些等候的壓力。

### Image 

![service image](https://developers.line.biz/media/line-mini-app/technicalcase/bravetechnology/en/bravetechnology_screenshot.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/line-mini-app/technicalcase/bravetechnology/en/bravetechnology_system_diagram.webp)

### Adopting AWS with future scalability in mind 

我們從「LINE de Junbanmachi」時代起便開始使用 AWS，採用雲端服務以便開發與營運都能由小型團隊處理。去年九月發布的 yoboca 採用無伺服器（serverless）架構。它建構於 AWS Lambda 與 Amazon SQS 等依用量計費的全代管服務之上，並結合 CI/CD 的自動化。此架構有助於降低營運與財務成本，同時為未來的成長提供可擴展的基礎。

### Aiming to deliver services that enhance marketing and customer loyalty through integration with other services 

最近，我們發布了能讓 matoca 與 yoboca 與 POS 系統、取票機及電子商務網站整合的 API。先前，這些服務各自獨立運作，但透過與 POS 系統等店內設備整合，便不需要額外的裝置，也能減少合作商家員工的操作步驟。除了與其他裝置及服務整合之外，我們也計劃進一步運用使用者行為資料，開發能強化合作商家行銷活動與顧客忠誠度的服務。

### A message for those developing new services 

如先前所述，LINE 是一個擁有極為龐大活躍使用者數量並提供多樣化 API 的平台。如同任何平台一樣，它有一定的限制，而開發者很自然地會想建構更靈活、更精緻的系統。然而，這樣的複雜度並不一定是使用者所追求的。我們鼓勵開發者專注於打造真正滿足使用者需求的服務，並據此選擇技術與平台。如果易用性是首要考量，善用 LINE Platform 會是一個有效的選擇。在這種情況下，我們建議將 LINE 列為您的選項之一加以考慮。

---

## Related links 

- [BraveTechnology inc.](https://bravetechnology.co.jp/)
- [matoca](https://junbanmachi.jp/)
- [yoboca](https://yoboca.jp/)
