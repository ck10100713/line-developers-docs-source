# 企業客戶的開發指南（Development guidelines for corporate customers）

以下是企業使用者的開發指南。在 LINE Platform 上進行開發時，請遵循這些指南。

**目錄**

<!-- table of contents -->

## About LINE bot 

### What is LINE Developers? 

LY Corporation 提供 API，讓外部企業與開發者能夠與 LY Corporation 的服務串接。LINE Developers 網站為開發者提供這些 LINE API 規格、說明開發程序的文件，以及用於設定的主控台（console）。如要瞭解更多，請參閱 [About LINE Developers site](https://developers.line.biz/en/about/)。

### How LINE bot works 

LINE bot 使用 Messaging API 來收發資訊。如要瞭解更多，請參閱 Messaging API 文件中的 [How it works](https://developers.line.biz/en/docs/messaging-api/overview/#how-messaging-api-works)。

### About the relationship between LINE bots and channels 

作為 LINE 官方帳號組成元素的 bot 與頻道（channel）之間的關係如下。

![Relationship between bots and channels](https://developers.line.biz/media/partner-docs/bot-and-channel-relations-en.png)

### Understanding various terms 

請參閱[詞彙表（Glossary）](https://developers.line.biz/en/glossary/)以瞭解各種術語的更多資訊。

### LINE bot development procedure 

1. 建立 LINE 官方帳號（bot）與 Messaging API 頻道。

   你可以從以下其中一個網站建立：
   - LINE Official Account Manager
   - LINE AGP

   如需瞭解如何建立 Messaging API 頻道，請參閱 Messaging API 文件中的 [Get started with the Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/)。

1. 準備以下系統與機制：
   - 呼叫 Messaging API、支援 [TLS 1.2 或更新版本](https://developers.line.biz/en/docs/partner-docs/development-guidelines/#use-higher-TLS1-2)的伺服器等環境
   - 取得 webhook 事件、支援 [TLS 1.2 或更新版本](https://developers.line.biz/en/docs/partner-docs/development-guidelines/#https-communication-compatible)的 bot 伺服器等環境

   呼叫 Messaging API 的伺服器環境與取得 webhook 事件的 bot 伺服器環境，並不一定需要分別準備不同的環境。

1. 準備並實作用於取得 webhook 事件的 bot 伺服器。

1. 在 LINE Developers Console 中，前往 **Messaging API** > **Webhook settings**，在 **Webhook URL** 設定 bot 伺服器 URL，然後啟用 **Use Webhook**。

1. 將你建立的 LINE 官方帳號加為好友，並確認 bot 伺服器是否正在取得 webhook 事件。

### Items to check before releasing the LINE bot 

在發佈 LINE bot 之前，請務必確認以下事項。

1. 需要存取 LINE Developers Console 的成員，已被授予頻道[權限（permissions）](https://developers.line.biz/en/docs/line-developers-console/managing-roles/)與 LINE Official Account Manager [權限（permissions）](https://www.lycbiz.com/jp/manual/OfficialAccountManager/account-settings_permission/)（僅提供日文版）。

1. 確認在 LINE Developers Console 的 **Messaging API** > **Webhook settings** > **Webhook URL** 中設定了正確的 URL，且 bot 伺服器能正確處理 webhook 事件。

1. 實作時已考量[發送 API 請求的注意事項（Notes on sending API requests）](https://developers.line.biz/en/docs/partner-docs/development-guidelines/#send-api-requests)中所述的注意事項。

1. 遵循 [LINE BOT security guidelines](https://vos.line-scdn.net/line-developers/docs/media/partner-docs/LINE_BOT_Security_Guidelines.pdf)（僅提供日文版）與 [LINE BOT security checklist](https://vos.line-scdn.net/line-developers/docs/media/partner-docs/LINE_BOT_Security_Checklist.xlsx)（僅提供日文版）中的安全標準，或建置同等或更佳的環境。

## Notes on receiving webhook events on bot servers 

### Secure communication and bot server environment 

#### HTTPS communication compatible with TLS 1.2 or later 

當 bot 伺服器取得從 LINE Platform 發送的 webhook 事件時，必須使用支援 TLS 1.2 或更新版本的 HTTPS 通訊。請使用由公開認證機構（public certification authority）核發的 SSL 憑證進行 HTTPS 通訊。你可以購買 SSL 憑證，也可以使用免費核發的憑證，例如 [Let's Encrypt](https://letsencrypt.org/)。如需瞭解更多設定 webhook 的資訊，請參閱 Messaging API 文件中的 [Set a Webhook URL](https://developers.line.biz/en/docs/messaging-api/building-bot/#setting-webhook-url)。

#### Build an environment that complies with security guidelines 

這些安全指南與檢查清單說明了建置 bot 伺服器時必須滿足的安全標準。在使用 LINE bot 提供服務時，請遵循所述的安全標準，或準備同等或更佳的環境。

- [LINE bot security guidelines](https://vos.line-scdn.net/line-developers/docs/media/partner-docs/LINE_BOT_Security_Guidelines.pdf)（僅提供日文版）
- [LINE bot security checklist](https://vos.line-scdn.net/line-developers/docs/media/partner-docs/LINE_BOT_Security_Checklist.xlsx)（僅提供日文版）

### Verification of received webhook events 

請求標頭 [`x-line-signature`](https://developers.line.biz/en/reference/messaging-api/#webhooks) 包含一組簽章，用於驗證所收到的 webhook 事件確實來自 LINE Platform。bot 伺服器使用既定的演算法，從收到的請求主體（request body）計算出摘要值（digest value），並驗證其是否與 `x-line-signature` 請求標頭中的簽章相符。透過驗證簽章相符，你可以確認所收到的請求是 LINE Platform 發送的正確 webhook 事件。

頻道密鑰（channel secret）會作為簽章的計算金鑰使用。因此，處理頻道密鑰時請務必小心。如需瞭解更多資訊與程式碼範例，請參閱 Messaging API reference 中的 [Signature validation](https://developers.line.biz/en/reference/messaging-api/#signature-validation)。

<!-- note start -->

**LINE Platform 的 IP 位址未公開**

發送 webhook 請求的 LINE Platform IP 位址並未公開。為了更佳的安全性，請使用[簽章驗證（signature validation）](https://developers.line.biz/en/reference/messaging-api/#signature-validation)，而非透過 IP 位址進行存取控制。

<!-- note end -->

![Signature validation image](https://developers.line.biz/media/partner-docs/webbhook-signature-verification-en.png)

### Support for mass and intensive webhook event delivery 

由於 LINE 官方帳號的特性，可能會無預期地發生大量存取（發送 webhook 事件）。如果發送了超過 bot 伺服器處理能力的 webhook 請求，發送給使用者的訊息可能會延遲或無法送達。

<!-- tip start -->

**容易發生存取集中的情境範例**

- 將 LINE 官方帳號的[顯示於搜尋結果（Show in search results）](https://www.lycbiz.com/jp/manual/OfficialAccountManager/tutorial-step5/)（僅提供日文版）設定為「Show」之後不久
- 實施[贊助貼圖（Sponsored sticker）](https://www.lycbiz.com/jp/service/line-promotion-sticker/)（僅提供日文版）等措施之後不久
- 使用[群發訊息（broadcast message）](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)等方式一次將訊息發送給所有好友之後不久（尤其是包含活動或其他措施時）
- 在新聞或電視等媒體上被報導之後不久

存取可能特別集中在中午 12:00 以及 17:00 至 24:00 的時段。

<!-- tip end -->

<!-- note start -->

**注意**

- LY Corporation 不提供對 bot 伺服器進行負載測試（load test）的環境。請勿以包含 LINE Platform 的方式進行負載測試。
- 如果你在好友數眾多（超過一百萬）的 LINE 官方帳號上發送被認為對使用者反應度很高的宣傳訊息（例如活動），可能會影響整個 LINE Platform 的效能。在這種情況下，請避免一次發送所有訊息，並採取分階段發送訊息等措施，以避免來自使用者的存取集中。

<!-- note end -->

### Webhook ON/OFF setting 

你可以在 LINE Developers Console 的 **Messaging API settings** > **Webhook settings** 中開啟或關閉 **Use webhook**。你也可以在 LINE Official Account Manager 的 **Settings** > **Response settings** 區段中開啟或關閉 **Webhooks**。

<!-- note start -->

**開始使用 webhook 的注意事項**

啟用 Webhook 設定時，請先使用驗證用帳號在測試環境中驗證運作情況，再將設定套用至目標 LINE 官方帳號。

<!-- note end -->

<!-- tip start -->

**同步 webhook 設定**

在 LINE Developers Console 與 LINE Official Account Manager 中所做的 webhook 設定會互相同步。

<!-- tip end -->

### Webhook ON/OFF and auto reply message settings 

以下是 **Webhooks** 設定與 LINE Official Account Manager 中的 **Response mode** 和 **Greeting message** 設定的組合。

| **Webhooks** | **Response mode** 與 **Greeting message** | 設定可用性 |
| --- | --- | --- |
| Enabled | Enabled | ✅ |
| Enabled | Disabled | ✅ |
| Disabled | Enabled | ✅ |
| Disabled | Disabled | ❌ |

<!-- note start -->

**不被允許的設定組合**

為了提供更佳的使用者體驗，不允許同時不使用 **Webhooks** 與 LINE Official Account Manager 的 **Response mode** 和 **Greeting message** 設定的組合，因為這會導致 LINE 官方帳號無法向使用者發送訊息。

<!-- note end -->

<!-- note start -->

**何時會發送問候訊息**

LINE Official Account Manager 的 **Greeting message** 是當 LINE 官方帳號被加為好友時自動發送的訊息。**Greeting message** 在被解除封鎖時也會發送。

<!-- note end -->

### Processing flow when receiving a webhook request 

bot 伺服器在取得 webhook 事件後，請在 2 秒內以 HTTP 狀態碼 `200` 回應。

建議在 bot 伺服器取得 webhook 請求時，將事件處理非同步化（desynchronize），以避免 webhook 請求的處理延遲後續的處理。如果事件處理採非同步方式，請實作成能在維持事件上下文（context）的情況下進行處理。

下圖描繪了非同步處理的情形。

![Processing flow when receiving a webhook request](https://developers.line.biz/media/partner-docs/flow-when-receiving-a-webhook-en.png)

### If a problem occurs when sending a webhook request 

對於認證服務提供者（certified provider）旗下的 Messaging API 頻道，如果在取得 webhook 事件後 2 秒內沒有回傳 HTTP 狀態碼 `2xx`，系統會向頻道管理員發送 [`request_timeout`](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/#check-error-reason) [錯誤通知（error notification）](https://developers.line.biz/en/docs/partner-docs/error-notification/)。

<!-- note start -->

**錯誤通知功能的使用**

錯誤通知功能僅適用於認證服務提供者旗下的 Messaging API 頻道。

<!-- note end -->

### Other precautions 

#### One webhook can contain multiple webhook event objects 

從 LINE Platform 發送的一個 webhook 可能包含多個 webhook 事件物件（webhook event object）。此外，一個 webhook 不一定只對應一位使用者，因此來自 A 的[訊息事件（Message event）](https://developers.line.biz/en/reference/messaging-api/#message-event)與來自 B 的[加入好友事件（Follow event）](https://developers.line.biz/en/reference/messaging-api/#follow-event)可能會出現在同一個 webhook 中。

請確保 bot 伺服器即使收到包含多個 webhook 事件物件的 webhook，也能正確處理所有內容。如需瞭解更多有關 webhook 事件物件的資訊，請參閱 Messaging API reference 中的 [Webhook Event Objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)。

#### Responding to structural changes in webhook event objects 

當 Messaging API 功能有新增或變更時，webhook 事件物件可能會新增屬性（property）。請將 bot 伺服器實作成即使收到帶有新屬性的 webhook 事件物件也不會造成問題。如需瞭解更多有關 webhook 事件物件的資訊，請參閱 Messaging API reference 中的 [Webhook Event Objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)。

#### About the header included in the webhook request 

請參閱 Messaging API reference 中的 [Request headers](https://developers.line.biz/en/reference/messaging-api/#request-headers)。

#### About processing unexpected chat transmissions 

你無法限制使用者向你的 LINE 官方帳號發送聊天訊息與對應的 webhook 事件。如果特定使用者發送了非預期的聊天訊息，請將系統實作成能依情況變更處理流程。

## Notes on sending API requests 

### Issuing channel access tokens 

Messaging API 請求使用[頻道存取權杖（channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/)來驗證使用者具有使用該頻道的權限。目前我們提供[四種頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#channel-access-token-types)，各有不同的有效期間（validity period）與核發方式。

<!-- note start -->

**關於長效期頻道存取權杖**

雖然可以從 LINE Developers Console 核發有效期間極長的長效期頻道存取權杖，但從安全的角度來看，我們不建議核發長效期頻道存取權杖。核發頻道存取權杖時，我們建議使用有效期間為 30 天的短效期頻道存取權杖、可由使用者指定到期時間的頻道存取權杖（channel access token v2.1），或無狀態（stateless）頻道存取權杖。

<!-- note end -->

### Reissuing channel access tokens 

短效期頻道存取權杖、可由使用者指定到期時間的頻道存取權杖，以及無狀態頻道存取權杖都有有效期間，一旦過期就無法再使用。此外，頻道存取權杖一旦核發後，其有效期間便無法延長（更新）。因此，有必要考量剩餘的有效期間，並建立定期重新核發新頻道存取權杖的流程。

你可以核發多個頻道存取權杖，但依頻道存取權杖的類型不同，可核發的數量會有上限。當從多台伺服器或多個系統使用 Messaging API 時，請務必正確管理各自使用的頻道存取權杖。

對於短效期頻道存取權杖或可由使用者指定到期時間的頻道存取權杖，在核發新的頻道存取權杖後，我們建議你撤銷（revoke）不再使用的舊頻道存取權杖。如需瞭解更多資訊，請參閱 LINE Platform basics 中的 [Example of channel access token operation](https://developers.line.biz/en/docs/basics/channel-access-token/#how-to-operate-channel-access-token)。

### Max channel access token issuance limit 

各類型頻道存取權杖的最大核發上限如下：

| 類型 | 最大核發上限 | 超過上限時的行為 | 頻道存取權杖失效的條件 |
| --- | --- | --- | --- |
| 短效期頻道存取權杖 | 30 | 依核發順序使現有的短效期頻道存取權杖失效 | <ul><li>有效期間已過期</li><li>超過最大核發上限</li><li>執行頻道存取權杖撤銷（revoke API）</li></ul> |
| 長效期頻道存取權杖 | 1 | 現有的長效期頻道存取權杖會被停用 | <ul><li>超過最大核發上限</li><li>執行頻道存取權杖撤銷（revoke API）</li></ul> |
| 可由使用者指定到期時間的存取權杖（channel access token v2.1） | 30 | 發生 API 錯誤且無法核發額外的權杖 | <ul><li>有效期間已過期</li><li>執行頻道存取權杖撤銷（revoke API）</li></ul> |
| 無狀態頻道存取權杖 | 無限制 | - | <ul><li>有效期間已過期</li></ul> |

### Message delivery request 

如果訊息成功發送，會回傳一個空的 JSON 物件，並帶有 HTTP 狀態碼 `200`（僅 narrowcast API 為 `202`）。

當發送訊息失敗時，會回傳包含錯誤訊息等 JSON 資料的回應主體，作為[錯誤回應（Error responses）](https://developers.line.biz/en/reference/messaging-api/#error-responses)。

<!-- note start -->

**關於錯誤回應**

錯誤回應中所含的錯誤訊息並無保證，且可能在不另行通知的情況下變更。當發生錯誤時，請依收到的 HTTP 狀態碼進行例外處理。

<!-- note end -->

<!-- tip start -->

**儲存記錄檔**

當你向 Messaging API 發出請求時，請將所請求的 API 與收到的回應記錄檔保存一段時間。如需瞭解更多有關儲存記錄檔的資訊，請參閱 Messaging API 文件中的 [Save logs](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#save-logs)。

<!-- tip end -->

### Retry message delivery request 

即使 LINE Platform 沒有發生故障，也可能因 bot 伺服器的網路連線狀態及其他因素而發生以下問題。

- API 請求未成功完成
- 無法正確從 LINE Platform 取得回應

在這種情況下，如果你連續發出相同的 API 請求，當第一個 API 請求其實已被成功接受時，使用者就會收到相同訊息兩次。為防止這種情況，請實作重試金鑰（retry key，`X-Line-Retry-Key`）以安全地重試請求。如需瞭解更多有關訊息發送請求的資訊，請參閱 Messaging API 文件中的 [Retry failed API requests](https://developers.line.biz/en/docs/messaging-api/retrying-api-request/)。

![Retrying a failed API request](https://developers.line.biz/media/partner-docs/retrying-a-failed-api-request-en.png)

### Request limits 

LINE bot 在單次請求中可發送的訊息長度有限制，在一定時間內可發送的訊息數量也有限制。

#### Text message limits 

[文字訊息（text messages）](https://developers.line.biz/en/reference/messaging-api/#text-message)與[文字訊息（v2）（text messages (v2)）](https://developers.line.biz/en/reference/messaging-api/#text-message-v2)中可指定的最大字元數為 5000。

#### Request size limits 

最大請求大小為 2MB。

#### Request rate limits 

Messaging API 會對每個端點（endpoint）套用[速率限制（Rate limits）](https://developers.line.biz/en/reference/messaging-api/#rate-limits)。

無論你使用的是正式帳號還是測試帳號，[禁止為了行為測試而發送大量請求](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#prohibiting-mass-requests-to-line-platform)。在對訊息發送進行負載測試時，請勿將 LINE Platform 納入其中。

### How to send messages 

如需瞭解更多有關如何發送訊息的資訊，請參閱以下文件：

- [Reply to messages and actions from users (reply messages)](https://developers.line.biz/en/docs/messaging-api/sending-messages/#reply-messages)
- [Send messages at any time](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-messages-at-any-time)

<!-- tip start -->

**回覆權杖（reply token）的有效期間**

如需瞭解更多有關[回覆訊息（Reply messages）](https://developers.line.biz/en/docs/messaging-api/sending-messages/#reply-messages)中所使用回覆權杖之有效期間的資訊，請參閱 Messaging API reference 中的 [Reply token](https://developers.line.biz/en/reference/messaging-api/#send-reply-message-reply-token)。

<!-- tip end -->

### Use HTTPS (TLS 1.2 or later) 

呼叫 Messaging API 的系統與 LINE API 伺服器之間的通訊，必須透過 HTTPS（TLS 1.2 或更新版本）進行。此外，當使用 Messaging API 發送[圖片訊息（Image message）](https://developers.line.biz/en/docs/messaging-api/message-types/#image-messages)或包含[圖片元件（Image component）](https://developers.line.biz/en/reference/messaging-api/#f-image)的 Flex Message 時，儲存該檔案的伺服器也必須支援 HTTPS（TLS 1.2 或更新版本）通訊。

### Dealing with high volume access 

依訊息發送對象的使用者數量與訊息內容而定，訊息中的 URL、圖片及其他內容可能會產生大量存取。

為因應這類情況，請使用 CDN 或負載平衡器（load balancer）等負載分散機制，或分階段發送訊息，以避免儲存內容的伺服器因大量存取而當機。

![Large volume of requests](https://developers.line.biz/media/partner-docs/large-volume-of-requests-en.png)

## Notes on using LINE Login 

透過使用 LINE Login，你可以在你的網路服務與原生應用程式中，實作使用使用者 LINE 帳號資訊的登入功能。

舉例來說，藉由在網頁應用程式中整合 LINE Login，並將取得的資訊與貴公司的會員資訊串接，你就能使用 Messaging API 向使用者發送更個人化的訊息。

如需瞭解更多有關 LINE Login 的資訊，請參閱 [LINE Login overview](https://developers.line.biz/en/docs/line-login/overview/)。

### LINE Login authorization and verification process 

網頁應用程式版 LINE Login（網頁登入）的流程，是以 [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) 授權碼授予流程（authorization code grant flow）與 [OpenID® Connect](https://openid.net/specs/openid-connect-core-1_0.html) 協定為基礎。如需瞭解更多有關網頁應用程式版 LINE Login 的資訊，請參閱 LINE Login 文件中的 [Login flow](https://developers.line.biz/en/docs/line-login/integrate-line-login/#login-flow)。

### About callback URLs 

回呼網址（callback URL，`redirect_uri`）會在使用者完成 LINE Login 的驗證與授權操作後，作為[在網頁應用程式中接收授權碼或錯誤回應（Receiving the authroization code or error response with a web app）](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code-or-error-response-with-a-web-app)的 URL 使用。回呼網址可在 LINE Developers Console 的頻道設定中的 **LINE Login** 設定。

如需瞭解更多有關回呼網址的資訊，請參閱 LINE Login 文件中的 [Setting a callback URL](https://developers.line.biz/en/docs/line-login/integrate-line-login/#setting-callback-url)。

<!-- note start -->

**設定回呼網址時的注意事項**

- 最多可註冊 400 個 URL 作為回呼網址。
- 你可以註冊包含查詢參數（query parameter）的 URL 作為回呼網址。
- 在授權請求時所指定的 `redirect_uri`，是註冊為回呼網址之 URL 的 URL 編碼字串。可以新增任何查詢參數。
  - 你可以註冊 `https://example.com` 作為回呼網址，並在授權請求時所指定的 `redirect_uri` 中指定 `https://example.com?key=value`。

<!-- note end -->

### Get authorization response or error response in web app 

當使用者的驗證與授權程序完成後，使用者會被重新導向至回呼網址。

當使用者授予應用程式存取權限時，會回傳包含授權碼的授權回應。但若使用者未授予應用程式存取權限，則會回傳錯誤回應。如需瞭解更多資訊，請參閱 LINE Login 文件中的 [Receiving the authorization response or error response with a web app](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code-or-error-response-with-a-web-app)。

### Issue an access token 

存取權杖（access token）會使用透過 LINE Login 授權請求所取得的授權碼來核發。如需瞭解更多有關核發存取權杖的資訊，請參閱 LINE Login v2.1 API reference 中的 [Issue access token](https://developers.line.biz/en/reference/line-login/#issue-access-token)。

<!-- note start -->

**核發存取權杖時的注意事項**

- 核發存取權杖時所指定的 `redirect_uri` 參數，必須與授權請求時所指定的值相同。
- 授權碼只能使用一次，無論存取權杖是否成功核發。

<!-- note end -->

### Verify the ID token 

當 LINE Login 的授權請求在 scope 中指定了 `openid` 時，所取得 token 端點的 [payload](https://developers.line.biz/en/docs/line-login/integrate-line-login/#response) 中會包含一組 ID token。你可以透過驗證所取得的 ID token 來取得使用者的個人資料資訊。如需瞭解更多資訊，請參閱 LINE Login 文件中的 [Get profile information from ID tokens](https://developers.line.biz/en/docs/line-login/verify-id-token/)。

### Other LINE Login APIs 

透過使用所取得的存取權杖，你可以檢查使用者與 LINE 官方帳號之間的好友關係，並取得使用者的個人資料資訊。如需瞭解更多有關 LINE Login API 的資訊，請參閱 [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

### Linking information obtained through LINE Login with information managed by your company (ID linking) 

藉由將透過 LINE Login 取得的使用者資訊（使用者 ID 等）與公司管理的會員資訊串接，便能發送更個人化的訊息。

![ID linkage flow](https://developers.line.biz/media/partner-docs/flow-for-linking-ids-en.png)

<!-- note start -->

**關於與會員資訊的串接與管理**

- LY Corporation 不提供將透過 LINE Login 取得的使用者資訊與公司管理之會員資訊串接的方式。
- 在串接會員資訊等資料時，請以安全為考量設計系統，以防止假冒（spoofing）。
- 請設立一套流程，用於解除 LINE Platform 的使用者資訊與會員資訊等資料之間的串接。
- 如果你在 LINE app 的 **Settings** > **Account** > **Authorized apps** 中選擇 **Unlink**，LINE Login 的「頻道同意（Channel consent）」會被撤回，但使用者資訊的關聯並不會被解除。將透過 LINE Login 取得的資訊與公司管理資訊串接的處理，必須由客戶另行進行。

![unlink](https://developers.line.biz/media/partner-docs/unlink.png)

<!-- note end -->

### Add friend option 

LINE Login 讓你能夠使用一個選項，在使用者登入時將你的 LINE 官方帳號加為好友。這稱為加入好友選項（add friend option）。用於加入好友選項的 LINE 官方帳號可在 LINE Developers Console 中設定。如需瞭解更多資訊，請參閱 LINE Login 文件中的 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)。

<!-- note start -->

**使用加入好友選項時的注意事項**

- 你串接的 LINE 官方帳號僅限於與該 LINE Login 頻道相關的帳號。例如，請勿將 A 公司的 LINE 官方帳號串接到與 A 公司無關的 B 公司 LINE Login 頻道。
- 設定的變更會立即反映，因此請謹慎操作，以避免不慎設定到非預期的 LINE 官方帳號（例如用於測試的帳號）。
- 如果該 LINE Login 頻道隸屬於認證服務提供者，則 LINE Login 同意畫面上的 **Add Friend (Unblock)** 選項預設會被選取（勾選）。

<!-- note end -->

### state verification 

請求 LINE Login 授權時所指定的 `state` 參數，是用於防止[跨站請求偽造（Cross-Site Request Forgery）](https://en.wikipedia.org/wiki/Cross-site_request_forgery)所必需的。請在你的網頁應用程式中為每個授權請求工作階段（session）隨機產生它，並在[接收授權回應或錯誤回應](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code-or-error-response-with-a-web-app)時加以驗證。

![state verification](https://developers.line.biz/media/partner-docs/state-verification-en.png)

## LINE Front-end Framework (LIFF) 

LINE Front-end Framework（LIFF）是 LY Corporation 提供的網頁應用程式平台。在此平台上執行的網頁應用程式稱為 LIFF app。

LIFF app 讓你能夠從 LINE Platform 取得 LINE 使用者 ID 及其他資訊。LIFF app 可以利用這些資訊提供運用使用者資訊的功能，或代表使用者發送訊息。

如需瞭解更多有關 LIFF app 的資訊，請參閱 [LIFF overview](https://developers.line.biz/en/docs/liff/overview/)。

## Other features 

### How to set the destination browser 

當從聊天室或從 LINE 應用程式內建瀏覽器（in-app browser）存取 URL 時，你可以透過以特殊查詢參數開啟 URL，將開啟該 URL 的瀏覽器改為外部瀏覽器。如需瞭解更多有關查詢參數的資訊，請參閱 [Opening a URL in an external browser](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/#opening-url-in-external-browser)。

### About URL schemes 

我們提供可在與 LINE 官方帳號的聊天室中使用的 URL scheme。如需瞭解更多有關 URL scheme 的資訊，請參閱 [Using LINE features with the LINE URL scheme](https://developers.line.biz/en/docs/line-login/using-line-url-scheme/)。

### About channel permissions 

LINE Login 頻道與 LINE MINI App 頻道在頻道建立後不久的狀態為「Developing（開發中）」。若要在狀態為「Developing」的頻道上登入 LINE 或存取 LIFF app，你需要一個在該頻道上具有管理員（admin）或測試者（tester）權限的 LINE 帳號。

如需瞭解更多有關權限的資訊，請參閱 LINE Developers Console 文件中的 [Channel roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel)。

### Stickers and emojis available in the Messaging API 

在 Messaging API 中，貼圖是使用[諸如貼圖包 ID（package ID）與貼圖 ID（sticker ID）等識別碼](https://developers.line.biz/en/docs/messaging-api/sticker-list/#sticker-definitions)來交換的。

#### Send stickers via the Messaging API 

如需瞭解更多有關可透過 Messaging API 發送之貼圖的資訊，請參閱 Messaging API 文件中的 [Stickers](https://developers.line.biz/en/docs/messaging-api/sticker-list/)。

#### Check the sticker sent by the user 

當使用者向 LINE 官方帳號發送貼圖時，所發送貼圖的貼圖包 ID 與貼圖 ID 會以 [Webhook message event](https://developers.line.biz/en/reference/messaging-api/#wh-sticker) 的形式發送。

我們不公開使用所收到 Webhook 事件中所含貼圖 ID 來取得已發送貼圖圖片的機制。我們僅在我們的[技術合作夥伴（Technology Partner）](https://www.lycbiz.com/jp/partner/technology/line/)（僅提供日文版）建立可與使用者直接互動的聊天工具（CRM 工具等），或 LY Corporation 認為適當時，才提供此項服務。詳情請洽詢我們的負責窗口。

#### Sending LINE emojis 

當你發送[文字訊息（text message）](https://developers.line.biz/en/reference/messaging-api/#text-message)或[文字訊息（v2）（text message (v2)）](https://developers.line.biz/en/reference/messaging-api/#text-message-v2)時，可以發送 LINE 表情貼（LINE emoji）。如需瞭解更多有關 LINE 表情貼的資訊，請參閱 Messaging API 文件中的 [LINE emoji](https://developers.line.biz/en/docs/messaging-api/emoji-list/)。

#### Getting LINE emojis 

當使用者向 LINE 官方帳號發送 LINE 表情貼時，它會以陣列形式儲存在訊息事件之 text 物件的 [emojis object](https://developers.line.biz/en/reference/messaging-api/#wh-text) 中。

<!-- note start -->

**已發送的 LINE 表情貼可能不會包含在 emojis 屬性中**

- 從 LINE for Android 發送的預設 LINE 表情貼不會被包含在內。
- Unicode 定義的表情符號與較舊版本的 LINE 表情貼可能無法正確取得。

<!-- note end -->
