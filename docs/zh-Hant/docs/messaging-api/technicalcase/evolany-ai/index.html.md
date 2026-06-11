# anybot for ChatGPT 的技術案例研究：充分運用 ChatGPT 達成更順暢的溝通

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![Evolany Co., Ltd.](https://developers.line.biz/media/messaging-api/technicalcase/evolany_ai/en/evolany_ai_logo.webp)

**Evolany Co., Ltd.**

Evolany Co., Ltd. 是一家由 Song Yu 與 Christian Forestell 於 2018 年在日本創立的 IT 新創公司。我們以「將數位轉型（DX）的效益帶給在地店家經營者」為座右銘，致力於運用數位技術為各類企業解決問題，並連續四年達成超過 200% 的年度高速成長。截至 2022 年 11 月，我們已支援超過 3,500 家企業。

## Development background of anybot for ChatGPT 

「anybot for ChatGPT」運用 ChatGPT，依據預先訓練的資訊為使用者的查詢提供 AI 驅動的回覆。促進內部溝通並推動與顧客的交流需要高昂的成本，使其成為一個極具挑戰、難以找到根本解決方案的領域。然而，ChatGPT 的問世讓系統能夠精準解讀自然語言，並在無須人工介入的情況下，將內容彙整為易於理解的回覆並加以傳達。我們善用這項潛力，決定導入能促進並推動溝通的功能至 anybot 中。另一方面，ChatGPT 也存在若干限制，包括無法管理對話歷史、無法保留新取得的資訊，以及無法存取最新資料（截至 2023 年 11 月，ChatGPT-3 的知識截止點為 2021 年 9 月）。這些限制經常被視為企業導入速度緩慢的原因。因此，我們決定運用至今透過提供聊天機器人所累積的專業知識，提供一項能彌補 ChatGPT 弱點的安全服務——這便促成了「anybot for ChatGPT」的開發。

### Image 

![service-image](https://developers.line.biz/media/messaging-api/technicalcase/evolany_ai/en/evolany_ai_overview_1.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/evolany_ai/en/evolany_ai_system_diagram.webp)

### Customer support system using AWS and ChatGPT 

在選擇基礎架構時，我們挑選了符合特定需求的服務。我們採用 Amazon Simple Storage Service（AWS S3）來管理大量的訓練資料，例如 PDF 檔案。此外，我們使用 Amazon Elastic File System（AWS EFS）為處理過程中經常需要的檔案提供高速且安全的存取。這項檔案儲存服務允許多個 Amazon Elastic Container Service（以下簡稱「AWS ECS」）執行個體同時存取，例如用於搜尋已處理的訓練資料。

我們採用 AWS ECS 來託管應用程式。其目的在於透過簡便的更新管理，以及依據存取數量與負載狀況進行擴大或縮減的能力，確保穩定的服務交付。此外，我們導入 ChatGPT（OpenAI）來進行問答工作。這項 AI 工具能運用自然語言處理回應使用者的詢問。ChatGPT（Azure OpenAI Service）也用於類似目的，以服務那些已熟悉 Azure 環境，或希望運用 Microsoft Azure 安全功能的企業。

### Improving infrastructure operation efficiency and enhancing security with AWS 

Amazon CloudWatch（以下簡稱「AWS CloudWatch」）與 Amazon Elastic Container Registry Service（以下簡稱「AWS ECR」）在我們的基礎架構營運中扮演重要角色。我們使用 AWS CloudWatch 進行日誌管理。這項工具是用於監控與分析由基礎架構及應用程式所產生之日誌資料的強大服務。我們選擇 AWS CloudWatch，是看中其收集與監控即時資料的能力，讓我們得以追蹤系統效能並在必要時迅速回應。它在快速偵測非預期的系統問題或安全漏洞、進而採取有效對策方面，也扮演著關鍵角色。同時，我們使用 AWS ECR 進行更新管理。AWS ECR 是一項管理並安全儲存容器化應用程式映像檔的服務。我們選擇這項工具主要是為了簡化並精簡應用程式的更新流程。使用 AWS ECR 可促進容器映像檔的版本控制，並實現從開發到部署的一致工作流程。這些營運工具支援基礎架構效能監控與更新流程的效率，在強化系統的安全性與保障方面扮演重要角色。

### Future outlook 

雖然許多與 AI 相關的服務都有陡峭的學習曲線，但我們致力於提供能讓使用者盡可能輕鬆達成目標的服務。我們了解部分使用者對於 ChatGPT 的安全性與穩定性仍有疑慮。秉持我們既有的做法，我們將持續維護能發揮其優勢、同時彌補其弱點的服務。

### Requests for the LINE API 

語言生成式 AI 具有逐一產生 token 而非一次產生全部內容的特性。因此，完整文字的生成需要一些時間。所以，從 UI/UX 的角度來看，我們認為串流（stream）回覆並顯示內容的能力，對於實際應用而言將變得至關重要。我們樂見 LINE Platform 未來能支援傳送內容的串流功能。

### A message for those developing new services 

我們相信生成式 AI 服務正處於新時代的開端。雖然這個領域仍然複雜，技術快速演進、法規環境也持續變動，但我們對於能與其他開發者一同推動生成式 AI 服務的進步感到興奮。

---

## Related links 

- [Evolany Co., Ltd.](https://evolany.com/en/)
- [anybot](https://anybot.me/campaign)
- [anybot for ChatGPT](https://chatgpt.anybot.me/)
