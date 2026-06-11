# GDL 平台技術案例研究：同時兼顧成本效益與彈性（Technical case study of the GDL platform: achieving both cost-efficiency and flexibility）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）移轉至 LINE Developers 網站的文章。本頁呈現採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![grandream](https://developers.line.biz/media/line-mini-app/technicalcase/grandream/en/grandream-logo.webp)

**Grandream Inc.**

我們是一家具備高度技術能力與提案能力的系統開發公司，提供從網頁應用程式開發到基礎設施建置與營運的端到端支援。我們的核心專注領域在於運用 LINE 技術的應用程式開發，近年來尤其著重於 LINE MINI App。我們致力於成為引領您的事業邁向成功的夥伴。

## Service overview and the challenges we want to solve 

使用 LINE API 開發應用程式時，不僅需要針對特定商業問題建立解決方案，還必須建構通用功能。例如：好友的追蹤與封鎖狀態管理、付款、圖文選單（rich menu）以及一對一聊天等。因此，必須同時將開發預算分配給通用功能與商業解決方案，往往使得建構必要功能變得困難。為了解決這個問題，我們的 GDL Platform 提供混合式解決方案：我們以 SaaS 或套件形式提供通用功能，同時交付為解決您特定商業問題量身打造的系統。這種做法讓開發者能夠專注於建構關鍵功能。2023 年 5 月，我們發布了「MONSTER」應用程式的 beta 版，這是一項按月訂閱的服務，旨在保護兒童免於霸凌。這項服務代表了一個成功的案例研究，透過運用 GDL Platform 來進行使用者資訊管理與付款功能，成功降低了開發成本。

MONSTER 網站：[https://www.monster-line.com](https://www.monster-line.com)

### Image 

![service-overview](https://developers.line.biz/media/line-mini-app/technicalcase/grandream/en/grandream-service-img.webp)

![service-image](https://developers.line.biz/media/line-mini-app/technicalcase/grandream/en/grandream-ui-img.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/line-mini-app/technicalcase/grandream/en/grandream-system-dialog.webp)

### Utilizing system data in services 

我們會盡可能將使用者在 LINE 官方帳號（LINE Official Account）與 LINE MINI App 中的行為\*記錄到我們的資料庫，以便進行更細緻的分群（segment）管理。透過建立適當的分群，我們不僅能向使用者傳遞相關資訊，還能協助降低訊息傳送成本。

\*取得並運用與 LINE 帳號連結的行為資料時，需要使用者同意。

### Utilizing AWS for its diverse services 

我們多年來一直在 AWS 上進行開發，累積了豐富的基礎設施建置資產，包括基礎設施即程式碼（Infrastructure as Code，IaC）。AWS 的另一項優勢在於，由於其服務種類極為多元，我們能夠完全在該平台內完成所有所需的工作。

### Cloud infrastructure running costs 

我們 AWS 營運成本中有相當大的部分來自於「持續運行（always-on）」的服務，例如 Amazon Elastic Compute Cloud（「AWS EC2」）、Amazon Elastic Container Service（「AWS ECS」）、Amazon ElastiCache（「AWS ElastiCache」）以及 Amazon Relational Database Service（「AWS RDS」）。雖然我們提供兩種標準環境——用於功能驗證的測試（staging）環境，以及用於營運正式服務的生產（production）環境——但我們特別著重於降低開發環境的營運成本。以下是我們降低成本措施的三個範例。

第一個是 AWS EventBridge，我們在測試環境與生產環境中都使用它。AWS EventBridge 是一項無伺服器（serverless）服務，透過使用事件來連接應用程式元件，實現事件驅動架構。事件驅動架構讓我們能夠建構鬆散耦合的軟體系統，這些系統藉由發出事件並對事件做出回應而協同運作。這提升了敏捷性，並有助於建構高度可靠且可擴展的應用程式。對於我們的服務，我們使用 AWS EventBridge 排程器來執行腳本，在非必要的開發時段自動停止服務。

第二個是 AWS ECS。AWS ECS 是一項全託管的容器編排服務，讓部署、管理與擴展容器化應用程式變得容易。營運成本在很大程度上取決於所選擇的資源與使用量。為了降低成本，我們利用「Fargate Spot」，這是 AWS 提供的一種以成本效益為優先的容器工作負載執行選項。

第三個是 AWS ElastiCache。AWS ElastiCache 是一項託管服務，讓設定、管理與擴展分散式記憶體內快取環境變得容易。這項服務提供高速的記憶體內快取，以改善應用程式效能。由於從記憶體內快取擷取資料的速度遠快於從資料庫擷取，因此快取經常存取的資料能顯著縮短應用程式的回應時間，提升應用程式效能並降低資料庫負載。成本取決於多項因素，包括傳輸的資料量以及執行個體運行的時間長度。對於開發環境，我們透過在 AWS EC2 上建構 Redis 執行個體，而非使用 AWS ElastiCache，來降低成本。

### Operational tools that support our infrastructure 

我們採用 AWS Cloud Development Kit（「AWS CDK」）作為支援基礎設施的 IaC 解決方案。由於 AWS 基礎設施可以使用程式碼建構，這讓我們能夠以程式化方式管理 AWS 資源。此外，我們採用 TypeScript 作為 AWS CDK 所使用的語言。這讓我們能夠充分運用開發工具（VS Code）中的型別推論與型別檢查功能，使編碼更有效率，並確保在執行前就能捕捉到拼字錯誤。同時，由於基礎設施是以程式化方式定義，我們可以輕鬆為不同環境（包括測試與生產環境）配置不同的設定。雖然我們過去有使用各種工具建構 AWS 環境的經驗（例如 CloudFormation 範本與 Terraform），但我們目前認為 AWS CDK 是現有最佳的工具。

### Future goals 

由於我們向各種不同的企業提供 GDL Platform，我們持續擴展其功能。我們希望確保現有的客戶也能從這些持續性的強化中受益。

---

## Related links 

- [Grandream Inc.](https://www.grandream.jp/)
- [GDL Platform](https://www.grandream.jp/services/gd-l-pf)
