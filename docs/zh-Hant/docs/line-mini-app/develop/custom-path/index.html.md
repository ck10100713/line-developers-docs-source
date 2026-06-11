# 設定 Custom Path

<!-- tip start -->

**此功能僅適用於已驗證的 MINI App**

此功能僅適用於已驗證的 MINI App。

<!-- tip end -->

Custom Path 是設定在已發布頻道（channel）LIFF URL 中的唯一字串。Custom Path 功能讓你能在 LIFF URL 中設定自訂字串，如下所示：

| 含 LIFF ID 的 URL 範例 | 設定 Custom Path 的範例 |
| --- | --- |
| `https://miniapp.line.me/123456-abcdefg` | `https://miniapp.line.me/cony_coffee` |

舉例來說，透過將唯一名稱設定為 Custom Path，使用者就能從 URL 辨識出這是哪個品牌或店家的 LINE MINI App。即使設定了 Custom Path，仍可如同以往透過 LIFF ID 的 URL 進行存取。

## How to apply 

如果你要在 LINE MINI App 中使用 Custom Path 功能，必須提出申請。申請方式會依服務提供的地區而有所不同。

- [如果你的服務地區為日本](https://developers.line.biz/en/docs/line-mini-app/develop/custom-path/#area-is-japan)
- [如果你的服務地區為台灣或泰國](https://developers.line.biz/en/docs/line-mini-app/develop/custom-path/#area-is-taiwan-or-thailand)

### If your service area is Japan 

如果你的服務地區為日本，要使用 Custom Path 功能，請使用下方表單進行申請。一次為多個 LINE MINI App 申請 Custom Path 的方法也可在下方表單中找到（僅提供日文版本）。

[申請表單](https://form-business.yahoo.co.jp/claris/enqueteForm?inquiry_type=lmini-custompath)

我們會以電子郵件通知你申請的確認結果與審查結果。從申請到 Custom Path 的 URL 可供使用，大約需要 1 到 2 週的時間。

### If your service area is Taiwan or Thailand 

如果你在台灣或泰國提供服務，並希望使用 Custom Path 功能，請聯絡你的業務代表。

## Notes on applying for Custom Path 

即使設定了 Custom Path，已設定 Custom Path 的 LIFF URL 也不會顯示在 [LINE Developers Console](https://developers.line.biz/console/) 上。

你可以在 LINE MINI App 通過審查之前就申請 Custom Path。不過，Custom Path 只會在 LINE MINI App 通過審查後才會被設定。

原則上，Custom Path 一旦設定後便無法變更。

### String that can be used as a Custom Path 

申請 Custom Path 時輸入的字串適用以下限制。填寫字串時請將這些限制納入考量。

- 必須至少 4 個字元，最多 29 個字元。
- 僅允許半形英數字（`a-z`、`0-9`）與底線（`_`）。
- 底線（`_`）不能作為最後一個字元使用。
- 不能只包含數字字元。
- 不允許使用空格。
- 須包含可辨識品牌或服務的專有名詞。
- 不能使用與 LY Corporation 所提供服務相同的字串。
- 不能使用已被使用的字串，包括他人正在使用的字串。
- 我們認定為不適當的字串可能無法使用。
