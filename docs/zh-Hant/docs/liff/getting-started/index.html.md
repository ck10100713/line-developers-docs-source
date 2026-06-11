# 建立頻道（Create a channel）

要開發 LIFF app，您必須先在 [LINE Developers Console](https://developers.line.biz/console/) 上建立一個 provider 與一個頻道（channel）。

## Log in to the LINE Developers Console 

要建立 provider 與頻道，您必須先登入 LINE Developers Console。關於如何登入的詳細資訊，請參閱 [Log in to the LINE Developers Console](https://developers.line.biz/en/docs/line-developers-console/login-account/)。

## Creating a provider and channel 

登入 [LINE Developers Console](https://developers.line.biz/console/) 並建立一個 provider 與一個頻道。

### 1. Create a provider 

如果您已經有想要使用的 provider，請前往 [2. Create a channel](https://developers.line.biz/en/docs/liff/getting-started/#step-two-create-channel)。

1. 在 Console 首頁，點擊 **Create a new provider** 按鈕。

   <!-- note start -->

   **如果找不到 Create a new provider 按鈕**

   如果您已經建立過 provider，**Create a new provider** 按鈕就不會顯示在 Console 首頁。如果您想再建立一個，請點擊 Console 首頁 **Providers** 區段中的 **Create** 按鈕。

   ![Create button in the Providers section](https://developers.line.biz/media/liff/getting-started/providers-section-en.png)

   <!-- note end -->

1. 在 **Create a new provider** 畫面中輸入任意的 **Provider name**，並點擊 **Create** 按鈕。

   **provider** 可以是透過 LINE Platform 提供服務的個人、公司或組織。請輸入您自己的名稱或公司名稱作為 provider 名稱。

   ![Create a provider](https://developers.line.biz/media/liff/getting-started/create-provider-en.png)

### 2. Create a channel 

**頻道（channel）** 是 LINE Platform 的功能與 provider 服務之間的通訊路徑。頻道必須具備名稱、說明與圖示影像。

LIFF app 可以新增至以下這兩種頻道類型：

| Type | Description |
| --- | --- |
| [LINE Login](https://developers.line.biz/en/docs/line-login/) | 如果您想建立 LIFF app、想在下一步驟[試用 LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/)，或想[使用 Create LIFF App 建置 LIFF app 開發環境](https://developers.line.biz/en/docs/liff/cli-tool-create-liff-app/)，請建立 LINE Login 頻道。 |
| [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/)  | 如果您想使用 [LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/quickstart/) 建立 LIFF app，請建立 LINE MINI App 頻道。 |

<!-- tip start -->

**我們建議將 LIFF app 建立為 LINE MINI App**

未來，LIFF 與 LINE MINI App 將整合為單一品牌。整合的結果是，LIFF 將被併入 LINE MINI App。基於這個原因，我們建議您將新的 LIFF app 建立為 LINE MINI App。詳細資訊請參閱 [2025 年 2 月 12 日](https://developers.line.biz/en/news/2025/02/12/line-mini-app/)的消息。

<!-- tip end -->

在本節中，我們將假設您想在下一步驟[試用 LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/)，示範如何建立 LINE Login 頻道。請點擊您想新增 LINE Login 頻道的 provider，並建立您的頻道。如果已經有想要使用的 LINE Login 頻道，請選取它。關於如何建立頻道的詳細資訊，請參閱 [Creating a channel](https://developers.line.biz/en/docs/line-developers-console/overview/#creating-a-channel)。

<!-- note start -->

**頻道名稱的限制**

頻道名稱中不可包含「LINE」或類似的字串。

<!-- note end -->

<!-- note start -->

**關於頻道的 App types**

開發 LIFF app 時，請在 App types 中選取 **Web app**。

<!-- note end -->

<!-- note start -->

**您無法將 LIFF app 新增至 LINE Login 與 LINE MINI App 以外的頻道**

您無法將 LIFF app 新增至以下這些頻道類型：

- Messaging API
- Blockchain Service

過去，LIFF app 可以新增至 Messaging API 頻道或 Blockchain Service 頻道。然而，對於已經新增至 Messaging API 與 Blockchain service 頻道的 LIFF app，新的 LIFF 功能將無法使用。詳細資訊請參閱以下消息文章。

- 2020 年 2 月 5 日的消息，[Users can no longer add LIFF apps to Messaging API channels](https://developers.line.biz/en/news/2020/02/05/liff-channel-type/)
- 2021 年 7 月 20 日的消息，[Users can no longer add LIFF apps to Blockchain Service channels](https://developers.line.biz/en/news/2021/07/20/liff-cannot-be-used-with-blockchain-service-channels/)

<!-- note end -->

#### Precautions for channel and provider linkage 

頻道一旦建立後，之後就無法將該頻道移動到其他 provider。

當開發將 LINE Login 頻道與 Messaging API 頻道連結的服務時，請在同一個 provider 內建立這兩個頻道。

使用開發者所提供服務的 LINE 使用者，會針對每個 provider 取得不同的使用者 ID。使用者 ID 無法用來識別不同 provider 下各頻道之間的同一位使用者。

![](https://developers.line.biz/media/line-developers-console/different-user-ids.png)

<!-- warning start -->

**建立頻道時需要特別注意的情況**

舉例來說，以下這些情況需要特別注意：

- 頻道與 provider 由個人或公司管理。
- 在一個 provider 下建立不相關服務或公司的頻道。
- 在由營運頻道管理工具等的服務（公司）所管理的 provider 下建立頻道。

在這類情況下，由於之後無法在 provider 之間移動頻道，以及使用者在不同 provider 下會取得不同的使用者 ID，未來可能會產生問題。在審慎考量所涉及的風險之後，請在適當的 provider 下建立頻道。

<!-- warning end -->

## Next steps 

您現在已經為您的 LIFF app 建立了一個頻道。接下來，請執行以下其中一項：

- [試用 LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/)
- [開發 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/)
