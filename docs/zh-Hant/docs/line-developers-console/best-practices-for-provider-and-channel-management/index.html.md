# Provider 與頻道管理的最佳實踐（Best practices for provider and channel management）

本頁說明 provider 與頻道（channel）管理的最佳實踐。

<!-- table of contents -->

## Characters 

以下使用假設的組織與人物作為範例：

| 組織、人物 | 說明 |
| --- | --- |
| Beverage Manufacturer A | 一家飲料製造商，提供咖啡飲料「Brown Coffee」與茶飲料「Cony Tea」。它將使用 LINE Platform 的服務開發委外給 Development Company C 與 Development Company D。 |
| Beverage Manufacturer B | 一家飲料製造商，提供可樂飲料「Sally Cola」。為 Beverage Manufacturer A 的美國子公司。 |
| Development Company C | 一家受 Beverage Manufacturer A 委外開發使用 LINE Platform 服務的開發公司。它正使用 LINE Login 為咖啡飲料「Brown Coffee」開發活動網站。 |
| Development Company D | 一家受 Beverage Manufacturer A 委外開發使用 LINE Platform 服務的開發公司。它正使用 Messaging API 為咖啡飲料「Brown Coffee」開發 LINE Bot，以及為茶飲料「Cony Tea」開發 LINE Bot。 |
| Brown | Beverage Manufacturer A 的員工。 |
| Cony | Beverage Manufacturer A 的員工。 |

假設 Beverage Manufacturer A 管理 provider「Beverage Manufacturer A」以及該 provider 底下的頻道。Provider「Beverage Manufacturer A」底下的頻道如下：

| 頻道類型 | 頻道名稱 | 說明 |
| --- | --- | --- |
| LINE Login | Brown Coffee | 用於咖啡飲料「Brown Coffee」活動網站的頻道。 |
| Messaging API | Brown Coffee | 用於咖啡飲料「Brown Coffee」LINE Bot 的頻道。 |
| Messaging API | Cony Tea | 用於茶飲料「Cony Tea」LINE Bot 的頻道。 |

## Grant admin roles to several developers for each provider and each channel 

| | |
| --- | --- |
| 良好範例 | 為每個 provider 與每個頻道授予多位開發者 admin 角色。 |
| 不良範例 | 為每個 provider 與每個頻道只授予一位開發者 admin 角色。 |

如果某個 provider 與頻道唯一擁有 admin 角色的開發者因為突然離職或其他原因而無法聯絡，將無法以 admin 角色存取這些 provider 與頻道。如此一來，可能難以繼續營運這些 provider 與頻道。為了因應這類意外狀況，請為每個 provider 與每個頻道授予多位開發者 admin 角色。

例如，假設 Brown 與 Cony 都擁有 provider「Beverage Manufacturer A」以及 LINE Login 頻道「Brown Coffee」的 admin 角色。即使 Brown 突然離職，Cony 也擁有 admin 角色，能夠繼續正常營運該 provider 與頻道。

![](https://developers.line.biz/media/line-developers-console/best-practices-for-provider-and-channel-management/grant-admin-role-to-several-developers-en.png)

請注意，provider 與頻道的角色彼此獨立，因此授予某個 provider 的 admin 角色，並不代表已授予該 provider 底下頻道的 admin 角色。

如需更多關於角色的資訊，請參閱 [Managing roles](https://developers.line.biz/en/docs/line-developers-console/managing-roles/)。

<!-- note start -->

**從 provider 刪除開發者時的注意事項**

在 [LINE Developers Console](https://developers.line.biz/console/) 上從 provider 刪除開發者時，如果你勾選 **Also delete the selected developer(s) from the channels that belong to this provider.** 並點選 **OK**，所選的開發者將從該 provider 底下的頻道中一併刪除。

然而，將所選開發者從該 provider 底下的頻道刪除後，可能會導致該頻道沒有任何擁有 admin 角色的開發者。因此，如果你勾選 **Also delete the selected developer(s) from the channels that belong to this provider.**，請確認這些頻道還有其他擁有 admin 角色的開發者。

![](https://developers.line.biz/media/line-developers-console/best-practices-for-provider-and-channel-management/delete-developer-from-provider-en.png)

<!-- note end -->

## Create a provider for each service provider 

| | |
| --- | --- |
| 良好範例 | 分別為 Beverage Manufacturer A 與 Beverage Manufacturer B 各建立一個 provider。 |
| 不良範例 | 為 Beverage Manufacturer A 與 Beverage Manufacturer B 建立一個共用的 provider。 |

服務提供者（service provider，在 LINE MINI App 中稱為 service company）是指提供服務並取得使用者資訊的個別開發者、公司或組織。服務提供者會在 [LINE Developers Console](https://developers.line.biz/console/) 中註冊為一個 provider。因此，請為每個服務提供者各建立一個 provider。

例如，假設 Beverage Manufacturer A 的美國子公司 Beverage Manufacturer B 想為「Sally Cola」開發 LINE Bot。在這種情況下，Beverage Manufacturer B 不應在 provider「Beverage Manufacturer A」底下建立 Messaging API 頻道，而是應為自己建立一個 provider，並在該 provider 底下建立 Messaging API 頻道。

![](https://developers.line.biz/media/line-developers-console/best-practices-for-provider-and-channel-management/create-provider-for-each-service-provider-1-en.png)

如果某家公司（委外方）將使用 LINE Platform 的服務開發委外給其他公司，應為作為主要服務提供者的委外方建立 provider。

例如，Beverage Manufacturer A 分別將使用 LINE Platform 的服務開發委外給 Development Company C 與 Development Company D。在這種情況下，主要服務提供者是身為委外方的 Beverage Manufacturer A。因此，不應為 Development Company C 或 Development Company D 建立 provider，而是應為 Beverage Manufacturer A 建立 provider，並在該 provider 底下建立頻道。

![](https://developers.line.biz/media/line-developers-console/best-practices-for-provider-and-channel-management/create-provider-for-each-service-provider-2-en.png)

## Create channels that you want to link under the same provider 

| | |
| --- | --- |
| 良好範例 | 將想要串聯的頻道建立在同一個 provider 底下。 |
| 不良範例 | 將想要串聯的頻道建立在不同的 provider 底下。 |

如果你要開發串聯多個頻道的服務，請將想要串聯的頻道建立在同一個 provider 底下。將頻道建立在同一個 provider 底下後，同一位使用者在各個頻道中會被指派相同的 [user ID](https://developers.line.biz/en/glossary/#user-id)。頻道日後無法移動到其他 provider，因此請小心，不要把想要串聯的頻道建立在不同的 provider 底下。

例如，為了在使用者登入「Brown Coffee」活動網站時，透過 [add friend option](https://developers.line.biz/en/docs/line-login/link-a-bot/) 鼓勵使用者將「Cony Tea」的 LINE Bot 加為好友，請將「Brown Coffee」的 LINE Login 頻道與「Cony Tea」的 Messaging API 頻道建立在 provider「Beverage Manufacturer A」底下。

![](https://developers.line.biz/media/line-developers-console/best-practices-for-provider-and-channel-management/create-channels-under-the-same-provider-en.png)

請注意，當你將 LINE Platform 用於多項服務時，必須發布 provider 頁面並遵守使用條款，才能串聯從各項服務取得的 LINE 使用者資料。如需更多資訊，請參閱企業客戶選項文件中的 [Cautions on the common use of user IDs](https://developers.line.biz/en/docs/partner-docs/provider-page/#cautions-on-the-common-use-of-user-ids)。

## Create channels by region where you provide services 

| | |
| ------------ | ------------------------------------------------------------- |
| 良好範例 | 依照提供服務的地區分別建立頻道。 |
| 不良範例  | 使用單一頻道對多個地區提供服務。 |

如果你以相同品牌在多個國家或地區提供服務，請為每個地區分別建立頻道，而不要共用單一頻道。

例如，假設 Beverage Manufacturer A 在日本營運其咖啡飲料「Brown Coffee」的活動網站，並決定在台灣與泰國推出同一產品的活動網站。在這種情況下，請在 provider「Beverage Manufacturer A」底下，為每個地區分別建立 LINE Login 頻道。

![](https://developers.line.biz/media/line-developers-console/best-practices-for-provider-and-channel-management/create-channels-by-region-en.png)

## Register a mailing list email address in Email address on the Basic settings tab 

| | |
| --- | --- |
| 良好範例 | 在 **Basic settings** 分頁的 **Email address** 中註冊群組郵寄清單（mailing list）的電子郵件地址。 |
| 不良範例 | 在 **Basic settings** 分頁的 **Email address** 中註冊個人的電子郵件地址。 |

你會在每個頻道的 **Basic settings** 分頁的 **Email address** 中所註冊的電子郵件地址收到重要公告。因此，請在這個 **Email address** 中註冊群組郵寄清單的電子郵件地址，而非個人的電子郵件地址。

例如，在 LINE Login 頻道「Brown Coffee」的 **Basic settings** 分頁上，於 **Email address** 中註冊 Brown 與 Cony 所屬部門的群組郵寄清單電子郵件地址。如此一來，即使 Brown 與 Cony 不在辦公室，該部門也能收到關於該頻道的重要公告。

關於頻道的重要公告，也可以在擁有頻道角色的開發者的電子郵件地址，或在通知中心（notification center）收到。如需更多資訊，請參閱 [Receive notifications via email or the notification center](https://developers.line.biz/en/docs/line-developers-console/notification/)。
