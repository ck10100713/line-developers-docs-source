# 使用 LINE URL scheme 開啟 LINE 功能（Using LINE features with the LINE URL scheme）

你可以使用 LINE URL scheme 開啟貼圖小舖（Sticker Shop）、LIFF app 或相機。LINE URL scheme 也適用於 LINE 官方帳號（LINE Official Account）。你可以透過開啟 LINE URL scheme 的 [action](https://developers.line.biz/en/reference/messaging-api/#uri-action)，讓使用者從[圖文選單（rich menu）](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)查看 LINE 內容。

## Supported LINE URL schemes 

支援以下 LINE URL scheme：

| URL scheme | Description |
| --- | --- |
| 以 `https://line.me/R/` 開頭的 URL scheme | 用於使用 LINE app 功能的 URL scheme |
| 以 `https://liff.line.me/` 開頭的 URL scheme | 用於開啟 [LIFF app](https://developers.line.biz/en/docs/liff/overview/) 的 URL scheme |
| 以 `https://miniapp.line.me/` 開頭的 URL scheme | 用於開啟 [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/) 的 URL scheme |

<!-- warning start -->

**「line://」已淘汰（deprecated）**

`line://` scheme 已淘汰，以防止接管攻擊（takeover attack）——這類攻擊會在使用者點擊 URL 時，違背 LY Corporation 或使用者的本意而啟動非 LINE 的 app。此攻擊在特定條件下可能發生。

`line://` URL scheme 尚未訂定確切的失效日期。

<!-- warning end -->

<!-- note start -->

**LY Corporation 不提供用於啟動 LINE 以外原生 app 的 URL scheme**

LY Corporation 不提供用於啟動 LINE 以外原生 app 的 URL scheme。不過，若其他公司的原生 app 本身具有用於啟動該原生 app 的 URL scheme，你可以在[圖文選單（rich menu）](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)或 [Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/) 的 URI action 物件中使用該 URL scheme。

<!-- note end -->

## What happens when a LINE URL scheme is clicked 

當使用者在已安裝 LINE 的裝置上點擊使用 LINE URL scheme 的 URL 時，LINE 會自動啟動並顯示該 URL 所指定的內容。若未安裝 LINE，則依 scheme 的不同而有不同結果：

| LINE URL scheme | 未安裝 LINE 時的結果 |
| --- | --- |
| `https://line.me/R/` | 啟動網頁瀏覽器並提示使用者下載 LINE。 |
| `line://`（已淘汰） | 沒有任何反應，或使用者被導向錯誤頁面。 |

## Supported platforms 

LINE URL scheme 支援 LINE for iOS 與 LINE for Android。

<!-- note start -->

**注意**

LINE URL scheme 不支援 LINE for PC（macOS、Windows）。

<!-- note end -->

## Available LINE URL schemes 

你可以使用 LINE URL scheme 進行下列操作。僅在特定平台支援的 LINE URL scheme 會在各章節中特別說明：

- [開啟相機與相簿](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-the-camera-and-camera-roll)
- [傳送位置資訊](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#sending-the-location-screen)
- [分享 LINE 官方帳號](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#sharing-line-official-account)
- [開啟 LINE 官方帳號的 LINE VOOM 與商業檔案](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-line-voom-and-profile)
- [開啟與 LINE 官方帳號的聊天畫面](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-chat-screen)
- [傳送文字訊息](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#sending-text-messages)
- [開啟個人檔案資訊](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-profile-information)
- [開啟常用的 LINE 畫面](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-common-line-app-screens)
- [開啟 LINE 設定](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-line-app-settings-screens)
- [開啟貼圖小舖](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-the-sticker-shop)
- [開啟主題小舖](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-the-theme-shop)
- [開啟 LIFF app](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-a-liff-app)
- [在外部瀏覽器中開啟 URL](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-url-in-external-browser)

### Opening the camera and camera roll 

你可以使用 LINE URL scheme 讓使用者開啟相機或相簿。相簿（camera roll）是使用者可選取圖片以在聊天中分享的位置。

<!-- note start -->

**開啟相機或相簿的限制**

你只能從 LINE 聊天（包括 LINE OpenChat）使用此 URL scheme 開啟相機或相簿。這些 URL scheme 不支援聊天以外的 LINE 功能、LIFF app 或 LINE 以外的 app。

<!-- note end -->

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/camera-screen.png)

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/camera-roll.png)

| LINE URL scheme | Description |
| --- | --- |
| `https://line.me/R/nv/camera/` | 開啟相機。對於具有多個相機（例如前置（自拍鏡頭）與後置（外鏡頭））的智慧型手機，你無法指定要開啟哪一個相機。 |
| `https://line.me/R/nv/cameraRoll/single` | 開啟相簿。使用者可選取一張圖片以在聊天中分享。 |
| `https://line.me/R/nv/cameraRoll/multi` | 開啟相簿。使用者可選取多張圖片以在聊天中分享。 |

### Sending location information 

你可以使用 LINE URL scheme 開啟位置資訊畫面，讓使用者將其位置資訊傳送給你的 LINE 官方帳號。

<!-- note start -->

**開啟位置資訊畫面的限制**

你只能在使用者與你的 LINE 官方帳號的一對一聊天中，使用此 URL scheme 讓使用者查看位置資訊。此 URL scheme 不支援其他聊天類型、LIFF app 或 LINE 以外的 app。

<!-- note end -->

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/location.png)

| LINE URL scheme | Description |
| --- | --- |
| `https://line.me/R/nv/location/` | 開啟位置畫面。使用者可在地圖上放置標記以選取要分享的位置。 |

### Sharing a LINE Official Account 

你可以使用 LINE URL scheme 推薦並鼓勵使用者及其好友加入你的 LINE 官方帳號。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/bot-add-friend-en.png)

| LINE URL scheme | Description |
| --- | --- |
| https://line.me/R/ti/p/`{Percent-encoded LINE ID}` | 開啟 LINE 官方帳號的個人檔案頁面。若使用者已是你 LINE 官方帳號的好友，則改為顯示一對一聊天。 |
| https://line.me/R/nv/recommendOA/`{Percent-encoded LINE ID}` | 開啟「分享給」畫面。使用者可選取好友、群組聊天或多人聊天，以分享你的 LINE 官方帳號。 |

<!-- note start -->

**「Percent-encoded LINE ID」必須經過百分比編碼（percent encoded）**

請確保 `{Percent-encoded LINE ID}` 已以 UTF-8 進行[百分比編碼（percent encoded）](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)。例如，若 LINE ID 為 `@linedevelopers`，請使用 `https://line.me/R/ti/p/%40linedevelopers` 與 `https://line.me/R/nv/recommendOA/%40linedevelopers`。若改用未經百分比編碼的 LINE ID 也可運作，但已淘汰（deprecated）。

不過，若你在開啟「分享給」畫面的 URL scheme 中對 LINE ID 進行百分比編碼（`https://line.me/R/nv/recommendOA/%40linedevelopers`），在 Android 早於 13.8.0 的 LINE 版本上將無法運作。

你可以指定 [Basic ID 或 Premium ID](https://help.linebiz.com/lineadshelp/s/article/L000001191?language=ja)（僅提供日文）作為你 LINE 官方帳號的 LINE ID。

<!-- note end -->

<!-- tip start -->

**確認 LINE 官方帳號的 LINE ID**

請在 [LINE Official Account Manager](https://manager.line.biz/) 中找到你 LINE 官方帳號的 LINE ID。詳情請參閱[分享你 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)。

<!-- tip end -->

<!-- tip start -->

**在 PC 瀏覽器上的 LINE URL scheme**

當使用者從 PC 開啟 `https://line.me/R/ti/p/{Percent-encoded LINE ID}` 時，會看到 LINE 官方帳號商業檔案的公開 URL（例如 [LINE FRIENDS 個人檔案頁面](https://line.me/R/ti/p/@linecharacter)）或僅有 QR code。使用者看到的內容取決於下列條件：

- 你的 LINE 官方帳號是已驗證帳號（verified account）
- LINE 官方帳號個人檔案的公開 URL 已設定為可使用

若兩個條件皆符合，使用者會看到你 LINE 官方帳號的公開 URL 及 QR code。若不符合，使用者只會看到你 LINE 官方帳號的 QR code。你可以在 [LINE Official Account Manager](https://manager.line.biz/) 調整設定，將未驗證帳號變更為已驗證帳號，或啟用個人檔案的公開 URL。

<!-- tip end -->

### Opening the LINE Official Account's LINE VOOM and business profile 

你可以使用 LINE URL scheme 讓使用者開啟 LINE VOOM 與你 LINE 官方帳號的商業檔案頁面。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/bot-line-voom.png)

| LINE URL scheme | Description |
| --- | --- |
| https://line.me/R/home/public/main?id=`{LINE ID without @}` | 開啟 LINE 官方帳號的 LINE VOOM。 |
| https://line.me/R/home/public/profile?id=`{LINE ID without @}` | 開啟 LINE 官方帳號的商業檔案。 |
| https://line.me/R/home/public/post?id=`{LINE ID without @}`&postId=`{postId}` | 開啟 LINE 官方帳號的 LINE VOOM 貼文。請在 [LINE VOOM Studio](https://voom-studio.line.biz/) 中找到個別貼文的 post ID。 |

<!-- note start -->

**在 URL scheme 中排除小老鼠（@）前綴**

請將 URL scheme 中的 `{LINE ID without @}` 替換為你 LINE 官方帳號的 LINE ID。你可以指定 basic ID 或 [premium ID](https://developers.line.biz/en/glossary/#premium-id)。請從你 LINE 官方帳號的 LINE ID 中排除小老鼠（`@`）前綴。例如，若 LINE ID 為 `@linedevelopers`，請使用 `https://line.me/R/home/public/main?id=linedevelopers`。

<!-- note end -->

<!-- tip start -->

**確認 LINE 官方帳號的 LINE ID**

請在 [LINE Official Account Manager](https://manager.line.biz/) 中找到你 LINE 官方帳號的 LINE ID。詳情請參閱[分享你 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)。

<!-- tip end -->

<!-- tip start -->

**在 LINE VOOM 上發文與自訂商業檔案**

若要在 LINE VOOM 上發文或自訂你 LINE 官方帳號的商業檔案，請使用 [LINE VOOM Studio](https://voom-studio.line.biz/) 或 [LINE Official Account Manager](https://manager.line.biz/)。

<!-- tip end -->

### Opening a chat screen with a LINE Official Account 

你可以使用 LINE URL scheme 讓使用者開啟與你 LINE 官方帳號的聊天畫面。

| LINE URL scheme | Description |
| --- | --- |
| https://line.me/R/oaMessage/`{Percent-encoded LINE ID}` | 開啟與你 LINE 官方帳號的聊天畫面。 |
| https://line.me/R/oaMessage/`{Percent-encoded LINE ID}`/?`{text_message}` | 開啟與你 LINE 官方帳號的聊天畫面，並在訊息輸入欄位中填入 `{text_message}` 所設定的文字訊息。 |

<!-- note start -->

**「Percent-encoded LINE ID」與「text_message」必須經過百分比編碼（percent encoded）**

請確保 `{Percent-encoded LINE ID}` 與 `{text_message}` 已以 UTF-8 進行[百分比編碼（percent encoded）](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)。例如，若你要向 LINE ID 為 `@linedevelopers` 的 LINE 官方帳號傳送文字訊息「Hi there!」，請使用 `https://line.me/R/oaMessage/%40linedevelopers/?Hi%20there%21`。若改用未經百分比編碼的 LINE ID 也可運作，但已淘汰（deprecated）。

你可以指定 [Basic ID 或 Premium ID](https://help.linebiz.com/lineadshelp/s/article/L000001191?language=ja)（僅提供日文）作為你 LINE 官方帳號的 LINE ID。

<!-- note end -->

<!-- tip start -->

**確認 LINE 官方帳號的 LINE ID**

請在 [LINE Official Account Manager](https://manager.line.biz/) 中找到你 LINE 官方帳號的 LINE ID。詳情請參閱[分享你 LINE 官方帳號的 LINE ID](https://developers.line.biz/en/docs/messaging-api/sharing-bot/#share-the-line-id-of-your-line-official-account)。

<!-- tip end -->

### Sending text messages 

你可以使用 LINE URL scheme 設定一則文字訊息，讓使用者傳送給好友或 LINE 官方帳號。

| LINE URL scheme | Description |
| --- | --- |
| https://line.me/R/share?text=`{text_message}` | 開啟「分享給」畫面。使用者可選取好友、群組聊天或多人聊天，以傳送由 `{text_message}` 指定的文字訊息。使用者也可將文字傳送至 Keep Memo、LINE VOOM 與其他 app。 |

<!-- note start -->

**「text_message」必須經過百分比編碼（percent encoded）**

請確保 `{text_message}` 已以 UTF-8 進行[百分比編碼（percent encoded）](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)。例如，若你要傳送文字訊息「Hi there!」，請使用 `https://line.me/R/share?text=Hi%20there%21`。

<!-- note end -->

### Opening profile information 

你可以使用 LINE URL scheme 讓使用者開啟其「個人檔案」（My profile）畫面。在此畫面中，使用者可更新顯示名稱與狀態消息、設定其 LINE ID 並查看個人檔案設定。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/my-profile.png)

| LINE URL scheme | Description |
| --- | --- |
| `https://line.me/R/nv/profile` | 開啟使用者的「個人檔案」（My profile）畫面。 |
| `https://line.me/R/nv/profileSetId` | 開啟使用者的「LINE ID」畫面。透過此 URL scheme，你可以讓尚未設定 LINE ID 的使用者設定其 LINE ID。 |

### Opening common LINE screens 

你可以使用 LINE URL scheme 讓使用者開啟不同的 LINE 畫面，包括「聊天」分頁。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/shopping-tab-en.png)

| LINE URL scheme | Description |
| --- | --- |
| `https://line.me/R/nv/chat` | 開啟「聊天」分頁。 |
| `https://line.me/R/nv/commerce` | 開啟「購物」分頁。 |
| `https://line.me/R/nv/wallet` | 開啟「錢包」分頁。 |
| `https://line.me/R/nv/addFriends` | 開啟「加入好友」畫面。 |
| `https://line.me/R/nv/officialAccounts` | 開啟「LINE 官方帳號」畫面。 |
| `https://line.me/R/nv/timeline` | 開啟 LINE VOOM「追蹤中」畫面。 |

### Opening LINE settings 

你可以使用 LINE URL scheme 開啟不同的設定選單。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/settings.png)

| LINE URL scheme | Description |
| --- | --- |
| `https://line.me/R/nv/settings` | 開啟「設定」。 |
| `https://line.me/R/nv/settings/account` | 開啟「帳號」設定。顯示使用者的 LINE 帳號資訊。 |
| `https://line.me/R/nv/connectedApps` | 開啟「帳號」>「已授權的 app」。顯示授予已授權 app 的權限，並讓使用者解除與 app 的連結。 |
| `https://line.me/R/nv/connectedDevices` | 開啟「帳號」>「已連結的裝置」。 |
| `https://line.me/R/nv/settings/privacy` | 開啟「隱私設定」。 |
| `https://line.me/R/nv/settings/sticker` | 開啟「貼圖」設定。 |
| `https://line.me/R/nv/stickerShop/mySticker` | 開啟「貼圖」>「我的貼圖」。 |
| `https://line.me/R/nv/settings/themeSettingsMenu`（iOS）、`https://line.me/R/nv/settings/theme`（Android） | 開啟「主題」設定。<br />iOS 與 Android 的 scheme 不同。 |
| `https://line.me/R/nv/themeSettings` | 開啟「主題」>「我的主題」。 |
| `https://line.me/R/nv/notificationServiceDetail` | 開啟「通知」>「已授權的 app」。讓使用者設定已授權 app 的通知。 |
| `https://line.me/R/nv/settings/chatSettings` | 開啟「聊天」設定。 |
| `https://line.me/R/nv/suggestSettings` | 開啟「聊天」>「顯示建議」。 |
| `https://line.me/R/nv/settings/callSettings` | 開啟「通話」設定。 |
| `https://line.me/R/nv/settings/addressBookSync` | 開啟「好友」設定。 |
| `https://line.me/R/nv/settings/timelineSettings` | 開啟 LINE VOOM 設定。 |

### Opening Sticker Shop 

你可以使用 LINE URL scheme 讓使用者開啟 LINE 中的貼圖小舖，以鼓勵購買官方與創作者的貼圖組。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/sticker-shop-categories.png)

| LINE URL scheme | Description |
| --- | --- |
| https://line.me/R/shop/sticker/detail/`{package_id}` | 開啟貼圖組資訊畫面。請將 `{package_id}` 指定為 [LINE STORE](https://store.line.me/) 中該貼圖頁面 URL 所指定的數字。 |
| https://line.me/R/shop/category/`{category_id}` | 開啟指定分類的人氣排行榜。請將 `{category_id}` 指定為 [LINE STORE](https://store.line.me/) >「官方貼圖」中該分類頁面 URL 所指定的數字。 |
| https://line.me/R/shop/sticker/author/`{author_id}` | 開啟指定作者的貼圖組清單。請將 `{author_id}` 指定為 [LINE STORE](https://store.line.me/) 中該創作者頁面 URL 所指定的數字。 |
| `https://line.me/R/nv/stickerShop` | 開啟貼圖小舖 >「HOME」分頁。 |
| `https://line.me/R/shop/sticker/hot` | 開啟貼圖小舖 >「RANK」分頁。 |
| `https://line.me/R/shop/sticker/new` | 開啟貼圖小舖 >「NEW」分頁。 |
| `https://line.me/R/shop/sticker/event` | 開啟貼圖小舖 >「FREE」分頁。 |
| `https://line.me/R/shop/sticker/category` | 開啟貼圖小舖 >「CATEGORIES」分頁。 |

<!-- tip start -->

**建立你自己的貼圖組**

若要為使用者建立你自己的貼圖組，請造訪 [LINE Creators Market](https://creator.line.me/en/) 並使用 [LINE Sticker Maker](https://creator.line.me/en/stickermaker/) app。

<!-- tip end -->

### Opening Theme Shop 

你可以使用 LINE URL scheme 讓使用者開啟 LINE 中的主題小舖，以鼓勵購買官方與創作者的主題。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/theme-shop.png)

| LINE URL scheme | Description |
| --- | --- |
| https://line.me/R/shop/theme/detail?id=`{product_id}` | 開啟主題資訊畫面。請將 `{product_id}` 指定為 [LINE STORE](https://store.line.me/) 中該主題頁面 URL 所指定的 ID。例如，若你要開啟 [Matte White](https://store.line.me/themeshop/product/0bac8fed-4c75-40c5-9982-e9ecc3b9d191/en)`https://store.line.me/themeshop/product/0bac8fed-4c75-40c5-9982-e9ecc3b9d191/en`，請指定 `0bac8fed-4c75-40c5-9982-e9ecc3b9d191`。 |

### Opening a LIFF app 

你可以使用 LINE URL scheme 讓使用者開啟 LIFF app。LIFF app 是使用 [LINE Front-end Framework (LIFF)](https://developers.line.biz/en/docs/liff/overview/) 建置的網頁 app。

![](https://developers.line.biz/media/messaging-api/using-line-url-scheme/liff-app.png)

| LINE URL scheme | Description |
| --- | --- |
| https://liff.line.me/`{liffId}` | 開啟具有指定 LIFF ID 的 LIFF app。此 URL scheme 稱為 LIFF URL。 |
| https://liff.line.me/`{liffId}`/path_A/path_B/?key1=value1&key2=value2 | 開啟具有指定 LIFF ID 的 LIFF app。你可以將 `/path_A/path_B/?key1=value1&key2=value2` 作為額外資訊傳遞。 |

如需開啟 LIFF app 流程的詳細資訊，請參閱 LIFF 文件中的[開啟 LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)。

<!-- note start -->

**「https://line.me/R/app/{liffId}」與「line://app/{liffId}」已淘汰（deprecated）**

[LIFF v1](https://developers.line.biz/en/docs/liff/versioning-policy/#life-cycle-schedule) 中使用的下列 LIFF URL 格式已[淘汰（deprecated）](https://developers.line.biz/en/glossary/#deprecated)：

- `https://line.me/R/app/{liffId}`&nbsp;
- `line://app/{liffId}`&nbsp;

<!-- note end -->

### Opening a URL in an external browser 

透過查詢參數（query parameter），你可以讓使用者在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)中開啟 URL，而非在 [LINE 的 in-app 瀏覽器](https://developers.line.biz/en/glossary/#line-iab)中開啟。

<!-- note start -->

**這些查詢參數不支援 LIFF app**

這些查詢參數適用於從 LINE app 存取的所有 URL，但 LIFF app 除外。即使你將這些查詢參數加到 LIFF URL，也不會在外部瀏覽器中開啟。

<!-- note end -->

| URL with the query parameter | Description |
| --- | --- |
| https://example.com/?`openExternalBrowser=1` | 在外部瀏覽器中開啟目標 URL。 |
| https://example.com/?`openInAppBrowser=0` | 在 Chrome custom tab 中開啟目標 URL（僅支援 LINE for Android）。 |
