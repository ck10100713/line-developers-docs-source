# LIFF CLI

<!-- table of contents -->

## What is the LIFF CLI 

LIFF CLI 是一個 CLI 工具，能協助你更順暢地開發 LIFF app。

- [GitHub](https://github.com/line/liff-cli)
- [npm](https://www.npmjs.com/package/@line/liff-cli)

LIFF CLI 可讓你執行以下操作：

- 建立、更新、列出與刪除 LIFF app
- 建立 LIFF app 開發環境
- 使用 [LIFF Inspector](https://developers.line.biz/zh-hant/docs/liff/liff-plugin/#liff-inspector) 對你的 LIFF app 進行除錯
- 啟動具備 HTTPS 的本地端開發伺服器

[LIFF Mock](https://developers.line.biz/zh-hant/docs/liff/liff-plugin/#liff-mock) 功能將於未來的更新中加入。

## Operating environment of the LIFF CLI 

LIFF CLI 在 Node.js 上執行。套件管理你可以使用 npm 或 Yarn，但本頁的說明採用 npm。本頁內容已在下列各版本上測試過：

| Name                                                     | Version |
| -------------------------------------------------------- | ------- |
| [LIFF CLI](https://www.npmjs.com/package/@line/liff-cli) | 0.4.1   |
| [LIFF SDK](https://www.npmjs.com/package/@line/liff)     | 2.24.0  |
| [Node.js](https://nodejs.org/en)                         | 22.2.0  |
| [npm](https://www.npmjs.com/)                            | 10.7.0  |

## Install the LIFF CLI 

開啟終端機或命令列工具（以下簡稱「終端機」），並執行以下指令：

```bash
$ npm install -g @line/liff-cli
```

此指令會安裝 LIFF CLI，並讓你能執行 `liff-cli` 指令。

## Manage channels 

`channel` 指令可讓你新增要由 LIFF CLI 管理的頻道（channel），或設定預設頻道。請注意，頻道必須事先在 [LINE Developers Console](https://developers.line.biz/console/) 中建立。

### Add channels 

`add` 子指令可讓你新增要由 LIFF CLI 管理的頻道。將你想新增的頻道之頻道 ID 傳遞給 `add` 子指令，系統會提示你輸入頻道密鑰（channel secret）。輸入頻道密鑰後，該頻道即新增完成。

```bash
$ liff-cli channel add 1234567890
? Channel Secret?: ********************************
Channel 1234567890 is now added.
```

如上所示，當你將頻道 ID 傳遞給各個 LIFF CLI 指令時，該頻道 ID 對應的頻道必須事先以 `add` 子指令新增。

### Set the default channel 

`use` 子指令可讓你設定 LIFF CLI 的預設頻道。將你想設定的頻道之頻道 ID 傳遞給 `use` 子指令即可。

```bash
$ liff-cli channel use 1234567890
Channel 1234567890 is now selected.
```

當各個 LIFF CLI 指令省略頻道 ID 時，便會使用預設頻道。

## Manage LIFF apps 

`app` 指令可讓你建立、更新、列出與刪除 LIFF app。

### Create a LIFF app 

`create` 子指令可讓你建立 LIFF app。若 LIFF app 建立成功，終端機會顯示 LIFF ID。

```bash
$ liff-cli app create \
   --channel-id 1234567890 \
   --name "Brown Coffee" \
   --endpoint-url https://example.com \
   --view-type full
Successfully created LIFF app: 1234567890-AbcdEfgh
```

#### Options 

`create` 子指令提供下列選項：

| Option | Required | Description |
| --- | --- | --- |
| `-c`, `--channel-id` |  | 指定你想為其建立 LIFF app 的頻道之頻道 ID。若省略頻道 ID，則會指定[預設頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-use)的頻道 ID。 |
| `-n`, `--name` | ✅ | 指定 LIFF app 名稱。LIFF app 名稱不可包含「LINE」或類似字串，或不適當的字串。 |
| `-e`, `--endpoint-url` | ✅ | <p>指定端點 URL（endpoint URL）。這是實作 LIFF app 的網頁應用程式之 URL（例如 `https://example.com`）。當使用 LIFF URL 啟動 LIFF app 時會用到此 URL。</p><p>URL scheme 必須為 **https**。不可指定 URL fragment（#URL-fragment）。</p> |
| `-v`, `--view-type` | ✅ | <p>LIFF app 畫面的大小。請指定下列其中一個值：</p><ul><li>`full`</li><li>`tall`</li><li>`compact`</li></ul>詳情請參閱 [Size of the LIFF browser](https://developers.line.biz/zh-hant/docs/liff/overview/#screen-size)。 |

### Update a LIFF app 

`update` 子指令可讓你更新 LIFF app。

```bash
$ liff-cli app update \
   --liff-id 1234567890-AbcdEfgh \
   --channel-id 1234567890 \
   --name "Brown Cafe"
Successfully updated LIFF app: 1234567890-AbcdEfgh
```

#### Options 

`update` 子指令提供下列選項：

| Option | Required | Description |
| --- | --- | --- |
| `--liff-id` | ✅ | 指定你想更新的 LIFF ID。 |
| `--channel-id` |  | 指定 LIFF app 所屬頻道的頻道 ID。若省略頻道 ID，則會指定[預設頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-use)的頻道 ID。 |
| `--name` |  | 指定 LIFF app 名稱。LIFF app 名稱不可包含「LINE」或類似字串，或不適當的字串。 |
| `--endpoint-url` |  | <p>指定端點 URL。這是實作 LIFF app 的網頁應用程式之 URL（例如 `https://example.com`）。當使用 LIFF URL 啟動 LIFF app 時會用到此 URL。</p><p>URL scheme 必須為 **https**。不可指定 URL fragment（#URL-fragment）。</p> |
| `--view-type` |  | <p>LIFF app 畫面的大小。請指定下列其中一個值：</p><ul><li>`full`</li><li>`tall`</li><li>`compact`</li></ul>詳情請參閱 [Size of the LIFF browser](https://developers.line.biz/zh-hant/docs/liff/overview/#screen-size)。 |

### List LIFF apps 

`list` 子指令可讓你列出 LIFF app。LIFF ID 與 LIFF app 名稱會以清單形式顯示。

```bash
$ liff-cli app list --channel-id 1234567890
LIFF apps:
1234567890-AbcdEfgh: Brown Coffee
1234567890-IjklMnop: Brown Cafe
```

#### Options 

`list` 子指令提供下列選項：

| Option | Required | Description |
| --- | --- | --- |
| `--channel-id` |  | 指定你想列出 LIFF app 的頻道之頻道 ID。若省略頻道 ID，則會指定[預設頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-use)的頻道 ID。 |

### Delete a LIFF app 

`delete` 子指令可讓你刪除 LIFF app。

```bash
$ liff-cli app delete \
   --liff-id 1234567890-AbcdEfgh \
   --channel-id 1234567890
Deleting LIFF app...
Successfully deleted LIFF app: 1234567890-AbcdEfgh
```

#### Options 

`delete` 子指令提供下列選項：

| Option | Required | Description |
| --- | --- | --- |
| `--liff-id` | ✅ | 指定你想刪除的 LIFF app 之 LIFF ID。 |
| `--channel-id` |  | 指定 LIFF app 所屬頻道的頻道 ID。若省略頻道 ID，則會指定[預設頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-use)的頻道 ID。 |

## Create a LIFF app template 

`scaffold` 指令可讓你使用 [Create LIFF App](https://developers.line.biz/zh-hant/docs/liff/cli-tool-create-liff-app/) 建立 LIFF app 範本。將 LIFF app 的專案名稱傳遞給 `scaffold` 指令，便會以該專案名稱執行 Create LIFF App。

```bash
$ liff-cli scaffold my-app --liff-id 1234567890-AbcdEfgh
```

關於 Create LIFF App 的更多資訊，請參閱 [Building a LIFF app development environment with Create LIFF App](https://developers.line.biz/zh-hant/docs/liff/cli-tool-create-liff-app/)。

### Options 

`scaffold` 指令提供下列選項：

| Option            | Required | Description                        |
| ----------------- | -------- | ---------------------------------- |
| `-l`, `--liff-id` |          | 指定 LIFF app 的 LIFF ID。 |

## Create a LIFF app development environment 

`init` 指令可讓你建立 LIFF app 開發環境。`init` 指令會依序執行以下三項處理：

1. [新增頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-add)
1. [建立 LIFF app](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-liff-apps-create)
1. [建立 LIFF app 範本](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#scaffold)

```bash
$ liff-cli init \
   --channel-id 1234567890 \
   --name "Brown Coffee" \
   --view-type full \
   --endpoint-url https://example.com
```

舉例來說，上述指令會新增頻道 ID 為「1234567890」的頻道。接著，該指令會為此頻道建立一個 LIFF app，其 LIFF app 名稱為「Brown Coffee」、端點 URL 為「https://example.com」、畫面大小為「Full」。最後，以所建立 LIFF app 的 LIFF ID 來建立範本。

```bash
liff-cli init \
   --channel-id 1234567890 \
   --name "Brown Coffee" \
   --view-type full \
   --endpoint-url https://example.com

? Channel Secret?: ********************************
Channel 1234567890 is now added.
Welcome to the Create LIFF App
? Which template do you want to use? vanilla
? JavaScript or TypeScript? JavaScript
? Which package manager do you want to use? npm

Installing dependencies:
- @line/liff

removed 10 packages in 944ms

22 packages are looking for funding
  run `npm fund` for details

Installing devDependencies:
- vite

added 10 packages in 7s

25 packages are looking for funding
  run `npm fund` for details

Done! Now run:

  cd Brown Coffee
  npm run dev

App 1234567890-AbcdEfgh successfully created.

Now do the following:
  1. go to app directory: `cd Brown Coffee`
  2. create certificate key files (e.g. `mkcert localhost`, see: https://developers.line.biz/en/docs/liff/liff-cli/#serve-operating-conditions )
  3. run LIFF app template using command above (e.g. `npm run dev` or `yarn dev`)
  4. open new terminal window, navigate to `Brown Coffee` directory
  5. run `liff-cli serve -l 1234567890-AbcdEfgh -u http://localhost:${PORT FROM STEP 3.}/`
  6. open browser and navigate to http://localhost:${PORT FROM STEP 3.}/
```

### Options 

`init` 指令提供下列選項。若你省略某個選項，執行 `init` 指令時系統會提示你輸入該選項。

```bash
$ liff-cli init
? Channel ID? 1234567890
? App name? Brown Coffee
? View type? full
? Endpoint URL? (leave empty for default 'https://localhost:9000') https://example.com
```

| Option | Required | Description |
| --- | --- | --- |
| `-c`, `--channel-id` | ✅ \*1 | 指定你想為其建立 LIFF app 的頻道之頻道 ID。 |
| `-n`,`--name` | ✅ \*2 | 指定 LIFF app 名稱。LIFF app 名稱不可包含「LINE」或類似字串，或不適當的字串。 |
| `-v`, `--view-type` | ✅ \*2 | <p>LIFF app 畫面的大小。請指定下列其中一個值：</p><ul><li>`full`</li><li>`tall`</li><li>`compact`</li></ul>詳情請參閱 [Size of the LIFF browser](https://developers.line.biz/zh-hant/docs/liff/overview/#screen-size)。 |
| `-e`, `--endpoint-url` |  | <p>指定端點 URL。這是 LIFF app 將部署到的 URL（例如 `https://example.com`）。當使用 LIFF URL 啟動 LIFF app 時會用到此 URL。</p><p>URL scheme 必須為 **https**。不可指定 URL fragment（#URL-fragment）。</p> |

\*1 若你未設定[預設頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-use)，則需指定此選項或透過提示輸入。<br>\*2 你需指定此選項或透過提示輸入。

## Launch a local development server with HTTPS 

`serve` 指令可讓你啟動具備 HTTPS 的本地端開發伺服器。

在 `serve` 指令中指定執行你 LIFF app 的本地端開發伺服器，便會啟動一個具備 HTTPS 的本地端代理伺服器（local proxy server），並將你 LIFF app 的端點 URL 改寫為本地端代理伺服器的 URL。這讓你更容易以 HTTPS 啟動本地端開發伺服器。

<!-- note start -->

**請勿對已發布的 LIFF app 執行 serve 指令**

`serve` 指令會將 LIFF app 的端點 URL 改寫為本地端代理伺服器的 URL，使用者將因此無法存取該 LIFF app。因此，請勿對已發布的 LIFF app 執行 `serve` 指令。

![](https://developers.line.biz/media/liff/liff-cli/endpoint-url-en.png)

<!-- note end -->

```bash
# If you specify your local development server with the URL
$ liff-cli serve \
   --liff-id 1234567890-AbcdEfgh \
   --url http://localhost:3000/

Successfully updated endpoint url for LIFF ID: 1234567890-AbcdEfgh.

→  LIFF URL:     https://liff.line.me/1234567890-AbcdEfgh
→  Proxy server: https://localhost:9000/
```

```bash
# If you specify your local development server with the host and port number
$ liff-cli serve \
   --liff-id 1234567890-AbcdEfgh \
   --host localhost \
   --port 3000

Successfully updated endpoint url for LIFF ID: 1234567890-AbcdEfgh.

→  LIFF URL:     https://liff.line.me/1234567890-AbcdEfgh
→  Proxy server: https://localhost:9000/
```

### Debug your LIFF app with the LIFF Inspector 

在 `serve` 指令中指定 `--inspect` 選項，你便能使用 [LIFF Inspector](https://developers.line.biz/zh-hant/docs/liff/liff-plugin/#liff-inspector) 對你的 LIFF app 進行除錯。

`--inspect` 選項會以 HTTPS 啟動 LIFF Inspector 的 LIFF Inspector Server。這讓開發者只需在其 LIFF app 中安裝 LIFF Inspector Plugin，即可對 LIFF app 進行除錯。詳情請參閱 LIFF Inspector 的 [README](https://github.com/line/liff-inspector/blob/main/README.md)。

```bash
$ liff-cli serve \
   --liff-id 1234567890-AbcdEfgh \
   --url http://localhost:3000/ \
   --inspect

Successfully updated endpoint url for LIFF ID: 1234567890-AbcdEfgh.

→  LIFF URL:     https://liff.line.me/1234567890-AbcdEfgh
→  Proxy server: https://localhost:9000/?li.origin=wss%3A%2F%2Flocalhost%3A9222
Debugger listening on wss://192.168.1.6:9222

You need to serve this server over SSL/TLS
For help, see: https://github.com/line/liff-inspector#important-liff-inspector-server-need-to-be-served-over-ssltls
```

當你存取 LIFF URL 時，執行 `serve` 指令的終端機會出現一個以 `devtools://devtools/` 開頭的 URL。若你以 Google Chrome 開啟此 URL，便可在 Google Chrome 上對該 LIFF app 進行除錯。

```bash
connection from client, id: 1234567890-AbcdEfgh
DevTools URL: devtools://devtools/bundled/inspector.html?wss=localhost:9222/?hi_id=1234567890-AbcdEfgh
```

### Expose your local development server 

LIFF CLI 支援將 [ngrok](https://ngrok.com/) 作為代理。若要使用 ngrok，請為 `serve` 指令的 `--proxy-type` 選項指定下列其中一個值：

- [ngrok](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#serve-proxy-type-ngrok)
- [ngrok-v1](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#serve-proxy-type-ngrok-v1)（已淘汰）

#### Proxy type: `ngrok` 

為 `--proxy-type` 選項指定 `ngrok`，可讓你使用 [ngrok](https://github.com/ngrok/ngrok-javascript) 取代本地端代理伺服器。這讓你能對外公開你的本地端開發伺服器。使用 ngrok 時，請將 ngrok 的 authtoken 設為環境變數 `NGROK_AUTHTOKEN`。

```bash
$ NGROK_AUTHTOKEN={Authentication token} liff-cli serve \
   --liff-id 1234567890-AbcdEfgh \
   --url http://localhost:3000/ \
   --proxy-type ngrok

Successfully updated endpoint url for LIFF ID: 1234567890-AbcdEfgh.

→  LIFF URL:     https://liff.line.me/1234567890-AbcdEfgh
→  Proxy server: https://1234abcd.ngrok.example.com/
```

#### Proxy type: `ngrok-v1` (deprecated) 

<!-- note start -->

**ngrok-v1 已淘汰**

ngrok v1 已不再開發或維護，因此 `ngrok-v1` 已淘汰。使用 ngrok 時，請將代理類型指定為 [`ngrok`](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#serve-proxy-type-ngrok)。

<!-- note end -->

為 `--proxy-type` 選項指定 `ngrok-v1`，可讓你使用 [ngrok v1](https://github.com/inconshreveable/ngrok) 取代本地端代理伺服器。這讓你能對外公開你的本地端開發伺服器。若要使用此功能，你需要安裝 [ngrok v1](https://github.com/inconshreveable/ngrok) 與 [node-pty](https://www.npmjs.com/package/node-pty)。

```bash
$ liff-cli serve \
  --liff-id 1234567890-AbcdEfgh \
  --url http://127.0.0.1:3000/ \
  --proxy-type ngrok-v1

ngrok-v1 is experimental feature.
Successfully updated endpoint url for LIFF ID: 1234567890-AbcdEfgh.

→  LIFF URL:     https://liff.line.me/1234567890-AbcdEfgh
→  Proxy server: https://1234abcd.ngrok.example.com/
```

### Operating conditions of the `serve` command 

`serve` 指令要能運作，必須符合下列所有條件：

- 為 localhost 建立有效的憑證（`localhost.pem`）與私鑰（`localhost-key.pem`）
- 在你建立 `localhost.pem` 與 `localhost-key.pem` 的位置（例如 LIFF app 專案的根目錄）執行 `serve` 指令

請依照下列步驟，為 localhost 建立有效的憑證（`localhost.pem`）與私鑰（`localhost-key.pem`）。此處使用 [mkcert](https://github.com/FiloSottile/mkcert)。關於 mkcert 的更多資訊，請參閱 mkcert 的 [README](https://github.com/FiloSottile/mkcert/blob/master/README.md)。

1. 執行以下指令以安裝 `mkcert`：

```bash
# For macOS (using Homebrew)
$ brew install mkcert

# For Windows (using Chocolatey)
$ choco install mkcert
```

2. 執行 `mkcert -install` 以建立本地端憑證頒發機構（local certificate authority）。

```bash
$ mkcert -install
```

3. 執行 `mkcert localhost` 以為 localhost 建立有效的憑證（`localhost.pem`）與私鑰（`localhost-key.pem`）。

```bash
$ mkcert localhost
Note: the local CA is not installed in the Firefox trust store.
Run "mkcert -install" for certificates to be trusted automatically ⚠️

Created a new certificate valid for the following names 📜
 - "localhost"

The certificate is at "./localhost.pem" and the key at "./localhost-key.pem" ✅
```

### Options 

`serve` 指令提供下列選項：

| Option | Required | Description |
| --- | --- | --- |
| `-l`、 `--liff-id` | ✅ | 指定你本地端開發伺服器上 LIFF app 的 LIFF ID。你只能指定[預設頻道](https://developers.line.biz/zh-hant/docs/liff/liff-cli/#manage-channels-use)中 LIFF app 的 LIFF ID。 |
| `-u`、 `--url` | ✅ \*1 | 指定你本地端開發伺服器的 URL。 |
| `--host` | ✅ \*2 | 指定你本地端開發伺服器的 host。 |
| `--port` | ✅ \*2 | 指定你本地端開發伺服器的連接埠號（port number）。 |
| `-i`、 `--inspect` |  | 指定此選項時，會啟動 LIFF Inspector。 |
| `--proxy-type` |  | <p>要使用的代理類型。請指定下列其中一個值：</p><ul><li>`local-proxy`：本地端代理</li><li>`ngrok`：[ngrok](https://github.com/ngrok/ngrok-javascript)</li><li>`ngrok-v1`：[ngrok v1](https://github.com/inconshreveable/ngrok)（已淘汰）</li></ul>預設值為 `local-proxy`。 |
| `--ngrok-command` |  | 指定執行 ngrok v1 的指令。預設值為 `ngrok`。 |
| `--local-proxy-port` |  | 指定供你本地端開發伺服器使用之本地端代理伺服器所監聽的連接埠號。預設值為 `9000`。 |
| `--local-proxy-inspector-port` |  | 指定供 LIFF Inspector Server 使用之本地端代理伺服器所監聽的連接埠號。預設值為 `9223`。 |

\*1 以 URL 指定你本地端開發伺服器時為必填<br>\*2 以 host 與連接埠號指定你本地端開發伺服器時為必填
