# 透過 CNAP 提升 LINE 服務開發效率的案例研究：為 LINE 服務開發導入基礎架構低程式碼

<!-- tip start -->

**關於本頁面**

本頁面收錄的文章是從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的內容。本頁面介紹採用 LINE Platform 企業的案例研究。請注意，文章內容反映的是發布當時所掌握的資訊。

<!-- tip end -->

![SoftBank Corp.](https://developers.line.biz/media/messaging-api/technicalcase/softbank/en/softbank-logo.webp)

**SoftBank Corp.**

SoftBank Corp. 經營涵蓋電信、雲端安全、AI 與機器人等廣泛領域的業務。SoftBank Corp. 期望透過資訊革命為所有人帶來幸福，進而成為「全世界最被需要的公司」，並將以既有的事業基礎為根基、運用數位科技的力量，致力於實現一個人人都能便利、舒適且安全生活的理想社會。

## What is CNAP and how does it shorten application development period? 

傳統的應用程式開發面臨以下挑戰。

- 開發與基礎架構維運由不同團隊負責，因此每次發布都必須提交變更請求，導致發布流程耗時更長。
- 開發與執行環境、設計慣例及政策缺乏一致性，難以確保適當的治理。
- 維運工作高度仰賴個人，且未經標準化，存在發生維運錯誤的風險。

這些挑戰可以透過遵循 DevOps 原則來解決，例如將建置與維運流程自動化，以及將系統設定標準化。然而，要在內部自行準備這樣的環境極為困難，因為涉及高昂的學習成本、需要投入大量時間累積技術專業，並且必須持續維護以跟上頻繁的版本更新。Cloud Native Application Platform（CNAP）是一項提供標準化且自動化平台的服務，匯整了 SoftBank 實踐的 DevOps 知識與經驗。CNAP 提供低程式碼的設定套件，其中設計已標準化、建置流程已自動化。透過維護與管理這些套件，客戶得以克服傳統挑戰，並專注於其核心開發工作。在本文中，我們將介紹一個使用 LINE Messaging API 開發詢問管理系統時運用 CNAP 的案例研究。

### Image 

![roadmap](https://developers.line.biz/media/messaging-api/technicalcase/softbank/en/softbank-overview-1.webp)

![cnap-benefits](https://developers.line.biz/media/messaging-api/technicalcase/softbank/en/softbank-overview-2.webp)

![about-cnap](https://developers.line.biz/media/messaging-api/technicalcase/softbank/en/softbank-overview-3.webp)

![service-image](https://developers.line.biz/media/messaging-api/technicalcase/softbank/en/softbank-overview-4.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/softbank/en/softbank-system-diagram.webp)

### Automated deployment to Azure environments using CNAP 

從前端到後端的所有基礎架構皆建構於 Azure 之上。我們提供支援公有雲平台的代管服務供應商（MSP）服務，涵蓋 Microsoft Azure、Google Cloud 與 Amazon Web Services（AWS）。透過在內部自行開發這些服務，我們已在公有雲平台方面累積了廣泛的專業知識。其中，Azure 是我們經驗最豐富的公有雲平台，因為我們早在 2019 年 10 月便開始提供 MSP 服務。因此，本專案我們選擇了 Azure。CNAP 讓使用者只需將以抽象化形式定義系統設定的 YAML 檔案推送至 Git 儲存庫，即可以統一的方式部署與管理 Kubernetes 環境及相關資源。Google Cloud 與 AWS 同樣受到支援。

### Performance and cost optimization using Azure Kubernetes Service 

由於應用程式運行於 Kubernetes 叢集上，Azure Kubernetes Service（AKS）佔了整體成本的最大部分。此外，由於叢集中的每個節點上可以放置多個 pod，只要節點資源足夠，就能將多個服務一同託管。再者，Kubernetes 能夠根據工作負載進行動態擴展。因此，此系統可依各服務的工作負載進行效能最佳化，同時將成本降至最低。

### Components of CNAP, including AKS 

CNAP 是一個透過緊密整合的 OSS 元件來支援基礎架構維運自動化的平台，這些元件圍繞著 AKS 等代管服務建構而成。我們採用 Helm 作為應用程式封裝平台，並使用 Flux CD 作為持續交付（CD）平台來實作 GitOps。此外，我們使用 Prometheus 與 Grafana 來監控應用程式的指標、日誌與錯誤。基於我們自身在應用程式開發與維運中累積的知識與經驗，CNAP 提供具備實績的 OSS 元件，並附帶建議的設定，讓客戶能夠以自助方式管理、維運與監控其系統。

### Future goals 

透過將應用程式基礎架構層抽象化並提供代管平台，CNAP 提供了一個讓客戶得以專注於應用程式開發的環境。我們相信，透過 CNAP 能夠支援各式各樣的應用程式開發專案，包括使用 LINE API 的應用程式。我們將持續擴展服務，並致力於更好地滿足客戶的需求。

### A message for those developing new services 

如前所述，LINE 擁有極為龐大的活躍使用者基礎。因此，在 LINE Platform 上提供的服務能夠觸及更廣泛的終端使用者。LINE 同時提供豐富的 API，讓開發者能透過不同的組合與創意，打造出各式各樣的應用程式。在開發應用程式時，敬請將 CNAP 納入考量選項。

---

## Related links 

- [Cloud-Native Application Platform（CNAP）](https://www.softbank.jp/biz/services/platform/msp-service/cnap/)
- [MSP Service](https://www.softbank.jp/biz/services/platform/msp-service/)
- [SoftBank Corp.](https://global.tm.softbank.jp/en/)
