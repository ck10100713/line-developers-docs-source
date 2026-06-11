# 給企業客戶的通知（Notice for corporate customers）

給企業客戶的通知。另請參閱 [News](https://developers.line.biz/en/news/)。

2026/05/18

## We'll stop accepting new applications for the Mark as read API (old) at the end of October 2026 

我們將於 2026 年 10 月底停止受理 [Mark as read API (old)](https://developers.line.biz/en/docs/partner-docs/mark-as-read/) 的新申請。目前正在使用 Mark as read API (old) 的 LINE 官方帳號，在停止受理新申請後仍可繼續使用。

我們正在考慮廢止 Mark as read API (old)。如果您提供的系統整合了 Mark as read API (old)，請考慮改用 Messaging API 的 [Mark messages as read](https://developers.line.biz/en/reference/messaging-api/#mark-as-read) 端點（endpoint）。「Mark messages as read」端點無須申請，且可與聊天功能搭配使用。

2026/02/19

## Changes to some error responses in the Mission Sticker API 

為避免推斷出使用者屬性資訊，我們已修改 Mission Sticker API [Provide mission stickers to the users](https://developers.line.biz/en/reference/partner-docs/#send-mission-stickers-v3) 端點中部分錯誤回應的內容。

詳情請參閱 provide mission stickers to the users 端點的 [Error messages](https://developers.line.biz/en/reference/partner-docs/#send-mission-stickers-v3-error-messages) 章節。

2025/06/30

## The subject and body of the emails sent for error notifications have changed 

自 2025 年 6 月 30 日起，我們更新了 Webhook 錯誤通知所寄送之電子郵件的主旨與內文。

詳情請參閱 [Notification email example](https://developers.line.biz/en/docs/partner-docs/error-notification/#sample-mail)。

2025/06/18

## LINE notification messages are now displayed as “Important notification” 

為了與其他訊息區別，LINE notification messages 現在會在 LINE 官方帳號圖示右側顯示「Important notification」。

![LINE notification messages 會在圖示右側顯示「Important notification」](https://developers.line.biz/media/line-notification-message/notification-messages-important-en.jpg)

詳情請參閱 LINE notification messages 文件中的 [Difference in appearance from other messages](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/overview/#difference-from-other-messages)。

2025/06/18

## We've changed the endpoint name of the Mission Sticker API 

為了提高清晰度，我們已重新命名 Mission Sticker API 的「Send mission stickers (v3)」端點。其功能沒有任何變更。

| 變更前名稱                 | 變更後名稱（現行）                    |
| -------------------------- | ------------------------------------- |
| Send mission stickers (v3) | Provide mission stickers to the users |

詳情請參閱企業客戶選用功能 API 參考文件中的 [Mission Sticker API](https://developers.line.biz/en/reference/partner-docs/#mission-stickers)。

2025/06/02

## LINE notification messages (template) now available 

新增了一項名為「[LINE notification messages (template)](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/template/)」的功能，讓您可以透過組合預先製作的範本、項目等，輕鬆建立訊息。

因此，先前需要進行 UX 審查的「LINE notification messages」已更名為「LINE notification messages (flexible)」。

詳情請參閱 [LINE notification messages overview](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/overview/)。

2025/01/28

## Source property in the webhook event of LINE notification messages has been removed 

如同 [2024 年 8 月 9 日](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20240809) 公告所述，自 2025 年 1 月 28 日起，LINE notification messages 的 [Webhook delivery completion event](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event) 中的 `source` 屬性已被移除。

在此之前，當您請求 LINE notification messages API，且 LINE notification message 完成傳送給使用者時，LINE Platform 會將下列 Webhook 事件傳送至 bot 伺服器：

```json
{
  "destination": "Uc7472b39e21dab71c2347e02714630d6",
  "events": [
    {
      "type": "delivery",
      "delivery": {
        "data": "68df277462529930889fab80ecffdc0883906320591df93c25efc08300410fc2"
      },
      "webhookEventId": "01G17DAF0QJ7A3ERC5EJ9MAMH8",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1650590038721,
      // The following source property has been removed
      "source": {
        "type": "user",
        "userId": "U8189cf6745fc0d808977bdb0b9f22995"
      },
      "mode": "active"
    }
  ]
}
```

上述 Webhook 事件中的 `source` 屬性自 2025 年 1 月 28 日起已被移除。

我們將持續努力為客戶提供更好的服務。感謝您的理解。

2024/10/18

## Add Quick-fill docs 

Quick-fill 是一項功能，透過點按 LINE MINI App 上的 **Auto-fill** 按鈕，自動填入所需的個人資料資訊。您可以在 LINE MINI App 中輕鬆使用使用者在 Account Center 中設定的 Common Profile 資訊。

![](https://developers.line.biz/media/line-mini-app/quick-fill/quick-fill-3-steps.png)

藉由將 Quick-fill 整合至您的 LINE MINI App，使用者只要點按一次，就能自動輸入地址或電話號碼。例如在餐廳訂位或在網路商店下單時，使用者可省去手動輸入資訊的麻煩。

只有經我們聯繫的特定企業客戶才能使用 Quick-fill 功能。

如需瞭解如何將 Quick-fill 整合至您的 LINE MINI App，請參閱 [Overview of Quick-fill](https://developers.line.biz/en/docs/partner-docs/quick-fill/overview/)。

2024/08/09

## As of January 28, 2025, source property in the webhook event of LINE notification messages will be removed 

自 2025 年 1 月 28 日起，LINE notification messages 的 [Webhook delivery completion event](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/#receive-delivery-event) 中的 `source` 屬性將被移除。

當您請求 LINE notification messages API，且 LINE notification message 完成傳送給使用者時，LINE Platform 會將下列 Webhook 事件傳送至 bot 伺服器：

```json
{
  "destination": "Uc7472b39e21dab71c2347e02714630d6",
  "events": [
    {
      "type": "delivery",
      "delivery": {
        "data": "68df277462529930889fab80ecffdc0883906320591df93c25efc08300410fc2"
      },
      "webhookEventId": "01G17DAF0QJ7A3ERC5EJ9MAMH8",
      "deliveryContext": {
        "isRedelivery": false
      },
      "timestamp": 1650590038721,
      // The following source property will be removed
      "source": {
        "type": "user",
        "userId": "U8189cf6745fc0d808977bdb0b9f22995"
      },
      "mode": "active"
    }
  ]
}
```

上述 Webhook 事件中的 `source` 屬性自 2025 年 1 月 28 日起將被移除。屬性移除的日期與時間可能會在未事先通知的情況下變更。

我們將持續努力為客戶提供更好的服務。感謝您的理解。

2024/05/07

## Module maintenance notice 

module 預計於 2024 年 6 月 5 日約 2:00 至約 3:00（UTC+9）進行維護。詳情請參閱 2024 年 5 月 7 日的消息 [Maintenance notice for Messaging API, module, and LINE Developers Console](https://developers.line.biz/en/news/2024/05/07/maintenance-notice/)。

2024/04/26

## Notification email is now be sent when webhook redelivery stopped 

在 Messaging API 的 [error notification](https://developers.line.biz/en/docs/partner-docs/error-notification/) 功能中，現在會在 Webhook 重新傳送停止時寄送通知電子郵件。

如果您在 Messaging API 頻道（channel）設定中 [啟用了 Webhook 重新傳送](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#enable-webhook-redelivery)，LINE Platform 會重新傳送您的 bot 伺服器未能接收的 Webhook。然而，如果重新傳送一段時間後您的伺服器仍無回應，LINE Platform 將會停止重新傳送。

先前在偵測到錯誤時，LINE Platform 只會寄送一次錯誤通知電子郵件。經此變更後，將會在 Webhook 重新傳送開始與停止時都寄送通知電子郵件。

詳情請參閱 [When the LINE Platform stopped webhook redelivery](https://developers.line.biz/en/docs/partner-docs/error-notification/#webhook-redelivery-stopped)。

2023/11/01

## As of October 31, 2023, the audience match API has been discontinued 

如同 [2023 年 7 月 18 日](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20230718) 公告所述，我們已自 2023 年 10 月 31 日起停止提供 audience match API。

LY Corporation 將持續為客戶提升服務品質。感謝您的理解。

2023/08/31

## Stateless channel access token released 

無狀態（stateless）頻道權杖是僅在 15 分鐘內有效的頻道權杖。可發行的無狀態頻道存取權杖（channel access token）數量沒有上限。無狀態頻道存取權杖可用於例如使用 Messaging API 頻道或 module 頻道等情境。

如需瞭解無狀態頻道存取權杖的更多資訊，請參閱 2023 年 8 月 31 日的消息 [Stateless channel access token released](https://developers.line.biz/en/news/2023/08/31/stateless-channel-access-token/)。

2023/07/18

## As of October 31, 2023, the feature for sending messages using phone number will be discontinued 

自 2023 年 10 月 31 日起，audience match API 中使用電話號碼傳送訊息的功能將不再提供。audience match API 也將停止提供。

相關文件與 API 參考資料將在停止提供後於未事先通知的情況下刪除。

### Target endpoints 

隨著停止提供，下列端點也將逐步停止提供：

- [Send a message using phone number](https://developers.line.biz/en/reference/partner-docs/#phone-audience-match)
- [Get result of message delivery using phone number](https://developers.line.biz/en/reference/partner-docs/#get-phone-audience-match)

### Scheduled date of discontinuation 

2023 年 10 月 31 日

此日期可能在未事先通知的情況下變更。

LINE 將持續為客戶提升服務品質。感謝您的理解。

2023/05/31

## The Send mission stickers (v2) endpoint has been discontinued 

如同 [2023 年 2 月 2 日](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20230202) 公告所述，我們已自 2023 年 5 月 31 日起停止提供 Send mission stickers (v2) 端點。今後請使用 [Send mission stickers (v3)](https://developers.line.biz/en/reference/partner-docs/#send-mission-stickers-v3) 端點。

2023/04/11

## Module maintenance notice 

module 預計於 2023 年 5 月 11 日約 2:00 至約 3:00（UTC+9）進行維護。詳情請參閱 2023 年 4 月 11 日的消息 [Maintenance notice for Messaging API, module, and LINE Developers Console](https://developers.line.biz/en/news/2023/04/11/messaging-api-module-and-console-maintenance/)。

2023/02/20

## We've changed the name of the Mark-as-Read API to "Mark as read API" 

我們已將 Mark-as-Read API 的名稱變更為「Mark as read API」。功能沒有任何變更。

| 語言     | 變更前名稱         | 變更後名稱        |
| -------- | ------------------ | ----------------- |
| 日文     | Mark-as-Read API   | 既読API           |
| 英文     | Mark-as-Read API   | Mark as read API  |

如需瞭解 Mark as read API 的更多資訊，請參閱 [Mark as read API](https://developers.line.biz/en/docs/partner-docs/mark-as-read/)。

2023/02/02

## The Send mission stickers (v2) endpoint will be discontinued on May 31, 2023 

我們將於 2023 年 5 月 31 日停止提供 Send mission stickers (v2) 端點。停止提供後，請使用 [Send mission stickers (v3)](https://developers.line.biz/en/reference/partner-docs/#send-mission-stickers-v3) 端點。

相關文件與 API 參考資料將在停止提供後於未事先通知的情況下刪除。

2022/12/20

## Notification of changes to how the Module reference is provided 

先前以 PDF 檔案形式提供的 Module 參考資料，現在將以 LINE Developers 網站上的文件形式提供。今後請參閱 Module 的[文件](https://developers.line.biz/en/docs/partner-docs/#module)與 [API 參考資料](https://developers.line.biz/en/reference/partner-docs/#module)。

2022/09/28

## Information on "Feature for getting statistics per aggregation unit" 

「[Feature for getting statistics per aggregation unit](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/)」已整合至 Messaging API。

詳情請參閱 2022 年 9 月 28 日的消息 ["Feature for getting statistics per aggregation unit" is now available in the Messaging API](https://developers.line.biz/en/news/2022/09/28/messaging-api-updated/)。

2022/08/23

## LINE API Policy Handbook released 

LINE API Policy Handbook 現已提供。本手冊是與 [LINE Official Account Terms of Use](https://terms2.line.me/official_account_terms_jp?country=JP&lang=en) 及 [LINE Official Account API Terms of Use](https://terms2.line.me/official_account_api_terms_jp?lang=ja&country=JP)（僅提供日文版）相關的文件，旨在協助您更深入理解並正確使用 LINE API。

詳情請參閱 [LINE API Policy Handbook](https://developers.line.biz/en/docs/partner-docs/api-policy-handbook/)。

2022/06/28

## The documentation for the LINE notification messages released 

LINE notification messages 是一項服務，讓您即使不知道使用者的 [User IDs](https://developers.line.biz/en/glossary/#user-id)，也能透過指定電話號碼向使用者傳送訊息。即使使用者尚未將您的 LINE 官方帳號加為好友，您仍可從您的 LINE 官方帳號向該使用者傳送訊息。

除了先前發布的 LINE notification messages 概觀之外，現在也已發布諸如 [Technical specifications of the LINE notification messages API](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/)（僅提供日文版）及 [LINE notification messages API Reference](https://developers.line.biz/en/reference/line-notification-messages/)（僅提供日文版）等文件。

如需瞭解 LINE notification messages 的更多資訊，請參閱 [LINE notification messages overview](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/overview/)。

2022/03/24

## The documentation for the module released 

透過使用 module，未使用 Messaging API 頻道的 LINE 官方帳號也能輕鬆新增使用 Messaging API 的進階功能。此 module 的文件現已提供。如需瞭解 module 的更多資訊，請參閱 [Module](https://developers.line.biz/en/docs/partner-docs/module/)。

2022/01/05

## Sending messages using IFA discontinued 

如同 [2021 年 12 月 1 日](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20211201) 公告所述，audience match API 中使用 IFA（Identifier for Advertisers，廣告識別碼）傳送訊息的功能預計於 2021 年 12 月底停止提供。

LINE 將持續為客戶提升服務品質。感謝您的理解。

2021/12/06

## Notification of changes to how the LINE Bot Development Guidelines are provided 

先前以 PDF 檔案形式提供的 LINE Bot Development Guidelines，現在將以 LINE Developers 網站上的文件形式提供。此外，本指南的名稱已變更為 [Development guidelines for corporate customers](https://developers.line.biz/en/docs/partner-docs/development-guidelines/)。今後請參閱此文件。

2021/12/01

## Sending messages using IFA discontinued 

自 2021 年 12 月 31 日起，audience match API 中使用 IFA（Identifier for Advertisers，廣告識別碼）傳送訊息的功能將不再提供。

相關文件與 API 參考資料將在停止提供後於未事先通知的情況下刪除。

### Target endpoints 

隨著停止提供，下列端點也將逐步停止提供：

- Send a message using mobile advertising ID
- Get message delivery result using mobile advertising ID

### Scheduled date of discontinuation 

2021 年 12 月 31 日

此日期可能在未事先通知的情況下變更。

LINE 將持續為客戶提升服務品質。感謝您的理解。

2021/07/09

## Corrections to the "Get statistics per aggregation unit" document 

在「[Get statistics per aggregation unit](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/)」的 API 參考資料中，request body 的說明有誤。我們已更正該錯誤，但對於此錯誤造成的任何不便，謹致歉意。

更正前後的差異請參閱下表：

- **傳送訊息時為任一彙總單位指派單位名稱**

  | 項目                                             | 錯誤      | 正確    |
  | ------------------------------------------------ | --------- | ------- |
  | `customAggregationUnits` 的字元數上限            | 100       | 30      |

請注意，如果您在傳送訊息時指定的彙總單位名稱超過字元數上限，請求不會失敗，但該單位名稱將不會被指派到目標訊息。

2021/04/28

## The subject of the email sent upon error notification will be changed 

<!-- note start -->

**2021 年 5 月 25 日更新**

我們更新了 [Changes](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20210428-01) 與 [Estimated date of change](https://developers.line.biz/en/docs/partner-docs/notice/#partner-news-20210428-02)。

<!-- note end -->

這些變更是針對作為 Messaging API 功能提供的 [error notification](https://developers.line.biz/en/docs/partner-docs/error-notification/) 所規劃。

### Changes 

[Notification email](https://developers.line.biz/en/docs/partner-docs/error-notification/#mail) 的主旨將變更如下。我們也會變更郵件內文的部分文字，使其更易於理解。

| 項目 | 變更前 | 變更後 |
| --- | --- | --- |
| **主旨** | Messaging API: Webhook transmission failed - `<Channel name>` | Messaging API: Your server did not return \[200 OK\] - `<Channel name>` |

`<Channel name>` 部分會顯示目標頻道的頻道名稱。

### Estimated date of change 

2021 年 5 月 25 日

詳情請參閱企業客戶選用功能文件中的 [Error notification](https://developers.line.biz/en/docs/partner-docs/error-notification/)。

2021/03/10

## We've released a feature for getting statistics per aggregation unit 

您現在可以取得多則推播訊息（push message）與多元發送訊息（multicast message）的各彙總單位統計資料。您可以在傳送訊息前指派單位名稱，以便日後查看各單位的統計資料。

<!-- tip start -->

**各彙總單位統計資料功能在什麼時候有用？**

當您向多位使用者傳送 narrowcast 或 broadcast 訊息時，可以指定一個 request ID 來[取得該特定訊息的使用者互動統計資料](https://developers.line.biz/en/reference/messaging-api/#get-message-event)。

![使用者互動統計資料](https://developers.line.biz/media/news/old_statistics_en.png)

當您向少於 20 位使用者傳送訊息時，由於必須保護使用者隱私，您將無法取得統計資料。然而，藉由全新發布的 [Get statistics per aggregation unit](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/) 功能，即使您向少數使用者傳送訊息，只要在傳送訊息前指派單位名稱，就能取得多則訊息的各單位統計資料。

![彙總各單位統計資料](https://developers.line.biz/media/news/new_statistics_en.png)

<!-- tip end -->

詳情請參閱企業客戶選用功能文件中的 [Get statistics per aggregation unit](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/)。

2020/03/17

## Information on Icon/Nickname Switch 

Icon/Nickname Switch 已整合至 Messaging API。

詳情請參閱「[You can now change the icon and display name of your LINE Official Account (2020/3/17)](https://developers.line.biz/en/news/2020/03/17/icon-nickname-switch/)」。
