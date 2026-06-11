# 停止使用 Messaging API

<!-- tip start -->

**停止使用您的 LINE 官方帳號**

如果您想停止使用與 Messaging API 頻道連動的 LINE 官方帳號，請參閱[停止使用您的 LINE 官方帳號](https://developers.line.biz/en/docs/messaging-api/stop-using-line-official-account/)。

<!-- tip end -->

如果您想繼續使用與 Messaging API 頻道（channel）連動的 LINE 官方帳號，但想停止使用 Messaging API，我們建議您執行以下操作。請注意，您無法在保留與 Messaging API 頻道連動的 LINE 官方帳號的情況下，只刪除 Messaging API 頻道。

<!-- table of contents -->

## Stop using webhooks 

1. 在 [LINE Developers Console](https://developers.line.biz/console/) 上選取您想停止使用的 Messaging API 頻道。
1. 點選 **Messaging API** 分頁。
1. 在 **Webhook settings** 區段中停用 **Use webhook**。

![Use webhook in the Webhook settings section](https://developers.line.biz/media/messaging-api/stop-using-messaging-api/disable-use-webhook-en.png)

## Revoke channel access tokens 

撤銷頻道存取權杖（channel access token）的端點（endpoint）會因頻道存取權杖的類型而有所不同。請使用對應於您所使用之頻道存取權杖的端點來撤銷頻道存取權杖。請注意，[無狀態頻道存取權杖（stateless channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)無法被撤銷。

- [Revoke channel access token v2.1](https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token-v2-1) 端點
- [Revoke short-lived or long-lived channel access token](https://developers.line.biz/en/reference/messaging-api/#revoke-longlived-or-shortlived-channel-access-token) 端點

## Display after stopping use of the Messaging API 

您可以透過上述步驟停用 webhook 並撤銷頻道存取權杖，以停止使用 Messaging API。

然而，即使您透過這些步驟停止使用 Messaging API，Messaging API 頻道本身仍然存在。因此，當您在 LINE Developers Console 中查看頻道清單時，您已停止使用的頻道與其他正在使用中的 Messaging API 頻道之間，在外觀上不會有任何差異。

此外，當您在 LINE 官方帳號管理介面（LINE Official Account Manager）的設定畫面中選取 **Messaging API** 時，狀態仍會維持為 **Enabled**。
