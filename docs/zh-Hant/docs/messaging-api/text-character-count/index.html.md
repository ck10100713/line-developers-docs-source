# 文字中的字元計數方式（Character counting in a text）

Messaging API 以 UTF-16 編碼單元（16 位元）計算文字字元數。由多個編碼單元組成的字元（例如某些漢字、Unicode 表情符號）會被計算為多個字元。舉例來說，Unicode 表情符號 🍎 是以兩個編碼單元表示，因此 🍎 的長度是兩個字元，而非一個。

當 Messaging API 計算含有 [LINE 表情貼（LINE emoji）](https://developers.line.biz/en/docs/messaging-api/emoji-list/)的文字時，表情貼的預留位置（placeholder，`$`）會被替換成該表情貼的替代文字（alternative text）。替代文字是在無法顯示 LINE 表情貼的裝置上，用來取代表情貼顯示的文字。因此，當你傳送含有 LINE 表情貼的文字訊息時，文字長度可能會在非預期的情況下超過上限，導致訊息傳送失敗。請注意，LINE 並不會公開 LINE 表情貼的替代文字。

不過，以下列出的屬性是以[字位叢集（grapheme cluster）](https://unicode.org/reports/tr29/)為單位計算，而非以 UTF-16 編碼單元計算：

| Type | Property |
| --- | --- |
| 所有[動作物件（action objects）](https://developers.line.biz/en/reference/messaging-api/#action-objects) | <ul><li>`label`</li></ul> |
| [Postback 動作物件（Postback action objects）](https://developers.line.biz/en/reference/messaging-api/#postback-action) | <ul><li>`displayText`</li><li>`fillInText`</li><li>`label`</li><li>`text`</li></ul> |
| [Message 動作物件（Message action objects）](https://developers.line.biz/en/reference/messaging-api/#message-action) | <ul><li>`label`</li><li>`text`</li></ul> |
| [Buttons 範本訊息（Buttons template messages）](https://developers.line.biz/en/reference/messaging-api/#buttons) | <ul><li>`text`</li><li>`title`</li></ul> |
| [Confirm 範本訊息（Confirm template messages）](https://developers.line.biz/en/reference/messaging-api/#confirm) | <ul><li>`text`</li></ul> |
| [Carousel 範本訊息（Carousel template messages）](https://developers.line.biz/en/reference/messaging-api/#carousel) | <ul><li>`text`</li><li>`title`</li></ul> |
| [Rich menu 物件（Rich menu objects）](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object) | <ul><li>`chatBarText`</li><li>`name`</li></ul> |
