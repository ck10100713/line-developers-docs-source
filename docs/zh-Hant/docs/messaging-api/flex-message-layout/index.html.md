# Flex Message 版面配置（Flex Message layout）

你可以依據 [CSS Flexible Box（CSS flexbox）](https://www.w3.org/TR/css-flexbox-1/)的規範，建構複雜的 Flex Message 版面配置。CSS flexbox 中的 flex 容器與 flex 項目，分別對應到 [box 元件](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box)與 Flex Message 的各個元件。

了解如何組合你的 Flex Message 版面配置。關於 JSON 結構描述的詳細資訊，請參閱 Messaging API 參考文件中的 [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)。

## Box component orientation 

[Box 元件](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box)有兩種方向：橫向（landscape）與縱向（portrait）。橫向模式的盒子稱為水平盒子（horizontal box），縱向模式的盒子稱為垂直盒子（vertical box）。方向會決定盒子的主軸（main axis）與交叉軸（cross axis）。主軸與方向平行，水平盒子的主軸為水平，垂直盒子的主軸為垂直。交叉軸則與主軸垂直。主軸會決定盒子的子元件如何排列。詳細資訊請參閱[以自由空間排列子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#justify-property)。

你需要在 box 元件的 `layout` 屬性中指定方向。除了水平盒子與垂直盒子之外，也提供基線盒子（baseline box）。

| Box | `layout` 屬性 | 主軸 | 交叉軸 | 子元件擺放方式 |
| --- | --- | --- | --- | --- |
| 水平盒子 | `horizontal` | 水平 | 垂直 | 水平排列 |
| 垂直盒子 | `vertical` | 垂直 | 水平 | 垂直排列 |
| 基線盒子 | `baseline` | 水平 | 垂直 | 水平排列<br />詳細資訊請參閱[基線盒子中的子元件](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#baseline-box)。 |

### Child components in baseline boxes 

基線盒子的行為方式與水平盒子相同。不過，基線盒子的行為在以下幾方面與水平盒子不同：

#### Vertical alignment position 

基線盒子中的元件會以相同的基線進行垂直對齊。這表示無論字型大小如何，所有子元件都使用相同的基線。[icon 元件](https://developers.line.biz/en/reference/messaging-api/#icon)的基線是圖示影像的底部。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/baseline.png)

#### Unavailable properties 

在基線盒子元件的子元件中，你無法使用 `gravity` 與 `offsetBottom` 屬性。

## Available child components 

盒子的 `layout` 屬性會決定你可以將哪些元件用作 box 元件的子元件：

| &nbsp; | 基線盒子 | 水平盒子<br >垂直盒子 |
| --- | :-: | :-: |
| [Box](https://developers.line.biz/en/reference/messaging-api/#box) | ❌ | ✅ |
| [Button](https://developers.line.biz/en/reference/messaging-api/#button) | ❌ | ✅ |
| [Image](https://developers.line.biz/en/reference/messaging-api/#f-image) | ❌ | ✅ |
| [Icon](https://developers.line.biz/en/reference/messaging-api/#icon) | ✅ | ❌ |
| [Text](https://developers.line.biz/en/reference/messaging-api/#f-text) | ✅ | ✅ |
| [Span](https://developers.line.biz/en/reference/messaging-api/#span)<br />（用作 text 元件的子元件是可以的） | ❌ | ❌ |
| [Separator](https://developers.line.biz/en/reference/messaging-api/#separator) | ❌ | ✅ |
| [Filler](https://developers.line.biz/en/reference/messaging-api/#filler)（已淘汰） | ✅ | ✅ |

✅：你可以在該盒子中使用此元件 ❌：你無法在該盒子中使用此元件

## Component size 

如果元件的 `position` 屬性設為 `relative`，則該元件的寬度與高度會由元件的 `flex` 屬性決定。

- [水平盒子中的寬度分配](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#horizontal-box)
- [垂直盒子中的高度分配](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#vertical-box)
- [盒子寬度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-width)
- [盒子的最大寬度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-max-width)
- [盒子高度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-height)
- [盒子的最大高度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-max-height)
- [影像大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#image-size)
- [Icon、text 與 span 的大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#other-component-size)
- [其他元件的大小](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#other-component)
- [自動縮小字型以符合空間](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#adjusts-fontsize-to-fit)
- [依字型大小設定縮放尺寸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#size-scaling)

### Width allocation in a horizontal box 

水平盒子中將 `flex` 屬性設為 `1` 或更大的子元件，會與同層的兄弟元件共享父盒子的寬度。`flex` 屬性的預設值為 `1`。每個子元件取得的寬度比例，是由該子元件 `flex` 屬性的值與所有 `flex` 屬性值的總和相比所決定。

假設一個水平盒子有兩個元件，一個的 `flex` 屬性設為 `2`，另一個設為 `3`。那麼可用寬度（也就是水平盒子的寬度）會以二比三的比例分割，並分配給每個元件。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/flexSample1.png)

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
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "wrap": true,
        "color": "#ff0000",
        "flex": 2
      },
      {
        "type": "text",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "wrap": true,
        "color": "#0000ff",
        "flex": 3
      }
    ]
  }
}
```

如果元件的 `flex` 屬性為 `0`，則該元件會在盒子寬度範圍內，占用顯示其所有內容所需的寬度。不過，超出盒子寬度的部分不會被顯示。

舉例來說，假設我們有一個水平盒子，內含三個子元件，其 `flex` 屬性分別設為 `0`、`2` 與 `3`。第一個元件的 `flex` 屬性設為 `0`，因此該元件會占用剛好能容納其文字「Hello」的寬度。接著剩餘的可用寬度會以二比三的比例在其餘兩個元件之間共享，如下圖所示。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/flexSample2.png)

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
        "text": "Hello",
        "color": "#00ff00",
        "flex": 0
      },
      {
        "type": "text",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "wrap": true,
        "color": "#ff0000",
        "flex": 2
      },
      {
        "type": "text",
        "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "wrap": true,
        "color": "#0000ff",
        "flex": 3
      }
    ]
  }
}
```

<!-- tip start -->

**flex 屬性與 CSS flexbox**

水平盒子中子元件的 `flex` 屬性，與 CSS flexbox 的 `flex` 屬性對應如下：

| Flex Message 子元件的 `flex` 屬性值 | 對應的 CSS flexbox 樣式 |
| :-: | --- |
| `0` | `flex: 0 0 auto;` |
| `0` 或更大 | `flex: X 0 0;`（其中 X 為子元件的 `flex` 值） |

<!-- tip end -->

### Height allocation in a vertical box 

垂直盒子中將 `flex` 屬性設為 `1` 或更大的子元件，會與同層的兄弟元件共享父盒子的高度。`flex` 屬性的預設值為 `0`。每個子元件取得的高度比例，是由其 `flex` 屬性的值與所有 `flex` 屬性值的總和相比所決定。

在以下範例中，一個水平盒子內含兩個垂直盒子。左邊的垂直盒子有一段占用五行的文字，右邊的垂直盒子則有兩段文字與三個分隔線。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/flexSample5.png)

每個元件依照以下規則進行版面配置：

1. 左邊的垂直盒子高度為五行。這使得右邊垂直盒子的高度也設定為相同。
1. 右邊垂直盒子中的子元件不需要占用整個高度，因此會產生一些自由空間。
1. 該自由空間會依兩個 text 元件 `flex` 屬性的值（分別為 `2` 與 `3`），以 2:3 的比例分割並分配給它們。

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "wrap": true,
            "text": "TEXT\nTEXT\nTEXT\nTEXT\nTEXT"
          }
        ],
        "backgroundColor": "#c0c0c0"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "text",
            "text": "flex=2",
            "flex": 2
          },
          {
            "type": "separator",
            "color": "#ff0000"
          },
          {
            "type": "text",
            "text": "flex=3",
            "flex": 3
          },
          {
            "type": "separator",
            "color": "#ff0000"
          }
        ]
      }
    ]
  }
}
```

<!-- tip start -->

**flex 屬性與 CSS flexbox**

垂直盒子中子元件的 `flex` 屬性，與 CSS flexbox 的 `flex` 對應如下：

| Flex Message 子元件的 `flex` 屬性值 | 對應的 CSS flexbox 樣式 |
| :-: | --- |
| `0` | `flex: 0 0 auto;` |
| `0` 或更大 | `flex: X 0 auto;`（其中 X 為子元件的 `flex` 值） |

<!-- tip end -->

### Box width 

你可以用 `width` 屬性指定盒子寬度，單位為像素，或以相對於父元件寬度的百分比表示。如果你在水平盒子中指定子盒子的寬度，該子盒子的 `flex` 屬性會被設為 `0`。

<!-- note start -->

**以像素為單位的 width 屬性**

bubble 的寬度取決於裝置螢幕的大小。如果你以像素指定 `width` 屬性來調整 bubble 的整體版面配置，最終可能會得到非預期的版面。我們建議你改用 `flex` 屬性，以減少受裝置螢幕大小的影響。

<!-- note end -->

### Maximum width of a box 

你可以用 `maxWidth` 屬性指定盒子的最大寬度，單位為像素，或以相對於父元件寬度的百分比表示。`maxWidth` 的優先順序高於 `width` 屬性。如果以 `width` 屬性計算出的寬度大於以最大值計算出的寬度，盒子寬度就會設為 `maxWidth` 屬性的值。

### Box height 

你可以用 `height` 屬性指定盒子高度，單位為像素，或以相對於父元件高度的百分比表示。如果你在水平盒子中指定子盒子的高度，該子盒子的 `flex` 屬性會被設為 `0`。

### Maximum height of a box 

你可以用 `maxHeight` 屬性指定盒子的最大高度，單位為像素，或以相對於父元件高度的百分比表示。`maxHeight` 的優先順序高於 `height` 屬性。如果以 `height` 屬性計算出的高度大於以最大值計算出的高度，盒子高度就會設為 `maxHeight` 屬性的值。

### Image size 

你可以用 `size` 屬性設定[影像元件（image component）](https://developers.line.biz/en/reference/messaging-api/#f-image)的寬度，單位為像素、百分比，或使用關鍵字。高度會自動調整以維持長寬比（在 `aspectRatio` 屬性中指定）。

| 單位 | 可接受的值 | 範例 |
| --- | --- | :-: |
| 百分比 | 相對於原始影像寬度的百分比，以正整數或小數後綴 `%` 表示。 | `50%` `23.5%` |
| 像素 | 以 `px` 為後綴的正整數或小數。 | `50px` `23.5px` |
| 關鍵字 | 以下任一值，依大小遞增排列：`xxs`、`xs`、`sm`、`md`、`lg`、`xl`、`xxl`、`3xl`、`4xl`、`5xl`、`full` | `md`（預設） |

### Icon, text, and span size 

你可以用 `size` 屬性指定 [icon](https://developers.line.biz/en/reference/messaging-api/#icon)、[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 與 [span](https://developers.line.biz/en/reference/messaging-api/#span) 元件的大小，單位為像素或使用關鍵字。你無法指定百分比。

| 單位 | 可接受的值 | 範例 |
| --- | --- | :-: |
| 像素 | 以 `px` 為後綴的正整數或小數。 | `50px` `23.5px` |
| 關鍵字 | 以下任一值，依大小遞增排列：`xxs`、`xs`、`sm`、`md`、`lg`、`xl`、`xxl`、`3xl`、`4xl`、`5xl` | `md`（預設） |

### Size of other components 

對於 button 之類的元件，你可以用 `flex` 以外的屬性指定元件大小。關於 JSON 結構描述的詳細資訊，請參閱 Messaging API 參考文件中的 [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)。

### Automatically shrink fonts to fit 

如果你為 [button](https://developers.line.biz/en/reference/messaging-api/#button) 與 [text](https://developers.line.biz/en/reference/messaging-api/#f-text) 元件的 `adjustMode` 屬性指定 `shrink-to-fit` 值，文字的字型大小會自動縮小以符合空間。`adjustMode` 屬性採取「盡力而為」（best-effort）的做法，在某些平台上可能會有不同的運作方式，甚至完全不起作用！

![](https://developers.line.biz/media/messaging-api/flex-message-layout/adjusts-fontsize-to-fit.png)

### Scaling to size according to the font size setting 

如果你將 Flex Message 的 [button](https://developers.line.biz/en/reference/messaging-api/#button)、[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 或 [icon](https://developers.line.biz/en/reference/messaging-api/#icon) 的 `scaling` 屬性設為 `true`，就可以依據 LINE app 的字型大小設定，自動縮放字型大小與圖示大小。這讓你可以發送兼顧無障礙考量的訊息。

| 字型大小**小（Small）**的範例 | 字型大小**特大（Extra large）**的範例 |
| --- | --- |
| ![](https://developers.line.biz/media/messaging-api/flex-message-layout/scaling-sample-small-en.jpg) | ![](https://developers.line.biz/media/messaging-api/flex-message-layout/scaling-sample-extra-large-en.jpg) |

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "hello, world",
        "size": "30px"
      },
      {
        "type": "text",
        "text": "hello, world",
        "margin": "10px",
        "size": "30px",
        "scaling": true
      }
    ]
  }
}
```

<!-- tip start -->

**同時使用自動縮小字型**

在 button 與 text 中，你可以同時將 `scaling` 屬性設為 `true`，並將 `adjustMode` 屬性設為 `shrink-to-fit`。在這種情況下，當字型大小因自動縮放而導致文字寬度超過元件寬度時，字型大小會縮小以符合元件寬度。

以下是 LINE app **特大（Extra Large）**字型大小的範例。

| | |
| --- | --- |
| ![](https://developers.line.biz/media/messaging-api/flex-message-layout/scaling-sample-small-tip.png) | <ol><li>預設</li><li>`scaling` 屬性設為 `true` 時</li><li>`scaling` 屬性設為 `true` 且 `adjustMode` 屬性設為 `shrink-to-fit` 時</li></ol> |

<!-- tip end -->

## Component position 

如果一個含有子元件的盒子有剩餘空間，你可以將每個子元件[水平](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#align-property)或[垂直](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#gravity-property)對齊。

若要定位子元件，可使用父元件的 [padding](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property) 或子元件的 [`margin` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property)。你可以在[主軸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#justify-content)上分配子元件，也可以在[交叉軸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#align-items)上分配子元件。[偏移（Offset）](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#component-offset)是你可以用來定位子元件的另一個選項。

### Horizontally align text or images 

若要將你的 [text](https://developers.line.biz/en/reference/messaging-api/#f-text) 或 [image](https://developers.line.biz/en/reference/messaging-api/#f-image) 元件水平對齊，請使用 `align` 屬性。父元件的方向不會影響此屬性。可用的對齊選項有：

- 靠左對齊：`start`
- 靠右對齊：`end`
- 置中對齊：`center`（預設）

![](https://developers.line.biz/media/messaging-api/flex-message-layout/alignSample.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "align=start",
        "align": "start"
      },
      {
        "type": "separator",
        "color": "#ff0000"
      },
      {
        "type": "text",
        "text": "align=center",
        "align": "center"
      },
      {
        "type": "separator",
        "color": "#ff0000"
      },
      {
        "type": "text",
        "text": "align=end",
        "align": "end"
      }
    ]
  }
}
```

### Vertically align text, images, or button 

若要將你的 [text](https://developers.line.biz/en/reference/messaging-api/#f-text)、[image](https://developers.line.biz/en/reference/messaging-api/#f-image) 或 [button](https://developers.line.biz/en/reference/messaging-api/#button) 元件垂直對齊，請使用 `gravity` 屬性。父元件的方向不會影響此屬性。可用的對齊選項有：

- 靠頂端對齊：`top`（預設）
- 靠底端對齊：`bottom`
- 置中對齊：`center`

<!-- note start -->

**備註**

如果元件是[基線盒子](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#baseline-box)的子元件，則 `gravity` 屬性會被忽略。

<!-- note end -->

![](https://developers.line.biz/media/messaging-api/flex-message-layout/gravitySample.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "wrap": true,
            "text": "TEXT\nTEXT\nTEXT\nTEXT\nTEXT"
          }
        ],
        "backgroundColor": "#c0c0c0"
      },
      {
        "type": "text",
        "text": "top",
        "gravity": "top"
      },
      {
        "type": "separator",
        "color": "#ff0000"
      },
      {
        "type": "text",
        "text": "center",
        "gravity": "center"
      },
      {
        "type": "separator",
        "color": "#ff0000"
      },
      {
        "type": "text",
        "text": "bottom",
        "gravity": "bottom"
      },
      {
        "type": "separator",
        "color": "#ff0000"
      }
    ]
  }
}
```

### Position child component with box padding 

你可以用 box 元件的 padding 來定位該盒子中的子元件。Padding 會在父元件的邊框與子元件之間分配空間。可用的 padding 屬性有 `paddingAll`、`paddingTop`、`paddingBottom`、`paddingStart` 與 `paddingEnd`。Padding 可以用像素、百分比（相對於父盒子寬度）或關鍵字指定。

| 單位 | 可接受的值 | 範例 |
| --- | --- | :-: |
| 百分比 | 相對於父盒子寬度的百分比，以正整數或小數後綴 `%` 表示。 | `50%` `23.5%` |
| 像素 | 以 `px` 為後綴的正整數或小數。 | `50px` `23.5px` |
| 關鍵字 | 以下任一值，依大小遞增排列：`none`（無 padding）、`xs`、`sm`、`md`、`lg`、`xl`、`xxl` | `md`（預設） |

`paddingTop`、`paddingBottom`、`paddingStart` 與 `paddingEnd` 屬性的優先順序高於 `paddingAll` 屬性。如果指定了 `paddingTop`、`paddingBottom`、`paddingStart` 或 `paddingEnd` 屬性，`paddingAll` 屬性就會被忽略。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/paddingSample.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "hello, world"
          }
        ],
        "backgroundColor": "#ffffff"
      }
    ],
    "backgroundColor": "#ffd2d2",
    "paddingTop": "20px",
    "paddingAll": "80px",
    "paddingStart": "40px"
  }
}
```

以相同 padding 顯示較長文字的結果如下所示。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/paddingSample2.png)

### Child component arrangement with free space 

你可以依軸線，將子元件以 [box](https://developers.line.biz/en/reference/messaging-api/#box) 中的剩餘空間進行排列。了解如何依[主軸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#justify-content)與[交叉軸](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#align-items)分配子元件。

<!-- tip start -->

**主軸與交叉軸的方向由父 box 元件決定**

`justifyContent` 與 `alignItems` 屬性分別設定子元件沿主軸與交叉軸的擺放方式。主軸與交叉軸的方向由父 box 元件決定。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/horizontal_vertical_axis_en.png)

無論父 box 元件的方向為何，文字方向（`LTR` 或 `RTL`）一律以水平方向套用。

<!-- tip end -->

#### Distribute child components on main axis 

若要沿主軸分配盒子中的子元件，請使用 `justifyContent` 屬性。水平盒子的主軸方向為水平，垂直盒子則為垂直。為了讓此屬性生效，所有子元件的 `flex` 屬性都必須為 `0`。因為只要任何一個子元件的 `flex` 屬性為 `1` 或更大，子元件就會擴展以填滿父盒子。這表示沒有空間可分配子元件。請注意，水平盒子中的子元件 `flex` 屬性預設值為 `1`。

來看看在 LTR 文字方向的水平盒子中，子元件如何依 `justifyContent` 屬性的值進行分配。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/justify-content-01.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/justify-content-02.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/justify-content-03.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/justify-content-04.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/justify-content-05.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/justify-content-06.svg)

| 屬性值 | 子元件分配方式 |
| --- | --- |
| `flex-start` | 水平盒子：聚集在父元件中文字開始的位置<br />垂直盒子：聚集在父元件的頂端 |
| `center` | 聚集在父元件的中央 |
| `flex-end` | 水平盒子：聚集在父元件中文字結束的位置<br />垂直盒子：聚集在父元件的底端 |
| `space-between` | 在父元件中平均分配，第一個與最後一個子元件分別位於父元件的兩端。子元件之間的間距相等。 |
| `space-around` | 在父元件中平均分配。父元件中的剩餘空間除以「2 × 元件數量」。每個子元件的左右各分得一份空間。 |
| `space-evenly` | 在父盒子中平均分配。父元件中的剩餘空間平均分配於每個子元件的兩側。 |

設定為 `flex-start` 的 Flex Message JSON 定義如下。

```json
{
  "type": "bubble",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "width": "40px",
        "height": "30px",
        "backgroundColor": "#00aaff",
        "flex": 0
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "width": "20px",
        "height": "30px",
        "backgroundColor": "#00aaff",
        "flex": 0
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "height": "30px",
        "width": "50px",
        "backgroundColor": "#00aaff",
        "flex": 0
      }
    ],
    "justifyContent": "flex-start",
    "spacing": "5px"
  }
}
```

#### Arranging child components along the cross axis with the `alignItems` property 

若要沿交叉軸分配盒子中的子元件，請使用 `alignItems` 屬性。水平盒子的交叉軸方向為垂直，垂直盒子則為水平。

來看看在 LTR 文字方向的水平盒子中，子元件如何依 `alignItems` 屬性的值進行分配。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/alignItems-01.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/alignItems-02.svg)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/alignItems-03.svg)

| 屬性值 | 子元件分配方式 |
| --- | --- |
| `flex-start` | 水平盒子：對齊父元件的頂端<br />垂直盒子：聚集在父元件中文字開始的位置 |
| `center` | 位於父元件的中央 |
| `flex-end` | 水平盒子：聚集在父元件的底端。<br />垂直盒子：聚集在父元件中文字結束的位置 |

設定為 `flex-start` 的 Flex Message JSON 定義如下。

```json
{
  "type": "bubble",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "height": "100px",
        "backgroundColor": "#00aaff",
        "flex": 0,
        "width": "85px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "height": "30px",
        "backgroundColor": "#00aaff",
        "flex": 0,
        "width": "85px"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "height": "60px",
        "backgroundColor": "#00aaff",
        "flex": 0,
        "width": "85px"
      }
    ],
    "spacing": "5px",
    "alignItems": "flex-start",
    "height": "200px"
  }
}
```

### `spacing` property for boxes 

你可以用父 box 元件的 `spacing` 屬性指定兩個元件之間的最小間距，單位為像素或使用關鍵字。你無法指定百分比。

| 單位 | 可接受的值 | 範例 |
| --- | --- | :-: |
| 像素 | 以 `px` 為後綴的正整數或小數。 | `50px` `23.5px` |
| 關鍵字 | 以下任一值，依大小遞增排列：`none`（無間距）、`xs`、`sm`、`md`、`lg`、`xl`、`xxl` | `md` |

這個 Flex Message 範例有一個水平盒子，內含三個垂直盒子作為子元件，並以相等的間距（`md`）排列。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/spacingSample.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEXT1"
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEXT2"
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEXT3"
          }
        ],
        "backgroundColor": "#80ffff"
      }
    ]
  }
}
```

若要針對特定元件覆寫此設定，請設定該元件的 `margin` 屬性。

### `margin` property of components 

你可以用子元件的 `margin` 屬性指定該子元件之前的最小間距，單位為像素或使用關鍵字。你無法指定百分比。

| 單位 | 可接受的值 | 範例 |
| --- | --- | :-: |
| 像素 | 以 `px` 為後綴的正整數或小數。 | `50px` `23.5px` |
| 關鍵字 | 以下任一值，依大小遞增排列：`none`（無 margin）、`xs`、`sm`、`md`、`lg`、`xl`、`xxl` | `md` |

`margin` 屬性的優先順序高於父盒子的 [`spacing` 屬性](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#spacing-property)。此外，如果為盒子中的第一個子元件指定 `margin` 屬性，該空間會配置在此元件之前。

這個 Flex Message 範例有一個水平盒子，內含三個垂直盒子作為子元件。父水平盒子的 `spacing` 屬性設為 `md`。第三個垂直盒子的 `margin` 屬性設為 `xxl`。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/marginSample.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "horizontal",
    "spacing": "md",
    "contents": [
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEXT1"
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEXT2"
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "TEXT3"
          }
        ],
        "backgroundColor": "#80ffff",
        "margin": "xxl"
      }
    ]
  }
}
```

### Offset 

定位元件的另一個選項是使用偏移（offset）。偏移屬性的運作方式會因父元件 `position` 屬性的值而不同，該值可以是 `relative` 或 `absolute`。但[區塊（block）](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)的第一個子元件不能是 `absolute`。

你可以使用的偏移屬性有 `offsetTop`、`offsetBottom`、`offsetStart` 與 `offsetEnd`。你可以用像素或關鍵字（`none`、`xs`、`sm`、`md`、`lg`、`xl` 或 `xxl`）指定屬性值。你也可以為 `offsetStart` 與 `offsetEnd` 指定相對於盒子寬度的百分比，並為 `offsetTop` 與 `offsetBottom` 指定相對於盒子高度的百分比。

了解偏移如何改變下方標示為「TARGET」的盒子位置。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample1.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "REFERENCE BOX\n1\n2\n3",
            "align": "center",
            "wrap": true
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "TARGET"
          }
        ],
        "backgroundColor": "#ff8080"
      }
    ]
  }
}
```

#### Offset when position is relative 

若要將你的元件從其原始位置移動，請將 `position` 屬性設為 `relative`。詳細資訊請參閱 CSS Positioned Layout Module Level 3 的[相對定位（Relative positioning）](https://www.w3.org/TR/css-position-3/#relpos-insets)。

| 屬性 | 說明 |
| --- | --- |
| `offsetTop` | 將元件從其原始位置的頂端邊緣向下移動。 |
| `offsetBottom` | 將元件從其原始位置的底端邊緣向上移動。 |
| `offsetStart` | 將元件從文字開始的位置移開。如果 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 的文字方向為 LTR，則向右移動；如果為 RTL，則向左移動。 |
| `offsetEnd` | 從文字結束的位置移開。如果 [bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 的文字方向為 LTR，則向左移動；如果為 RTL，則向右移動。 |

第一張圖顯示標示為「TARGET」的元件在其原始位置的樣子。第二張圖顯示透過 `position` 與偏移屬性移動後的元件。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample1.png)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample2.png)

若要像範例那樣移動你的元件，請依下方指定方式設定屬性。

| 屬性       | 值      |
| -------------- | ---------- |
| `position`     | `relative` |
| `offsetTop`    | `10px`     |
| `offsetBottom` | -          |
| `offsetStart`  | `40px`     |
| `offsetEnd`    | -          |

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "REFERENCE BOX\n1\n2\n3",
            "align": "center",
            "wrap": true
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "TARGET"
          }
        ],
        "backgroundColor": "#ff8080",
        "offsetTop": "10px",
        "offsetStart": "40px",
        "position": "relative"
      }
    ]
  }
}
```

#### Offset when position is absolute 

若要將你的元件從父元件的邊緣移動，請將 `position` 屬性設為 `absolute`。詳細資訊請參閱 CSS Positioned Layout Module Level 3 的[絕對定位（Absolute positioning）](https://www.w3.org/TR/css-position-3/#abs-pos)。

<table>
  <thead>
    <tr>
      <th>屬性</th>
      <th colspan="2">說明</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>offsetTop</code></td>
      <td colspan="2">指定從父元件上端到該元件上端的相對位置。</td>
    </tr>
    <tr>
      <td><code>offsetBottom</code></td>
      <td colspan="2">指定從父元件下端到該元件下端的相對位置。</td>
    </tr>
    <tr>
      <td rowspan="2"><code>offsetStart</code></td>
      <td>如果 <a href="https://developers.line.biz/en/reference/messaging-api/#bubble">bubble</a> 中的文字方向為 LTR</td>
      <td>指定從父元件左端到該元件左端的相對位置。</td>
    </tr>
    <tr>
      <td>如果 <a href="https://developers.line.biz/en/reference/messaging-api/#bubble">bubble</a> 中的文字方向為 RTL</td>
      <td>指定從父元件右端到該元件右端的相對位置。</td>
    </tr>
    <tr>
      <td rowspan="2"><code>offsetEnd</code></td>
      <td>如果 <a href="https://developers.line.biz/en/reference/messaging-api/#bubble">bubble</a> 中的文字方向為 LTR</td>
      <td>指定從父元件右端到該元件右端的相對位置。</td>
    </tr>
    <tr>
      <td>如果 <a href="https://developers.line.biz/en/reference/messaging-api/#bubble">bubble</a> 中的文字方向為 RTL</td>
      <td>指定從父元件左端到該元件左端的相對位置。</td>
    </tr>
  </tbody>
</table>

<!-- note start -->

**備註**

如果你未指定偏移屬性，元件的位置可能會因裝置而異。我們建議你同時指定垂直方向（`offsetTop` 或 `offsetBottom`）與水平方向（`offsetStart` 或 `offsetEnd`）的偏移。

<!-- note end -->

第一張圖顯示標示為「TARGET」的元件在其原始位置的樣子。第二張圖顯示透過 `position` 與偏移屬性移動後的元件。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample1.png)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample3.png)

若要像範例那樣移動你的元件，請依下方指定方式設定屬性。

| 屬性       | 值      |
| -------------- | ---------- |
| `position`     | `absolute` |
| `offsetTop`    | `10px`     |
| `offsetBottom` | `20px`     |
| `offsetStart`  | `40px`     |
| `offsetEnd`    | `80px`     |

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "direction": "ltr",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "REFERENCE BOX\n1\n2\n3",
            "align": "center",
            "wrap": true
          }
        ],
        "backgroundColor": "#80ffff"
      },
      {
        "type": "box",
        "layout": "horizontal",
        "contents": [
          {
            "type": "text",
            "text": "TARGET"
          }
        ],
        "backgroundColor": "#ff8080",
        "position": "absolute",
        "offsetStart": "40px",
        "offsetEnd": "80px",
        "offsetTop": "10px",
        "offsetBottom": "20px"
      }
    ]
  }
}
```

##### Size of child and parent components with absolute position 

`position` 屬性設為 `absolute` 的子 box 元件，不會改變父元件的大小。同樣地，該元件也不會被父元件調整大小。如果某元件比父元件大，超出父元件的部分不會被顯示。

讓我們比較絕對定位與相對定位的效果。第一張圖中的「REFERENCE BOX」元件是一個水平盒子，其 position 設為 relative。第二張圖則顯示同一個元件在 position 設為 absolute 時的樣子。

![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample1.png)
![](https://developers.line.biz/media/messaging-api/flex-message-layout/offsetSample4.png)

如同你在第二張圖的範例中所見，「REFERENCE BOX」的大小不會影響父元件（垂直盒子）的大小，也不會被父元件影響。因此，比父元件大的部分（第「2」與「3」行）不會被顯示。此外，原本因父元件效果而變大的左右兩側自由空間（free space），會恢復為其原始大小（文字「REFERENCE BOX」的寬度）。

## Linear gradient backgrounds 

你可以用線性漸層（linear gradient）設定 [box](https://developers.line.biz/en/reference/messaging-api/#box) 元件的背景。請為 `background.type` 屬性指定 `linearGradient`。了解如何設定漸層的[角度](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#linear-gradient-bg-angle)與[色彩停駐點（color stops）](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#linear-gradient-bg-center-color)。

<!-- note start -->

**父元件的文字方向不會影響漸層的方向**

父元件的文字方向（`LTR` 或 `RTL`）不會影響漸層的方向。

<!-- note end -->

### Angle of linear gradient 

你可以將線性漸層的角度指定為 0 到小於 360 度之間的整數或小數。若要將角度設為 90 度，請指定為 `90deg`；23.5 度則指定為 `23.5deg`。漸層的方向會隨角度而改變：

- 0 度：由下而上
- 45 度：由左下到右上
- 90 度：由左到右
- 180 度：由上而下

角度增加時，方向會以順時針方向旋轉。

**0 度的線性漸層（由下而上）**

![](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-deg-0.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [],
    "background": {
      "type": "linearGradient",
      "angle": "0deg",
      "startColor": "#ff0000",
      "endColor": "#0000ff"
    },
    "height": "200px"
  }
}
```

**45 度的線性漸層（由左下到右上）**

![](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-deg-45.png)

**90 度的線性漸層（由左到右）**

![](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-deg-90.png)

**180 度的線性漸層（由上而下）**

![](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-deg-180.png)

詳細資訊請參閱 Messaging API 參考文件中的 [Box](https://developers.line.biz/en/reference/messaging-api/#box)。

### Gradient color stops 

若要為漸層新增色彩停駐點，也就是讓漸層擁有三種顏色，請指定 `centerColor` 屬性。你可以用 `centerPosition` 屬性指定色彩停駐點的位置。

**色彩停駐點位於 10% 處**

![三色漸層，中間色彩停駐點位於距起點 10% 處](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-percent-10.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [],
    "background": {
      "type": "linearGradient",
      "angle": "0deg",
      "startColor": "#ff0000",
      "centerColor": "#0000ff",
      "endColor": "#00ff00",
      "centerPosition": "10%"
    },
    "height": "200px"
  }
}
```

**色彩停駐點位於 50% 處**

![三色漸層，中間色彩停駐點位於距起點 50% 處](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-percent-50.png)

**色彩停駐點位於 90% 處**

![三色漸層，中間色彩停駐點位於距起點 90% 處](https://developers.line.biz/media/messaging-api/flex-message-layout/linear-gradient-bg-percent-90.png)

## Rendering order 

元件會依 JSON 中指定的順序進行算繪（render）。JSON 定義開頭的元件最先算繪。接著下一個元件會算繪在前一個元件之上。因此最後一個元件會算繪在 bubble 的最上層。

若要變更算繪順序，請更改 JSON 定義中元件的順序。

## Learn more 

- [發送 Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)
- [Flex Message 元素](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)
- [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)（Messaging API 參考文件）
