# LINE 通知訊息 API 的技術規格（Technical specifications of the LINE notification messages API）

<!-- note start -->

**使用選用功能需提出申請**

只有已提交必要申請的企業用戶，才能使用本文件所述的功能。若要在您的 LINE 官方帳號上使用這些功能，請聯絡您的業務負責人，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## Send LINE notification messages to users 

企業會根據其所持有的客戶電話號碼，向 LINE Platform 伺服器發送訊息請求，並將 LINE 通知訊息發送至已將該電話號碼註冊至 LINE 的用戶帳號。企業所傳送的電話號碼會經過雜湊處理，LY Corporation 僅將接收到的資訊用於比對訊息發送的目的地，並在比對完成後立即銷毀。此外，為確認包含個人資訊在內的通知內容並繼續後續程序，可能需要透過 SMS 驗證您的身分。

LINE 通知訊息有兩種類型：LINE 通知訊息（範本）與 LINE 通知訊息（彈性）。每種類型有不同的 API 端點（endpoint）。

- LINE 通知訊息（範本）
  - [Send a LINE notification message (template)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template)
  - [Get number of sent LINE notification messages (template)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-template)
- LINE 通知訊息（彈性）
  - [Send a LINE notification message (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-flexible)
  - [Get number of sent LINE notification messages (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-flexible)

如需更多資訊，請參閱 [LINE notification messages API reference](https://developers.line.biz/en/reference/line-notification-messages/)。

### Message types that can be sent in LINE notification messages 

透過 LINE 通知訊息（範本），您可以結合預先製作好的範本、項目與按鈕，輕鬆建立訊息。建立訊息時，請遵循 [LINE notification messages (template) UX guidelines](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE_Official_Notification_Template_UXGuideline.pdf)（僅提供日文版）。

![Sample of a LINE notification message (template)](https://developers.line.biz/media/line-notification-message/notification-messages-template.png)

透過 LINE 通知訊息（彈性），您可以使用 [Flex Message](https://developers.line.biz/en/docs/messaging-api/message-types/#flex-messages) 及其他類似的訊息類型，更彈性地建立訊息。不過，不允許包含圖片、影片或音訊的訊息。此外，LINE 通知訊息（彈性）需要事先經過 UX 審查，只有通過審查的訊息才能發送。建立訊息時，請遵循 [LINE notification messages (flexible) UX guidelines](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%E9%80%9A%E7%9F%A5%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8UX%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3.pdf)（僅提供日文版）。

### Phone number hashing 

在 LINE 通知訊息 API 中指定發送目的地 `to` 時，請指定一個字串，內容為已正規化為 [E.164](https://developers.line.biz/en/glossary/#e164) 格式的電話號碼（例如 `+818000001234`）並以 SHA256 雜湊後的結果。請勿包含連字號。以下是使用 Python3 對電話號碼進行雜湊處理的範例。

```python
import hashlib

phone_number = "+818000001234"
hashed_phone_number = hashlib.sha256(phone_number.encode()).hexdigest()
print(hashed_phone_number)

# d41e0ad70dddfeb68f149ad6fc61574b9c5780ab7bcb2fba5517771ffbb2409c
```

### Get message delivery notifications 

當您請求 LINE 通知訊息 API 並向用戶發送 LINE 通知訊息時，LINE Platform 會發送一個專用的 webhook 事件（[發送完成事件](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event)）。

若您在發出請求時於請求標頭的 `X-Line-Delivery-Tag` 中指定任何字串，該字串會在 webhook 的[發送完成事件](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event)的 `delivery.data` 屬性中回傳。`X-Line-Delivery-Tag` 可用於諸如在接收 webhook 時判斷哪一則訊息已被發送等用途。

如需更多資訊，請參閱 [Webhook delivery completion event](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/)。

### Get the number of sent LINE notification messages 

您可以使用以下 API 取得已發送的 LINE 通知訊息數量：

- [Get number of sent LINE notification messages (template)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-template)
- [Get number of sent LINE notification messages (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-flexible)

<!-- note start -->

**注意**

只有實際發送給用戶的 LINE 通知訊息數量，才會計入已發送訊息數量。如需更多關於發送條件的資訊，請參閱 [Conditions for sending LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#conditions-for-sending-line-notification-messages)。

<!-- note end -->

## Conditions for sending LINE notification messages 

LINE 通知訊息 API 在符合以下所有條件時，才會向用戶發送訊息：

- 您指定為 LINE 通知訊息發送目的地的電話號碼，與用戶 LINE 帳號中註冊的電話號碼相符。
- 用戶 LINE 帳號中註冊的電話號碼為有效（用戶已在特定期間內透過 SMS 驗證該電話號碼）。
- 用戶同意接收 LINE 通知訊息。
- 用戶未封鎖您的 LINE 官方帳號。
- 該電話號碼是在日本、泰國及台灣發行的，且[該電話號碼可用於在 LINE app 中進行電話號碼驗證](https://help.line.me/line/smartphone/pc?lang=en&contentId=20000104)。
- 用戶同意 LINE 的隱私權政策（2022 年 3 月或之後修訂的版本）。

如需更多關於在 LINE app 中設定 LINE 通知訊息的資訊，請參閱 LINE 用戶指南中的[如何接收 LINE 通知訊息](https://guide.line.me/ja/services/notification-message.html)（僅提供日文版）。

## Additional information about LINE notification messages and API 

- [關於「已收到 LINE 通知訊息」訊息](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#about-recive-the-new-line-notification-message)
- [LINE 通知訊息接收設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#how-to-consent-for-line-notification-messages)
- [當您尚未同意接收 LINE 通知訊息時所發送的訊息](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#user-has-not-given-consent-when-receive-line-notification-messages)
- [關於針對已封鎖 LINE 官方帳號的用戶發出的 LINE 通知訊息 API 請求](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#about-pnp-api-block-response)
- [當 LINE 通知訊息 API 請求成功但訊息未發送時](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#why-i-cant-receive-line-notification-messages)
- [關於向非 LINE 官方帳號好友的用戶發送 LINE 通知訊息時的加入好友與封鎖行為](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#when-user-add-or-block-oa)
- [向非 LINE 官方帳號好友的用戶發送 LINE 通知訊息時的圖文選單顯示](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#about-richmenu-displayed)
- [關於 LINE 通知訊息 API 中會被計入使用費用的項目](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#about-delivered-pnp-messages)

### About the "LINE notification message received" message 

在發送 LINE 通知訊息時，名為「LINE」的 LINE 官方帳號（系統帳號）會發送以下訊息。每次發送 LINE 通知訊息時，都一定會發送這則訊息。LINE 通知訊息的發送方無法阻止這則訊息的發送，也無法減少其發送次數。

![Message received notification](https://developers.line.biz/media/line-notification-message/type1-pnpflow-3-ja.png)

<!-- note start -->

**封鎖時的行為**

若被 LINE 通知訊息 API 指定為通知訊息接收方的用戶，已封鎖發送該訊息的 LINE 官方帳號，則該通知訊息以及來自「LINE」系統帳號的「已收到 LINE 通知訊息」訊息都不會被發送。

此外，在用戶封鎖 LINE 官方帳號期間所發送的 LINE 通知訊息，即使用戶之後解除封鎖，也不會被送達。

<!-- note end -->

### LINE notification message reception settings 

當 LINE 通知訊息發送給用戶時，用戶可以同意（或拒絕）接收 LINE 通知訊息。即使沒有任何 LINE 通知訊息被發送，用戶也可以隨時從 LINE app 中前往**設定** > **隱私設定** > **提供使用資料** > **LINE 通知訊息**進行同意（或拒絕）。

![Agree to receive LINE notification messages](https://developers.line.biz/media/line-notification-message/consent-line-notification-message-en.png)

#### States of reception settings 

LINE 通知訊息的接收設定有三種狀態。

| 狀態 | 說明 |
| --- | --- |
| 同意（開啟） | 已同意接收。將會發送 LINE 通知訊息。 |
| 拒絕（關閉） | 已拒絕接收。不會發送 LINE 通知訊息。 |
| 未設定 | 尚未同意也尚未拒絕。當收到 LINE 通知訊息時，會發送一則訊息詢問是否同意接收 LINE 通知訊息。<ul><li>若您是在 LINE app 8.0.0 版或更早的版本中建立新的 LINE 帳號，您對於接收 LINE 通知訊息的同意狀態將為「未設定」。</li><li>若您曾經將狀態變更為「未設定」以外的任何狀態，即使只有一次，也無法再回到「未設定」狀態。</li></ul> |

### Messages sent when you haven't consented to get LINE notification messages 

| 狀態 | 說明 |
| --- | --- |
| 拒絕（關閉） | 所請求的 LINE 通知訊息不會被發送，並會被刪除。 |
| 未設定 | 若您在收到[接收 LINE 通知訊息的設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-1)後 24 小時內同意接收 LINE 通知訊息，該訊息就會被發送。若您未在 24 小時內同意接收 LINE 通知訊息，所請求的訊息將不會被發送，並會被刪除。 |

### About LINE notification messages API requests for users who have blocked the LINE Official Account 

若透過 LINE 通知訊息 API 向已封鎖 LINE 官方帳號的用戶發出發送 LINE 通知訊息的請求，將會回傳 HTTP 狀態碼 `200` 或 `202` 的回應。但在此情況下，LINE 通知訊息實際上並不會被發送，且不會發送 [Webhook delivery completion event](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/)。

### When the LINE notification messages API request is successful but the message isn't sent 

若您已成功向未封鎖 LINE 官方帳號的用戶請求 LINE 通知訊息 API（收到 HTTP 狀態碼 `200` 或 `202`），但 LINE 通知訊息實際上並未發送給用戶，可能是以下原因：

- 與請求 LINE 通知訊息 API 時所指定電話號碼相關聯的用戶，尚未設定[接收 LINE 通知訊息的設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-1)，且在收到接收 LINE 通知訊息的設定時，將其變更為「拒絕」。
- 與請求 LINE 通知訊息 API 時所指定電話號碼相關聯的用戶，尚未設定[接收 LINE 通知訊息的設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-1)，且在收到接收 LINE 通知訊息的設定時，將其保留為未設定狀態。
- 與請求 LINE 通知訊息 API 時所指定電話號碼相關聯的用戶需要進行 SMS 驗證，但該用戶在收到[電話號碼驗證](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-3)訊息時並未執行 SMS 驗證。

### About adding and blocking friends when sending LINE notification messages to users who aren't friends with the LINE Official Account 

若一位並非 LINE 通知訊息發送方之 LINE 官方帳號好友的用戶收到 LINE 通知訊息，他可以選擇是否將該 LINE 官方帳號加入為好友。加入好友時會發送 [follow event](https://developers.line.biz/en/reference/messaging-api/#follow-event)。若封鎖則會發送 [unfollow event](https://developers.line.biz/en/reference/messaging-api/#unfollow-event)。使用 LINE 通知訊息時，您可能會從從未收過 follow event 的用戶那裡收到 unfollow event。

### Rich menu display when sending LINE notification messages to users who aren't friends with the LINE Official Account 

收到 LINE 通知訊息的用戶，無須將 LINE 官方帳號加入為好友，即可開啟一對一聊天並使用圖文選單。此時會顯示在 [LINE Official Account Manager](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-with-the-line-manager) 或透過 [Messaging API](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/#set-the-default-rich-menu) 所設定的預設圖文選單。但是，透過 Messaging API 為未將 LINE 官方帳號加入為好友的用戶所設定的[個別用戶圖文選單](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)則不會顯示。

![Users can access the rich menu without adding the LINE Official Account as a friend](https://developers.line.biz/media/line-notification-message/about-richmenu-displayed.png)

收到 LINE 通知訊息的用戶，也可以在未將 LINE 官方帳號加入為好友的情況下向其發送訊息。因此，您可能會透過 webhook 從非您 LINE 官方帳號好友的用戶那裡收到 [postback event](https://developers.line.biz/en/reference/messaging-api/#postback-event) 或 [message event](https://developers.line.biz/en/reference/messaging-api/#message-event)。

### What is billed for LINE notification messages usage fees 

只有**實際發送給用戶**的訊息，才會計入 LINE 通知訊息的使用費用。

您可以使用 API 查詢實際發送給用戶的訊息數量。如需更多資訊，請參閱 [Get the number of sent LINE notification messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#get-number-of-sent-line-notification-messages)。
