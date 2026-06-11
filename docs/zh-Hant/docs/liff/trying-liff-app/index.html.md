# 試用 LIFF 入門範例 app（Trying the LIFF starter app）

當你剛開始學習 LIFF 時，可能不知道該如何著手進行 LIFF app 開發。這種情況下，[LIFF starter app](https://github.com/line/line-liff-v2-starter) 可以幫上忙。

LIFF starter app 是一個範本，具備開發 LIFF app 所需的最基本功能。你可以以 LIFF starter app 為基礎進行自訂，開發出屬於自己的 LIFF app。本頁將透過以下步驟說明 LIFF starter app：

<!-- table of contents -->

讀完本頁後，你將能夠把 LIFF app 部署到伺服器上，並體驗在 LINE 上開啟 LIFF app，藉此了解如何運用 LIFF 建構 app。

<!-- tip start -->

**在試用 LIFF starter app 之前**

- 關於 LIFF 的更多資訊，請參閱 [LIFF overview](https://developers.line.biz/en/docs/liff/overview/)。
- 如果你想在線上試用 LIFF 的各項功能，可使用 [LIFF Playground](https://liff-playground.netlify.app/) 來看看 LIFF 能做些什麼。[LIFF Playground 的原始碼](https://github.com/line/liff-playground)已公開於 GitHub 上，開發者可以設定自己的 LIFF ID 並執行自己的 LIFF Playground。舉例來說，諸如 [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) 或 [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) 等各個 client API，都可以根據開發者的 LIFF ID 在網頁上執行。

<!-- tip end -->

## What is the LIFF starter app? 

LIFF starter app 是一個 LIFF app 的範本。你可以從頭開始建立 LIFF app，但使用 LIFF starter app 能讓你的開發體驗更快速。

LIFF starter app 提供了以 vanilla JavaScript、Next.js 以及 Nuxt 撰寫的實作版本。各個儲存庫如下：

- [使用 vanilla JavaScript 的實作](https://github.com/line/line-liff-v2-starter/tree/master/src/vanilla)
- [使用 Next.js 的實作](https://github.com/line/line-liff-v2-starter/tree/master/src/nextjs)
- [使用 Nuxt 的實作](https://github.com/line/line-liff-v2-starter/tree/master/src/nuxtjs)

你可以依照各個儲存庫的 README 開始開發 LIFF app。本頁將說明如何以 vanilla JavaScript 開始開發 LIFF app。

## How to get started with the LIFF starter app 

本節的目標是將 LIFF starter app 部署到伺服器上，並在 LINE 的 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中開啟它。第一步是在本機環境中確認 LIFF app。接著將 LIFF app 部署到伺服器上，最後在伺服器端設定一個稱為 LIFF ID 的值。

### Environment 

LIFF starter app 在 Node.js 上執行。此外，套件管理使用的是 Yarn。本頁的內容（包含下文所述的 Netlify CLI）已在以下各版本上測試過：

| 名稱                                    | 版本    |
| --------------------------------------- | ------- |
| [Node.js](https://nodejs.org/en)        | 16.13.1 |
| [Yarn](https://yarnpkg.com/)            | 1.22.17 |
| [Netlify CLI](https://cli.netlify.com/) | 9.16.3  |

### Downloading and running the source code 

1. 首先，下載 LIFF starter app 的原始碼。開啟終端機或命令列工具（以下簡稱「終端機」）。在任意目錄下，執行以下指令：

   ```bash
   $ git clone https://github.com/line/line-liff-v2-starter.git
   ```

1. 在下載下來的原始碼（`line-liff-v2-starter` 目錄）的 `src` 目錄中，你會找到以 vanilla JavaScript、Next.js 與 Nuxt 實作的 LIFF app。前往你想使用的實作版本所在的目錄。在此我們將使用 vanilla JavaScript。

   ```bash
   $ cd line-liff-v2-starter/src/vanilla
   ```

   <!-- tip start -->

   **如果你想使用 Next.js 或 Nuxt**

   如果你想使用 Next.js，請執行 `cd line-liff-v2-starter/src/nextjs/`；如果你想使用 Nuxt，請執行 `cd line-liff-v2-starter/src/nuxtjs/`，以前往各自的目錄。

   <!-- tip end -->

1. 下一步是安裝相依套件，然後啟動 LIFF app。執行 `yarn install` 指令進行安裝，再執行 `yarn dev` 指令啟動 LIFF app。當編譯成功的訊息（`compiled successfully`）出現，且終端機畫面的輸出停止時，代表 LIFF app 已在本機伺服器上執行。

   ```bash
   $ yarn install
   $ yarn dev
   ```

1. 當你用瀏覽器存取終端機中顯示的 URL（vanilla JavaScript 為 `http://localhost:3000`）時，你會看到以下畫面。

   ![LIFF app](https://developers.line.biz/media/liff/trying-liff-app/screenshot-pc.png)

   <!-- note start -->

   **你需要設定 LIFF ID**

   你需要將 LIFF ID 設定為環境變數，但我們目前還沒有這麼做。你可以在 [Getting and Setting a LIFF ID](https://developers.line.biz/en/docs/liff/trying-liff-app/#get-and-set-liff-id) 中設定 LIFF ID。

   <!-- note end -->

1. 在你確認 LIFF app 已可在瀏覽器中執行後，在 Windows 上以 ctrl+c、在 macOS 上以 command+c 停止本機伺服器。

### Deploying to a server 

依照目前為止的步驟，我們已經能夠在本機伺服器上啟動 LIFF starter app。下一步是使用 Netlify 將 LIFF app 部署到伺服器上。

<!-- tip start -->

**需要一個 Netlify 帳號**

[Netlify](https://www.netlify.com/) 是一項靜態網站的代管服務，在部署到 Netlify 之前，請先開立帳號。本頁的內容可在 Netlify 的免費方案上執行。

<!-- tip end -->

1. 第一步是安裝 Netlify CLI。這是一個命令列工具，讓你能夠登入 Netlify 並部署你的網站。

   ```bash
   $ npm install -g netlify-cli
   ```

1. 現在你可以使用 `netlify` 指令了。接著，以 `netlify login` 指令登入你的 Netlify 帳號。執行指令後，Netlify 的登入畫面會在你的瀏覽器中開啟，請進行登入。

   <!-- tip start -->

   **在執行 netlify login 指令之前**

   請先在 [Netlify](https://www.netlify.com/) 網站開立帳號，再執行 `netlify login` 指令。

   <!-- tip end -->

   ```bash
   $ netlify login
   ```

1. 登入後，當 Netlify 的授權畫面出現時，點選 **Authorize**。

   ![Netlify authorization screen](https://developers.line.biz/media/liff/trying-liff-app/netlify-authorized.png)

1. 下一步是產生部署用的檔案。這可以在 `src/vanilla` 目錄下執行以下指令來完成。請注意，LIFF starter app 是使用 [webpack](https://webpack.js.org/) 建構的。

   ```bash
   $ yarn build
   ```

1. 現在，HTML 與 JavaScript 檔案已產生在 `src/vanilla/dist` 之下。接著你需要將這些檔案部署到 Netlify。

   若要部署到 Netlify，請在儲存庫的根目錄（`line-liff-v2-starter`）執行 `netlify deploy` 指令。在不加選項的情況下，`netlify deploy` 指令會以草稿狀態進行部署。首先，請嘗試以草稿狀態部署。

   ```bash
   $ cd ../../      # Go to the root directory of the repository
   $ netlify deploy # Deploy in draft state
   ```

   執行 `netlify deploy` 指令後，當系統如下詢問你要部署到哪個網站時，選擇 `Create & configure a new site`。你可以使用上下方向鍵在各選項之間移動。

   ```bash
   This folder isn't linked to a site yet
   ? What would you like to do?
   Link this directory to an existing site
   ❯ +  Create & configure a new site # Create and configure a new site
   ```

   系統會詢問你想在哪個團隊底下建立此網站。沿用預設團隊繼續即可。

   ```bash
   ? Team: (Use arrow keys)
   ❯ testlinedevelopers's team # Continue with the default team
   ```

   系統會詢問你想為此網站取什麼名稱。請輸入一個唯一的名稱。

   ```bash
   ? Site name (optional): # Enter a unique name
   ```

   草稿狀態的部署已完成。你可以用瀏覽器存取終端機中顯示的 `Website Draft URL` 來檢視此頁面。

1. 如果以草稿狀態試用後沒有問題，請在 `netlify deploy` 指令加上 `--prod` 選項，部署到正式環境（production environment）。

   ```bash
   $ netlify deploy --prod # Deploy to the production environment
   ```

你現在已經將你的 LIFF app 部署到 Netlify 了。你可以用網頁瀏覽器存取部署過程中終端機所顯示的 `Website URL` 來檢視此頁面。

### Getting and Setting a LIFF ID 

你現在已經在伺服器上部署了 LIFF starter app。

此時，如果你在[外部瀏覽器（external browser）](https://developers.line.biz/en/glossary/#external-browser)或 [in-app browser](https://developers.line.biz/en/glossary/#line-iab) 中開啟 Netlify 的 `Website URL`，你會看到已部署的 LIFF starter app 以一個頁面的形式呈現。然而，這個 LIFF starter app 還無法在 LINE 的 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中以 LIFF app 的形式開啟。

要將 LIFF starter app 以 LIFF App 的形式開啟，需要一組 LIFF ID。請先閱讀 [Create a channel](https://developers.line.biz/en/docs/liff/getting-started/) 與 [Adding a LIFF app to your channel](https://developers.line.biz/en/docs/liff/registering-liff-apps/) 以取得你的 LIFF ID。

<!-- tip start -->

**輸入端點 URL**

在將 LIFF app 加入頻道（channel）時，你需要輸入 **Endpoint URL**。請在此輸入你在前一步驟部署到正式環境時所取得的 `Website URL`。

<!-- tip end -->

依照上述程序，你便能取得你的 LIFF ID。請將它設定為伺服器端的環境變數 `LIFF_ID`。

1. 若要在 Netlify 中設定環境變數，請使用 `netlify env:set` 指令。也就是說，若要設定 `LIFF_ID`，請執行以下指令：

   ```bash
   $ netlify env:set LIFF_ID "Your LIFF ID"
   ```

1. 設定好環境變數後，請再次部署到 Netlify。這是因為 Netlify 會在部署時套用環境變數。

   ```bash
   $ netlify build
   $ netlify deploy --prod
   ```

   <!-- tip start -->

   **如何確認環境變數**

   你可以在 Netlify 的網站設定（site settings）中確認環境變數。更多資訊請參閱 Netlify Docs 中的 [Build environment variables](https://docs.netlify.com/build/configure-builds/environment-variables/)。

   ![Netlify's site settings](https://developers.line.biz/media/liff/trying-liff-app/netlify-environment.png)

   <!-- tip end -->

1. 現在你可以從 LINE 開啟這個 LIFF app 了，且該 LIFF app 的 URL 會以 LIFF URL 的形式顯示在你於 [LINE Developers Console](https://developers.line.biz/console/) 中所建立頻道的 **LIFF** 分頁中。

   將該 LIFF URL 傳送到 LINE 的聊天室，並在聊天室中點選該 LIFF URL，即可在 LINE 的 [LIFF browser](https://developers.line.biz/en/glossary/#liff-browser) 中開啟此 LIFF app。

   ![LIFF app](https://developers.line.biz/media/liff/trying-liff-app/screenshot-mobile.png)

<!-- tip start -->

**如果你在未設定 LIFF ID 的情況下開啟 LIFF app**

如果你在未設定 `LIFF_ID` 環境變數的情況下開啟 LIFF app，使用 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 初始化 LIFF app 會失敗，但 LIFF starter app 的外觀不會有任何變化。

<!-- tip end -->

<!-- tip start -->

**在本機伺服器上設定 LIFF_ID 時**

若要在本機伺服器上設定 `LIFF_ID`，請執行以下指令：

```bash
$ LIFF_ID="Your LIFF ID" yarn dev
```

<!-- tip end -->

## Next step 

你現在已經準備好開發你的 LIFF app 了。關於實際開發的更多資訊，請參閱 [Developing a LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/)。
