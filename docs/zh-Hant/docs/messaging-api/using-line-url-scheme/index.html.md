# 使用 LINE URL scheme 使用 LINE 功能（Use LINE features with the LINE URL scheme）

你可以透過 LINE URL scheme 開啟貼圖小舖（Sticker Shop）、LIFF app 或相機。LINE URL scheme 也適用於 LINE 官方帳號（LINE Official Account）。你可以在[圖文選單（rich menus）](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)中，透過開啟 LINE URL scheme 的[動作（action）](https://developers.line.biz/en/reference/messaging-api/#uri-action)，讓使用者瀏覽 LINE 內容。

## Supported LINE URL schemes 

支援以下 LINE URL scheme：

| URL scheme | 說明 |
| --- | --- |
| 以 `https://line.me/R/` 開頭的 URL scheme | 用於使用 LINE app 功能的 URL scheme |
| 以 `https://liff.line.me/` 開頭的 URL scheme | 用於開啟 [LIFF app](https://developers.line.biz/en/docs/liff/overview/) 的 URL scheme |
| 以 `https://miniapp.line.me/` 開頭的 URL scheme | 用於開啟 [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/) 的 URL scheme |

<!-- warning start -->

**「line://」已淘汰（deprecated）**

`line://` scheme 已淘汰，目的是防止在使用者點擊 URL 時，違反 LY Corporation 或使用者的意願，啟動非 LINE 的 app 的劫持攻擊（takeover attack）。這類攻擊在特定條件下可能發生。

目前並未為 `line://` URL scheme 設定明確的廢止日期。

<!-- warning end -->

<!-- note start -->

**LY Corporation 不提供用於啟動 LINE 以外原生 app 的 URL scheme**

LY Corporation 不提供用於啟動 LINE 以外原生 app 的 URL scheme。不過，如果其他公司的原生 app 有用於啟動該原生 app 的 URL scheme，你可以在[圖文選單（rich menus）](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)或 [Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/) 的 URI action 物件中使用該 URL scheme。

<!-- note end -->

## What happens when a LINE URL scheme is clicked 

當使用者在已安裝 LINE 的裝置上點擊使用 LINE URL scheme 的 URL 時，會自動啟動 LINE 並顯示該 URL 指定的內容。如果未安裝 LINE，依 scheme 不同會有不同結果：

| LINE URL scheme | 未安裝 LINE 時會發生的情況 |
| --- | --- |
| `https://line.me/R/` | 啟動網頁瀏覽器並提示使用者下載 LINE。 |
| `line://`（已淘汰） | 不會發生任何事，或使用者被導向錯誤頁面。 |

## Supported platforms 

LINE URL scheme 支援 LINE for iOS 與 LINE for Android。

<!-- note start -->

**備註**

LINE URL scheme 不支援 LINE for PC（macOS、Windows）。

<!-- note end -->

## Available LINE URL schemes 

你可以透過 LINE URL scheme 執行以下操作。僅在特定平台支援的 LINE URL scheme 會在各章節中註明：

- [開啟相機與相簿](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-the-camera-and-camera-roll)
- [傳送位置資訊](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#sending-the-location-screen)
- [分享 LINE 官方帳號](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#sharing-line-official-account)
- [開啟 LINE 官方帳號的 LINE VOOM 與商業檔案](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-line-voom-and-profile)
- [開啟與 LINE 官方帳號的聊天畫面](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-chat-screen)
- [傳送文字訊息](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#sending-text-messages)
- [開啟個人檔案資訊](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-profile-information)
- [開啟常用的 LINE 畫面](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-common-line-app-screens)
- [開啟 LINE 設定](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-line-app-settings-screens)
- [開啟貼圖小舖](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-the-sticker-shop)
- [開啟主題小舖](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-the-theme-shop)
- [開啟 LIFF app](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-a-liff-app)
- [在外部瀏覽器中開啟 URL](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-url-in-external-browser)

### Opening the camera and camera roll 

透過 LINE URL scheme，你可以讓使用者開啟相機或相簿。相簿是使用者可以選取圖片以在聊天中分享的地方。

<!-- note start -->

**開啟相機或相簿的限制**

你只能在 LINE 聊天（包含 LINE OpenChat）中，透過此 URL scheme 開啟相機或相簿。這些 URL scheme 不支援聊天以外的 LINE 功能、LIFF app 或 LINE 以外的 app。

<!-- note end -->

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/camera-screen.png)

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/camera-roll.png)

| LINE URL scheme | 說明 |
| --- | --- |
| `https://line.me/R/nv/camera/` | 開啟相機。對於具有前鏡頭（自拍鏡頭）與後鏡頭（外拍鏡頭）等多個相機的智慧型手機，你無法指定要開啟哪一個相機。 |
| `https://line.me/R/nv/cameraRoll/single` | 開啟相簿。使用者可以選取一張圖片以在聊天中分享。 |
| `https://line.me/R/nv/cameraRoll/multi` | 開啟相簿。使用者可以選取多張圖片以在聊天中分享。 |

### Sending location information 

透過 LINE URL scheme，你可以開啟位置資訊畫面，讓使用者將其位置資訊傳送給你的 LINE 官方帳號。

<!-- note start -->

**開啟位置資訊畫面的限制**

你只能在使用者與你的 LINE 官方帳號之間的一對一聊天中，透過此 URL scheme 讓使用者檢視位置資訊。此 URL scheme 不支援其他聊天類型、LIFF app 或 LINE 以外的 app。

<!-- note end -->

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/location.png)

| LINE URL scheme | 說明 |
| --- | --- |
| `https://line.me/R/nv/location/` | 開啟位置畫面。使用者可以在地圖上放置圖釘以選取要分享的位置。 |

### Sharing a LINE Official Account 

透過 LINE URL scheme，你可以推薦並鼓勵使用者及其好友加入你的 LINE 官方帳號。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/bot-add-friend-en.png)

| LINE URL scheme | 說明 |
| --- | --- |
| https://line.me/R/ti/p/`{Percent-encoded LINE ID}` | 開啟 LINE 官方帳號的個人檔案頁面。如果使用者已經是你的 LINE 官方帳號的好友，則改為顯示一對一聊天。 |
| https://line.me/R/nv/recommendOA/`{Percent-encoded LINE ID}` | 開啟「分享給」畫面。使用者可以選取好友、群組聊天或多人聊天來分享你的 LINE 官方帳號。 |

<!-- note start -->

**「Percent-encoded LINE ID」必須經過百分比編碼（percent encoded）**

請確保 `{Percent-encoded LINE ID}` 以 UTF-8 進行[百分比編碼（percent encoded）](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)。例如，如果 LINE ID 是 `@linedevelopers`，請使用 `https://line.me/R/ti/p/%40linedevelopers` 與 `https://line.me/R/nv/recommendOA/%40linedevelopers`。如果你以未經百分比編碼的 LINE ID 替換，也能運作，但已淘汰。

不過，如果你在開啟「分享給」畫面的 URL scheme（`https://line.me/R/nv/recommendOA/%40linedevelopers`）中對 LINE ID 進行百分比編碼，在 Android 版 13.8.0 之前的 LINE 版本上將無法運作。

你可以指定[基本 ID（Basic ID）或進階 ID（Premium ID）](https://help.linebiz.com/lineadshelp/s/article/L000001191?language=ja)（僅提供日文）作為你的 LINE 官方帳號的 LINE ID。

<!-- note end -->

<!-- tip start -->

**確認 LINE 官方帳號的 LINE ID**

在 [LINE Official Account Manager](https://manager.line.biz/) 中查詢你的 LINE 官方帳號的 LINE ID。如需更多資訊，請參閱[分享你的 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)。

<!-- tip end -->

<!-- tip start -->

**在 PC 瀏覽器上的 LINE URL scheme**

當使用者從 PC 開啟 `https://line.me/R/ti/p/{Percent-encoded LINE ID}` 時，他們會看到 LINE 官方帳號商業檔案的公開 URL（例如 [LINE FRIENDS 個人檔案頁面](https://line.me/R/ti/p/@linecharacter)），或僅看到 QR code。使用者看到的內容取決於以下條件：

- 你的 LINE 官方帳號是已驗證帳號
- 已設定 LINE 官方帳號個人檔案的公開 URL 為可用

如果同時滿足這兩個條件，使用者會看到你的 LINE 官方帳號的公開 URL 以及 QR code。如果未滿足，使用者只會看到你的 LINE 官方帳號的 QR code。你可以在 [LINE Official Account Manager](https://manager.line.biz/) 中調整設定，將未驗證帳號變更為已驗證帳號，或使用你個人檔案的公開 URL。

<!-- tip end -->

### Opening the LINE Official Account's LINE VOOM and business profile 

透過 LINE URL scheme，你可以讓使用者開啟你的 LINE 官方帳號的 LINE VOOM 與商業檔案頁面。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/bot-line-voom.png)

| LINE URL scheme | 說明 |
| --- | --- |
| https://line.me/R/home/public/main?id=`{LINE ID without @}` | 開啟 LINE 官方帳號的 LINE VOOM。 |
| https://line.me/R/home/public/profile?id=`{LINE ID without @}` | 開啟 LINE 官方帳號的商業檔案。 |
| https://line.me/R/home/public/post?id=`{LINE ID without @}`&postId=`{postId}` | 開啟 LINE 官方帳號的 LINE VOOM 貼文。可在 [LINE VOOM Studio](https://voom-studio.line.biz/) 中查詢各別貼文的 post ID。 |

<!-- note start -->

**在 URL scheme 中排除小老鼠符號（@）前綴**

將 URL scheme 中的 `{LINE ID without @}` 替換為你的 LINE 官方帳號的 LINE ID。你可以指定基本 ID 或[進階 ID（premium ID）](https://developers.line.biz/en/glossary/#premium-id)。請從你的 LINE 官方帳號的 LINE ID 中排除小老鼠符號（`@`）前綴。例如，如果 LINE ID 是 `@linedevelopers`，請使用 `https://line.me/R/home/public/main?id=linedevelopers`。

<!-- note end -->

<!-- tip start -->

**確認 LINE 官方帳號的 LINE ID**

在 [LINE Official Account Manager](https://manager.line.biz/) 中查詢你的 LINE 官方帳號的 LINE ID。如需更多資訊，請參閱[分享你的 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)。

<!-- tip end -->

<!-- tip start -->

**在 LINE VOOM 上發文與自訂商業檔案**

若要在你的 LINE 官方帳號上於 LINE VOOM 發文或自訂商業檔案，請使用 [LINE VOOM Studio](https://voom-studio.line.biz/) 或 [LINE Official Account Manager](https://manager.line.biz/)。

<!-- tip end -->

### Opening a chat screen with a LINE Official Account 

透過 LINE URL scheme，你可以讓使用者開啟與你的 LINE 官方帳號的聊天畫面。

| LINE URL scheme | 說明 |
| --- | --- |
| https://line.me/R/oaMessage/`{Percent-encoded LINE ID}` | 開啟與你的 LINE 官方帳號的聊天畫面。 |
| https://line.me/R/oaMessage/`{Percent-encoded LINE ID}`/?`{text_message}` | 開啟與你的 LINE 官方帳號的聊天畫面，並將 `{text_message}` 中設定的文字訊息輸入到訊息輸入欄位中。 |

<!-- note start -->

**「Percent-encoded LINE ID」與「text_message」必須經過百分比編碼**

請確保 `{Percent-encoded LINE ID}` 與 `{text_message}` 以 UTF-8 進行[百分比編碼（percent encoded）](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)。例如，如果你要向 LINE ID 為 `@linedevelopers` 的 LINE 官方帳號傳送文字訊息「Hi there!」，請使用 `https://line.me/R/oaMessage/%40linedevelopers/?Hi%20there%21`。如果你以未經百分比編碼的 LINE ID 替換，也能運作，但已淘汰。

你可以指定[基本 ID（Basic ID）或進階 ID（Premium ID）](https://help.linebiz.com/lineadshelp/s/article/L000001191?language=ja)（僅提供日文）作為你的 LINE 官方帳號的 LINE ID。

<!-- note end -->

<!-- tip start -->

**確認 LINE 官方帳號的 LINE ID**

在 [LINE Official Account Manager](https://manager.line.biz/) 中查詢你的 LINE 官方帳號的 LINE ID。如需更多資訊，請參閱[分享你的 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)。

<!-- tip end -->

### Sending text messages 

透過 LINE URL scheme，你可以為使用者設定一則文字訊息，供其傳送給好友或 LINE 官方帳號。

| LINE URL scheme | 說明 |
| --- | --- |
| https://line.me/R/share?text=`{text_message}` | 開啟「分享給」畫面。使用者可以選取好友、群組聊天或多人聊天，以傳送由 `{text_message}` 指定的文字訊息。使用者也可以將該文字傳送到 Keep Memo、LINE VOOM 與其他 app。 |

<!-- note start -->

**「text_message」必須經過百分比編碼**

請確保 `{text_message}` 以 UTF-8 進行[百分比編碼（percent encoded）](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)。例如，如果你要傳送文字訊息「Hi there!」，請使用 `https://line.me/R/share?text=Hi%20there%21`。

<!-- note end -->

### Opening profile information 

透過 LINE URL scheme，你可以讓使用者開啟他們的「我的個人檔案」畫面。在此畫面中，使用者可以更新顯示名稱與狀態消息、設定他們的 LINE ID 並檢視個人檔案設定。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/my-profile.png)

| LINE URL scheme | 說明 |
| --- | --- |
| `https://line.me/R/nv/profile` | 開啟使用者的「我的個人檔案」畫面。 |
| `https://line.me/R/nv/profileSetId` | 開啟使用者的「LINE ID」畫面。透過此 URL scheme，你可以讓尚未設定 LINE ID 的使用者設定他們的 LINE ID。 |

### Opening common LINE screens 

透過 LINE URL scheme，你可以讓使用者開啟不同的 LINE 畫面，包括聊天分頁。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/shopping-tab-en.png)

| LINE URL scheme | 說明 |
| --- | --- |
| `https://line.me/R/nv/chat` | 開啟聊天分頁。 |
| `https://line.me/R/nv/commerce` | 開啟購物分頁。 |
| `https://line.me/R/nv/wallet` | 開啟錢包分頁。 |
| `https://line.me/R/nv/addFriends` | 開啟「加入好友」畫面。 |
| `https://line.me/R/nv/officialAccounts` | 開啟「LINE 官方帳號」畫面。 |
| `https://line.me/R/nv/timeline` | 開啟 LINE VOOM「追蹤中」畫面。 |

### Opening LINE settings 

透過 LINE URL scheme，你可以開啟不同的設定選單。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/settings.png)

| LINE URL scheme | 說明 |
| --- | --- |
| `https://line.me/R/nv/settings` | 開啟設定。 |
| `https://line.me/R/nv/settings/account` | 開啟帳號設定。顯示使用者的 LINE 帳號資訊。 |
| `https://line.me/R/nv/connectedApps` | 開啟帳號 > 已授權的 app。顯示授予已授權 app 的權限，並讓使用者解除連結 app。 |
| `https://line.me/R/nv/connectedDevices` | 開啟帳號 > 已連結的裝置。 |
| `https://line.me/R/nv/settings/privacy` | 開啟隱私設定。 |
| `https://line.me/R/nv/settings/sticker` | 開啟貼圖設定。 |
| `https://line.me/R/nv/stickerShop/mySticker` | 開啟貼圖 > 我的貼圖。 |
| `https://line.me/R/nv/settings/themeSettingsMenu`（iOS）、`https://line.me/R/nv/settings/theme`（Android） | 開啟主題設定。<br />iOS 與 Android 的 scheme 不同。 |
| `https://line.me/R/nv/themeSettings` | 開啟主題 > 我的主題。 |
| `https://line.me/R/nv/notificationServiceDetail` | 開啟通知 > 已授權的 app。讓使用者設定已授權 app 的通知。 |
| `https://line.me/R/nv/settings/chatSettings` | 開啟聊天設定。 |
| `https://line.me/R/nv/suggestSettings` | 開啟聊天 > 顯示建議。 |
| `https://line.me/R/nv/settings/callSettings` | 開啟通話設定。 |
| `https://line.me/R/nv/settings/addressBookSync` | 開啟好友設定。 |
| `https://line.me/R/nv/settings/timelineSettings` | 開啟 LINE VOOM 設定。 |

### Opening Sticker Shop 

透過 LINE URL scheme，你可以讓使用者開啟 LINE 中的貼圖小舖（Sticker Shop），以鼓勵購買官方與創作者的貼圖組。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/sticker-shop-categories.png)

| LINE URL scheme | 說明 |
| --- | --- |
| https://line.me/R/shop/sticker/detail/`{package_id}` | 開啟貼圖組資訊畫面。將 `{package_id}` 指定為 [LINE STORE](https://store.line.me/) 中貼圖頁面 URL 所指定的數字。 |
| https://line.me/R/shop/category/`{category_id}` | 開啟指定類別的人氣排行榜。將 `{category_id}` 指定為 [LINE STORE](https://store.line.me/) > 官方貼圖中類別頁面 URL 所指定的數字。 |
| https://line.me/R/shop/sticker/author/`{author_id}` | 開啟指定作者的貼圖組清單。將 `{author_id}` 指定為 [LINE STORE](https://store.line.me/) 中創作者頁面 URL 所指定的數字。 |
| `https://line.me/R/nv/stickerShop` | 開啟貼圖小舖 > HOME 分頁。 |
| `https://line.me/R/shop/sticker/hot` | 開啟貼圖小舖 > RANK 分頁。 |
| `https://line.me/R/shop/sticker/new` | 開啟貼圖小舖 > NEW 分頁。 |
| `https://line.me/R/shop/sticker/event` | 開啟貼圖小舖 > FREE 分頁。 |
| `https://line.me/R/shop/sticker/category` | 開啟貼圖小舖 > CATEGORIES 分頁。 |

<!-- tip start -->

**建立你自己的貼圖組**

若要為使用者建立你自己的貼圖組，請造訪 [LINE Creators Market](https://creator.line.me/en/) 並使用 [LINE Sticker Maker](https://creator.line.me/en/stickermaker/) app。

<!-- tip end -->

### Opening Theme Shop 

透過 LINE URL scheme，你可以讓使用者開啟 LINE 中的主題小舖（Theme Shop），以鼓勵購買官方與創作者的主題。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/theme-shop.png)

| LINE URL scheme | 說明 |
| --- | --- |
| https://line.me/R/shop/theme/detail?id=`{product_id}` | 開啟主題資訊畫面。將 `{product_id}` 指定為 [LINE STORE](https://store.line.me/) 中主題頁面 URL 所指定的 ID。例如，如果你開啟 [Matte White](https://store.line.me/themeshop/product/0bac8fed-4c75-40c5-9982-e9ecc3b9d191/en)`https://store.line.me/themeshop/product/0bac8fed-4c75-40c5-9982-e9ecc3b9d191/en`，請指定 `0bac8fed-4c75-40c5-9982-e9ecc3b9d191`。 |

### Opening a LIFF app 

透過 LINE URL scheme，你可以讓使用者開啟 LIFF app。LIFF app 是使用 [LINE Front-end Framework（LIFF）](https://developers.line.biz/en/docs/liff/overview/)建構的網頁 app。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/liff-app.png)

| LINE URL scheme | 說明 |
| --- | --- |
| https://liff.line.me/`{liffId}` | 開啟具有指定 LIFF ID 的 LIFF app。此 URL scheme 稱為 LIFF URL。 |
| https://liff.line.me/`{liffId}`/path_A/path_B/?key1=value1&key2=value2 | 開啟具有指定 LIFF ID 的 LIFF app。你可以將 `/path_A/path_B/?key1=value1&key2=value2` 作為額外資訊傳遞。 |

如需開啟 LIFF app 流程的更多資訊，請參閱 LIFF 文件中的[開啟 LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

<!-- note start -->

**「https://line.me/R/app/{liffId}」與「line://app/{liffId}」已淘汰**

[LIFF v1](https://developers.line.biz/en/docs/liff/versioning-policy/#life-cycle-schedule) 中使用的以下 LIFF URL 格式已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)：

- `https://line.me/R/app/{liffId}`&nbsp;
- `line://app/{liffId}`&nbsp;

<!-- note end -->

### Opening a URL in an external browser 

透過查詢參數（query parameter），你可以讓使用者在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟 URL，而非在 [LINE 的應用程式內瀏覽器（in-app browser）](https://developers.line.biz/en/glossary/#line-iab)中開啟。

<!-- note start -->

**這些查詢參數不支援 LIFF app**

這些查詢參數適用於從 LINE app 存取的所有 URL，但 LIFF app 除外。即使你將這些查詢參數加入 LIFF URL，也不會在外部瀏覽器中開啟。

<!-- note end -->

| 帶有查詢參數的 URL | 說明 |
| --- | --- |
| https://example.com/?`openExternalBrowser=1` | 在外部瀏覽器中開啟目標 URL。 |
| https://example.com/?`openInAppBrowser=0` | 在 Chrome 自訂分頁（Chrome custom tab）中開啟目標 URL（僅在 LINE for Android 中可用）。 |
