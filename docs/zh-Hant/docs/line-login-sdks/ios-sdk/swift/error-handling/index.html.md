# 處理錯誤（Handling errors）

## Overview 

SDK 會處理可能發生的錯誤，並提供適當的資訊，讓你能在最終產品中妥善處理這些錯誤。

LINE SDK for iOS Swift 中所有的方法都會回傳一個 `Result` 列舉作為其回應。當回應包含 `.failure` 案例時，你可以取得相關聯的錯誤，如下所示：

```swift
API.getProfile { result in
    switch result {
    case .success(let profile):
        print(profile.displayName)
    case .failure(let error):
        print(error)
        // Handle the error
    }
}
```

上面的範例程式碼只是單純地將錯誤列印出來。記錄中列印出的錯誤會以人類可讀的語句描述錯誤的成因。利用這些資訊，你可以決定如何處理個別的錯誤案例。

## Error types and error reasons 

LINE SDK for iOS Swift 回報的任何錯誤都是一個 `LineSDKError` 實體，它是一個符合 `Swift.Error` 協定的列舉。其成員代表一個原因類別，用以指出錯誤在哪個階段、因什麼原因而發生。目前共定義了四種錯誤原因類別：

- `.requestFailed(reason: RequestErrorReason)`：在建立 API 請求時發生錯誤。可能是因為參數無效或缺少存取權杖（access token）。
- `.responseFailed(reason: ResponseErrorReason)`：在收到伺服器回應後發生錯誤。可能是因為回應不正確或網路錯誤。
- `.authorizeFailed(reason: AuthorizeErrorReason)`：在授權流程中發生錯誤。例如使用者取消了流程，或 ID 權杖（ID token）驗證失敗。
- `.generalError(reason: GeneralErrorReason)`：其他一般性的錯誤成因，例如資料與字串之間的轉換失敗，或參數不符合前置條件。

每個錯誤類別都關聯到一個詳細的原因，而這個原因同樣是一個列舉。這些列舉包含帶有必要資訊的原因成員，或來自系統的底層 `Error` 實體。

若想了解一個原因看起來是什麼樣子，請參考下方 `ResponseErrorReason` 列舉的片段：

```swift
public enum ResponseErrorReason {
    // Error happens in the underlying `URLSession`. Code 2001.
    case URLSessionError(Error)
    // The response is not a valid `HTTPURLResponse`. Code 2002.
    case nonHTTPURLResponse
    // Cannot parse received data to an instance of target type. Code 2003.
    case dataParsingFailed(Any.Type, Data, Error)
    // Received response contains an invalid HTTP status code. Code 2004.
    case invalidHTTPStatusAPIError(detail: APIErrorDetail)
}
```

<!-- note start -->

**Note**

這只是為了示範用途。你的最終程式碼可能與上面不同。

<!-- note end -->

## Getting error data 

若要從最上層的 `LineSDKError` 實體中找出關於錯誤的細節，你可以使用 Swift 的模式比對（pattern matching），並從錯誤中擷取相關聯的資料。例如，你可以檢查某個錯誤是否來自伺服器回傳的無效 HTTP 狀態碼：

```swift
case .failure(let error):
    if case .responseFailed(
        reason: .invalidHTTPStatusAPIError(let detail)) = error
    {
        print("HTTP Status Code: \(detail.code)")
        print("API Error Detail: \(detail.error?.detail ?? "nil")")
        print("Raw Response: \(detail.raw)")
    }
```

根據錯誤類型及其成因，你可以決定如何處理該錯誤。例如，如果發生 `.invalidHTTPStatusAPIError`，你可以檢查其 `detail` 參數的 `code` 屬性。如果錯誤碼為 `500`，表示這是伺服器錯誤，除了顯示彈出訊息之外，你可能無能為力。然而，如果錯誤碼為 `403`，則表示你目前的權杖權限不足，無法存取目標 API 端點（endpoint）。在這種情況下，你可以提示使用者重新登入，並授予你的 app 所需的權限以存取目標端點。

下方的程式碼示範如何處理上述說明的錯誤：

```swift
case .failure(let error):
    if case .responseFailed(
        reason: .invalidHTTPStatusAPIError(let detail)) = error
    {
        if detail.code == 500 {
            print("LINE API Server Error: \(String(describing: detail.error)")
        } else if detail.code == 403 {
            print("Not enough permission. Login again with required permissions?")
            // Do Login
        }
    }
```

## Using shortcuts to handle common errors 

在使用 LINE SDK for iOS Swift 時，可能會發生許多常見的錯誤。有幾種捷徑可以快速辨識這些錯誤。你可以使用這些捷徑來減少對回傳錯誤進行模式比對的工作：

```swift
case .failure(let error):
    if error.isUserCancelled {
        // User cancelled the login process himself/herself.

    } else if error.isPermissionError {
        // Equivalent to checking .responseFailed.invalidHTTPStatusAPIError
        // with code 403. Should login again.

    } else if error.isURLSessionTimeOut {
        // Underlying request timeout in URL session. Should try again later.

    } else if error.isRefreshTokenError {
        // User is accessing a public API with expired token, LINE SDK tried to
        // refresh the access token automatically, but failed (due to refresh token)
        // also expired. Should login again.

    } else if /* error.isXYZ other condition */ {
        // You could also extend LineSDKError to make your own shortcuts.

    } else {
        // Any other errors.
        print("\(error)")
    }
```

藉由使用捷徑來處理常見錯誤，你能更輕鬆地將錯誤處理程式碼抽象化。雖然設計簡潔的錯誤處理取決於你的 app 架構，但一個常見且被廣泛接受的做法是避免重複撰寫相同的錯誤處理程式碼。作為一個良好的實務做法，請將所有錯誤處理程式碼放在單一位置。

## Error code and user data 

`LineSDKError` 列舉符合 `CustomNSError` 協定與 `LocalizedError` 協定。每個錯誤原因都有其自己的 `errorCode` 與 `errorUserInfo` 屬性，協助你辨識錯誤類型及額外的細節。

## Conclusion 

錯誤處理並非易事，但這絕對值得你投入一些時間。透過徹底處理錯誤，你可以大幅改善 app 的使用者體驗。

關於可能的錯誤碼及其代表的意義，請參考 LINE SDK for iOS Swift 參考文件中的 [LineSDKError](https://developers.line.biz/en/reference/ios-sdk-swift/Enums/LineSDKError.html)。

隨著 LINE SDK for iOS Swift 持續演進，可能會新增更多錯誤。在升級 SDK 之前，請務必查看 [Release notes for LINE SDK for iOS](https://developers.line.biz/en/docs/line-login-sdks/ios-sdk/release-notes/)，了解是否有任何重大變更，並判斷你是否需要更新你的錯誤處理方法。
