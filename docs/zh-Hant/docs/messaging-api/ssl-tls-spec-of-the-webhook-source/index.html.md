# Webhook 來源的 SSL/TLS 規格

當機器人伺服器接收從 LINE Platform 傳送的 Webhook 事件時，必須使用 HTTPS 通訊。請使用由公開憑證頒發機構（public certification authority）所核發的 SSL/TLS 憑證來進行 HTTPS 通訊。您可以購買 SSL 憑證，或使用免費憑證，例如 [Let's Encrypt](https://letsencrypt.org/)。

接收 Webhook 的機器人伺服器必須支援符合下列規格的 HTTPS 通訊：

<!-- table of contents -->

## Supported cipher suites 

狀態為 [Deprecated](https://developers.line.biz/en/glossary/#deprecated)（已淘汰）的加密套件（cipher suite）為了相容性而保留，但在不久的將來可能會在不另行通知的情況下停止支援。此外，支援的 SSL/TLS 協定版本與 HTTP 版本會依加密套件而有所不同。

<!-- tip start -->

**表格可以向左或向右捲動**

將表格向右捲動，即可查看各個加密套件的狀態、支援的 SSL/TLS 協定版本，以及支援的 HTTP 版本。

<!-- tip end -->

| IANA | OpenSSL | Hex code | 狀態 | 支援的 SSL/TLS 協定版本 | 支援的 HTTP 版本 |
| --- | --- | --- | --- | --- | --- |
| TLS_AES_256_GCM_SHA384 | TLS_AES_256_GCM_SHA384 | 0x13, 0x02 |  | TLS 1.3 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_CHACHA20_POLY1305_SHA256 | TLS_CHACHA20_POLY1305_SHA256 | 0x13, 0x03 |  | TLS 1.3 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_AES_128_GCM_SHA256 | TLS_AES_128_GCM_SHA256 | 0x13, 0x01 |  | TLS 1.3 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 | ECDHE-ECDSA-AES128-GCM-SHA256 | 0xc0, 0x2b |  | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 | ECDHE-RSA-AES128-GCM-SHA256 | 0xc0,0x2f |  | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 | ECDHE-ECDSA-AES256-GCM-SHA384 | 0xc0, 0x2c |  | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 | ECDHE-RSA-AES256-GCM-SHA384 | 0xc0, 0x30 |  | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 | ECDHE-ECDSA-CHACHA20-POLY1305 | 0xcc, 0xa9 |  | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 | ECDHE-RSA-CHACHA20-POLY1305 | 0xcc, 0xa8 |  | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li><li>HTTP/2</li></ul> |
| TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA | ECDHE-RSA-AES128-SHA | 0xc0, 0x13 | Deprecated | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li></ul> |
| TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA | ECDHE-RSA-AES256-SHA | 0xc0, 0x14 | Deprecated | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li></ul> |
| TLS_RSA_WITH_AES_128_GCM_SHA256 | AES128-GCM-SHA256 | 0x00, 0x9c | Deprecated | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li></ul> |
| TLS_RSA_WITH_AES_128_CBC_SHA | AES128-SHA | 0x00, 0x2f | Deprecated | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li></ul> |
| TLS_RSA_WITH_AES_256_CBC_SHA | AES256-SHA | 0x00, 0x35 | Deprecated | TLS 1.2 | <ul><li>HTTP/1.0</li><li>HTTP/1.1</li></ul> |

## Supported SSL/TLS protocol versions 

支援的協定版本會依加密套件而有所不同。詳情請參閱 [Supported cipher suites](https://developers.line.biz/en/docs/messaging-api/ssl-tls-spec-of-the-webhook-source/#cipher-suites) 中的「支援的 SSL/TLS 協定版本」欄位。

| 協定版本 | 是否支援 |
| ---------------- | --------- |
| TLS 1.3          | ✅        |
| TLS 1.2          | ✅        |
| TLS 1.1 或更低版本 | ❌        |

## Supported HTTP versions 

支援的 HTTP 版本會依加密套件而有所不同。詳情請參閱 [Supported cipher suites](https://developers.line.biz/en/docs/messaging-api/ssl-tls-spec-of-the-webhook-source/#cipher-suites) 中的「支援的 HTTP 版本」欄位。

| HTTP 版本 | 是否支援 |
| ------------ | --------- |
| HTTP/2       | ✅        |
| HTTP/1.1     | ✅        |
| HTTP/1.0     | ✅        |
