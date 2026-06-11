# 在 LINE Developers Console 管理 LINE MINI App 設定（Managing LINE MINI App settings on LINE Developers Console）

部分在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊會顯示給 LINE MINI App 的使用者。

## Provider settings 

LINE MINI App 頻道（channel）所屬服務供應商（provider）的下列設定資訊會顯示給使用者：

### **Settings** tab 

| 項目 | 顯示位置 |
| --- | --- |
| **Provider name** | <ul><li>[驗證畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#verification-screen)</li><li>[頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)</li></ul> |

## Channel settings 

LINE MINI App 頻道設定的下列資訊會顯示給使用者：

### **Basic settings** tab 

| 項目 | 顯示畫面 |
| --- | --- |
| **Channel icon** | <ul><li>[Action button](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#built-in-share-settings)</li><li>[Multi-tab view](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#multi-tab-view-settings)</li><li>[驗證畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#verification-screen)</li><li>[頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)</li><li>[服務訊息的頁尾區塊](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#footer-section-of-service-message)</li><li>[新增捷徑畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#add-shortcut-screen)</li></ul>使用者會將此圖片辨識為該 LINE MINI App 的 Channel icon。 |
| **Channel name** | <ul><li>[Action button](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#built-in-share-settings)</li><li>[Multi-tab view](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#multi-tab-view-settings)</li><li>[驗證畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#verification-screen)</li><li>[頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)</li><li>[服務訊息的頁尾區塊](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#footer-section-of-service-message)</li><li>[新增捷徑畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#add-shortcut-screen)</li></ul><p>使用者會將此文字辨識為該 LINE MINI App 的名稱。**Channel name** 會被複製到 **Web app settings** 分頁下的 **LIFF app name**。</p><p>請以英文輸入。若要以其他語言（例如日文）輸入頻道名稱，請參閱 [頻道同意畫面的多語言支援](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#localization)。</p> |
| **Channel description** | <ul><li>[驗證畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#verification-screen)</li><li>[頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)</li></ul>請以英文輸入。若要以其他語言（例如日文）輸入頻道描述，請參閱 [頻道同意畫面的多語言支援](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#localization)。 |
| **Privacy policy URL** | [頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings) |
| **Localization (multi-language support)** | [頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings) |

<!-- note start -->

**頻道描述中必須包含的資訊**

如果你將服務的 LINE MINI App 開發外包，且透過該 LINE MINI App 提供服務的公司與開發該 LINE MINI App 的公司不同，**Channel description** 中必須包含載明下列資訊的聲明：

- 服務公司名稱
- 開發公司名稱
- 你會將透過 LINE MINI App 取得的使用者資料提供給哪些實際公司名稱

<!-- note end -->

### **Web app settings** tab 

| 項目            | 顯示畫面                              |
| ---------------- | ------------------------------------------- |
| **Endpoint URL** | [新增捷徑畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#add-shortcut-screen) |

## Action button 

當使用者透過 [action button](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button) 分享 LINE MINI App 頁面時，下列在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊會顯示在分享頁面所在的聊天室中。

![Action button](https://developers.line.biz/media/line-mini-app/mini_share_builtin_share.png)

| 資訊        | 設定                                  |
| ------------------ | ----------------------------------------- |
| LINE MINI App 名稱 | **Basic settings** tab > **Channel name** |
| LINE MINI App 圖示 | **Basic settings** tab > **Channel icon** |

## Multi-tab view 

當使用者點按 [action button](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button) 時，下列在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊會顯示在 [multi-tab view](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#multi-tab-view) 中。

![](https://developers.line.biz/media/line-mini-app/discover/mini-multi-tab-view-en.png)

| 資訊        | 設定                                  |
| ------------------ | ----------------------------------------- |
| LINE MINI App 名稱 | **Basic settings** tab > **Channel name** |
| LINE MINI App 圖示 | **Basic settings** tab > **Channel icon** |

## Verification screen 

下列在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊會顯示在 [驗證畫面](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid) 上。

![](https://developers.line.biz/media/line-mini-app/line-mini-app-playground-verification-screen-en.png)

| 資訊 | 設定 |
| --- | --- |
| LINE MINI App 圖示 | **Basic settings** tab > **Channel icon** |
| LINE MINI App 名稱 | **Basic settings** tab > **Channel name** |
| Provider name | LINE MINI App 頻道所屬服務供應商的 **Settings** tab > **Provider name** |
| Description | **Basic settings** tab > **Channel description** |

## Channel consent screen 

下列在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊會顯示在 [頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#authorization-flow-disabled) 上。

![Channel consent screen](https://developers.line.biz/media/line-mini-app/mini-permission-request-en.png)

| 資訊 | 設定 |
| --- | --- |
| LINE MINI App 圖示 | **Basic settings** tab > **Channel icon** |
| LINE MINI App 名稱 | **Basic settings** tab > **Channel name** |
| Provider name | LINE MINI App 頻道所屬服務供應商的 **Settings** tab > **Provider name** |
| Description | **Basic settings** tab > **Channel description** |
| Privacy policy URL | **Basic settings** tab > **Privacy policy URL** |

如果該 LINE MINI App 是已驗證的 MINI App，LINE MINI App 名稱旁會顯示驗證徽章。如果該 LINE MINI App 的服務供應商不是已認證的服務供應商，則會顯示「LY Corporation hasn't verified this service provider.」的提示。

### Multi-language support of the Channel consent screen 

頻道同意畫面上的 LINE MINI App 名稱與描述會以使用者 LINE 設定中所設定的語言顯示。例如，如果使用者將 LINE 的語言設定為日文，便會顯示日文的頻道名稱與頻道描述。

| 資訊 | 設定 |
| --- | --- |
| LINE MINI App 名稱 | **Channel basic settings** tab > **Localization (multi-language support)** > **Channel name** |
| Description | **Basic settings** tab > **Localization (multi-language support)** > **Channel description** |

<!-- note start -->

**備註**

- 請務必針對你透過 LINE MINI App 提供服務的國家／地區所使用的主要語言進行在地化（localize）。
- 除非已啟用 **Localization (multi-language support)** 以支援使用者 LINE 設定中所設定的語言，否則所有與 **Channel name** 及 **Channel description** 相關的資訊都會以英文顯示。

<!-- note end -->

## Footer section of service message 

服務訊息的頁尾區塊會使用下列在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊。有關服務訊息的詳細資訊，請參閱 [傳送服務訊息](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)。

![Service messages](https://developers.line.biz/media/line-mini-app/mini_service_notifier.png)

| 資訊        | 設定                                  |
| ------------------ | ----------------------------------------- |
| LINE MINI App 名稱 | **Basic settings** tab > **Channel name** |
| Image              | **Basic settings** tab > **Channel icon** |

## Add Shortcut screen 

下列在 [LINE Developers Console](https://developers.line.biz/console/) 上登錄的資訊會顯示在新增捷徑畫面上。有關新增捷徑畫面的詳細資訊，請參閱 [將 LINE MINI App 的捷徑新增至使用者裝置的主畫面](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)。

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-ios-en.png)

| 資訊                | 設定                                    |
| -------------------------- | ------------------------------------------- |
| LINE MINI App 名稱         | **Basic settings** tab > **Channel name**   |
| LINE MINI App 圖示         | **Basic settings** tab > **Channel icon**   |
| LINE MINI App endpoint URL | **Web app settings** tab > **Endpoint URL** |
