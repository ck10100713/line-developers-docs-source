# LIFF plugin（LIFF plugin）

<!-- table of contents -->

## What is LIFF plugin 

LIFF plugin 是用來擴充 LIFF SDK 的功能。使用 LIFF plugin，你可以為 LIFF SDK 加入自己的 API，或變更 LIFF API 的行為。

LIFF plugin 是一個具有特定屬性與特定方法的物件或類別（class）。

## Operating environment of LIFF Plugin 

LIFF plugin 可在 LIFF v2.19.0 以後的版本使用。

## Using a LIFF plugin 

使用 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法來啟用 LIFF plugin。將 LIFF plugin 傳遞給 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法即可啟用該 LIFF plugin。當 LIFF plugin 被啟用時，`liff` 物件會被擴充，並且該 LIFF plugin 的 API 將可供使用。

以下是啟用名為 `GreetPlugin` 的 LIFF plugin，並執行 `liff.$greet.hello()` 方法的範例。

### If the LIFF plugin is a class 

如果 LIFF plugin 是類別（class），你需要將其實例（instance）傳遞給 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法。

```js
class GreetPlugin {
  constructor() {
    this.name = "greet";
  }

  install() {
    return {
      hello: this.hello,
    };
  }

  hello() {
    console.log("Hello, World!");
  }
}

liff.use(new GreetPlugin());

liff.$greet.hello(); // Hello, World!

liff
  .init({
    liffId: "123456-abcedfg", // Use own liffId
  })
  .then(() => {
    // ...
  });
```

### If the LIFF plugin is an object 

```js
const hello = () => {
  console.log("Hello, World!");
};

const greetPlugin = {
  name: "greet",
  install() {
    return {
      hello,
    };
  },
};

liff.use(greetPlugin);

liff.$greet.hello(); // Hello, World!

liff
  .init({
    liffId: "123456-abcedfg", // Use own liffId
  })
  .then(() => {
    // ...
  });
```

如上所示，當 LIFF plugin 被啟用時，會在 `liff` 物件中加入一個屬性，其名稱為 `name` 屬性的值前面加上 `$` 前綴。如此一來，你便能以 `liff.${LIFF plugin 的 name 屬性值}.{屬性名稱}` 與 `liff.${LIFF plugin 的 name 屬性值}.{方法名稱}()` 的格式來使用 LIFF plugin 的 API。

## Creating a LIFF plugin 

你可以建立一個具有 [`name`](https://developers.line.biz/en/docs/liff/liff-plugin/#name) 屬性與 [`install()`](https://developers.line.biz/en/docs/liff/liff-plugin/#install) 方法的物件或類別（class），作為 LIFF plugin。

以下是一個名為 `GreetPlugin` 的 LIFF plugin 範例，它提供 `hello` 方法與 `goodbye()` 方法作為 API。

### If the LIFF plugin is a class 

```js
class GreetPlugin {
  constructor() {
    this.name = "greet";
  }

  install() {
    return {
      hello: this.hello,
      goodbye: this.goodbye,
    };
  }

  hello() {
    console.log("Hello, World!");
  }

  goodbye() {
    console.log("Goodbye, World!");
  }
}

liff.use(new GreetPlugin());

liff.$greet.hello(); // Hello, World!
liff.$greet.goodbye(); // Goodbye, World!
```

### If the LIFF plugin is an object 

```js
const hello = () => {
  console.log("Hello, World!");
};

const goodbye = () => {
  console.log("Goodbye, World!");
};

const greetPlugin = {
  name: "greet",
  install() {
    return {
      hello,
      goodbye,
    };
  },
};

liff.use(greetPlugin);

liff.$greet.hello(); // Hello, World!
liff.$greet.goodbye(); // Goodbye, World!
```

### name propery 

`name` 屬性的值就是 LIFF plugin 的名稱。請將 `name` 屬性指定為字串。

所指定的值將成為 `liff` 物件的屬性名稱，如 `liff.${LIFF plugin 的 name 屬性值}`。

### install() method 

`install()` 方法是一個會執行以下工作的函式：

- [描述 LIFF plugin 的初始化處理](https://developers.line.biz/en/docs/liff/liff-plugin/#describe-initialization-process-for-liff-plugin)
- [定義 LIFF plugin 的 API](https://developers.line.biz/en/docs/liff/liff-plugin/#define-liff-plugin-api)

#### Describing the initialization process of the LIFF plugin 

當 LIFF plugin 被啟用時，`install()` 方法會由 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法執行。因此，你可以在 `install()` 方法中描述 LIFF plugin 的初始化處理。

#### Defining the API of the LIFF plugin 

LIFF plugin 的 API 是以 `install()` 方法的回傳值來定義。你可以透過回傳一個物件來定義多個 API。

如果 LIFF plugin 只有一個 API，也可以將該 API 直接作為回傳值。以下是 `install()` 方法回傳一個函式（而非物件）的範例。

```js
class GreetPlugin {
  constructor() {
    this.name = "greet";
  }

  install() {
    return this.hello;
  }

  hello() {
    console.log("Hello, World!");
  }
}

liff.use(new GreetPlugin());

liff.$greet(); // Hello, World!
```

#### Arguments of the `install()` method 

`install()` 方法的第一個引數為 [`context`](https://developers.line.biz/en/docs/liff/liff-plugin/#context) 物件，第二個引數為 [`option`](https://developers.line.biz/en/docs/liff/liff-plugin/#option)。

```js
class GreetPlugin {
  constructor() {
    this.name = "greet";
  }

  install(context, option) {}
}
```

##### `context` object 

`install()` 方法的第一個引數。`context` 物件具有以下兩個屬性：

| Property | Value |
| --- | --- |
| `liff` | `liff` 物件 |
| `hooks` | 提供[在 hook 上註冊回呼（callback）](https://developers.line.biz/en/docs/liff/liff-plugin/#register-callback-with-hook)之方法的物件 |

##### `option` 

`install()` 方法的第二個引數。會傳入 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法第二個引數所指定的值。如果未指定 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法的第二個引數，則 `option` 的值會是 `undefined`。

你可以利用 `option`，透過將引數傳遞給 [`liff.use()`](https://developers.line.biz/en/reference/liff/#use) 方法來自訂 LIFF plugin 的行為。

## About hook 

Hook 是 LIFF plugin 中的一種機制，可讓事先註冊的回呼（callback）在 LIFF API 處理過程中的特定時機執行。你可以將 hook 視同 JavaScript 中的事件處理。如果某個回呼已註冊在某個 hook 上，當該 hook 觸發時，該回呼就會被執行。

除了使用 LIFF API 所提供的 hook 之外，LIFF plugin 也可以提供自己的 hook。

### Hooks for LIFF API 

目前，LIFF API 僅針對 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法提供 hook。

<table>
  <thead>
    <tr>
      <th>LIFF API</th>
      <th>Hook</th>
      <th>Hook type</th>
      <th>When the hook fires</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2"><code>liff.init()</code>方法</td>
      <td><code>before</code> hook</td>
      <td><a href="#async-hook">async hook</a></td>
      <td>呼叫 <code>liff.init()</code> 之後立即觸發（在 LIFF app 初始化之前）</td>
    </tr>
    <tr>
      <td><code>after</code> hook</td>
      <td><a href="#async-hook">async hook</a></td>
      <td>呼叫 <code>successCallback</code> 之前立即觸發（在 LIFF app 初始化之後）</td>
    </tr>
  </tbody>
</table>

### Hook types 

Hook 有兩種類型：[sync hook](https://developers.line.biz/en/docs/liff/liff-plugin/#sync-hook) 與 [async hook](https://developers.line.biz/en/docs/liff/liff-plugin/#async-hook)。

#### Sync hook 

Sync hook 會以同步方式處理已註冊的回呼。已註冊的回呼會依照註冊的順序處理。已註冊回呼的回傳值會被忽略。

#### Async hook 

Async hook 會以非同步方式處理已註冊的回呼。已註冊的回呼會使用 `Promise.all()` 方法平行處理。已註冊回呼的回傳值必須是 `Promise` 物件。

### Registering a callback on a hook 

要在 hook 上註冊回呼，請使用 [`install()`](https://developers.line.biz/en/docs/liff/liff-plugin/#install) 方法的 [`context.hooks`](https://developers.line.biz/en/docs/liff/liff-plugin/#context) 屬性。

以下是在 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法的 `before` hook 與 `after` hook 上註冊回呼的範例。當 [`liff.init()`](https://developers.line.biz/en/reference/liff/#initialize-liff-app) 方法被執行時，`before` hook 與 `after` hook 會觸發，已註冊的回呼便會被執行。

請注意，`before` hook 與 `after` hook 都是 async hook，因此已註冊的回呼必須回傳一個 `Promise` 物件。

```js
class GreetPlugin {
  constructor() {
    this.name = "greet";
  }

  install(context) {
    context.hooks.init.before(this.initBefore);
    context.hooks.init.after(this.initAfter);
    return {
      hello: this.hello,
      goodbye: this.goodbye,
    };
  }

  hello() {
    console.log("Hello, World!");
  }

  goodbye() {
    console.log("Goodbye, World!");
  }

  initBefore() {
    console.log("before hook is called");
    return Promise.resolve();
  }

  initAfter() {
    console.log("after hook is called");
    return Promise.resolve();
  }
}

liff.use(new GreetPlugin());

liff
  .init({
    liffId: "123456-abcedfg", // Use own liffId
  })
  .then(() => {
    // ...
  });
```

### Creating a hook 

你可以建立 `SyncHook` 類別或 `AsyncHook` 類別的實例，作為 hook。

| Hook type                            | Class       |
| ------------------------------------ | ----------- |
| <a href="#sync-hook">sync hook</a>   | `SyncHook`  |
| <a href="#async-hook">async hook</a> | `AsyncHook` |

以下是建立名為 `helloBefore` 與 `helloAfter` 之 hook 的範例。請注意，你需要從 `@liff/hooks` 套件匯入 `SyncHook` 類別與 `AsyncHook` 類別。

要觸發所建立的 hook，請執行 `SyncHook` 類別與 `AsyncHook` 類別之實例的 [`call()`](https://developers.line.biz/en/docs/liff/liff-plugin/#call) 方法。

```js
import { SyncHook, AsyncHook } from "@liff/hooks";

class GreetPlugin {
  constructor() {
    this.name = "greet";
    this.hooks = {
      helloBefore: new SyncHook(),
      helloAfter: new AsyncHook(),
    };
  }

  install(context) {
    return {
      hello: this.hello.bind(this),
      goodbye: this.goodbye,
    };
  }

  hello() {
    this.hooks.helloBefore.call();
    console.log("Hello, World!");
    this.hooks.helloAfter.call();
  }

  goodbye() {
    console.log("Goodbye, World!");
  }
}
```

所建立的 hook 可供其他 LIFF plugin 用來註冊回呼。以下是在名為 `GreetPlugin` 的 LIFF plugin 之 `helloBefore` hook 與 `helloAfter` hook 上註冊回呼的範例。

```js
import { SyncHook, AsyncHook } from "@liff/hooks";

class GreetPlugin {
  constructor() {
    this.name = "greet";
    this.hooks = {
      helloBefore: new SyncHook(),
      helloAfter: new AsyncHook(),
    };
  }

  install(context) {
    return {
      hello: this.hello.bind(this),
      goodbye: this.goodbye,
    };
  }

  hello() {
    this.hooks.helloBefore.call();
    console.log("Hello, World!");
    this.hooks.helloAfter.call();
  }

  goodbye() {
    console.log("Goodbye, World!");
  }
}

class OtherPlugin {
  constructor() {
    this.name = "other";
  }

  install(context) {
    context.hooks.$greet.helloBefore(this.greetBefore);
    context.hooks.$greet.helloAfter(this.greetAfter);
  }

  greetBefore() {
    console.log("helloBefore hook is called");
  }

  greetAfter() {
    console.log("helloAfter hook is called");
    return Promise.resolve();
  }
}

liff.use(new GreetPlugin());
liff.use(new OtherPlugin());
liff.$greet.hello();
// helloBefore hook is called
// Hello, World!
// helloAfter hook is called
```

#### `call()` method 

`call()` 方法是一個用來觸發 hook 的函式。你可以傳遞任意數量的引數給 `call()` 方法。傳遞給 `call()` 方法的引數，可由註冊在該 hook 上的回呼作為引數接收。

以下是將引數傳遞給 hook 的 `call()` 方法，並讓回呼接收這些引數的範例。

```js
import { SyncHook, AsyncHook } from "@liff/hooks";

class GreetPlugin {
  constructor() {
    this.name = "greet";
    this.hooks = {
      helloBefore: new SyncHook(),
      helloAfter: new AsyncHook(),
    };
  }

  install(context) {
    return {
      hello: this.hello.bind(this),
      goodbye: this.goodbye,
    };
  }

  hello() {
    this.hooks.helloBefore.call("foo");
    console.log("Hello, World!");
    this.hooks.helloAfter.call("foo", 0);
  }

  goodbye() {
    console.log("Goodbye, World!");
  }
}

class OtherPlugin {
  constructor() {
    this.name = "other";
  }

  install(context) {
    context.hooks.$greet.helloBefore(this.greetBefore);
    context.hooks.$greet.helloAfter(this.greetAfter);
  }

  greetBefore(foo) {
    console.log(foo); // foo
  }

  greetAfter(foo, bar) {
    console.log(foo, bar); // foo 0
    return Promise.resolve();
  }
}

liff.use(new GreetPlugin());
liff.use(new OtherPlugin());
liff.$greet.hello(); // Hello, World!
```

## Official LIFF plugins 

我們提供以下官方 LIFF plugin：

- [LIFF Inspector](https://developers.line.biz/en/docs/liff/liff-plugin/#liff-inspector)
- [LIFF Mock](https://developers.line.biz/en/docs/liff/liff-plugin/#liff-mock)

### LIFF Inspector 

LIFF Inspector 是用來對你的 LIFF app 進行除錯的 LIFF plugin。使用 LIFF Inspector，你可以在與執行 LIFF app 的裝置不同的另一台電腦上，透過 [Chrome DevTools](https://developer.chrome.com/docs/devtools/) 對你的 LIFF app 進行除錯。

關於 LIFF Inspector 的更多資訊，請參閱 GitHub 上的 [README](https://github.com/line/liff-inspector/blob/main/README.md)，或 [npm](https://www.npmjs.com/package/@line/liff-inspector) 上的 **Readme** 分頁。

- [GitHub](https://github.com/line/liff-inspector)
- [npm](https://www.npmjs.com/package/@line/liff-inspector)

### LIFF Mock 

LIFF Mock 是讓你能輕鬆測試 LIFF app 的 LIFF plugin。使用 LIFF Mock，你可以為 LIFF SDK 加入 mock 模式。在 mock 模式下，你的 LIFF app 不依賴 LIFF 伺服器，且 LIFF API 會回傳 mock 資料。因此，你可以更輕鬆地進行單元測試或負載測試。

關於 LIFF Mock 的更多資訊，請參閱 GitHub 上的 [README](https://github.com/line/liff-mock/blob/main/README.md)，或 [npm](https://www.npmjs.com/package/@line/liff-mock) 上的 **Readme** 分頁。

- [GitHub](https://github.com/line/liff-mock)
- [npm](https://www.npmjs.com/package/@line/liff-mock)
