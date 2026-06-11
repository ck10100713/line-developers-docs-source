# 使用 SDK 啟用加好友選項（Enabling the add friend option with the SDK）

當使用者登入您的應用程式時，您可以顯示一個將 LINE 官方帳號加為好友的選項。這稱為**加好友選項（add friend option）**。開發者可以指定要加為好友的 LINE 官方帳號。

在開始進行設定之前，請參閱 LINE Login 文件中的 [Add a LINE Official Account as a friend when logged in (add friend option)](https://developers.line.biz/en/docs/line-login/link-a-bot/)，以了解加好友選項以及下列細節：

- 在 LINE Developers Console 將 LINE 官方帳號與您的頻道（channel）連結
- 傳送至 LINE Platform 的 bot prompt 參數及其行為
- LINE Platform 回傳的好友狀態旗標（friendship status flag）及其意義

本主題說明如何透過 LINE SDK 啟用這些與加好友選項相關的功能：

- [Setting the bot prompt parameter in the login request](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/#bot_prompt)
- [Checking the friendship status between the user and the LINE Official Account](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/#get_friendship)

## Setting the bot prompt parameter in the login request 

下列範例程式碼示範如何在使用 `LoginButton` 元件時設定 `botPrompt` 參數。

```java
...
LoginButton loginButton = rootView.findViewById(R.id.line_login_btn);

loginButton.setAuthenticationParams(new LineAuthenticationParams.Builder()
        .scopes(Arrays.asList(Scope.PROFILE))
        .botPrompt(BotPrompt.normal) // configure it here
        .build()
);
...
```

下列範例程式碼示範如何在使用 `LoginApi.getLoginIntent()` 方法時設定 `botPrompt` 參數。

```java
Intent loginIntent = LineLoginApi.getLoginIntent(
    view.getContext(),
    Constants.CHANNEL_ID,
    new LineAuthenticationParams.Builder()
            .scopes(Arrays.asList(Scope.PROFILE))
            .botPrompt(BotPrompt.normal) // configure it here
            .build());

startActivityForResult(loginIntent, REQUEST_CODE);
```

有關參數值的更多資訊，請參閱 LINE SDK for Android 參考文件中的 [LineAuthenticationParams.BotPrompt](https://developers.line.biz/en/reference/android-sdk/reference/com/linecorp/linesdk/auth/LineAuthenticationParams.BotPrompt.html)。

## Checking the friendship status between the user and the LINE Official Account 

您可以使用下列方法檢查使用者與 LINE 官方帳號之間的好友狀態。

- [Check the `LineLoginResult` object in the login response](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/#use-friendship_status_changed)：此方法會檢查登入期間好友狀態是否有所變更。
- [Use LINE Login to get friendship status](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/link-a-bot/#use-line-login-api)：此方法會取得使用者與 LINE 官方帳號之間的好友狀態。

### Check the `LineLoginResult` object in the login response 

登入成功後，`LineLoginResult` 物件會包含一個布林值，用來表示好友狀態是否有所變更。您可以透過 `getFriendshipStatusChanged()` 方法取得此值。

必須符合下列條件才能取得好友狀態旗標：

- 在登入請求中以 `LineAuthenticationParams` 物件指定了 `botPrompt` 參數。
- 向使用者顯示了含有將您的 LINE 官方帳號加為好友選項的同意畫面。

下列範例程式碼示範如何從 `LineLoginResult` 物件取得好友狀態。

```java
public void onActivityResult(int requestCode, int resultCode, Intent data) {
    ...

    LineLoginResult result = LineLoginApi.getLoginResultFromIntent(data);

    boolean friendshipStatusChanged = result.getFriendshipStatusChanged();

    ...
}
```

有關回傳值的更多資訊，請參閱 LINE SDK for Android 參考文件中的 [getFriendshipStatusChanged()](https://developers.line.biz/en/reference/android-sdk/reference/com/linecorp/linesdk/auth/LineLoginResult.html#getFriendshipStatusChanged())。

### Use LINE Login to get friendship status 

在使用者登入您的應用程式且已回傳存取權杖（access token）後，呼叫 `LineApiClient.getFriendshipStatus()` 方法。

```
boolean isFriendToTheBot = lineApiClient.getFriendshipStatus();
```

有關回傳值的更多資訊，請參閱 LINE SDK for Android 參考文件中的 [getFriendshipStatus()](https://developers.line.biz/en/reference/android-sdk/reference/com/linecorp/linesdk/api/LineApiClient.html#getFriendshipStatus())。
