# Module（模組）

<!-- note start -->

**使用選用功能須先完成相關手續**

本文件所說明的功能僅提供給已完成規定申請手續的企業客戶使用。若您想使用 module（模組）發布擴充功能，請聯絡業務負責窗口，或透過 [LINE Marketplace Inquiry](https://line-marketplace.com/jp/inquiry)（僅提供日文）與我們聯繫。

<!-- note end -->

## Overview 

module（模組）是一種機制，讓您可以透過連結（attach，附加）至您的 LINE 官方帳號（LINE Official Account），為其新增使用 Messaging API 的各項功能。module 以一種頻道（channel）的形式提供，稱為 [module channel（模組頻道）](https://developers.line.biz/en/docs/line-developers-console/overview/#channel)。即使您的 LINE 官方帳號尚未建立 Messaging API 頻道，您仍可從 module channel 呼叫 Messaging API，向使用者發送訊息並設定圖文選單（rich menu）。

![module channel](https://developers.line.biz/media/partner-docs/module/module-channel-en.png)

### Relationship between module channel and LINE Official Account 

一般情況下，一個 LINE 官方帳號只能建立（開設）一個 Messaging API 頻道。而 module channel 則可以連結至多個 LINE 官方帳號。

![Attach same service](https://developers.line.biz/media/partner-docs/module-technical/attach-same-service-en.png)

- OA "X"、OA "Y"、OA "Z"：LINE 官方帳號
- Module CH：module channel
- System：Module CH 的 webhook 發送目的地與 bot 伺服器

<!-- tip start -->

**關於 module channel 所使用的伺服器**

在 module channel 中，與 LINE Platform 系統通訊的伺服器由負責開發 module channel 的公司自行準備。設定為 webhook 發送目的地的伺服器，與呼叫 Messaging API 等的伺服器，不一定要是同一台。

<!-- tip end -->

### Module usage example 

舉例來說，假設您有一個 LINE 官方帳號，使用 LINE 官方帳號管理介面（LINE Official Account Manager）的聊天功能與使用者溝通。如果將一個「具備門市預約功能的 module channel」連結至此 LINE 官方帳號，您就可以在 LINE 官方帳號管理介面上與使用者聊天，並透過 module 將門市預約流程自動化。

<!-- tip start -->

**module channel 的 webhook 為啟用狀態**

如果您在 LINE 官方帳號的回應設定中[停用 webhook](https://developers.line.biz/en/reference/messaging-api/#get-webhook-endpoint-information)，webhook 事件就不會發送至 Messaging API 頻道。但在此設定下，webhook 事件仍會發送至 module channel。

module channel 可以根據所取得的 webhook 事件內容，實作為向使用者發送訊息。

<!-- tip end -->

![Sample](https://developers.line.biz/media/partner-docs/module/module-sample.png)

| Number | Description |
| --- | --- |
| 1 | 使用者發送訊息 |
| 2 | 操作人員使用 LINE 官方帳號管理介面的聊天功能向使用者發送訊息 |
| 3 | 使用者按下圖文選單，執行具備預約功能的 module |
| 4 | 預約功能的 bot 進行回應，預約流程開始 |

## Reference 

如需 module 所提供的 REST API 等技術規格的詳細資訊，請參閱企業客戶選用功能 API 參考文件中的 [Module](https://developers.line.biz/en/reference/partner-docs/#module)。

## Prepare the necessary systems and mechanisms 

<!-- note start -->

**注意**

目前，module 僅能作為付費擴充功能在 [LINE Marketplace](https://line-marketplace.com/)（僅提供日文）上發布。

<!-- note end -->

LY Corporation 在 module 中所提供的功能如下。

| Function name | Description |
| --- | --- |
| 將 module channel 連結至 LINE 官方帳號的機制 | 提供 OAuth 2.0 授權機制，以及使用 REST API 將 module channel 連結至 LINE 官方帳號的機制。詳情請參閱 [Attach module channels using the OAuth 2.0 authorization mechanism](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#attach-module-channels-using-oauth-2-0-auth-mechanism)。 |
| 將 LINE 官方帳號與 module channel 解除連結的 API | 提供可將 LINE 官方帳號與 module channel 解除連結的 REST API。詳情請參閱企業客戶選用功能 API 參考文件中的 [Unlink (detach) the module channel by the operation of the module channel administrator](https://developers.line.biz/en/reference/partner-docs/#unlink-detach-module-channel-by-operation-mc-admin)。 |
| 控制聊天主導權的 API | module channel 具有一個稱為聊天主導權（chat initiative，Chat Control）的概念。具有主導權的頻道可以向使用者、群組或聊天室發送[回覆訊息（reply message）](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)。<br>一般而言，在 LINE Marketplace 上提供的 module channel 不需要控制主導權，但為了因應因非預期事件而導致聊天主導權變更的情況，我們提供了控制聊天主導權的 REST API。<br>詳情請參閱 [Control chat initiative (Chat Control)](https://developers.line.biz/en/docs/partner-docs/module-technical-chat-control/)。 |
| 從 module channel 使用 Messaging API 的機制 | 從 module channel 呼叫 Messaging API 時，您需要指定一個 module 專用的特殊請求標頭（request header）。詳情請參閱 [Using the Messaging API from a module channel](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/)。 |
| module channel 專用的 webhook 事件 | module channel 提供專用的 webhook 事件。詳情請參閱 [Receive module channel-specific webhook events](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-module-channel-specific-webhook-events)。 |
| 取得連結至 module channel 的 LINE 官方帳號資訊的 API | 提供可取得連結至 module channel 的 LINE 官方帳號資訊的 REST API。詳情請參閱 [Get the LINE Official Account information from the module channel](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-line-oa-info-from-module-channel)。 |

除上述項目外，在 LINE Marketplace 上發布擴充功能所需的所有其他系統（伺服器等）與機制，皆須由客戶自行提供（開發）。例如：

- [使用 module 所提供功能的機制](https://developers.line.biz/en/docs/partner-docs/module/#develop-your-system)
- [從 module channel 使用 Messaging API 的機制](https://developers.line.biz/en/docs/partner-docs/module/#develop-messaging-api-and-backend)
- [使用者使用擴充功能所需的管理畫面與操作主控台機制](https://developers.line.biz/en/docs/partner-docs/module/#develop-cms)
- [module 使用費用的付款與管理機制](https://developers.line.biz/en/docs/partner-docs/module/#manage-payment-system)
- [使用者支援機制](https://developers.line.biz/en/docs/partner-docs/module/#user-support)

### Mechanisms for using the functions provided by the module 

module channel 是以 [OAuth 2.0 授權碼授予流程（authorization code granting flow）](https://datatracker.ietf.org/doc/html/rfc6749)為基礎，與 LINE 官方帳號搭配使用。客戶必須準備各種機制，才能使用 [Prepare the necessary systems and mechanisms](https://developers.line.biz/en/docs/partner-docs/module/#module-functions) 中所述的功能，包括授予 OAuth 2.0 授權碼（授權請求）所需的系統。

### Mechanism for using the Messaging API from a module channel 

若要從連結至您 LINE 官方帳號的 module channel 使用 Messaging API，您需要在請求 Messaging API 時帶上 module channel 專用的特殊請求標頭。客戶必須準備請求 Messaging API 的機制，以及 module 所提供的擴充功能（聊天機器人等）機制。

<!-- tip start -->

**發送訊息可能需要額外費用**

從 module channel 呼叫 Messaging API 向使用者發送訊息時，連結至該 module channel 的 LINE 官方帳號營運者可能需要支付 [Messaging API 費用](https://developers.line.biz/en/docs/messaging-api/pricing/)。這與從 Messaging API 頻道使用 Messaging API 發送訊息時的情況相同。

<!-- tip end -->

### Mechanism of management screen and operation console required for users to use extended functions 

客戶必須自行提供使用者使用 module 所實作之擴充功能所需的管理畫面、操作主控台及其他機制。

### Mechanism for payment and management of module usage fees 

module 將作為付費擴充功能在 [LINE Marketplace](https://line-marketplace.com/)（僅提供日文）上提供。客戶必須自行提供管理使用擴充功能之使用者，以及結算使用費用的機制。

### Support mechanism for users 

客戶必須為使用 module 擴充功能的使用者準備支援機制。LY Corporation 不會為在 [LINE Marketplace](https://line-marketplace.com/jp/inquiry)（僅提供日文）上發布之擴充功能的使用者提供支援。

## Note 

在 LINE Marketplace 中使用 module channel 功能時，您必須遵守以下各項：

- [從 Messaging API 頻道呼叫 Messaging API（合併使用）](https://developers.line.biz/en/docs/partner-docs/module/#restrict-messaging-api-request)
- [可連結的 module channel 數量上限](https://developers.line.biz/en/docs/partner-docs/module/#attach-limit)
- [module channel 可使用的 Messaging API 類型](https://developers.line.biz/en/docs/partner-docs/module/#module-scopes)
- [取得 webhook 事件](https://developers.line.biz/en/docs/partner-docs/module/#bot-module-channel-receive-webhook)

### Messaging API calls from Messaging API channel (combined) 

對於已連結至 module channel 的 LINE 官方帳號，我們不建議從 Messaging API 頻道使用 Messaging API。這是因為，視系統實作方式而定，module 所提供的擴充功能可能會發生非預期的行為。

例如，可能會發生以下問題：

- 由於[透過 Messaging API 將圖文選單連結至使用者](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)，導致 module 所提供的圖文選單未顯示。
- 使用者對從 Messaging API 頻道發送的訊息發送訊息或執行操作，因而[發送了 webhook 事件](https://developers.line.biz/en/docs/partner-docs/module/#bot-module-channel-receive-webhook)。由於 module 系統並未預期會收到此 webhook 事件，因此無法正確處理。

### Max number of module channels that can be linked 

在 LINE Marketplace 中，一個 LINE 官方帳號同一時間只能連結一個 module channel（擴充功能）。

### Types of Messaging APIs available for module channel 

module channel 可使用的 Messaging API 類型，取決於連結 module channel 時所授予的權限（scope，範圍）。詳情請參閱 Attach Module Channel 文件中的 [Scopes](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#scopes)。

### Get webhook event 

在 module channel 中，您可以設定一個端點 URL（endpoint URL）來取得 webhook 事件。

當 module channel 連結至 LINE 官方帳號時，與發送至該 LINE 官方帳號聊天室之內容相對應的 webhook 事件，也會發送至 module channel 中所設定的端點。如需 module channel 中 webhook 事件的詳細資訊，請參閱 [Receiving a webhook](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-webhook)。

<!-- tip start -->

**module channel 專用的 webhook 事件**

有些 webhook 事件只會發送至 module channel。詳情請參閱 [Receive module channel-specific webhook events](https://developers.line.biz/en/docs/partner-docs/module-technical-using-messaging-api/#get-module-channel-specific-webhook-events)。

<!-- tip end -->

<!-- note start -->

**關於 Messaging API 頻道中的 webhook 事件**

如果連結至 module channel 的 LINE 官方帳號正在[使用 Messaging API 頻道](https://developers.line.biz/en/docs/messaging-api/getting-started/)且[已啟用 webhook](https://developers.line.biz/en/docs/messaging-api/building-bot/#set-up-bot-on-line-developers-console)，則 webhook 事件會同時發送至 module channel 以及為 Messaging API 頻道所設定的端點 URL。在此情況下，發送至 Messaging API 頻道端點 URL 的 webhook 事件，其 [`mode` 屬性會被設為 `standby`](https://developers.line.biz/en/reference/messaging-api/#common-properties)，且該 webhook 事件不會包含用於[發送回覆訊息](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)的回覆權杖（reply token）。

<!-- note end -->
