# 「PoHUNT」開發案例研究：富山縣朝日町促進移動與健康的數位活化計畫（A development case study of "PoHUNT," a digital revitalization initiative for mobility and health promotion in Asahi Town, Toyama Prefecture）

<!-- tip start -->

**關於本頁**

本頁包含從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。本頁介紹採用 LINE Platform 的企業案例研究。請注意，文章內容反映的是發布當時所掌握的資訊。

<!-- tip end -->

![HAKUHODO Inc.](https://developers.line.biz/media/line-mini-app/technicalcase/hakuhodo/en/hakuhodo_logo.webp)

**HAKUHODO Inc.（博報堂股份有限公司）**

博報堂股份有限公司創立於 1895 年，秉持「生活者洞察（Sei-katsu-sha Insight）」與「夥伴關係的承諾（Commitment to Partnership）」這兩項至今不變的理念，持續每日追求創新。我們由高度創意的專業人才組成團隊，協同合作支援客戶解決各領域的挑戰——不僅是廣告，還包括經營、事業開發與社會議題。近年來，我們也致力於地方活化與推動數位轉型，啟動了專注於解決社會議題的專案。

## The service provider's thoughts on developing the system 

日本許多地方政府正面臨交通業者因人口高齡化與人口外流而退出的問題。隨著居民的交通選擇減少，外出次數也隨之降低，進而引發各種問題，例如城鎮經濟活動衰退、交流機會減少，以及高齡者健康狀況惡化。為了解決這些問題，富山縣朝日町開發了「PoHUNT」，這是一項旨在鼓勵居民移動的社區活化計畫。在 LINE MINI App 上，使用者可以透過掃描設置於商業設施的 QR code，以及瀏覽健康相關資訊來累積點數。這些點數可用於參加抽獎或地區性競賽，打造出一套將移動與健康相關活動遊戲化的機制。透過與 2020 年推出的共乘式公共交通服務「Nokkaru Asahimachi」整合，本計畫得以同時提供交通選擇並創造交通需求，以達到活化城鎮的目標。

### Image 

![](https://developers.line.biz/media/line-mini-app/technicalcase/hakuhodo/en/hakuhodo_screenshot.webp)

## System overview 

![System architecture diagram](https://developers.line.biz/media/line-mini-app/technicalcase/hakuhodo/en/hakuhodo_system_diagram.webp)

### Using AWS for its comprehensive functionality and ease of maintenance 

我們採用了 Evolany Co., Ltd. 提供的服務 anybot 來實作 PoHUNT。服務基礎架構主要使用 AWS（Amazon Web Services）EC2，原因有以下兩點。

**全面的功能**

- AWS 在為服務新增核心功能時，能夠順暢地整合，例如資料庫、通知功能（電子郵件與簡訊）以及儲存空間。

**基礎架構維護的便利性**

- 透過利用雲端基礎架構，維護流程可以輕鬆地自動化與管理。

### Ongoing cloud infrastructure and operational costs 

在傳統的地端（on-premises）基礎架構管理中，會產生各種成本，包括設備費用與實體空間。相較之下，雲端基礎架構（AWS）採用按用量計費（pay-as-you-go）的模式，僅針對實際使用的部分產生費用，大幅降低營運成本。此外，基礎架構可以依據服務的規模與大小，輕鬆且快速地擴充或調整，使營運成本能控制在合理的水準。

### Operational tools supporting the infrastructure 

CloudWatch（監控）/ Zabbix（監控）

### Linking with the municipality's LINE Official Account to revitalize the entire town 

作為城鎮發展工作的一環，我們也透過 PoHUNT 發送居民問卷調查，而高回收率驗證了它作為城鎮發展平台的成效。基於這些成果，我們計畫以 PoHUNT 的點數功能為核心，推動地方政府的數位轉型計畫。透過與地方政府的 LINE Official Account 連動，並定期推出各項計畫，我們希望將此解決方案不僅應用於商業與健康相關領域，更能橫跨廣泛的各個領域，最終活化整座城鎮。此外，基於從本案例中獲得的洞察，我們也正在考慮將其應用於其他地方政府與企業的行銷計畫。

### A message for those developing new services 

我們認為不必為每個 OS 或版本分別開發是一項優勢，這讓初期開發與營運的工作量得以維持在較低的水準。此外，由於博報堂的主要角色是服務開發而非系統開發，因此我們在設計服務時，會高度聚焦於如何讓使用者真正能夠使用，以及如何在有限的預算內維持服務。對於重視這些觀點的企業與組織而言，LINE 被各個年齡層廣泛使用、且帳號營運免費這兩點極具吸引力。

---

## Related links 

- [Toward a "Community Revitalization DX" That Everyone Can Participate In — A New Platform for Regional Co-Creation, "PoHUNT" (Part 1)](https://seikatsusha-ddm.com/article/12588/)
- [Toward a "Community Revitalization DX" That Everyone Can Participate In — A New Platform for Regional Co-Creation, "PoHUNT" (Part 2)](https://seikatsusha-ddm.com/article/12596/)
- [Nokkaru](https://www.hakuhodo.co.jp/news/info/94130/)
- [HAKUHODO Inc.](https://www.hakuhodo-global.com/)
