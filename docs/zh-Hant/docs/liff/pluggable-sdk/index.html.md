# 可插拔 SDK（Pluggable SDK）

<!-- table of contents -->

## What is the pluggable SDK 

可插拔 SDK（pluggable SDK）是一項功能，讓你可以選擇要在 LIFF SDK 中納入哪些 LIFF API。

藉由只納入你的 LIFF app 實際使用的 LIFF API，你可以將 LIFF SDK 的檔案大小縮減至多約 34%。如此一來，便能提升 LIFF app 的顯示速度。

## Use conditions of the pluggable SDK 

可插拔 SDK 僅在 npm 版本的 LIFF v2.22.0 或更新版本中提供。CDN 版本則不支援。如需更多關於使用 npm 套件的資訊，請參閱[Use the npm package](https://developers.line.biz/en/docs/liff/developing-liff-apps/#use-npm-package)。

## How to use the pluggable SDK 

可插拔 SDK 的使用方式如下：

- [Import the liff object](https://developers.line.biz/en/docs/liff/pluggable-sdk/#import-liff-object)
- [Activate the LIFF APIs](https://developers.line.biz/en/docs/liff/pluggable-sdk/#activate-liff-api)

### Import the liff object 

首先，從 `@line/liff/core` 匯入（import）`liff` 物件。

```js
import liff from "@line/liff/core";
```

這個 `liff` 物件只包含以下屬性與方法：

- [`liff.id`](https://developers.line.biz/en/reference/liff/#id) 屬性
- [`liff.ready`](https://developers.line.biz/en/reference/liff/#ready) 屬性
- [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法
- [`liff.getVersion()`](https://developers.line.biz/en/reference/liff/#get-version) 方法
- [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法

若要使用上述以外的 LIFF API，請匯入對應的模組。在以下範例中，分別為 [`liff.getOS()`](https://developers.line.biz/en/reference/liff/#get-os) 方法與 [`liff.getAppLanguage()`](https://developers.line.biz/en/reference/liff/#get-app-language) 方法匯入了對應的模組：

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";
import GetAppLanguage from "@line/liff/get-app-language";
```

如需更多關於各 LIFF API 對應模組的資訊，請參閱 [LIFF API and the corresponding module list](https://developers.line.biz/en/docs/liff/pluggable-sdk/#liff-api-and-module-list)。

### Activate the LIFF APIs 

接著，將匯入的 LIFF API 模組傳遞給 `liff.use()` 方法，以啟用這些 LIFF API。由於 LIFF API 模組是以類別（class）定義的，因此你必須將實例（instance）傳遞給 `liff.use()` 方法。

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";
import GetAppLanguage from "@line/liff/get-app-language";

liff.use(new GetOS());
liff.use(new GetAppLanguage());
```

一旦啟用了這些 LIFF API，你就可以使用它們了。

在以下範例中，已啟用的 `liff.getOS()` 方法與 `liff.getAppLanguage()` 方法可供使用，但未啟用的 `liff.login()` 方法則無法使用：

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";
import GetAppLanguage from "@line/liff/get-app-language";

liff.use(new GetOS());
liff.use(new GetAppLanguage());

liff.init({
  liffId: "123456-abcedfg",
});

liff.getOS(); // Available
liff.getAppLanguage(); // Available
liff.login(); // Not available
```

## Important points about the pluggable SDK 

由於技術上的限制，`liff.use()` 方法應在 `liff.init()` 方法之前執行。在 `liff.init()` 方法之後執行 `liff.use()` 方法並不保證能正常運作。

### Example of correct execution of the liff.use() method 

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";

// The liff.use() method is executed before the liff.init() method
liff.use(new GetOS());

liff.init({
  liffId: "123456-abcedfg",
});
```

### Example of wrong execution of the liff.use() method 

```js
import liff from "@line/liff/core";
import GetOS from "@line/liff/get-os";

liff.init({
  liffId: "123456-abcedfg",
});

// The liff.use() method is executed after the liff.init() method
liff.use(new GetOS());
```

## LIFF API and the corresponding module list 

| LIFF API | Module |
| --- | --- |
| [`liff.getOS()`](https://developers.line.biz/en/reference/liff/#get-os) | `@line/liff/get-os` |
| [`liff.getAppLanguage()`](https://developers.line.biz/en/reference/liff/#get-app-language) | `@line/liff/get-app-language` |
| [`liff.getLanguage()`](https://developers.line.biz/en/reference/liff/#get-language) (deprecated) | `@line/liff/get-language` |
| [`liff.getLineVersion()`](https://developers.line.biz/en/reference/liff/#get-line-version) | `@line/liff/get-line-version` |
| [`liff.getContext()`](https://developers.line.biz/en/reference/liff/#get-context) | `@line/liff/get-context` |
| [`liff.isInClient()`](https://developers.line.biz/en/reference/liff/#is-in-client) | `@line/liff/is-in-client` |
| [`liff.isLoggedIn()`](https://developers.line.biz/en/reference/liff/#is-logged-in) | `@line/liff/is-logged-in` |
| [`liff.isApiAvailable()`](https://developers.line.biz/en/reference/liff/#is-api-available) | `@line/liff/is-api-available` |
| [`liff.login()`](https://developers.line.biz/en/reference/liff/#login) | `@line/liff/login` |
| [`liff.logout()`](https://developers.line.biz/en/reference/liff/#logout) | `@line/liff/logout` |
| [`liff.getAccessToken()`](https://developers.line.biz/en/reference/liff/#get-access-token) | `@line/liff/get-access-token` |
| [`liff.getIDToken()`](https://developers.line.biz/en/reference/liff/#get-id-token) | `@line/liff/get-id-token` |
| [`liff.getDecodedIDToken()`](https://developers.line.biz/en/reference/liff/#get-decoded-id-token) | `@line/liff/get-decoded-id-token` |
| [`liff.permission.getGrantedAll()`](https://developers.line.biz/en/reference/liff/#permission-get-granted-all)<br><br>[`liff.permission.query()`](https://developers.line.biz/en/reference/liff/#permission-query)<br><br>[`liff.permission.requestAll()`](https://developers.line.biz/en/reference/liff/#permission-request-all) | `@line/liff/permission` |
| [`liff.getProfile()`](https://developers.line.biz/en/reference/liff/#get-profile) | `@line/liff/get-profile` |
| [`liff.getFriendship()`](https://developers.line.biz/en/reference/liff/#get-friendship) | `@line/liff/get-friendship` |
| [`liff.openWindow()`](https://developers.line.biz/en/reference/liff/#open-window) | `@line/liff/open-window` |
| [`liff.closeWindow()`](https://developers.line.biz/en/reference/liff/#close-window) | `@line/liff/close-window` |
| [`liff.sendMessages()`](https://developers.line.biz/en/reference/liff/#send-messages) | `@line/liff/send-messages` |
| [`liff.shareTargetPicker()`](https://developers.line.biz/en/reference/liff/#share-target-picker) | `@line/liff/share-target-picker` |
| [`liff.scanCodeV2()`](https://developers.line.biz/en/reference/liff/#scan-code-v2) | `@line/liff/scan-code-v2` |
| [`liff.scanCode()`](https://developers.line.biz/en/reference/liff/#scan-code) (deprecated) | `@line/liff/scan-code` |
| [`liff.permanentLink.createUrlBy()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url-by)<br><br>[`liff.permanentLink.createUrl()`](https://developers.line.biz/en/reference/liff/#permanent-link-create-url)<br><br>[`liff.permanentLink.setExtraQueryParam()`](https://developers.line.biz/en/reference/liff/#permanent-linke-set-extra-query-param) | `@line/liff/permanent-link` |
| [`liff.i18n.setLang()`](https://developers.line.biz/en/reference/liff/#i18n-set-lang) | `@line/liff/i18n` |
| [`liff.createShortcutOnHomeScreen()`](https://developers.line.biz/en/reference/liff/#create-shortcut-on-home-screen) | `@line/liff/create-shortcut-on-home-screen` |
