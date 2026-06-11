# Common Profile Quick-fill 設計規範

<!-- tip start -->

**僅在已驗證的 MINI App 中可用**

若要使用 Common Profile Quick-fill，您的 LINE MINI App 必須通過驗證，且您必須申請使用 Quick-fill。詳情請參閱[使用 Quick-fill 的步驟](https://developers.line.biz/en/docs/line-mini-app/quick-fill/overview/#process)。

<!-- tip end -->

## User experience with Quick-fill 

在 LINE MINI App Quick-fill 中，當終端使用者點選 [Auto-fill 按鈕](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#what-is-auto-fill-button)時，會出現一個用來確認使用者個人資料的對話框（modal）。在顯示的對話框中確認個人資料後，使用者即可點選 **Auto-fill**，個人資料便會自動填入。

您可以呼叫 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 方法來顯示此對話框。因此，貴公司無需自行開發此對話框。

顯示對話框的時機可依照 LINE MINI App 的設定自由設置，但以下為建議與禁止的模式。

- [建議的畫面轉換](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#recommended-screen-transition)
- [禁止的畫面轉換](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#prohibited-screen-transition)

### Recommended screen transitions 

在將 Quick-fill 整合至您的 LINE MINI App 時，我們建議採用以下畫面轉換：

- [移動至會員註冊畫面後立即顯示對話框](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#show-modal-immediately-after-transition)
- [當使用者選擇輸入表單時顯示對話框](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#show-modal-when-selecting-input-form)
- [當使用者點選 Auto-fill 按鈕後顯示對話框](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#show-modal-when-tapping-auto-fill-button)
- [當使用者在頻道同意畫面上同意後，於目的地畫面顯示對話框](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#show-modal-after-consent-screen)

#### Display a modal immediately after moving to the member registration screen 

當使用者移動至註冊畫面時，立即呼叫 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 方法以顯示對話框。在這種情況下，請在會員註冊畫面上放置一個 Auto-fill 按鈕，讓使用者即使關閉了對話框一次，也能再次顯示對話框。

![](https://developers.line.biz/media/line-mini-app/quick-fill/recommended-screen-transition-02.png)

#### Display a modal when the user selects an input form 

當使用者在註冊畫面上選擇輸入表單時，呼叫 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 方法以顯示對話框。

![](https://developers.line.biz/media/line-mini-app/quick-fill/recommended-screen-transition-04.png)

#### Display a modal after the user taps the Auto-fill button 

當使用者在會員註冊畫面上點選 Auto-fill 按鈕時，呼叫 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 方法以顯示對話框。

![](https://developers.line.biz/media/line-mini-app/quick-fill/recommended-screen-transition-01.png)

#### Display a modal at the destination after the user agrees on the channel consent screen 

當使用者在 LINE MINI App 的[頻道同意畫面（channel consent screen）](https://developers.line.biz/en/docs/line-mini-app/develop/configure-console/#consent-screen-settings)上點選 **Allow** 時，將使用者直接轉換至註冊畫面。轉換至註冊畫面後，立即呼叫 [`liff.$commonProfile.get()`](https://developers.line.biz/en/reference/line-mini-app/#get-common-profile) 方法以顯示對話框。在這種情況下，請在會員註冊畫面上放置一個 Auto-fill 按鈕，讓使用者即使關閉了對話框一次，也能再次顯示對話框。

![](https://developers.line.biz/media/line-mini-app/quick-fill/recommended-screen-transition-03.png)

### Prohibited screen transitions 

在將 Quick-fill 整合至 LINE MINI App 時，我們禁止以下類型的畫面轉換。若我們發現有應用程式執行了禁止的畫面轉換，我們可能會根據您申請使用 Quick-fill 時所同意的使用條款，撤銷（revoke）Quick-fill 權限。

- [在沒有可自動填入表單的畫面上顯示對話框](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#show-modal-on-non-auto-fill-form)
- [取得表單中不存在的項目](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#get-non-existent-item)
- [未自動填入表單即移動至確認畫面](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#skip-input-form)

#### Display a modal on a screen that doesn't have a form to automatically fill in 

禁止在沒有可自動填入欄位之表單的畫面上顯示對話框。

![](https://developers.line.biz/media/line-mini-app/quick-fill/prohibited-screen-transition-01.png)

#### Getting items that don't exist in the form 

禁止取得表單中不存在的項目。例如，即使註冊表單上沒有讀音（phonetic）欄位，您也不得取得讀音資訊。

![](https://developers.line.biz/media/line-mini-app/quick-fill/prohibited-screen-transition-02.png)

#### Move to the confirmation screen without auto-filling the form 

禁止在使用者於對話框中點選 **Auto-fill** 按鈕後，未自動填入表單即立即移動至下一個畫面。例如，您不得未自動填入表單就移動至註冊確認畫面，也不得未顯示已取得的個人資料資訊即進行註冊並移動至註冊完成畫面。

![](https://developers.line.biz/media/line-mini-app/quick-fill/prohibited-screen-transition-03.png)

## Auto-fill button guidelines 

在將 Quick-fill 整合至您的 LINE MINI App 時，您必須遵守以下項目。

### What is the Auto-fill button 

共有 4 種類型、總計 13 種不同的 Auto-fill 按鈕。請依照您的 LINE MINI App 使用您想要的按鈕。您可以在 [Auto-fill 按鈕的類型](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#auto-fill-button)中查看按鈕清單。

![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-01.png)

### Example of using the Auto-fill button 

請直接使用按鈕，不要修改或編輯，也不要添加動畫或特效（縮放、旋轉、裝飾等）。有關禁止項目的更多資訊，請參閱 [Auto-fill 按鈕的禁止項目](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#auto-fill-button-prohibition)。

![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-02.png)

### Location of the Auto-fill button 

為提升使用者的可見性，請將 Auto-fill 按鈕對齊表單輸入欄位的左側或中央。

#### Example of left alignment 

![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-03.png)

#### Example of center alignment 

![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-04.png)

#### Notes on placement 

請將 Auto-fill 按鈕放置在適當的位置，讓使用者在點選按鈕後能看到將被填入的表單。

![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-05.png)

#### Leave a clear space around the button 

為確保按鈕的可見性與獨立性，請在按鈕的上、下、左、右各留出 10px 的邊距。

![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-06.png)

### Prohibited items for the Auto-fill button 

以下針對 Auto-fill 按鈕的操作為禁止項目。

| ❌ 放大與縮小 | ❌ 變形（傾斜、旋轉、斜體、標準化） |
| --- | --- |
| ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-07.png) | ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-08.png) |

| ❌ 裝飾（陰影、邊框、3D 顯示） | ❌ 將元素重疊顯示 |
| --- | --- |
| ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-09.png) | ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-guideline-10.png) |

以下類型的 Auto-fill 按鈕顯示與使用方式同樣為禁止項目。

| ❌ 使用您自訂的按鈕 | ❌ 在 Auto-fill 按鈕下方添加文字 |
| --- | --- |
| ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-prohibition-01.png) | ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-prohibition-02.png) |

| ❌ 放大與縮小 Auto-fill 按鈕 | ❌ 隱藏 Auto-fill 按鈕 |
| --- | --- |
| ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-prohibition-03.png) | ![](https://developers.line.biz/media/line-mini-app/quick-fill/auto-fill-button-prohibition-04.png) |

## Types of Auto-fill buttons 

共有 4 種類型、總計 13 種不同的 Auto-fill 按鈕。請依照您的 LINE MINI App 使用您想要的按鈕。

- [Type A](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#type-a)
- [Type B](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#type-b)
- [Type C](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#type-c)
- [Type D](https://developers.line.biz/en/docs/line-mini-app/quick-fill/design-regulations/#type-d)

<!-- tip start -->

**以指定的尺寸顯示 Auto-fill 按鈕**

請以每種類型所指定的尺寸顯示 Auto-fill 按鈕。Auto-fill 按鈕圖片為指定尺寸的兩倍。因此，請注意不要以圖片的原始尺寸顯示。

<!-- tip end -->

<!-- note start -->

**透過指定 URL 來使用 Auto-fill 按鈕的圖片**

自動輸入按鈕的圖片可能會在不另行通知的情況下變更。請務必直接使用本頁所指定的 URL，而不要下載圖片後再使用。此外，我們可能會在事先通知後刪除特定圖片或變更 URL。感謝您的理解。

<!-- note end -->

### Type A 

在 Type A 中，1 號為基本形狀。2 號至 4 號為顏色變化版本。尺寸為寬 264px、高 73px。ALT 屬性請指定 `ユーザー情報を自動入力。LINEやYahoo! JAPANに登録した情報を利用できます`。

|  | 自動輸入按鈕 | URL |
| --- | --- | --- |
| 1 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_black.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_black.png` |
| 2 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_white.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_white.png` |
| 3 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_gray.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_gray.png` |
| 4 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_blue.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_AC_blue.png` |

### Type B 

在 Type B 中，1 號為基本形狀。2 號至 4 號為顏色變化版本。尺寸為寬 264px、高 73px。ALT 屬性請指定 `ユーザー情報を自動入力。LINEやYahoo! JAPANに登録した情報を利用できます`。

|  | 自動輸入按鈕 | URL |
| --- | --- | --- |
| 1 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_black.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_black.png` |
| 2 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_white.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_white.png` |
| 3 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_gray.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_gray.png` |
| 4 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_blue.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_simple_blue.png` |

### Type C 

Type C 僅提供基本形狀。尺寸為寬 264px、高 73px。ALT 屬性請指定 `ユーザー情報を自動入力。LINEやYahoo! JAPANに登録した情報を利用できます`。

|  | 自動輸入按鈕 | URL |
| --- | --- | --- |
| 1 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_LY_white.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_LY_white.png` |

### Type D 

在 Type D 中，1 號為基本形狀。2 號至 4 號為顏色變化版本。尺寸為寬 288px、高 66px。ALT 屬性請指定 `LINEで自動入力しますか？氏名、電話番号、メールアドレス、住所など。自動入力`。

|  | 自動輸入按鈕 | URL |
| --- | --- | --- |
| 1 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_white.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_white.png` |
| 2 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_black.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_black.png` |
| 3 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_gray.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_gray.png` |
| 4 | ![](https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_blue.png) | `https://account-center-fe.line-scdn.net/images/quick_fill_button_LINE_blue.png` |
