# 建立永久連結（Creating permanent links）

使用者除了可以使用 LIFF URL 之外，也可以使用永久連結（permanent link）來存取 LINE MINI App。不過，若是為了分享 LINE MINI App 頁面，應該使用永久連結，而非 LIFF URL。

當你從[標題列](https://developers.line.biz/en/docs/line-mini-app/discover/ui-components/#header)中顯示的動作按鈕分享 LINE MINI App 頁面時，LINE app 會自動產生該頁面的永久連結。

至於其他所有情況，你需要依照以下公式自行建立永久連結。

`LIFF URL + (LINE MINI App URL - Endpoint URL) = Permanent Link`

範例：

| 項目 | 設定 |
| --- | --- |
| LIFF URL\* | `https://miniapp.line.me/123456-abcedfg` |
| LINE MINI App 頁面的 URL | `https://example.com/shop?search=shoes#item10` |
| Endpoint URL\* | `https://example.com` |

\* 你可以在 [LINE Developers Console](https://developers.line.biz/console/) 的 **Web app settings** 分頁中找到。

在這個情況下，對應到該 LINE MINI App 頁面 URL 的永久連結如下：

```
https://miniapp.line.me/123456-abcedfg/shop?search=shoes#item10
```

<!-- tip start -->

**Tip**

你可以在 LINE MINI App 頁面的 URL 中使用指向頁面的原始路徑（raw path）、查詢參數（query parameters）以及雜湊片段（hash fragments）。

<!-- tip end -->

<!-- note start -->

**LINE MINI App 的 LIFF URL 已變更**

自 [2023 年 12 月 13 日](https://developers.line.biz/en/news/2023/12/13/change-of-liff-url-for-line-mini-app/)起，LINE MINI App 的 LIFF URL 已變更為 `https://miniapp.line.me/{liffId}`。

如果使用者存取既有的 `https://liff.line.me/{liffId}`，LINE MINI App 同樣會開啟。因此，你可以繼續使用你已經發行的 QR code。

<!-- note end -->

## Differences in domain names depending on the LINE app version 

當你從標題列中顯示的[動作按鈕](https://developers.line.biz/en/docs/line-mini-app/discover/builtin-features/#action-button)分享 LINE MINI App 頁面時，所產生的永久連結的網域名稱會依 LINE app 的版本而有所不同。

| LINE app 版本   | 產生的 URL 範例          |
| ------------------ | ---------------------------------- |
| 13.20 或更新版本     | `https://miniapp.line.me/{liffId}` |
| 早於 13.20 | `https://liff.line.me/{liffId}`    |

## If the user doesn't have LINE installed 

當已安裝 LINE 的使用者點擊永久連結時，LINE 會將使用者帶往該連結所指向的確切頁面。如果使用者未安裝 LINE，則會開啟網頁瀏覽器，並引導使用者在 LINE 中開啟該 LINE MINI App。從這個引導畫面中，使用者也可以在網頁瀏覽器中開啟 LIFF endpoint URL 頁面。
