# 連結模組頻道（Attach Module Channel）

<!-- note start -->

**使用選用功能需經過特定程序**

本文件所說明的功能僅提供給已完成規定申請程序的企業客戶使用。若您想透過模組發布擴充功能，請聯絡業務代表，或透過 [LINE Marketplace Inquiry](https://line-marketplace.com/jp/inquiry) 與我們聯絡（僅提供日文）。

<!-- note end -->

若要使用模組頻道（module channel）功能，您需要取得 LINE 官方帳號管理者的授權，並依照下列步驟連結（attach）模組頻道：

## Attach module channels using the OAuth 2.0 authorization mechanism 

依循 OAuth 2.0 授權機制的流程，您可以取得 LINE 官方帳號管理者的授權後連結模組頻道。

## Flow for attaching the module 

第一個畫面與第五個畫面應由負責開發模組頻道的公司自行準備。

![Flow of attaching module channels using the OAuth 2.0 auth mechanism](https://developers.line.biz/media/partner-docs/module-technical/flow-en.png)

<!-- note start -->

**對 LINE 官方帳號連結多個模組頻道的限制**

單一 LINE 官方帳號只能連結一個具備「Default Active」功能的模組頻道。

<!-- note end -->

1. [向 LINE 官方帳號管理者請求授權](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#request-auth-from-line-oa-admin)
1. [關於連結畫面](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#about-linkage-screen)
1. [接收授權碼或錯誤回應](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#get-auth-code)
1. [由模組頻道提供者操作進行連結](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#link-attach-by-operation-of-module-channel-provider)

### 1. Request authorization from the LINE Official Account admin 

讓 LINE 官方帳號管理者存取用於認證與授權的 URL（授權 URL `https://manager.line.biz/module/auth/v1/authorize` 加上查詢參數），即可開始將模組頻道連結至 LINE 官方帳號的程序。

**認證與授權 URL 範例**

```
https://manager.line.biz/module/auth/v1/authorize?response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fcallback&scope=message%3Asend%20message%3Areceive&state={CSRF token}&region=JP&basic_search_id={LINE Official Account basic ID}&brand_type=premium
```

一般而言，您會在開始連結模組頻道的頁面上設置一個存取此 URL 的連結，然後請 LINE 官方帳號管理者點擊該連結。在上述範例的流程中，當您在「'In Your Service' Click to Attach」頁面點擊 **Attach Module** 按鈕時，即可存取此 URL。

#### Query Parameters 

<!-- parameter start (props: required) -->

response_type

String

`code`

<!-- parameter end -->
<!-- parameter start (props: required) -->

redirect_uri

String

重新導向 URL。供模組頻道開發者接收授權碼的 URL。在完成認證與授權（於連結畫面上的操作）後，LINE 官方帳號管理者將被重新導向至此 URL。

此 URL 應由模組頻道開發者提供。此 URL 必須與您先前在 [LINE Developers Console](https://developers.line.biz/console/) 中為該模組頻道註冊的重新導向 URL 一致。

<!-- note start -->

**為 redirect_uri 指定的值應經過 URL 編碼**

若您忘記對查詢參數進行 URL 編碼，則第二個及後續的查詢參數會被認定為認證 URL 的查詢參數，而不會被傳遞至重新導向的目的地。

在認證 URL 中將 `https://example.com/auth?param1=value1&param2=value2` 指定為 `redirect_uri` 的範例為 `https://manager.line.biz/module/auth/v1/authorize?response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%3Fparam1%3Dvalue1%26param2%3Dvalue2&scope=message%3Asend%20message%3Areceive&state={CSRF token}&region=JP&basic_search_id={LINE Official Account basic id}&brand_type=premium`。

<!-- note end -->

<!-- parameter end -->
<!-- parameter start (props: required) -->

client_id

String

模組頻道的頻道 ID（channel ID）。由 LINE Platform 發行的頻道專屬識別碼。

<!-- parameter end -->
<!-- parameter start (props: required) -->

scope

String

指定您想要請求 LINE 官方帳號管理者允許的權限（scope）。若要指定多個 scope，請以經過 URL 編碼的空格（%20）分隔。詳情請參閱 [scopes](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#scopes)。

<!-- parameter end -->
<!-- parameter start (props: required) -->

state

String

用於防止[跨站請求偽造（cross-site request forgery, CSRF）](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12)的唯一英數字串。此值應由負責開發模組頻道的公司系統隨機產生的唯一字串。不可使用經過 URL 編碼的字串。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

region

String

模組頻道所連結的 LINE 官方帳號的地區。請指定 `JP` 或 `TW`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

basic_search_id

String

LINE 官方帳號的 [basic ID](https://help.linebiz.com/lineadshelp/s/article/L000001191?language=ja)。當您只想允許模組頻道連結至特定 LINE 官方帳號時指定。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

brand_type

String

指定以限制可連結的 [LINE 官方帳號的帳號類型](https://www.lycbiz.com/jp/service/line-official-account/account-type/)。

- 進階帳號（Premium Account）：`premium`
- 認證帳號（Verified Account）：`verified`
- 未認證帳號（Unverified Account）：`unverified`

若要指定多種帳號類型，請以經過 URL 編碼的空格（%20）串接。例如，若要限制只能連結進階帳號與認證帳號，您可以指定 `brand_type=premium%20verified`。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

code_challenge

String

當使用 OAuth 2.0 擴充規格中定義的 PKCE（Proof Key for Code Exchange）作為防範授權碼攔截攻擊的對策時指定。符合 [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)。

<!-- parameter end -->
<!-- parameter start (props: optional) -->

code_challenge_method

String

`S256`

當使用 OAuth 2.0 擴充規格中定義的 PKCE（Proof Key for Code Exchange）作為防範授權碼攔截攻擊的對策時指定。符合 [RFC 7636](https://datatracker.ietf.org/doc/html/rfc7636)。

<!-- parameter end -->

#### Scopes 

您可以透過 `scope` 參數指定下列 scope。若要指定多個 scope，請以經過 URL 編碼的空格（%20）分隔。

| Scope | 模組頻道可使用的 API |
| --- | --- |
| 不需指定（預設） | 無 scope 即可使用。<ul><li>[Issue link token (/v2/bot/user/{userId}/linkToken)](https://developers.line.biz/en/reference/messaging-api/#issue-link-token)</li></ul> |
| `message%3Asend`<br />(message:send) | <ul><li>[Send reply message (/v2/bot/message/reply)](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)</li><li>[Send push message (/v2/bot/message/push)](https://developers.line.biz/en/reference/messaging-api/#send-push-message)</li><li>[Send multicast message (/v2/bot/message/multicast)](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)</li><li>[Send broadcast message (/v2/bot/message/broadcast)](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)</li><li>[Send narrowcast message (/v2/bot/message/narrowcast)](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message) 及相關 API</li><li>[Managing Audience (/v2/bot/audienceGroup/\*\*\*)](https://developers.line.biz/en/reference/messaging-api/#manage-audience-group)</li><li>[Get the target limit for additional messages (/v2/bot/message/quota)](https://developers.line.biz/en/reference/messaging-api/#get-quota)</li><li>[Get number of messages sent this month (/v2/bot/message/quota/consumption)](https://developers.line.biz/en/reference/messaging-api/#get-consumption)</li><li>[Display a loading animation (/v2/bot/chat/loading/start)](https://developers.line.biz/en/reference/messaging-api/#display-a-loading-indicator)</li></ul> |
| `message%3Areceive`<br />(message:receive) | <ul><li>取得 Messaging API 與模組頻道的 webhook 事件</li><ul><li>[Webhooks](https://developers.line.biz/en/reference/messaging-api/#webhooks)</li><li>[Webhook Event Objects](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)</li></ul><li>[Chat control (Chat Control)](https://developers.line.biz/en/docs/partner-docs/module-technical-chat-control/#what-is-chat-control)</li></ul> |
| `account%3Amanage`<br />(account:manage) | <ul><li>[Set default rich menu (/v2/bot/user/all/richmenu/{richMenuId})](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu)</li><li>[Get number of message deliveries (/v2/bot/insight/message/delivery?date={date})](https://developers.line.biz/en/reference/messaging-api/#get-number-of-delivery-messages)</li><li>[Get number of followers (/v2/bot/insight/followers?date={date})](https://developers.line.biz/en/reference/messaging-api/#get-number-of-followers)</li><li>[Get friend demographics (/v2/bot/insight/demographic)](https://developers.line.biz/en/reference/messaging-api/#get-demographic)</li><li>[Get user interaction statistics (/v2/bot/insight/message/event?requestId={requestId})](https://developers.line.biz/en/reference/messaging-api/#get-message-event)</li><li>[Get statistics per unit (/v2/bot/insight/message/event/aggregation?customAggregationUnit={customAggregationUnit}&from={from}&to={to})](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit)</li></ul> |
| `message%3Amark_as_read`<br />(message:mark_as_read) | <ul><li>[Mark messages from users as read (/v2/bot/message/markAsRead)](https://developers.line.biz/en/reference/partner-docs/#mark-messages-from-users-as-read)</li></ul> |
| `message%3Atemplated_pnp`<br />(message:templated_pnp) | <ul><li>[Send a LINE notification message (template) (/v2/bot/message/pnp/templated/push)](https://developers.line.biz/en/reference/line-notification-messages/#send-line-notification-message-template)</li><li>[Get number of sent LINE notification messages (template) (/v2/bot/message/delivery/pnp/templated)](https://developers.line.biz/en/reference/line-notification-messages/#get-number-of-sent-line-notification-messages-template)</li><li>當 LINE notification message 送達時接收 webhook 事件（[Webhook delivery completion event](https://developers.line.biz/en/docs/partner-docs/line-notification-messages/message-sending-complete-webhook-event/)）</li></ul> |
| `profile%3Aread`<br />(profile:read) | <ul><li>[Get profile (/v2/bot/profile/{userId})](https://developers.line.biz/en/reference/messaging-api/#get-profile)</li><li>[Get group chat summary (/v2/bot/group/{groupId}/summary)](https://developers.line.biz/en/reference/messaging-api/#get-group-summary)</li><li>[Get group chat member profile (/v2/bot/group/{groupId}/member/{userId})](https://developers.line.biz/en/reference/messaging-api/#get-group-member-profile)</li><li>[Get multi-person chat member profile (/v2/bot/room/{roomId}/member/{userId})](https://developers.line.biz/en/reference/messaging-api/#get-room-member-profile)</li><li>[Get number of users in a group chat (/v2/bot/group/{groupId}/members/count)](https://developers.line.biz/en/reference/messaging-api/#get-members-group-count)</li><li>[Get number of users in a multi-person chat (/v2/bot/room/{roomId}/members/count)](https://developers.line.biz/en/reference/messaging-api/#get-members-room-count)</li></ul> |
| `coupon%3Amanage`<br />(coupon:manage) | <ul><li>[Create a coupon (/v2/bot/coupon)](https://developers.line.biz/en/reference/messaging-api/#create-coupon)</li><li>[Discontinue a coupon (/v2/bot/coupon/{couponId}/close)](https://developers.line.biz/en/reference/messaging-api/#discontinue-coupon)</li><li>[Get a list of coupons (/v2/bot/coupon)](https://developers.line.biz/en/reference/messaging-api/#get-coupons-list)</li><li>[Get details of a coupon (/v2/bot/coupon/{couponId})](https://developers.line.biz/en/reference/messaging-api/#get-coupon)</li><li>傳送 message type 設為 [Coupon message](https://developers.line.biz/en/docs/messaging-api/message-types/#coupon-messages) 的訊息</li></ul> |
| `crm%3Amanage`<br />(crm:manage) | 此 scope 僅能為使用 Chat Plugin 功能\*的模組頻道指定。否則請勿指定。<br />使用 Chat Plugin 時為必填。若使用 Chat Plugin 功能的模組頻道未指定此 scope，未來可能無法使用 Chat Plugin 所提供的功能。 |

\* Chat Plugin 功能目前僅提供給部分特定企業使用者使用。

### 2. About the linkage screen 

當 LINE 官方帳號管理者存取用於認證與授權的 URL 時，會顯示 LINE Official Account Manager 的連結畫面。連結畫面會顯示您在建立模組頻道時所申請的內容。您可以在 [LINE Developers Console](https://developers.line.biz/console/) 中確認這些設定。

![Linkage screen](https://developers.line.biz/media/partner-docs/attach-disp-en.png)

### 3. Receive the authorization code or error response 

當 LINE 官方帳號管理者完成認證與授權後，授權碼與錯誤碼會透過這些查詢參數，傳遞至認證與授權 URL 中所指定的重新導向 URL（`redirect_uri`）。在上述範例所呈現的[流程](https://developers.line.biz/en/docs/partner-docs/module-technical-attach-channel/#attach-flow)中，當在「OAM Confirm and Attach」畫面點擊 **Link** 按鈕時，授權碼與錯誤碼即會被傳遞。

#### Receiving the authorization code 

一旦 LINE 官方帳號管理者完成認證並完成授權，便會帶著這些查詢參數被重新導向至重新導向 URL（`redirect_uri`）。

##### Query Parameters 

<!-- parameter start -->

code

String

這是連結（attach）至 LINE 官方帳號所需的授權碼。此授權碼具有有效期間（validity period），且僅能使用一次。

<!-- parameter end -->
<!-- parameter start -->

state

String

防 CSRF 字串。請確認此字串與認證與授權 URL 的 `state` 查詢參數中所指定的內容相同。

<!-- parameter end -->

#### Receiving an error response 

若 LINE 官方帳號管理者的認證失敗，您會帶著這些查詢參數被重新導向至重新導向 URL（`redirect_uri`）。

##### Query Parameters 

<!-- parameter start -->

error

String

錯誤碼。

<!-- parameter end -->
<!-- parameter start -->

error_description

String

錯誤詳細資訊。

<!-- parameter end -->
<!-- parameter start -->

state

String

防 CSRF 字串。請確認此字串與認證與授權 URL 的 `state` 查詢參數中所指定的內容相同。

<!-- parameter end -->

### 4. Attach by operation of the module channel provider 

一旦您取得授權碼，並確認 `state` 查詢參數中所傳遞的字串無誤後，即可將模組頻道連結至 LINE 官方帳號。

詳情請參閱企業客戶選用功能 API 參考文件中的 [Attach by operation of the module channel provider](https://developers.line.biz/en/reference/partner-docs/#link-attach-by-operation-module-channel-provider)。
