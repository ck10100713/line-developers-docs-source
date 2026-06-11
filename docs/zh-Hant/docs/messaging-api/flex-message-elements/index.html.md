# Flex Message 元素（Flex Message elements）

Flex Message 採用階層式的建構區塊結構，共分為三個層級。最上層是 [container](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#container)，接著是 [區塊（header、hero、body、footer）](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)，最後是 [元件（component）](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#component)。本頁將透過範例說明構成 Flex Message 的各種元素。

![Structure of a Flex Message](https://developers.line.biz/media/messaging-api/using-flex-messages/overviewSample.png)

## Container 

Container 是 Flex Message 最上層的建構區塊。可用的 container 類型如下：

| 類型 | 說明 |
| --- | --- |
| [Bubble](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#bubble) | 顯示單一訊息泡泡（message bubble）的 container |
| [Carousel](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#carousel) | 顯示多個並排訊息泡泡的 container |

### Bubble 

Bubble 是只包含單一訊息泡泡實例的 container。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Bubble](https://developers.line.biz/en/reference/messaging-api/#bubble)。

![Bubble example](https://developers.line.biz/media/messaging-api/flex-message-elements/bubbleSample.png)

### Carousel 

Carousel 是包含多個 bubble 的 container。您可以左右滑動瀏覽 carousel 中的各個 bubble。

![Carousel example](https://developers.line.biz/media/messaging-api/flex-message-elements/carouselSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Carousel](https://developers.line.biz/en/reference/messaging-api/#f-carousel)。

```json
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
            "wrap": true
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Go",
              "uri": "https://example.com"
            }
          }
        ]
      }
    },
    {
      "type": "bubble",
      "body": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "Hello, World!",
            "wrap": true
          }
        ]
      },
      "footer": {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "button",
            "style": "primary",
            "action": {
              "type": "uri",
              "label": "Go",
              "uri": "https://example.com"
            }
          }
        ]
      }
    }
  ]
}
```

## Block 

Block 是構成 bubble 的單位。可用的 block 類型如下：

| 類型   | 說明                                               |
| ------ | --------------------------------------------------------- |
| Header | 顯示訊息主旨或標題的區塊         |
| Hero   | 顯示主要圖片的區塊                        |
| Body   | 顯示主要訊息的區塊                      |
| Footer | 顯示按鈕與補充資訊的區塊 |

排列順序依序為 header、hero、body、footer。您不必在一則訊息泡泡中使用所有的 block 類型。但若有使用，每種 block 類型在一則訊息泡泡中只能使用一次。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中 [Bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 的 `header`、`hero`、`body` 與 `footer` 屬性。

![Block style example](https://developers.line.biz/media/messaging-api/flex-message-elements/blockStylesSample.png)

此 Flex Message 範例的 JSON 定義如下：

```json
{
  "type": "bubble",
  "styles": {
    "header": {
      "backgroundColor": "#ffaaaa"
    },
    "body": {
      "backgroundColor": "#aaffaa"
    },
    "footer": {
      "backgroundColor": "#aaaaff"
    }
  },
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "header"
      }
    ]
  },
  "hero": {
    "type": "image",
    "url": "https://example.com/flex/images/image.jpg",
    "size": "full",
    "aspectRatio": "2:1"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "body"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "footer"
      }
    ]
  }
}
```

## Component 

Component 是構成 [block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) 的單位。可用的元件如下：

| 元件 | 說明 |
| --- | --- |
| [Box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) | 此元件定義水平或垂直的版面配置方向，並將多個元件組合在一起。 |
| [Button](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#button) | 此元件繪製按鈕。當使用者點擊按鈕時，會執行指定的動作。 |
| [Image](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image) | 此元件繪製圖片。 |
| [Video](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#video) | 此元件繪製影片。 |
| [Icon](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#icon) | 此元件繪製圖示。 |
| [Text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) | 此元件繪製文字字串。您可以指定字型顏色、大小與粗細。 |
| [Span](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#span) | 此元件以不同樣式繪製多個文字字串。您可以指定字型顏色、大小、粗細與裝飾。 |
| [Separator](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#separator) | 此元件繪製分隔線。 |
| [Filler](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#filler)（已淘汰） | 此元件繪製空白空間。 |

### Box 

此元件定義水平或垂直的版面配置方向，並將多個元件組合在一起。可包含任何元件，包括 box 本身。如需版面配置的詳細資訊，請參閱 [Flex Message 版面配置](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Box](https://developers.line.biz/en/reference/messaging-api/#box)。

### Button 

此元件繪製按鈕。您可以設定當使用者點擊按鈕時要執行的[動作（action）](https://developers.line.biz/en/docs/messaging-api/actions/)。如下所示，您有三種按鈕樣式可供選擇。所有按鈕樣式的按鈕顏色都可以變更。

![Button example](https://developers.line.biz/media/messaging-api/flex-message-elements/buttonSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Button](https://developers.line.biz/en/reference/messaging-api/#button)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "button",
        "style": "primary",
        "action": {
          "type": "uri",
          "label": "Primary style button",
          "uri": "https://example.com"
        }
      },
      {
        "type": "button",
        "style": "secondary",
        "action": {
          "type": "uri",
          "label": "Secondary style button",
          "uri": "https://example.com"
        }
      },
      {
        "type": "button",
        "style": "link",
        "action": {
          "type": "uri",
          "label": "Link style button",
          "uri": "https://example.com"
        }
      }
    ]
  }
}
```

### Image 

此元件繪製圖片。

![Image example](https://developers.line.biz/media/messaging-api/flex-message-elements/imageSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Image](https://developers.line.biz/en/reference/messaging-api/#f-image)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "image",
        "url": "https://example.com/flex/images/image.jpg",
        "size": "md"
      }
    ]
  }
}
```

### Video 

此元件繪製影片。如需使用影片的詳細資訊，請參閱[建立包含影片的 Flex Message](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/)。

![Video example](https://developers.line.biz/media/messaging-api/flex-message-elements/video-sample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Video](https://developers.line.biz/en/reference/messaging-api/#f-video)。

```json
{
  "type": "bubble",
  "size": "mega",
  "hero": {
    "type": "video",
    "url": "https://example.com/video.mp4",
    "previewUrl": "https://example.com/video_preview.jpg",
    "altContent": {
      "type": "image",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "url": "https://example.com/image.jpg"
    },
    "aspectRatio": "20:13"
  }
}
```

### Icon 

此元件繪製用於裝飾相鄰文字的圖示。您只能在 [baseline box](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#baseline-box) 中使用此元件。

![Icon example](https://developers.line.biz/media/messaging-api/flex-message-elements/iconSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Icon](https://developers.line.biz/en/reference/messaging-api/#icon)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://example.com/flex/images/icon.png",
            "size": "md"
          },
          {
            "type": "text",
            "text": "The quick brown fox jumps over the lazy dog",
            "size": "md"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://example.com/flex/images/icon.png",
            "size": "lg"
          },
          {
            "type": "text",
            "text": "The quick brown fox jumps over the lazy dog",
            "size": "lg"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://example.com/flex/images/icon.png",
            "size": "xl"
          },
          {
            "type": "text",
            "text": "The quick brown fox jumps over the lazy dog",
            "size": "xl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://example.com/flex/images/icon.png",
            "size": "xxl"
          },
          {
            "type": "text",
            "text": "The quick brown fox jumps over the lazy dog",
            "size": "xxl"
          }
        ]
      },
      {
        "type": "box",
        "layout": "baseline",
        "contents": [
          {
            "type": "icon",
            "url": "https://example.com/flex/images/icon.png",
            "size": "3xl"
          },
          {
            "type": "text",
            "text": "The quick brown fox jumps over the lazy dog",
            "size": "3xl"
          }
        ]
      }
    ]
  }
}
```

### Text 

此元件繪製文字字串。您可以指定文字的顏色、大小與粗細。您可以[換行](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text-wrap)較長的文字，並調整換行文字的行距。

![Text example](https://developers.line.biz/media/messaging-api/flex-message-elements/textSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Text](https://developers.line.biz/en/reference/messaging-api/#f-text)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Closing the distance",
        "size": "md",
        "align": "center",
        "color": "#ff0000"
      },
      {
        "type": "text",
        "text": "Closing the distance",
        "size": "lg",
        "align": "center",
        "color": "#00ff00"
      },
      {
        "type": "text",
        "text": "Closing the distance",
        "size": "xl",
        "align": "center",
        "weight": "bold",
        "color": "#0000ff"
      }
    ]
  }
}
```

#### Text wrapping 

預設情況下，溢出的文字會以省略號截斷。以下是長文字顯示方式的範例。

![Example without text wrapping](https://developers.line.biz/media/messaging-api/flex-message-elements/nowrapSample.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
      }
    ]
  }
}
```

為了避免截斷，您可以換行較長的文字。要套用文字換行，請將 `wrap` 屬性設為 `true`。您可以使用換行字元（`\n`）讓部分文字從新的一行開始。以下是套用文字換行與換行字元的 Flex Message 範例。

![Example with text wrapping](https://developers.line.biz/media/messaging-api/flex-message-elements/wrap-sample.png)

<!-- note start -->

**注意**

文字結尾的換行字元（`\n`）可能會因裝置環境不同而呈現不同的顯示效果。

<!-- note end -->

文字換行範例的 JSON 定義如下。新增了 `wrap` 屬性並設為 `true`。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\n tempor incididunt ut labore et dolore magna aliqua.",
        "wrap": true
      }
    ]
  }
}
```

##### Line spacing in a text 

當您換行文字時，可以使用 `lineSpacing` 屬性指定換行文字的行距。

<!-- note start -->

**行距的適用範圍**

行距不會套用至第一行的上方與最後一行的下方。

<!-- note end -->

![Example of increasing the line spacing in a text](https://developers.line.biz/media/messaging-api/flex-message-elements/line-spacing-sample.png)

此 Flex Message 範例的 JSON 定義如下。新增了 `lineSpacing` 屬性並設為 `20px`。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod\n tempor incididunt ut labore et dolore magna aliqua.",
        "wrap": true,
        "lineSpacing": "20px"
      }
    ]
  }
}
```

### Span 

此元件以不同樣式繪製多個文字字串。您可以指定每段文字的顏色、大小、粗細與裝飾。Span 會設定於 [text](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#text) 的 `contents` 屬性中。

![Span examples](https://developers.line.biz/media/messaging-api/flex-message-elements/spanSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Span](https://developers.line.biz/en/reference/messaging-api/#span)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "text",
        "text": "hello, world",
        "contents": [
          {
            "type": "span",
            "text": "Hello, world!",
            "decoration": "line-through"
          },
          {
            "type": "span",
            "text": "\nClosing",
            "color": "#ff0000",
            "size": "sm",
            "weight": "bold",
            "decoration": "none"
          },
          {
            "type": "span",
            "text": " "
          },
          {
            "type": "span",
            "text": "the",
            "size": "lg",
            "color": "#00ff00",
            "decoration": "underline",
            "weight": "bold"
          },
          {
            "type": "span",
            "text": " "
          },
          {
            "type": "span",
            "text": "distance",
            "color": "#0000ff",
            "weight": "bold",
            "size": "xxl"
          }
        ],
        "wrap": true,
        "align": "center"
      }
    ]
  }
}
```

### Separator 

此元件在 [box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) 內繪製分隔線。若包含在水平版面配置的 box 中，會繪製一條垂直線；同理，若包含在垂直版面配置的 box 中，則會繪製一條水平線。

![Separator example](https://developers.line.biz/media/messaging-api/flex-message-elements/separatorSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Separator](https://developers.line.biz/en/reference/messaging-api/#separator)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "spacing": "md",
        "contents": [
          {
            "type": "text",
            "text": "orange"
          },
          {
            "type": "separator"
          },
          {
            "type": "text",
            "text": "apple"
          }
        ]
      },
      {
        "type": "separator"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "spacing": "md",
        "contents": [
          {
            "type": "text",
            "text": "grape"
          },
          {
            "type": "separator"
          },
          {
            "type": "text",
            "text": "lemon"
          }
        ]
      }
    ]
  }
}
```

### Filler 

<!-- warning start -->

**Filler 已淘汰**

若要新增空間，請改用各元件的屬性，而非新增 filler。如需詳細資訊，請參閱[元件位置](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-position)。

<!-- warning end -->

此元件繪製空白空間。您可以在 [box](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box) 內的元件之間、之前或之後放置空白空間。以下範例示範一個 box，內含兩張[圖片](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#image)，並在兩張圖片之間放置一個 filler。

![Filler example](https://developers.line.biz/media/messaging-api/flex-message-elements/fillerSample.png)

此 Flex Message 範例的 JSON 定義如下。如需 JSON schema 的詳細資訊，請參閱 Messaging API 參考文件中的 [Filler](https://developers.line.biz/en/reference/messaging-api/#filler)。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "image",
        "url": "https://example.com/flex/images/image.jpg"
      },
      {
        "type": "filler"
      },
      {
        "type": "image",
        "url": "https://example.com/flex/images/image.jpg"
      }
    ]
  }
}
```

## Learn more 

- [傳送 Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)
- [Flex Message 版面配置](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)
- [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)（Messaging API 參考文件）
