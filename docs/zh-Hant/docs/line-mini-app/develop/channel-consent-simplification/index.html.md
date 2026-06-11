# LINE MINI App 授權流程（LINE MINI App authorization flow）

LIFF app 若要取得使用者資訊或向使用者傳送訊息，使用者必須在首次存取該 LIFF app 時，於頻道同意畫面（channel consent screen）上同意對應的權限。

在 LINE MINI App 中，透過「頻道同意簡化（Channel consent simplification）」功能，使用者只需要同意一次簡化即可。此後，當使用者首次存取另一個 LINE MINI App 時，會略過頻道同意畫面，讓使用者可以立即開始使用該 LINE MINI App。

本頁面說明「頻道同意簡化」功能，以及以此為基礎的授權流程。

<!-- table of contents -->

## What is the "Channel consent simplification" feature 

「頻道同意簡化」功能是一種機制，可簡化使用者首次存取 LINE MINI App 時所需的權限同意。一旦使用者同意了簡化，就視為他們也已對其他 LINE MINI App 所需的權限表示同意。此後使用者首次存取的 LINE MINI App（\*）會略過頻道同意畫面，讓他們可以立即開始使用該 LINE MINI App。

不過，根據 LY Corporation 的隱私權政策，「頻道同意簡化」功能唯一會略過同意的權限是取得[使用者 ID](https://developers.line.biz/en/glossary/#user-id)（`openid` scope）。取得使用者個人檔案資訊或傳送訊息所需的權限（例如 [`profile` scope 與 `chat_message.write` scope](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app)）並不包含在「頻道同意簡化」功能中。對於這些額外權限，會在需要該權限時於各個 LINE MINI App 內顯示驗證畫面（verification screen）。詳情請參閱[在驗證畫面上請求 openid scope 以外的權限](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

啟用「頻道同意簡化」功能可讓使用者更容易存取 LINE MINI App。為了改善使用者體驗，我們建議啟用「頻道同意簡化」功能。

對於在日本的新 LINE MINI App 頻道（channel），「頻道同意簡化」功能一律為啟用狀態。詳情請參閱 [2026 年 1 月 8 日](https://developers.line.biz/en/news/2026/01/08/channel-consent-simplification/)的消息。

\* 在[「頻道同意簡化」功能已停用的 LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#authorization-flow-disabled) 中，會顯示頻道同意畫面。

<!-- note start -->

**LINE MINI App 可能因其設計而無法如預期運作**

如果你的 LINE MINI App 設計為使用透過 LIFF SDK 取得的[存取權杖（access token）](https://developers.line.biz/en/glossary/#access-token)或 [ID 權杖（ID token）](https://developers.line.biz/en/glossary/#id-token)來呼叫 [LINE Login API](https://developers.line.biz/en/reference/line-login/)，「頻道同意簡化」功能可能會導致你的 LINE MINI App 行為與預期不同。

例如，如果你的 LINE MINI App 設計為呼叫 [Verify ID token](https://developers.line.biz/en/reference/line-login/#verify-id-token) 端點（endpoint），並使用取得的使用者[個人檔案資訊（profile information）](https://developers.line.biz/en/glossary/#profile-information)來為你的 LINE MINI App 建立服務帳號，那麼 ID 權杖的 payload 將不會包含使用者的個人檔案資訊，因為「頻道同意簡化」功能會略過取得使用者個人檔案資訊（`profile` scope）的同意。因此，你將無法使用使用者的個人檔案資訊來建立服務帳號。

為了避免這個問題，在取得存取權杖或 ID 權杖之前，請使用 [`liff.permission.query()`](https://developers.line.biz/en/reference/liff/#permission-query) 方法與 [`liff.permission.requestAll()`](https://developers.line.biz/en/reference/liff/#permission-request-all) 方法顯示驗證畫面，並向使用者請求所需的權限。詳情請參閱[在驗證畫面上請求 `openid` scope 以外的權限](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

<!-- note end -->

### The "Channel consent simplification" feature setup 

只有在符合以下所有條件時，才能設定「頻道同意簡化」功能：

- LINE MINI App 頻道的 **Region to provide the service** 設定為「Japan」。
- LINE MINI App 頻道的狀態為「Not yet reviewed」。

對於在 2026 年 1 月 8 日之前建立的 LINE MINI App 頻道，若要啟用「頻道同意簡化」功能，請在 [LINE Developers Console](https://developers.line.biz/console/) 中該 LINE MINI App 頻道的 **Web app settings** 分頁裡，開啟 Channel consent simplification 區段的切換開關。

![](https://developers.line.biz/media/line-mini-app/simplification-feature-setup-en.png)

請注意，由於「頻道同意簡化」功能會簡化取得使用者 ID（`openid` scope）的同意，啟用它也會自動在 Scope 區段中啟用 `openid`。

![](https://developers.line.biz/media/line-mini-app/simplification-scope-en.png)

對於在 2026 年 1 月 8 日當天或之後建立的 LINE MINI App 頻道，「頻道同意簡化」功能一律為啟用狀態。無需在 LINE Developers Console 中進行任何設定。

### Operating conditions for the "Channel consent simplification" feature 

為了讓「頻道同意簡化」功能運作，必須符合以下所有條件：

- LINE MINI App 為已驗證的 MINI App（\*）。
- LINE MINI App 的 LIFF SDK 版本為 v2.13.x 或更新版本。
- LINE MINI App 並非透過 [LIFF-to-LIFF transition](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff) 開啟。

\* 對於未驗證的 MINI App，此功能僅在 LINE MINI App for Developing 與 for Review 中運作。

## Authorization flow in LINE MINI Apps where the "Channel consent simplification" feature is enabled 

「頻道同意簡化」功能已啟用的 LINE MINI App 會以下列兩個步驟向使用者請求權限：

1. [在簡化同意畫面上請求取得使用者 ID（`openid` scope）的權限](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-openid)
1. [在驗證畫面上請求 `openid` scope 以外的權限](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)

### 1. Request permission to get the user ID (the `openid` scope) on the simplification consent screen 

當使用者首次存取「頻道同意簡化」功能已啟用的 LINE MINI App 時，會顯示簡化同意畫面。在簡化同意畫面上，會詢問使用者是否願意允許該 LINE MINI App 取得他們的使用者 ID（`openid` scope）。

![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/simplification-consent-screen-en.png)

當使用者點選 **Agree** 時，會顯示載入畫面，之後使用者即可開始使用該 LINE MINI App。

![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/loading-screen-en.png)

點選 **Agree** 後，也視為使用者已同意其他 LINE MINI App 取得他們的使用者 ID。此後，當使用者首次存取「頻道同意簡化」功能已啟用的 LINE MINI App 時，會略過頻道同意畫面，讓他們可以立即開始使用該 LINE MINI App。

<!-- tip start -->

**使用者點選「Not now」時的行為**

當使用者點選 **Not now** 時，會略過對簡化的同意。此後，即使使用者開啟「頻道同意簡化」功能已啟用的 LINE MINI App，也不會再顯示簡化同意畫面。略過後經過 24 小時，簡化同意畫面會再次顯示。

此外，在略過對簡化的同意期間，會為每個 LINE MINI App 顯示個別的頻道同意畫面，就如同[「頻道同意簡化」功能已停用的 LINE MINI App 的授權流程](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#authorization-flow-disabled)一樣。

<!-- tip end -->

### 2. Request permissions other than the `openid` scope on the verification screen 

當你執行需要 `openid` scope 以外權限的方法時，例如 [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 方法或 [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 方法，會顯示驗證畫面。在驗證畫面上，會顯示該 LINE MINI App 所請求的額外權限，並詢問使用者是否願意授予這些權限。

![](https://developers.line.biz/media/line-mini-app/line-mini-app-playground-verification-screen-en.png)

以下方法需要 `openid` scope 以外的權限：

| Scope | Method |
| --- | --- |
| `email` | <ul><li>[`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token)</li><li>[`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token)</li></ul> |
| `profile` | <ul><li>[`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile)</li><li>[`liff.getFriendship()`](https://developers.line.biz/en/reference/liff/#get-friendship)</li></ul> |
| `chat_message.write` | <ul><li>[`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages)</li></ul> |

你可以使用 [`liff.permission.query()`](https://developers.line.biz/en/reference/liff/#permission-query) 方法與 [`liff.permission.requestAll()`](https://developers.line.biz/en/reference/liff/#permission-request-all) 方法，隨時顯示驗證畫面。

```javascript
liff.permission.query("profile").then((permissionStatus) => {
  if (permissionStatus.state === "prompt") {
    liff.permission.requestAll();
  }
});
```

詳情請參閱 LIFF API 參考文件中的 [`liff.permission.query()`](https://developers.line.biz/en/reference/liff/#permission-query) 與 [`liff.permission.requestAll()`](https://developers.line.biz/en/reference/liff/#permission-request-all)。

<!-- tip start -->

**「驗證畫面」何時顯示**

「驗證畫面」首次顯示的時機並非使用者首次開啟 LINE MINI App 時，而是當需要 `openid` scope 以外的 scope 權限（例如 [`profile` scope 或 `chat_message.write` scope](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app) 等）時。

因此，如果你將 LINE MINI App 設計為在啟動後立即執行需要 `openid` scope 以外權限的請求（例如 [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 方法），那麼當使用者存取你的 LINE MINI App 時，看起來就會像是頻道同意畫面未被略過而直接顯示。我們建議盡可能將你的 LINE MINI App 實作為：只有在實際需要時，才執行需要 `openid` scope 以外權限的請求。

<!-- tip end -->

### Important points about using the "Channel consent simplification" feature together with the add friend option 

在 LINE MINI App 中，你可以使用[加入好友選項（add friend option）](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/#link-a-line-official-account-with-your-channel)，從驗證畫面或頻道同意畫面提示使用者加入你的 LINE 官方帳號。

![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/add-friend-option-verification-screen-en.png) ![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/add-friend-option-channel-consent-screen-en.png)

不過，如果你的 LINE MINI App 頻道 **Web app settings** 分頁的 Scope 區段中只指定了 `openid`，啟用「頻道同意簡化」功能將會使驗證畫面與頻道同意畫面都不顯示。因此，你將無法使用加入好友選項來提示使用者加入好友。

若要同時使用「頻道同意簡化」功能與加入好友選項，我們建議在你的 LINE MINI App 頻道 **Web app settings** 分頁的 Scope 區段中指定 `openid` 以外的 scope，並顯示驗證畫面。詳情請參閱[在驗證畫面上請求 openid scope 以外的權限](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#request-permissions-other-than-openid)。

你也可以使用 [`liff.requestFriendship()`](https://developers.line.biz/en/reference/liff/#request-friendship) 方法，隨時顯示子視窗，提示使用者將你的 LINE 官方帳號加為好友或解除封鎖。

## Authorization flow in LINE MINI Apps where the "Channel consent simplification" feature is disabled 

當使用者首次存取「頻道同意簡化」功能已停用的 LINE MINI App 時，會顯示頻道同意畫面。在頻道同意畫面上，會顯示該 LINE MINI App 所請求的權限清單，並詢問使用者是否願意授予這些權限。

當使用者點選 **Allow** 時，即可開始使用該 LINE MINI App。

![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/line-mini-app-playground-channel-consent-screen-en.png)

## Differences in behavior based on whether users have consented to the simplification 

如果使用者已在簡化同意畫面上同意了簡化，當他們首次存取「頻道同意簡化」功能已啟用的 LINE MINI App 時，會略過頻道同意畫面，並在顯示載入畫面後讓使用者立即開始使用該 LINE MINI App。

另一方面，如果使用者尚未在簡化同意畫面上同意簡化，那麼當他們首次存取 LINE MINI App 時，無論該 LINE MINI App 是否啟用「頻道同意簡化」功能，都會顯示頻道同意畫面。

下表顯示使用者首次存取 LINE MINI App 時，依其是否已同意簡化而產生的行為差異：

| LINE MINI App | Users have consented to the simplification | Users haven't consented to the simplification |
| --- | --- | --- |
| 「頻道同意簡化」功能已啟用的 LINE MINI App | ![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/difference-between-consent-and-no-consent-consent-en.png)<br>會略過頻道同意畫面。 | ![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/difference-between-consent-and-no-consent-no-consent-en.png)<br>會顯示頻道同意畫面。 |
| 「頻道同意簡化」功能已停用的 LINE MINI App | ![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/difference-between-consent-and-no-consent-no-consent-en.png)<br>會顯示頻道同意畫面。 | ![](https://developers.line.biz/media/line-mini-app/channel-consent-simplification/difference-between-consent-and-no-consent-no-consent-en.png)<br>會顯示頻道同意畫面。 |
