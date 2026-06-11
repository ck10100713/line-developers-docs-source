# 透過電子郵件或通知中心接收通知（Receive notifications via email or the notification center）

在 [LINE Developers Console](https://developers.line.biz/console/) 的通知中心，您可以即時接收各種更新訊息。本頁說明您可以接收的通知類型，以及如何設定接收通知的相關選項。

## Types of notifications that can be received 

您可以接收以下類型的通知：

| 通知類型 | 概要 |
| --- | --- |
| [Important announcements](https://developers.line.biz/en/docs/line-developers-console/notification/#notification-important-announcements) | 關於 LINE Platform 的重要公告 |
| [Activity](https://developers.line.biz/en/docs/line-developers-console/notification/#notification-activity) | 您在 LINE Developers Console 上的活動 |
| [News](https://developers.line.biz/en/docs/line-developers-console/notification/#notification-news) | 來自 LINE Developers 網站的公告 |
| [Channel activity](https://developers.line.biz/en/docs/line-developers-console/notification/#notification-channel-activity) | 與您具有管理員角色的頻道（channel）相關的活動 |
| [Provider activity](https://developers.line.biz/en/docs/line-developers-console/notification/#notification-provider-activity) | 與您具有管理員角色的服務提供者（provider）相關的活動 |

### Important announcements 

通知您關於 LINE Platform 的重要公告。

範例：[Notice Concerning Use of Information in Connection with Group Restructuring (share target picker)](https://developers.line.biz/en/news/2023/09/21/notice-concerning-use-of-information-for-liff/)

### Activity 

通知您在 LINE Developers Console 上的活動。系統會通知以下活動。

| 操作類型 | 活動詳情 |
| --- | --- |
| 與服務提供者（provider）相關的操作 | <ul><li>建立服務提供者</li><li>刪除服務提供者</li><li>寄送邀請加入服務提供者的邀請電子郵件</li><li>將服務提供者角色授予您的開發者帳號</li></ul> |
| 與頻道（channel）相關的操作 | <ul><li>建立頻道</li><li>刪除頻道</li><li>寄送邀請加入頻道的邀請電子郵件</li><li>將頻道角色授予您的開發者帳號</li></ul> |

### News 

通知您來自 LINE Developers 網站的公告。當 [news](https://developers.line.biz/en/news/) 發布時，系統會通知該則消息的標題。

### Channel activity 

通知您與具有管理員角色的頻道相關的活動。系統會通知以下活動。

| 頻道類型 | 活動詳情 |
| --- | --- |
| 一般頻道 | <ul><li>刪除頻道</li><li>新增成員至頻道</li></ul> |
| LINE MINI App 頻道 | <ul><li>依審查結果更新頻道狀態</li><li>啟用 LINE MINI App 的搜尋功能</li><li>自動刪除附加於頻道的審查檔案（審查完成時，或上傳後超過 30 天仍未提出審查申請時）</li></ul> |

### Provider activity 

通知您與具有管理員角色的服務提供者相關的活動。系統會通知以下活動。

- 刪除服務提供者
- 新增成員至服務提供者

## Configure notification types and reception methods 

您可以設定通知的類型與接收方式。前往 LINE Developers Console 中的個人檔案，在 **Settings** 區段中，將通知選項旁的滑桿切換為開啟（右側）或關閉（左側），以啟用或停用該設定。請注意，**Important announcements**（重要公告）無法關閉。

![Settings section of the profile of the LINE Developers console](https://developers.line.biz/media/line-developers-console/console-notification-center-settings-en.png)

<!-- note start -->

**通知電子郵件**

您在 LINE Developers Console 個人檔案中註冊的電子郵件地址，必須經過驗證才能接收電子郵件通知。如果您個人檔案中的電子郵件地址標示為 **Your email is not yet verified**（您的電子郵件尚未驗證），請點選 **Get Verification Link**（取得驗證連結）以驗證您的電子郵件地址。

您只會收到您已啟用的通知設定所對應的電子郵件通知。

<!-- note end -->

## Check notifications 

若要顯示通知中心，請點選 LINE Developers Console 右上角的鈴鐺圖示。如果有未讀的通知，圖示旁會出現一個綠色圓點。

![Notification center icon of the LINE Developers Console](https://developers.line.biz/media/news/console-notification-center-icon.png)

點選此圖示後，您將看到通知中心。在這裡，您可以查看最近的更新與活動。

![The dropdown menu of the notification center of the LINE Developers Console](https://developers.line.biz/media/line-developers-console/notification-01-en.png)
