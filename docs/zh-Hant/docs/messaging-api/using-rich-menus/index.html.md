# 使用圖文選單（Use rich menus）

本頁說明如何設定「預設圖文選單（default rich menu）」，這個選單會顯示給所有將你的 LINE 官方帳號加為好友的使用者。

<!-- tip start -->

**也可以透過 LINE Official Account Manager 設定圖文選單**

你也可以從 [LINE Official Account Manager](https://manager.line.biz/) 設定預設圖文選單。詳情請參閱 [Set rich menus with LINE Official Account Manager](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#creating-a-rich-menu-with-the-line-manager)。

<!-- tip end -->

<!-- table of contents -->

## Set default rich menu 

若要透過 Messaging API 設定預設圖文選單：

1. [準備圖文選單圖片](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/#prepare-a-rich-menu-image)。
1. [建立圖文選單](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/#create-a-rich-menu)並指定可點擊區域。
1. [上傳並附加圖文選單圖片](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/#upload-the-rich-menu-image)。
1. [設定預設圖文選單](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/#set-the-default-rich-menu)。

### 1. Prepare a rich menu image 

準備一張圖文選單圖片。你需要思考要如何在圖文選單圖片上配置點擊區域。

這裡我們使用以下範本圖片（`richmenu-template-guide-04.png`）作為圖文選單。請將它儲存在任意目錄中。

![本指南中使用的圖文選單範本圖片](https://developers.line.biz/media/messaging-api/rich-menu/richmenu-template-guide-04.png)

以這張圖片為例，假設要定義 A、B、C 三個點擊區域。

<!-- tip start -->

**圖文選單範本圖片**

你可以從 [LINE Official Account Manager](https://manager.line.biz) 下載圖文選單的範本圖片。在建立圖文選單的頁面中，點擊 **Design guide**。你可以使用與 [LINE Developers Console](https://developers.line.biz/console/) 相同的帳號登入 LINE Official Account Manager。

<!-- tip end -->

如需更多有關圖片需求的資訊，請參閱 Messaging API 參考文件中的 [Requirements for rich menu image](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image-requirements)。

### 2. Create a rich menu 

建立一個與步驟 1 中所準備的圖文選單圖片相符的圖文選單。請確認點擊區域有正確對應到圖片中的 A、B、C。

當你[透過 Messaging API 建立圖文選單](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu)時，請在請求主體（request body）中指定一個[圖文選單物件（rich menu object）](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)。在你的終端機中執行此指令。這裡指定了 [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action)，讓 A、B、C 各個點擊區域分別開啟不同的 URL。

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "size": {
        "width": 2500,
        "height": 1686
    },
    "selected": false,
    "name": "Test the default rich menu",
    "chatBarText": "Tap to open",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 1666,
                "height": 1686
            },
            "action": {
                "type": "uri",
                "label": "Tap area A",
                "uri": "https://developers.line.biz/en/news/"
            }
        },
        {
            "bounds": {
                "x": 1667,
                "y": 0,
                "width": 834,
                "height": 843
            },
            "action": {
                "type": "uri",
                "label": "Tap area B",
                "uri": "https://api.line-status.info/"
            }
        },
        {
            "bounds": {
                "x": 1667,
                "y": 844,
                "width": 834,
                "height": 843
            },
            "action": {
                "type": "uri",
                "label": "Tap area C",
                "uri": "https://techblog.lycorp.co.jp/en/"
            }
        }
    ]
}'
```

<!-- tip start -->

**Tip**

- 若要自動開啟與使用者連結的圖文選單，請將請求主體中的 `selected` 屬性設為 `true`。
- 若要設定聊天列（chat bar）的文字，請在請求主體中指定 `chatBarText` 屬性。
- 在建立圖文選單之前，你可以[檢查](https://developers.line.biz/en/reference/messaging-api/#validate-rich-menu-object)[圖文選單物件（rich menu object）](https://developers.line.biz/en/reference/messaging-api/#rich-menu-object)的有效性。

<!-- tip end -->

如果圖文選單建立成功，回應中會傳回圖文選單 ID（rich menu ID）。我們會在後續步驟中使用這個圖文選單 ID。

```json
{
  "richMenuId": "richmenu-88c05..."
}
```

### 3. Upload and attach the rich menu image 

將你在步驟 1 中準備的圖片[上傳並附加](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)到你在步驟 2 中建立的圖文選單。在你的終端機中執行以下指令：

1. 移動到包含步驟 1 中所準備圖片的目錄。
1. 將 `{richMenuId}` 替換為你在步驟 2 中取得的圖文選單 ID 後，執行此指令。

```sh
curl -v -X POST https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: image/png" \
-T richmenu-template-guide-04.png
```

### 4. Set the default rich menu 

現在準備工作都完成了，接著來設定圖文選單的顯示。在這裡，我們[設定預設圖文選單](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu)。除非使用者已連結到個別使用者圖文選單（per-user rich menu），否則與你的 LINE 官方帳號為好友的使用者都會看到這個預設圖文選單。在你的終端機中執行此指令。

```sh
curl -v -X POST https://api.line.me/v2/bot/user/all/richmenu/{richMenuId} \
-H "Authorization: Bearer {channel access token}"
```

#### 4-1. Check the rich menu displa 

確認所設定的預設圖文選單有顯示出來。開啟你已設定圖文選單的 LINE 官方帳號的聊天畫面。本次建立的圖文選單會以收合狀態顯示，點擊 **Tap to open** 即可開啟圖文選單。

![](https://developers.line.biz/media/messaging-api/rich-menu/default-rich-menu-example.png)

## About per-user rich menu 

你可以使用 Messaging API 以個別使用者為單位設定圖文選單。如需更多有關個別使用者圖文選單（per-user rich menu）的資訊，請參閱 [Use per-user rich menus](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/)。
