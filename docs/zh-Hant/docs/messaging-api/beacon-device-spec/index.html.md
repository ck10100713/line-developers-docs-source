# LINE Beacon 裝置規格（LINE Beacon device specification）

本 LINE Beacon 規格適用於希望部署 beacon 裝置以使用 LINE Beacon 的企業用戶。您的 beacon 裝置必須符合本規格。

與 [LINE Simple Beacon](https://github.com/line/line-simple-beacon) 封包不同，LINE Beacon 封包具備 [secure message](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#generating-secure-message) 欄位作為安全機制。

## Requirements for LINE Beacon compliant devices 

符合 LINE Beacon 規格的 beacon 裝置必須支援 Bluetooth® Low Energy Version 4.0 與 Apple 的 [iBeacon](https://developer.apple.com/ibeacon/)，且能夠廣播 LINE Beacon 封包。具體而言，裝置必須符合以下要求：

- 廣播 [LINE Beacon 封包](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#line-beacon-packet)。
- 透過 SHA-256 雜湊與 XOR（互斥或，exclusive OR）運算後的資料產生 [secure message](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#generating-secure-message)。
- 每 15 秒更新一次 secure message。
- 在裝置中寫入並於裝置外殼上標示一組唯一的 [HWID](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#hwid)。

## LINE Beacon packets 

為了讓 LINE 能快速偵測到您的 beacon 裝置，請依照 generic access profile 中所指定的 broadcaster role（BLUETOOTH SPECIFICATION Version 4.0 [Vol 3]，Part C Section 2.2.2.1）來控制 beacon 裝置。

### Packet transmission interval 

我們強烈建議您以 152.5ms 的間隔傳送 LINE Beacon 封包。

### Advertising packet specification 

如下圖所示，請以三個 AD structure 來組成廣播封包。

![LINE Beacon packet](https://developers.line.biz/media/messaging-api/beacon-device-spec/advDataFormat.png)

廣播封包規格如下。value 欄位中的十六進位值等同於 description 欄位中括號內的值。

| Octet | Field | Value | Description |
| --- | --- | --- | --- |
| 00 | Length | 0x02 | 第一個 AD structure 的資料長度（2 bytes） |
| 01 | AD type | 0x01 | 第一個 AD structure 的 AD type（Flags） |
| 02 | AD data | 0x06 | 設定的 flags（LE General Discoverable Mode、BR/EDR Not Supported） |
| 03 | Length | 0x03 | 第二個 AD structure 的資料長度（3 bytes） |
| 04 | AD type | 0x03 | 第二個 AD structure 的 AD type（Complete list of 16-bit UUIDs available） |
| 05 | 16-bit UUID | 0x6F | LINE 的 16-bit UUID，與下一個 byte 合併後為（0xFE6F） |
| 06 | 16-bit UUID | 0xFE | LINE 的 16-bit UUID，與前一個 byte 合併後為（0xFE6F） |
| 07 | Length | 0x11 | 第三個 AD structure 的資料長度（17 bytes） |
| 08 | AD type | 0x16 | 第三個 AD structure 的 AD type（Service Data - 16-bit UUID） |
| 09 | 16-bit UUID | 0x6F | LINE 的 16-bit UUID，與下一個 byte 合併後為（0xFE6F） |
| 10 | 16-bit UUID | 0xFE | LINE 的 16-bit UUID，與前一個 byte 合併後為（0xFE6F） |
| 11 | Frame type | 0x02 | frame type（LINE Beacon） |
| 12-16 | HWID | 裝置特定值 | beacon 裝置的 5-byte 唯一 ID。詳情請參閱 [HWID](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#hwid)。 |
| 17 | Measured TxPower | 裝置特定值 | 安裝 LINE 的裝置與 beacon 裝置相距一公尺時的 RSSI（Received Signal Strength Indicator，接收訊號強度指標）。請設定與 iBeacon 封包相同的值。詳情請參閱 iBeacon 文件。<br />若您不使用 RSSI 資料，請將此欄位設為 0x7F。 |
| 18-21 | Message authentication code | Variable | 用於 [message authentication](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#step-one-generate-message-auth-code) 的 4-byte 代碼 |
| 22-23 | Masked timestamp | Variable | 2-byte 的 [masked timestamp](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#step-two-generate-masked-timestamp) |
| 24 | Battery level | Variable | 剩餘 [battery level](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#battery-level) |
| 25-30 | Non-significant part | 0x00 | 未使用。請將每個 byte 設為 0x00。 |

## Generate a secure message 

LINE 要求您傳送 secure message，以防止 LINE Beacon 封包遭竄改與重放攻擊（replay attack）。secure message 為 7-byte 的資料，包含 message authentication code、masked timestamp 與 battery level。LINE 會將 beacon 裝置傳送的 secure message 傳遞給 LINE Platform 進行驗證。

若要產生 secure message，請依照下圖所示的流程，對以 SHA-256 計算出的雜湊值執行三次 XOR（互斥或，exclusive OR）運算。關於所需參數的詳情，請參閱 [Required parameters for secure messages](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#parameters)。

![Generation algorithm of the secure message](https://developers.line.biz/media/messaging-api/beacon-device-spec/secureMessageAlgorithm.png)

請依照以下說明產生 secure message。

### 1. Generate a message authentication code 

1. 依照下列順序串接這些項目，並以 SHA-256 產生 32-byte 的雜湊值。

   - [Timestamp](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#timestamp)
   - [HWID](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#hwid)
   - [Vendor key](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#vendor-key)
   - [Lot key](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#lot-key)
   - [Battery level](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#battery-level)

1. 對雜湊值的前 16 bytes 與後 16 bytes 執行 XOR 運算。
1. 對上一步驟所計算出的值的前 8 bytes 與後 8 bytes 執行 XOR 運算。
1. 對上一步驟所計算出的值的前 4 bytes 與後 4 bytes 執行 XOR 運算。

如此即可得到 message authentication code。

### 2. Generate a masked timestamp 

從 timestamp 的開頭遮蔽 6 bytes，並保留最後 2 bytes。這就是 masked timestamp。

### 3. Concatenate items 

若要產生 secure message，請依照下列順序串接這些項目：

- 於 [步驟 1](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#step-one-generate-message-auth-code) 產生的 message authentication code
- 於 [步驟 2](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#step-two-generate-masked-timestamp) 產生的 masked timestamp
- [Battery level](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#battery-level)

串接的結果即為 secure message。請參閱 [Sample code and data for generating secure messages](https://developers.line.biz/en/docs/messaging-api/secure-message-sample/)，以針對您的 beacon 裝置開發與測試 secure message 的產生。

### Required parameters for secure messages 

若要產生 secure message，您需要這些參數：

- [Battery level](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#battery-level)
- [HWID](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#hwid)
- [Lot key](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#lot-key)
- [Timestamp](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#timestamp)
- [Vendor key](https://developers.line.biz/en/docs/messaging-api/beacon-device-spec/#vendor-key)

HWID、lot key 與 vendor key 由 LY Corporation 產生並管理。若要取得這些所需參數，請聯絡貴組織的 LY Corporation 代表人。只有在您（企業用戶）提交申請表並取得許可後，才會核發這些所需參數給您。

#### Battery level 

battery level 為剩餘的電池容量。請依照下方指引指定此值：

| Decimal value | Hexadecimal value | Description |
| --- | --- | --- |
| 0 | 0x00 | 未知，或已連接外部電源。 |
| 1 | 0x01 | 剩餘 0%。電池已完全放電。 |
| 2 | 0x02 | 剩餘 10% |
| … | … | … |
| 10 | 0x0A | 剩餘 90% |
| 11 | 0x0B | 100%。電池已充飽。 |
| 12–255 | 0x0C–0xFF | 保留供未來使用。請勿使用。 |

#### HWID 

HWID 是由 LY Corporation 核發的 beacon 裝置硬體 ID。此 ID 為 10 個字元的十六進位字串。請將 HWID 轉換為位元組陣列，並將此位元組陣列以 5-byte 二進位資料寫入 beacon 裝置。此外，也請在 beacon 裝置上標示 HWID。

#### Lot key 

lot key 由 LY Corporation 核發，分配給每個批次（lot）。這些 key 為 16 個字元的字串。與 HWID 相同，請將此 key 轉換為位元組陣列，並將此位元組陣列以 8-byte 二進位資料寫入 beacon 裝置。

#### Timestamp 

timestamp 為一個無號 64-bit 整數。

- 在 beacon 裝置首次開機時開始遞增 timestamp。
- timestamp 從零開始，每 15 秒遞增一次。例如，beacon 開機一分鐘後的 timestamp 為 4。
- 當 beacon 裝置再次開機時，請勿將 timestamp 重設為零。即使關機後重新開機，也請繼續從上次的值遞增 timestamp。
- 當您將 beacon 裝置的 HWID 重新寫入為新核發的 HWID 時，請將 timestamp 重設，從零重新開始。

#### Vendor key 

vendor key 由 LY Corporation 核發，分配給每個供應商（vendor）。此 key 為 8 個字元的十六進位字串。與 HWID 相同，請將此 key 轉換為位元組陣列，並將此位元組陣列以 4-byte 二進位資料寫入 beacon 裝置。

## iBeacon packets 

為了通知 iOS 裝置附近有 LINE Beacon 裝置，您必須傳送 iBeacon 封包。請在 iBeacon 封包中包含這些 LINE Beacon 特定的參數。

| Parameter | Value                                |
| --------- | ------------------------------------ |
| UUID      | D0D2CE24-9EFC-11E5-82C4-1C6A7A17EF38 |
| Major     | 0x4C49                               |
| Minor     | 0x4E45                               |

關於 iBeacon 封包的 AD structure 與傳送間隔的詳情，請參閱 Apple 的 Proximity Beacon Specification 文件。您可以從 [Apple Developer 網站的 iBeacon 章節](https://developer.apple.com/ibeacon/) 下載此文件。
