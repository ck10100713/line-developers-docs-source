# 驗證 Webhook 簽章（Verify webhook signature）

當 bot 伺服器收到 webhook 事件時，請先驗證請求標頭中所含的簽章，再處理 [webhook 事件物件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)。這個驗證步驟很重要，可確認該 webhook 確實來自 LINE Platform，且在傳輸過程中未遭竄改。

![Signature verification](https://developers.line.biz/media/partner-docs/webbhook-signature-verification-en.png)

<!-- tip start -->

**我們建議您驗證 webhook 的簽章**

驗證 webhook 簽章是一項重要的安全措施。[Messaging API 開發指引](https://developers.line.biz/en/docs/messaging-api/development-guidelines/#verify-webhook-signature)中也建議驗證 webhook 簽章。

<!-- tip end -->

<!-- tip start -->

**LINE Platform 不會公開 IP 位址**

發送 webhook 的 LINE Platform IP 位址並未對外公開。請透過驗證簽章來確保安全，而不要以 IP 位址控管存取。

<!-- tip end -->

## Preparations required for signature verification 

要驗證 webhook 簽章，您需要該 Messaging API 頻道（channel）的頻道密鑰（channel secret）。

### Get Channel Secret 

在 [LINE Developers Console](https://developers.line.biz/console/) 開啟該頻道的 **Basic settings** 分頁，取得頻道密鑰。您必須擁有該頻道的 Admin 權限才能取得頻道密鑰。

![](https://developers.line.biz/media/messaging-api/verify-webhook-signature/channel-secret-en.png)

頻道密鑰是只有 LINE Platform 與開發者才知道的私密金鑰。此頻道密鑰會作為簽章驗證的雜湊金鑰（hash key），應由 bot 伺服器妥善管理。

#### Reissue Channel Secret 

要重新發行頻道密鑰，請在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Basic Settings** 分頁中點選 **Issue**。如果您擔心頻道密鑰可能已遭洩漏（compromised），請重新發行頻道密鑰。您必須擁有該頻道的 Admin 權限才能重新發行頻道密鑰。

發行新的頻道密鑰會使目前的頻道密鑰失效。在重新發行頻道密鑰之前，請徹底調查對於原本使用既有頻道密鑰的服務會造成的影響。

LINE Platform 不會在未經開發者同意的情況下重新發行頻道密鑰。

## How signature verification works 

簽章驗證是指 webhook 的發送方（LINE Platform）與接收方（開發者營運的 bot 伺服器）都使用相同的雜湊金鑰進行運算，並透過檢查所產生的簽章是否一致，來驗證 webhook 的正當性。

![](https://developers.line.biz/media/messaging-api/verify-webhook-signature/webhook-validation-flow.png)

以下是簽章驗證運作方式的逐步說明。

1. [LINE Platform 將 webhook 發送至 bot 伺服器](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#line-platform-sends-webhook-request)
1. [bot 伺服器接收 webhook](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#receiving-webhook-request)
1. [在 bot 伺服器上驗證 webhook 簽章](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#signature-validation)

### The LINE Platform sends a webhook to the bot server 

LINE Platform 在發送 webhook 時，會依照以下步驟建立簽章：

1. 以 [webhook 事件](https://developers.line.biz/en/reference/messaging-api/#webhook-event-objects)作為輸入資料、以頻道密鑰作為雜湊金鑰，使用 HMAC-SHA256 產生簽章。
2. 將產生的簽章設定至 `x-line-signature` 標頭。
3. 將 webhook 事件與簽章（`x-line-signature`）發送至 bot 伺服器。

![](https://developers.line.biz/media/messaging-api/verify-webhook-signature/line-platform-sends-webhook-request.png)

### The bot server receives the webhook 

bot 伺服器會從 LINE Platform 取得 webhook。

請勿修改所收到 webhook 的[請求標頭](https://developers.line.biz/en/reference/messaging-api/#request-headers)中的簽章（`x-line-signature`）或請求本文字串，並將它們原樣儲存在記憶體或資料庫中。

<!-- note start -->

**在驗證簽章之前請勿修改資料**

如果在簽章驗證之前對簽章或請求本文字串做了任何修改（字串替換、反序列化、跳脫處理等），就會與遭第三方竄改的請求無法區分，導致簽章驗證失敗。無論請求本文字串中是否包含反斜線（`\`）或換行（`\n`）等特殊跳脫字元，皆是如此。在任何請求上驗證簽章之前，都請勿修改資料。

<!-- note end -->

### The webhook signature is verified on the bot server 

bot 伺服器會依照以下方式驗證來自 LINE Platform 的 webhook：

1. 以收到的 Webhook 請求本文中的字串作為輸入資料、以 bot 伺服器管理的頻道密鑰作為雜湊金鑰，使用 HMAC-SHA256 產生簽章。
2. 比對收到的簽章（`x-line-signature`）與產生的簽章。
3. 如果兩個簽章一致，即可保證所收到的 webhook 是由 LINE Platform 發送，且抵達 bot 伺服器時未遭竄改。
4. 如果簽章一致，請依據 webhook 事件的內容採取相應行動。

![](https://developers.line.biz/media/messaging-api/verify-webhook-signature/signature-validation.png)

如果兩個簽章不一致，或 webhook 請求標頭中未包含簽章，請勿處理該 webhook 事件，並以錯誤結束處理流程。如果簽章不一致，可能是因為以下原因：

- bot 伺服器所收到的請求是由 LINE Platform 以外的來源發送
- bot 伺服器所收到的 webhook 已遭第三方竄改
- bot 伺服器驗證簽章的方式有誤

如果該 webhook 是由 LINE Platform 發送，您可以在 LINE Developers Console 的 **Statistics** 下查看您嘗試發送的 webhook 歷史紀錄。關於如何查看錯誤統計資料的詳細資訊，請參閱[查看 webhook 錯誤原因與統計資料](https://developers.line.biz/en/docs/messaging-api/check-webhook-error-statistics/)。

如果 webhook 確實是由 LINE Platform 發送，但簽章仍不一致，那麼 bot 伺服器驗證簽章的方式可能有誤。詳細資訊請參閱[常見的簽章驗證失敗原因與解決方法](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#common-signature-verification-failures-and-their-solutions)。

## Signature verification procedure 

使用 `openssl` 指令來檢視簽章驗證的流程。

首先，從 [LINE Developers Console](https://developers.line.biz/console/) 開啟該頻道的 **Messaging API** 分頁，並點選 webhook URL 的 **Verify**，讓 LINE Platform 發送一個確認用的 webhook。

![Click Verify to send a webhook to confirm communication.](https://developers.line.biz/media/news/webhook-url-verify-button.png)

1. 發送至 bot 伺服器的 Webhook 請求本文
   ```json
   {"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[]}
   ```
1. 發送至 bot 伺服器的 webhook 簽章（`x-line-signature`）
   ```
   GhRKmvmHys4Pi8DxkF4+EayaH0OqtJtaZxgTD9fMDLs=
   ```
1. 該頻道的頻道密鑰
   ```
   8c570fa6dd201bb328f1c1eac23a96d8
   ```
1. 在 bot 伺服器上驗證簽章的指令
   ```sh
   echo -n '{"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[]}' | openssl dgst -sha256 -hmac '8c570fa6dd201bb328f1c1eac23a96d8' -binary | openssl base64
   ```
1. 由 bot 伺服器產生的簽章
   ```
   GhRKmvmHys4Pi8DxkF4+EayaH0OqtJtaZxgTD9fMDLs=
   ```

由於從 LINE Platform 收到的步驟 2 簽章，與 bot 伺服器產生的步驟 5 簽章一致，因此我們確認 bot 伺服器所收到的 webhook 是由 LINE Platform 發送，且未遭竄改。

在實際開發中，您可以使用 [LINE Messaging API SDK](https://developers.line.biz/en/docs/messaging-api/line-bot-sdk/) 輕鬆驗證簽章。各語言的實作範例請參閱 Messaging API Reference 中的 [Signature validation](https://developers.line.biz/en/reference/messaging-api/#signature-validation)。

## Common signature verification failures and their solutions 

如果 webhook 確實是由 LINE Platform 發送，但簽章仍不一致，那麼 bot 伺服器驗證簽章的方式可能有誤。

以下列出一些常見的簽章驗證失敗原因，以及解決方法。

- [Webhook 在抵達 bot 伺服器前遭到變更](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#modified-webhook-request-before-it-reaches-the-bot-server)
- [剖析與反序列化 webhook](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#parsing-or-deserializing-webhook-request)
- [Webhook 請求本文字串（JSON）格式不正確](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#formatted-webhook-event)
- [使用了 HMAC-SHA256 以外的演算法來驗證簽章](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#used-incorrect-algorithm-for-signature-validation)
- [使用了其他頻道的頻道密鑰](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#used-wrong-channel-secret)
- [其他開發者重新發行了頻道密鑰](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#reissued-channel-secret)
- [跳脫字元被解譯](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#interpreted-escape-characters)
- [處理 webhook 時使用的字元編碼不是 UTF-8](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#non-utf8-encoding-for-webhook-processing)

### Webhook changed before reaching the bot server 

如果您在簽章驗證之前對 webhook 的 `x-line-signature` 或請求本文字串做了任何變更，簽章驗證就會失敗。

請確保在 webhook 抵達您的 bot 伺服器之前，沒有任何代理伺服器（proxy）或負載平衡器修改了請求標頭或本文。

### Parsing and deserializing webhooks 

如果您在驗證簽章之前，剖析或反序列化所收到 webhook 請求本文中的字串並將其轉換為物件或陣列，簽章驗證就會失敗。

1. bot 伺服器所收到的 Webhook 請求本文
   ```json
   {"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[]}
   ```
1. 反序列化並輸出 webhook 請求本文
   ```python
   decoded_data = json.loads('{"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[]}')
   print(decoded_data)
   ```
1. 反序列化已將雙引號改為單引號，且／或加入了空格
   ```python
   {'destination': 'U8e742f61d673b39c7fff3cecb7536ef0', 'events': []}
   ```

進行簽章驗證時，請使用所收到 webhook 請求本文中的精確字串。

### Incorrect formatting of the webhook request body string (JSON) 

如果您在驗證簽章之前，為了方便開發者檢視而將所收到 webhook 的 JSON 請求本文格式化，簽章驗證就會失敗。

1. bot 伺服器所收到的 Webhook 請求本文
   ```json
   {"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[]}
   ```
1. 當 webhook 請求本文字串（JSON）被格式化時，簽章驗證會失敗
   ```json
   {
     "destination": "U8e742f61d673b39c7fff3cecb7536ef0",
     "events": []
   }
   ```

進行簽章驗證時，請使用所收到 webhook 請求本文中的精確字串。

### An algorithm other than HMAC-SHA256 was used to verify the signature 

如果在簽章驗證過程中使用了 HMAC-SHA256 以外的演算法，簽章驗證就會失敗。

請確認您沒有誤用 HMAC-SHA1 等 HMAC-SHA256 以外的演算法來產生簽章。

### Used a channel secret for a different channel 

如果您使用了所收到 webhook `destination` 中所指定 bot 以外頻道的頻道密鑰，簽章驗證就會失敗。

要驗證簽章，webhook 的發送方（LINE Platform）與接收方（開發者營運的 bot 伺服器）都必須使用相同的雜湊金鑰進行運算。頻道密鑰即對應此雜湊金鑰，且每個頻道各不相同。

請在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Basic settings** 分頁中確認 Channel secret 的值。

### Another developer has reissued the channel secret 

當在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Basic settings** 分頁中發行新的頻道密鑰時，先前的頻道密鑰就會失效。

如果原本正常運作的簽章驗證突然開始失敗，有可能是擁有同一頻道 admin 權限的其他開發者重新發行了頻道密鑰。

請在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Basic settings** 分頁中確認目前的頻道密鑰值。如果頻道密鑰已被重新發行，就必須將 bot 伺服器上用於簽章驗證的頻道密鑰更換為新的頻道密鑰。

### Interpreted escape characters 

所收到 webhook 的請求本文可能包含反斜線（`\`）或換行（`\n`）等特殊跳脫字元。如果未妥善處理跳脫字元而將其加以解譯，簽章驗證就會失敗。

例如，在本機環境中使用 `echo` 指令檢查簽章驗證的運作時，請以單引號而非雙引號將跳脫字元括起來，使其按原樣處理。

```sh
echo -n '{"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[]}' | openssl dgst -sha256 -hmac '8c570fa6dd201bb328f1c1eac23a96d8' -binary | openssl base64
```

在 Python 中，您可以使用原始字串字面值（raw string literal，`r"..."`）來按原樣處理跳脫字元。

```python
body = r'{"destination":"U8e742f61d673b39c7fff3cecb7536ef0","events":[{"type":"message","text":"hello\ntest1\ntest2"}]}'
```

驗證簽章時，請勿解譯跳脫字元，並按原樣使用所收到 webhook 請求本文中的字串。

### Character encoding used when processing webhooks wasn't UTF-8 

來自 LINE Platform 的 webhook 是以 UTF-8 編碼發送（`Content-Type: application/json; charset=utf-8`）。

使用所收到的 webhook 請求本文驗證簽章時，如果以 UTF-8 以外的編碼處理資料，換行碼可能會從 LF（`\n`）變成 CRLF（`\r\n`），表情符號與特殊字元（tab、控制字元等）也可能被誤判，導致簽章驗證失敗。

驗證簽章時，請確保字元編碼為 UTF-8。
