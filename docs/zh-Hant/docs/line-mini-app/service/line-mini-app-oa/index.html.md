# 使用 LINE 官方帳號（Use LINE Official Account）

本頁說明如何運用 LINE 官方帳號（LINE Official Account）來推廣你的 LINE MINI App。如需更多關於如何建立 LINE 官方帳號的資訊，請參閱 Messaging API 文件中的 [Create a LINE Official Account](https://developers.line.biz/en/docs/messaging-api/getting-started/#create-oa)。

![Promote your LINE MINI App on LINE Official Account](https://developers.line.biz/media/line-mini-app/mini_with_oa.png)

## Send rich messages 

傳送具有視覺吸引力的圖文訊息（rich message），有助於使用者快速理解你的 LINE MINI App 的價值，並鼓勵更多使用者前來使用。

如需更多關於圖文訊息的資訊，請參閱 LINE for Business 中的 [Rich messages](https://www.lycbiz.com/jp/manual/OfficialAccountManager/rich-messages/)（僅提供日文版）。

## Set a link to your LINE MINI App in a rich menu 

在圖文選單（rich menu）中設定你的 LINE MINI App 的 [LIFF URL](https://developers.line.biz/en/glossary/#liff-url) 或[永久連結（permanent link）](https://developers.line.biz/en/glossary/#permanent-link-liff)後，使用者就能從 LINE 官方帳號的聊天畫面輕鬆存取你的 LINE MINI App。

如需更多關於圖文選單的資訊，請參閱 Messaging API 文件中的 [Rich menus overview](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/)。

## Add the LINE Official Account as a friend on the LINE MINI App 

你可以使用下列任一功能，鼓勵使用者在 LINE MINI App 上將你的 LINE 官方帳號加為好友：

- [加好友選項（Add friend option）](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/#link-a-line-official-account-with-your-channel)
- [`liff.requestFriendship()` 方法](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/#use-liff-request-friendship)

### Add friend option 

你可以在 LINE MINI App 的[驗證畫面（verification screen）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#verification-screen)或[頻道同意畫面（channel consent screen）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)上，顯示將你的 LINE 官方帳號加為好友的選項。這稱為加好友選項（add friend option）。

若要使用加好友選項將 LINE MINI App 與 LINE 官方帳號連結，必須符合下列所有條件：

- 該 LINE 官方帳號使用 Messaging API（\*1）。
- 與該 LINE 官方帳號連結的 Messaging API 頻道（channel）和 LINE MINI App 頻道屬於同一個供應商（provider）。
- 用於執行此操作的帳號同時具有 LINE MINI App 頻道的 Admin 角色（\*2）以及 LINE 官方帳號的 Administrator 角色（\*3）。

\*1 如需更多關於如何在 LINE 官方帳號上使用 Messaging API 的資訊，請參閱 Messaging API 文件中的 [Enable the Messaging API for your LINE Official Account](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager)。\
\*2 你可以在 [LINE Developers Console](https://developers.line.biz/console/) 中查看 LINE MINI App 頻道的 Admin 角色。\
\*3 你可以在 [LINE Official Account Manager](https://manager.line.biz) 中查看 LINE 官方帳號的 Administrator 角色。

#### How to set the add friend option 

1. 在 [LINE Developers Console](https://developers.line.biz/console/) 中，點選 LINE MINI App 頻道的 **Basic settings** 分頁。
1. 在「Linked LINE Official Account」區段中，點選 **Edit**。
1. 選擇要與 LINE MINI App 頻道連結的 LINE 官方帳號，然後點選 **Update**。
1. 點選 LINE MINI App 頻道的 **Web app settings** 分頁。
1. 在「Add friend option」區段中，點選 **Edit**。
1. 選擇 **On (normal)**，然後點選 **Update**。

<!-- tip start -->

**對於認證供應商，授權畫面上的加好友選項預設為啟用**

如果 LINE MINI App 頻道屬於[認證供應商（certified provider）](https://developers.line.biz/en/docs/line-developers-console/overview/#certified-provider)，驗證畫面與頻道同意畫面上的加好友選項預設為啟用。

除非使用者手動關閉此選項，否則當使用者在驗證畫面或頻道同意畫面上授予授權時，為加好友選項指定的 LINE 官方帳號將會被加為好友。

<!-- tip end -->

#### Important points about using the "Channel consent simplification" feature concurrently 

如果你同時使用「[Channel consent simplification](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#what-is-channel-consent-simplification)」功能（\*）與加好友選項，驗證畫面與頻道同意畫面可能不會顯示。

如需更多資訊，請參閱 [Important points about using the "Channel consent simplification" feature together with the add friend option](https://developers.line.biz/en/docs/line-mini-app/develop/channel-consent-simplification/#add-friend-option)。

\* 對於日本的新 LINE MINI App 頻道，[自 2026 年 1 月 8 日起，使用「Channel consent simplification」功能已成為強制規定](https://developers.line.biz/en/news/2026/01/08/channel-consent-simplification/)。

### `liff.requestFriendship()` method 

透過呼叫 [`liff.requestFriendship()`](https://developers.line.biz/en/reference/liff/#request-friendship) 方法，你可以顯示一個子視窗，提示使用者將你的 LINE 官方帳號加為好友或解除封鎖。

如需更多資訊，請參閱 LIFF 文件中的 [Requesting the user to add the LINE Official Account as a friend or unblock it](https://developers.line.biz/en/docs/liff/developing-liff-apps/#request-friendship)。
