# LINE Ads API 開發準則（LINE Ads API development guidelines）

使用 LINE Ads API 進行開發時，請遵循以下開發準則：

<!-- table of contents -->

## Prohibiting mass requests to the LINE Platform 

請勿以負載測試或運作測試為目的，向 LINE Platform 發送大量請求。

無論基於任何目的，都請勿發送超過指定速率限制（rate limit）的請求。如需更多關於速率限制的資訊，請參閱 [Ad Tech API documentation](https://ads.line.me/public-docs/certificated-ad-tech-general-partner) 與 [Data Provider API documentation](https://ads.line.me/public-docs/data-general-partner)。

<!-- note start -->

**Note**

如果您發送的請求超過速率限制，將會收到 `429 Too Many Requests` 的錯誤訊息。

<!-- note end -->

## Prohibiting requests for non-existent IDs 

發送請求時，請勿指定不存在的 ID（`Ad account ID`、`Ad ID` 等）。

## Saving logs 

我們建議將 API 請求的日誌（log）保存一段時間，以便當問題發生時，開發者本身能夠順利調查問題的成因與影響範圍。

### Logs for LINE Ads API request 

當向 LINE Ads API 發送請求時，我們建議將下列資訊保存為日誌：

- API 請求的時間
- 請求方法（request method）
- API 端點（endpoint）
- LINE Platform 在回應中回傳的狀態碼（status code）

更具體地說，請使用下列格式將其保存於日誌檔案中。

| API 請求的時間 | 請求方法 | API 端點 | 狀態碼 |
| --- | --- | --- | --- |
| Mon, 05 Jul 2022 08:14:35 GMT | GET | `https://ads.line.me/api/v3/codes/ssps` | 200 |
