# 管理角色（Managing roles）

透過管理 provider 與頻道（channel）的角色，您可以控制開發人員在 [LINE Developers Console](https://developers.line.biz/console/) 上能檢視與編輯的資訊。本頁說明可指派給已在 provider 與頻道上註冊之開發人員的各種角色類型。

provider 與頻道各自擁有對應的角色。

- [Provider roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-provider)
- [Channel roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel)

## Provider roles 

註冊為 provider 的開發人員可被賦予 Admin 角色或 Member 角色。

您也可以在不授予 provider 存取權限的情況下，授予開發人員頻道存取權限。在這種情況下，該開發人員在 provider 中的角色會是「No role」。

|                                          | Admin | Member | No role \*1 |
| ---------------------------------------- | ----- | ------ | ----------- |
| 檢視 provider 名稱                       | ✅    | ✅     | ✅          |
| 檢視 provider ID                         | ✅    | ✅ \*2 | ✅ \*2      |
| 編輯 provider 名稱                       | ✅    | ❌     | ❌          |
| 刪除 provider \*3                        | ✅    | ❌     | ❌          |
| 檢視與 provider 連結的頻道清單           | ✅    | ❌     | ❌          |
| 在 provider 底下建立頻道                 | ✅    | ❌     | ❌          |
| 將開發人員加入 provider 或自其中刪除     | ✅    | ❌     | ❌          |
| 檢視或編輯 provider 角色設定             | ✅    | ❌     | ❌          |

\*1 僅限有權存取與 provider 連結之頻道的情況。

\*2 無法檢視 **Provider settings** 畫面，但開發人員選擇某個 provider 時，provider ID 會包含在 URL 中。

\*3 無法刪除已有頻道的 provider。

<!-- note start -->

**關於 provider 角色與頻道角色**

關於 provider 角色與頻道角色，請注意以下幾點：

- 即使在 provider 上擁有 Admin 角色，若沒有頻道存取權限，仍無法檢視與該 provider 連結之頻道的詳細資訊
- 即使授予開發人員 provider 存取權限，該開發人員也不會自動取得與該 provider 連結之頻道的存取權限
- 從 provider 刪除開發人員時，即使勾選了 **Also delete the selected developer(s) from the channels that belong to this provider.**，狀態為「Pending」的頻道仍不會刪除該開發人員

<!-- note end -->

<!-- tip start -->

**provider 上的「Member」與「No role」有什麼差別？**

provider 上的「Member」與「No role」都只能檢視 provider 名稱。

如果您在 provider 上授予開發人員 Member 角色，只要在頻道的 **Roles** 分頁中點擊 **Import from provider**，即可將該開發人員加入與該 provider 連結的頻道。

**Import from provider** 僅供在頻道與 provider 上皆擁有 Admin 角色的開發人員帳號使用。

![Import from provider](https://developers.line.biz/media/line-developers-console/managing-roles-en.png)

<!-- tip end -->

### Adding developers, editing roles, and deleting developers on provider 

請依照以下步驟開啟 **Roles** 分頁。

1. 從 [LINE Developers Console](https://developers.line.biz/console/) 側邊欄選擇 provider。
1. 點擊 **Roles** 分頁。

   | 操作 | 步驟 |
   | --- | --- |
   | 新增 | 點擊 **Invite by email**，註冊電子郵件地址，設定開發人員的角色，然後點擊 **Send invitation**。該開發人員會收到一封標題為「You have received an invitation to join a provider」的電子郵件。若開發人員接受邀請，便會被加入該 provider。 |
   | 編輯 | 點擊 **Edit**，然後從下拉清單中選擇角色。 |
   | 刪除 | 勾選成員名稱旁的核取方塊，並點擊 **Delete selected**。 |

## Channel roles 

開發人員可在頻道上被賦予 Admin、Member 或 Tester 角色。這些角色針對各頻道類型可執行的操作如下：

- [Common to all channel types](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel-common)
- [LINE Login channel](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel-line-login)
- [Messaging API channel](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel-messaging-api)
- [LINE MINI App channel](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel-line-mini-app)

### Common to all channel types 

#### **Basic settings** tab 

|  | Admin | Member | Tester | No role |
| --- | --- | --- | --- | --- |
| 檢視 **Channel ID** | ✅ | ✅ | ✅ | ❌ |
| 檢視 **Region to provide the service** \*1 | ✅ | ❌ | ❌ | ❌ |
| 檢視或編輯 **Company or owner's country or region** \*1 | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Channel icon** | ✅ | ✅ | ✅ | ❌ |
| 編輯 **Channel icon** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Channel name** | ✅ | ✅ | ✅ | ❌ |
| 編輯 **Channel name** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Channel description** | ✅ | ✅ | ❌ | ❌ |
| 編輯 **Channel description** | ✅ | ❌ | ❌ | ❌ |
| 檢視或編輯 **Email address** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Privacy policy URL** | ✅ | ✅ | ❌ | ❌ |
| 編輯 **Privacy policy URL** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Terms of use URL** | ✅ | ✅ | ❌ | ❌ |
| 編輯 **Terms of use URL** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **App types** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Permissions** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Channel secret** | ✅ | ❌ | ❌ | ❌ |
| 檢視或編輯 **Assertion Signing Key** | ✅ | ❌ | ❌ | ❌ |
| 檢視 **Your user ID** \*2 | ✅ | ✅ | ✅ | ❌ |
| 檢視或編輯 **Require two-factor authentication** \*3 | ✅ | ❌ | ❌ | ❌ |
| 檢視或編輯 **Localization (multi-language support)** \*1 | ✅ | ❌ | ❌ | ❌ |
| 檢視或編輯 **Linked LINE Official Account** \*1 | ✅ | ❌ | ❌ | ❌ |
| 檢視或編輯 **Email address permission** \*1 | ✅ | ❌ | ❌ | ❌ |
| 執行 **Delete this channel** \*4 | ✅ | ❌ | ❌ | ❌ |
| 執行 **Leave channel** | ❌ | ✅ | ✅ | ❌ |

\*1 僅在 LINE Login 頻道或 LINE MINI App 頻道中顯示。<br>\*2 僅在 LINE Login 頻道或 Messaging API 頻道中顯示。在任一角色下，若您的 Business ID 未連結 LINE 帳號，則不會顯示 **Your user ID**。詳情請參閱 [Available features](https://developers.line.biz/en/docs/line-developers-console/login-account/#available-features)。<br>\*3 僅在 LINE MINI App 頻道中顯示。<br>\*4 您無法刪除 Blockchain Service 頻道或 LINE MINI App 頻道。

#### **Roles** tab 

|                            | Admin | Member | Tester | No role |
| -------------------------- | ----- | ------ | ------ | ------- |
| 檢視或編輯 **Roles** 分頁  | ✅    | ❌     | ❌     | ❌      |

#### Test on a channel set to "Developing" 

| Admin | Member | Tester | No role |
| ----- | ------ | ------ | ------- |
| ✅    | ❌     | ✅     | ❌      |

只有 LINE Login 頻道、LINE MINI App 頻道與 Blockchain Service 頻道具有狀態。關於在 LINE Login 頻道中為您的開發人員帳號授予 Tester 角色後的測試方法，請參閱 [How to test with a LINE Login channel with the "Developing" status](https://developers.line.biz/en/docs/line-login/getting-started/#how-to-test-login-channel)。

### LINE Login channel 

|                                 | Admin | Member | Tester | No role |
| ------------------------------- | ----- | ------ | ------ | ------- |
| 檢視或編輯 **LINE Login** 分頁  | ✅    | ❌     | ❌     | ❌      |
| 檢視或編輯 **LIFF** 分頁        | ✅    | ❌     | ❌     | ❌      |

### Messaging API channel 

|                                    | Admin | Member | Tester | No role |
| ---------------------------------- | ----- | ------ | ------ | ------- |
| 檢視或編輯 **Messaging API** 分頁  | ✅    | ❌     | ❌     | ❌      |
| 檢視 **LIFF** 分頁                 | ✅    | ❌     | ❌     | ❌      |
| 檢視或編輯 **Security** 分頁       | ✅    | ❌     | ❌     | ❌      |
| 檢視 **Webhook errors** 分頁 \*1   | ✅    | ✅     | ❌     | ❌      |
| 檢視 **QR code** \*2               | ✅    | ✅     | ✅     | ❌      |

\*1 **Webhook errors** 分頁只會在 **Messaging API** 分頁上啟用 **Error statistics aggregation** 的頻道中顯示。

\*2 對於擁有 Admin 角色的開發人員，它會顯示在 **Messaging API** 分頁下。對於擁有 Member 角色或 Tester 角色的開發人員，它會顯示在 **Basic settings** 分頁下。

### LINE MINI App channel 

|                                               | Admin | Tester | No role |
| --------------------------------------------- | ----- | ------ | ------- |
| 檢視或編輯 **Web app settings** 分頁          | ✅    | ❌     | ❌      |
| 檢視或編輯 **Review request** 分頁            | ✅    | ❌     | ❌      |
| 檢視或編輯 **Business information** 分頁      | ✅    | ❌     | ❌      |
| 檢視或編輯 **Contact information** 分頁       | ✅    | ❌     | ❌      |
| 檢視或編輯 **Service message template** 分頁  | ✅    | ❌     | ❌      |
| 檢視 **LIFF URL** \*                          | ✅    | ✅     | ❌      |

\* 對於擁有 Admin 角色的開發人員，它會顯示在 **Web app settings** 分頁下。對於擁有 Tester 角色的開發人員，它會顯示在 **Basic settings** 分頁下。請注意，擁有 Tester 角色的開發人員只能檢視 Developing 用的 LIFF URL。

### Adding developers, editing roles, and deleting developers on channel 

在 [LINE Developers Console](https://developers.line.biz/console/) 上開啟頻道的 **Roles** 分頁。

| 操作 | 步驟 |
| --- | --- |
| 新增 | <ul><li>點擊 **Invite by email**，註冊電子郵件地址，設定開發人員的角色，然後點擊 **Send inivitaion**。該開發人員會收到一封標題為「You have received an invitation to join a channel」的電子郵件。若開發人員接受邀請，便會被加入該頻道。</li><li>點擊 **Import from provider** 並選擇先前已在同一 provider 下註冊的成員。點擊 **Import** 後，角色會立即指派給該開發人員，開發人員無需接受您的邀請。</li></ul> |
| 編輯 | 點擊 **Edit**，並從下拉清單中選擇角色。 |
| 刪除 | 勾選成員名稱旁的核取方塊，並點擊 **Delete selected**。 |

<!-- note start -->

**在 Messaging API 頻道中新增具有 Admin 角色之開發人員的限制**

如果開發人員 A 已在 100 個 Messaging API 頻道中註冊為 Admin，則開發人員 A 無法以 Admin 身分加入由開發人員 B 建立的 Messaging API 頻道，但可以以 Member 或 Tester 身分加入。

這是因為它與 [The number of channels that can be created](https://developers.line.biz/en/docs/line-developers-console/overview/#number-of-channels) 中所述的「LINE Official Account Manager restrictions」相衝突。

<!-- note end -->

#### "The email address entered when sending an invitation" will be used only for the invitation 

您在點擊 **Invite by email** 時所輸入的電子郵件地址，僅會用於頻道的邀請。邀請時所指定的角色，會在點擊電子郵件中的 **Accept the invitation** 後，授予登入 LINE Developers Console 的開發人員帳號。

「邀請時所輸入的電子郵件地址」不一定要與「被授予角色的開發人員帳號之電子郵件地址」相同。因此，請注意角色可能會在無意間被授予以不同於邀請所用電子郵件地址註冊的開發人員帳號。

<!-- note start -->

**收到邀請時的注意事項**

當您收到邀請並要為您的開發人員帳號授予角色時，請注意以下事項：

- 若您尚未登入 LINE Developers Console，請以應被授予該角色的開發人員帳號登入 LINE Developers Console
- 若您已登入 LINE Developers Console，請確認您正在登入的開發人員帳號就是應被授予該角色的帳號

<!-- note end -->
