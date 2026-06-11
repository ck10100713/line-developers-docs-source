# 建立包含影片的 Flex Message（Create a Flex Message including a video）

使用 Flex Message 的 video 元件，你可以在 hero [block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) 中顯示影片。如需有關傳送 Flex Message 的詳細資訊，請參閱[傳送 Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)。

<!-- table of contents -->

## Requirements to include videos in Flex Messages 

若要在 Flex Message 中加入 [video](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#video) 元件，你必須：

- 將 hero [block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block) 的類型指定為 `video`。
- 將 bubble 的尺寸指定為 `kilo`、`mega` 或 `giga`。
- 該 bubble 不是 carousel 的子元素。

## Video aspect ratio 

如果你的影片太寬或太高，根據裝置的不同，影片可能無法完整顯示，而是被裁切。為了讓影片正確顯示，請確保以下所有項目的長寬比（aspect ratio）都相同：

- `url` 屬性所指定影片的長寬比
- `aspectRatio` 屬性所指定的長寬比
- `previewUrl` 屬性所指定預覽圖片的長寬比

![A video in a LINE chat room. A preview image with a 1:1 aspect ratio is displayed behind the video that has an aspect ratio of 16:9.](https://developers.line.biz/media/messaging-api/messages/image-overlapping-en.png)

## URI actions for videos 

使用 `action` 屬性，你可以指定 [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)。這個 action 可讓使用者在 LINE 的應用程式內瀏覽器中開啟 URL，或使用裝置的通話應用程式撥打指定號碼。URI action 的標籤會顯示在以下三個位置：

- [聊天室（影片播放後）](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#chat-room-screen)
- [影片播放器（影片播放期間）](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#video-player-screen1)
- [影片播放器（影片播放後）](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#video-player-screen2)

![A chat room when a video finishes playing](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/label-in-chat-room-en.png)
![A video player while a video is playing](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/label-in-video-player1-en.png)
![A video player when a video finishes playing](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/label-in-video-player2-en.png)

## Define a Flex Message with a video 

包含影片的 Flex Message 最基本的版面配置就是只有影片，如下所示。

![Video component example](https://developers.line.biz/media/messaging-api/flex-message-elements/video-sample.png)

你必須使用 `hero` block 來插入影片。為了讓包含影片的 Flex Message 在不支援 video 元件的 LINE 版本上也能正常顯示，請指定替代內容。在 hero block 的 `altContent` 屬性中指定要取代影片顯示的內容。此 Flex Message 範例的 JSON 定義如下。

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

只包含影片的 Flex Message 看起來會像[影片訊息](https://developers.line.biz/en/reference/messaging-api/#video-message)。使用 Flex Message，你可以用更複雜的版面配置來建立包含影片的訊息。

![Video component example](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/video.png)

此 Flex Message 範例的 JSON 定義如下。

```json
{
  "type": "bubble",
  "size": "mega",
  "hero": {
    "type": "video",
    "url": "https://example.com/video.mp4",
    "previewUrl": "https://example.com/video_preview.png",
    "altContent": {
      "type": "image",
      "size": "full",
      "aspectRatio": "20:13",
      "aspectMode": "cover",
      "url": "https://example.com/image.png"
    },
    "action": {
      "type": "uri",
      "label": "More information",
      "uri": "http://example.com/"
    },
    "aspectRatio": "20:13"
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": "Brown Cafe",
        "weight": "bold",
        "size": "xl"
      },
      {
        "type": "box",
        "layout": "baseline",
        "margin": "md",
        "contents": [
          {
            "type": "icon",
            "size": "sm",
            "url": "https://example.com/star.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://example.com/star.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://example.com/star.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://example.com/star.png"
          },
          {
            "type": "icon",
            "size": "sm",
            "url": "https://example.com/gray_star.png"
          },
          {
            "type": "text",
            "text": "4.0",
            "size": "sm",
            "color": "#999999",
            "margin": "md",
            "flex": 0
          }
        ]
      },
      {
        "type": "box",
        "layout": "vertical",
        "margin": "lg",
        "spacing": "sm",
        "contents": [
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Place",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "1-3 Kioicho, Chiyoda-ku, Tokyo",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          },
          {
            "type": "box",
            "layout": "baseline",
            "spacing": "sm",
            "contents": [
              {
                "type": "text",
                "text": "Time",
                "color": "#aaaaaa",
                "size": "sm",
                "flex": 1
              },
              {
                "type": "text",
                "text": "10:00 - 23:00",
                "wrap": true,
                "color": "#666666",
                "size": "sm",
                "flex": 5
              }
            ]
          }
        ]
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "spacing": "sm",
    "contents": [
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "CALL",
          "uri": "https://example.com"
        }
      },
      {
        "type": "button",
        "style": "link",
        "height": "sm",
        "action": {
          "type": "uri",
          "label": "WEBSITE",
          "uri": "https://example.com"
        }
      },
      {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "margin": "sm"
      }
    ],
    "flex": 0
  }
}
```

## Playback behavior 

你可以從[聊天室](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#chat-room)或使用[影片播放器](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#video-player)來播放以 Flex Message 傳送的影片。

<!-- note start -->

**如果影片無法正常播放**

即使包含影片的訊息成功傳送，影片在使用者的裝置上仍可能無法正常播放。如需詳細資訊，請參閱常見問題中的[為什麼我無法播放以訊息傳送的影片？](https://developers.line.biz/en/faq/#why-cant-i-play-a-video-i-sent)。

<!-- note end -->

### Playback in a chat room 

播放如何開始取決於使用者在 LINE 中的設定，位於 **設定** > **照片與影片** > **自動播放影片**。LINE for PC（macOS 與 Windows）不支援自動播放。

| 設定                  | 影片播放                                          |
| --------------------- | ------------------------------------------------- |
| **行動網路與 Wi-Fi**  | 影片播放會自動開始                                |
| **僅限 Wi-Fi**        | 僅在 Wi-Fi 環境下影片播放才會自動開始             |
| **永不**              | 影片播放永遠不會自動開始                          |

#### Screen when video playback finishes 

當影片播放結束時，你最多可以在影片上方顯示兩個按鈕。第一個是 **播放**，當使用者點擊此按鈕時會啟動影片播放器並開始播放。如需詳細資訊，請參閱[在影片播放器中播放](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#video-player)。

第二個按鈕是 **More information**，會顯示你在 video 元件中指定的 URI action 標籤。你可以變更此文字。如果你沒有為 video 元件指定 URI action，則只會顯示 **播放**。如需詳細資訊，請參閱 [URI actions for videos](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#uri-action)。

![Screen when a video finishes playing](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/auto-play-finished-en.png)

### Playback in a video player 

當使用者點擊聊天室中的影片時，會啟動影片播放器並開始播放影片。你在[播放期間](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#video-player-screen1)與[播放後](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#video-player-screen2)看到的按鈕並不相同。

#### Screen during playback 

當影片正在播放時，你最多可以在影片播放器頂部顯示兩個按鈕。第一個是 **完成**，當使用者點擊此按鈕時會關閉影片播放器，並將使用者帶回聊天室。如果符合[自動播放](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#chat-room)的條件，影片會在聊天室中繼續播放。

第二個按鈕是 **More information**，會顯示你在 video 元件中指定的 URI action 標籤。你可以變更此文字。如果你沒有為 video 元件指定 URI action，則只會顯示 **完成**。如需詳細資訊，請參閱 [URI actions for videos](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#uri-action)。

![Screen while a video is playing](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/video-player-en.png)

#### Screen when playback is complete 

當影片播放結束時，你最多可以在影片上方顯示兩個按鈕。第一個是 **重播**，當使用者點擊此按鈕時會在影片播放器中重新開始播放。

第二個按鈕是 **More information**，會顯示你在 video 元件中指定的 URI action 標籤。你可以變更此文字。如果你沒有為 video 元件指定 URI action，則只會顯示 **重播**。如需詳細資訊，請參閱 [URI actions for videos](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#uri-action)。

![Screen when a video finishes playing](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/video-player-finished-en.png)

## Display on version of LINE that doesn't support the video component 

如果 LINE 的版本低於支援 video 元件的版本，則會顯示指定為 `altContent` 屬性值的元件。請在 `altContent` 屬性中使用 [box](https://developers.line.biz/en/reference/messaging-api/#box) 元件或 [image](https://developers.line.biz/en/reference/messaging-api/#f-image) 元件。

## Videos in Flex Message Simulator 

你無法在 [Flex Message Simulator](https://developers.line.biz/flex-simulator/) 上預覽影片。取而代之，你設定的替代內容會顯示在 Flex Message Simulator 的預覽區域中，就像在 [Display on version of LINE that doesn't support the video component](https://developers.line.biz/en/docs/messaging-api/create-flex-message-including-video/#alt-content) 中一樣。

若要檢視你以 Flex Message Simulator 編輯的 Flex Message 中的影片，請從模擬器將訊息傳送到你的 LINE。你可以使用 Flex Message Simulator 右上角的 **Send...** 選單，從模擬器傳送測試訊息。

![The Send... button on Flex Message Simulator](https://developers.line.biz/media/messaging-api/create-flex-message-including-video/send.png)

## Related pages 

- [傳送 Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)
- [Flex Message 元素](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)
- [Flex Message 版面配置](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)
- [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)（Messaging API reference）
- [Flex Message Simulator](https://developers.line.biz/flex-simulator/)
