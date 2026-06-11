# LINE Messaging API SDK

LINE Messaging API SDK 包含函式庫、工具與範例，讓你能更輕鬆地開始使用 Messaging API 開發機器人應用程式。無論是[官方 SDK](https://developers.line.biz/en/docs/messaging-api/line-bot-sdk/#official-sdks) 還是[社群 SDK](https://developers.line.biz/en/docs/messaging-api/line-bot-sdk/#community-sdks)，皆為開放原始碼，並提供多種程式語言的版本。

### Official SDKs 

官方 SDK 支援下列語言：

- [Java](https://github.com/line/line-bot-sdk-java)（[版本資訊](https://github.com/line/line-bot-sdk-java/releases)）
- [PHP](https://github.com/line/line-bot-sdk-php)（[版本資訊](https://github.com/line/line-bot-sdk-php/releases)）
- [Python](https://github.com/line/line-bot-sdk-python)（[版本資訊](https://github.com/line/line-bot-sdk-python/releases)）
- [Node.js](https://github.com/line/line-bot-sdk-nodejs)（[版本資訊](https://github.com/line/line-bot-sdk-nodejs/releases)）
- [Go](https://github.com/line/line-bot-sdk-go)（[版本資訊](https://github.com/line/line-bot-sdk-go/releases)）
- [Ruby](https://github.com/line/line-bot-sdk-ruby)（[版本資訊](https://github.com/line/line-bot-sdk-ruby/releases)）

#### Archives 

下列語言的官方 SDK 將不再更新。各 SDK 仍可繼續使用，但不會再進行任何變更，例如新增功能、修正錯誤或安全性改善。

- [Perl](https://github.com/line/line-bot-sdk-perl)（[版本資訊](https://github.com/line/line-bot-sdk-perl/releases)）

### LINE OpenAPI 

LINE OpenAPI 是一組由 LINE Platform 提供的 API 介面，例如 Messaging API 與 LIFF server API，並依照 OpenAPI 規格定義。透過 [OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator) 與 [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) 等程式碼產生器，即使是未提供 SDK 的程式語言，你也能輕鬆使用 LINE Platform 提供的各項功能。

- [LINE OpenAPI](https://github.com/line/line-openapi)

### Community SDKs and libraries 

社群 SDK 與函式庫由第三方開發者開發，並以一般開放原始碼授權條款提供。LY Corporation 對社群 SDK 進行有限度的審查，但不提供官方支援或保證。請參閱各社群 SDK 的授權條款與免責聲明。

| 函式庫 | 語言／<br />技術 | 說明 | 發佈者 | 授權 | Stars |
| --- | --- | --- | --- | --- | --- |
| [fireliff-cli](https://github.com/micksatana/fireliff-cli) | N/A | LIFF 的 CLI | [intocode](https://github.com/intocode-dev) | MIT | [![GitHub stars](https://img.shields.io/github/stars/intocode-io/fireliff-cli.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/micksatana/fireliff-cli) |
| [LINEChannelConnector](https://github.com/kenakamu/LINEChannelConnector) | N/A | 供 BotBuilder 使用的 LINE Channel Connector | [kenakamu](https://github.com/kenakamu) | MIT | [![GitHub stars](https://img.shields.io/github/stars/kenakamu/LINEChannelConnector.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/kenakamu/LINEChannelConnector) |
| [line_bot_framework](https://github.com/shidec/line_bot_framework) | PHP | 機器人開發框架 | [shidec](https://github.com/shidec) | MIT | [![GitHub stars](https://img.shields.io/github/stars/shidec/line_bot_framework.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/shidec/line_bot_framework) |
| [line-chatbot-boilerplate](https://github.com/mgilangjanuar/line-chatbot-boilerplate) | Python | 機器人開發範本 | [mgilangjanuar](https://github.com/mgilangjanuar) | MIT | [![GitHub stars](https://img.shields.io/github/stars/mgilangjanuar/line-chatbot-boilerplate.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/mgilangjanuar/line-chatbot-boilerplate) |
| [LINESimulator](https://github.com/kenakamu/linesimulator) | N/A | 用於除錯機器人的 LINE 模擬器 | [kenakamu](https://github.com/kenakamu) | MIT | [![GitHub stars](https://img.shields.io/github/stars/kenakamu/linesimulator.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/kenakamu/linesimulator) |
| [line-richmenus-manager](https://github.com/kenakamu/line-richmenus-manager) | N/A | 用於建立與管理圖文選單（rich menu）的 GUI 工具 | [kenakamu](https://github.com/kenakamu) | MIT | [![GitHub stars](https://img.shields.io/github/stars/kenakamu/line-richmenus-manager.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/kenakamu/line-richmenus-manager) |
| [linebot](https://github.com/boybundit/linebot) | Node.js | 供 Node.js 使用的 LINE Messaging API SDK | [boybundit](https://github.com/boybundit) | MIT | [![GitHub stars](https://img.shields.io/github/stars/boybundit/linebot.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/boybundit/linebot) |
| [botbuilder-linebot-connector](https://github.com/Wolke/botbuilder-linebot-connector) | Node.js | 供 LINE Messaging API 使用的 Microsoft Bot Framework v3 連接器 | [Wolke](https://github.com/Wolke) | MIT | [![GitHub stars](https://img.shields.io/github/stars/Wolke/botbuilder-linebot-connector.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/Wolke/botbuilder-linebot-connector) |
| [bottender](https://github.com/Yoctol/bottender) | Node.js | 讓你能快速建立可在多個平台上執行之機器人的框架 | [Yoctol](https://github.com/Yoctol) | MIT | [![GitHub stars](https://img.shields.io/github/stars/Yoctol/bottender.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/Yoctol/bottender) |
| [messaging-api-line](https://github.com/bottenderjs/messaging-apis/tree/master/packages/messaging-api-line) | Node.js | 供 Node.js 使用的 LINE Messaging API SDK | [Yoctol](https://github.com/Yoctol) | MIT | [![GitHub stars](https://img.shields.io/github/stars/Yoctol/messaging-apis.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/bottenderjs/messaging-apis/tree/master/packages/messaging-api-line) |
| [line-bot-sdk-dotnet](https://github.com/dlemstra/line-bot-sdk-dotnet) | C# | 供 .NET Standard 使用的 LINE Messaging API SDK | [dlemstra](https://github.com/dlemstra) | Apache-2.0 | [![GitHub stars](https://img.shields.io/github/stars/dlemstra/line-bot-sdk-dotnet.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/dlemstra/line-bot-sdk-dotnet) |
| [LineMessagingApi](https://github.com/pierre3/LineMessagingApi) | C# | 供 C# 使用的 LINE Messaging API SDK | [pierre3](https://github.com/pierre3) | MIT | [![GitHub stars](https://img.shields.io/github/stars/pierre3/LineMessagingApi.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/pierre3/LineMessagingApi) |
| [line-bot-sdk](https://github.com/moleike/line-bot-sdk) | Haskell | 供 Haskell 使用的 LINE Messaging API SDK | [moleike](https://github.com/moleike) | BSD | [![GitHub stars](https://img.shields.io/github/stars/moleike/line-bot-sdk.svg){:zoom="false" .mb-0-important .w-max-inherit}](https://github.com/moleike/line-bot-sdk) |
