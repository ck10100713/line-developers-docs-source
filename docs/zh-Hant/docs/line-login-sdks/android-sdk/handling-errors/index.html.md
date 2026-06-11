# 處理錯誤（Handling errors）

`LineLoginResult` 物件的 `getResponseCode()` 方法會回傳下列其中一個回應碼。

Response code | Description
-------------- | -------------
SUCCESS | 登入成功。
CANCEL | 因為使用者取消了登入流程，所以登入失敗。
AUTHENTICATION_AGENT_ERROR | 因為使用者在同意畫面上點選了「Cancel」（取消）或「Back」（返回）按鈕，所以登入失敗。
SERVER_ERROR | 因為伺服器端錯誤，所以登入失敗。
NETWORK_ERROR | 因為 SDK 無法連線到 LINE Platform，所以登入失敗。
INTERNAL_ERROR | 因為不明錯誤，所以登入失敗。
