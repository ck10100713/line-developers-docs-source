# Channel access token（頻道存取權杖）

頻道存取權杖（channel access token）是一串不透明的字串，用來驗證嘗試使用[頻道（channel）](https://developers.line.biz/en/glossary/#channel)的應用程式是否擁有使用該頻道的權限。有了頻道存取權杖，你就能使用 [LINE Platform](https://developers.line.biz/en/glossary/#line-platform) 提供的眾多實用功能，例如 Messaging API。

在本頁中，你將學到頻道存取權杖的基礎知識，例如概觀與類型。讀完本頁後，你將更容易運用 LINE Platform 的各項功能進行開發。

<!-- table of contents -->

## What is a channel 

首先，簡單說明什麼是頻道。頻道是用來存取 LINE Platform 所提供功能的通訊路徑。舉例來說，有以下幾種頻道：

- Messaging API 頻道
- LINE Login 頻道
- LINE MINI App 頻道

舉例來說，當應用程式使用 Messaging API 頻道時，會用頻道存取權杖來驗證使用者是否被授權使用該頻道。

![Channel](https://developers.line.biz/media/basics/channel.png)

## Why use channel access tokens 

為什麼要使用頻道存取權杖呢？在某些系統中，驗證使用者是否被授權最常見的方式是使用帳號（ID）與密碼，這種情況下，應用程式在使用頻道時就要輸入帳號與密碼。

然而一般來說，在提供服務的過程中，頻道會被使用許多次。由於要求頻道使用者在每次應用程式使用頻道時都輸入帳號與密碼並不實際，因此改用頻道存取權杖。頻道存取權杖讓頻道使用者不必輸入帳號與密碼就能使用頻道。

![Channel access token](https://developers.line.biz/media/basics/channel-access-token.png)

<!-- note start -->

**撤銷任何疑似遭洩漏的頻道存取權杖**

頻道存取權杖用來驗證應用程式是否被授權使用頻道。這表示若頻道存取權杖遭到洩漏，頻道就可能被非預期的第三方使用。因此，若你懷疑頻道存取權杖已遭洩漏，請將其撤銷。詳情請參閱[撤銷任何疑似遭洩漏的頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#revoke-channel-access-token)。

<!-- note end -->

## Types of channel access tokens 

頻道存取權杖有四種類型。這些頻道存取權杖在有效期間，以及每個頻道可發行的權杖數量上各有不同。

| 類型 | 有效期間 | 每個頻道可發行數量 |
| --- | --- | --- |
| 使用者指定到期時間的頻道存取權杖 | 最長 30 天 | 30 |
| 無狀態（stateless）頻道存取權杖 | 15 分鐘 | 無上限 |
| 短期（short-lived）頻道存取權杖 | 30 天 | 30 |
| 長期（long-lived）頻道存取權杖 | 無限期 | 1 |

頻道存取權杖的發行數量是依各類型分別計算的。因此，即使已發行 30 個使用者指定到期時間的頻道存取權杖，仍可再發行 30 個短期頻道存取權杖。已過期的頻道存取權杖不會被計入發行數量。

<!-- tip start -->

**在有效期間內可重複使用**

同一個頻道存取權杖在其有效期間內可以多次使用。詳情請參閱[在有效期間內可重複使用](https://developers.line.biz/en/docs/basics/channel-access-token/#use-repeatedly)。

<!-- tip end -->

此外，你可使用的頻道存取權杖類型會依產品與功能而有所不同。例如，長期頻道存取權杖僅適用於 Messaging API 頻道。請參閱各產品的文件，以了解每個產品可使用哪些頻道存取權杖。

以下各節將分別說明各種頻道存取權杖：

- [使用者指定到期時間的頻道存取權杖（Channel access token v2.1）](https://developers.line.biz/en/docs/basics/channel-access-token/#user-specified-expiration)
- [無狀態頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#stateless-channel-access-token)
- [短期頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#short-lived-channel-access-token)
- [長期頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token)

### Channel access token with a user-specified expiration (Channel access token v2.1) 

Channel access token v2.1 讓開發者可設定最長 30 天的有效期間。此外，也可透過使用 JSON Web Token（JWT）來產生頻道存取權杖，以強化安全性。

每個頻道最多可發行 30 個 channel access token v2.1。任何超過可發行數量的嘗試都會導致發行請求被拒絕。關於 channel access token v2.1 的詳情，請參閱 Messaging API 文件中的[發行 channel access token v2.1](https://developers.line.biz/en/docs/messaging-api/generate-json-web-token/)。

### Stateless channel access token 

無狀態頻道權杖是僅在 15 分鐘內有效的頻道存取權杖。可發行的無狀態頻道存取權杖數量沒有上限。無狀態頻道存取權杖一旦發行，便無法撤銷。

關於發行無狀態存取權杖的詳情，請參閱 Messaging API 參考文件中的[發行無狀態頻道存取權杖](https://developers.line.biz/en/reference/messaging-api/#issue-stateless-channel-access-token)。

### Short-lived channel access token 

短期頻道存取權杖是有效期間為 30 天的頻道存取權杖。每個頻道最多可發行 30 個。若發行數量超過上限，最舊的頻道存取權杖將被撤銷。

關於發行短期頻道存取權杖的詳情，請參閱 Messaging API 參考文件中的[發行短期頻道存取權杖](https://developers.line.biz/en/reference/messaging-api/#issue-shortlived-channel-access-token)。

### Long-lived channel access token 

長期頻道存取權杖是不會過期、且僅能透過 Messaging API 頻道發行的頻道存取權杖。你可隨時從 [LINE Developers Console](https://developers.line.biz/console/) 中 Messaging API 頻道的 **Messaging API** 分頁發行此權杖。你也可以隨時撤銷這些權杖。

重新發行長期頻道存取權杖會使目前有效的長期頻道存取權杖失效。重新發行時，你也可將目前有效的長期頻道存取權杖的有效期間最多延長 24 小時。

## Example of channel access token operation 

頻道存取權杖的設計用意是為每個開發團隊或使用者群組分別發行。例如，開發團隊 A 與開發團隊 B 會取得不同的頻道存取權杖。如此一來，若開發團隊 A 的頻道存取權杖疑似遭洩漏，或開發團隊 A 因自身原因需要重新發行頻道存取權杖，開發團隊 B 都不會受到影響。

此外，如下圖所示，為確保服務不中斷，每個開發團隊或使用者群組最多可發行兩個頻道存取權杖。

![Example of channel access token operation](https://developers.line.biz/media/basics/operate-channel-access-token.png)

## Checklist 

使用頻道存取權杖時，請注意以下事項：

- [在有效期間內可重複使用](https://developers.line.biz/en/docs/basics/channel-access-token/#use-repeatedly)
- [撤銷任何疑似遭洩漏的頻道存取權杖](https://developers.line.biz/en/docs/basics/channel-access-token/#revoke-channel-access-token)

### Can be used repeatedly within the validity period 

同一個頻道存取權杖在其有效期間內可以多次使用。基於此，對於 channel access token v2.1 與短期頻道存取權杖，請勿在每次使用頻道時都重新發行頻道存取權杖。若在短時間內發行大量頻道存取權杖，且判定此舉會影響 LINE Platform 的運作，發行可能會被暫時限制。請注意，無狀態頻道存取權杖的設計本就是在每次使用頻道時發行。

此外，若你使用有效期間已過期的頻道存取權杖，將因無法驗證你的頻道授權而無法使用該頻道。建議你建立一套機制，在頻道存取權杖過期前自動發行新的權杖。

### Revoke any channel access tokens suspected of being compromised 

頻道存取權杖用來驗證頻道權限。這表示若頻道存取權杖遭到洩漏，頻道就有可能被非預期的第三方使用。

舉例來說，以 Messaging API 為例，有一項稱為「群發訊息（Broadcast message）」的功能，可將同一則訊息發送給所有與 LINE 官方帳號為好友的使用者。若頻道存取權杖遭洩漏，第三方便可發送群發訊息，導致惡意訊息被發送給所有好友。

因此，若你懷疑可撤銷的頻道存取權杖已遭洩漏，請將其撤銷。關於撤銷頻道存取權杖的詳情，請參閱以下參考文件：

- [撤銷 channel access token v2.1](https://developers.line.biz/en/reference/messaging-api/#revoke-channel-access-token-v2-1)
- [撤銷短期或長期頻道存取權杖](https://developers.line.biz/en/reference/messaging-api/#revoke-longlived-or-shortlived-channel-access-token)
