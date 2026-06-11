# 版本管理政策（Versioning policy）

為了將適當的 LIFF SDK 整合到您的 LIFF app 中，請務必了解 LIFF 版本管理政策。

- [The LIFF MAJOR version status](https://developers.line.biz/en/docs/liff/versioning-policy/#version-support-status)
- [The LIFF Versioning policy](https://developers.line.biz/en/docs/liff/versioning-policy/#versioning-policy)
- [The LIFF SDK (sdk.js) update policy](https://developers.line.biz/en/docs/liff/versioning-policy/#update-policy)
- [The LIFF SDK life cycle](https://developers.line.biz/en/docs/liff/versioning-policy/#life-cycle)

<!-- note start -->

**注意**

由於 LIFF SDK 的更新，整合在您 LIFF app 中的 LIFF SDK 可能會被停止提供。使用已停止提供之 LIFF SDK 的 LIFF app 將無法開啟。

如果您會長時間使用該 LIFF app，請定期查看本頁面，並整合適當的 LIFF SDK。

<!-- note end -->

## The LIFF MAJOR version status 

[The LIFF SDK life cycle](https://developers.line.biz/en/docs/liff/versioning-policy/#life-cycle) 是針對各個 MAJOR 版本所指定的。目前支援的 LIFF SDK MAJOR 版本以及各版本的狀態如下：

| LIFF Version<br>(Release date) | Status<br>(Period of current status) | Availability and description |
| --- | --- | --- |
| LIFF v1<br>(June 6, 2018) | End-of-life<br>(October 1, 2021) | ❌ 所有 CDN edge path 與 CDN fixed path 將不經事先通知即被停用，您將無法開啟這些 LIFF app。 |
| LIFF v2<br>(October 16, 2019) | Active<br>(~ Release date of the LIFF v3) | ✅ 此 LIFF SDK 為目前的版本。會頻繁新增功能並改善既有功能。 |
| LIFF v3<br>(TBD) |  |

## The LIFF Versioning policy 

自 LIFF v2.2.0 起，LIFF 的版本編號將遵循 [Semantic Versioning](https://semver.org/)（SemVer，語意化版本）所制定的規則。

SemVer 定義了以下的版本格式：

`MAJOR.MINOR.PATCH`

舉例來說，在 `v1.2.3` 中，`1` 是 MAJOR 版本、`2` 是 MINOR 版本、`3` 是 PATCH 版本。

以下是各個版本所代表的意義：

| Version | Description |
| --- | --- |
| MAJOR | 當公開 API 引入任何向下不相容（backwards incompatible）的變更時，會遞增此版本。<br>例如：v1.1.12 -> **v2.0.0** |
| MINOR | 當公開 API 引入新的、向下相容（backwards compatible）的功能時，會遞增此版本。<br>例如：v1.1.12 -> **v1.2.0** |
| PATCH | 當僅引入向下相容的錯誤修正時，會遞增此版本。錯誤修正定義為修復不正確行為的內部變更。<br>例如：v1.1.12 -> **v1.1.13** |

## LIFF SDK (sdk.js) update policy 

自 LIFF v2.1.13 發布以來，我們準備了以下兩種類型的 CDN path。在[將 LIFF SDK 整合到 LIFF app](https://developers.line.biz/en/docs/liff/developing-liff-apps/#integrating-sdk) 時，請指定符合您用途的 CDN path。

| CDN path | Description |
| --- | --- |
| CDN edge path | 這是僅包含 MAJOR 版本的 CDN path。如果您希望始終使用最新的 LIFF 功能，請使用此 CDN path。只有在新的 MAJOR 版本發布時，您才需要更新您的 URL。<br>例如：https://static.line-scdn.net/liff/edge/**2**/sdk.js |
| CDN fixed path | 這是包含到 PATCH 版本為止的 CDN path。如果您想使用特定版本的 LIFF 功能，請使用此 CDN path。只要您不更新 LIFF app，就可以持續使用所指定的 PATCH 版本。只有在您想導入我們的新功能、安全性更新和錯誤修正時，才需要更新您的 URL。它不會自動更新，也不會受到 LIFF SDK 更新的影響。<br>例如：https://static.line-scdn.net/liff/edge/**versions/2.22.3**/sdk.js |

<!-- note start -->

**您應該使用哪個版本？**

使用 CDN fixed path 的開發者需要自行決定何時更新其 LIFF app。您可以透過頻繁查看 LIFF 文件中的[版本資訊（Release notes）](https://developers.line.biz/en/docs/liff/release-notes/)來評估我們提供的每次更新，並判斷該更新是否適合您。

<!-- note end -->

指定 CDN fixed path 的範例：

```html
<script charset="utf-8" src="https://static.line-scdn.net/liff/edge/versions/2.22.3/sdk.js"></script>
```

<!-- tip start -->

**用於維持向下相容性的 CDN path**

為了保證已建立的 LIFF app 的行為，我們將持續以下列 CDN path 提供 LIFF SDK。

透過此 CDN path 可取得的 LIFF SDK，與透過 CDN edge path 可取得的 LIFF SDK 為相同版本。

用於向下相容性的 CDN path：<br> https://static.line-scdn.net/liff/edge/**2.1**/sdk.js

<!-- tip end -->

<!-- note start -->

**向下相容 CDN path 的停止提供**

用於維持向下相容性的 CDN path 可能會不受 [LIFF SDK 的生命週期排程（Life Cycle Schedule of the LIFF SDK）](https://developers.line.biz/en/docs/liff/versioning-policy/#life-cycle-schedule)影響而被停止提供。

我們建議將您 LIFF app 中所指定的 CDN path 改為 CDN edge path。

一旦政策確定，我們將盡快通知您。

<!-- note end -->

## The LIFF SDK life cycle 

LIFF SDK 的生命週期針對各個 MAJOR 版本定義如下。

當新的 MAJOR 版本發布時，狀態為「Active」。當下一個 MAJOR 版本發布時，目前 MAJOR 版本的狀態會從「active」變更為「maintenance」，經過一段時間後，會變更為「deprecated」，接著變更為「obsolete」。

| Status | Availability and description | Support period |
| --- | --- | --- |
| Active | ✅ 此 LIFF SDK 為目前的版本。會頻繁新增功能並改善既有功能。 | 從此 MAJOR 版本的發布日期，到下一個 MAJOR 版本的發布日期 |
| Maintaining | ✅ 為維持既有功能所需的錯誤修正與安全性改善 | 「Active」期間結束後的 12 個月 |
| Deprecated | ✅ 此 LIFF SDK 將不再更新。 | 「Maintaining」期間結束後的 6 個月 |
| End-of-life | ❌ 停止提供日期之後，所有 CDN edge path 與 CDN fixed path 將不經通知即失效，LIFF app 將無法再使用。 | - |

### The LIFF SDK life cycle schedule 

請熟悉 LIFF SDK 各 MAJOR 版本的生命週期，並做好適當的準備。

| LIFF Version<br>(Release date) | Active period | Maintenance period | Deprecation period | End-of-life date |
| --- | --- | --- | --- | --- |
| LIFF v1<br>(June 6, 2018) | ~ October 15, 2019<br>`✅ LIFF v1` | ~ April 1, 2021<br>` ✅ LIFF v1` | ~ September 30, 2021<br>`✅ LIFF v1` | October 1, 2021<br>`❌ LIFF v1` |
| LIFF v2<br>(October 16, 2019) | ~ Release date of the LIFF v3<br>`✅ LIFF v2` | ~ TBD<br>`✅ LIFF v2` | ~ TBD<br>`✅ LIFF v2` | TBD<br>`❌ LIFF v2` |
| LIFF v3<br>(TBD) |  |  |  |

`✅ LIFF v1`/`❌ LIFF v1`：https://**d.line-scdn.net/liff/1.0**/sdk.js 的可用性

`✅ LIFF v2`/`❌ LIFF v2`：https://static.line-scdn.net/liff/edge/**2**/sdk.js、https://static.line-scdn.net/liff/edge/**versions/2.x.x**/sdk.js 與 https://static.line-scdn.net/liff/edge/**2.1**/sdk.js 的可用性
