# LINE 通知訊息總覽（LINE notification messages overview）

<!-- note start -->

**使用選用功能需要提出申請**

只有已提交所需申請的企業用戶才能使用本文件所述的功能。若要在您的 LINE 官方帳號（LINE Official Account）上使用這些功能，請聯絡您的業務窗口，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## Overview 

LINE 通知訊息（LINE notification messages）是一項可讓您透過指定用戶的電話號碼來向其發送訊息的服務。即使用戶尚未將您的 LINE 官方帳號加為好友，您也可以從您的 LINE 官方帳號向他們發送訊息。

LINE 通知訊息僅能用於日本、泰國及台灣的 LINE 官方帳號。

LINE 通知訊息有兩種類型：[LINE notification messages (template)](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/) 可讓您透過組合預先製作的範本與項目來輕鬆建立訊息；[LINE notification messages (flexible)](https://developers.line.biz/en/reference/line-notification-messages/#flexible) 則需要事先通過 UX 審查。每種類型都有不同的 API 端點（endpoint）。

以下是 LINE 通知訊息（template）的範例：

![Sample of LINE notification messages (template)](https://developers.line.biz/media/line-notification-message/line-notification-messages-sample-ja.png)

如需更多資訊，請參閱 [Technical specifications of the LINE notification messages API](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/) 以及 [LINE notification messages API reference](https://developers.line.biz/en/reference/line-notification-messages/)。

<!-- tip start -->

**LINE 通知訊息的使用目的**

LINE 通知訊息的使用目的僅限於我們認為對用戶有用且適當的用途，不得用於商業或廣告目的。如需更多資訊，請參閱 LINE for Business 中的 [LINE notification messages (template) UX guidelines](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE_Official_Notification_Template_UXGuideline.pdf)（僅提供日文版）與 [LINE notification messages (flexible) UX guidelines](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%E9%80%9A%E7%9F%A5%E3%83%A1%E3%83%83%E3%82%BB%E3%83%BC%E3%82%B8UX%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3.pdf)（僅提供日文版）。

<!-- tip end -->

## Difference in appearance from other messages 

LINE 通知訊息會在 LINE 官方帳號圖示的右側顯示「Important notification（重要通知）」，以與其他訊息區隔。此功能適用於 iOS、Android 及 iPad 的 LINE 15.9.0 或更新版本。

![LINE notification messages are displayed with “Important notification” to the right of the icon](https://developers.line.biz/media/line-notification-message/notification-messages-important-en.jpg)

顯示的文字可能會因接收 LINE 通知訊息的 LINE app 語言設定而有所不同。

| LINE app language settings       | Text displayed           |
| -------------------------------- | ------------------------ |
| Japanese                         | `重要なお知らせ`         |
| Thai                             | `การแจ้งเตือนสำคัญ`      |
| Chinese (Simplified/Traditional) | `重要通知`               |
| Other                            | `Important notification` |

如需更多關於 LINE app 語言設定的資訊，請參閱說明中心的 [Changing the LINE app language setting](https://help.line.me/line/?contentId=20007465&lang=en)。

## Related pages 

- [Technical specifications of the LINE notification messages API](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/)
- [LINE notification messages API reference](https://developers.line.biz/en/reference/line-notification-messages/)
- [Webhook delivery completion event](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/)
- [Flow when receiving a LINE notification message](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/)
