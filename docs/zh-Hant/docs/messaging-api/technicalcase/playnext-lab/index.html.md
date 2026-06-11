# Smart Public Lab 技術案例研究：支援行政數位轉型的 LINE 運用策略（Technical case study of Smart Public Lab: LINE utilization strategy supporting administrative digital transformation）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時可取得的資訊。

<!-- tip end -->

![Playnext Lab Inc.](https://developers.line.biz/media/messaging-api/technicalcase/playnext-lab/en/playnext-lab-logo.png)

**Playnext Lab Inc.**

我們成立於 2016 年，秉持「以技術與多樣性打造未來」的願景營運，並提供包括智慧型手機遊戲、HR tech 服務、聊天機器人系統開發等廣泛的服務。近年來，我們也致力於提供連結政府與市民的 GovTech 服務。憑藉著由來自 17 個國家的成員所組成的全球工程師團隊的開發能力，我們努力發展自有服務，並期望透過尖端技術支援社會與客戶雙方的數位轉型。

## Service overview and the challenges we want to solve 

Smart Public Lab 是一項在提升居民滿意度的同時，支援地方政府職員作業效率的服務。Smart Public Lab 以「Smart Public Lab with LINE SMART CITY GovTech Program」（可透過 LINE 帳號以簡單易用的方式，實現行政服務新世代數位轉型）與線上申請服務為核心，作為地方政府的綜合性數位接觸點。它消除了親自前往、在服務櫃檯等候，以及紙本作業流程的需求，目前已透過全日本約 100 個地方政府的 LINE 官方帳號（LINE Official Account）使用中。

Smart Public Lab GovTech Program 提供一套廣泛的功能，包括文件與表單製作、可進行細緻條件設定的分眾資訊發送、進階情境式聊天機器人訊息、公共設施與活動的行事曆預約、為緊急應變最佳化的災害模式、以地點為基礎的景點搜尋，以及付款功能。這些能力超越了標準 LINE 官方帳號功能所能提供的範圍。Smart Public Lab 的線上申請服務支援需要使用 My Number Card 進行身分驗證的申請，以及便於支付核發費用與行政規費的線上付款。它也支援連接 LGWAN（Local Government Wide Area Network，地方政府廣域網路），讓既有的政府配發電腦可以使用，並將導入負擔降至最低。Smart Public Lab 的 Tourist Guide 服務讓地方政府得以開發觀光導覽服務，客製化景點搜尋功能並運用觀光網站的內容，透過觀光專用的 LINE 官方帳號將相關資訊傳遞給非居民使用者。聊天機器人從 LINE 聊天畫面引導使用者，並能依不同的使用情境提供量身打造的景點推薦。

服務可根據使用者目前的所在位置或所選的區域，依歷史、美食或住宿等類別顯示相關設施。由於已與 Google Maps 連動，另一項吸引人的特色是使用者可以快速查看所選景點的路線與詳細資訊。

### Image 

![service-image](https://developers.line.biz/media/messaging-api/technicalcase/playnext-lab/en/playnext-lab-ui-img.png)

## System Overview 

![System architecture diagram](https://developers.line.biz/media/messaging-api/technicalcase/playnext-lab/en/playnext-lab-system-diagram.png)

### Improving administrative services using acquired data 

透過行政 DX 系統，居民問卷調查可從紙本轉移至 LINE，藉由資料數位化提升作業效率。此外，可根據居民的出生日期發送癌症篩檢通知，並可透過 LINE 進行癌症篩檢的預約。\* 透過讓居民在 LINE 上登錄他們希望收到的資訊類型，便能將資訊傳遞給特定的分眾。因此，LINE 被廣泛用於向各年齡層居民傳達行政資訊的管道。

\*與 LINE 帳號連動的行為資料僅在取得使用者同意後才會被蒐集與使用。

### Background to selecting AWS for system construction 

我們採用 Amazon Web Services（以下簡稱「AWS」）來建構行政 DX 系統。由於行政服務與市民的日常生活直接相關，系統必須隨時穩定運作，並提供能因應存取量突然激增的擴展性。AWS 提供了符合這些需求的高效能。此外，在處理行政資料時，安全性是最關鍵的考量之一。AWS 提供穩固的安全措施與豐富的合規認證，為機密資訊的安全管理提供了可靠的環境。

營運與維護的便利性也是選擇的因素之一。AWS 提供一套廣泛的工具與服務，可簡化管理與維護、減輕營運負擔，並能迅速改善服務。我們在使用 AWS 方面擁有豐富的經驗，並累積了充分運用該平台所需的專業知識。基於這些原因，我們採用了 AWS。我們定期使用 AWS Billing and Cost Management 檢視基礎設施的運行成本，並分析諸如各使用者使用頻率等趨勢。在開發過程中，我們使用 GitHub 進行原始碼管理，因為它易於管理。

### Future outlook for municipal digital service counters 

作為行政 DX 措施的一環，Smart Public Lab 致力於擴展能解決居民與地方政府職員所面臨之挑戰的功能範圍，藉此擴大地方政府數位服務櫃檯所提供的支援範疇。

2023 年 1 月，我們推出了可在 LINE 官方帳號上進行 My Number Card 驗證的線上申請服務。在福岡縣大川市，有 96% 的生育與育兒支援津貼申請是透過其 LINE 官方帳號受理的（PlayNext Lab Inc. 調查），為居民提供了高度易用的系統。雖然高度功能化的系統往往會變得更難以操作，但 Smart Public Lab 是專為地方政府而設計的。我們始終致力於提供高度著重於 UI 與 UX 的服務，確保居民與職員都能持續以直覺且簡單的方式使用本系統。

### Requests for LINE API development 

我們認為，若能提供可取得使用者所在位置資訊與「已讀」狀態的 API，將能進一步擴展可在 LINE 上提供的服務範圍。

### A message for those developing new services 

LINE 最大的優勢之一在於其壓倒性的使用者基礎與高度的活躍使用者比率，使我們得以觸及所有年齡層的使用者。透過運用 LINE 驗證，Smart Public Lab 的預約功能消除了使用者註冊的需求。

事實上，有 54% 的諮詢預約（PlayNext Lab Inc. 調查）是透過 LINE 完成的。運用 LINE API 協助我們擴展了使用者觸及範圍並減少了使用者流失，使我們得以開發出有助於降低行銷與成長駭客相關成本的系統。

---

## Related links 

- [Smart Public Lab](https://www.playnext-lab.co.jp/govtech/)
