# 在圖文選單的分頁之間切換（Switch between tabs on rich menus）

你可以使用每位使用者專屬的圖文選單，為使用者提供具備分頁切換功能的圖文選單。若要像切換分頁一樣輕鬆地在圖文選單之間切換，請使用[圖文選單別名（rich menu alias）](https://developers.line.biz/en/glossary/#rich-menu-alias)與[圖文選單切換動作（rich menu switch action）](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)。

![](https://developers.line.biz/media/messaging-api/rich-menu/switching-richmenu-ja.png)

以下是設定兩個圖文選單（圖文選單 A 與圖文選單 B），並啟用兩者之間切換的步驟：

1. [準備圖文選單圖片](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-01)
1. [建立圖文選單 A](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-02)
1. [上傳圖文選單 A 的圖片](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-03)
1. [建立圖文選單 B](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-04)
1. [上傳圖文選單 B 的圖片](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-05)
1. [將圖文選單 A 設為預設](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-06)
1. [建立圖文選單別名 A](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-07)
1. [建立圖文選單別名 B](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-08)
1. [停止顯示圖文選單](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-09)

## 1. Prepare rich menu images 

請準備圖文選單 A 的圖片（`richmenu-a.png`）與圖文選單 B 的圖片（`richmenu-b.png`）。如需更多關於支援的圖片規格資訊，請參閱 Messaging API 參考文件中的[圖文選單圖片的需求](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image-requirements)。

| 圖文選單 A 的圖片 | 圖文選單 B 的圖片 |
| :-: | :-: |
| ![Rich menu A image](https://developers.line.biz/media/messaging-api/rich-menu/richmenu-a.png) | ![Rich menu B image](https://developers.line.biz/media/messaging-api/rich-menu/richmenu-b.png) |

## 2. Create rich menu A 

使用 Messaging API [建立圖文選單](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu)。在本範例中，請在[區域物件（area object）](https://developers.line.biz/en/reference/messaging-api/#area-object)中為可點擊區域指定如下動作：

- **圖文選單 A 左側的可點擊區域**
  - 動作：[URI 動作（URI action）](https://developers.line.biz/en/reference/messaging-api/#uri-action)
  - URI：[LINE Developers 網站](https://developers.line.biz/)
- **圖文選單 A 右側的可點擊區域**
  - 動作：[圖文選單切換動作（Rich menu switch action）](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)（type：`richmenuswitch`）
  - 切換目標：圖文選單 B（richMenuAliasId：`richmenu-alias-b`）。

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
    "name": "richmenu-a",
    "chatBarText": "Tap to open",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 1250,
                "height": 1686
            },
            "action": {
                "type": "uri",
                "uri": "https://developers.line.biz/"
            }
        },
        {
            "bounds": {
                "x": 1251,
                "y": 0,
                "width": 1250,
                "height": 1686
            },
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "richmenu-alias-b",
                "data": "richmenu-changed-to-b"
            }
        }
    ]
}'
```

當圖文選單 A 建立完成後，會以回應的形式回傳該圖文選單的 ID。

```json
{
  "richMenuId": "richmenu-19682466851b21e2d7c0ed482ee0930f"
}
```

## 3. Upload rich menu A image 

我們已建立圖文選單 A，現在請使用 Messaging API 為圖文選單 A [上傳圖片](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)。請以[步驟 2](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-02) 中取得的圖文選單 ID 作為路徑參數來指定目標選單。

```sh
curl -v -X POST https://api-data.line.me/v2/bot/richmenu/richmenu-19682466851b21e2d7c0ed482ee0930f/content \
-H 'Authorization: Bearer {channel access token}' \
-H "Content-Type: image/png" \
-T richmenu-a.png
```

## 4. Create rich menu B 

以與圖文選單 A 相同的方式建立圖文選單 B（`richmenu-b`）。請在[區域物件（area object）](https://developers.line.biz/en/reference/messaging-api/#area-object)中為可點擊區域指定如下動作。

- **圖文選單 B 左側的可點擊區域**
  - 動作：[圖文選單切換動作（Rich menu switch action）](https://developers.line.biz/en/reference/messaging-api/#richmenu-switch-action)（type：`richmenuswitch`）
  - 切換目標：圖文選單 A（richMenuAliasId：`richmenu-alias-a`）
- **圖文選單 B 右側的可點擊區域**
  - 動作：[URI 動作（URI action）](https://developers.line.biz/en/reference/messaging-api/#uri-action)
  - URI：[LY Corporation Tech Blog](https://techblog.lycorp.co.jp/)

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
    "name": "richmenu-b",
    "chatBarText": "Tap to open",
    "areas": [
        {
            "bounds": {
                "x": 0,
                "y": 0,
                "width": 1250,
                "height": 1686
            },
            "action": {
                "type": "richmenuswitch",
                "richMenuAliasId": "richmenu-alias-a",
                "data": "richmenu-changed-to-a"
            }
        },
        {
            "bounds": {
                "x": 1251,
                "y": 0,
                "width": 1250,
                "height": 1686
            },
            "action": {
                "type": "uri",
                "uri": "https://techblog.lycorp.co.jp/"
            }
        }
    ]
}'
```

當圖文選單 B 建立完成後，會以回應的形式回傳該圖文選單的 ID。

```json
{
  "richMenuId": "richmenu-4ecc8d672d9da4ba375fb82fa938fe5e"
}
```

## 5. Upload rich menu B image 

我們已建立圖文選單 B，現在請使用 Messaging API 為圖文選單 B [上傳圖片](https://developers.line.biz/en/reference/messaging-api/#upload-rich-menu-image)。請以[步驟 4](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-04) 中取得的圖文選單 ID 作為路徑參數來指定目標選單。

```sh
curl -v -X POST https://api-data.line.me/v2/bot/richmenu/richmenu-4ecc8d672d9da4ba375fb82fa938fe5e/content \
-H 'Authorization: Bearer {channel access token}' \
-H "Content-Type: image/png" \
-T richmenu-b.png
```

## 6. Set rich menu A as default 

將[預設圖文選單](https://developers.line.biz/en/reference/messaging-api/#set-default-rich-menu)設定為圖文選單 A。

```sh
curl -v -X POST https://api.line.me/v2/bot/user/all/richmenu/richmenu-19682466851b21e2d7c0ed482ee0930f \
-H 'Authorization: Bearer {channel access token}'
```

這會讓圖文選單 A 以預設選單的形式顯示。如果你點擊圖文選單 A 的右半邊，選單並不會切換到圖文選單 B。這是因為我們還沒有為圖文選單 B 建立別名。

![Default rich menu displayed](https://developers.line.biz/media/messaging-api/rich-menu/set-default-rich-menu.png)

<!-- note start -->

**如果圖文選單 A 沒有顯示**

如果使用者設有一個顯示優先順序高於預設圖文選單的每位使用者專屬圖文選單，圖文選單 A 就不會顯示。若要讓圖文選單 A 顯示，請[刪除](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu)該每位使用者專屬的圖文選單，或將該圖文選單從使用者[取消連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)。如需更多資訊，請參閱[圖文選單的顯示優先順序](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-display)。

<!-- note end -->

## 7. Create rich menu alias A 

為圖文選單 A [建立別名](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu-alias)。以下是為我們在[步驟 2](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-02) 中建立的圖文選單 A 設定別名 `richmenu-alias-a` 的範例請求。

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/alias \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "richMenuAliasId": "richmenu-alias-a",
    "richMenuId": "richmenu-19682466851b21e2d7c0ed482ee0930f"
}'
```

## 8. Create rich menu alias B 

為圖文選單 B [建立別名](https://developers.line.biz/en/reference/messaging-api/#create-rich-menu-alias)。以下是為我們在[步驟 4](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-04) 中建立的圖文選單 B 設定別名 `richmenu-alias-b` 的範例請求。

```sh
curl -v -X POST https://api.line.me/v2/bot/richmenu/alias \
-H 'Authorization: Bearer {channel access token}' \
-H 'Content-Type: application/json' \
-d \
'{
    "richMenuAliasId": "richmenu-alias-b",
    "richMenuId": "richmenu-4ecc8d672d9da4ba375fb82fa938fe5e"
}'
```

現在，當你點擊圖文選單 A 的右側可點擊區域時，便可切換到圖文選單 B。當你點擊圖文選單 B 的左側可點擊區域時，便可切換回圖文選單 A。

| 圖文選單 A | 圖文選單 B |
| :-: | :-: |
| ![Rich menu A](https://developers.line.biz/media/messaging-api/rich-menu/set-default-rich-menu.png) | ![Rich menu B](https://developers.line.biz/media/messaging-api/rich-menu/switch-rich-menu.png) |

你可以隨時[變更別名](https://developers.line.biz/en/reference/messaging-api/#update-rich-menu-alias)。

## 9. Stop displaying rich menu 

假設我們想要停止顯示圖文選單。使用 Messaging API 時，請依下列順序撤回圖文選單：

1. [清除圖文選單的預設選單設定](https://developers.line.biz/en/reference/messaging-api/#clear-default-rich-menu)。
1. [刪除圖文選單別名](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu-alias)。
1. [刪除圖文選單](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu)。

你可以在不[將圖文選單從使用者取消連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)的情況下刪除圖文選單。但這樣並不會立即移除圖文選單，而是在使用者下次開啟聊天室時才會移除。

如果你知道使用者 ID，便可將圖文選單從身為你 LINE 官方帳號好友的使用者取消連結。若要將圖文選單從使用者取消連結但保留該圖文選單：

- [將圖文選單從使用者取消連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)
- [將圖文選單從多位使用者取消連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-users)

當你將圖文選單從使用者取消連結的那一刻，圖文選單便會立即從聊天室中消失。

## When the intended rich menu isn't displayed 

如果預期的圖文選單沒有顯示，請檢查以下幾點：

- [清除預設後你仍會看到圖文選單](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#youll-still-see-the-rich-menu-after-you-clear-the-default)
- [你設定了新的預設圖文選單，但看到的是另一個圖文選單](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#you-see-a-different-rich-menu)

### You'll still see the rich menu after you clear the default 

當你從圖文選單 A 切換到 B，或從 B 切換到 A 時，你會看到顯示優先順序最高的每位使用者專屬選單。因此，清除在[步驟 6](https://developers.line.biz/en/docs/messaging-api/switch-rich-menus/#richmenu-switch-06) 中設定的預設圖文選單，對你所看到的內容並沒有影響。你仍會看到圖文選單 A 或 B。

此時，如果你[刪除圖文選單](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu)或[將圖文選單從使用者取消連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)，圖文選單便不再顯示。如需更多關於圖文選單顯示優先順序的資訊，請參閱[圖文選單的顯示優先順序](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-display)。

### You set a new default rich menu but you see a different rich menu 

如果你沒有看到你設為新預設的圖文選單，問題出在顯示優先順序上。有可能存在一個顯示優先順序更高的每位使用者專屬圖文選單。

若要讓新的預設選單顯示，你可以[刪除](https://developers.line.biz/en/reference/messaging-api/#delete-rich-menu)你目前看到的圖文選單，或[將圖文選單從使用者取消連結](https://developers.line.biz/en/reference/messaging-api/#unlink-rich-menu-from-user)。如需更多資訊，請參閱[圖文選單的顯示優先順序](https://developers.line.biz/en/docs/messaging-api/rich-menus-overview/#rich-menu-display)。
