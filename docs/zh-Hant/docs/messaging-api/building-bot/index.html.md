# 建置機器人（Build a bot）

本指南說明如何使用 Messaging API 來建置 LINE 機器人。

## Before you begin 

在開始設定與建置機器人之前，請先確認你已具備：

- 一個專屬於你機器人的 [Messaging API 頻道（Messaging API channel）](https://developers.line.biz/en/docs/messaging-api/getting-started/)
- 一台用來託管機器人的伺服器

## Settings on LINE Developers Console 

請準備一組[頻道存取權杖（channel access token）](https://developers.line.biz/en/docs/messaging-api/building-bot/#issue-a-channel-access-token)並設定 [webhook URL](https://developers.line.biz/en/docs/messaging-api/building-bot/#setting-webhook-url)。權杖是機器人呼叫 Messaging API 所必需的。webhook URL 則是機器人從 LINE Platform 接收 webhook payload 所必需的。完成設定後，請[將你的 LINE 官方帳號加為好友](https://developers.line.biz/en/docs/messaging-api/building-bot/#add-your-line-official-account-as-friend)以便進行[驗證](https://developers.line.biz/en/docs/messaging-api/building-bot/#confirm-webhook-behavior)。

### Prepare a channel access token 

如果你還沒有頻道存取權杖，請先發行一組。頻道存取權杖是用於 Messaging API 的存取權杖。你可以發行以下任一種權杖：

- [可由使用者指定有效期間的頻道存取權杖（Channel access token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)（建議使用）
- [無狀態頻道存取權杖（Stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)
- [短效頻道存取權杖（Short-lived channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)
- [長效頻道存取權杖（Long-lived channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)

### Set a webhook URL 

webhook URL 是你機器人伺服器的端點（endpoint），LINE Platform 會將 webhook payload 傳送到這個位置。webhook URL 只能設定一個機器人伺服器端點。

請依照以下步驟設定 webhook URL：

1. 登入 [LINE Developers Console](https://developers.line.biz/console/)，並點選該 Messaging API 頻道所屬的供應商（provider）。
1. 點選該 Messaging API 頻道。
1. 點選 **Messaging API** 分頁。
1. 在 **Webhook URL** 下方點選 **Edit**。輸入 webhook URL（LINE Platform 要傳送事件的目的地），然後點選 **Update**。

   webhook URL 必須使用 HTTPS，並且要有由一般網頁瀏覽器廣泛信任的憑證授權單位所核發的 SSL/TLS 憑證。不允許使用自簽憑證。如果你遇到與 SSL/TLS 設定相關的問題，請檢查你的 SSL/TLS 憑證鏈是否完整，以及中繼憑證是否已正確安裝在你的伺服器上。

1. 點選 **Verify**。如果 webhook URL 確實接受請求，你會看到 **Success**。
1. 啟用 **Use webhook**。

![](https://developers.line.biz/media/messaging-api/build-bot/webhook-url-example-com.png)

### Add your LINE Official Account as a friend 

將與該 Messaging API 頻道關聯的 LINE 官方帳號加為你 LINE 帳號的好友，以便稍後進行測試。一個簡便的加入方式是掃描 [LINE Developers Console](https://developers.line.biz/console/) 中 **Messaging API** 分頁上的 QR code。

### Restrict who can call the API when using a long-lived channel access token (optional) 

使用長效頻道存取權杖時，你可以依 IP 位址限制哪些伺服器可以呼叫 LINE Platform API。

若要登錄 IP 位址，請前往 [LINE Developers Console](https://developers.line.biz/console/)，開啟頻道設定並切換到 **Security** 分頁。你可以逐一登錄 IP 位址，或使用無類別域間路由（CIDR）標記法登錄你的網路位址。

我們建議你在 Messaging API 中使用[可由使用者指定有效期間的頻道存取權杖（Channel access token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)。

![](https://developers.line.biz/media/messaging-api/build-bot/security-settings-input-en.png)

## Verify that webhook works 

當使用者將你的 LINE 官方帳號加為好友，或向你的 LINE 官方帳號傳送訊息時，LINE Platform 會向你的機器人伺服器傳送一個 HTTP POST 請求。此請求的目的地就是你在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Messaging API** 分頁中所登錄的 **Webhook URL**。該請求包含一個 webhook 事件物件，並在標頭中帶有簽章。

本節說明如何檢查你的伺服器是否能夠[接收 webhook 事件](https://developers.line.biz/en/docs/messaging-api/building-bot/#receive-webhook-events)。

### Receive webhook events 

若要檢查你的機器人伺服器是否確實接收到 webhook 事件，請先封鎖你在[先前步驟](https://developers.line.biz/en/docs/messaging-api/building-bot/#set-up-bot-on-line-developers-console)中加入的 LINE 官方帳號。接著，在你的伺服器日誌中找出機器人伺服器收到來自 LINE Platform 的 [unfollow event](https://developers.line.biz/en/reference/messaging-api/#unfollow-event)。以下是一段範例日誌。

```sh
2017-07-21T09:18:46.755256+00:00 app[web.1]: 2017-07-21 09:18:46.737  INFO 4 --- [io-13386-exec-2] c.e.bot.spring.KitchenSinkController     : unfollowed this bot: UnfollowEvent(source=UserSource(userId=Uxxxxxxxxxx...), timestamp=2017-07-21T09:18:46.031Z)
```

如果你得到類似的日誌，表示你的機器人伺服器確實收到了來自 LINE Platform 的 webhook 事件。檢查完日誌後，別忘了將該 LINE 官方帳號解除封鎖。

## Settings on LINE Official Account Manager 

[LINE Official Account Manager](https://manager.line.biz/) 是用來管理你 LINE 官方帳號的工具。除了使用 Messaging API 所提供的功能之外，你還可以透過[自訂你的商業檔案](https://developers.line.biz/en/docs/messaging-api/building-bot/#customize-profile)、建立 LINE VOOM 貼文等方式來改善使用者體驗。

如需 LINE 官方帳號可用功能的完整清單，請參閱 [LY for Business](https://www.lycbiz.jp/en/)。

<!-- tip start -->

**問候訊息與自動回覆訊息（Greeting messages and auto-reply messages）**

如果在頻道的 **Messaging API Settings** 分頁中將 **Greeting messages** 與 **Auto-reply messages** 設定為 **Enabled**，當使用者將你的 LINE 官方帳號加為好友或向你傳送訊息時，LINE 官方帳號將會自動回應。當頻道建立時，**Greeting Message** 與 **Auto-reply messages** 的預設設定為 **Enabled**。

如果你不希望自動傳送問候與回覆訊息（因為回應流程是由 Messaging API 處理），請在 [LINE Official Account Manager](https://manager.line.biz/) 中將 **Greeting Messages** 與 **Auto-reply messages** 設定為 **Disabled**。

你也可以兩者並用，例如以問候訊息回應使用者將你的 LINE 官方帳號加為好友，並以 Messaging API 處理其他回應。但你可能會難以分辨某個自動回應是來自問候訊息或回覆訊息，還是來自使用 Messaging API 的機器人。為避免混淆，我們建議你將 **Greeting messages** 與 **Auto-reply messages** 設定為 **Disabled**，尤其是當你第一次建立 LINE 機器人時。

<!-- tip end -->

### Customize your business profile 

商業檔案（business profile）是你輸入並設定 LINE 官方帳號基本資訊、並顯示給使用者的地方。你可以自訂檔案相片、封面相片、按鈕與外掛程式。若要設定你的檔案，請前往 LINE Official Account Manager。

如需更多關於檔案自訂的資訊，請參閱 LINE for Business 中的 [Profile](https://www.lycbiz.com/jp/manual/OfficialAccountManager/profile/)（僅提供日文版）。

### Set a greeting message (optional) 

當使用者第一次將你的 LINE 官方帳號加為好友時，你可以傳送一則問候訊息。若要設定問候訊息，請在 [LINE Developers Console](https://developers.line.biz/console/) 開啟頻道設定並點選 **Messaging API** 分頁。在 **Greeting messages** 下方點選 **Edit**。這會開啟 LINE Official Account Manager，請在那裡設定問候訊息。或者，你也可以透過程式化方式達成，亦即在收到 [follow event](https://developers.line.biz/en/reference/messaging-api/#follow-event) 後回應使用者。

### Set auto reply messages (optional) 

當使用者向你的 LINE 官方帳號傳送訊息時，你可以向他們傳送自動回覆訊息。若要設定自動回覆訊息，請在 [LINE Developers Console](https://developers.line.biz/console/) 開啟頻道設定並點選 **Messaging API** 分頁。在 **Auto-reply messages** 下方點選 **Edit**。這會開啟 LINE Official Account Manager，請在那裡設定自動回覆訊息。不過，使用 Messaging API 你能做的更多，因為你可以撰寫程式讓機器人針對各種 webhook 事件以不同方式回覆。

## Next steps 

設定好機器人後，你的 LINE 官方帳號便可以接收來自使用者的訊息，並向使用者傳送訊息。你也可以使用圖文選單（rich menu）與快速回覆（quick reply）來打造個人化的體驗。如需更多關於 Messaging API 可用功能的資訊，請參閱 [Messaging API documentation](https://developers.line.biz/en/docs/messaging-api/)。
