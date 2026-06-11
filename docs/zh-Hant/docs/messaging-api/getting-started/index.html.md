# 開始使用 Messaging API（Get started with the Messaging API）

若要使用 Messaging API，您必須擁有一個頻道（channel）。若要建立頻道，請先建立一個 [LINE 官方帳號（LINE Official Account）](https://developers.line.biz/en/glossary/#line-official-account)，並為您的 LINE 官方帳號啟用 Messaging API 的使用。

本頁說明如何透過下列兩個步驟來建立 Messaging API 頻道：

1. [建立 LINE 官方帳號](https://developers.line.biz/en/docs/messaging-api/getting-started/#create-oa)
1. [為您的 LINE 官方帳號啟用 Messaging API](https://developers.line.biz/en/docs/messaging-api/getting-started/#using-oa-manager)

若要為既有的 LINE 官方帳號啟用 Messaging API，請參閱步驟 2。

<!-- tip start -->

**什麼是頻道（channel）？**

**頻道（channel）**是供應商（provider）在其服務中使用 LINE Platform 功能（例如 Messaging API 與 LINE Login）的通訊路徑。若要使用 LINE Platform，您必須擁有一個頻道。接著，您就可以使用頻道的資訊（例如存取權杖）來使用 Messaging API 的各項功能。

![](https://developers.line.biz/media/messaging-api/getting-started/channel.png)

<!-- tip end -->

## 1. Create a LINE Official Account 

若要使用 Messaging API，您必須先建立一個 LINE 官方帳號。LINE 官方帳號可依下列步驟建立：

- [步驟 1-1. 註冊 Business ID](https://developers.line.biz/en/docs/messaging-api/getting-started/#create-oa-business-id)
- [步驟 1-2. 填寫申請表單](https://developers.line.biz/en/docs/messaging-api/getting-started/#create-oa-entry-form)
- [步驟 1-3. 確認您的 LINE 官方帳號](https://developers.line.biz/en/docs/messaging-api/getting-started/#create-oa-check)

### Step 1-1. Register for Business ID 

若要建立 LINE 官方帳號，您需要註冊 [Business ID](https://account.line.biz/signup?redirectUri=https://entry.line.biz/form/entry/unverified)。您可以使用您的 LINE 帳號或電子郵件位址來註冊 Business ID。

![](https://developers.line.biz/media/messaging-api/getting-started/sign-up-business-id-en.png)

### Step 1-2. Fill in the entry form 

當您註冊好 Business ID 後，LINE 官方帳號的[申請表單](https://entry.line.biz/form/entry/unverified)就會出現。請在此表單中填寫必填資訊。完成表單後，您的 LINE 官方帳號就會建立完成。

![](https://developers.line.biz/media/messaging-api/getting-started/oa-entry-form-en.png)

### Step 1-3. Check your LINE Official Account 

以上步驟會建立您的 LINE 官方帳號。您可以在 [LINE 官方帳號管理後台（LINE Official Account Manager）](https://manager.line.biz/)查看已建立的 LINE 官方帳號。

![](https://developers.line.biz/media/messaging-api/getting-started/oa-manager-list-en.png)

確認您的 LINE 官方帳號已建立後，請繼續進行步驟 2。

## 2. Enable the Messaging API for your LINE Official Account 

當您為已建立的 LINE 官方帳號啟用 Messaging API 的使用後，系統便會建立一個 Messaging API 頻道。請依下列步驟，從 [LINE 官方帳號管理後台（LINE Official Account Manager）](https://manager.line.biz/)啟用 Messaging API 的使用：

- [步驟 2-1. 啟用 Messaging API 的使用](https://developers.line.biz/en/docs/messaging-api/getting-started/#step-one-enable-use-of-messaging-api)
- [步驟 2-2. 登入 LINE Developers Console](https://developers.line.biz/en/docs/messaging-api/getting-started/#step-two-log-in-to-line-developers-console)
- [步驟 2-3. 確認您已擁有頻道](https://developers.line.biz/en/docs/messaging-api/getting-started/#step-three-confirm-channel)

### Step 2-1. Enable the use of the Messaging API 

當您在 [LINE 官方帳號管理後台（LINE Official Account Manager）](https://manager.line.biz/)中啟用 Messaging API 的使用時，系統便會建立一個 Messaging API 頻道。詳情請參閱 LINE for Business 中的 [Messaging API](https://www.lycbiz.com/jp/manual/OfficialAccountManager/account-settings_messaging_api/)（僅提供日文版）。

如果您用來登入 [LINE 官方帳號管理後台（LINE Official Account Manager）](https://manager.line.biz/)的帳號從未在 [LINE Developers Console](https://developers.line.biz/console/) 上使用過，畫面上會出現用於註冊開發者資訊的畫面。請輸入您的姓名與電子郵件，以建立開發者帳號。

![](https://developers.line.biz/media/messaging-api/getting-started/developer-registration-en.png)

接著，選擇一個供應商（provider）來管理您的 LINE 官方帳號。如果您打算將 LINE 官方帳號與既有的頻道（例如 LINE Login 頻道）整合，請選擇要整合的頻道所屬的供應商。

<!-- note start -->

**選擇供應商時請務必小心**

一旦您指定某個供應商來管理您的 LINE 官方帳號，便無法變更或取消指定該供應商。

<!-- note end -->

<!-- warning start -->

**選擇供應商時需特別注意的情況**

例如，下列情況需要特別注意：

- 頻道與供應商由個人或公司管理。
- 在同一個供應商底下建立彼此無關的服務或公司的頻道。
- 在由經營頻道管理工具等的服務（公司）所管理的供應商底下建立頻道。

在這類情況下，由於日後無法在供應商之間移動頻道，且使用者在不同供應商會被賦予不同的使用者 ID，未來可能會衍生問題。請在審慎評估相關風險後，選擇適當的供應商。

<!-- warning end -->

### Step 2-2. Log in to the LINE Developers Console 

已建立的 Messaging API 頻道可以在 LINE Developers Console 中進行設定。請使用您登入 [LINE 官方帳號管理後台（LINE Official Account Manager）](https://manager.line.biz/)時所用的帳號，登入 [LINE Developers Console](https://developers.line.biz/console/)。

![](https://developers.line.biz/media/messaging-api/getting-started/login-dialog.png)

### Step 2-3. Check that you have a channel 

選擇您在[步驟 2-1](https://developers.line.biz/en/docs/messaging-api/getting-started/#step-one-enable-use-of-messaging-api)中選擇的供應商。確認該供應商底下已建立一個頻道。

![](https://developers.line.biz/media/messaging-api/getting-started/console-home-en.png)

## [End-of-life] Create a channel in the LINE Developers Console 

現在已無法再直接從 LINE Developers Console 建立 Messaging API 頻道。詳情請參閱 2024 年 9 月 4 日的最新消息：[自 2024 年 9 月 4 日起，已無法再直接從 LINE Developers Console 建立 Messaging API 頻道](https://developers.line.biz/en/news/2024/09/04/no-longer-possible-to-create-messaging-api-channels-from-console/)。

## Next steps 

現在您已擁有頻道，便可以開始使用 Messaging API 了。在以下頁面中，您將設定頻道以建立機器人（bot）：

- [建立機器人](https://developers.line.biz/en/docs/messaging-api/building-bot/)
