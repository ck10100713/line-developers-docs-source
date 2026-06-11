# 取得已傳送訊息的統計資料

針對你傳送給多位使用者的[推播訊息（push messages）](https://developers.line.biz/en/reference/messaging-api/#send-push-message)與[群發訊息（multicast messages）](https://developers.line.biz/en/reference/messaging-api/#send-multicast-message)，你可以依彙總單位（aggregation unit）取得使用者與這些訊息互動方式的統計資料。

一般來說，為了保護使用者隱私，你無法取得使用者對訊息所執行動作的統計資料，例如開啟訊息或點擊 URL。不過，你可以將資料彙總成你自行定義的單位，並使其無法識別個別使用者，藉此取得統計資料。

如下圖所示，你可以指定單位名稱（unit name）並傳送訊息，藉此取得各單位的統計資料。

![](https://developers.line.biz/media/news/customAggregationUnits_en.png)

## What are message statistics 

你可以針對訊息取得以下各單位的統計資料：

- 開啟訊息的使用者數
- 開啟訊息中任一 URL 的使用者數
- 開始播放訊息中任一影片或音訊的使用者數

透過取得訊息統計資料，你可以了解使用者對你所傳送訊息的操作情形。運用這類統計資料，可以確認以下資訊：

**運用所取得統計資料的範例**

| 收件者數 | 開啟次數 | 開啟率 | URL 點擊次數 | URL 點擊率 |
| -------------- | ------ | ------ | ----------- | ----------- |
| 500          | 433    | 87%    | 323          | 65%         |

### Notes on aggregated statistics 

統計資料可能包含一些誤差。為了保護使用者隱私，在以下情況下，部分與使用者互動相關的屬性值會顯示為 `null`：

- 彙總統計值小於 20。
- 即使彙總統計值大於或等於 20，但實際產生該事件的使用者數小於 20。
  - 例如，若影片的播放次數為 30，但開始播放該影片的使用者數為 15，則兩者都會顯示為 `null`。

## Assign a unit name 

若要彙總資料，你必須在傳送推播訊息或群發訊息時，為這些訊息指定彙總單位名稱。若要為推播訊息或群發訊息指定單位名稱，請在請求主體（request body）的 `customAggregationUnits` 屬性中指定名稱。傳送訊息時，你只能指定一個單位名稱。關於傳送推播訊息或群發訊息的規格，請參閱 Messaging API reference 中的 [Message](https://developers.line.biz/en/reference/messaging-api/#messages)。

以下是在推播訊息上指定彙總單位名稱 `promotion_a` 的請求範例：

```sh
curl -v -X POST https://api.line.me/v2/bot/message/push \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": "U4af4980629...",
    "messages":[
        {
            "type": "text",
            "text": "Hello, world1"
        }
    ],
    "customAggregationUnits": [
        "promotion_a"
    ]
}'
```

<!-- tip start -->

**事後指定或變更單位名稱**

訊息傳送後，你無法為推播訊息或群發訊息指定或變更單位名稱。

<!-- tip end -->

### Maximum number of unit name types 

在當月期間（從該月 1 日到最後一天），你最多可以使用 1,000 個不同的單位名稱來傳送訊息。

例如，若你在 3 月使用從 `promotion_0001` 到 `promotion_1000` 共 1,000 種單位名稱來傳送訊息，你可以在下個月（4 月）使用相同的 1,000 種單位名稱（從 `promotion_0001` 到 `promotion_1000`）來傳送訊息。你也可以在下個月（4 月）使用 1,000 種新的單位名稱（從 `promotion_1001` 到 `promotion_2000`）來傳送訊息。

請注意，當訊息使用第 1,001 種或之後的單位名稱傳送時，這些單位名稱會被視為未指定給該訊息。例如，若你使用從 `promotion_0001` 到 `promotion_1500` 共 1,500 種單位名稱來傳送訊息，則第 1,001 種單位名稱（`promotion_1001` 之後）的訊息仍會被傳送，但這些單位名稱不會被指定給訊息。

如果你有許多種類的單位名稱，請使用以下方法之一，確認單位名稱可以被指定或已經被指定：

- 在傳送訊息前，使用 [Get the number of unit name types assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-the-number-of-unit-name-types-assigned-during-this-month) 端點，確認當月的單位名稱數量尚未達到 1,000 個
- 在傳送訊息後，使用 [Get a list of unit names assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-a-list-of-unit-names-assigned-during-this-month) 端點，確認所指定的單位名稱存在

<!-- tip start -->

**關於單位名稱的數量限制**

指定單位名稱時有「當月最多 1,000 種單位名稱」的限制，但如果你在傳送訊息後[依單位取得統計資料](https://developers.line.biz/en/docs/messaging-api/unit-based-statistics-aggregation/#get-statistics-per-unit)，則對於彙總所涵蓋的期間，你可以取得從 `from` 到 `to` 之間所有存在單位的統計資料。

<!-- tip end -->

## Get statistics per unit 

你可以使用 [Get statistics per unit](https://developers.line.biz/en/reference/messaging-api/#get-statistics-per-unit) 端點，取得使用單位名稱傳送的推播訊息與群發訊息的使用者互動統計資料。以下是取得名為 `promotion_a` 單位統計資料的請求範例：

```sh
curl -v -X GET https://api.line.me/v2/bot/insight/message/event/aggregation \
-H 'Authorization: Bearer {channel access token}' \
--data-urlencode 'customAggregationUnit=promotion_a' \
--data-urlencode 'from=20210301' \
--data-urlencode 'to=20210331' \
-G
```

此外，你可以使用 [Get a list of unit names assigned during this month](https://developers.line.biz/en/reference/messaging-api/#get-a-list-of-unit-names-assigned-during-this-month) 端點，取得當月所指定的單位名稱清單。並沒有可用來查詢上個月之前所指定單位名稱的端點。

## Example of getting statistics of a message containing a URL 

以下是依單位取得包含 URL 的訊息統計資料的步驟範例：

### 1. Send a message by assigning a unit name 

首先，將內容相同的訊息傳送給多位使用者。

![](https://developers.line.biz/media/messaging-api/insight/new-item-message-example-en.png)

假設我們想使用群發訊息將訊息傳送給 150 位使用者。接著在 `customAggregationUnits` 屬性中指定單位名稱。

```sh
curl -v -X POST https://api.line.me/v2/bot/message/multicast \
-H 'Content-Type: application/json' \
-H 'Authorization: Bearer {channel access token}' \
-d '{
    "to": ["U4af4980629...","U0c229f96c4...",...], // 150 user IDs
    "messages":[
        {
            "type": "text",
            "text": "🆕 Our new product is available now!\nhttps://example.com/new-item/"
        }
    ],
    "customAggregationUnits": [
        "new-item-message-yyyymmdd"
    ]
}'
```

### 2. Get and aggregate statistics 

傳送訊息後等待幾天，再依單位取得統計資料。

```sh
curl -v -X GET https://api.line.me/v2/bot/insight/message/event/aggregation \
-H 'Authorization: Bearer {channel access token}' \
--data-urlencode 'customAggregationUnit=new-item-message-yyyymmdd' \
--data-urlencode 'from=20210301' \
--data-urlencode 'to=20210331' \
-G
```

在此範例中，可取得以下統計資料：

```json
{
  "overview": {
    "uniqueImpression": 111,
    "uniqueClick": 74,
    "uniqueMediaPlayed": null,
    "uniqueMediaPlayed100Percent": null
  },
  "messages": [
    {
      "seq": 1,
      "impression": 111,
      "uniqueImpression": 111,
      "mediaPlayed": null,
      "mediaPlayed25Percent": null,
      "mediaPlayed50Percent": null,
      "mediaPlayed75Percent": null,
      "mediaPlayed100Percent": null,
      "uniqueMediaPlayed": null,
      "uniqueMediaPlayed25Percent": null,
      "uniqueMediaPlayed50Percent": null,
      "uniqueMediaPlayed75Percent": null,
      "uniqueMediaPlayed100Percent": null
    }
  ],
  "clicks": [
    {
      "seq": 1,
      "url": "https://example.com/new-item/",
      "click": 74,
      "uniqueClick": 74,
      "uniqueClickOfRequest": 74
    }
  ]
}
```

你可以運用這些資訊來查看訊息開啟率、URL 點擊率等。

| 收件者數 | 開啟次數 | 開啟率 | URL 點擊次數 | URL 點擊率 |
| -------------- | ------ | ------ | ----------- | ----------- |
| 150          | 111    | 74%    | 74          | 67%         |

## Get statistics on narrowcast messages or broadcast messages 

透過使用 Get user interaction statistics 端點，你可以取得使用者與你的 LINE 官方帳號（LINE Official Account）所傳送之分眾訊息（narrowcast messages）或廣播訊息（broadcast messages）互動方式的統計資料。詳情請參閱 Messaging API reference 中的 [Get user interaction statistics](https://developers.line.biz/en/reference/messaging-api/#get-message-event)。
