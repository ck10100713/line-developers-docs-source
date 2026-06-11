# 隨需自動駕駛巴士預約系統的 LINE MINI App 案例研究（A LINE MINI App case study of an on-demand autonomous bus reservation system）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）移轉至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![BOLDLY Inc.](https://developers.line.biz/media/messaging-api/technicalcase/boldly/en/boldly_logo.webp)

**BOLDLY Inc.**

BOLDLY 致力於實現一個人人都能自由、平價且安全出行的世界。透過運用 IoT 與自動駕駛技術，BOLDLY 與全球各地的在地交通業者及車輛開發商合作，落實永續的公共交通解決方案。

## The service provider’s thoughts on developing the system 

我們將自動駕駛巴士設計成社區的「水平電梯」。

這套解決方案在有限的區域內提供低速且高頻率的移動服務，藉此提升居民的便利性。

在像是茨城縣境町這樣大片區域缺乏公共交通的城鎮，依固定班表行駛巴士以涵蓋整個區域，從成本與效率的角度來看並不實際。

因此，我們決定打造一套像計程車一樣的服務——一種你需要時就能輕鬆呼叫的服務。雖然市面上已經有許多隨需叫車應用程式，但我們選擇在擁有 9,200 萬名使用者（根據 LINE Corporation 調查；截至 2022 年 6 月底的 LINE app 每月活躍使用者數）的 LINE Platform 上開發這套系統。我們希望，如果可能不熟悉智慧型手機的年長居民能習慣使用 LINE，他們得到的將不只是一個巴士預約工具；他們還會獲得一種與家人和朋友保持聯繫的方式。我們相信，如果人們能從他們原本就在使用的 LINE app 呼叫自動駕駛巴士，而不必學習如何使用新的應用程式，這將給予他們更自由外出的信心。這也是為什麼我們將 LINE 官方帳號以角色「Sakai ARMA」命名。我們希望人們能像和朋友聊天一樣呼叫自動駕駛巴士。

### Image 

![service image](https://developers.line.biz/media/messaging-api/technicalcase/boldly/en/boldly_screenshot.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/boldly/en/boldly_system_diagram.webp)

### Optimizing operations by migrating to AWS 

由於我們既有的內部系統已經在 AWS 上運行，因此我們將 LINE 預約系統的基礎架構也建置在同一個平台上。

雖然最初的原型使用了 Google Apps Script 之類的工具，但隨著我們邁向全面的服務開發與營運，我們將整個基礎架構移轉至 AWS，以讓新服務的架構與資料管理與我們既有的系統一致。

透過移轉基礎架構，我們也得以最佳化營運，包括將建置流程（build pipeline）與既有系統整合。

### Running costs of cloud infrastructure 

除了以 API 為基礎的整合之外，Dispatcher 還仰賴多種通訊管道，包括從車載裝置傳輸影像與音訊，以及透過 WebSocket 即時交換遙測資料（telemetry data）。

因此，從服務開發的早期階段起，我們就明確打算使用雲端基礎架構，以降低與基礎架構管理及維護相關的成本。此外，隨著連線車輛數量增加、通訊量預期也會隨之成長，我們運用可隨服務成長輕鬆擴充的雲端基礎架構，得以有效率地管理資源。

### Exploring a boarding authentication system using facial recognition with data registered through LINE 

我們正在考慮更新乘車時的乘客驗證流程。

目前，乘客可透過向駕駛出示預約時所核發的 ID 來搭乘巴士。然而，隨著自動駕駛巴士朝向無人駕駛營運發展，這種做法有明顯的限制。

為了解決這項挑戰，我們正在開發一套以臉部辨識為基礎的乘客驗證系統。透過在乘車時使用攝影機，系統會根據透過 LINE 登錄的臉部資料，驗證乘客是否為當初進行預約的同一人。從營運效率的角度來看，我們也正在考慮更新預約系統，以實現共乘功能。

### A message for those developing new services 

在我們的服務中，使用者需要自行完成所有事項——從車輛預約到乘車驗證。對於這類 B2C 服務，開發者經常面臨與客戶溝通及客戶名單管理相關的挑戰。LINE Platform 提供多種功能來應對這些挑戰，包括透過聊天進行溝通，以及透過好友註冊進行客戶管理。藉由在我們的預約系統中運用這些功能，我們得以順利推進開發，未遇到重大障礙。如果你正在打造 B2C 服務，我們鼓勵你考慮使用 LINE Platform。

---

## Related links 

- [BOLDLY Inc.](https://www.softbank.jp/drive/)
