# 體驗圖文選單（Play with rich menus）

Rich Menu Playground 是一個讓你測試圖文選單（rich menu）功能的 LINE 官方帳號。此帳號僅提供日文服務。你可以實際操作圖文選單的各項功能，例如透過 [datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action) 選擇日期，以及使用 [rich menu aliases](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/) 切換不同的圖文選單。

![Rich Menu Playground main screen](https://developers.line.biz/media/messaging-api/rich-menu-playground/richmenu-playground-bot-overview.png)

## Add Rich Menu Playground 

將 Rich Menu Playground 加為你的 LINE 帳號好友，即可測試圖文選單功能。你可以依照下列指示，以不同方式加入 Rich Menu Playground。

<!-- tip start -->

**在智慧型手機上使用 Rich Menu Playground**

圖文選單不會顯示在 LINE for PC（macOS、Windows）上。請使用智慧型手機來體驗 Rich Menu Playground。

<!-- tip end -->

| 加入方式 | 如何加入 |
| --- | --- |
| URL | 在你的智慧型手機瀏覽器中開啟 [https://lin.ee/7ALASDvA](https://lin.ee/7ALASDvA) 並加入。 |
| QR code | 掃描此 Rich Menu Playground 的 QR code 並加入。[^qrcode]</br></br>![QR code of Rich Menu Playground](https://qr-official.line.me/sid/M/976nukmg.png) |
| ID | 在 LINE 中搜尋 ID `@try_richmenu` 並加入此帳號。[^search-line-id] |

[^qrcode]: 在 LINE 使用者指南中了解[如何透過連結或 QR code 加好友](https://guide.line.me/ja/friends-and-groups/add-qrurl.html)（僅提供日文）。
[^search-line-id]: 在 LINE 使用者指南中了解[如何透過 ID 搜尋加好友](https://guide.line.me/ja/friends-and-groups/search-line-id.html)（僅提供日文）。

## Common features of Rich Menu Playground 

如果你已將 Rich Menu Playground 加為好友，現在就可以試試設定在圖文選單上的各項動作（action）。請了解[圖文選單的版面配置](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#main-rich-menu)，以及在試用某個動作後如何查看[動作詳細資訊](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#message-from-rich-menu-playground)。

### Rich menu layout 

Rich Menu Playground 的圖文選單有四個主要元件：

1. 分頁（Tabs）：包含用來試用不同動作的選單。
2. 導覽按鈕（Navigation button）：在不同分頁群組之間切換。
3. 動作按鈕（Action button）：觸發設定在該按鈕上的動作。如果某個動作需要參數，每個參數都會各有一個按鈕供你試用。
4. 說明按鈕（Help button）：開啟對應動作的文件。

![Main Menu](https://developers.line.biz/media/messaging-api/rich-menu-playground/menu-descriptions.png)

### Action detail 

當你觸發某個動作時，Rich Menu Playground 會執行該動作，然後顯示你所觸發動作的詳細資訊。這有助於你確認動作已被觸發，尤其是在動作不會呈現任何視覺結果的情況下特別有用。動作詳細資訊包含動作的說明、動作設定（參數），以及 LINE Platform 傳送給 bot 伺服器的 webhook 事件。

![Message after the action is executed](https://developers.line.biz/media/messaging-api/rich-menu-playground/message.png)

## Actions available on Rich Menu Playground 

透過 Rich Menu Playground，你可以測試：

- [Message action](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-message-action)
- [Postback action (1)](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-postback-1-action)
- [Postback action (2)](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-postback-2-action)
- [Postback action (3)](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-postback-3-action)
- [URI action](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-uri-action)
- [Datetime picker action](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-datetime-picker-action)
- [Rich menu switch action](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/#try-richmenu-switch-action)

### Test message action 

此分頁讓你觸發 [message action](https://developers.line.biz/en/reference/messaging-api/#message-action)，從圖文選單傳送訊息。

![Try Message Action](https://developers.line.biz/media/messaging-api/rich-menu-playground/01-message-action-ja.png)

<!-- tip start -->

**Message action**

當使用者在與你的 LINE 官方帳號的聊天中，透過圖文選單傳送訊息時，LINE Platform 會將對應的 [message event](https://developers.line.biz/en/reference/messaging-api/#message-event) 傳送給你的 bot 伺服器。你的 bot 伺服器接著就能使用透過 message event 取得的回覆權杖（reply token），傳送[回覆訊息（reply message）](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)。

<!-- tip end -->

| Button label | Action | Action object |
| --- | --- | --- |
| Send message | 傳送一則訊息 | `{"type":"message", "label":"メッセージを送信する","text":"message sent successfully!"}` |

### Test postback action (1) 

此分頁讓你從圖文選單觸發 [postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)。當你觸發此動作時，LINE Platform 會將一個 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 傳送給 bot 伺服器，其中包含你在 postback action object 的 `data` 屬性中指定的字串。

![Try Postback Action (1)](https://developers.line.biz/media/messaging-api/rich-menu-playground/02-postback-action-ja.png)

<!-- tip start -->

**Postback action**

當使用者點選設有 [postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action) 的圖文選單時，LINE Platform 會將 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 傳送給你的 bot 伺服器。此 postback event 會帶有你在 postback action 的 `data` 屬性中指定的字串。

你在 `data` 屬性中指定的內容不會顯示給使用者。這可確保諸如獨特參數和識別碼等資料能安全地傳送至你的 bot 伺服器。你可以使用從 postback event 取得的回覆權杖，傳送[回應訊息（response message）](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)。

<!-- tip end -->

| Button label | Action | Action object |
| --- | --- | --- |
| With `displayText`  | 觸發 postback action 並在聊天中顯示一段文字 | `{"type":"postback","label":"ディスプレイテキストあり","data":"actionId=21","displayText":"ディスプレイテキストです。トーク画面に表示されます。"}` |
| No `displayText` | 觸發 postback action 但不在聊天中顯示文字 | `{"type":"postback","label":"ディスプレイテキストなし","data":"actionId=22"}` |

<!-- tip start -->

**聊天中的文字（displayText）**

若要在觸發 postback action 時，於聊天中以使用者訊息的形式顯示文字，請在 postback action object 中指定 `displayText` 屬性。該文字會顯示在聊天中，但不會以 [message event](https://developers.line.biz/en/reference/messaging-api/#message-event) 的形式傳送給 bot 伺服器。

<!-- tip end -->

### Test postback action (2) 

在此分頁中，你可以試用開啟與關閉圖文選單的 [postback actions](https://developers.line.biz/en/reference/messaging-api/#postback-action)。當 postback action 執行時，LINE Platform 會將一個含有你在 `data` 屬性中指定字串的 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 傳送給 bot 伺服器。

![Try Postback Action (2)](https://developers.line.biz/media/messaging-api/rich-menu-playground/02-2-postback-action-ja.png)

| Button label | Action | Action object |
| --- | --- | --- |
| Open rich menu | 執行設有 `inputOption:openRichMenu` 的 postback action。 | `{"type":"postback","label":"リッチメニューを開く","data":"actionId=","inputOption":"openRichMenu"}` |
| Close rich menu | 執行設有 `inputOption:closeRichMenu` 的 postback action。 | `{"type":"postback","label":"リッチメニューを閉じる","data":"actionId=","inputOption":"closeRichMenu"}` |

### Test postback action (3) 

在此分頁中，你可以試用設定為開啟鍵盤與語音訊息輸入模式的 [postback actions](https://developers.line.biz/en/reference/messaging-api/#postback-action) 圖文選單。一旦 postback action 執行，LINE Platform 會將一個含有你在 `data` 屬性中指定字串的 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 傳送給 bot 伺服器。

![Try Postback Action (3)](https://developers.line.biz/media/messaging-api/rich-menu-playground/02-3-postback-action-ja.png)

| Button label | Action | Action object |
| --- | --- | --- |
| Open keyboard | 執行設有 `inputOption:openKeyboard` 的 postback action。 | `{"type":"postback","label":"キーボードを開く","data":"actionId=","inputOption":"openKeyboard"}` |
| Open keyboard with fillinText | 執行設有 `inputOption:openKeyboard` 與 `fillInText` 的 postback action。 | `{"type":"postback","label":"キーボードを開くフィルインテキストあり","data":"actionId=","inputOption":"openKeyboard","fillInText":"---\予約番号: \予約メニュー番号: \n予約日時: \n---"}` |
| Open voice message input mode | 執行設有 `inputOption:openVoice` 的 postback action。 | `{"type":"postback","label":"ボイスメッセージ入力モードを開く","data":"actionId=","inputOption":"openVoice"}` |

### Test URI Action 

在此分頁中，你可以從圖文選單觸發 [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)。當你觸發此動作時，設定在該動作的 `uri` 會在網頁瀏覽器中開啟。

![Try URI action](https://developers.line.biz/media/messaging-api/rich-menu-playground/03-uri-action-ja.png)

| Button label | Action | Action object |
| --- | --- | --- |
| Open a URL | 開啟指定的 URI | `{"type":"uri","label":"URLを開く","uri":"https://developers.line.biz/docs/messaging-api/actions/#uri-action"}` |
| Open in an external browser | 在[外部瀏覽器（external browser）](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-url-in-external-browser)中開啟 URI（`openExternalBrowser=0`） | `{"type":"uri","label":"外部ブラウザで開く","uri":"https://developers.line.biz/docs/messaging-api/actions/?openExternalBrowser=1#uri-action"}` |
| Open in a Chrome custom tab (Android only) | 在支援的情況下，於[應用程式內瀏覽器（in-app browser）](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-url-in-external-browser)中開啟 URI（`openInAppBrowser=0`） | `{"type":"uri","label":"Chromeカスタムタブで開く","uri":"https://developers.line.biz/docs/messaging-api/actions/?openInAppBrowser=0#uri-action"}` |
| Check configuration (The white buttons) | 不會開啟 URI，而是顯示設定在 URI action object 中的值 | 不適用 |

<!-- tip start -->

**關於 openInAppBrowser**

`openInAppBrowser` 參數僅在 LINE for Android 中開啟 LINE 的應用程式內瀏覽器。關於 `openInAppBrowser` 參數的規格，請參閱[在外部瀏覽器中開啟 URL](https://developers.line.biz/en/docs/messaging-api/using-line-url-scheme/#opening-url-in-external-browser)。

<!-- tip end -->

### Test datetime picker action 

在此分頁中，你可以從圖文選單觸發 [datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)。當你觸發此動作時，會顯示日期與時間選擇對話框。一旦你選擇了日期，LINE Platform 會將一個含有所選日期與時間的 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 傳送給你的 bot 伺服器。

![Try Datetime Picker Action](https://developers.line.biz/media/messaging-api/rich-menu-playground/04-datetime-picker-action-ja.png)

| Button label | Action | Action object |
| --- | --- | --- |
| Date and time selection (datetime mode) | 開啟設定為目前日期與時間的日期時間選擇器（`mode` 設為 `datetime`） | `{"type":"datetimepicker","label":"datetimeモード","data":"actionId=31","mode":"datetime"}` |
| With initial value set (with `initial` property) | 開啟設定為 `initial` 屬性值的日期時間選擇器 | `{"type":"datetimepicker","label":"初期値設定あり","data":"actionId=32","initial:"2021-11-01t00:00","mode":"datetime"}` |
| With max and min values set (with `min`, `max` properties) | 開啟已設定最小與最大日期的日期時間選擇器 | `{"type":"datetimepicker","label":"最大・最小値設定あり","data":"actionId=33","mode":"datetime","max":"2021-12-31t23:59","min":"2021-11-01t00:00"}` |
| Select date (date mode) | 開啟設定為目前日期的日期時間選擇器 | `{"type":"datetimepicker","label":"dateモード","data":"actionId=34","mode":"date"}` |
| Select time (time mode) | 開啟設定為目前時間的日期時間選擇器 | `{"type":"datetimepicker","label":"timeモード","data":"actionId=35","mode":"time"}` |

### Test rich menu switch action 

在此分頁中，你可以從圖文選單觸發 [rich menu switch action](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)。當你觸發此動作時，圖文選單會切換成在 [rich menu aliases](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/) 中定義的選單。當圖文選單切換時，LINE Platform 會將一個 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 傳送給你的 bot 伺服器。此事件帶有你為 postback action object 中的 `data` 屬性與 `postback.params` object 所指定的值。

![Try Rich Menu Switching Action](https://developers.line.biz/media/messaging-api/rich-menu-playground/05-rich-menu-switch-action-ja.png)

| Button label | Action | Action object |
| --- | --- | --- |
| Switch rich menu | 切換圖文選單 | `{"type":"richmenuswitch","label":"リッチメニューを切り替える","richMenuAliasId":"richmenu-richmenuswitch_2","data":"actionId=42"}` |
| Switch rich menu to a smaller size | 將圖文選單切換成由 rich menu object 中 `size` 屬性的 `height` 所指定的較小尺寸 | `{"type":"richmenuswitch","label":"小さいサイズのリッチメニューに切り替える","richMenuAliasId":"richmenu-richmenuswitch_3","data":"actionId=43"}` |
