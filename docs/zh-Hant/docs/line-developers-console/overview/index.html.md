# LINE Developers Console 總覽（LINE Developers Console overview）

LY Corporation 透過 **LINE Platform** 為第三方開發者提供下列功能：

- 以使用者 LINE 帳號的憑證來驗證使用者身分的功能（LINE Login）
- 讓你能與使用者交換 LINE 訊息的功能（Messaging API）

開發者在 **LINE Developers Console** 等管理工具上建立使用這些功能的**頻道（channel）**後，即可取得使用 LINE Platform 所提供功能的權限。

[LINE Developers Console Login](https://developers.line.biz/console/)

在 LINE Developers Console 上，你可以管理 **Developer**、**Provider** 與 **Channel**。

![Overview](https://developers.line.biz/media/line-developers-console/overview-01.png)

## Developer 

在 LINE Developers 網站上，存取 LINE Developers Console 的人被稱為 **Developer**（開發者）。

當你將開發者註冊到 provider 與 channel 時，便可控管每位開發者在 LINE Developers Console 上可檢視或編輯的資訊。

例如，你可以將某位開發者所建立頻道的角色（role）指派給另一位開發者。關於角色指派的詳細資訊，請參閱 [Managing roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/)。

## Provider 

在 LINE Developers 網站上，提供服務並為此取得使用者資訊的個別開發者、公司或組織被稱為**服務提供者（Service provider）**（在 LINE MINI App 中稱為 **Service company**）。

服務提供者會在 LINE Developers Console 上註冊為 **Provider**。

### Creating a provider 

1. 在 Console 首頁的 Providers 頁面，點選 **Create** 按鈕。

1. 在 **Create a new provider** 畫面中輸入你想要的 **Provider name**，並點選 **Create** 進行確認。

<!-- tip start -->

**Tip**

- provider 名稱會顯示在使用者同意畫面上。使用者會根據 provider 名稱來辨識服務提供者。因此，provider 名稱不應使用臨時性的名稱（例如僅在你的組織內部使用的品牌名稱、專案名稱等）。

  ![Sample Provider](https://developers.line.biz/media/line-developers-console/consent-screen-sample-provider.png)

- 當你以公司或組織的身分提供服務時，請使用該公司或組織的名稱來建立 provider。
- 服務提供者所使用的頻道必須建立在同一個 provider 之內。

<!-- tip end -->

### Deleting a provider 

根據你的 provider 角色，你可以點選 **Settings** 分頁底部的 **Delete** 按鈕來刪除你的 provider。關於 provider 角色的資訊，請參閱 [Provider roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-provider)。

### The number of providers that can be created 

可建立的 provider 數量有以下限制。

| Restrictions when creating channels | Description |
| --- | --- |
| LINE Developers Console restrictions | 每位開發者最多可建立 10 個 provider。無法建立第 11 個 provider。 |

### Certified provider 

一旦你成為認證的 provider（certified provider），使用者在檢視的頻道同意畫面上便會顯示「Certified」文字。你也可以設定並發佈一個 [Provider page](https://developers.line.biz/en/docs/partner-docs/provider-page/)。

![](https://developers.line.biz/media/line-developers-console/consent-screen-certified-provider-en.png)

認證的 provider 代表 LY Corporation 已確認建立該 provider 的服務提供者的真實性。LY Corporation 會確認以下事項：

- 該組織是否為真實存在的實體
- 申請是否由隸屬於該組織的人員（或代表人）所提出
- 該組織是否已建立並公開隱私權政策

<!-- note start -->

**成為認證 provider 所需的程序**

原則上，只有企業使用者才符合 provider 認證的資格。如果你想成為認證的 provider，需要提出特定的申請。請聯絡你的業務代表，或向 [our Sales partners](https://www.lycbiz.com/jp/partner/sales/) 提出你的詢問。

<!-- note end -->

<!-- note start -->

**Note**

- 顯示「Certified」文字並不代表 LY Corporation 對服務提供者所提供的服務予以支援或保證。
- 若要變更認證 provider 的名稱，你必須向 LY Corporation 提出審查申請。

<!-- note end -->

## Channel 

**Channel**（頻道）讓服務提供者得以使用 LINE Platform 所提供的功能。

要開發使用 LINE Platform 的服務，你必須建立一個頻道。

![Channel](https://developers.line.biz/media/messaging-api/getting-started/channel.png)

LINE Platform 會使用與頻道關聯的憑證，來確認開發者擁有使用 LINE Platform 的權限。

<!-- warning start -->

**為保護使用者資料所設的禁止事項**

當你將 LINE Platform 用於多項服務時，請勿將從各個別服務取得的 LINE 使用者資料相互串連。

<!-- warning end -->

### Creating a channel 

Messaging API 頻道可透過建立 LINE 官方帳號（LINE Official Account）來建立。詳細資訊請參閱 Messaging API 文件中的 [Get started with the Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/)。

若要建立其他類型的頻道，請依照以下步驟：

1. 在你的 provider 頁面上的 **Channels** 分頁中，選擇你想建立的頻道類型。可在 LINE Developers Console 上建立以下類型的頻道：

   | Type | Description |
   | --- | --- |
   | [LINE Login](https://developers.line.biz/en/docs/line-login/) | 你可以使用 LINE 帳號憑證來驗證你所開發服務的使用者。 |
   | Blockchain Service | 你可以提供使用區塊鏈服務（blockchain service）的服務。 |
   | LINE MINI App  | 你可以透過 [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/quickstart/) 提供服務，而無須開發原生應用程式。 |

1. 輸入你的頻道名稱以及任何必填／選填資訊，然後點選 **Create**。

   <!-- note start -->

   **頻道名稱限制**

   頻道名稱中不可包含「LINE」或類似的字串。

   <!-- note end -->

   <!-- note start -->

   **使用 LINE Login 頻道的注意事項**

   - 在你建立 LINE Login 頻道後，該頻道會立即被設定為 **Developing**（開發中）模式。
   - 當頻道被設定為 **Developing** 時，只有註冊為該頻道 Admin 或 Tester 的開發者才能使用 LINE Login。
   - 若要讓終端使用者能使用 LINE Login，請將該 LINE Login 頻道設定為 **Published**（已發佈）。

   <!-- note end -->

#### Precautions for channel and provider linkage 

一旦你建立了頻道，日後便無法將該頻道移動到另一個 provider。

如果你[將 Messaging API 用於透過 LINE Official Account Manager 建立的現有 LINE 官方帳號](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager)（由 [LINE Official Account Manager](https://manager.line.biz/) 所建立），你必須在初始設定期間建立一個新的 provider，或選擇一個讓該頻道所屬的現有 provider。在這種情況下同樣地，日後也無法將該頻道移動到另一個 provider。

當你開發一項將 Messaging API 頻道與 LINE Login 頻道串連的服務時，請在同一個 provider 之內建立這兩個頻道。

使用開發者所提供服務的 LINE 使用者，在每個 provider 下會被賦予不同的 user ID。user ID 無法用來跨越不同 provider 下的頻道辨識同一位使用者。

![](https://developers.line.biz/media/line-developers-console/different-user-ids.png)

<!-- warning start -->

**建立頻道時需特別注意的情況**

例如，以下情況需要特別注意：

- 頻道與 provider 由個人或公司管理。
- 在同一個 provider 下建立不相關服務或公司的頻道。
- 在由經營頻道管理工具等的服務（公司）所管理的 provider 下建立頻道。

在這類情況下，由於頻道日後無法在 provider 之間移動，且使用者在不同 provider 下會被賦予不同的 user ID，未來可能會產生問題。在考量所涉及的風險後，請在適當的 provider 下建立頻道。

<!-- warning end -->

### Deleting a channel 

根據你的頻道角色，你可以點選 **Basic Settings** 分頁底部的 **Delete** 按鈕來刪除你的頻道。

關於頻道角色的資訊，請參閱 [Channel roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/#roles-for-channel)。

### The number of channels that can be created 

可建立的頻道數量有以下限制與規範。

| Restrictions or specifications when creating channels | Description |
| --- | --- |
| LINE Developers Console restrictions | 不論頻道類型為何，開發者在同一個 provider 下最多可擁有 100 個具有 Admin 角色的頻道。 |
| LINE Official Account Manager restrictions | 對於每個登入 LINE Official Account Manager 的帳號，開發者最多可擁有 100 個 LINE 官方帳號。 |

<!-- tip start -->

**關於 LINE Official Account Manager**

你可以使用與 LINE Developers Console 相同的帳號登入 [LINE Official Account Manager](https://manager.line.biz/)，以檢查並設定你的 LINE 官方帳號。

<!-- tip end -->
