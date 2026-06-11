# 使用 LINE SDK 呼叫其他 API 及處理結果（Using LINE SDK for other APIs and result handling）

## Calling LINE APIs with result handling 

LINE SDK for Unity 中每個可能失敗的 API 操作，都會在回呼（callback）中提供一個 `Result` 物件。透過檢查結果值，你可以優雅地同時處理成功與失敗的情況：

```csharp
LineSDK.Instance.Login(scopes, result => {
    result.Match(
        value => {
            Debug.Log("Login OK");
        },
        error => {
            Debug.Log("Login failed, error code: " + error.Code);
        }
    );
});
```

在 `error` 分支中，每個 `Error` 物件都包含一個錯誤碼 `Code`。錯誤碼會因平台而異。詳情請參閱以下頁面：

- [Handling errors for LINE SDK for iOS Swift](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/swift/error-handling/)
- [Handling errors for LINE SDK for Android](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/handling-errors/)
- [Error API reference and definition for Swift](https://developers.line.biz/en/reference/ios-sdk-swift/Enums/LineSDKError.html)
- [Error API reference and definition for Android](https://developers.line.biz/en/reference/android-sdk/reference/com/linecorp/linesdk/LineApiResponseCode.html)

## Getting user profile 

若登入請求是帶著 `profile` scope 送出的，你就可以取得使用者的 LINE 個人檔案資訊。使用者個人檔案包含使用者 ID、顯示名稱、個人檔案媒體（圖片或影片）以及狀態訊息。

如下呼叫 `LineAPI.GetProfile` 方法：

```csharp
LineAPI.GetProfile(result => {
    result.Match(
        value => {
            Debug.Log("User ID: " + value.UserId);
            Debug.Log("User Display Name: " + value.DisplayName);
            Debug.Log("User Status Message: " + value.StatusMessage);
            Debug.Log("User Icon: " + value.PictureUrl);
        },
        error => {
            Debug.Log(error.Message);
        }
    );
});
```

### Logging out users 

你可以將使用者從你的應用程式登出。為了提供更好的使用者體驗，我們建議提供讓使用者登出應用程式的方式。

呼叫 `Logout` 方法即可讓使用者的存取權杖（access token）失效，並將其登出你的應用程式。登出後，使用者必須再次經過登入流程才能登入。

```csharp
LineSDK.Instance.Logout(result => {
    result.Match(
        _ => { /* User logout done. Update UI. */ },
        error => {
            Debug.Log(error.Message);
        }
    );
});
```

### Getting access token 

伺服器端程式碼可以使用存取權杖來呼叫 LINE Login API。詳情請參閱 [LINE Login v2.1 API reference](https://developers.line.biz/en/reference/line-login/)。

如下取得 `LineSDK` 實例的 `CurrentAccessToken` 屬性，即可取得目前的存取權杖：

```csharp
var currentToken = LineSDK.Instance.CurrentAccessToken;
if (currentToken != null) {
    Debug.Log("Current token value: " + currentToken.Value);
}
```

<!-- note start -->

**Note**

將存取權杖傳送至你的伺服器時，我們建議先加密存取權杖，並使用 SSL 傳送加密後的資料。你也應該驗證伺服器所收到的存取權杖與呼叫 LINE Login 時所使用的存取權杖相符，且其頻道 ID（channel ID）與你的頻道（channel）相符。

<!-- note end -->

### Verify and refresh access tokens 

即使 `CurrentAccessToken` 回傳非 null 值，也無法保證該存取權杖有效。存取權杖可能已過期或已被撤銷（revoke）。請使用 `LineAPI.VerifyToken` 來檢查目前的存取權杖是否仍然有效：

```csharp
LineAPI.VerifyAccessToken(result => {
    result.Match(
        value => {
            Debug.Log("Channel Id bound to the token: " + value.ChannelId);
        },
        error => {
            Debug.Log("The token verifying failed: " + error.Message);
        }
    );
});
```

透過 `LineAPI` 發出 API 請求時，LINE SDK 會自動重新整理（refresh）任何已過期的存取權杖。不過，若權杖已過期很長一段時間，重新整理操作就會失敗。在這種情況下會發生錯誤，你需要讓使用者重新登入。

我們建議不要自行重新整理存取權杖。讓 LINE SDK 自動管理存取權杖既更簡單也更安全。不過，你仍可以如下手動重新整理存取權杖：

```csharp
LineAPI.RefreshAccessToken(result => {
    result.Match(
        token => {
            Debug.Log("Token refreshed. New token: " + token.Value);
        },
        error => {
            Debug.Log("Something wrong when refreshing token: " + error.Message);
        }
    );
});
```
