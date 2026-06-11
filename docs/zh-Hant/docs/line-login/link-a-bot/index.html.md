# 登入時加入 LINE 官方帳號為好友（加入好友選項）（Add a LINE Official Account as a friend when logged in (add friend option)）

你可以在使用者登入你的應用程式時，顯示加入 LINE 官方帳號（LINE Official Account）為好友的選項。這稱為**加入好友選項（add friend option）**。請在 LINE Developers Console 上指定要加入為好友的 LINE 官方帳號。

![Consent screen](https://developers.line.biz/media/line-login/link-a-bot/consent-screen-with-bot-en.png)

如果使用者在登入時於上述同意畫面（consent screen）啟用**加入好友（Add as friend）**，該 LINE 官方帳號就會被加入為好友。如需更多有關建立機器人（bot）的資訊，請參閱 Messaging API 文件中的 [Messaging API overview](https://developers.line.biz/en/docs/messaging-api/overview/)。

## Displaying the option to add your LINE Official Account as a friend 

若要在同意畫面上顯示加入你的 LINE 官方帳號為好友的選項，請依下列方式進行設定。

1. [Link a LINE Official Account with your channel](https://developers.line.biz/en/docs/line-login/link-a-bot/#link-a-line-official-account)
1. [Redirect users to the LINE Login authorization URL with the `bot_prompt` query parameter](https://developers.line.biz/en/docs/line-login/link-a-bot/#redirect-users)

### Link a LINE Official Account with your channel 

在 LINE Developers Console 上，將 LINE 官方帳號與你的 LINE Login 頻道（channel）連結。

<!-- note start -->

**Note**

必須滿足下列條件，你才能將 LINE 官方帳號連結到你的 LINE Login 頻道。

- 與該 LINE 官方帳號關聯的 Messaging API 頻道，與你的 LINE Login 頻道屬於同一個服務提供者（provider）。
- 你同時是該 LINE Login 頻道與該 LINE 官方帳號的管理員。
  - 你可以透過 [LINE Developers Console](https://developers.line.biz/console/) 查看 LINE Login 頻道的管理員權限。
  - 你可以透過 [LINE Official Account Manager](https://manager.line.biz) 查看 LINE 官方帳號的管理員權限。

<!-- note end -->

1. 登入 [LINE Developers Console](https://developers.line.biz/console/)，並點選包含該 LINE Login 頻道的服務提供者。

1. 開啟你的 LINE Login 頻道設定。

1. 在 **Basic settings** 分頁的 **Linked LINE Official Account** 下方，點選 **Edit**。

1. 選取你希望使用者加入的 LINE 官方帳號，然後點選 **Update**。

   你可以選取你具有管理員身分的 LINE 官方帳號。

   每個 LINE Login 頻道只能連結一個 LINE 官方帳號。

### Redirect users to the LINE Login authorization URL with the `bot_prompt` query parameter 

當你完成將 LINE 官方帳號與頻道連結後，請將使用者重新導向至帶有 `bot_prompt` 查詢參數的 LINE Login 授權 URL。

```
https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id={CHANNEL_ID}&redirect_uri={CALLBACK_URL}&state={STATE}&bot_prompt={BOT_PROMPT}&scope={SCOPE_LIST}
```

會根據 `bot_prompt` 查詢參數的值顯示這些選項。

| Value | Description |
| --- | --- |
| `normal` | 在同意畫面中顯示加入 LINE 官方帳號為好友的選項。 |
| `aggressive` | 在同意畫面之後開啟一個新畫面，提供加入 LINE 官方帳號為好友的選項。 |

![Screen to be displayed](https://developers.line.biz/media/line-login/link-a-bot/bot-prompt-en.png)

<!-- tip start -->

**Tip**

如需更多有關 `bot_prompt` 以外其他查詢參數的資訊，請參閱 [Making an authorization request](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)。

<!-- tip end -->

#### Display options on the consent screen 

加入 LINE 官方帳號為好友的選項，會根據使用者與 LINE 官方帳號之間的關係，以下列方式顯示。

| Friend relationship when consent screen is displayed | Options shown to the user |
| --- | --- |
| Not a friend | 顯示加入 LINE 官方帳號為好友的選項。如果使用者選取該選項並繼續，該 LINE 官方帳號就會被加入為好友。 |
| Blocked | 顯示解除封鎖該 LINE 官方帳號的選項。如果使用者選取該選項並繼續，該 LINE 官方帳號就會被解除封鎖。 |
| Added as friend | 顯示使用者已將該 LINE 官方帳號加入為好友。不會顯示加入 LINE 官方帳號為好友的選項。 |

<!-- tip start -->

**若你的服務提供者為認證服務提供者，此選項預設為已選取（This option is selected by default if your provider is a certified provider）**

如果該 LINE Login 頻道隸屬於認證服務提供者（certified provider），則 `bot_prompt=normal` 時出現的同意畫面選項預設為已選取。

![](https://developers.line.biz/media/line-login/link-a-bot/add-friend-option-on-certified-provider-en.png)

如需更多有關認證服務提供者的資訊，請參閱 LINE Developers Console 文件中的 [Certified provider](https://developers.line.biz/en/docs/line-developers-console/overview/#certified-provider)。

<!-- tip end -->

## Getting the friendship status of the user and the LINE Official Account 

使用加入好友選項時，你可以透過下列其中一種方式，取得使用者與連結到你 LINE Login 頻道的 LINE 官方帳號之間的好友關係狀態（friendship status）。

- [Use the `friendship_status_changed` query parameter](https://developers.line.biz/en/docs/line-login/link-a-bot/#use-friendship_status_changed)
- [Use the LINE Login API to determine the friendship status](https://developers.line.biz/en/docs/line-login/link-a-bot/#use-line-login-api)

### Use the `friendship_status_changed` query parameter 

如果你在[發出授權請求](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request)時指定了 `bot_prompt` 查詢參數，則使用者完成驗證並授權你的應用程式後，會被帶有 `friendship_status_changed` 查詢參數重新導向至回呼 URL（callback URL）。

重新導向目標的 URL 範例：

```
https://client.example.org/cb?code={CODE}&state={STATE}&friendship_status_changed={FRIENDSHIP_STATUS_CHANGED}
```

`friendship_status_changed` 查詢參數可以是下列值。如需更多有關回呼 URL 的資訊，請參閱 [Receiving the authorization code](https://developers.line.biz/en/docs/line-login/integrate-line-login/#receiving-the-authorization-code)。

| Value | Description |
| --- | --- |
| `true` | 使用者與 LINE 官方帳號的好友關係狀態在登入期間發生變化。發生於下列其中一種情況：<br /><ul><li>使用者將該 LINE 官方帳號加入為好友</li><li>使用者解除封鎖了該 LINE 官方帳號</li></ul> |
| `false` | 使用者與 LINE 官方帳號的好友關係狀態在登入期間沒有變化。發生於下列其中一種情況：<br /><ul><li>使用者先前已將該 LINE 官方帳號加入為好友</li><li>使用者沒有將該 LINE 官方帳號加入為好友</li><li>使用者沒有解除封鎖該 LINE 官方帳號</li></ul> |

<!-- note start -->

**Note**

如果未向使用者顯示帶有加入你 LINE 官方帳號為好友選項的同意畫面，則不會包含 `friendship_status_changed` 查詢參數。

<!-- note end -->

### Use the LINE Login API to get the friendship status 

你可以使用[你的網頁應用程式所取得的存取權杖](https://developers.line.biz/en/docs/line-login/integrate-line-login/#get-access-token)，取得使用者與連結到你 LINE Login 頻道的 LINE 官方帳號之間的好友關係狀態。

請求範例：

```sh
curl -v -X GET https://api.line.me/friendship/v1/status \
-H 'Authorization: Bearer {access token}'
```

回應範例：

```json
{
  "friendFlag": true
}
```

如需深入了解，請參閱 LINE Login v2.1 API 參考文件中的 [Getting the friendship status of the user and the LINE Official Account](https://developers.line.biz/en/reference/line-login/#get-friendship-status)。
