# 開始使用 LINE MINI App（Get started with LINE MINI App）

LINE MINI App 是一種在 LINE 上執行的網頁應用程式。

開發者運用這個平台，無須另外開發獨立的原生應用程式（native app），即可提供自己的服務。

同樣地，使用者也能用自己的 LINE 帳號，在 LINE 內享受各種服務，而不必另外下載獨立的應用程式。

## Process from LINE MINI App development to release 

開發並發布 LINE MINI App 的整體流程如下：

1. 建立 LINE MINI App 頻道（channel）後，您就可以開始[開發 LINE MINI App](https://developers.line.biz/en/docs/line-mini-app/develop/develop-overview/)。在這個階段，它會以未驗證 MINI App 的身分發布。
1. [提交您的 LINE MINI App 進行審查](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)。
1. 若通過審查，您就能以已驗證 MINI App 的身分[提供您的服務](https://developers.line.biz/en/docs/line-mini-app/service/service-operation/)。

## Common Guidelines 

無論您擔任什麼角色，都可以查看開發 LINE MINI App 的整體工作流程。

- [**了解 LINE MINI App 的基礎知識**](https://developers.line.biz/en/docs/line-mini-app/discover/introduction/)：了解 LINE MINI App 內建的標準功能，以及您可以自行實作的自訂功能。
  - [LINE MINI App specifications](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)
  - [Built-in Features](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/)
  - [Custom Features](https://developers.line.biz/en/docs/line-mini-app/discover/custom-features/)
  - [LINE MINI App UI components](https://developers.line.biz/en/docs/line-mini-app/discover/ui-components/)

## Guideline per Role 

請依照各角色提供的指引，查看開發 LINE MINI App 的工作流程。

### Guideline for Service Planners 

如果您負責設計透過 LINE MINI App 提供的服務，以下是您應留意的事項。

- [**查看 LINE MINI App Policy**](https://terms2.line.me/LINE_MINI_App?lang=en) 在規劃階段，請瀏覽 LINE MINI App Policy。在提交您的 LINE MINI App 進行審查之前，請確認您的 LINE MINI App 符合 LINE MINI App Policy。

### Guideline for Developers 

如果您負責開發與實作 LINE MINI App，以下是您應留意的事項。

- [**LINE MINI App specifications**](https://developers.line.biz/en/docs/line-mini-app/discover/specifications/)：查看哪些功能在哪些平台的哪些版本上受支援，以及 LIFF 的支援版本。
- **Guideline for Developers**
  - [**Getting started**](https://developers.line.biz/en/docs/line-mini-app/develop/develop-overview/)：在開發 LINE MINI App 之前，請花點時間閱讀。
  - [**Implement a custom action button**](https://developers.line.biz/en/docs/line-mini-app/develop/share-messages/)：您可以自訂用於與好友分享 LINE MINI App 的分享訊息。
  - [**Sending a service message**](https://developers.line.biz/en/docs/line-mini-app/develop/service-messages/)：您可以傳送服務訊息（service message），作為對使用者操作的確認或回應。
  - [**Using a payment system**](https://developers.line.biz/en/docs/line-mini-app/develop/payment/)：可將 LINE Pay 及其他支付系統整合至 LINE MINI App，為使用者提供支付系統。
  - [**Creating a permanent link**](https://developers.line.biz/en/docs/line-mini-app/develop/permanent-links/)：您可以使用 LINE MINI App 的永久連結（permanent link），讓使用者能立即存取您的 LINE MINI App。
  - [**Managing LINE MINI App settings on LINE Developers Console**](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/)：LINE MINI App 會使用在 LINE Developers Console 上設定的資料，因此請務必在 LINE Developers Console 上設定正確的資料。
  - [**Open a LINE MINI App in an external browser**](https://developers.line.biz/en/docs/line-mini-app/develop/external-browser/)：查看在外部瀏覽器中開啟 LINE MINI App 的注意事項。
  - [**Check the performance guide**](https://developers.line.biz/en/docs/line-mini-app/develop/performance-guidelines/)：我們建議您瀏覽 LINE MINI App Performance Guide。
- **API References**
  - [Service Message API](https://developers.line.biz/en/reference/line-mini-app/#service-messages)
  - [LIFF API](https://developers.line.biz/en/reference/liff/)
  - [LINE Pay API](https://developers-pay.line.me/online-api-v3)
- [**Submit a request for review**](https://developers.line.biz/en/docs/line-mini-app/submit/submission-guide/)：只有經認定遵循指引的 LINE MINI App 才會成為已驗證 MINI App。若要讓您的 LINE MINI App 成為已驗證 MINI App，請提交審查申請。

### Guideline for Designers 

如果您負責設計 LINE MINI App 頁面，以下是您應留意的事項。

- [**LINE MINI App icon specifications and guidelines**](https://developers.line.biz/en/docs/line-mini-app/design/line-mini-app-icon/)：依照指引製作圖示，並在 LINE Developers Console 上設定頻道圖示。如需更多資訊，請參閱 [Managing LINE MINI App settings on LINE Developers Console](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/)。
- [**Check the safe area for landscape mode**](https://developers.line.biz/en/docs/line-mini-app/design/landscape/)：為了讓您的 LINE MINI App 各部分都能顯示，即使在有瀏海（notch）的裝置上也是如此，請使用 CSS 將 LINE MINI App 限制在安全區域（safe area）內。
- [**Check your loading icon**](https://developers.line.biz/en/docs/line-mini-app/design/loading-icon/)：載入圖示（loading icon）是 LINE MINI App 建議採用的 UI 元素。請使用指定的檔案。

### Guideline for Service Operators and Marketers 

如果您負責營運與推廣透過 LINE MINI App 提供的服務，以下是您應留意的事項。

- [**Check the Service Operation Guide**](https://developers.line.biz/en/docs/line-mini-app/service/service-operation/)：為了實際營運，請務必了解透過永久連結分享您的 LINE MINI App、以及傳送服務訊息等相關事項。
  - [Know-Hows for service providers](https://developers.line.biz/en/docs/line-mini-app/service/service-operation/)
  - [Place ads in LINE MINI Apps](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-ads/)
  - [Re-review after updating your verified MINI App](https://developers.line.biz/en/docs/line-mini-app/service/update-service/)
  - [Use LINE Official Account](https://developers.line.biz/en/docs/line-mini-app/service/line-mini-app-oa/)
