# 取得使用者個人資料資訊的同意（Consent on getting user profile information）

若要透過 [LINE 官方帳號](https://developers.line.biz/en/glossary/#line-official-account)存取使用者的[個人資料資訊（profile information）](https://developers.line.biz/en/glossary/#profile-information)，使用者必須同意允許存取其個人資料資訊。

## Users of LINE for iOS and LINE for Android 

在 LINE for iOS 與 LINE for Android 上，使用者於開始使用 LINE 時就會同意允許存取其個人資料資訊。舉例來說，這裡的「使用者」包含以下情況的人：

- 在 LINE for iOS 或 LINE for Android 上建立 LINE 帳號，且仍在使用該帳號者
- 原本在 LINE for PC 上建立 LINE 帳號，但改在 LINE for iOS 或 LINE for Android 上使用其帳號者

## Users who aren't using LINE for iOS or LINE for Android 

從未使用過 LINE for iOS 或 LINE for Android 的使用者，無法同意允許存取其個人資料資訊。舉例來說，這些是在 LINE for PC 上建立 LINE 帳號，且持續只使用 LINE for PC 的使用者。這些使用者仍可將您的 LINE 官方帳號加為好友，甚至邀請它加入聊天。

<!-- note start -->

**Note**

自 2020 年 4 月起，您無法在 LINE for PC 上建立帳號。

<!-- note end -->

若使用者未同意允許存取其個人資料資訊，則該使用者的個人資料資訊不會包含在以下這些 Webhook 事件物件與端點（endpoint）回應中。此外，也不會傳送 Webhook [membership event](https://developers.line.biz/en/reference/messaging-api/#membership-event)。

- [Webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)的[來源使用者（source user）](https://developers.line.biz/en/reference/messaging-api/#source-user)
- [文字訊息物件（text message object）](https://developers.line.biz/en/reference/messaging-api/#wh-text)的 `mention` 物件
- [取得將您的 LINE 官方帳號加為好友的使用者清單](https://developers.line.biz/en/reference/messaging-api/#get-follower-ids)端點
- [取得已加入會員的使用者清單](https://developers.line.biz/en/reference/messaging-api/#get-membership-user-ids)端點
- [取得群組聊天成員使用者 ID](https://developers.line.biz/en/reference/messaging-api/#get-group-member-user-ids)端點
- [取得多人聊天成員使用者 ID](https://developers.line.biz/en/reference/messaging-api/#get-room-member-user-ids)端點

<!-- tip start -->

**如果您無法取得使用者個人資料資訊**

無法取得使用者個人資料資訊的可能原因，可能出在使用者本身，因為他們：

- 未同意允許存取其個人資料資訊
- 未將您的 LINE 官方帳號加為好友
- 在將您的 LINE 官方帳號加為好友後將其封鎖
- 將您的 LINE 官方帳號從群組聊天或多人聊天中移除
- 離開了您的 LINE 官方帳號所在的群組聊天或多人聊天

<!-- tip end -->
