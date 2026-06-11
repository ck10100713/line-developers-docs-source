# 搭配 LINE 使用 beacon（Use beacons with LINE）

透過 LINE Beacon，每當 LINE 使用者進入 beacon 區域時，你的 bot 就會收到 [beacon webhook 事件](https://developers.line.biz/en/reference/messaging-api/#beacon-event)。你可以依據商業需求，自訂你的 bot 應用程式，在合適的情境下透過 LINE Beacon 與使用者互動。

<!-- note start -->

**Note**

LINE Beacon 可在日本、台灣與泰國使用。

<!-- note end -->

<!-- tip start -->

**Use the latest LINE for LINE Beacon**

我們建議你使用最新版本的 LINE 來使用 LINE Beacon。

<!-- tip end -->

## Prepare beacon devices 

要使用 LINE Beacon，你需要一台 Bluetooth® Low Energy beacon 裝置，以便與你的 LINE 官方帳號（LINE Official Account）連結。你可以使用下列其中一種裝置：

- 支援 [LINE Beacon](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/) 的 beacon 裝置。這些裝置僅在其所屬國家提供支援。
  - 日本支援的裝置請見[這裡](https://beacon.theshop.jp/items/6617930)。
  - 泰國支援的裝置請見[這裡](https://linedevth.line.me/th/tech-partner?filterTech=Beacon)。
- 使用 [LINE Simple Beacon](https://github.com/line/line-simple-beacon) 規格的 Bluetooth® Low Energy 裝置。

## Link beacon to LINE Official Account 

要將你的 LINE 官方帳號與 beacon 連結，請從 [LINE Official Account Manager](https://manager.line.biz/beacon/register) 開啟 beacon 註冊頁面。在註冊頁面中，將支援 LINE Beacon 的裝置與你的 LINE 官方帳號連結。你也可以為該裝置發行一組 **LINE Simple Beacon hardware ID**。

<!-- note start -->

**Note**

你可以將多個 beacon 連結到同一個 LINE 官方帳號。但每個 beacon 只能連結一個 LINE 官方帳號。

<!-- note end -->

## Receive a webhook event 

當符合下列條件的使用者進入你的 beacon 區域時，你的 bot 伺服器就會收到 [beacon webhook 事件](https://developers.line.biz/en/reference/messaging-api/#beacon-event)：

- 在自己的 LINE 上已啟用 Bluetooth 與 LINE Beacon 設定的使用者
- 事先已將與 bot 應用程式連結的 LINE 官方帳號加為好友的使用者

要嘗試觸發 beacon webhook 事件：

1. 確認你的智慧型手機已啟用 Bluetooth。
2. 在 LINE 的 **設定** > **隱私設定** 中啟用 **使用 LINE Beacon**。
3. 確認 beacon 裝置已開機。將你的智慧型手機帶到 beacon 的範圍內。
4. 查看你的 bot 伺服器是否收到 beacon event object。

以下是 [beacon event object](https://developers.line.biz/en/reference/messaging-api/#beacon-event) 的範例：

```json
{
  "destination": "xxxxxxxxxx",
  "events": [
    {
      "replyToken": "nHuyWiB7yP5Zw52FIkcQobQuGDXCTA",
      "type": "beacon",
      "mode": "active",
      "timestamp": 1462629479859,
      "source": {
        "type": "user",
        "userId": "U4af4980629..."
      },
      "webhookEventId": "01FZ74A0TDDPYRVKNK77XKC3ZR",
      "deliveryContext": {
        "isRedelivery": false
      },
      "beacon": {
        "hwid": "d41d8cd98f",
        "type": "enter"
      }
    }
  ]
}
```

## Beacon banner 

beacon banner 是當你的 beacon 偵測到 LINE 使用者時，會出現在使用者聊天列表畫面上方的橫幅。

只要點一下橫幅，就可以讓尚未將你 beacon 所連結的 LINE 官方帳號加為好友的使用者，將該帳號加為好友。

當使用者點擊 beacon banner 時，就會開啟 LINE 官方帳號所指定的網頁。此外，你也可以讓使用者在點擊橫幅的當下，從你的 LINE 官方帳號收到訊息。

<!-- note start -->

**Note**

beacon banner 僅供企業使用者使用。要使用 beacon banner，請聯絡你的 LINE 業務代表，或透過 [LY for Business](https://www.lycbiz.jp/en/) 網站提出洽詢。

<!-- note end -->

![](https://developers.line.biz/media/messaging-api/using-beacons/beacon-banner_en.png)
