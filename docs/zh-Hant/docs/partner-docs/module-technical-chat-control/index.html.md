# 控制聊天主導權（Chat Control）

<!-- warning start -->

**警告**

目前提供的 module 頻道（channel）在掛載至 LINE 官方帳號（LINE Official Account）時，會自動取得聊天主導權 [(Default Active)](https://developers.line.biz/en/docs/partner-docs/module-technical-chat-control/#default-active)，因此不需要另行控制聊天主導權。

<!-- warning end -->

<!-- note start -->

**使用選用功能需要先完成相關程序**

本文件中所說明的功能，僅開放給已完成指定申請程序的企業客戶使用。如果您想透過 module 發布擴充功能，請聯絡業務代表，或透過 [LINE Marketplace Inquiry](https://line-marketplace.com/jp/inquiry)（僅提供日文）與我們聯絡。

<!-- note end -->

## What is chat control (Chat Control)? 

為了避免多個 module 頻道（channel）同時回覆或處理使用者（end user）的操作，我們為 module 頻道導入了主導權（Chat Control）的概念。

![Chat control](https://developers.line.biz/media/partner-docs/module-technical/chat-control-en.png)

| 主導權（Chat Control） | 說明 |
| --- | --- |
| Active Channel | 擁有主導權（Chat Control）的頻道。預設情況下，Primary CH（與 LINE 官方帳號關聯的標準 Messaging API 頻道）即為「Active Channel」。<br>您可以從此頻道發送回覆訊息（reply message）、推播訊息（push message）等。<br>每個 LINE 官方帳號只能掛載一個「Active Channel」。 |
| Standby Channel | 不具有 Chat Control 的頻道。<br>請避免從此頻道發送訊息。<br>除了 Active Channel 以外的所有頻道皆為「Standby Channel」。 |

<!-- note start -->

**主導權（Chat Control）並非以每個 module 頻道為單位統一設定**

主導權（Chat Control）是以每位使用者、每個聊天室或每個群組為單位進行管理。

<!-- note end -->

<!-- note start -->

**具備「Default Active」功能的 module 頻道**

具備「Default Active」功能的 module 頻道，是指在掛載至 LINE 官方帳號時會自動成為 Active Channel 的 module 頻道。

詳細資訊請參閱 [Default Active](https://developers.line.biz/en/docs/partner-docs/module-technical-chat-control/#default-active)。

<!-- note end -->

## API reference 

- [Acquire Control API](https://developers.line.biz/en/reference/partner-docs/#acquire-control-api)
- [Release Control API](https://developers.line.biz/en/reference/partner-docs/#release-control-api)

## Default active 

在 LINE Marketplace 上提供的 module 頻道皆具備「Default Active」功能。

<!-- note start -->

**此功能為 LINE Marketplace 專屬**

「Default Active」功能僅適用於在 [LINE Marketplace](https://line-marketplace.com/jp/inquiry) 上發布的 module 頻道。

<!-- note end -->

具備「Default Active」功能的 module 頻道，其特性如下。

### Auto active 

一般的 module 頻道在掛載至 LINE 官方帳號時會成為 Standby Channel。在那之後，module 頻道會視需要（由使用者操作等觸發）透過 Acquire Control API 取得主導權（Chat Control），並成為 Active Channel。

而具備「Default Active」功能的 module 頻道，在掛載至 LINE 官方帳號時會自動成為 Active Channel，因此不需要呼叫 Acquire Control API。

### Exclusive control 

每個 LINE 官方帳號只能掛載一個具備「Default Active」功能的 module 頻道。

如果某個 LINE 官方帳號已經掛載了一個具備「Default Active」功能的 module 頻道，您就無法再為該帳號掛載其他具備「Default Active」功能的 module 頻道。

您可以掛載多個不具備「Default Active」功能的 module 頻道，但目前並未提供這類頻道。
