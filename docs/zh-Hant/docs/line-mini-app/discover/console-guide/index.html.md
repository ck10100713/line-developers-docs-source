# LINE MINI App 的 LINE Developers Console 指南（LINE Developers Console Guide for LINE MINI App）

在申請審查之前，請先了解 [LINE Developers Console](https://developers.line.biz/console/) 的基本結構與注意事項。

<!-- table of contents -->

## LINE Developers Console for LINE MINI App 

LINE Developers Console 是用來開發及測試你的 LINE MINI App 的工具，同時也用於提交 LINE MINI App 以進行驗證審查，使其成為已驗證的 MINI App。LINE Developers Console for LINE MINI App 可供任何符合 [LINE MINI App Policy](https://terms2.line.me/LINE_MINI_App?lang=en) 中所定義的合格客戶使用。

## Precautions for using LINE Developers Console for LINE MINI App 

以下說明在 LINE MINI App 頻道（channel）上設定的 LINE MINI App，與新增至 LINE Login 頻道的 LIFF app 之間的差異。

<!-- tip start -->

**我們建議將 LIFF app 建立為 LINE MINI App**

未來 LIFF 與 LINE MINI App 將整合為單一品牌。整合後，LIFF 將併入 LINE MINI App。因此，我們建議你將新的 LIFF app 建立為 LINE MINI App。詳情請參閱 [2025 年 2 月 12 日](https://developers.line.biz/en/news/2025/02/12/line-mini-app/)的最新消息。

<!-- tip end -->

### Basic structure of a LINE MINI App channel 

與 LINE Login 頻道不同，LINE MINI App 頻道具有以下結構特性：

當你在 LINE Developers Console 上建立 LINE MINI App 頻道時，會同時建立三個內部頻道（internal channel）：**Developing**、**Review** 與 **Published**。每個內部頻道都有各自的功能與用途。關於設定何時會生效的更多資訊，請參閱 [When settings on the LINE Developers Console are reflected](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#timing-of-settings-reflection)。

| Internal channel | Usage | Channel status | Admin who can check the details of the internal channel | Users that access the LINE MINI App |
| --- | --- | --- | --- | --- |
| **Developing** | 用於開發及測試的內部頻道 | 永遠為「Developing」 | 只有已接受你所授予權限的管理員<br><ul><li>你可以在 LINE Developers Console 上的 LINE MINI App 頻道設定畫面中查看設定</li></ul> | 只有已接受你所授予權限的測試人員 |
| **Review** | LY Corporation 用來審查你的 LINE MINI App 的內部頻道 | 永遠為「Developing」 | <ul><li>已接受你所授予權限的管理員<ul><li>你可以在 LINE Developers Console 上的 LINE MINI App 頻道設定畫面中查看設定</li></ul></li><li>LY Corporation 審查人員</li></ul> | 只有 LY Corporation 審查人員 |
| **Published** | 對使用者發布的內部頻道 | 永遠為「Published」 | 只有已接受你所授予權限的管理員<br><ul><li>你可以點擊 LINE MINI App 頻道右上角的 **Published Data** 按鈕，查看關於「Published」頻道的資訊。</li></ul> | 一般使用者 |

<!-- note start -->

**你無法變更頻道狀態**

你無法變更各內部頻道的狀態。

<!-- note end -->

<!-- tip start -->

**LINE MINI App 測試人員登錄**

若要新增使用者來測試 LINE MINI App，請將該使用者登錄為 LINE MINI App 頻道的測試人員。詳情請參閱 [Managing roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/)。

<!-- tip end -->

### Confirm LIFF ID and set endpoint URL 

在 LINE MINI App 頻道中，每個內部頻道都會新增一個 LINE MINI App（LIFF app）。請確認各內部頻道專屬的 **LIFF ID**，並為各內部頻道指定 **Endpoint URL**，然後將 LIFF app 部署至各自的端點 URL。

- 在申請審查之前，請將「Review」的 LIFF app 部署至「Review」的端點 URL。
- 在發布 LINE MINI App 時，請將「Published」的 LIFF app 部署至「Published」的端點 URL。

你可以在 **Developing** 或 **Review** 的 **Endpoint URL** 中指定具有基本驗證（basic authentication）的 URL。詳情請參閱 [Use basic authentication to restrict access to your LINE MINI App before it is released](https://developers.line.biz/en/docs/line-mini-app/develop/develop-overview/#use-basic-authentication)。

<!-- note start -->

**每個內部頻道都有不同的 LIFF ID**

- 在 LINE MINI App 上呼叫 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法時，請為各內部頻道指定不同的 LIFF ID。例如，當你從「Review」頻道執行初始化時，請使用 `liff.init()` 指定 Review 頻道的 LIFF ID，再進行初始化。如果你無法在所有內部頻道上啟動 LINE MINI App，請確認以下兩個 LIFF ID 是否相符。
  - 為各內部頻道所核發的 LIFF ID
  - 初始化 LIFF app 時在 `liff.init()` 中指定的 LIFF ID
- LIFF ID 會包含在 LIFF URL 中（例如 `https://miniapp.line.me/{liffId}`）。換句話說，如果你想從某個 LIFF app 傳送自訂分享訊息，請傳送該 LIFF app 所對應的 URL。例如，如果你想從「Review」的 LIFF 傳送自訂分享訊息，請傳送用於分享「Review」LIFF app 的 URL。
- 單一內部頻道無法新增多個 LIFF app（無法核發多個 LIFF ID）

<!-- note end -->

<!-- note start -->

**LINE Login 頻道的 [LIFF] 分頁與 LINE MINI App 頻道的 [Web app settings] 分頁之間的差異**

- 在 LINE MINI App 頻道的 **Web app settings** 分頁中，除了預設的 LINE MINI App（LIFF app）之外，你無法新增任何其他 LIFF app。
- 在 LINE MINI App 頻道的 **Web app settings** 分頁中，你無法為各 LIFF app（內部頻道）變更 scope、加入好友選項等設定。
- 在 LINE MINI App 頻道的 **Web app settings** 分頁中，你無法設定 **Module mode**。

<!-- note end -->

<!-- tip start -->

**LINE Developers Console 上的設定**

LINE Developers Console 上的設定會在需要時自動反映（複製）。詳情請參閱 [When settings on the LINE Developers Console are reflected](https://developers.line.biz/en/docs/line-mini-app/discover/console-guide/#timing-of-settings-reflection)。

<!-- tip end -->

<!-- note start -->

**LINE MINI App 的 LIFF URL 已變更**

自 [2023 年 12 月 13 日](https://developers.line.biz/en/news/2023/12/13/change-of-liff-url-for-line-mini-app/)起，LINE MINI App 的 LIFF URL 已變更為 `https://miniapp.line.me/{liffId}`。

如果使用者存取既有的 `https://liff.line.me/{liffId}`，LINE MINI App 也會開啟。因此，你可以繼續使用先前已核發的 QR code。

<!-- note end -->

### Issuing a channel access token 

請為 LINE MINI App 頻道使用[無狀態頻道存取權杖（stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)。

請為運行 LINE MINI App（LIFF app）的每個內部頻道核發頻道存取權杖（channel access token）。Channel ID 與 Channel secret 可在 LINE Developers Console 上的 **Channel basic settings** 分頁中找到。

![Channel ID and Channel Secret](https://developers.line.biz/media/line-mini-app/channel_id_secret.png)

<!-- note start -->

**必須為每個內部頻道核發頻道存取權杖**

從「Review」與「Published」的 LINE MINI App 傳送 Service Message 時，請勿指定「Developing」LINE MINI App 頻道的頻道存取權杖

<!-- note end -->

<!-- note start -->

**建議使用無狀態頻道存取權杖**

[長期頻道存取權杖（long-lived channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)與[可由使用者指定有效期間的頻道存取權杖（Channel Access Token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)無法用於 LINE MINI App 頻道。

開發 LINE MINI App 時，可使用[無狀態頻道存取權杖（stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)或[短期頻道存取權杖（short-lived channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)。在這兩者之中，建議使用無狀態頻道存取權杖。無狀態頻道存取權杖的核發次數沒有上限，因此應用程式無需管理權杖的生命週期。

<!-- note end -->

### About configuring the company or owner's country or region 

建立 LINE MINI App 頻道時，你必須同意 **I represent and warrant that the region to provide the LINE MINI App and service company's country or region are the same.** 這個核取方塊的內容。該國家或地區會在頻道同意畫面（channel consent screen）中向一般使用者顯示。

![I represent and warrant that the region to provide the LINE MINI App and service company's country or region are the same.](https://developers.line.biz/media/line-mini-app/configuring-country-or-region-en.png)

<!-- note start -->

**你無法編輯既有 LINE MINI App 頻道的公司或擁有者所在國家或地區**

如果你需要變更，請在申請審查時，於 **Review request** 分頁的 **Reference materials for the review** 區段中，填寫你希望變更設定的意願以及你想變更成的國家或地區。

<!-- note end -->

### When settings on the LINE Developers Console are reflected 

當你建立 LINE MINI App 頻道時，你所輸入的設定資訊會複製到三個內部頻道。

如果該 LINE MINI App 是未驗證的 MINI App，當你在 LINE Developers Console 中變更設定時，「Developing」頻道的內容會反映到「Published」頻道。不過，除非該 LINE MINI App 通過驗證審查，否則 [**Service message template**] 分頁的內容，以及 [**Web app settings**] 分頁上的 [**Channel consent simplification**] 不會被反映。

如果該 LINE MINI App 是已驗證的 MINI App，且你變更了頻道名稱、LIFF app 的 scope、加入好友選項等項目，則只有「Developing」頻道上的設定會變更。變更不會反映到「Review」或「Published」頻道。這是為了讓你能夠在「Developing」內部頻道中自由變更設定，以確保開發順利進行。

對於已驗證的 MINI App，下表顯示在 LINE Developers Console 上變更的設定何時會反映到「Review」與「Published」。

| Internal channel | When settings are reflected |
| --- | --- |
| Developing | 在 LINE Developers Console 上設定時即反映。 |
| Review | 當審查開始時，會反映（複製）Developing 頻道的設定。 |
| Published | 當發布時，會反映（複製）Developing 頻道的設定。 |

### Channel description 

**Basic settings** 分頁上的 **Channel description** 有兩個用途。為了這些用途，請提供正確的服務說明：

- 協助使用者了解 LINE MINI App 服務的內容。
- 讓 LY Corporation 在審查時了解 LINE MINI App 的服務內容。

![Channel description](https://developers.line.biz/media/line-mini-app/line-mini-app-channel-description-en.png)

關於 **Channel description** 的輸入範例，請參閱下表。

|  | Channel name | Channel description |
| --- | --- | --- |
| 不良範例 | LINE FRIENDS STORE | LINE FRIENDS STORE 是販售 LINE 角色商品的商店。 |
| 良好範例 | LINE FRIENDS STORE | 這是 LINE FRIENDS STORE 的行動點餐服務。你可以預先下單並付款，然後到店領取商品。 |

## Differences in the behavior of the 3 LINE MINI Apps 

某些畫面在「Developing」LINE MINI App、「Review」LINE MINI App 與「Published」LINE MINI App 中的顯示方式有所不同。

| LINE MINI App | Header subtext [(reference)](https://developers.line.biz/en/docs/line-mini-app/discover/ui-components/#header) |
| --- | --- |
| 「Developing」LINE MINI App | **永遠**顯示你正在瀏覽的頁面網域。 |
| 「Review」LINE MINI App | **永遠**顯示你正在瀏覽的頁面網域。 |
| 「Published」LINE MINI App | 在未驗證的 MINI App 中，會顯示頁面的網域。在已驗證的 MINI App 中，會顯示 LINE MINI App 名稱與驗證徽章。 |
