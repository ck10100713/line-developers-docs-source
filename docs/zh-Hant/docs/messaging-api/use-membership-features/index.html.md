# 使用會員功能（Use membership features）

[會員（Membership）](https://www.lycbiz.com/jp/service/line-official-account/Membership/)（僅提供日文版）是 LINE 官方帳號可使用的每月會員訂閱功能。使用者可以訂閱您 LINE 官方帳號的會員方案，以獲得專屬的會員優惠。

## Endpoint for getting membership information 

透過 Messaging API，您可以使用下列端點（endpoint）取得會員資訊：

- [取得使用者的會員訂閱狀態](https://developers.line.biz/en/docs/messaging-api/use-membership-features/#get-a-users-membership-subscription-status)
- [取得已加入會員的使用者清單](https://developers.line.biz/en/docs/messaging-api/use-membership-features/#get-membership-user-ids)
- [取得目前提供的會員方案](https://developers.line.biz/en/docs/messaging-api/use-membership-features/#get-membership-plans)

<!-- tip start -->

**如何開始會員功能**

您可以在 [LINE Official Account Manager](https://manager.line.biz/) 上設定並發布您的會員功能。如需更多資訊，請參閱 LINE for Business 中的[在 LINE 上輕鬆建立訂閱服務！LINE 官方帳號的「會員」功能是什麼？](https://www.lycbiz.com/jp/column/line-official-account/service-information/membership/)（僅提供日文版）。

目前會員功能僅適用於日本的 LINE 官方帳號。

<!-- tip end -->

### Get a user's membership subscription status 

此端點可讓您取得由使用者 ID 指定的使用者所訂閱的會員資訊。如需更多資訊，請參閱 Messaging API 參考文件中的 [Get a user's membership subscription status](https://developers.line.biz/en/reference/messaging-api/#get-a-users-membership-subscription-status)。

### Get a list of users who have joined the membership 

此端點可讓您取得已加入您 LINE 官方帳號會員的使用者 ID 清單。如需更多資訊，請參閱 Messaging API 參考文件中的 [Get a list of users who have joined the membership](https://developers.line.biz/en/reference/messaging-api/#get-membership-user-ids)。

### Get membership plans being offered 

此端點可讓您取得目前透過您 LINE 官方帳號會員所提供的會員方案。如需更多資訊，請參閱 Messaging API 參考文件中的 [Get membership plans being offered](https://developers.line.biz/en/reference/messaging-api/#get-membership-plans)。

## Webhook membership event 

當使用者加入、續訂或退出您 LINE 官方帳號的會員時，會發送 Webhook 會員事件。如需更多資訊，請參閱 Messaging API 參考文件中的 [Membership event](https://developers.line.biz/en/reference/messaging-api/#membership-event)。
