# 設定 module 頻道設定（Configure module channel settings）

<!-- note start -->

**使用選用功能需先完成相關手續**

本文件所說明的功能僅供已提出規定申請的企業客戶使用。若您想使用 module 發布擴充功能，請聯絡業務負責人，或透過 [LINE Marketplace Inquiry](https://line-marketplace.com/jp/inquiry) 與我們聯繫（僅提供日文）。

<!-- note end -->

在 module 頻道中，[LINE Developers Console](https://developers.line.biz/console/) 會出現一個專屬的 **module** 分頁。

在 **module** 分頁中，您可以設定 module 頻道的 webhook URL、是否接收 webhook，以及[向 LINE 官方帳號管理員請求授權](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin)時所指定的 `redirect_uri`。

![Module tab in LINE Developers Console](https://developers.line.biz/media/partner-docs/module-technical/module-tab-in-console-en.png)

## 1. module tab 

**module** 分頁是 module 頻道專屬的設定項目。

## 2. Webhook settings 

### Webhook URL 

您可以為 module 頻道設定一組 webhook URL。另請參閱[接收 webhook](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-webhook)。

### Using webhook 

您可以設定 module 頻道是否接收 webhook 事件。

### Resend webhook 

您可以設定當 module 頻道的 webhook URL 取得 webhook 事件失敗時，是否要由 LINE Platform 重新傳送該 webhook 事件。

### Error stats 

您可以設定是否在 **Webhook errors** 分頁中顯示 webhook 事件接收失敗的統計資料。

## 3. Redirect settings 

### Redirect URL 

redirect URL 請指定[向 LINE 官方帳號管理員請求授權](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin)時所使用的 `redirect_uri` 參數的值。redirect URL 的 scheme 必須為 `https`。

單一頻道可以指定多組 redirect URL。
