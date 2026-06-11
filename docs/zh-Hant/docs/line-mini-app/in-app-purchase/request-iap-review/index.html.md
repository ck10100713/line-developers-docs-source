# 申請使用應用程式內購買（Apply to use in-app purchase）

本頁說明如何申請使用應用程式內購買（in-app purchase）。

## Things to check prior to applying 

在申請使用應用程式內購買之前，請務必詳閱「[In-app purchase overview](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/overview/)」與「[In-app purchase development guidelines](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-guidelines/)」。此外，也請留意以下事項。

### Relationship between the in-app purchase review and the verification review 

- 即使應用程式內購買審查已完成，除非通過[驗證審查（以已驗證的 MINI App 形式發布之審查）](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)，否則使用者仍無法使用應用程式內購買。
- 在驗證審查期間，您無法申請應用程式內購買。
- 在應用程式內購買審查期間，您無法申請驗證審查。

### In-app purchase review period 

- LY Corporation 完成應用程式內購買審查約需兩週時間。您無法事先指定審查的完成日期，敬請見諒。
- 若您的申請在審查後遭到拒絕，重新申請與重新審查的流程將需要再多花費數天時間。
- 在您的應用程式內購買申請通過後，您必須申請[驗證審查（verification review）](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)。此審查也有另外的審查期間。

## Application flow 

如要申請使用應用程式內購買，請依照以下步驟進行。

### 1. Enter the required information 

在 [LINE Developers Console](https://developers.line.biz/console/) 的 **In-app purchase** 分頁中輸入必要資訊。

申請時，請正確輸入所有資訊，包括公司名稱：

- 註冊 Business information / LINE MINI App information
- 註冊 Information security 資訊
- 上傳 LY Corporation business partner information 申請表

#### In-app purchase contract entity 

使用應用程式內購買時，以下資訊必須全部與相關 LINE MINI App 頻道（channel）**Business information** 分頁中「Service company information」區段所設定的資訊一致：

- 「Business information / LINE MINI App information」區段
  - **Company name**
- 「Information security」區段
  - **Name of the organization performing the operations**
- 「LY Corporation business partner information」區段中的 LY Corporation business partner information 申請表
  - Your company information - Company name
  - Payment account information - Account holder name

### 2. Apply to use in-app purchase 

當您完成輸入必要資訊後，請點選 **Apply to use in-app purchase** 按鈕。

LY Corporation 將審查您的申請，並決定是否核准或拒絕。當申請獲得核准時，「Workflow in progress」區段中的狀態顯示會變更為「Approved」。

<!-- tip start -->

**在審查開始前，您可以取消申請**

當您申請使用應用程式內購買後，在審查實際開始之前，工作流程狀態會顯示為「Applied for review」。在「Applied for review」狀態期間，您可以取消申請。

<!-- tip end -->

### 3. Configure after approval 

當您的應用程式內購買使用申請獲得核准，且狀態變更為「Approved」後，**Apply to use in-app purchase** 分頁與 **In-app purchase settings** 分頁將會顯示出來。

![](https://developers.line.biz/media/line-mini-app/in-app-purchase/tabs-in-iap-tab-en.png)

如需更多關於在 **In-app purchase settings** 分頁中應設定哪些項目的資訊，請參閱 [Set up in-app purchase](https://developers.line.biz/en/docs/line-mini-app/in-app-purchase/iap-settings/)。

## Change application information 

如要修改您的申請資訊，請選擇 **Apply to use in-app purchase** 分頁並編輯相關項目。

- 若您已申請應用程式內購買審查，且「Workflow in progress」中的狀態為「Applied for review」或「Reviewing」，則無法編輯資訊。
  - 若狀態為「Applied for review」：請點選 **Cancel the application** 取消申請，然後再進行編輯。
  - 若狀態為「Reviewing」：在您的申請審查期間無法取消。請在審查完成後再更新資訊。
- 若您在 **Apply to use in-app purchase** 分頁中變更資訊，則需要重新申請應用程式內購買。
- **In-app purchase settings** 分頁中的資訊（webhook URL 與測試者資訊）不需要重新審查。
- 若與公司相關的資訊有所變更，請先完成[驗證審查（verification review）](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)的重新申請，然後再重新申請應用程式內購買審查。
