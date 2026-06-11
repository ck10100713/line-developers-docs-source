# 行動點餐系統 CX ORDER 案例研究（A case study of mobile order system CX ORDER）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![Classmethod](https://developers.line.biz/media/line-mini-app/technicalcase/classmethod/classmethod_logo.webp)

**Classmethod, Inc.**

Classmethod 以「為每個人賦予創造力（empower creativity for everyone）」為使命，在雲端、資料分析、行動、IoT、AI 與機器學習等多個領域提供技術支援。該公司也透過提供 LINE MINI App 開發服務，以及讓企業能建立行動點餐 LINE MINI App 的服務「CX ORDER」，協助企業善用 LINE。

## The service provider’s thoughts on developing the system 

雖然我們是一家 IT 公司，但我們也在秋葉原經營一間完全無現金的咖啡廳「[DevelopersIO CAFE](https://cafe.classmethod.jp/)」。\*

憑藉開發與營運各種線上銷售通路（例如 LINE、網站與原生 App）的經驗，我們推出了 [CX ORDER](https://cxorder.jp/lp/)，這是一項透過 LINE MINI App 提供行動點餐功能的雲端服務。

短期而言，我們的目標是協助企業（主要為餐飲業）透過擴展外帶通路，彌補因營業時間縮短或暫時歇業而流失的營收。中長期而言，我們希望提升營運效率、減少人力需求，並透過 LINE 支援持續性的使用者互動。

雖然行動點餐正受到關注，但它仍是一項創新的新服務，因此盡可能降低採用門檻至關重要。我們相信，透過善用 LINE，我們能提供順暢無阻的顧客體驗。

\*「DevelopersIO CAFE」已於 2022 年 12 月 20 日關閉。

### Image 

| Product List | Product Details | Order Confirmation | Order Complete |
| --- | --- | --- | --- |
| ![Product List](https://developers.line.biz/media/line-mini-app/technicalcase/classmethod/classmethod_screenshot_1.webp) | ![Product Details](https://developers.line.biz/media/line-mini-app/technicalcase/classmethod/classmethod_screenshot_2.webp) | ![Order Confirmation](https://developers.line.biz/media/line-mini-app/technicalcase/classmethod/classmethod_screenshot_3.webp) | ![Order Complete](https://developers.line.biz/media/line-mini-app/technicalcase/classmethod/classmethod_screenshot_4.webp) |

## System overview 

![System architecture diagram](https://developers.line.biz/media/line-mini-app/technicalcase/classmethod/classmethod_system_diagram.webp)

### Built primarily on AWS, with the adoption of Google Cloud also underway 

我們主要使用 AWS，這是我們最擅長的領域。使用者透過 Amazon CloudFront 存取各個 App 與 API。在核心功能方面，我們使用 Amazon ECS 與 Amazon Aurora，並設定了自動擴展（auto-scaling）以因應流量增加。

此外，我們也運用 Amazon DynamoDB 處理頻繁存取的資料，並使用 AWS Lambda 與 Amazon SQS。雖然 AWS 是我們的主要平台，但我們也已開始在某些功能上運用 Google Cloud。

### Ongoing cloud infrastructure and operational costs 

由於核心功能建構於 Amazon ECS 與 Amazon Aurora 之上，相較於完全無伺服器（serverless）的環境會產生一些額外成本。綜合考量導入成本與中長期營運成本後，我們認為目前的配置是合適的。不過，隨著情況的演變，我們也計劃探索各種選項，例如將特定功能遷移至無伺服器環境，或調整整體配置。

### Operational tools supporting the infrastructure 

我們使用 AWS CDK（TypeScript）進行基礎設施配置管理。由於 CX ORDER 的 App 與 API 都以 TypeScript 建構，工程師能無縫處理從基礎設施層到前端的所有環節。我們也導入了 Sentry 來監控 App 錯誤並發送通知至 Slack。當同一租戶（tenant）在短時間內發生多起事件時，我們會與客戶成功團隊（Customer Success Team）合作，了解客戶的情況並協助解決錯誤。我們使用 Google Analytics 追蹤使用者行為，並運用這些資料改善 App，以及建立用於訊息發送的使用者區隔（segment）。

### Aiming to boost sales, improve operational efficiency, and reduce labor needs at client stores 

我們的首要任務是為導入系統的門市提升營收、改善營運效率並減少人力需求。我們將持續透過收集更多客戶的意見回饋來新增與精進功能。此外，我們也藉由導入新功能與透過客戶成功的努力，並借助來自內部實驗的洞見，探索如何運用 LINE 促進客戶溝通。

### Requests for the LINE API 

LINE API 易於實作，並提供一組聚焦明確的核心功能，使其保持簡潔。隨著未來越來越多服務與 LINE 整合，維持這份簡潔性並確保穩定運作至關重要。在客戶理解方面，將 LINE 所持有的屬性資訊與服務所持有的資訊結合，將能實現更細緻的策略。

### A message for those developing new services 

使用 LINE API 與 SDK 有助於減少開發工作量。此外，透過採用 LINE 作為您的 ID 基礎架構，您可以降低使用者開始使用您服務的門檻。一旦使用者開始使用服務，您便能透過 LINE 官方帳號（LINE Official Account）持續溝通，將他們轉化為忠實顧客。這是另一項重要的好處。雖然不同通路各有其特性，但圍繞 LINE 建構您的服務能帶來顯著的效益。

---

## Related Links 

- [Classmethod, Inc. | LINE for Business](https://www.lycbiz.com/jp/partner/technology/line/classmethod/)
- [Classmethod, Inc.](https://classmethod.jp/english/)
- [CX ORDER](https://cxorder.jp/lp/)
