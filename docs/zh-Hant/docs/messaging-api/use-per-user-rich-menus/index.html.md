# 使用個別使用者圖文選單（Use per-user rich menus）

本頁說明如何設定「個別使用者圖文選單（per-user rich menu）」。

<!-- table of contents -->

## What is per-user rich menu 

你可以使用 Messaging API 以個別使用者為單位設定圖文選單。因此，你可以準備多組圖文選單，並為每位使用者設定不同的圖文選單，藉此提升使用者體驗。

個別使用者圖文選單具有以下特性：

1. 顯示優先順序高於預設圖文選單
   - 個別使用者圖文選單的顯示優先順序高於預設圖文選單。因此，若你已為某個 LINE 官方帳號設定了預設圖文選單，又為某位使用者設定了個別使用者圖文選單，則個別使用者圖文選單會優先於預設圖文選單顯示。詳情請參閱 [Display priority of rich menus](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-display)。
1. 設定變更會立即生效
   - 個別使用者圖文選單的設定會立即生效並變更顯示內容，使用者無需重新進入聊天畫面。詳情請參閱 [When rich menu setting changes take effect](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#when-setting-change-takes-effect)。

## Set a per-user rich menu 

個別使用者圖文選單的基本設定流程如下：

1. [建立圖文選單並附加圖片](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/#create-a-rich-menu)
1. [準備一個使用者 ID](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/#prepare-user-id)
1. [將圖文選單連結至使用者](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/#link-the-rich-menu-to-user)
1. [從使用者解除圖文選單連結](https://developers.line.biz/en/docs/messaging-api/use-per-user-rich-menus/#unlink-the-rich-menu-from-user)以停止顯示個別使用者圖文選單（選用）

### 1. Create a rich menu and attach an image 

首先，建立一個圖文選單。關於如何建立圖文選單的詳細資訊，請參閱 [Use rich menus](https://developers.line.biz/en/docs/messaging-api/using-rich-menus/)。

這裡我們使用以下範本圖片（`richmenu-template-guide-07.png`）作為圖文選單的圖片。請將其儲存在任意目錄中。

![The template image for rich menus used in this guide](https://developers.line.biz/media/messaging-api/rich-menu/richmenu-template-guide-07.png)

在你的終端機中執行此指令，以[建立圖文選單](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu)：

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
    "selected": true,
    "name": "Test the per-user rich menu",
    "chatBarText": "Tap to open",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 2500,
                "height": 1686
            },
            "action": {
                "type": "uri",
                "label": "Tap area A",
                "uri": "https://developers.line.biz/en/news/"
            }
        }
    ]
}'
```

接著，在你的終端機中執行此指令，以[上傳並附加圖片至圖文選單](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)。

```sh
curl -v -X POST https://api-data.line.me/v2/bot/richmenu/{richMenuId}/content \
-H "Authorization: Bearer {channel access token}" \
-H "Content-Type: image/png" \
-T richmenu-template-guide-07.png
```

### 2. Prepare a user ID 

準備一個將顯示此圖文選單的使用者 ID。這裡請準備你自己的使用者 ID，以便實際確認顯示效果。

使用者 ID 範例：`U8189cf6745fc0d808977bdb0b9f22995`

關於取得使用者 ID 的詳細資訊，請參閱 [Get user IDs](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/) 中的 [Developer gets their own user ID](https://developers.line.biz/en/docs/messaging-api/getting-user-ids/#get-own-user-id)。

### 3. Link the rich menu to the user 

當圖文選單與你的使用者 ID 都準備好之後，[將圖文選單連結至使用者](https://developers.line.biz/en/reference/messaging-api/#link-rich-menu-to-user)。在你的終端機中執行此指令。

```sh
curl -v -X POST https://api.line.me/v2/bot/user/{userId}/richmenu/{richMenuId} \
-H "Authorization: Bearer {channel access token}"
```

#### 3-1. Check the rich menu display 

確認步驟 3 所設定的個別使用者圖文選單是否有顯示。開啟你已設定圖文選單的 LINE 官方帳號的聊天畫面。

![](https://developers.line.biz/media/messaging-api/rich-menu/per-user-rich-menu-example.png)

### 4. Unlink the rich menu from the user 

最後，[從使用者解除圖文選單連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)並停止顯示圖文選單。在顯示步驟 4 中開啟的聊天畫面時，於你的終端機中執行此指令。

```sh
curl -v -X DELETE https://api.line.me/v2/bot/user/{userId}/richmenu \
-H 'Authorization: Bearer {channel access token}'
```

由於個別使用者圖文選單的設定會立即生效，因此執行完成後，個別使用者圖文選單的顯示便會結束。

請注意，若已設定預設圖文選單，則會改為顯示預設圖文選單。

## Allow users to switch between rich menus 

你可以使用個別使用者圖文選單，為使用者提供具有分頁切換功能的圖文選單。若要像切換分頁一樣輕鬆地在圖文選單之間切換，請使用[圖文選單別名（rich menu aliases）](https://developers.line.biz/en/glossary/#rich-menu-alias)與[圖文選單切換動作（rich menu switch action）](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)。

![](https://developers.line.biz/media/messaging-api/rich-menu/switching-richmenu-ja.png)

詳情請參閱 [Switch between tabs on rich menus](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/)。
