# Mark as read API（舊版）

<!-- tip start -->

**請使用新的端點來標示為已讀**

Mark as read API（舊版）仍可繼續使用。不過，若您今後要實作將使用者訊息標示為已讀的功能，請使用 Messaging API 的 [Mark messages as read](https://developers.line.biz/en/reference/messaging-api/#mark-as-read) 端點。「Mark messages as read」端點不需要任何申請，並且可以與聊天功能搭配使用。

<!-- tip end -->

<!-- note start -->

**使用選用功能需要提出申請**

只有已提交必要申請的企業用戶才能使用本文件所述的功能。若要在您的 LINE 官方帳號上使用這些功能，請聯絡您的業務負責人，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

我們將於 2026 年 10 月底停止受理 Mark as read API（舊版）的新申請。目前正在使用 Mark as read API（舊版）的 LINE 官方帳號，在停止受理新申請後仍可繼續使用。

<!-- note end -->

## Overview 

透過使用 Mark as read API（舊版），可以在特定使用者所傳送的所有訊息中顯示「已讀」。

## Disabling the automatic read setting function 

LINE 官方帳號預設會在收到使用者的訊息時自動顯示「已讀」（自動已讀設定功能）。然而，當使用 Mark as read API（舊版）時，此設定將會被停用。

因此，在使用 Mark as read API（舊版）的 LINE 官方帳號中，除非送出 Mark as read API（舊版）的請求，否則使用者的訊息不會顯示「已讀」。

<!-- note start -->

**顯示「已讀」的時機**

我們建議您在每次使用者傳送新訊息時，都送出一次 Mark as read API（舊版）請求。如果您在送出請求之前就先傳送訊息給使用者，該訊息在使用者的畫面上會看起來像是 LINE 官方帳號在未顯示「已讀」的情況下送出的。

<!-- note end -->

## Using with the chat function 

您可以透過 [LINE 官方帳號管理頁面（LINE Official Account Manager）](https://manager.line.biz/)或 LINE 官方帳號管理頁面 App 上的聊天功能，回覆使用者的訊息。

聊天功能與 Mark as read API（舊版）無法同時使用。請注意，一旦您開始使用 Mark as read API（舊版），就無法再使用聊天功能。

## Retrying a failed Mark as read API (old) request 

送出 Mark as read API（舊版）請求時，若發生狀態碼為 5xx 的錯誤，或請求逾時，請重試該請求。

請注意，如果在請求成功重試之前，您又收到了使用者的新訊息，則包含該新訊息在內的所有訊息都會顯示「已讀」。

## Reference 

關於 API 規格的詳細資訊，請參閱企業客戶選用功能 API 參考資料中的 [Mark as read API（舊版）](https://developers.line.biz/en/reference/partner-docs/#mark-as-read)。
