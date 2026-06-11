# 處理付款（Handling payments）

你可以透過將付款系統整合到你的 LINE MINI App 中，為使用者提供付款功能。

## Available payment system 

LINE MINI App 上可使用的付款系統會因國家或地區而有所不同。

| 付款方式 | 日本 | 台灣 | 泰國 |
| --- | :-: | :-: | :-: |
| [LINE Pay](https://developers.line.biz/en/docs/line-mini-app/develop/payment/#line-pay) | ❌ | ✅ | ✅ |
| [LINE MINI App 的應用程式內購買（In-app purchase）](https://developers.line.biz/en/docs/line-mini-app/develop/payment/#in-app-purchase) | ✅ | ❌ | ❌ |
| [其他方式](https://developers.line.biz/en/docs/line-mini-app/develop/payment/#other-payment-methods) | ✅ | ✅ | ✅ |

<!-- note start -->

**日本的 LINE Pay 服務已終止**

日本的 LINE Pay 服務已於 2025 年 4 月 30 日終止。台灣與泰國的 LINE Pay 服務仍持續提供。

<!-- note end -->

## LINE Pay 

### Preparing LINE Pay Merchant Account 

若要在 LINE MINI App 上使用 LINE Pay，你需要一個 LINE Pay 商家帳號（LINE Pay Merchant Account）。如果你還沒有，請至 [LINE Pay 的官方網站](https://pay.line.me/portal/global/main)申請。

### Developing a service that uses LINE Pay 

當你取得 LINE Pay 商家帳號後，請將 LINE Pay 整合到你的 LINE MINI App 中。有關 LINE Pay 的更多資訊，請參閱 LINE Pay Developers 中的 [Online payment 文件](https://developers-pay.line.me/online)。

使用 LINE Pay 時，付款流程如下：

1. 當使用者在你的 LINE MINI App 上發起一筆交易時，LINE Pay 上的付款流程隨即啟動。

   LINE MINI App 顯示的畫面：<br>![](https://developers.line.biz/media/line-mini-app/mini_linepay_flow01.png)

2. 使用者透過 LINE Pay 確認付款明細，並輸入 LINE Pay 的驗證資訊。

   LINE Pay 顯示的畫面：<br>![](https://developers.line.biz/media/line-mini-app/mini_linepay_flow02.png)

3. 顯示訂單確認頁面。

   LINE MINI App 顯示的畫面：<br>![](https://developers.line.biz/media/line-mini-app/mini_linepay_flow03.png)

### Testing LINE Pay 

若要測試你的付款流程實作，你可以使用 LINE Pay 提供的 [sandbox](https://developers-pay.line.me/sandbox)。

## In-app purchase for the LINE MINI App 

[應用程式內購買（In-app purchase）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)是一種讓使用者購買 LINE MINI App 中所提供之數位內容的系統。使用者在 LINE app 中啟動 LINE MINI App 以開始購買數位內容，付款則透過 App Store 或 Google Play 的付款系統處理。

目前，應用程式內購買僅在日本提供。有關資格與其他要求的更多資訊，請參閱[應用程式內購買概述（In-app purchase overview）](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)。

## Other payment methods 

若要在你的 LINE MINI App 中提供上述以外的其他付款方式，請比照一般網頁的做法來實作。但是，你必須將流程設計成：使用者在外部網域或 app 上完成交易後，會被重新導向回你的 LINE MINI App 頁面。
