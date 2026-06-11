# 動作（Actions）

當使用者在訊息中點選某個控制項時，你可以設定要觸發的不同類型動作。可用的動作會依訊息類型而有所不同。詳情請參閱 Messaging API 參考文件中的 [Message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)。

可用的動作有：

- [Postback action](https://developers.line.biz/en/docs/messaging-api/actions/#postback-action)
- [Message action](https://developers.line.biz/en/docs/messaging-api/actions/#message-action)
- [URI action](https://developers.line.biz/en/docs/messaging-api/actions/#uri-action)
- [Datetime picker action](https://developers.line.biz/en/docs/messaging-api/actions/#datetime-picker-action)
- [Camera action](https://developers.line.biz/en/docs/messaging-api/actions/#camera-action)
- [Camera roll action](https://developers.line.biz/en/docs/messaging-api/actions/#camera-roll-action)
- [Location action](https://developers.line.biz/en/docs/messaging-api/actions/#location-action)
- [Rich menu switch action](https://developers.line.biz/en/docs/messaging-api/actions/#richmenu-switch-action)
- [Clipboard action](https://developers.line.biz/en/docs/messaging-api/actions/#clipboard-action)

## Postback action 

回傳動作（postback action）會將你在動作中指定的文字，連同 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 一併傳送到你的伺服器。你可以設定讓該文字以使用者訊息的形式顯示。

你也可以指定要如何顯示，例如根據使用者動作來顯示 rich menu。可指定的顯示方式如下：

- 關閉 rich menu
- 開啟 rich menu
- 開啟鍵盤
- 開啟語音訊息輸入模式

根據使用者動作指定顯示方式的功能，在 iOS 或 Android 的 LINE 版本 `12.6.0` 以後可使用。詳情請參閱 Messaging API 參考文件中的 [Postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)。

## Message action 

訊息動作（message action）會回傳一段文字作為使用者的訊息。詳情請參閱 Messaging API 參考文件中的 [Message action](https://developers.line.biz/en/reference/messaging-api/#message-action)。

## URI action 

URI 動作（URI action）會在 LINE 的應用程式內建瀏覽器中開啟一個 URL。你也可以在 URI 動作中使用 [LINE URL scheme](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/)，以指定號碼啟動通話應用程式，或開啟分享任一 LINE 官方帳號的畫面。

![URI action](https://developers.line.biz/media/messaging-api/actions/quick-reply-uri-action-en.png)

以下是為上方範例中的快速回覆按鈕設定了 URI 動作的請求主體（request body）。詳情請參閱 Messaging API 參考文件中的 [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)。

```json
{
  "messages": [
    {
      "type": "text",
      "text": "Have you decided on your order?",
      "quickReply": {
        "items": [
          {
            "type": "action",
            "action": {
              "type": "uri",
              "label": "Menu",
              "uri": "https://example.com/menu"
            }
          },
          {
            "type": "action",
            "action": {
              "type": "uri",
              "label": "Phone order",
              "uri": "tel:09001234567"
            }
          },
          {
            "type": "action",
            "action": {
              "type": "uri",
              "label": "Recommend to friend",
              "uri": "https://line.me/R/nv/recommendOA/%40linedevelopers"
            }
          }
        ]
      }
    }
  ]
}
```

## Datetime picker action 

日期時間選擇器動作（datetime picker action）會提示使用者從選擇器中選擇日期、時間，或日期與時間。當使用者選擇日期與時間後，你會透過 webhook 在 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 中取得該日期與時間資訊。詳情請參閱 Messaging API 參考文件中的 [Datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)。

![Datetime picker action](https://developers.line.biz/media/messaging-api/actions/datetime-picker.png)

## Camera action 

相機動作（camera action）會在 LINE 中開啟相機畫面。你只能在快速回覆按鈕上設定此動作。詳情請參閱 Messaging API 參考文件中的 [Camera action](https://developers.line.biz/en/reference/messaging-api/#camera-action)。

## Camera roll action 

相機膠卷動作（camera roll action）會在 LINE 中開啟相機膠卷畫面。你只能在快速回覆按鈕上設定此動作。詳情請參閱 Messaging API 參考文件中的 [Camera roll action](https://developers.line.biz/en/reference/messaging-api/#camera-roll-action)。

## Location action 

位置動作（location action）會在 LINE 中開啟位置畫面。你只能在快速回覆按鈕上設定此動作。詳情請參閱 Messaging API 參考文件中的 [Location action](https://developers.line.biz/en/reference/messaging-api/#location-action)。

## Rich menu switch action 

rich menu 切換動作（rich menu switch action）可讓 rich menu 互相切換。你只能在 rich menu 上設定此動作。詳情請參閱 Messaging API 參考文件中的 [Rich menu switch action](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)。

## Clipboard action 

剪貼簿動作（clipboard action）會將文字複製到剪貼簿。當使用者點選與此動作關聯的控制項時，`clipboardText` 屬性中指定的文字就會被複製到裝置的剪貼簿。

![](https://developers.line.biz/media/news/2024/clipbord-action-example-en.png)

以下是為上方範例中的訊息設定了剪貼簿動作的請求主體（request body）。詳情請參閱 Messaging API 參考文件中的 [Clipboard action](https://developers.line.biz/en/reference/messaging-api/#clipboard-action)。

```json
{
  "messages":[
    {
      "type": "template",
      "altText": "This is your coupon code.",
      "template": {
        "type": "buttons",
        "thumbnailImageUrl": "{your coupon image}",
        "imageAspectRatio": "rectangle",
        "imageSize": "cover",
        "imageBackgroundColor": "#FFFFFF",
        "title": "Your exclusive coupon!",
        "text": "Period: Feb 2024.\nCopy and use the code from the button.",
        "actions": [
          {
            "type": "clipboard",
            "label": "Copy",
            "clipboardText": "3B48740B"
          }
        ]
      }
    }
  ]
}
```
