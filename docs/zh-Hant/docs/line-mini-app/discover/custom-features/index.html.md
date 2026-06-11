# 自訂功能（Custom features）

您可以為您的 LINE MINI App 加上以下功能，以進一步提升使用者體驗。可使用的功能取決於該 LINE MINI App 是未驗證的 MINI App，還是已驗證的 MINI App。

| 功能 | 未驗證的 MINI App | 已驗證的 MINI App |
| --- | --- | --- |
| [Service messages](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#service-messages) | ❌ | ✅ |
| [Custom Path](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#custom-path) | ❌ | ✅ |
| [將您的 LINE MINI App 捷徑加入使用者裝置的主畫面](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#create-shortcut-on-home-screen) | ❌ | ✅ |
| [Common Profile Quick-fill](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#quick-fill) | ❌ | ✅ |
| [引導使用者將您的官方帳號（Official Account）加為好友](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#OA-friend) | ✅ | ✅ |
| [自訂動作按鈕（custom action button）](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#custom-action-button) | ✅ | ✅ |
| [使用付款系統](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#using-payment-systems) | ✅ | ✅ |
| [刊登廣告](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/#place-ads) | ✅ | ✅ |

## Service messages 

若您想向使用者傳送餐廳或住宿訂位的確認資訊，可使用 Service messages。

Service messages 是一項由 LINE MINI App 通知使用者其應知悉之相關請求資訊的功能。

無論 LINE MINI App 屬於哪種類型，從 LINE MINI App 傳送的 Service messages 都會顯示在依各個提供 LINE MINI App 的地區所決定的聊天室中。

| Japan | Thailand | Taiwan |
| :-: | :-: | :-: |
| LINEミニアプリ お知らせ | LINE MINI App Notice | LINE MINI App 通知 |
| ![LINEミニアプリ お知らせ](https://developers.line.biz/media/line-mini-app/mini_service_notifier_jp.png) | ![LINE MINI App Notice](https://developers.line.biz/media/line-mini-app/mini_service_notifier_th.png) | ![LINE MINI App 通知](https://developers.line.biz/media/line-mini-app/mini_service_notifier_tw.png) |

若要傳送 Service messages，請使用 service message API。詳情請參閱[傳送 Service messages](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)。

<!-- note start -->

**傳送 Service messages 的條件**

您僅能在 LINE MINI App 上作為對使用者動作的確認或回應時傳送 Service messages。禁止傳送廣告與活動通知，包括折扣、購物回饋、新產品、折價券或促銷等資訊。如需有關 Service messages 條件的更多資訊，請參閱 [Service messages 的條件](https://developers.line.biz/en/docs/line-mini-app/service/service-operation/#conditions-for-service-messages)。

<!-- note end -->

## Custom Path 

Custom Path 是設定於已發布頻道（channel）的 LIFF URL 中的唯一字串。Custom Path 功能可讓您在 LIFF URL 中設定您自己的字串，如下所示：

| 含 LIFF ID 的範例 URL | 設定 Custom Path 的範例 |
| --- | --- |
| `https://miniapp.line.me/123456-abcdefg` | `https://miniapp.line.me/cony_coffee` |

例如，藉由將獨特名稱設定為 Custom Path，使用者就能從 URL 辨識出這是哪個品牌或店家的 LINE MINI App。如需有關 Custom Path 的更多資訊，請參閱[設定 Custom Path](https://developers.line.biz/en/docs/line-mini-app/develop/custom-path/)。

## Add a shortcut to your LINE MINI App to the home screen of the user's device 

使用者可以將您的 LINE MINI App 捷徑加入其裝置的主畫面。這讓使用者能直接從裝置的主畫面存取您的 LINE MINI App。

![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/add-shortcut-screen-ios-en.png)
![](https://developers.line.biz/media/line-mini-app/develop/add-to-home-screen/shortcut-ios-en.png)

對於會員卡、行動點餐等使用者經常使用的服務運用此功能，可以提升使用者體驗。

如需更多資訊，請參閱[將您的 LINE MINI App 捷徑加入使用者裝置的主畫面](https://developers.line.biz/en/docs/line-mini-app/develop/add-to-home-screen/)。

## Common Profile Quick-fill 

Quick-fill 是當您在 LINE MINI App 中點按 **Auto-fill** 時，自動填入所需個人資料資訊的功能。在 Account Center 中設定的 Common Profile 資訊，可以輕鬆地在 LINE MINI App 中使用。如需更多資訊，請參閱 [Common Profile Quick-fill 概覽](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/)。

![](https://developers.line.biz/media/line-mini-app/quick-fill/quick-fill-3-steps.png)

藉由在 LINE MINI App 中實作 Quick-fill，使用者只要點按一下按鈕，就能自動填入地址、電話號碼等所需資訊。這免去了手動輸入的需求，讓使用者在店家訂位或在線上商店下單時更加方便。

## Inducing users to add your Official Account as a friend 

透過 LINE MINI App，您可以使用加好友選項，從[驗證畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#verification-screen)或[頻道同意畫面](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)引導使用者將您的官方帳號（Official Account）加為好友。

如需更多資訊，請參閱[加好友選項](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/#link-a-line-official-account-with-your-channel)。

![bot link feature 1](https://developers.line.biz/media/line-mini-app/miniguide-incremental-01-en.png)
![bot link feature 2](https://developers.line.biz/media/line-mini-app/miniguide-incremental-02-en.png)

您也可以使用 [`liff.requestFriendship()`](https://developers.line.biz/en/reference/liff/#request-friendship) 方法，在任何時候顯示子視窗，提示使用者將您的 LINE 官方帳號（LINE Official Account）加為好友或解除封鎖。

## Custom action button 

[內建動作按鈕（built-in action button）](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)是為了讓使用者能輕鬆在好友之間分享 LINE MINI App 而提供的，但您也可以選擇[實作自訂動作按鈕](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/)。

![](https://developers.line.biz/media/line-mini-app/mini_share_custom.png)

## Using payment systems 

您可以將 LINE Pay 等付款方式整合到您的 LINE MINI App 中。此外，僅限於日本，您可以使用 [LINE MINI App in-app purchase](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/) 功能。

LINE MINI App 上可使用的付款系統會因國家或地區而異。

| 付款方式                       | Japan | Taiwan | Thailand |
| ------------------------------------- | :---: | :----: | :------: |
| LINE Pay                              |  ❌   |   ✅   |    ✅    |
| In-app purchase for the LINE MINI App |  ✅   |   ❌   |    ❌    |
| Other methods                         |  ✅   |   ✅   |    ✅    |

如需更多資訊，請參閱[處理付款](https://developers.line.biz/en/docs/line-mini-app/develop/payment/)。

![mini intro linepay](https://developers.line.biz/media/line-mini-app/mini_intro_linepay.png)

## Place ads 

LINE MINI App 可以藉由顯示 [LY Ads Network Display Ads (Web)](https://www.lycbiz.com/jp/partner/adnetwork/ly-ads/)（僅提供日文版）來進行營利。已驗證與未驗證的 MINI App 皆可刊登廣告，但該服務必須在日本提供。

如需更多資訊，請參閱[在 LINE MINI App 中刊登廣告](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-ads/)。
