# 使用受眾（Use audiences）

受眾（audience）可協助你套用進階的目標鎖定。例如，你可以鎖定一群已讀取你訊息，或點擊了訊息中 URL 的使用者。

<!-- note} start -->

**使用廣告識別碼（IFA）**

你可以使用 IFA 來指定收件人，但此功能僅開放給有提交申請表的企業用戶。若要在你的 LINE 官方帳號中使用 IFA，請聯絡你的業務代表，或聯絡[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note} end -->

## Create an audience 

你可以使用 Messaging API 建立受眾。支援的受眾類型如下：

| 受眾 | 說明 |
| --- | --- |
| [上傳使用者 ID 的受眾](https://developers.line.biz/en/reference/messaging-api/#create-upload-audience-group) | 以[使用者 ID（user ID）](https://developers.line.biz/en/glossary/#user-id)或 IFA（廣告識別碼）指定的一群使用者 |
| [訊息點擊受眾](https://developers.line.biz/en/reference/messaging-api/#create-click-audience-group) | 點擊了已傳送訊息中 URL 的一群使用者 |
| [訊息曝光受眾](https://developers.line.biz/en/reference/messaging-api/#create-imp-audience-group)  | 讀取了已傳送訊息的一群使用者 |

你無法使用 Messaging API 建立下列類型的受眾：

- 聊天標籤受眾
- 好友來源受眾
- 預約受眾
- 圖文選單曝光受眾
- 圖文選單點擊受眾
- 網站流量受眾（LINE Tag）
- 網站流量受眾（Tracking Tag）
- App 事件受眾
- 影片觀看受眾
- 圖片點擊受眾
- LINE Beacon Network 廣告曝光受眾

<!-- note start -->

**並行操作的數量限制**

對於以使用者 ID 為基礎的受眾，每個受眾 ID（`audienceGroupId`）的並行端點（endpoint）操作數量是有限制的。此限制適用於建立上傳使用者 ID 的受眾，以及將使用者 ID 加入受眾。如需更多資訊，請參閱[並行操作數量的限制](https://developers.line.biz/en/reference/messaging-api/#limit-on-the-number-of-concurrent-operations)。

<!-- note end -->

## Use audiences 

你可以使用受眾來傳送指定群發訊息（narrowcast message）。如需更多資訊，請參閱[傳送指定群發訊息](https://developers.line.biz/en/docs/messaging-api/sending-messages/#send-narrowcast-message)。

## Share audiences 

Messaging API 與 [LINE Official Account Manager](https://manager.line.biz/) 可以互相使用為同一個 LINE 官方帳號所建立的受眾。互相使用受眾不需要任何初始設定。

如果你想在 Messaging API 與 LINE Official Account Manager 以外的工具（例如 [LINE Ads Manager](https://admanager.line.biz/)）之間使用受眾，則需要設定受眾共享。如需更多關於如何共享受眾的資訊，請參閱[在 Business Manager 中共享你的受眾](https://developers.line.biz/en/docs/messaging-api/using-audience/#audience-sharing-business-manager)。

| 建立受眾的工具 | 使用受眾的工具 | 受眾是否可用 |
| --- | --- | --- |
| Messaging API | LINE Official Account Manager | ✅ |
| LINE Official Account Manager | Messaging API | ✅ |
| Messaging API | LINE Official Account Manager 以外的工具 | ✅ \*1 |
| LINE Official Account Manager 以外的工具 | Messaging API | ✅ \*1 |

\*1 若你在 Business Manager 中共享受眾即可使用。

### Share your audience in Business Manager 

[Business Manager](https://data.linebiz.com/solutions/business-manager) 可讓你跨多個服務（例如 LINE Ads Manager）共享特定受眾，並互相使用這些受眾。

你可以使用 Business Manager 的受眾共享功能，在同一個 provider 下的多個 Messaging API 頻道（channel）之間共享受眾。但是，只有認證帳號與[付費帳號（premium account）](https://developers.line.biz/en/glossary/#premium-account)才能在 Business Manager 中設定受眾共享。

你可以使用下列端點取得 Business Manager 中已共享受眾的資料：

- [取得 Business Manager 中已共享受眾的清單](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience-list)
- [取得 Business Manager 中已共享受眾的資料](https://developers.line.biz/en/reference/messaging-api/#get-shared-audience)

如需更多關於如何共享受眾的資訊，請參閱 Business Manager 手冊中的[共享資源](https://data.linebiz.com/business-manager/manual/bmmaniyuarushare003)（僅提供日文版）。

## Audience specification 

受眾規格如下。

| 屬性 | 規格 |
| --- | --- |
| 每個頻道的受眾數量 | 最多 1,000 個 |
| 保留期間 | 最多 180 天（15,552,000 秒） |
| 每次請求可上傳以建立受眾的使用者 ID 或 IFA 數量 | <ul><li>JSON：最多 10,000 個</li><li>檔案：最多 1,500,000 個</li></ul> |
| 每個受眾的使用者數量 | <ul><li>上傳使用者 ID 的受眾：無上限</li><li>訊息點擊受眾：最少 50 個</li><li>訊息曝光受眾：最少 50 個</li></ul> |
| 傳送訊息後建立再行銷受眾[^retargeting-audiences]<br />的時間限制 | 最多 60 天（5,184,000 秒） |

[^retargeting-audiences]: 此項僅適用於訊息點擊受眾與訊息曝光受眾

如需更多關於指定群發訊息限制的資訊，請參閱 Messaging API 參考文件中的[使用屬性與受眾傳送訊息的限制](https://developers.line.biz/en/reference/messaging-api/#send-narrowcast-message-restrictions)。
