# 圖文選單概覽（Rich menus overview）

了解你可以在 LINE 官方帳號參與的聊天室中顯示的圖文選單（rich menu）：

## What is rich menu 

圖文選單（rich menu）是顯示在 LINE 官方帳號聊天室底部的選單。你可以為圖文選單設定連往外部網站、預約頁面以及 LINE 官方帳號功能的連結，讓使用者體驗更加「豐富」。請依照[圖文選單結構](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-structure)，使用[建立圖文選單的工具](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#choosing-tool-for-creating-rich-menus)。

<!-- note start -->

**圖文選單無法在 LINE for PC 上使用**

圖文選單不會顯示在 LINE for PC（macOS、Windows）上。

<!-- note end -->

## Rich menu structure 

圖文選單由選單圖片、可點擊區域與聊天列（chat bar）組成。

![](https://developers.line.biz/media/messaging-api/rich-menu/bot-demo-rich-menu-image.png)

1. 圖文選單圖片：一個包含選單項目的 JPEG 或 PNG 圖片檔。如需更多關於圖片要求的資訊，請參閱 Messaging API 參考文件中的 [Requirements for rich menu image](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image-requirements)。
1. 可點擊區域：你劃分為選單項目的區域。可在每個選單項目上指派一個[動作（action）](https://developers.line.biz/en/reference/messaging-api/#action-objects)，例如取得 postback 事件與開啟 URL。
1. 聊天列：用來開啟與關閉圖文選單的選單。你可以自訂這個選單的文字。

## Tools for setting rich menus 

要建立圖文選單，可使用 [LINE Official Account Manager](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-with-the-line-manager) 或 [Messaging API](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-using-the-messaging-api)。請找出最符合你需求的工具。

<!-- note start -->

**一個圖文選單只能使用一種工具**

你無法用兩種工具來取得或編輯同一個圖文選單實例。以 LINE Official Account Manager 建立的圖文選單，只能透過 LINE Official Account Manager 取得與編輯。同樣地，你也無法對以 Messaging API 建立的圖文選單使用 LINE Official Account Manager。

<!-- note end -->

| 工具 | 優點 |
| --- | --- |
| [LINE Official Account Manager](https://manager.line.biz/) | <ul><li>開發時間快</li><li>易於使用的圖形化介面</li><li>可設定顯示期間</li><li>可取得顯示次數與點擊率等統計資料</li></ul><p>如需更多資訊，請參閱 LINE for Business 的 [How to use the rich menus](https://www.lycbiz.com/jp/column/line-official-account/technique/20180731-01/)（僅提供日文版）與 [Insight - Rich menus](https://www.lycbiz.com/jp/manual/OfficialAccountManager/insight_rich-menus/)（僅提供日文版）。</p> |
| Messaging API | <ul><li>進階自訂</li><li>你可以在圖文選單上設定 [postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action) 與 [datetime picker action](https://developers.line.biz/en/reference/messaging-api/#datetime-picker-action)。</li><li>你可以[在圖文選單的分頁之間切換](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/)。</li></ul><p>如果你想試用圖文選單功能，請參閱 [Play with rich menus](https://developers.line.biz/en/docs/messaging-api/try-rich-menu/)。</p> |

使用 Messaging API 圖文選單時，你無法取得顯示次數與點擊率等統計資料。

### Set rich menus with LINE Official Account Manager 

你可以從 LINE Official Account Manager 建立圖文選單並將其設為預設。除非設定了具有較高[顯示優先順序](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-display)的不同圖文選單，否則使用者會看到預設的圖文選單。

使用 LINE Official Account Manager 的 GUI，你可以根據預先定義的範本來設定圖文選單的可點擊區域。如需更多資訊，請參閱 [LINE Official Account Manager manual](https://www.lycbiz.com/jp/manual/OfficialAccountManager/rich-menus/)（僅提供日文版）。

### Set rich menus with the Messaging API 

要以 Messaging API 設定圖文選單，必須依序呼叫所需的端點（endpoint）。基本步驟如下：

1. 準備一張圖文選單圖片。
1. 使用 [Create rich menu](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu) 端點。
1. 使用 [Upload rich menu image](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image) 端點。
1. 使用 [Set default rich menu](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu) 端點。

如需更多關於如何以 Messaging API 設定圖文選單的資訊，請參閱 [Use rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)。

## Scope of rich menus 

圖文選單有兩種範圍（scope），你可以使用不同的工具來設定。

| 範圍 | 工具 |
| --- | --- |
| 所有開啟 LINE 官方帳號聊天畫面的使用者（預設圖文選單） | <ul><li>LINE Official Account Manager</li><li>Messaging API</li></ul> |
| 個別使用者（個別使用者圖文選單） | Messaging API |

依範圍與設定工具的不同，圖文選單的顯示優先順序，以及變更在使用者聊天畫面上生效的時機也會有所不同。

- [圖文選單的顯示優先順序](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-display)
- [圖文選單設定變更何時生效](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#when-setting-change-takes-effect)

### Display priority of rich menus 

依設定方式與目標對象的不同，共有三種圖文選單類型。這些類型的顯示優先順序就是以下列出的順序，由高至低：

1. 以 Messaging API 設定的個別使用者圖文選單
1. 以 Messaging API 設定的預設圖文選單
1. 以 [LINE Official Account Manager](https://manager.line.biz) 設定的預設圖文選單

### When rich menu setting changes take effect 

當你變更圖文選單的設定時，變更會在不同的時機生效，取決於圖文選單的範圍與設定工具。

| 範圍與設定工具 | 變更何時生效 |
| --- | --- |
| 以 Messaging API 設定的個別使用者圖文選單 | 立即生效。但如果你在未[將圖文選單與使用者解除連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)的情況下刪除圖文選單，刪除會在使用者重新開啟聊天時生效。 |
| 以 Messaging API 設定的預設圖文選單 | 當使用者重新開啟聊天時生效。變更生效最多可能需要一分鐘。 |
| 以 LINE Official Account Manager 設定的預設圖文選單 | 當使用者重新開啟聊天時 |

### When users who are not friends with your LINE Official Account open the chat screen 

當尚未成為你 LINE 官方帳號好友的使用者開啟聊天畫面時，會顯示在 LINE Official Account Manager 或以 Messaging API 設定的預設圖文選單。

請注意，你無法將圖文選單連結到尚未成為你 LINE 官方帳號好友的使用者。如需更多資訊，請參閱 Messaging API 參考文件中的 [Conditions for linking rich menu](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user-conditions)。

## Rich menu API reference 

- [Rich menu](https://developers.line.biz/en/reference/messaging-api/#rich-menu)
- [Per-user rich menu](https://developers.line.biz/en/reference/messaging-api/#per-user-rich-menu)
- [Rich menu alias](https://developers.line.biz/en/reference/messaging-api/#rich-menu-alias)
