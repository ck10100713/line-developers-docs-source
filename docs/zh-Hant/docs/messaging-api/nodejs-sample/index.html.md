# 教學 - 製作一個回覆機器人（Tutorial - Make a reply bot）

在本教學中，你將學會如何透過回覆機器人，使用 Messaging API 與 Node.js 來傳送訊息。

Messaging API 讓你的服務與 LINE 使用者之間能進行雙向溝通。透過 Messaging API，你可以善用它所提供的各種功能來提升與使用者的互動。這些功能包括傳送各種類型的訊息、取得使用者個人檔案、取得使用者傳送的內容，以及[更多功能](https://developers.line.biz/en/docs/messaging-api/overview/#what-you-can-do)。

本教學的成果是一個能自動回覆使用者訊息的應用程式。

![Conversation with a sample bot](https://developers.line.biz/media/messaging-api/node-js-sample/sample-bot-test.png)

## Before you start 

本教學假設你已具備 JavaScript 與 Node.js 的基本知識。在繼續本教學之前，我們建議你先閱讀 [Messaging API overview](https://developers.line.biz/en/docs/messaging-api/overview/)。

<!-- tip start -->

**本教學不使用 SDK**

為了協助你學習 Messaging API，本教學示範如何使用 Node.js 搭配 Messaging API，但不使用 LY Corporation 提供的 SDK。若想加快開發速度並減少 Node.js 專案的程式碼行數，可以試試 [LINE Messaging API SDK for nodejs](https://line.github.io/line-bot-sdk-nodejs/)。

<!-- tip end -->

### Preparation 

為了在本教學中建立回覆機器人，請先依下列說明註冊所需的系統並安裝所需的工具。

註冊這些帳號：

- 一個 [LINE Developers Console](https://developers.line.biz/console/) 帳號：使用你的 LINE 帳號或商業帳號登入 LINE Developers Console，若你尚未擁有開發者帳號，請[建立開發者帳號](https://developers.line.biz/en/docs/line-developers-console/login-account/#register-as-developer)。
- 一個 [Heroku](https://www.heroku.com/) 帳號

  <!-- note start -->

  **Heroku 的免費方案已停止提供**

  Heroku 的免費方案自 2022 年 11 月 27 日起停止提供。若想免費嘗試本教學，請改用其他平台。如需更多資訊，請參閱 [Heroku’s Next Chapter](https://www.heroku.com/blog/next-chapter/)。

  <!-- note end -->

安裝這些工具：

- [Node.js](https://nodejs.org/en)
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
- [Git](https://git-scm.com/downloads)

## 1. Set up Heroku 

登入 Heroku CLI。在你的終端機或命令列工具中執行此指令。

```sh
heroku login
```

為本教學建立一個目錄並移動到該目錄。初始化 Git，並用 Heroku 建立一個應用程式。請將 `{Name of your app}` 替換為一個獨一無二的名稱，例如 `msg-api-tutorial-{YYYYMMDD}`。

```sh
mkdir sample-app
cd sample-app
git init
heroku create {Name of your app}
```

若你的應用程式建立成功，會產生一個格式為 `https://{Name of your app}.herokuapp.com/` 的 Heroku URL。本教學稍後會用到這個 URL，所以請保留它。在瀏覽器中開啟這個 Heroku URL，會顯示歡迎頁面。

![Welcome page](https://developers.line.biz/media/messaging-api/node-js-sample/welcome-page.png)

## 2. Set up the project 

我們需要透過 `package.json` 檔案讓 npm 辨識我們的專案。這個檔案會包含此專案的中繼資料（metadata）並定義相依套件。使用 `npm init` 指令來建立這個檔案，它會初始化你的 npm 套件。指定 `-y` 選項可略過設定過程中詢問的所有問題，因為本教學不需要任何特殊設定。

```sh
npm init -y
```

執行後，會建立一個類似這樣的 `package.json` 檔案：

```json
{
  "name": "sample-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

接著，指定 start script。這會讓像 Heroku 這樣的伺服器平台知道啟動伺服器時要使用哪個檔案。在本教學中，我們會將 `index.js` 設為伺服器設定檔。在文字編輯器中開啟 `package.json`，並為 `"start"` 屬性指定 `"node index.js"`。

```json
{
  "name": "sample-app",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}
```

使用下方指令安裝 [Express.js](https://expressjs.com/) 套件。這是一個輕量的 Node.js 網頁伺服器框架，我們會在專案中使用它。

```sh
npm install express
```

當 Express.js 安裝完成後，`package.json` 中會新增一個套件相依項目。同時，也會建立一個名為 `node_modules` 的目錄。這個目錄包含本機安裝的套件，而我們不希望將此目錄中的內容推送到 Heroku。要將此目錄過濾掉，請建立一個 `.gitignore` 檔案：

```sh
touch .gitignore
```

在文字編輯器中開啟剛建立的 `.gitignore` 檔案，並如下所示在檔案中加入要過濾掉的目錄名稱。

```
node_modules/
```

這可避免指定的目錄被推送。

## 3. Implement the bot 

設定完成後，現在讓我們開始實作回覆機器人：

1. [Set global configuration](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#global-config)
2. [Set middleware](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#middleware-config)
3. [Set routing](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#routing-config)
4. [Send a reply](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#send-reply)

### 3-1. Set global configuration 

讓我們建立用於伺服器設定的主要 JavaScript 檔案 `index.js`。

```sh
touch index.js
```

在剛建立的 `index.js` 檔案中加入程式碼，以匯入並實例化我們安裝的套件 `express`。同時也匯入 `https` 套件，用來處理進入機器人的 HTTP 請求。我們不需要安裝這個套件，因為它是 Node.js 預設內建的。

在文字編輯器中開啟 `index.js`，並加入這段程式碼：

```javascript
const https = require("https");
const express = require("express");
const app = express();
```

現在，加入環境變數以簡化設定流程並保護憑證。`process.env.PORT` 變數指定伺服器要監聽哪個連接埠。`process.env.LINE_ACCESS_TOKEN` 則包含呼叫 Messaging API 所需的[頻道存取權杖（channel access token）](https://developers.line.biz/en/glossary/#channel-access-token)。在 `index.js` 中，於匯入的套件下方加入這些設定：

```javascript
const PORT = process.env.PORT || 3000;
const TOKEN = process.env.LINE_ACCESS_TOKEN;
```

### 3-2. Set middleware 

我們安裝並匯入的 Express.js 是一個中介軟體（middleware）網頁框架。中介軟體函式決定了請求-回應週期的流程。

在本教學中，我們會使用 Express.js 的函式 `express.json()` 與 `express.urlencoded()`。這些是預先定義的中介軟體函式，分別用來辨識以 JSON 格式，以及以字串或陣列格式傳入的請求物件。要載入這些中介軟體函式，請呼叫 `app.use()`。在 `index.js` 檔案中加入這段程式碼：

```javascript
app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);
```

### 3-3. Set routing 

現在讓我們為機器人伺服器加入基本的路由邏輯。為了避免健康檢查（health check）失敗，當有 HTTP GET 請求傳送到我們網域的根路徑（`/`）時，我們回傳狀態碼 `200`。在 `index.js` 檔案中加入這段程式碼：

```javascript
app.get("/", (req, res) => {
  res.sendStatus(200);
});
```

接著，使用 `app.listen()` 函式為我們的伺服器設定一個監聽器（listener）。將監聽器的連接埠設為我們稍早設定的 `PORT` 環境變數。除非你指定不同的連接埠號碼，否則我們的監聽器會監聽 `3000`，因為那是我們設定的值。在 `index.js` 中加入這段程式碼：

```javascript
app.listen(PORT, () => {
  console.log(`Example app listening at http://localhost:${PORT}`);
});
```

現在我們的伺服器已能監聽，我們要加入程式碼來處理 LINE Platform 傳送到 Webhook URL 的請求。當使用者與你的機器人互動時，LINE Platform 會傳送一個請求（webhook 事件）到你的機器人伺服器所代管的 Webhook URL。要處理這類請求，請使用 `app.post()` 進行路由。在 `index.js` 檔案中，於 `app.get()` 與 `app.listen()` 函式之間加入這段程式碼：

```javascript
app.post("/webhook", function (req, res) {
  res.send("HTTP POST request sent to the webhook URL!");
});
```

這段程式碼告訴機器人伺服器：當有 HTTP POST 請求傳送到 `/webhook` 端點（endpoint）時，回傳 HTTP 回應 `HTTP POST request sent to the webhook URL!`。

到目前為止，你的 `index.js` 看起來應該類似這樣：

```javascript
const https = require("https");
const express = require("express");
const app = express();
const PORT = process.env.PORT || 3000;
const TOKEN = process.env.LINE_ACCESS_TOKEN;

app.use(express.json());
app.use(
  express.urlencoded({
    extended: true,
  })
);

app.get("/", (req, res) => {
  res.sendStatus(200);
});

app.post("/webhook", function (req, res) {
  res.send("HTTP POST request sent to the webhook URL!");
});

app.listen(PORT, () => {
  console.log(`Example app listening at http://localhost:${PORT}`);
});
```

### 3-4. Send a reply 

現在該來實作回覆機器人的核心功能：回覆使用者的訊息。我們要做的第一件事，是偵測使用者何時傳送訊息給你。當我們在 Webhook URL 收到 `type` 屬性設為 `message` 的[訊息事件（message event）](https://developers.line.biz/en/reference/messaging-api/#message-event)時，就偵測到了。

<!-- warning start -->

**若要將機器人發布供正式環境使用，請驗證簽章**

如果你要將這個範例機器人發布到正式（production）環境，供不特定數量的使用者使用，就必須進行簽章驗證。請驗證請求標頭 `x-line-signature` 中的簽章，以確認 HTTP 請求是由 LINE Platform 傳送的。

如需更多關於如何驗證簽章的資訊，請參閱 [Verify signature](https://developers.line.biz/en/docs/messaging-api/receiving-messages/#verify-signature)。

<!-- warning end -->

要回覆使用者，我們使用[傳送回覆訊息（send reply message）](https://developers.line.biz/en/reference/messaging-api/#send-reply-message)端點。從 `index.js` 檔案中的 `app.post()`，呼叫傳送回覆訊息端點（`https://api.line.me/v2/bot/message/reply`）。將 `app.post` 替換為這段程式碼。詳細說明請參閱下方程式碼中的註解：

```javascript
app.post("/webhook", function (req, res) {
  res.send("HTTP POST request sent to the webhook URL!");
  // If the user sends a message to your bot, send a reply message
  if (req.body.events[0].type === "message") {
    // You must stringify reply token and message data to send to the API server
    const dataString = JSON.stringify({
      // Define reply token
      replyToken: req.body.events[0].replyToken,
      // Define reply messages
      messages: [
        {
          type: "text",
          text: "Hello, user",
        },
        {
          type: "text",
          text: "May I help you?",
        },
      ],
    });

    // Request header. See Messaging API reference for specification
    const headers = {
      "Content-Type": "application/json",
      Authorization: "Bearer " + TOKEN,
    };

    // Options to pass into the request, as defined in the http.request method in the Node.js documentation
    const webhookOptions = {
      hostname: "api.line.me",
      path: "/v2/bot/message/reply",
      method: "POST",
      headers: headers,
      body: dataString,
    };

    // When an HTTP POST request of message type is sent to the /webhook endpoint,
    // we send an HTTP POST request to https://api.line.me/v2/bot/message/reply
    // that is defined in the webhookOptions variable.

    // Define our request
    const request = https.request(webhookOptions, (res) => {
      res.on("data", (d) => {
        process.stdout.write(d);
      });
    });

    // Handle error
    // request.on() is a function that is called back if an error occurs
    // while sending a request to the API server.
    request.on("error", (err) => {
      console.error(err);
    });

    // Finally send the request and the data we defined
    request.write(dataString);
    request.end();
  }
});
```

## 4. Prepare a Messaging API channel 

要使用 Messaging API，你需要有一個 Messaging API 頻道（channel）並註冊你的 Webhook URL。若你尚未擁有頻道，請[建立一個頻道](https://developers.line.biz/en/docs/messaging-api/getting-started/)。

在 LINE Developers Console 的 Messaging API 頻道頁面中，開啟 **Messaging API** 分頁並核發一個[頻道存取權杖（channel access token）](https://developers.line.biz/en/docs/basics/channel-access-token/)。我們會在[將機器人部署到 Heroku](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#deploy-on-heroku) 時使用這個權杖。

![Channel access token section in a Messaging API channel](https://developers.line.biz/media/messaging-api/node-js-sample/channel-access-token-en.png)

接著，註冊你的 Webhook URL。在 **Messaging API** 分頁中，根據你在 [Set up Heroku](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#set-up-heroku) 一節取得的 Heroku URL，填入你的伺服器監聽 webhook 的 URL。這個 URL 的格式為 `https://{Name of your app}.herokuapp.com/webhook`。請注意，**Webhook URL** 不是 `https://{Name of your app}.herokuapp.com/`。

<!-- tip start -->

**忘記 Heroku URL 了嗎？**

如果你忘記或遺失了 Heroku URL，可以從 [Heroku Dashboard](https://dashboard.heroku.com/) 取得該 URL。

<!-- tip end -->

最後，啟用 **Use webhook** 設定。

!["Enable webhook" setting in Messaging API tab](https://developers.line.biz/media/messaging-api/node-js-sample/enable-webhook-en.png)

要測試你的機器人，請掃描 **Messaging API** 分頁上的 QR code，在 LINE 上將與你機器人關聯的 LINE 官方帳號（LINE Official Account）加為好友。為了測試，請停用 **Auto-reply messages** 與 **Greeting messages** 設定。

現在你的 Messaging API 頻道就準備好了！

## 5. Deploy to Heroku 

稍早在[全域設定](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#global-config)一節中，我們設定了一個環境變數 `LINE_ACCESS_TOKEN` 作為頻道存取權杖。為了讓部署到 Heroku 的應用程式能正常運作，我們需要設定並註冊環境變數 `LINE_ACCESS_TOKEN`。

要透過環境變數註冊你的頻道存取權杖，請在終端機或命令列工具中執行此指令。將 `LINE_ACCESS_TOKEN` 設為你在 [Prepare a Messaging API channel](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#prepare-channel) 一節取得的頻道存取權杖。

```sh
heroku config:set LINE_ACCESS_TOKEN={enter your channel access token here}
```

現在你的應用程式可以部署了！將你的程式碼推送到 Heroku。在終端機或命令列工具中執行這些指令：

```sh
git add .
git commit -m "First commit"
git push heroku main
```

### Verify webhook URL 

在測試機器人之前，我們要先確認 webhook 是否正常運作。前往你在 [Prepare a Messaging API channel](https://developers.line.biz/en/docs/messaging-api/nodejs-sample/#prepare-channel) 一節中建立的頻道的 **Messaging API** 分頁。在 **Webhook URL** 中點選 **Verify**，以確認 webhook 是否正常運作。如果 Webhook URL 沒有問題，你會看到一則訊息「Success」。你已經做出一個可運作的機器人了。

### Try the bot 

試著在你的 LINE 上傳送訊息給機器人。如果一切順利，你會收到來自機器人的訊息，如下所示：

![Conversation with a sample bot in the LINE chat room](https://developers.line.biz/media/messaging-api/node-js-sample/sample-bot-test.png)

### Troubleshoot the sample bot 

如果你的機器人無法運作，請使用此指令檢查 Heroku 的日誌：

```sh
heroku logs --tail
```

## Next steps 

繼續你在 Messaging API 上的冒險。你的下一個任務是為機器人加入更多功能：

- 加入[圖文選單（rich menus）](https://developers.line.biz/en/reference/messaging-api/#rich-menu)，向使用者顯示可點選的選項。
- 根據使用者觸發動作時收到的[動作物件（action object）](https://developers.line.biz/en/reference/messaging-api/#action-objects)來回覆使用者。
- [取得使用者的個人檔案](https://developers.line.biz/en/reference/messaging-api/#get-profile)，並根據個人檔案資訊傳送客製化的訊息。

如本教學開頭所介紹的，[LINE Messaging API SDK for nodejs](https://line.github.io/line-bot-sdk-nodejs/) 能幫助你更快速地建立機器人。動手試試看吧！

## Learn more 

- [Messaging API reference](https://developers.line.biz/en/reference/messaging-api/)
- [Messaging API overview](https://developers.line.biz/en/docs/messaging-api/overview/)
- [https.request specification (Node.js)](https://nodejs.org/api/https.html#https_https_request_options_callback)
