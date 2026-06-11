# 傳送 Flex Message（Send Flex Messages）

Flex Message 是一種與一般 LINE 訊息相比，能提供更豐富且更具互動性版面配置的訊息。一般 LINE 訊息只能傳遞單一來源類型，例如文字、圖片與影片。你可以依據 [CSS Flexible Box（CSS Flexbox）](https://www.w3.org/TR/css-flexbox-1/) 規格，自由自訂版面配置。

Flex Message 的構成元素為容器（container）、區塊（block）與元件（component）。每則 Flex Message 都有一個頂層元素，也就是包含訊息泡泡（message bubble）的容器。容器可以包含多個訊息泡泡。泡泡內有區塊，而區塊內有元件。

Flex Message 讓你能設定文字的方向，可由左至右或由右至左。

<!-- note start -->

**Flex Message 的限制**

同一則 Flex Message 在接收者裝置的環境不同時，可能會以不同方式呈現。呈現結果可能會受到裝置的 OS、LINE 版本、裝置解析度、語言設定與字型所影響。

<!-- note end -->

![Flex Message examples](https://developers.line.biz/media/messaging-api/using-flex-messages/bubbleSamples-Update1.png)

與其他訊息類型一樣，你以 JSON 來定義 Flex Message。如需更多關於 Flex Message 的資訊，請參閱：

- [Flex Message elements](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)
- [Flex Message layout](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)
- [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)（Messaging API 參考文件）

## Operating environment 

所有 LINE 版本都支援 Flex Message。但以下列出的功能並非所有 LINE 版本都支援：

| 功能 | LINE for iOS<br>LINE for Android | LINE for PC<br />（macOS、Windows） |
| --- | :-: | :-: |
| <ul><li>[box](https://developers.line.biz/en/reference/messaging-api/#box) 的 `maxWidth` 屬性</li><li>[box](https://developers.line.biz/en/reference/messaging-api/#box) 的 `maxHeight` 屬性</li><li>[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 的 `lineSpacing` 屬性</li><li>[Video](https://developers.line.biz/en/reference/messaging-api/#f-video) \*1</li></ul> | 11.22.0 或以上版本 | 7.7.0 或以上版本 |
| <ul><li>[bubble](https://developers.line.biz/en/reference/messaging-api/#bubble) 的 `size` 屬性中的 `deca` 與 `hecto` 值 \*2</li><li>[button](https://developers.line.biz/en/reference/messaging-api/#button)、[text](https://developers.line.biz/en/reference/messaging-api/#f-text) 與 [icon](https://developers.line.biz/en/reference/messaging-api/#icon) 的 `scaling` 屬性</li></ul> | 13.6.0 或以上版本 | 7.17.0 或以上版本 |

\*1 為了讓 Flex Message 中的影片元件在不支援影片元件的版本上也能正確呈現，請指定 `altContent` 屬性。系統會改為顯示你在此屬性中指定的圖片。

\*2 如果 LINE 的版本低於支援 `deca` 與 `hecto` 的版本，泡泡的尺寸會以 `kilo` 顯示。

## Flex Message Simulator 

透過 [Flex Message Simulator](https://developers.line.biz/flex-simulator/)，你不必實際傳送訊息，就能檢查 Flex Message 的版面配置並查看其呈現結果。

![Flex Message Simulator](https://developers.line.biz/media/messaging-api/using-flex-messages/flex-message-simulator-en.png)

如需更多關於 Flex Message Simulator 的資訊，請參閱 [Tutorial - Create a digital business card with Flex Message Simulator](https://developers.line.biz/en/docs/messaging-api/using-flex-message-simulator/)。

## Send "Hello, World!" 

要開始使用 Flex Message，請試著以 Flex Message 傳送「Hello, World!」。首先，以 JSON [定義 Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/#preparing-json-data)，接著[呼叫 Messaging API](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/#sending-messages-with-the-messaging-api) 來傳送訊息。

![Hello, World!](https://developers.line.biz/media/messaging-api/using-flex-messages/helloWorld.png)

### Define a Flex Message in JSON 

在呼叫 Messaging API 傳送 Flex Message 之前，請先以 JSON 定義 Flex Message。以下說明如何為「Hello, World!」訊息以 JSON 定義 Flex Message。這則 Flex Message 只需要單一訊息泡泡，因此我們使用 [Bubble container](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#bubble) 類型。

```json
{
  "type": "bubble", // 1
  "body": {
    // 2
    "type": "box", // 3
    "layout": "horizontal", // 4
    "contents": [
      // 5
      {
        "type": "text", // 6
        "text": "Hello,"
      },
      {
        "type": "text", // 6
        "text": "World!"
      }
    ]
  }
}
```

請參閱程式碼註解標號 1 至 6 的說明：

| | |
| --- | --- |
| 1 | 為單一訊息泡泡建立一個容器。因此將容器類型設定為 `"bubble"`。 |
| 2 | 指定一個 body 以_容納_泡泡的內容。我們只需要一個區塊類型來顯示訊息，也就是 [body block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)。 |
| 3 | 將 body block 設定為 [box component](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#box)。 |
| 4 | 將 body 的方向設定為水平。如此會將 box 內的子元件水平排列。 |
| 5 | 指定要放入 box 的元件。 |
| 6 | 插入兩個 text 元件：「Hello,」與「World!」。 |

### Call the Messaging API to send a Flex Message 

你可以透過任何一種[訊息傳送類型](https://developers.line.biz/en/docs/messaging-api/sending-messages/)來傳送 Flex Message。在訊息請求的 request body 中，將 `messages.contents` 屬性設定為 [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message) 物件定義。

以下是以 Flex Message 形式傳送 push message 的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
  "to": "U4af4980629...",
  "messages": [
    {
      "type": "flex",
      "altText": "This is a Flex Message",
      "contents": {
        "type": "bubble",
        "body": {
          "type": "box",
          "layout": "horizontal",
          "contents": [
            {
              "type": "text",
              "text": "Hello,"
            },
            {
              "type": "text",
              "text": "World!"
            }
          ]
        }
      }
    }
  ]
}'
```

## Related pages 

- [Flex Message elements](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)
- [Flex Message layout](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)
- [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)（Messaging API 參考文件）
- [Flex Message Simulator](https://developers.line.biz/flex-simulator/)
