# 將 LIFF app 新增至頻道（Adding a LIFF app to your channel）

當你在 [LINE Developers Console](https://developers.line.biz/console/) 上將 LIFF app 新增至 LINE Login 頻道時，這個 LIFF app 可以在 LINE 內或外部瀏覽器中執行。

<!-- tip start -->

**我們建議將 LIFF app 建立為 LINE MINI App**

未來，LIFF 與 LINE MINI App 將整合為單一品牌。隨著這項整合，LIFF 將被整合進 LINE MINI App。因此，我們建議你將新的 LIFF app 建立為 LINE MINI App。詳情請參閱 [2025 年 2 月 12 日](https://developers.line.biz/en/news/2025/02/12/line-mini-app/)的消息。

<!-- tip end -->

## Before you begin 

請確認你已完成以下事項：

- 為你的 app [建立頻道](https://developers.line.biz/en/docs/liff/getting-started/)。
- 依照[試用 LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/) 或[開發 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/)中的說明，將 LIFF app 部署到任一伺服器上。

## Adding the LIFF app to your channel 

每個頻道（channel）最多可以新增 30 個 LIFF app。

1. 在 [LINE Developers Console](https://developers.line.biz/console/) 上，選取你想新增 LIFF app 的 LINE Login 頻道，然後點擊 **LIFF** 分頁。

1. 點擊 **Add**。

1. 依照下列順序設定以下項目。你之後隨時可以變更這些設定：

   **Basic information**

   | Item | Description | Location displayed to users |
   | --- | --- | --- |
   | LIFF app name | LIFF app 的名稱。LIFF app 名稱不可包含「LINE」或類似字串，也不可包含不適當的字串。 | <ul><li>[開啟另一個 LIFF app 時顯示的訊息](https://developers.line.biz/en/docs/liff/opening-liff-app/#messages-liff-to-liff)</li><li>[多分頁檢視（Multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)</li></ul> |
   | Size | LIFF app 檢視畫面的大小。請從以下選項中擇一：<ul><li>`Compact`</li><li>`Tall`</li><li>`Full`</li></ul><br/><img src="/media/liff/overview/viewTypes.png" width="375px"> | - |
   | Endpoint URL | LIFF web app 的 URL（例如 `https://example.com`）。當使用 LIFF URL 啟動 LIFF app 時，會使用這個 URL。<br />URL scheme 必須為 **https**。不可指定 URL 片段（#URL-fragment）。 | [LIFF 瀏覽器（LIFF browser）](https://developers.line.biz/en/docs/liff/overview/#liff-browser)標頭（僅顯示網域名稱） |
   | Scopes \*1 | 部分 LIFF SDK 方法運作時所需的範圍（scope）。<ul><li>`openid`：使用 [`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token) 與 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 時所需的範圍。</li><li>`email`：使用 [`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token) 或 [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) 取得使用者電子郵件地址時所需的範圍。\*2 <li>`profile`：使用 [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 或 [`liff.getFriendship()`](https://developers.line.biz/en/reference/liff/#get-friendship) 時所需的範圍。</li><li>`chat_message.write`：使用 [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) 時所需的範圍。視你的帳號類型而定，此選項可能會顯示在 **View all** 底下。\*3</li></ul> | 啟動 LIFF app 時的權限同意畫面 |
   | Add friend option \*4 | [加入好友選項（add friend option）](https://developers.line.biz/en/docs/line-login/link-a-bot/)的設定<ul><li>`On (normal)`：在 LIFF app 權限同意畫面上新增將 LINE 官方帳號加入好友的選項。</li><li>`On (aggressive)`：在 LIFF app 權限同意畫面之後顯示一個畫面，以確認使用者是否要將 LINE 官方帳號加入好友。</li><li>`Off`：不顯示將 LINE 官方帳號加入好友的選項。</li></ul> | 啟動 LIFF app 時的權限同意畫面 |

   **Options**

   | Item | Description |
   | --- | --- |
   | Scan QR | 在此頻道新增的 LIFF app 中使用 [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) 時，請啟用這項設定。 |
   | Module mode  | 在 module mode 下使用 LIFF app 時，請啟用這項設定。啟用 **Module mode** 後，標頭中的動作按鈕會被隱藏。只有在 LIFF app 檢視畫面大小選取 **Full** 時，才會顯示這個選項。 |

   \*1 關於顯示給已註冊使用這些範圍的企業客戶的範圍詳情，請參閱企業客戶選項文件中的 [LINE Profile+](https://developers.line.biz/en/docs/partner-docs/line-profile-plus/)。</br> \*2 只有在你於 LINE Login 頻道申請了 OpenId Connect email 權限時才會顯示。<br> \*3 在 LIFF 與 LIFF 之間轉換後，LIFF app 中的 `chat_message.write` 範圍可能會被停用。詳情請參閱[關於在 LIFF app 之間轉換後的「chat_message.write」範圍](https://developers.line.biz/en/docs/liff/opening-liff-app/#about-chat-message-write-scope)。<br> \*4 僅針對 LINE Login 頻道顯示。

1. 點擊 **Add**。

   新增 LIFF app 時，會建立一組 LIFF ID 與 LIFF URL。

   | Item | Description |
   | --- | --- |
   | LIFF ID | LIFF app ID。<br>例如 `1234567890-AbcdEfgh` |
   | LIFF URL | 用來存取 LIFF app 的 URL。當使用者存取 LIFF URL 時，會經由 LY Corporation 提供的 LIFF 伺服器，被重新導向至開發者提供的 LIFF app 伺服器（端點 URL）。<br>例如 `https://liff.line.me/1234567890-AbcdEfgh` |

## The order of LIFF apps on the LIFF tab 

在 LINE Login 頻道的 **LIFF** 分頁上，LIFF app 會以下列順序顯示：

1. 於 2023 年 5 月 23 日當天或之後新增至 LINE Login 頻道的 LIFF app，會依新增日期由新到舊的順序顯示
1. 於 2023 年 5 月 23 日之前新增至 LINE Login 頻道的 LIFF app，則不依特定順序顯示

![LIFF 分頁上顯示的 LIFF app 範例](https://developers.line.biz/media/liff/order-of-liff-apps-en.png)

## Other operations 

你也可以從 LINE Developers Console 的 **LIFF** 分頁執行以下操作。

- 編輯 LIFF app 設定
- 從頻道中刪除 LIFF app

## Next steps 

將 LIFF app 新增至頻道後，試著開啟它。

- [開啟 LIFF app](https://developers.line.biz/en/docs/liff/opening-liff-app/)
