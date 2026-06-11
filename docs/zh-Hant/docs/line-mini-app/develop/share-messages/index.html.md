# 實作自訂動作按鈕（Implementing a custom action button）

LINE MINI App 在 (A) [header](https://developers.line.biz/en/docs/line-mini-app/discover/ui-components/#header) 中內建了一個動作按鈕，讓使用者可以將目前開啟的頁面分享給好友。由於這個動作按鈕是由 LINE 實作並預設顯示，按鈕的行為與分享訊息的內容無法自訂。

不過，若你在 (B) body 中實作自訂動作按鈕，就可以在分享 LINE MINI App 之前自訂分享訊息的內容。

![](https://developers.line.biz/media/line-mini-app/mini_concept.png)

## Guidelines 

當你實作自訂動作按鈕以傳送自訂分享訊息時，請遵循以下準則，協助使用者快速且準確地理解訊息的內容。

<!-- note start -->

**Note**

如果因為你所提供服務的特性而無法滿足此處的設計需求，請透過 [mini_request@linecorp.com](mailto:mini_request@linecorp.com) 與我們聯絡。

<!-- note end -->

<!-- note start -->

**LINE MINI App 的 LIFF URL 已變更**

自 [2023 年 12 月 13 日](https://developers.line.biz/en/news/2023/12/13/change-of-liff-url-for-line-mini-app/)起，LINE MINI App 的 LIFF URL 已變更為 `https://miniapp.line.me/{liffId}`。

如果使用者存取既有的 `https://liff.line.me/{liffId}`，LINE MINI App 同樣會開啟。因此，你可以繼續使用先前已發行的 QR code。

<!-- note end -->

### Using share target picker 

在 body 中實作自訂動作按鈕，並在按鈕被點選時顯示 target picker（選擇群組或好友的畫面）。當使用者在 target picker 中選擇收件對象後，即可傳送由開發者建立的分享訊息，例如 [Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)。

![target picker](https://developers.line.biz/media/liff/share-target-picker_tobe_en.png)

關於使用 share target picker 的詳細指南，請參閱[傳送訊息給使用者的好友](https://developers.line.biz/en/docs/liff/developing-liff-apps/#share-target-picker)。

### Custom share message format 

使用 Flex Message 的 [Bubble](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#bubble) 容器來組成自訂分享訊息。請勿使用 Flex Message 的 [Carousel](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#carousel) 容器。

自訂分享訊息包含 [standard type](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/#standard) 與 [image list type](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/#image-list)，兩者皆分別劃分為以下 A 到 F 的區塊：

![](https://developers.line.biz/media/line-mini-app/mini_design_flex_msg_common.png)

| Label | Section | Required | Description |
| --- | --- | --- | --- |
| A | Image | Optional | 圖片尺寸必須夠小，使整則訊息能完整顯示於畫面內，無需捲動。 |
| B | Title | Required | 摘要訊息的內容。 |
| C | Subtitle | \* | 這是你訊息的副標題。 |
| D | Detail | \* | 由標籤與說明所構成的項目清單：standard type 與 image list type 的項目數量上限不同：<ul><li>Standard type：最多 10 個項目的清單</li><li>Image list type：最多 5 個項目的清單</li></ul> |
| E | Button | Required | <ul><li>你最多可以插入三個按鈕。</ll><li>至少應設定一個按鈕來顯示詳述你想分享內容的頁面（詳細頁面）。</li></ul> |
| F | Footer | Required | 由你的 LINE MINI App 圖示、LINE MINI App 名稱以及一張圖片 ![>](https://vos.line-scdn.net/service-notifier/footer_go_btn.png) 組成。請勿變更此圖片。指定 URI action，使使用者點選此圖片時會顯示 LINE MINI App 的首頁（`https://miniapp.line.me/{your-liffId}`）。 |

\* 你必須插入 C（副標題）或 D（詳細區塊）其中之一。你也可以兩者皆使用。

#### Standard type 

對於 standard type 的 Flex Message，請遵循以下準則：

關於 JSON 檔案範例，請參閱[符合準則的 JSON 檔案範例](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages-standard/)。

<!-- note start -->

**Note**

- 只能在按鈕（E）與 footer（F）的指定元件上設定 action。
- 請勿變更此處未說明的任何屬性。

<!-- note end -->

![](https://developers.line.biz/media/line-mini-app/mini_design_flex_msg_standard.png)

##### Standard type - Image (A) 

將圖片（A）放在 hero block 中。

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| A | Image | [Hero block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) > [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "{URL}"`</li><li>`"size": "full"`</li><li>`"aspectRatio": "{width}:{height}"`<br>但 `{height}` 請設為 `{width} * 2` 或更小。</li><li>`"aspectMode": "cover"`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { // Hero block
        // Image (A)
        "type": "image",
        "url": "https://example.com/hero-image.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
    },
    "body": {. . .}
}
```

##### Standard type - Body 

依以下方式指定包含標題（B）、副標題（C）、詳細（D）與按鈕（E）的 body block：

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| - | - | [Body block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) > [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "md"`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": { // Body block
        // Box
        "type": "box",
        "layout": "vertical",
        "contents": [ ... ],
        "spacing": "md"
    }
}
```

##### Standard type - Title (B) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| B | Title | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "none"`</li></ul> |
| B | Title | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Title}"`<br>文字最大行數：2</li><li>`"size": "lg"`</li><li>`"color": "#000000"`</li><li>`"weight": "bold"`</li><li>`"wrap": true`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Text
                        "type": "text",
                        "text": "Main title",
                        "size": "lg",
                        "color": "#000000",
                        "weight": "bold",
                        "wrap": true
                    }
                ],
                "spacing": "none"
            }
        ],
        "spacing": "md"
    }
}
```

##### Standard type - Sub-title (C) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| C | Sub-title | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "none"`</li></ul> |
| C | Sub-title | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Sub-title}"`<br>文字最大行數：2</li><li>`"size": "sm"`</li><li>`"color": "#999999"`</li><li>`"wrap": true`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                ...
            },
            {   // Sub-title (C) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Text
                        "type": "text",
                        "text": "Sub-title",
                        "size": "sm",
                        "color": "#999999",
                        "wrap": true
                    }
                ],
                "spacing": "none"
            }
        ],
        "spacing": "md"
    }
}
```

##### Standard type - Details (D) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| D | Details | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "sm"`</li><li>`"margin": "lg"`</li><li>`"flex": 1`</li></ul> |
| D | Details - item | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 這是只包含一組 D-1 與 D-2 的 box。<ul><li>`"layout": "horizontal"`</li><li>`"spacing": "sm"`</li><li>`"flex": 1`</li></ul> |
| D-1 | Details - label | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Label}"`<br>文字最大行數：1</li><li>`"size": "sm"`</li><li>`"color": "#555555"`</li><li>`"wrap": false`</li><li>`"flex": 20`</li></ul> |
| D-2 | Details - description | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Description}"`<br>文字最大行數：1</li><li>`"size": "sm"`</li><li>`"color": "#111111"`</li><li>`"wrap": false`</li><li>`"flex": 55`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                ...
            },
            {   // Sub-title (C) - Box
                ...
            },
            {   // Details (D) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Label (D-1) - Box
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {   // Text
                                "type": "text",
                                "text": "Label 1",
                                "size": "sm",
                                "color": "#555555",
                                "wrap": false
                                "flex": 20
                            },
                            {   Description
                                "type": "text",
                                "text": "Description 1",
                                "size": "sm",
                                "color": "#111111",
                                "wrap": false,
                                "flex": 55
                            }
                        ],
                        "flex": 1,
                        "spacing": "sm"
                    },
                    {   // Detail (D-2) - Box
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {   // Text
                                "type": "text",
                                "text": "Label 2",
                                "size": "sm",
                                "color": "#555555",
                                "wrap": false
                                "flex": 20
                            },
                            {   // Text
                                "type": "text",
                                "text": "Description 2",
                                "size": "sm",
                                "color": "#111111",
                                "wrap": false,
                                "flex": 55
                            }
                        ],
                        "flex": 1,
                        "spacing": "sm"
                    }
                ],
                "spacing": "sm",
                "margin": "lg",
                "flex": 1
            }
        ],
        "spacing": "md"
    }
}
```

##### Standard type - Button (E) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| E | Button | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 包含 E-1 與 E-2 的 box。<ul><li>`"layout": "vertical"`</li><li>`"spacing": "xs"`</li><li>`"margin": "lg"`</li></ul> |
| E-1 | Button<br>（僅使用 link 樣式時） | [Button](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#button) | <ul><li>`"style": "link"`</li><li>`"height": "sm"`</li><li>`"color": "{Text Color}"`</li><li>`"action" : { ... }`<br>指定 URI action，使使用者點選此按鈕時會顯示 LINE MINI App 頁面。如果該頁面不是你 LINE MINI App 的首頁，你必須指派一個[永久連結（permanent link）](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)。</li></ul> |
| E-2 | Button<br>（使用 primary 樣式時） | [Button](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#button) | <ul><li>最上方的按鈕指定 `"style": "primary"`，其他所有按鈕指定 `"style": "link"`。不可使用 `"secondary"`。</li><li>`"height": "md"`</li><li>`"color": "{Text or Background Color}"`</li><li>`"action" : { ... }`<br>指定 URI action，使使用者點選此按鈕時會顯示 LINE MINI App 頁面。如果該頁面不是你 LINE MINI App 的首頁，你必須指派一個[永久連結（permanent link）](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)。</li></ul></li></ul> |

使用 primary 樣式時：

```json
{
    "type": "bubble",
    "hero": { ... }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                ...
            },
            {   // Sub-title (C) - Box
                ...
            },
            {   // Details (D) - Box
                ...
            },
            {   // Button (E) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Button (primary)
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "View details",
                            "uri": "https://miniapp.line.me/123456-abcedfg"
                        },
                        "style": "primary",
                        "height": "md",
                        "color": "#17c950"
                    },
                    {   // Button (link)
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "Share",
                            "uri": "https://miniapp.line.me/123456-abcedfg/share"
                        },
                        "style": "link",
                        "height": "md",
                        "color": "#469fd6"
                    }
                ],
                "spacing": "xs",
                "margin": "lg"
            }
        ],
        "spacing": "md"
    }
}
```

##### Standard type - Footer (F) 

將 footer（F）放在 footer block 中。

| Label | Section | Element | Description |
| --- | --- | --- | --- |
| - | - | [Footer block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) > [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li></ul> |
| - | - | [Separator](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#separator) | <ul><li>`"color": "#f0f0f0"`</li></ul> |
| F | Footer | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 包含 F-1 到 F-3 的 box。<ul><li>`"layout": "horizontal"`</li><li>`"flex": 1`</li><li>`"spacing": "md"`</li><li>`"margin": "md"`</li></ul> |
| F-1 | LINE MINI App icon | [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "{Image URL}"`</li><li>`"flex": 1`</li><li>`"gravity": "center"`</li></ul> |
| F-2 | LINE MINI App name | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{LINE MINI App Name}"`<br>文字最大行數：1</li><li>`"flex": 19`</li><li>`"size": "xs"`</li><li>`"color": "#999999"`</li><li>`"weight": "bold"`</li><li>`"gravity": "center"`</li><li>`"wrap": false`</li></ul> |
| F-3 | ![>](https://vos.line-scdn.net/service-notifier/footer_go_btn.png) | [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "https://vos.line-scdn.net/service-notifier/footer_go_btn.png"`</li><li>`"flex": 1`</li><li>`"gravity": "center"`</li><li>`"size": "xxs"`</li><li>`"action" : { ... }`<br>指定 URI action，使使用者點選此圖片時會顯示 LINE MINI App 首頁（`https://miniapp.line.me/{your-liffId}`）。</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": { ... },
    "footer": { // Footer block
        // Box
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Separator
                "type": "separator",
                "color": "#f0f0f0"
            },
            {   // Footer (F) - Box
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {   // LINE MINI App icon (F-1)
                        "type": "image",
                        "url": "https://example.com/line-mini-app-icon.png",
                        "flex": 1,
                        "gravity": "center"
                    },
                    {   // LINE MINI App name (F-2)
                        "type": "text",
                        "text": "Service name",
                        "flex": 19,
                        "size": "xs",
                        "color": "#999999",
                        "weight": "bold",
                        "gravity": "center",
                        "wrap": false
                    },
                    {   // > (F-3)
                        "type": "image",
                        "url": "https://vos.line-scdn.net/service-notifier/footer_go_btn.png",
                        "flex": 1,
                        "gravity": "center",
                        "size": "xxs",
                        "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://miniapp.line.me/123456-abcedfg"
                        }
                    }
                ],
                "flex": 1,
                "spacing": "md",
                "margin": "md"
            }
        ]
    }
}
```

#### Image list type 

對於 image list type 的 Flex Message，請遵循以下準則：

關於 JSON 檔案範例，請參閱[符合準則的 JSON 檔案範例](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages-standard/)。

<!-- note start -->

**Note**

- 只能在按鈕（E）與 footer（F）的指定元件上設定 action。
- 請勿變更此處未說明的任何屬性。

<!-- note end -->

![](https://developers.line.biz/media/line-mini-app/mini_design_flex_msg_list.png)

##### Image list type - Image (A) 

將圖片（A）放在 hero block 中。

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| A | Image | [Hero block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) > [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "{Image URL}"`</li><li>`"size": "full"`</li><li>`"aspectRatio": "{width}:{height}"`<br>但 `{height}` 請設為 `{width} * 2` 或更小。</li><li>`"aspectMode": "cover"`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { // Hero block
        // Image (A)
        "type": "image",
        "url": "https://example.com/hero-image.png",
        "size": "full",
        "aspectRatio": "20:13",
        "aspectMode": "cover"
    },
    "body": {. . .}
}
```

##### Image list type - Body 

依以下方式指定包含標題（B）、副標題（C）、詳細（D）與按鈕（E）的 body block：

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| - | - | [Body block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) > [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "md"`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": { // Body block
        // Box
        "type": "box",
        "layout": "vertical",
        "contents": [ ... ],
        "spacing": "md"
    }
}
```

##### Image list type - Title (B) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| B | Title | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "none"`</li></ul> |
| B | Title | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Title}"`<br>文字最大行數：2</li><li>`"size": "lg"`</li><li>`"color": "#000000"`</li><li>`"weight": "bold"`</li><li>`"wrap": true`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Text
                        "type": "text",
                        "text": "Main title",
                        "size": "lg",
                        "color": "#000000",
                        "weight": "bold",
                        "wrap": true
                    }
                ],
                "spacing": "none"
            }
        ],
        "spacing": "md"
    }
}
```

##### Image list type - Sub-title (C) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| C | Sub-title | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "none"`</li></ul> |
| C | Sub-title | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Sub-title}"`<br>文字最大行數：2</li><li>`"size": "sm"`</li><li>`"color": "#999999"`</li><li>`"wrap": true`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                ...
            },
            {   // Sub-title (C) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Text
                        "type": "text",
                        "text": "Sub-title",
                        "size": "sm",
                        "color": "#999999",
                        "wrap": true
                    }
                ],
                "spacing": "none"
            }
        ],
        "spacing": "md"
    }
}
```

##### Image list type - Details (D) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| D | Details | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li><li>`"spacing": "xl"`</li><li>`"margin": "lg"`</li></ul> |
| - | Details - Item | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 只包含一組 D-1 到 D-4 的 box。<ul><li>`"layout": "horizontal"`</li><li>`"flex": 1`</li></ul> |
| D-1 | Details - Image | [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "{Image URL}"`</li><li>`"flex": 3`</li><li>`"size": "sm"`</li><li>`"aspectRatio": "1:1"`</li><li>`"aspectMode": "cover"`</li></ul> |
| - | Details - Text area | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 包含 D-2 到 D-4 的 box。<ul><li>`"layout": "vertical"`</li><li>`"flex": 8`</li><li>`"spacing": "xs"`</li><li>`"margin": "md"`</li></ul> |
| D-2 | Details - General text | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{General Text}"`</li><li>`"size": "md"`</li><li>`"color": "#111111"`</li></ul> |
| D-3 | Details - Text to emphasize | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{Text to emphasize}"`</li><li>`"size": "md"`</li><li>`"color": "#111111"`</li></ul> |
| D-4 | Details - Image+text | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 包含 D-4 的圖片與文字的 box：<ul><li>`"layout": "horizontal"`</li><li>`"flex": 1`</li></ul>D-4 的 [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image)：<ul><li>`"flex": 8`</li><li>`"url": "{Image URL}"`</li><li>`"gravity": "center"`</li><li>`"size": "xxs"`</li><li>`"aspectRatio": "1:1"`</li></ul>D-4 的 [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text)：<ul><li>`"flex": 85`</li><li>`"margin": "xs"`</li><li>`"text": "{Text}"`</li><li>`"size": "sm"`</li><li>`"color": "{Color}"`</li><li>`"gravity": "center"`</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                ...
            },
            {   // Sub-title (C) - Box
                ...
            },
            {   // Details (D) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Item
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                            {   // Image
                                "type": "image",
                                "url": "https://example.com/item-image01.png",
                                "flex": 3,
                                "size": "sm",
                                "aspectRatio": "1:1",
                                "aspectMode": "cover"
                            },
                            {   // Text area
                                "type": "box",
                                "layout": "vertical",
                                "contents": [
                                    {   // General text (D-2)
                                        "type": "text",
                                        "text": "General text",
                                        "size": "md",
                                        "color": "#111111"
                                    },
                                    {   // Text to emphasize (D-3)
                                        "type": "text",
                                        "text": "Text to emphasize",
                                        "size": "md",
                                        "color": "#111111"
                                    },
                                    {   // Image+text (D-4)
                                        "type": "box",
                                        "layout": "horizontal",
                                        "contents": [
                                            {   // Image
                                                "type": "image",
                                                "url": "https://example.com/item-image02.png",
                                                "flex": 8,
                                                "gravity": "center",
                                                "size": "xxs",
                                                "aspectRatio": "1:1"
                                            },
                                            {   // Text
                                                "type": "text",
                                                "text": "Text",
                                                "flex": 85,
                                                "gravity": "center",
                                                "size": "sm",
                                                "color": "#17c950",
                                                "margin": "xs"
                                            }
                                        ],
                                        "flex": 1
                                    }
                                ],
                                "flex": 8,
                                "spacing": "xs",
                                "margin": "md"
                            }
                        ],
                        "flex": 1
                    }
                ],
                "spacing": "xl",
                "margin": "lg"
            }
        ],
        "spacing": "md"
    }
}
```

##### Image list type - Button (E) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| E | Button | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 包含 E-1 與 E-2 的 box。<ul><li>`"layout": "vertical"`</li><li>`"spacing": "xs"`</li></ul> |
| E-1 | Button<br>（僅使用 link 時） | [Button](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#button) | <ul><li>`"style": "link"`</li><li>`"height": "sm"`</li><li>`"color": "{Text Color}"`</li><li>`"action" : { ... }`<br>指定 URI action，使使用者點選此按鈕時會顯示 LINE MINI App 頁面。當要顯示的頁面不是你 LINE MINI App 的首頁時，你必須指派[永久連結（permanent link）](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)。</li></ul> |
| E-2 | Button<br>（使用 primary 樣式時） | [Button](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#button) | <ul><li>最上方的按鈕指定 `"style": "primary"`，其他按鈕指定 `"style": "link"`。不可使用 `"secondary"`。</li><li>`"height": "md"`</li><li>`"color": "{Text or Background Color}"`</li><li>`"action" : { ... }`<br>指定 URI action，使使用者點選此按鈕時會顯示 LINE MINI App 頁面。當要顯示的頁面不是你 LINE MINI App 的首頁時，你必須指派[永久連結（permanent link）](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)。</li></ul></li></ul> |

使用 primary 樣式時：

```json
{
    "type": "bubble",
    "hero": { ... }
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Title (B) - Box
                ...
            },
            {   // Sub-title (C) - Box
                ...
            },
            {   // Details (D) - Box
                ...
            },
            {   // Button (E) - Box
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {   // Button (primary)
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "View details",
                            "uri": "https://miniapp.line.me/123456-abcedfg"
                        },
                        "style": "primary",
                        "height": "md",
                        "color": "#17c950"
                    },
                    {   // Button (link)
                        "type": "button",
                        "action": {
                            "type": "uri",
                            "label": "Share",
                            "uri": "https://miniapp.line.me/123456-abcedfg/share"
                        },
                        "style": "link",
                        "height": "md",
                        "color": "#469fd6"
                    }
                ],
                "spacing": "xs"
            }
        ],
        "spacing": "md"
    }
}
```

##### Image list type - Footer (F) 

| Label | Section | Type | Description |
| --- | --- | --- | --- |
| - | - | [Footer block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) > [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | <ul><li>`"layout": "vertical"`</li></ul> |
| - | - | [Separator](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#separator) | <ul><li>`"color": "#f0f0f0"`</li></ul> |
| F | Footer | [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 包含 F-1 到 F-3 的 box。<ul><li>`"layout": "horizontal"`</li><li>`"flex": 1`</li><li>`"spacing": "md"`</li><li>`"margin": "md"`</li></ul> |
| F-1 | LINE MINI App icon | [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "{Image URL}"`</li><li>`"flex": 1`</li><li>`"gravity": "center"`</li></ul> |
| F-2 | LINE MINI App name | [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | <ul><li>`"text": "{LINE MINI App Name}"`<br>文字最大行數：1</li><li>`"flex": 19`</li><li>`"size": "xs"`</li><li>`"color": "#999999"`</li><li>`"weight": "bold"`</li><li>`"gravity": "center"`</li><li>`"wrap": false`</li></ul> |
| F-3 | ![>](https://vos.line-scdn.net/service-notifier/footer_go_btn.png) | [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | <ul><li>`"url": "https://vos.line-scdn.net/service-notifier/footer_go_btn.png"`</li><li>`"flex": 1`</li><li>`"gravity": "center"`</li><li>`"size": "xxs"`</li><li>`"action" : { ... }`<br>指定 URI action，使使用者點選此圖片時會顯示 LINE MINI App 首頁（`https://miniapp.line.me/{your-liffId}`）。</li></ul> |

```json
{
    "type": "bubble",
    "hero": { ... },
    "body": { ... },
    "footer": { // Footer block
        // Box
        "type": "box",
        "layout": "vertical",
        "contents": [
            {   // Separator
                "type": "separator",
                "color": "#f0f0f0"
            },
            {   // Footer (F) - Box
                "type": "box",
                "layout": "horizontal",
                "contents": [
                    {   // LINE MINI App icon (F-1)
                        "type": "image",
                        "url": "https://example.com/line-mini-app-icon.png",
                        "flex": 1,
                        "gravity": "center"
                    },
                    {   // LINE MINI App name (F-2)
                        "type": "text",
                        "text": "Service name",
                        "flex": 19,
                        "size": "xs",
                        "color": "#999999",
                        "weight": "bold",
                        "gravity": "center",
                        "wrap": false
                    },
                    {   // > (F-3)
                        "type": "image",
                        "url": "https://vos.line-scdn.net/service-notifier/footer_go_btn.png",
                        "flex": 1,
                        "gravity": "center",
                        "size": "xxs",
                        "action": {
                            "type": "uri",
                            "label": "action",
                            "uri": "https://miniapp.line.me/123456-abcedfg"
                        }
                    }
                ],
                "flex": 1,
                "spacing": "md",
                "margin": "md"
            }
        ]
    }
}
```
