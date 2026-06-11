# 建立優惠券並傳送給使用者（Create coupons and send them to users）

你可以使用 Messaging API 建立優惠券，並從你的 LINE 官方帳號（LINE Official Account）以訊息形式傳送給使用者。

![](https://developers.line.biz/media/messaging-api/coupon/several-coupons.jpg)

<!-- table of contents -->

## Steps to send coupons using the Messaging API 

使用 Messaging API，你可以透過兩個步驟將優惠券傳送給使用者：

1. [建立優惠券](https://developers.line.biz/en/docs/messaging-api/send-coupons-to-users/#create-coupon)
2. [傳送優惠券](https://developers.line.biz/en/docs/messaging-api/send-coupons-to-users/#send-coupon)

<!-- tip start -->

**你也可以使用 LINE Official Account Manager 傳送優惠券**

除了 Messaging API 之外，你也可以使用 [LINE Official Account Manager](https://manager.line.biz/) 建立並傳送優惠券。詳情請參閱 LINE for Business 中的 [Coupons](https://www.lycbiz.com/jp/manual/OfficialAccountManager/coupons-create/)（僅提供日文版）。

<!-- tip end -->

## Create a coupon 

首先，使用 [Create a coupon](https://developers.line.biz/en/reference/messaging-api/#create-coupon) 端點建立優惠券。

```sh
curl -v -X POST https://api.line.me/v2/bot/coupon \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'
{
  "title": "Friends-only coupon",
  "description": "- To use this coupon, please show this screen to the staff.\n- Used coupons cannot be used again. If you accidentally mark it as \"used\", it will also become unavailable.\n- This coupon may be changed or terminated without notice regardless of the validity period.",
  "reward": {
    "type": "discount",
    "priceInfo": {
      "type": "fixed",
      "fixedAmount": 100
    }
  },
  "acquisitionCondition": {
    "type": "normal"
  },
  "startTimestamp": 0,
  "endTimestamp": 1924959599,
  "imageUrl": "https://developers.line.biz/media/messaging-api/coupon/sample-coupon-image-100-yen-off.jpg",
  "timezone": "ASIA_TOKYO",
  "visibility": "UNLISTED",
  "maxUseCountPerTicket": 1
}'
```

當你建立優惠券時，回應中會傳回優惠券 ID。

```json
{
  "couponId": "01JYNW8JMQVFBNWF1APF8Z3FS7"
}
```

建立優惠券時，你可以在請求主體中將 `acquisitionCondition.type` 設為 `lottery`，以設定領取條件，例如「只有抽獎中獎的使用者才能領取」。你也可以使用 [reward 物件](https://developers.line.biz/en/reference/messaging-api/#create-coupon-reward-object)（`reward`）指定優惠券的優惠內容，例如「五折優惠」或「現金回饋 100 日圓」。

詳情請參閱 Messaging API 參考文件中的 [Create a coupon](https://developers.line.biz/en/reference/messaging-api/#create-coupon)。

建立優惠券後，請繼續進行[傳送優惠券](https://developers.line.biz/en/docs/messaging-api/send-coupons-to-users/#send-coupon)步驟。

### You can't edit coupons you have created 

優惠券一旦建立後就無法修改。若要變更優惠券的內容，你必須先[停用優惠券](https://developers.line.biz/en/docs/messaging-api/send-coupons-to-users/#discontinue-coupon)，然後再建立一張新的優惠券。

使用 LINE Official Account Manager 建立優惠券時，你可以將其儲存為草稿。然而，使用 Messaging API 建立優惠券時，無法將優惠券設為「草稿」狀態。

## Send a coupon 

建立優惠券並取得優惠券 ID 後，在[優惠券訊息（coupon message）](https://developers.line.biz/en/docs/messaging-api/message-types/#coupon-messages)中指定該優惠券 ID 並傳送。如果你不知道優惠券 ID，可以[取得優惠券清單](https://developers.line.biz/en/docs/messaging-api/send-coupons-to-users/#check-coupon-list)來查看。

```sh
curl -v -X POST https://api.line.me/v2/bot/message/broadcast \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d '
{
  "messages": [
    {
      "type": "coupon",
      "couponId": "01JYNW8JMQVFBNWF1APF8Z3FS7"
    }
  ]
}'
```

優惠券訊息可以透過下列任一種訊息類型傳送。你也可以將使用 Messaging API 建立的優惠券，在 LINE Official Account Manager 中以訊息形式傳送。

- [Push message](https://developers.line.biz/en/reference/messaging-api/#send-push-message)
- [Multicast message](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)
- [Broadcast message](https://developers.line.biz/en/reference/messaging-api/#send-broadcast-message)
- [Narrowcast message](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message)
- [Reply message](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)

使用者可以開啟並領取送達的優惠券，並在有效期間（validity period）內使用。

![](https://developers.line.biz/media/messaging-api/coupon/coupon-message-ja.jpg)

## Discontinue a coupon 

優惠券會在建立時所指定的有效期間結束後自動失效，但你也可以在期間結束前使用 [Discontinue a coupon](https://developers.line.biz/en/reference/messaging-api/#discontinue-coupon) 端點手動停用優惠券。

```sh
curl -v -X PUT https://api.line.me/v2/bot/coupon/01JYNW8JMQVFBNWF1APF8Z3FS7/close \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json'
```

優惠券一旦停用後，已收到該優惠券訊息的使用者將無法再領取，而已領取的使用者也將無法再使用。

已停用的優惠券無法重新啟用。

詳情請參閱 Messaging API 參考文件中的 [Discontinue a coupon](https://developers.line.biz/en/reference/messaging-api/#discontinue-coupon)。

## Check the list of created coupons 

你可以使用 [Get a list of coupons](https://developers.line.biz/en/reference/messaging-api/#get-coupons-list) 端點，查看你所建立優惠券的優惠券 ID 與標題。

```sh
curl -v -X GET https://api.line.me/v2/bot/coupon \
-H 'Authorization: Bearer {channel access token}'
```

此優惠券清單同時包含使用 Messaging API 與 [LINE Official Account Manager](https://manager.line.biz/) 建立的優惠券。你可以在 LINE Official Account Manager 中查看相同的清單。

```json
{
  "items": [
    {
      "couponId": "01JZMWQ9HMDW9ENJP4C167CXP8",
      "title": "Year-end and New Year coupon"
    },
    {
      "couponId": "01JZA9NPPFDJ3RFG8NA9DJ0NQT",
      "title": "Friends-only coupon"
    }
  ]
}
```

你也可以使用查詢參數 `status` 僅取得有效的優惠券或僅取得已過期的優惠券。詳情請參閱 Messaging API 參考文件中的 [Get a list of coupons](https://developers.line.biz/en/reference/messaging-api/#get-coupons-list)。

## Get details of a coupon 

你可以使用 [Get details of a coupon](https://developers.line.biz/en/reference/messaging-api/#get-coupon) 端點取得特定優惠券的詳細資訊。

```sh
curl -v -X GET https://api.line.me/v2/bot/coupon/01JYNW8JMQVFBNWF1APF8Z3FS7 \
-H 'Authorization: Bearer {channel access token}'
```

你不僅可以取得使用 Messaging API 建立的優惠券詳細資訊，也可以取得使用 LINE Official Account Manager 建立的優惠券詳細資訊。

```json
{
  "couponId": "01K0B456W5Y6SBD3YH74YM6QE6",
  "title": "Friends-only coupon",
  "description": "- To redeem your coupon, present this screen at checkout.\n- Redeemable once only, even if previously redeemed only unintentionally by the customer.\n- The validity period of this coupon may change or it may be canceled without notice.",
  "acquisitionCondition": {
    "type": "lottery",
    "lotteryProbability": 50,
    "maxAcquireCount": -1
  },
  "startTimestamp": 1752678000,
  "endTimestamp": 1924959540,
  "timezone": "ASIA_TOKYO",
  "couponCode": "COUPONCODE123456",
  "maxUseCountPerTicket": 1,
  "maxTicketPerUser": 1,
  "visibility": "UNLISTED",
  "reward": {
    "type": "discount",
    "priceInfo": {
      "type": "fixed",
      "fixedAmount": 100,
      "currency": "JPY"
    }
  },
  "imageUrl": "https://oa-coupon.line-scdn-dev.net/0h9gbUqRVkZkhfLHhXMLYZHwdyaCosWGBAPFR7cD5tZidsTnofYDVfezt-ZAR3YER9OzRfK35XZwR6TH5uYDF2TnJ-cBNyfURpPRl2RSFSXQc0TiJhYCFiXiZ8XXk0",
  "usageCondition": "Usable for payments of 1,000 yen or more",
  "status": "RUNNING",
  "createdTimestamp": 1752720120
}
```

詳情請參閱 Messaging API 參考文件中的 [Get details of a coupon](https://developers.line.biz/en/reference/messaging-api/#get-coupon)。

## Check the number of views and uses of sent coupons 

你可以在 [LINE Official Account Manager](https://manager.line.biz/) 中查看已傳送優惠券的瀏覽次數與使用次數。詳情請參閱 LINE for Business 中的 [Insight - Coupons](https://www.lycbiz.com/jp/manual/OfficialAccountManager/insight_coupon/)（僅提供日文版）。

## Coupon image display size 

建立優惠券時，可以在 `imageUrl` 中指定圖片 URL 以顯示優惠券圖片。如果你指定的是正方形圖片，在聊天畫面中的長寬比會是 1.51:1（寬:高），因此圖片的上下部分會被部分裁切掉。

![](https://developers.line.biz/media/messaging-api/coupon/how-images-look.jpg)

<!-- tip start -->

**我該如何建立優惠券圖片**

你可以使用 LINE Marketing Campus 中 [Free template image collection](https://lymcampus.jp/line-official-account/courses/template/lessons/6-1-1)（僅提供日文版）所提供的優惠券圖片，或使用 [LINE Creative Lab](https://creativelab.line.biz/)（僅提供日文版）提供的範本。

![Sample coupon image](https://developers.line.biz/media/messaging-api/coupon/sample-coupon-image-100-yen-off.jpg)

<!-- tip end -->
