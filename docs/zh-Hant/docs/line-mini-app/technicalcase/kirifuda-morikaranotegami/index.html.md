# 寓教於樂的自然保育：在 LINE MINI App 上推出的「來自森林的信」技術案例研究

<!-- tip start -->

**關於本頁**

本頁包含自 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發佈當時可取得的資訊。

<!-- tip end -->

![KIRIFUDA Inc.](https://developers.line.biz/media/line-mini-app/technicalcase/kirifuda-morikaranotegami/en/kirifuda-morikaranotegami-logo.png)

**KIRIFUDA Inc.**

我們是 KIRIFUDA Inc.（以下簡稱「KIRIFUDA」），一家支援區塊鏈（blockchain）實際落地應用的解決方案供應商與系統開發商，以「打造一個讓創意與價值能透過 Web3 流通的社會」為使命。我們為日本國內外的企業提供從商業策略諮詢到系統開發的一站式服務，協助他們建構 Web3 時代的商業基礎。

## Service overview: "Letters from the Forest", a LINE MINI App for logging environmental actions 

「來自森林的信」是一款用於記錄環境行動的 LINE MINI App，由東急不動產（Tokyu Land Corporation）與 KIRIFUDA 共同導入至長野縣的 Resort Town Tateshina（蓼科度假村）。訪客會參與各種具環境意識的行動，例如自備個人盥洗用品以減少消耗、不更換床單，或參加森林保育計畫以加深相關知識。這些行動會以區塊鏈上發行的 NFT 來呈現。當使用者掃描設置於現場的木雕 QR code 時，會自動加入 LINE 官方帳號為好友並啟動 LINE MINI App。點選「領取 NFT」按鈕後，會啟動一段動畫，將數位印章置入使用者帳號中。透過 LINE 官方帳號的圖文選單（rich menu），使用者隨時都能進入自己的 My Page 查看已收集的印章，並在累積到所需數量後兌換成可於設施內使用的優惠券。此設計藉由採用日本「集點活動（poi-katsu）」文化的元素，將環境貢獻遊戲化。

東急不動產在全公司範圍內致力於投入去碳化（decarbonization）並推動森林保育計畫。值得注意的是，Resort Town Tateshina 的森林是必須透過適當疏伐與保育管理才能永續維持的區域資源。然而，僅僅要求訪客「以環境友善的方式行動」，對於激發主動參與的效果有限。因此，需要一種結合「學習與樂趣」的數位內容。此外，這些行動最終可能會彙整成碳權（carbon credits）。在此過程中，維持每位訪客環境貢獻的真實紀錄至關重要。為了滿足這項對可驗證證明的需求，KIRIFUDA 提議以 NFT 作為一種具防篡改性的方法來記錄個人的行動紀錄。透過 NFT，數位印章等視覺內容可與活動資料整合在一起，創造出一種引人入勝的體驗，讓訪客在享受收集印章樂趣的同時，也能切實感受到自己對環境的貢獻。從企業的角度來看，此系統能確保資料被安全地儲存，並為這個專案可靠地追蹤。

### Image 

![service-image](https://developers.line.biz/media/line-mini-app/technicalcase/kirifuda-morikaranotegami/en/kirifuda-morikaranotegami-ui-img.gif)

## System overview 

![System configuration diagram](https://developers.line.biz/media/line-mini-app/technicalcase/kirifuda-morikaranotegami/en/kirifuda-morikaranotegami-system.png)

### Technical configuration of "Letters from the Forest": Seamless integration of LIFF and blockchain 

在客戶端，我們以 LIFF 作為基礎；而在伺服器端，我們實作了與 LINE Login 基礎架構連動的使用者驗證，以及透過 Messaging API 的訊息傳送功能。  
我們使用 Web3Auth 來產生錢包（wallet），並使用 Alchemy 來鑄造（minting）與查詢 NFT。鑄造流程透過 Google Cloud Tasks 以非同步佇列（asynchronous queues）處理。為確保使用者體驗順暢、不受區塊鏈特有延遲的影響，所有耗費資源的後端流程都會送入佇列，讓使用者能不中斷地繼續操作。透過運用 LINE Login 工作階段（session），此系統的設計能安全地追蹤每位使用者的環境活動歷程與 NFT 持有情況。

為了在 LINE MINI App 環境中執行區塊鏈操作，嚴格遵循 LIFF 特定的初始化流程至關重要。由於 LINE MINI App 是在 LINE 內的嵌入式檢視（embedded view）中載入，因此涉及多階段的初始化流程。這需要一種設計，能在所有必要條件都滿足的確切時機，觸發區塊鏈操作——例如錢包產生與 NFT 鑄造，這些操作需要與 LIFF 分開進行各自的初始化。即使是些微的時機誤差，也可能導致初始化失敗，或讓使用者看到空白畫面，嚴重損害使用者體驗。因此，這項實作要求極為精準的精確度。

此外，與獨立的原生 App 不同，LINE MINI App 的真正價值在於它與聊天畫面、圖文選單等既有功能的無縫整合。舉例來說，我們必須細緻地設計以 LINE 使用者流程為核心的互動情境——例如在 NFT 鑄造完成後立即透過 Messaging API 傳送確認訊息，或引導使用者從聊天室的按鈕啟動 MINI App 並鑄造 NFT。我們最大的挑戰並不僅僅在於整合各項技術，而是在於打造一種對使用者而言自然流暢的體驗。這需要在前端工程與產品規劃兩方面持續發揮巧思。

### Initial feedback and operational reality 

Resort Town Tateshina 位於森林地帶，部分地點的行動電信涵蓋範圍有限，但這並未對使用者體驗造成顯著阻礙。在營運方面，KIRIFUDA 完整地管理 LINE 官方帳號，只請當地工作人員設置木雕 QR code 並向訪客提供基本的引導。由於整個流程與既有的度假村獎勵計畫非常相似，使用者與工作人員都能在毫無困惑的情況下享受這項體驗。

關於推出後所發現的改善之處，部分使用者覺得將 NFT 印章兌換成優惠券的流程令人困惑。我們目前正在優化 UI，並改善獎勵兌換畫面上的說明，讓兌換流程更直覺、更順暢。另一方面，我們也收到了大量正面的回饋，使用者表示他們「在毫無察覺這是 NFT 的情況下就收到了物品」、「印章設計太可愛了，讓人想收集」，以及「邊玩邊學環境知識很有趣」。本專案也獲得 TV Tokyo 節目報導，東急不動產更高度讚賞訪客在「不知不覺中為環境做出貢獻」這種讓人有真實感受的方式。

### Future outlook: Building a cross-sector environmental contribution program 

我們的目標是將環境貢獻優惠券從蓼科的「來自森林的信」擴展到東急不動產旗下的其他都市設施。透過建構一套讓森林貢獻證明能在各種地點兌換的系統——例如 SHIBUYA FUKURAS、代官山的飯店或其他商業設施——我們能在度假村與都市據點之間創造出雙向的顧客互動流動。舉例來說，在東京某間咖啡廳採取的環境友善行動（如使用環保袋）便能換得可在蓼科兌換的小型優惠。這種集團全體層級的誘因設計，旨在持續鼓勵環保行為，並提升整個東急集團生態系中以永續性為核心的使用者體驗。

這項整合 LINE MINI App 與 NFT 技術的服務，其應用範圍不僅限於環境貢獻，也可適用於任何忠誠度計畫（loyalty program）。近年來，在音樂與運動等由粉絲驅動的產業中，透過 NFT 來記錄並視覺化粉絲的參與和社群分享的趨勢日益興盛。透過將 LINE 官方帳號個人化的一對一溝通功能與可作為數位商品販售及收藏的 NFT 結合，我們能達成比傳統電商或社群媒體平台更深層的粉絲互動。展望未來，KIRIFUDA 的目標是在這個領域擴展技術驗證與合作夥伴關係，為能在 LINE Platform 上無縫銜接數位與實體世界的 Web3 計畫樹立新的標準。

### A message for those considering using LINE API 

最後，對於開發者與企劃人員而言，運用 LINE API 最大的優勢在於能透過單一平台，無縫觸及日本超過 9,700 萬名 LINE 使用者作為潛在用戶。除了標準的 LINE 官方帳號與 LINE MINI App 之外，此平台正以連接線上與線下體驗的功能快速演進，例如 eKYC 整合與透過 LINE Beacon 的推播通知（push notifications）。正如本專案所展示的，只要將體驗設計成讓使用者能直覺地開始使用，將區塊鏈與 NFT 整合至 LINE，便能大幅降低進入 Web3 的門檻。在 KIRIFUDA，我們已設計出融合 LINE 多樣化 API 與區塊鏈技術的服務。如果您對於想透過 LINE 達成什麼有任何想法，或對於運用 Web3 實現新型態使用者體驗有任何願景，歡迎隨時與我們聯繫。讓我們攜手在 LINE Platform 上打造次世代的使用者體驗。

---

## Related links 

- [KIRIFUDA Inc.](https://kirifuda.io/)
