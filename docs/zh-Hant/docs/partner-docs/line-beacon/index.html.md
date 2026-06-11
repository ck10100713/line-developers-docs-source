# LINE Beacon

<!-- note start -->

**使用選用功能需提出申請**

本文件中的功能僅供已提交所需申請的企業用戶使用。若要為您公司的 LINE 官方帳號（LINE Official Account）使用此服務，請聯絡您的業務代表或[我們的業務合作夥伴](https://www.lycbiz.com/jp/partner/sales/)。

<!-- note end -->

## About user settings 

使用者必須符合下列條件才能接收 LINE Beacon：

- 您用於 LINE 的作業系統（OS）版本必須符合需求。
- 智慧型手機的藍牙（Bluetooth）設定為開啟。
- 您已在 LINE 上同意使用 LINE Beacon。（「設定」>**隱私設定**>**提供使用資料**>**LINE Beacon**）

如需更多資訊（包含 OS 版本需求），請參閱說明中心的[使用 LINE Beacon](https://help.line.me/line/?contentId=50001493)。

## About LINE Beacon reception conditions 

LINE Beacon 的接收條件會因 OS 類型與 LINE 應用程式的執行狀態而有所不同。

以下是接收條件中所使用的「前景（foreground）」與「背景（background）」的意義：

| 詞彙       | 說明                    |
| ---------- | ------------------------------ |
| 前景（Foreground） | LINE 正在執行且使用中     |
| 背景（Background） | LINE 正在執行但未使用 |

<!-- note start -->

**LINE 未執行時的行為**

LINE 未執行時的行為為未定義。它不包含在「背景」之內。

<!-- note end -->

### LINE Beacon reception conditions (iOS) 

iOS 上各 LINE 應用程式執行狀態的接收條件如下：

| LINE 應用程式執行狀態 | 接收條件 |
| --- | --- |
| 前景 | [使用者設定](https://developers.line.biz/en/docs/partner-docs/line-beacon/#about-user-settings-for-line-beacon)符合條件 |
| 背景 | 必須符合以下所有條件：<ul><li>[使用者設定](https://developers.line.biz/en/docs/partner-docs/line-beacon/#about-user-settings-for-line-beacon)符合條件</li><li>**定位服務**（\*1）為開啟</li><li>LINE 應用程式的**允許存取位置**（\*2）設定為「永遠」</li><li>LINE 應用程式的**精確位置**（\*2\*3）為開啟</li></ul> |

\*1 **設定**>**隱私權與安全性**>**定位服務**\
\*2 **設定**>**LINE**>**位置**\
\*3 僅在**允許存取位置**為開啟時顯示

### LINE Beacon reception conditions (Android) 

Android 上各 LINE 應用程式執行狀態的接收條件如下：

| LINE 應用程式執行狀態 | 接收條件 |
| --- | --- |
| 前景 | 必須符合以下所有條件：<ul><li>[使用者設定](https://developers.line.biz/en/docs/partner-docs/line-beacon/#about-user-settings-for-line-beacon)符合條件</li><li>**使用位置**（\*1）為開啟</li><li>LINE 應用程式的**位置權限**（\*2）設定為「僅在使用應用程式時允許」</li><li>LINE 應用程式的**使用精確位置**（\*2）為開啟</li><li>LINE 應用程式的**鄰近裝置權限**（\*3）設定為「允許」</li></ul> |
| 背景 | Android 不支援背景接收。 |

\*1 **設定**>**位置**>**使用位置**\
\*2 **設定**>**應用程式**>**LINE**>**權限**>**位置**\
\*3 **設定**>**應用程式**>**LINE**

### Beacon banner display conditions 

<!-- note start -->

**注意**

這些條件同樣適用於測試帳號。

<!-- note end -->

#### If your LINE Official Account is searchable 

| LINE 官方帳號<br>與好友關係 | 同意 LINE Beacon<br>使用條款 | Beacon 橫幅顯示 |
| --- | --- | --- |
| 已加入好友 | 已同意 | 隱藏 |
| 已加入好友 | 未同意 | 隱藏 |
| 未加入好友 | 已同意 | 顯示 |
| 未加入好友 | 未同意 | 隱藏 |

#### If your LINE Official Account isn't searchable 

無論您是否為該 LINE 官方帳號的好友，或是否同意 LINE Beacon 使用條款，Beacon 橫幅都不會顯示。
