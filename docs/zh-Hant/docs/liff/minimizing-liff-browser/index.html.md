# 最小化 LIFF browser（Minimizing LIFF browser）

本頁說明 LIFF browser 最小化功能。

<!-- table of contents -->

## What is LIFF browser minimization 

[LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 最小化是一項功能，可讓你暫停瀏覽 LIFF browser，以執行其他操作。

當使用者在聊天室中瀏覽 LIFF browser 時，可能會想執行其他操作，例如傳送訊息到聊天室。在這種情況下，最小化 LIFF browser 即可暫停瀏覽 LIFF browser，讓使用者執行該操作。執行操作後，使用者可以將 LIFF browser 最大化，以恢復瀏覽 LIFF browser。

LIFF browser 最小化時會以圖示顯示。

![LIFF browser minimization](https://developers.line.biz/media/liff/minimizing-liff-app/liff-minimize-en.png)

<!-- tip start -->

**最小化 LINE 的應用程式內瀏覽器**

與 LIFF browser 一樣，[LINE 的應用程式內瀏覽器（LINE's in-app browser）](https://developers.line.biz/en/glossary/#line-iab)同樣支援最小化。詳情請參閱 LINE 使用者指南中的 [Minimizing the browsing web page](https://guide.line.me/ja/chats-calls-notifications/chats/minimizebrowser.html)（僅提供日文版）。

<!-- tip end -->

## Conditions of use for LIFF browser minimization 

要最小化 LIFF browser，必須符合下列條件：

- LINE for iOS 版本 12.18.0 以上，或 LINE for Android 版本 15.0.0 以上
- 使用者裝置已開啟 **設定** > **應用程式** > **LINE** > **在其他應用程式上層顯示**（僅 LINE for Android 需要）
- 你的 LIFF app 的[螢幕大小（screen size）](https://developers.line.biz/en/docs/liff/overview/#screen-size)指定為 `Full`
- 你的 LIFF app 的 [`chat_message.write` scope](https://developers.line.biz/en/docs/liff/registering-liff-apps/#registering-liff-app) 為關閉狀態
- LIFF browser 未與其他互動視窗（modal）重疊

<!-- note start -->

**LIFF-to-LIFF 轉換後的 LIFF app 必須符合使用條件**

要在 [LIFF-to-LIFF 轉換](https://developers.line.biz/en/docs/liff/opening-liff-app/#move-liff-to-liff)後最小化 LIFF browser，轉換後的 LIFF app 必須符合使用條件。

例如，如同 LIFF 文件中[依 LIFF app 螢幕大小而異的行為（Behavior based on screen size of the LIFF app）](https://developers.line.biz/en/docs/liff/opening-liff-app/#behavior-by-screen-size)所述，無論指定的螢幕大小為何，轉換後的 LIFF app 都會以 `Full` 顯示。然而，若轉換後的 LIFF app 螢幕大小指定為 `Tall` 或 `Compact`，則轉換後的 LIFF app 將不符合 LIFF browser 最小化的使用條件。

<!-- note end -->

LIFF browser 最小化功能將會在 LINE for iPadOS 上推出，但日期尚未確定。

## Minimizing a LIFF browser 

最小化 LIFF browser 有三種方式：

- [從動作按鈕點選選項](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/#tap-action-button-option)
- [點選應用程式內提示](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/#tap-in-app-alert)
- [滑動 LIFF browser](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/#swipe-liff-browser)

### Tapping an option from the action button 

從[動作按鈕（action button）](https://developers.line.biz/en/docs/liff/overview/#action-button)開啟下拉式選單後，點選 **最小化瀏覽器（Minimize browser）** 選項。

![](https://developers.line.biz/media/liff/minimizing-liff-app/tap-action-button-en.png)

### Tapping an in-app alert 

點選應用程式內提示。

![LIFF browser minimization (tapping an in-app alert)](https://developers.line.biz/media/liff/minimizing-liff-app/tap-in-app-alert.png)

### Swiping a LIFF browser 

向下滑動 LIFF browser。

![LIFF browser minimization (swiping a LIFF browser)](https://developers.line.biz/media/liff/minimizing-liff-app/swipe-liff-browser-en.png)

### Tapping the option from the action button (LINE version earlier than 26.7.0) 

從[動作按鈕（action button）](https://developers.line.biz/en/docs/liff/overview/#action-button)開啟[多分頁檢視（multi-tab view）](https://developers.line.biz/en/docs/liff/overview/#multi-tab-view)後，點選 **最小化瀏覽器（Minimize browser）** 選項。

![LIFF browser minimization (tapping the action button option)](https://developers.line.biz/media/liff/minimizing-liff-app/tap-action-button-option-en.png)

## Maximizing a LIFF browser 

要最大化 LIFF browser，請點選已最小化的 LIFF browser。

![LIFF browser maximization](https://developers.line.biz/media/liff/minimizing-liff-app/maximize-liff-browser-en.png)

## Moving a minimized LIFF browser 

要移動已最小化的 LIFF browser，請拖曳該 LIFF browser。

![Moving a minimized LIFF browser](https://developers.line.biz/media/liff/minimizing-liff-app/move-minimized-liff-browser-en.png)

## Closing a minimized LIFF browser (LINE version earlier than 15.20.0) 

在 15.20.0 以前的 LINE 版本中，有兩種方式可以關閉已最小化的 LIFF browser：

- [將 LIFF browser 滑出螢幕（僅 LINE for iOS 可用）](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/#close-minimized-liff-browser-1)
- [將已最小化的 LIFF browser 拖曳至關閉圖示](https://developers.line.biz/en/docs/liff/minimizing-liff-browser/#close-minimized-liff-browser-2)

### Swiping a LIFF browser off the screen (only available in LINE for iOS) 

將已最小化的 LIFF browser 滑出螢幕。

![Closing a minimized LIFF browser](https://developers.line.biz/media/liff/minimizing-liff-app/close-minimized-liff-browser-en.png)

### Drag a minimized LIFF browser to the close icon 

拖曳已最小化的 LIFF browser 時，螢幕底部會顯示關閉圖示。將已最小化的 LIFF browser 拖曳至關閉圖示後放開手指。

![Closing a minimized LIFF browser](https://developers.line.biz/media/liff/minimizing-liff-app/close-minimized-liff-browser-ios-12-12-0-or-later-en.png)

## Closing a minimized LIFF browser (LINE version 15.20.0 or later) 

在 15.20.0 以上的 LINE 版本中，你可以點選已最小化的 LIFF browser 右上角顯示的關閉按鈕，來關閉該 LIFF browser。

![Close minimized liff browser](https://developers.line.biz/media/liff/minimizing-liff-app/close-minimized-liff-browser-line-15-20-0-or-later-en.png)

## Priority of LIFF browser icon display 

LIFF browser 最小化時會以圖示顯示。LIFF browser 圖示顯示的優先順序如下：

1. 頻道圖示（Channel icon）：LINE Login 頻道的頻道圖示
1. Favicon：LIFF app 的 favicon
1. 通用圖示（Common icon）：連結圖示
