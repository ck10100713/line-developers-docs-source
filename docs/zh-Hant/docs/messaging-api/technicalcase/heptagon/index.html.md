# 開發處理搬遷與定居相關諮詢的 LINE 機器人案例研究

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹了採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![heptagon inc.](https://developers.line.biz/media/messaging-api/technicalcase/heptagon/en/heptagon-logo.webp)

**heptagon inc.**

身為 AWS 進階諮詢合作夥伴（AWS Advanced Consulting Partner），我們主要為位於日本東北地區的企業提供雲端導入支援。我們也積極推動東北地區企業的數位轉型（DX）。透過與那些希望藉由採用先進技術與新思維來成長的企業合作，heptagon inc. 為提升生產力、改善營運流程以及導入新工作型態做出貢獻。

## The service provider’s thoughts on developing the system 

在 COVID-19 疫情期間，由於已無法舉辦實體活動，三澤市（Misawa City）向我們提出需求，希望打造一套線上系統，讓民眾能夠諮詢搬遷與定居相關事宜。由於這項專案是在會計年度進行到一半時才啟動的，預算有限，因此必須開發一套能讓盡可能多的人使用、同時將市政府工作人員營運負擔降到最低的系統。

為了滿足這些需求，我們很快就達成以下開發方針的共識：

- 使用民眾早已廣泛使用的平台 LINE 作為介面
- 針對可預期的諮詢，運用 AI 提供自動回覆
- 採用可以小規模起步的無伺服器（serverless）架構，以壓低營運成本
- 透過運用雲端供應商所提供的 API 與 SaaS 等雲端原生（cloud-native）技術，而非從零開始打造一切，藉此減少開發工時
- 讓上線後的營運能主要由市政府工作人員自行處理，而不需依賴外部廠商

我們將這項專案視為運用自身技術優勢來支援地方政府的絕佳機會，因此決定著手推進這項專案。

### Image 

![service-image](https://developers.line.biz/media/messaging-api/technicalcase/heptagon/en/heptagon-screenshot.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/heptagon/en/heptagon-system-diagram.webp)

### Achieving minimal development hours and operating costs with AWS 

我們將我們的核心專長領域 AWS 置於 API 後端的核心位置。在管理介面方面，我們採用了能輕鬆建立 AI 聊天機器人的 Azure QnA Maker，以及市政府工作人員早已熟悉的 Google Sheets。為了確保專案維持在核准的預算範圍內，我們將開發工時降到最低，並組合運用各項服務，以避免服務上線後使用費用與營運成本上升。

### Ongoing cloud infrastructure and operational costs 

後端運算環境採用以 AWS Lambda 為核心的無伺服器架構。電子郵件寄送、資料庫與儲存空間皆透過完全託管（fully managed）的按用量計費（pay-as-you-go）服務提供。這種做法消除了固定的基礎設施成本，並將持續性的營運成本維持在低點。以目前的規模而言，這些服務多數都在各自的免費額度（free tier）範圍內運作。

### Operational tools supporting the infrastructure 

Serverless Framework（部署與設定管理）／ CloudWatch（監控）／ Zabbix（監控）

### Solving local challenges with the LINE API 

雖然 LINE 官方帳號（LINE Official Account）在地方地區早已廣泛使用，但運用 LINE API 能大幅擴展所能提供的服務範圍。我們的目標是透過運用 LINE 的服務，解決地方社群所面臨的各項挑戰。

### A message for those developing new services 

透過運用 LINE 生態系，開發者能為使用者提供易於使用且熟悉的介面，同時大幅減少開發工時。此外，將 LINE 與企業的核心競爭力整合，能創造更多機會，向廣大受眾提供易於取用的服務。我們相信，將 LINE 納入開發選項之一，會是一項強而有力的策略優勢。

---

## Related links 

- [heptagon inc.](https://heptagon.co.jp/)
