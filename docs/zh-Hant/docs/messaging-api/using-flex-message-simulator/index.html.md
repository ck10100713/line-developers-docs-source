# 教學 - 使用 Flex Message Simulator 製作電子名片（Tutorial - Create a digital business card with Flex Message Simulator）

Flex Message 是一種能根據 [CSS Flexible Box（CSS Flexbox）](https://www.w3.org/TR/css-flexbox-1/) 自由自訂的訊息。你可以依需求調整訊息的尺寸、將文字、圖片與圖示配置在特定位置，並加入可互動的按鈕。

在本教學中，你將學會如何使用 [Flex Message Simulator](https://developers.line.biz/flex-simulator/) 製作電子名片。Flex Message Simulator 是一項工具，可協助你**不需撰寫程式碼**就能發想、設計並製作 Flex Message 原型。如果你是第一次接觸 Flex Message，請先參閱 [Sending Flex Messages](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)。

## Goal 

本教學的成果是一張如下所示的電子名片。你可以從這個[下載連結](https://developers.line.biz/media/code-samples/flex-message-simulator-example.json)看到以 JSON 定義的成果。但我們建議你實際走過這份教學，熟悉 Flex Message Simulator。我們保證這項工具會非常方便地應付數不盡的 Flex Message 使用情境。

![Final Output](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-final-output.png)

## Before you start 

為了順利進行本教學，我們建議你在開始前先閱讀 [Messaging API overview](https://developers.line.biz/en/docs/messaging-api/overview/) 與 [Send Flex Messages](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)。此外，如果你是第一次使用這個模擬器，請繼續閱讀本節以了解 Flex Message Simulator。如果你已經熟悉這個模擬器，可以[直接從教學開始](https://developers.line.biz/en/docs/messaging-api/using-flex-message-simulator/#select-flex-message)。

### Learn about Flex Message Simulator 

Flex Message Simulator 是一項可用來編寫與預覽 Flex Message 的工具。你不需要建置開發環境或撰寫程式碼，就能編寫 Flex Message 並傳送 Flex Message 進行預覽。

首先，開啟 [Flex Message Simulator](https://developers.line.biz/flex-simulator/)。如果你尚未登入 [LINE Developers Console](https://developers.line.biz/console/)，系統會提示你登入。如果你有 LINE Developers 帳號，請使用你的帳號登入。如果沒有，請點選 **Create an account** 建立一個。

Flex Message Simulator 的 UI 有三個區域：

- **Preview area**（預覽區）：顯示以 tree view 區與 property 區所指定的資料產生的 Flex Message。
- **Tree view area**（樹狀檢視區）：顯示並讓你編輯 Flex Message 的資料結構。
- **Property area**（屬性區）：讓你設定在 tree view 區中所選項目的屬性。模擬器會使用此處輸入的資料來產生 Flex Message。

![Flex Message Areas](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-areas.png)

如果你將滑鼠移到 tree view 區的某個項目上，預覽區中對應的區域就會被高亮顯示。你可以從影片中看到實際操作。

<video width="883" height="381" controls>
  <source src="https://vos.line-scdn.net/line-developers/docs/media/video/flex-message-simulator.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

#### You can use Flex Message layout presets 

Flex Message Simulator 提供預先定義好的 Flex Message 版面配置。

要使用預先定義的版面配置，請點選模擬器頂端的 **Showcase**。做出選擇後，點選 **Create**。

<!-- note start -->

**關於版面配置**

在本教學中，我們不使用預先定義的版面配置。我們將從零開始製作一則 Flex Message。

<!-- note end -->

![Flex Message Simulator Showcase](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/showcase.png)

#### You can copy the Flex Message in JSON 

要複製以 JSON 產生的 Flex Message，請點選 **</>View as JSON**，然後點選 **Copy** 按鈕。

![View as JSON](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/view-as-json.png)

## Tutorial shortcut 

如果你想跳過閱讀說明、直接預覽成果，請[下載](https://developers.line.biz/media/code-samples/flex-message-simulator-example.json) JSON 格式的 Flex Message 物件。要在 Flex Message Simulator 中預覽成果：

1. 點選 **</>View as JSON**。會顯示一個含有 JSON 資料的對話框。
1. 移除對話框中的內容。
1. 將下載的 JSON 檔案內容複製貼上到對話框中。
1. 點選 **Apply** 以儲存變更。預覽區會顯示我們貼上的 Flex Message。

![Preview Flex Message created from sample JSON data](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-confirm-example-code-output.png)

## 1. Select container type 

既然我們已經認識了 Flex Message Simulator，接下來就開始製作電子名片。製作名片只需要一個 bubble，因此我們會將 Flex Message 容器設定為 [bubble 類型](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#bubble)。

要建立 bubble 容器，請點選 **New** 並從下拉式選單中選擇 **bubble**。

![Select Bubble Type Container](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/select-bubble-type.png)

<!-- tip start -->

**提示**

當你從下拉式選單選擇 **bubble** 時，預覽區底部會跳出一則「OK」訊息。這表示你的更新已成功反映在預覽區。

![Select Message Type](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/type.png)

<!-- tip end -->

關於容器類型的更多資訊，請參閱 [container](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#container)。

## 2. Add a header 

在我們建立的容器中，讓我們加入一個 header 來顯示公司名稱。header 是一種 [block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)，hero、body 與 footer 也都是。header 主要用來顯示訊息主旨或內容標題。

![Block style example](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/elements.png)

1. 要加入 header，請在 tree view 區選擇 **header** 節點。點選頂端的 **+**，再點選 **box**。
1. 設定 header 的背景顏色。在 property 區，於 **backgroundColor** 欄位設定十六進位色碼，本教學使用 `#00B900`，然後按下 Enter 鍵。現在 header 在視覺上就能與 body block 區分開來。

   <!-- tip start -->

   **按下 Enter 鍵以套用你的輸入**

   每當你在 property 區新增或選擇一個屬性時，請按下 Enter 鍵，將你的輸入套用到預覽區。接著你就能在預覽區看到結果。從本教學接下來的部分起，為了不讓你感到繁瑣，我們將省略這項說明。

   <!-- tip end -->

   ![Set Header Background Color](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/set-header-color.png)

1. 在 header 中加入文字：
   1. 從 tree view 中，點選 **header** 下的 **box [vertical]** 節點。

      <!-- tip}

      Vertical box 是 Flex Message 的 box 類型之一，它決定 box 的子元件如何在 box 內排列。更多資訊請參閱 [Box component orientation](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-component-orientation)。

      ::

   1. 在 tree view 中點選 **+**，然後從下拉式選單選擇 **text**。一個 **text** 節點會建立在 **box [vertical]** 節點之下。
   1. 從 tree view 點選 text 節點。
   1. 在 property 區，將 **text** 欄位中的「hello, world」替換為「Flex Message Corp」。

我們以新的背景顏色讓 header 變得醒目，但 header 文字有點難以閱讀。讓我們以新的顏色與樣式讓文字更突出。在 tree view 中點選 text 節點，將 **color** 屬性設為 `#FFFFFF`，並將 **weight** 設為 `bold`。

現在你應該會看到類似這樣的畫面。我們有了一個醒目的 header，且文字清晰可見。

![Add Header Final Output](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/add-header-final.png)

## 3. Add an image 

讓電子名片在視覺上更豐富的方法之一，就是加入一張圖片。使用 Flex Message Simulator 來加入或設計圖片再簡單不過了。要加入圖片，我們會使用 [hero block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)，它主要用來顯示圖片類型的內容。

1. 在 tree view 中，點選 **hero** 節點。
2. 點選 **+**，然後從下拉式清單選擇 **image**。預覽中會顯示一張預設圖片。
3. 要更換圖片，請從 tree view 點選 **image** 節點。在 property 區，將 **url** 屬性的值更改為你圖片所在的位置。你的圖片必須是直式（portrait mode）。在本教學中，你可以使用[這張圖](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/mary.png) start -->

      **圖片需求**

   你無法將圖片檔案上傳到 Flex Message Simulator。請指定一個已上傳於網路上的圖片 URL。圖片與圖片 URL 必須符合以下條件：
   - 通訊協定：HTTPS（TLS 1.2 或更新版本）
   - 圖片格式：JPEG 或 PNG
   - 最大圖片尺寸：1024 x 1024 px
   - 最大檔案大小：10 MB

   <!-- tip}

      Vertical box 是 Flex Message 的 box 類型之一，它決定 box 的子元件如何在 box 內排列。更多資訊請參閱 [Box component orientation](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#box-component-orientation)。

      ::

   1. 在 tree view 中點選 **+**，然後從下拉式選單選擇 **text**。一個 **text** 節點會建立在 **box [vertical]** 節點之下。
   1. 從 tree view 點選 text 節點。
   1. 在 property 區，將 **text** 欄位中的「hello, world」替換為「Flex Message Corp」。

我們以新的背景顏色讓 header 變得醒目，但 header 文字有點難以閱讀。讓我們以新的顏色與樣式讓文字更突出。在 tree view 中點選 text 節點，將 **color** 屬性設為 `#FFFFFF`，並將 **weight** 設為 `bold`。

現在你應該會看到類似這樣的畫面。我們有了一個醒目的 header，且文字清晰可見。

![Add Header Final Output](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/add-header-final.png)

## 3. Add an image 

讓電子名片在視覺上更豐富的方法之一，就是加入一張圖片。使用 Flex Message Simulator 來加入或設計圖片再簡單不過了。要加入圖片，我們會使用 [hero block](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/#block)，它主要用來顯示圖片類型的內容。

1. 在 tree view 中，點選 **hero** 節點。
2. 點選 **+**，然後從下拉式清單選擇 **image**。預覽中會顯示一張預設圖片。
3. 要更換圖片，請從 tree view 點選 **image** 節點。在 property 區，將 **url** 屬性的值更改為你圖片所在的位置。你的圖片必須是直式（portrait mode）。在本教學中，你可以使用[這張圖](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/mary.png) end -->

   <!-- tip start -->

   **檔案大小建議**

   為了讓訊息能不延遲地顯示，我們建議你將每個圖片檔案的大小控制在 1 MB 以下。

   <!-- tip end -->

圖片已成功更換，但與背景相比，圖片看起來有點小。讓我們把圖片放大。

![Add Image](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/add-image.png)

要更改圖片尺寸，請從 tree view 點選 **image** 節點，並在 **size** 屬性中設定圖片的最大寬度。在本教學中，請點選屬性輸入欄位旁的按鈕，並從下拉式清單選擇 `xl` 關鍵字。你也_可以_改為輸入以像素或 % 為單位的值。更多資訊請參閱 [Image](https://developers.line.biz/en/reference/messaging-api/#f-image) 的「size」屬性規格。

現在你有了一張圖片放大的名片：

![Add Image Final Output](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/add-image-final.png)

## 4. Add a name 

名片上一定要有名字。將名字之類的重要資訊以醒目的樣式呈現會很有幫助。要在圖片下方加入名字：

1. 在 tree view 中，點選 **body** 下的 **box [vertical]** 節點。
1. 點選 **+**，然後從下拉式選單選擇 **text**。一個 text 節點會建立在 box 節點之下。
1. 從 tree view 點選 **text** 節點。
1. 在 property 區，將 **text** 欄位中的「hello, world」替換為一個名字。

就像我們對 [header text](https://developers.line.biz/en/docs/messaging-api/using-flex-message-simulator/#add-header) 所做的那樣，讓我們為名字文字設計樣式。我們想要放大字型大小、將字型加粗，並讓文字置中對齊。

- **Size**：將 **size** 屬性設為 `xl`。（預設大小為「md」。）
- **Bold**：將 **weight** 屬性設為 `bold`。
- **Center align**：將 **align** 屬性設為 `center`。

現在你的名片在圖片下方有了名字：

![Add Name Final Output](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-add-name-final.png)

## 5. Add a job title 

名片上另一項與名字同樣重要的資訊就是你的職稱。讓我們在名字下方加入職稱。

1. 在 tree view 中，點選 **body** 下的 **box [vertical]** 節點。
1. 點選 **+**，然後從下拉式選單選擇 **text**。一個新的 text 節點會被建立。
1. 從 tree view 點選新的 **text** 節點。
1. 在 property 區，將 **text** 欄位中的「hello, world」替換為一個職稱。

由於我們將名字置中對齊，因此也想將職稱置中對齊。在選取 text 節點的狀態下，將 **align** 屬性設為 `center`。

現在你的名片有了職稱：

![Add Job Title Final](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-add-job-title-final.png)

## 6. Add a separator 

稍後我們會加入按鈕讓名片可以互動。在那之前，讓我們先加入一個 [separator](https://developers.line.biz/en/reference/messaging-api/#separator)，以在視覺上將資訊區段與互動區段分隔開來。

1. 在 tree view 中，點選 **body** 下的 **box [vertical]** 節點。
1. 點選 **+**，然後從下拉式選單選擇 **separator**。一個 separator 會建立在職稱的正下方。

![Add Separator](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-add-separator.png)

separator 與職稱之間幾乎沒有間距。讓我們透過為 separator 設定 [margin](https://developers.line.biz/en/reference/messaging-api/#separator) 來在兩者之間留出空間。關於 margin 的更多資訊，請參閱 Messaging API reference 中的 [Separator](https://developers.line.biz/en/reference/messaging-api/#separator)。

1. 在 tree view 中，點選 **separator** 節點。
1. 在 property 區，將 **margin** 屬性設為 `md`。

現在你的名片中有了一個帶有些許間距的 separator：

![Add Separator Final](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-add-separator-final.png)

## 7. Add buttons 

如同步驟 6 所述，我們想加入按鈕讓名片可以互動。我們想在 separator 下方加入兩個按鈕。首先，我們需要一個元件來將這些按鈕分組。

1. 點選 **body** 下的 **box [vertical]**。
1. 點選 **+**，然後從下拉式選單選擇 **box**。一個用來加入按鈕的 box 節點會被建立。

我們希望按鈕在被按下時執行某個動作。按鈕可用的動作類型有 [URI action](https://developers.line.biz/en/reference/messaging-api/#uri-action) 與 [postback action](https://developers.line.biz/en/reference/messaging-api/#postback-action)。在本教學中，我們將加入按鈕來：

1. [跳轉到公司網站](https://developers.line.biz/en/docs/messaging-api/using-flex-message-simulator/#add-action-1)
1. [開啟以 LIFF 製作的註冊表單](https://developers.line.biz/en/docs/messaging-api/using-flex-message-simulator/#add-action-2)

### 7-1. Add a button to jump to the company's website 

要設定一個用來開啟公司網站的按鈕：

1. 在 tree view 中，點選為按鈕建立的 **box [vertical]**。
1. 點選 **+**，然後從下拉式選單選擇 **button**。
1. 點選 **button [action]** 節點。
1. 在 property 區，向下捲動到 **Action** 區段。**type** 屬性預設為 `uri`。由於我們想開啟一個網站 URL，因此維持原值即可。
1. 在 **Action** 區段中，將 **label** 屬性設為「Visit our website」。這會成為按鈕標籤。
1. 要開啟網站，請將 **uri** 屬性設為你想要的 URL。

<!-- note start -->

**對 URI 套用百分比編碼**

請以 UTF-8 編碼，對 `uri` 屬性中的網域名稱、路徑、查詢參數與片段套用[百分比編碼（Percent-encode）](https://en.wikipedia.org/wiki/Percent-encoding)。例如，在以下設定下，最終的 URL 會變成 `https://example.com/path?q=Good%20morning#Good%20afternoon`：

| Scheme | Domain name | Path  | Query parameter | Fragment       |
| ------ | ----------- | ----- | --------------- | -------------- |
| https  | example.com | /path | q=Good morning  | Good afternoon |

<!-- note end -->

現在我們的名片中有了一個用來開啟公司網站的按鈕。

![Add URI Action Button](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-add-uri-button.png)

就像我們對 header 文字、名字與職稱所做的那樣，我們想為按鈕設計樣式。為了讓可點擊的區域更明顯，我們可以為按鈕加上顏色。你可以從三種預設按鈕樣式中選擇要套用的顏色：

- **Primary**：深色按鈕的樣式
- **Secondary**：淺色按鈕的樣式
- **Link**：將按鈕呈現得像 HTML 文字連結

如果你像本教學一樣有多個按鈕垂直堆疊，我們建議你使用 link 樣式。讓我們不為背景上色，而是為按鈕套用 link 樣式：

1. 在 tree view 中，點選 **button** 節點。
1. 在 property 區，將 **style** 屬性設為 `link`。

你的按鈕應該會看起來像這樣：

![Change Button Color](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-change-button-color.png)

### 7-2. Add a button to open a registration form made with LIFF 

讓我們繼續加入其餘的按鈕。對於第二個按鈕，我們想加入一個指向公司註冊表單的 [LINE Front-end Framework（LIFF）](https://developers.line.biz/en/docs/liff/overview/) URL。你可以使用 LIFF 製作註冊表單，之後再以你從表單擷取到的資訊向使用者傳送新訊息。關於 LIFF 的更多資訊，請參閱 [Developing a LIFF App](https://developers.line.biz/en/docs/liff/developing-liff-apps/) 或 [Trying the LIFF starter app](https://developers.line.biz/en/docs/liff/trying-liff-app/)。

要建立第二個按鈕：

1. 在 tree view 中，點選你為第一個按鈕建立的 **box [vertical]** 節點。
1. 點選 **+**，然後從下拉式選單選擇 **button**。一個 button 節點會被建立。
1. 在 property 區：
   - 將 **style** 屬性設為 `link`。
   - 將 **label** 屬性設為「Register with us」。
   - 將 **type** 屬性維持為 `uri`。
   - 將 **uri** 屬性設為一個 LIFF app URL。

現在我們的第二個按鈕設定了 LIFF URL：

![Add LIFF Button](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-add-liff-button.png)

### 7-3. Distribute the buttons 

這些按鈕彼此堆疊得非常緊密。雖然看起來不明顯，但如果你將按鈕樣式改為 primary 或 secondary，馬上就能看出來。要讓按鈕之間有些間距而分散開來，你可以在父節點（對我們而言就是一個 box 元件）上使用 [margin](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#margin-property) 或 [padding](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/#padding-property)。在本教學中，我們會加入 padding：

1. 在 tree view 中，點選包含你所建立的兩個按鈕的 **box [vertical]**。
1. 在 property 區的 **Padding** 區段下，將 **paddingTop** 屬性設為 `10px`。

現在我們的按鈕之間有了更多空間：

![Style Buttons](https://developers.line.biz/media/messaging-api/using-flex-message-simulator/en-style-buttons.png)

就是這樣。你已完成這份製作電子名片的教學！

## Next steps 

當你編寫完一則 Flex Message 後，請如本教學[開頭](https://developers.line.biz/en/docs/messaging-api/using-flex-message-simulator/#copy-json)所介紹的那樣，將結果以 JSON 匯出。當你想使用 Messaging API 傳送 Flex Message 時，這會很方便。更多資訊請參閱 [Call the Messaging API to send the Flex Message](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/#sending-messages-with-the-messaging-api)。

## Conclusion 

Flex Message Simulator 是一項簡單的工具，可協助你不需撰寫程式碼就能發想、設計並製作 Flex Message 原型。就像這份教學一樣，Flex Message 有數不盡的使用情境。使用 Flex Message Simulator 來構思點子、測試原型，並在沒有技術門檻的情況下加速 Flex Message 的製作。使用 Flex Message Simulator 製作獨一無二的 Flex Message 吧！

## Related pages 

- [Send Flex Messages](https://developers.line.biz/en/docs/messaging-api/using-flex-messages/)
- [Flex Message elements](https://developers.line.biz/en/docs/messaging-api/flex-message-elements/)
- [Flex Message layouts](https://developers.line.biz/en/docs/messaging-api/flex-message-layout/)
- [Flex Message](https://developers.line.biz/en/reference/messaging-api/#flex-message)（Messaging API reference）
