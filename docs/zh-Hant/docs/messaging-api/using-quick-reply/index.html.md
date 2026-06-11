# 使用快速回覆（Use quick replies）

快速回覆（quick reply）是一項功能，它會在訊息旁顯示按鈕，供使用者用來回覆。使用者只要點選聊天畫面下方所顯示的回覆按鈕，就能回覆 LINE 官方帳號。快速回覆可用於 LINE 官方帳號所加入的一對一聊天、群組聊天，以及多人聊天。您可以為任何類型的訊息設定最多 13 個快速回覆按鈕。

<!-- note start -->

**Note**

快速回覆於 LINE for iOS 與 LINE for Android 上受到支援。

<!-- note end -->

![Quick reply sample](https://developers.line.biz/media/messaging-api/using-quick-reply/quickReplySample.png)

## Quick reply components 

快速回覆按鈕的組成元件為 [action](https://developers.line.biz/en/docs/messaging-api/using-quick-reply/#action)、[icon](https://developers.line.biz/en/docs/messaging-api/using-quick-reply/#icon) 與 [label](https://developers.line.biz/en/docs/messaging-api/using-quick-reply/#label)。詳情請參閱 Messaging API 參考文件中的 [Quick reply](https://developers.line.biz/en/reference/messaging-api/#quick-reply)。

### Action 

動作（action）會在快速回覆按鈕被點選時觸發。詳情請參閱 [Actions](https://developers.line.biz/en/docs/messaging-api/actions/)。

以下動作僅可用於快速回覆按鈕：

- [Camera action](https://developers.line.biz/en/reference/messaging-api/#camera-action)
- [Camera roll action](https://developers.line.biz/en/reference/messaging-api/#camera-roll-action)
- [Location action](https://developers.line.biz/en/reference/messaging-api/#location-action)

以下動作與其他訊息類型共通，您也可以用於快速回覆按鈕：

- [Postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)
- [Message action](https://developers.line.biz/en/reference/messaging-api/#message-action)
- [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)
- [Datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)
- [Clipboard action](https://developers.line.biz/en/reference/messaging-api/#clipboard-action)

<!-- tip start -->

**Rich menu switch action is not available**

有一項動作無法用於快速回覆按鈕，就是 [rich menu switch action](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)。

<!-- tip end -->

### Icon 

快速回覆按鈕會以圖示（icon）標示。

如果您未設定圖示影像，則會以下列方式顯示：

- Camera、camera roll、location 動作：顯示預設圖示。
- 上述以外的動作：將省略圖示顯示。

### Label 

標籤（label）是顯示在快速回覆按鈕上的文字。

## Set quick reply buttons 

假設您正在開發一個餐廳搜尋機器人。這個機器人會依使用者對食物類別的偏好，或依使用者的位置來推薦餐廳。讓我們撰寫一則訊息，請使用者回覆：

1. 建立一個文字訊息物件，向使用者詢問需求。
1. 加入一個 `quickReply` 物件，並在其中放入一個 `items` 陣列。在該陣列中加入三個快速回覆按鈕物件。
1. 前兩個快速回覆按鈕用來指定餐點類型。設定圖示、標籤與 message action。當使用者點選任一按鈕時，使用者所選的餐點類型就會作為使用者的回覆被送出。
1. 第三個快速回覆按鈕用來提示使用者傳送其位置。為此按鈕加入引導使用者傳送位置資訊的標籤，以及一個 location action。若要使用預設圖示，請不要指定 `imageUrl` 屬性。

以下是帶有快速回覆按鈕的訊息範例。標有數字的那幾行對應到上方所列的指示編號。

```sh
{
  "type": "text", // 1
  "text": "Select your favorite food category or send me your location!",
  "quickReply": { // 2
    "items": [
      {
        "type": "action", // 3
        "imageUrl": "https://example.com/sushi.png",
        "action": {
          "type": "message",
          "label": "Sushi",
          "text": "Sushi"
        }
      },
      {
        "type": "action",
        "imageUrl": "https://example.com/tempura.png",
        "action": {
          "type": "message",
          "label": "Tempura",
          "text": "Tempura"
        }
      },
      {
        "type": "action", // 4
        "action": {
          "type": "location",
          "label": "Send location"
        }
      }
    ]
  }
}
```

以下是使用者在聊天中看到的快速回覆按鈕，搭配上方指定的訊息。

![Quick reply sample 2](https://developers.line.biz/media/messaging-api/using-quick-reply/quickReplySample2.png)

## Quick reply buttons disappear 

快速回覆按鈕會在下列情況消失：

- 使用者點選其中一個快速回覆按鈕。（camera、camera roll、datetime picker action 與 location 動作除外。帶有這些動作的按鈕會持續顯示，直到送出所預期的資料為止。）
- 您的 LINE 官方帳號、使用者或其他成員在該聊天室中傳送了新訊息。（若該新訊息被刪除，快速回覆按鈕會再次出現。）

對於某些動作而言，點選快速回覆按鈕並不會自動將使用者的選擇張貼到聊天中。為了讓使用者知道並看到自己按了哪個回覆按鈕來回覆，請以讓所送出的回覆作為訊息留存在聊天中的方式來實作。

## Related pages 

- [Message types](https://developers.line.biz/en/docs/messaging-api/message-types/)
- [Actions](https://developers.line.biz/en/docs/messaging-api/actions/)
- Messaging API 參考文件中的 [Message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)
