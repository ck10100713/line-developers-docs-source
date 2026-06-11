# 原生 App 與 LINE MINI App 的差異（The differences between native apps and LINE MINI Apps）

<!-- tip start -->

**關於本頁**

本頁收錄了從 LINE API Use Case 網站（已於 2026 年 3 月 31 日關閉）遷移至 LINE Developers 網站的文章。請注意，文章內容反映的是發布當下所提供的資訊。

<!-- tip end -->

LINE MINI App 是在 LINE app 內的 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中執行的網頁應用程式。由於透過網頁應用程式所能提供的相同使用者體驗與功能，同樣可以用 LINE MINI App 來實作，因此 LINE MINI App 已被廣泛應用於各式各樣的服務。當企業考慮透過數位通路提供服務時，LINE MINI App 與原生 App 常被拿來作為可能的提供方式互相比較。

LINE MINI App 的目的，是直接在 LINE 上提供諸如行動點餐、數位會員卡、預約管理等服務，使其能在 LINE 環境中實現幾乎等同於原生 App 的功能。企業可以將 LINE 官方帳號（LINE Official Account）與 LINE MINI App（用於透過企業與使用者之間的訊息往來及優惠券發放來提升回訪率）相互結合，並搭配 LINE Login、LINE 通知訊息（LINE notification messages）等其他 LINE API，藉此擴大服務的範疇。

在本文中，我們會比較 LINE MINI App 與原生 App，並介紹 LINE MINI App 的優點、特色與成本。

![](https://developers.line.biz/media/basics/native-mini/en/native-mini-img-8.webp)

<!-- table of contents -->

## Experiences that can be realized with LINE MINI Apps 

我們從三個面向比較 LINE MINI App 與原生 App 的差異：使用門檻、通知送達率，以及留存率。比較結果如下所示。原生 App 的使用門檻較高，通知送達率與留存率較低；而 LINE MINI App 的使用門檻較低，通知送達率與留存率則較高。

![](https://developers.line.biz/media/basics/native-mini/en/native-mini-img-1.webp)

### 1. Barrier to use 

對於已經在使用 LINE 的使用者來說，LINE MINI App 與 LINE 官方帳號可以輕鬆存取，無需額外下載 App。相較之下，原生 App 的進入門檻高出許多，從必須下載 App 本身就開始了。例如在門市情境中，若要求使用者當場下載 App 並完成會員註冊，其難度與 LINE MINI App 相比明顯高出許多。

![](https://developers.line.biz/media/basics/native-mini/en/native-mini-img-2.webp)

LINE MINI App 與原生 App 的初次啟動流程差異如下：

對於原生 App：

對於原生 App 而言，使用者會透過網站上的連結、各種媒體上顯示的 QR code、廣告連結，或社群媒體上的連結進入 App store，接著下載原生 App 並啟動它。在使用者安裝 App 之前，企業必須建立與顧客連結的接觸點與路徑。

對於 LINE MINI App：

LINE MINI App 的初次啟動路徑與原生 App 類似，例如網站上的連結、各種媒體上顯示的 QR code、廣告連結，以及社群媒體上的連結。不過，LINE MINI App 可以直接啟動，無需經過 App store。此外，企業還可以將 LINE MINI App 的啟動路徑放在 LINE 官方帳號的圖文選單（rich menu）與圖文訊息（rich message）中。透過提供 LINE MINI App 中可用的分享目標選擇器（share target picker）所支援的使用者對使用者分享功能，使用者也可以從他們每天用來與家人、朋友溝通的 LINE 聊天室中，直接啟動 LINE MINI App。

如果你是 LINE 官方帳號的常用者，你可能會疑惑：啟動圖文選單與圖文訊息的路徑，是否僅限於已將該 LINE 官方帳號加為好友的使用者才能使用。然而，透過使用 LINE 通知訊息（LINE notification messages）—它能透過電話號碼將訊息發送給尚未將該 LINE 官方帳號加為好友的使用者—使用者在收到 LINE 通知訊息後，便可從 LINE 官方帳號的圖文選單啟動 LINE MINI App，並且也可能因收到該通知而將該 LINE 官方帳號加為好友。

### 2. Notification delivery rate 

原生 App 的強項在於其高度的自訂能力與對豐富媒體（rich media）的支援。然而，通知較容易被使用者停用，這可能導致送達率較低。LINE MINI App 需要依照通知限制及其他指引來運作，但其強項在於高通知送達率，以及與 LINE 生態系的緊密整合。

原生 App 的通知是透過智慧型手機的推播通知功能來送達。它們可以對設計與內容進行進階控制，並能引導使用者前往 App 內特定的功能或頁面。一項缺點是，雖然推播通知對於頻繁使用該 App 的使用者非常有效，但當使用頻率偏低時，送達率往往會下降。

LINE MINI App 的通知則是透過 LINE 官方帳號發送。它們能可靠地將重要資訊送達給使用者，例如預約提醒、排隊叫號通知，以及商品完成通知。由於 LINE 是每天都會使用的工具，通知較不容易被遺漏，因而帶來較高的通知送達率。

### 3. Retention 

原生 App 的強項在於進階個人化與離線功能。然而，當通知被停用時，便難以促進使用者持續使用。另一方面，雖然 LINE MINI App 在進階功能自訂上的彈性不如原生 App，但其高通知送達率與低使用門檻，使其更容易支援留存相關的努力。

對於原生 App，當通知被停用時，便沒有辦法促使使用者重新使用該 App，導致難以重新喚回他們。在某些情況下，使用者甚至可能會忘記這個 App 的存在。為了讓使用者保持興趣，必須持續提供新功能或新內容。

如同下方「原生 App 與 LINE MINI App 中可用的功能」所述，雖然 LINE MINI App 無法提供與原生 App 相同等級的進階功能，但它們在促進服務持續使用方面相當有效。使用者在首次使用時，可以順暢地將該服務的 LINE 官方帳號加為好友，讓服務能持續發送促進回訪的訊息。這進而使得強化與使用者的關係、並提升回訪率成為可能。

## Features available in native apps and LINE MINI Apps 

LINE MINI App 與原生 App 在便利性與功能性方面各自具有不同的特性。LINE MINI App 支援諸如存取相機與麥克風、以及將圖示新增至主畫面等功能，使其易於存取。然而，在 GPS 精準度與藍牙（Bluetooth）功能的使用上則有所限制。原生 App 能充分運用裝置的所有功能並提供進階服務，但需要初始設定以及更高的使用者投入。重要的是要根據服務的特性與使用者的需求，選擇最合適的平台。

![](https://developers.line.biz/media/basics/native-mini/en/native-mini-img-3.webp)

### Camera / microphone 

原生 App 能充分運用裝置的相機與麥克風。這使得製作高品質的媒體內容成為可能；然而，這些功能伴隨著高昂的 App 開發與維護成本。

LINE MINI App 也可以透過 WebRTC 提供使用裝置相機與麥克風的功能。不過，與原生 App 相比，進階的相機與麥克風功能可能會受到限制。

### GPS 

原生 App 能運用裝置的 GPS 功能來取得精準的位置資訊，並據此提供服務。然而，由於電池耗電與隱私方面的疑慮，使用 GPS 需要取得使用者授權。

LINE MINI App 可以在 App 執行期間取得位置資訊。例如，在外帶 App 中，便可提供「尋找鄰近門市」之類的功能。不過，由於無法在背景持續取得位置資訊，因此像跑步追蹤 App 這類應用必須以原生 App 的形式提供。

### Bluetooth 

原生 App 能運用藍牙功能來實現短距離通訊、裝置間的資料傳輸，以及與 IoT 裝置的整合。

LINE MINI App 無法存取裝置的藍牙功能，因此無法搜尋或連接藍牙裝置。像連接 IoT 裝置這類情境需要使用原生 App。

### Adding icons to home screen 

當原生 App 被安裝時，會自動將圖示新增至裝置的主畫面。

LINE MINI App 也可以被新增至裝置的主畫面。雖然需要引導使用者完成將圖示新增至主畫面的流程，但這可以在不下載 App 的情況下完成，使 LINE MINI App 能以幾乎等同於原生 App 的方式被新增。

## Development costs of native apps and LINE MINI Apps 

原生 App 與 LINE MINI App 在開發成本上有明顯的差異。原生 App 提供進階功能與高度的自訂性。然而，其缺點包括高昂的開發成本與較長的更新週期。相對地，雖然 LINE MINI App 在進階功能與自訂性上有某些限制，但它們能以較低的成本實現更快速的開發與更新。

![](https://developers.line.biz/media/basics/native-mini/en/native-mini-img-4.webp)

### Development costs 

原生 App 能充分運用裝置能力，並支援自訂功能與複雜的互動。然而，iOS 與 Android 需要分別開發，這同時增加了工作量與成本。

雖然 LINE MINI App 有一些功能上的限制，但它們是網頁應用程式，因此無論作業系統為何，都可以使用共通的程式來開發。如此一來，實作與測試所需的投入便會減少，開發成本往往也低於原生 App。

### Ease of updates 

原生 App 需要持續更新，以新增服務並維護既有功能。底層程式的更新必須持續處理，這會增加開發成本。

對於 LINE MINI App，未涉及 LINE Developers Console 中設定更新的變更不需要重新審查（關於需要重新審查的項目，請參閱[這裡](https://developers.line.biz/en/docs/line-mini-app/service/update-service/)）。這使得能根據服務的使用趨勢與業務狀況，快速推出更新。

## FAQ 

如需更多資訊，請參閱以下 FAQ 條目：

- [使用者可以將 LINE MINI App 圖示新增至裝置的主畫面嗎？](https://developers.line.biz/en/faq/#can-i-add-line-mini-app-icon-to-home-screen)
- [從 LINE MINI App 向使用者發送通知需要費用嗎？](https://developers.line.biz/en/faq/#does-it-cost-money-to-send-notifications-with-line-mini-apps)
- [使用者可以在不安裝 LINE app 的情況下存取 LINE MINI App 嗎？](https://developers.line.biz/en/faq/#can-users-who-do-not-use-line-use-line-mini-apps)
- [我可以將網頁 App 或 LIFF app 遷移為 LINE MINI App 嗎？](https://developers.line.biz/en/faq/#can-i-migrate-a-web-app-or-liff-app-to-line-mini-app)
- [搭配既有的原生 App 一併使用 LINE MINI App 有什麼好處嗎？](https://developers.line.biz/en/faq/#is-there-any-benefit-to-using-line-mini-apps-with-native-app)
