# 訊息類型（Message types）

透過 Messaging API，你可以讓你的機器人傳送以下這些類型的訊息。若要讓訊息具有互動性，你可以在訊息上指定一個動作（action），供使用者觸發。各訊息類型的規格說明，請參閱 Messaging API 參考文件中的 [Message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)。

- [Text message](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)
- [Text message (v2)](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages-v2)
- [Sticker message](https://developers.line.biz/en/docs/messaging-api/message-types/#sticker-messages)
- [Image message](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)
- [Video message](https://developers.line.biz/en/docs/messaging-api/message-types/#video-messages)
- [Audio message](https://developers.line.biz/en/docs/messaging-api/message-types/#audio-messages)
- [Location message](https://developers.line.biz/en/docs/messaging-api/message-types/#location-messages)
- [Coupon message](https://developers.line.biz/en/docs/messaging-api/message-types/#coupon-messages)
- [Imagemap message](https://developers.line.biz/en/docs/messaging-api/message-types/#imagemap-messages)
- [Template message](https://developers.line.biz/en/docs/messaging-api/message-types/#template-messages)
- [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages)

## Text message 

文字訊息（text message）包含文字內容，也包含表情符號（emoji）。若要傳送文字訊息，請在你透過 Messaging API 傳送的 [message object](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中加入文字。詳情請參閱 Messaging API 參考文件中的 [Text message](https://developers.line.biz/en/reference/messaging-api/#text-message)。

![Text message](https://developers.line.biz/media/messaging-api/messages/text.png)

你可以在文字訊息中使用 LINE 表情符號與 Unicode 表情符號。請查看可透過 Messaging API 傳送的 [LINE emojis](https://developers.line.biz/en/docs/messaging-api/emoji-list/) 清單。

![Emoji](https://developers.line.biz/media/messaging-api/messages/emoji.png)

<!-- tip start -->

**文字裝飾與調整大小**

若要為文字加上裝飾或調整大小，請使用 [Flex Messages](https://developers.line.biz/en/reference/messaging-api/#flex-message)。

<!-- tip end -->

## Text message (v2) 

你可以使用文字訊息（v2）來傳送文字。與[文字訊息](https://developers.line.biz/en/docs/messaging-api/message-types/#text-messages)不同的是，你可以將以 `{` 和 `}` 括住的字串替換成提及（mention）與表情符號。詳情請參閱 Messaging API 參考文件中的 [Text message (v2)](https://developers.line.biz/en/reference/messaging-api/#text-message-v2)。

![](https://developers.line.biz/media/messaging-api/messages/text-v2.png)

你仍可以繼續使用我們至今提供的文字訊息。不過，今後我們可能只會為文字訊息（v2）新增新功能。

## Sticker message 

貼圖（sticker）能讓你的機器人對使用者來說更有吸引力、更有趣。若要透過 Messaging API 傳送貼圖，請在 [message object](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中指定貼圖的 package ID 與 sticker ID。請查看可傳送的[貼圖](https://developers.line.biz/en/docs/messaging-api/sticker-list/)清單。詳情請參閱 Messaging API 參考文件中的 [Sticker message](https://developers.line.biz/en/reference/messaging-api/#sticker-message)。

![Sticker message](https://developers.line.biz/media/messaging-api/messages/sticker.png)

## Image message 

圖片訊息（image message）會向使用者傳遞單一圖片檔。傳送圖片時，請在 [message object](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中指定兩個 URL：一個是原始圖片，另一個是預覽圖。預覽圖是顯示在聊天室中的圖片，因此請指定一張比原始圖片更小的圖片。

當使用者點按預覽圖時，會顯示完整圖片，如下所示。請確認 URL 使用 HTTPS（TLS 1.2 以上）通訊協定。詳情請參閱 Messaging API 參考文件中的 [Image message](https://developers.line.biz/en/reference/messaging-api/#image-message)。

![Image message](https://developers.line.biz/media/messaging-api/messages/image.png) ![Full image message](https://developers.line.biz/media/messaging-api/messages/image-full.png)

## Video message 

影片訊息（video message）會向使用者傳遞單一影片檔。傳送影片訊息時，請在 [message object](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中指定兩個 URL，一個是影片檔，另一個是預覽圖。

當使用者點按預覽圖時，LINE 會播放該影片。請確認 URL 使用 HTTPS（TLS 1.2 以上）通訊協定。詳情請參閱 Messaging API 參考文件中的 [Video message](https://developers.line.biz/en/reference/messaging-api/#video-message)。

![Video message](https://developers.line.biz/media/messaging-api/messages/video.png)

## Audio message 

音訊訊息（audio message）會向使用者傳遞單一音訊檔。若要傳送音訊檔，請在 [message object](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中指定該檔案的 URL 與播放時長。

請確認 URL 使用 HTTPS（TLS 1.2 以上）通訊協定。詳情請參閱 Messaging API 參考文件中的 [Audio message](https://developers.line.biz/en/reference/messaging-api/#audio-message)。

![Audio message](https://developers.line.biz/media/messaging-api/messages/audio.png)

## Location message 

位置訊息（location message）會向使用者傳遞位置資訊。請在 [message object](https://developers.line.biz/en/reference/messaging-api/#message-objects) 中指定標題、地址、緯度座標與經度座標。詳情請參閱 Messaging API 參考文件中的 [Location message](https://developers.line.biz/en/reference/messaging-api/#location-message)。

![Location message](https://developers.line.biz/media/messaging-api/messages/location-en.png)

## Coupon message 

優惠券訊息（coupon message）透過指定 coupon ID，向使用者傳遞優惠券。

![](https://developers.line.biz/media/messaging-api/coupon/several-coupons.jpg)

詳情請參閱 Messaging API 參考文件中的 [Coupon message](https://developers.line.biz/en/reference/messaging-api/#coupon-message)。

## Imagemap message 

Imagemap 訊息是帶有一張圖片、且該圖片具有多個可點按區域的訊息。你可以設定可點按區域，讓它開啟網頁或代替使用者傳送訊息。你也可以設定在圖片上播放影片，並在播放結束後顯示一段連結文字。詳情請參閱 Messaging API 參考文件中的 [Imagemap message](https://developers.line.biz/en/reference/messaging-api/#imagemap-message)。

![Imagemap message](https://developers.line.biz/media/messaging-api/messages/imagemap.png)

## Template message 

範本訊息（template message）具有預先定義的版面配置，能協助你為使用者打造更豐富的體驗。使用[動作（actions）](https://developers.line.biz/en/docs/messaging-api/actions/)讓使用者與你的機器人互動。使用者只需點按一下即可觸發動作，比起必須輸入訊息要簡單得多。

可用的範本如下：

- [Buttons](https://developers.line.biz/en/docs/messaging-api/message-types/#buttons-template)
- [Confirm](https://developers.line.biz/en/docs/messaging-api/message-types/#confirm-template)
- [Carousel](https://developers.line.biz/en/docs/messaging-api/message-types/#carousel-template)
- [Image carousel](https://developers.line.biz/en/docs/messaging-api/message-types/#image-carousel-template)

關於範本訊息的更多資訊，請參閱 Messaging API 參考文件中的 [Template messages](https://developers.line.biz/en/reference/messaging-api/#template-messages)。此外，若你想傳送版面配置更靈活的訊息，請使用 [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages)。

### Buttons template 

按鈕範本（buttons template）包含圖片、標題、文字以及[動作（action）](https://developers.line.biz/en/docs/messaging-api/actions/)按鈕等欄位。除了按鈕之外，你也可以在圖片、標題或文字區域上設定動作。當使用者點按已設定動作的元素時，就會觸發該動作。詳情請參閱 Messaging API 參考文件中的 [Buttons template](https://developers.line.biz/en/reference/messaging-api/#buttons)。

![Buttons template message](https://developers.line.biz/media/messaging-api/messages/buttons.png)

### Confirm template 

確認範本（confirm template）包含文字與兩個按鈕等欄位。詳情請參閱 Messaging API 參考文件中的 [Confirm template](https://developers.line.biz/en/reference/messaging-api/#confirm)。

![Confirm template message](https://developers.line.biz/media/messaging-api/messages/confirm.png)

### Carousel template 

輪播範本（carousel template）包含多個欄（column），使用者可以左右切換瀏覽。除了按鈕之外，你也可以在每個欄物件中設定[動作（action）](https://developers.line.biz/en/docs/messaging-api/actions/)。

當使用者點按某個欄物件的圖片、標題或文字區域的任意處時，就會觸發動作。詳情請參閱 Messaging API 參考文件中的 [Carousel template](https://developers.line.biz/en/reference/messaging-api/#carousel)。

![Carousel template message](https://developers.line.biz/media/messaging-api/messages/carousel.png)

### Image carousel template 

圖片輪播範本（image carousel template）包含多張圖片，使用者可以左右切換瀏覽。詳情請參閱 Messaging API 參考文件中的 [Image carousel template](https://developers.line.biz/en/reference/messaging-api/#image-carousel)。

![Image carousel template message](https://developers.line.biz/media/messaging-api/messages/image-carousel.png)

## Flex Message 

Flex Message 是版面配置可自訂的訊息。你可以在 [CSS Flexible Box（CSS Flexbox）](https://www.w3.org/TR/css-flexbox-1/)規格的範圍內自訂版面配置。詳情請參閱 [Send Flex Messages](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/) 以及 Messaging API 參考文件中的 [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)。

![Flex Message examples](https://developers.line.biz/media/messaging-api/using-flex-messages/bubbleSamples-Update1.png)

## Common features 

此功能適用於所有訊息類型。

### Quick reply 

快速回覆（quick reply）按鈕適用於所有訊息類型，並顯示在聊天室底部。使用者可以點按其中一個按鈕來回覆你的機器人。詳情請參閱 [Use quick replies](https://developers.line.biz/en/docs/messaging-api/using-quick-reply/) 以及 Messaging API 參考文件中的 [Quick reply](https://developers.line.biz/en/reference/messaging-api/#quick-reply)。

![Quick reply sample](https://developers.line.biz/media/messaging-api/using-quick-reply/quickReplySample.png)

## Related pages 

進一步了解 Messaging API：

- [Sending messages](https://developers.line.biz/en/docs/messaging-api/sending-messages/)
- [Message objects](https://developers.line.biz/en/reference/messaging-api/#message-objects)
- [Actions](https://developers.line.biz/en/docs/messaging-api/actions/)
