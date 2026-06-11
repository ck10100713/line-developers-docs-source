# 接收 LINE 通知訊息（LINE notification message）時的流程

<!-- note start -->

**使用選用功能需要提出申請**

只有已提交必要申請的企業用戶，才能使用本文件所述的功能。若要在您的 LINE 官方帳號（LINE Official Account）使用這些功能，請聯絡您的業務負責人，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## User flow when receiving LINE notification messages 

除了同意接收 LINE 通知訊息之外，用戶還必須每 180 天透過 SMS 驗證一次自己的電話號碼（SMS 驗證），才能接收 LINE 通知訊息。

![接收 LINE 通知訊息時的用戶流程](https://developers.line.biz/media/line-notification-message/pnp-receive-flow-en.png)

- [用戶已同意接收 LINE 通知訊息且不需要 SMS 驗證時的流程](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#receiving-line-notification-messages)
- [LINE 通知訊息接收設定為「未設定」且不需要 SMS 驗證時的流程](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-1)
- [LINE 通知訊息接收設定為「未設定」且需要 SMS 驗證時的流程](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-2)
- [用戶已同意接收 LINE 通知訊息且需要 SMS 驗證時的流程](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#user-consent-flow-for-receiving-line-notification-messages-3)
- [備註：變更 LINE 帳號所註冊電話號碼的流程](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/flow-when-receiving-message/#when-changing-your-phone-number)

<!-- note start -->

**接收 LINE 通知訊息的設定為全體適用**

一旦用戶同意接收 LINE 通知訊息，便視為同意接收來自所有 LINE 官方帳號的 LINE 通知訊息。

例如，某位用戶在收到由 LINE 官方帳號 A 發送的 LINE 通知訊息後同意接收，當該用戶又收到由另一個 LINE 官方帳號 B 發送的 LINE 通知訊息時，由於該用戶已同意接收 LINE 通知訊息，因此不需要再次表示同意。

<!-- note end -->

<!-- note start -->

**每個用戶的 LINE 帳號必須每 180 天進行一次 SMS 驗證**

用戶一旦完成 SMS 驗證，在 180 天內接收來自所有 LINE 官方帳號的 LINE 通知訊息時，皆不需要再進行 SMS 驗證。

例如，某位用戶在收到由 LINE 官方帳號 A 發送的 LINE 通知訊息後進行了 SMS 驗證，若在 180 天內又收到由另一個 LINE 官方帳號 B 發送的 LINE 通知訊息，由於該用戶已完成 SMS 驗證，因此不需要再次進行 SMS 驗證。

<!-- note end -->

<!-- note start -->

**不需要 SMS 驗證的情況**

在以下情況下接收 LINE 通知訊息時，不需要 SMS 驗證：

- 建立新 LINE 帳號後的 180 天內
- 變更用戶 LINE 帳號所註冊電話號碼後的 180 天內。

<!-- note end -->

### Flow for the case where a user has already agreed to receive LINE notification messages and doesn't need SMS authentication 

| Number | Image | Description |
| --- | --- | --- |
| 1 | ![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-3-ja.png)<br><br>![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-4-ja.png) | 若用戶已同意接收 LINE 通知訊息且不需要 SMS 驗證，「LINE」系統帳號會向用戶發送「已收到 LINE 通知訊息」的訊息。同時，所請求的 LINE 通知訊息也會發送給用戶。 |

### Flow for the case where the LINE notification message reception settings are "not set" and SMS authentication isn't needed 

| Number | Image | Description |
| --- | --- | --- |
| 1 | ![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-1-ja.png) | 若 LINE 通知訊息的[接收設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#user-consent-state)為「未設定」且不需要 SMS 驗證，當用戶收到 LINE 通知訊息時，用戶會收到來自「LINE」系統帳號的「您已收到 LINE 通知訊息」和「設定以接收 LINE 通知訊息」的訊息。 |
| 2 | ![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-2-ja.png) | 點擊「設定以接收 LINE 通知訊息」下方的「設定」按鈕，會將用戶帶往同意接收 LINE 通知訊息的畫面。 |
| 3 | ![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-3-ja.png)<br><br>![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-4-ja.png) | 若用戶同意「設定以接收 LINE 通知訊息」，用戶會收到來自「LINE」系統帳號表示您已收到 LINE 通知訊息的訊息。接著，所請求的 LINE 通知訊息便會發送給用戶。 |

### Flow for the case where the LINE notification message reception settings are "not set" and SMS authentication is needed 

| Number | Image | Description |
| --- | --- | --- |
| 1 | ![](https://developers.line.biz/media/line-notification-message/type3-pnpflow-1-ja.png) | 若 LINE 通知訊息的[接收設定](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/technical-specs/#user-consent-state)為「未設定」且需要 SMS 驗證，當用戶收到 LINE 通知訊息時，「LINE」系統帳號會向用戶發送「您已收到 LINE 通知訊息」和「設定以接收 LINE 通知訊息」的訊息。 |
| 2 | ![](https://developers.line.biz/media/line-notification-message/type3-pnpflow-2-ja.png) | 點擊「設定以接收 LINE 通知訊息」下方的「設定」按鈕，會將用戶帶往同意接收 LINE 通知訊息的畫面。 |
| 3 | ![](https://developers.line.biz/media/line-notification-message/type3-pnpflow-3-ja.png) | 若用戶同意「設定以接收 LINE 通知訊息」，會顯示一個確認對話框，詢問是否向 LINE 帳號所註冊的電話號碼發送 SMS 訊息。請注意，若用戶在此對話框中點擊 **Change** 來變更發送 SMS 的電話號碼（即 LINE 帳號所註冊的電話號碼），則發送至舊電話號碼的 LINE 通知訊息將不會送達該用戶。 |
| 4 | ![](https://developers.line.biz/media/line-notification-message/type3-pnpflow-4-ja.png) | 系統會向指定的電話號碼發送一則 SMS 訊息。請輸入訊息中提供的 PIN 碼。 |
| 5 | ![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-3-ja.png)<br><br>![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-4-ja.png) | SMS 驗證完成後，「LINE」系統帳號會向用戶發送「已收到 LINE 通知訊息」的訊息。同時，所請求的 LINE 通知訊息也會發送給用戶。 |

### Flow for the case where a user has already agreed to receive LINE notification messages and SMS authentication is needed 

| Number | Image | Description |
| --- | --- | --- |
| 1 | ![](https://developers.line.biz/media/line-notification-message/type2-pnpflow-1-ja.png) | 若用戶已同意接收 LINE 通知訊息且需要 SMS 驗證，當用戶收到 LINE 通知訊息時，「LINE」系統帳號會向用戶發送「已收到 LINE 通知訊息」的訊息和「電話號碼驗證」的訊息。 |
| 2 | ![](https://developers.line.biz/media/line-notification-message/type2-pnpflow-2-ja.png) | 點擊「電話號碼驗證」訊息中的「設定」，會將用戶帶往電話號碼驗證畫面。 |
| 3 | ![](https://developers.line.biz/media/line-notification-message/type2-pnpflow-3-ja.png) | 按下「發送 SMS」按鈕後，會顯示一個確認對話框，詢問是否向 LINE 帳號所註冊的電話號碼發送 SMS 訊息。請注意，若用戶在此對話框中點擊 **Change** 來變更發送 SMS 的電話號碼（即 LINE 帳號所註冊的電話號碼），則發送至舊電話號碼的 LINE 通知訊息將不會送達該用戶。 |
| 4 | ![](https://developers.line.biz/media/line-notification-message/type2-pnpflow-4-ja.png) | 系統會向指定的電話號碼發送一則 SMS 訊息。請輸入訊息中提供的 PIN 碼。 |
| 5 | ![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-3-ja.png)<br><br>![](https://developers.line.biz/media/line-notification-message/type1-pnpflow-4-ja.png) | SMS 驗證完成後，「LINE」系統帳號會向用戶發送「已收到 LINE 通知訊息」的訊息。同時，所請求的 LINE 通知訊息也會發送給用戶。 |

## Note: Flow for changing the phone number registered to the LINE account 

若要變更 LINE 帳號所註冊的電話號碼，用戶須在接收 LINE 通知訊息進行 SMS 驗證時點擊 **Change**、點擊 **Next**，然後輸入電話號碼。

<!-- tip start -->

**變更 LINE 帳號所註冊的電話號碼**

您也可以在 LINE App 中前往 **設定** > **個人檔案** > **電話號碼** 來變更電話號碼。詳情請參閱 LINE 幫助中心的[查看／變更您的電話號碼](https://help.line.me/line/smartphone/pc?lang=en&contentId=20000120)。

<!-- tip end -->

| Number | Image | Description |
| --- | --- | --- |
| 1 | ![](https://developers.line.biz/media/line-notification-message/change-phone-number-1-en.png) | 輸入您想變更的電話號碼，然後點擊「Next」。 |
| 2 | ![](https://developers.line.biz/media/line-notification-message/change-phone-number-2-en.png) | 系統會向指定的電話號碼發送一則 SMS 訊息。請輸入訊息中提供的 PIN 碼。 |
| 3 | ![](https://developers.line.biz/media/line-notification-message/change-phone-number-3-ja.png) | 透過 SMS 成功驗證電話號碼後，您會收到來自您 LINE 帳號的「您的電話號碼已變更」訊息。 |

<style scoped>
.table-user-content-flow td:nth-child(2) {
    min-width: 160px;
}
.table-user-content-flow td:nth-child(3) {
    min-width: 200px;
}
</style>
