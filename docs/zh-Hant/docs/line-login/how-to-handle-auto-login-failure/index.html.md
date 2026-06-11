# 如何處理自動登入失敗（How to handle auto login failure）

## Overview 

對於已整合 LINE Login 的網頁應用程式而言，當啟用私密瀏覽時，[自動登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#line-auto-login)可能會失敗。此外，視使用者作業系統（OS）的規格而定，自動登入也可能會失敗。

- [當 LINE 應用程式上的自動登入失敗時](https://developers.line.biz/en/docs/line-login/how-to-handle-auto-login-failure/#case-auto-login-on-line-app-fails)
- [當 Universal Links 或 App Links 無法運作，導致 LINE 應用程式無法啟動時](https://developers.line.biz/en/docs/line-login/how-to-handle-auto-login-failure/#case-line-app-will-not-launch)

## When auto login on the LINE app fails 

當啟用私密瀏覽時，LINE 應用程式上的自動登入可能會失敗。即使登入失敗，使用者仍會被重新導向至帶有 `code` 和 `state` 參數的回呼網址（callback URL）。

在這種情況下，`code` 參數會是無效的值，因此你無法核發存取權杖（access token）。此外，`state` 參數也不會與該登入工作階段所關聯的值相符。

![](https://developers.line.biz/media/line-login/handle-auto-login-failure/auto-login-failure-case-1-en.png)

本節說明如何偵測自動登入失敗，並提供登入失敗時應向使用者顯示的回應範例。

### Detecting auto login failure 

你可以使用 [Authenticating users and making authorization requests](https://developers.line.biz/en/docs/line-login/integrate-line-login/#making-an-authorization-request) 中說明的 `state` 參數來偵測自動登入失敗。

當 LINE 應用程式上的登入失敗時，會導致提供給回呼網址的 `state` 參數值與授權網址（authorization URL）中所設定的 `state` 參數值不一致。你的網頁應用程式設計應考量到：當 `state` 參數的值不一致時，即代表自動登入失敗。

<!-- tip start -->

**「state」參數不一致的情況**

在 LINE Login 中，`state` 參數不一致可能是因為第三方的攻擊所造成，例如[跨站請求偽造（Cross site request forgery，CSRF）](https://datatracker.ietf.org/doc/html/rfc6749#section-10.12)。因此，無法判斷 `state` 參數不一致的原因究竟是自動登入失敗，還是諸如 CSRF 等第三方的攻擊。

所以，當發生 `state` 參數不一致時，請考量如何處理使用者非預期地自動登入失敗的情況。

<!-- tip end -->

### When auto login fails 

在自動登入會失敗的環境中，如果讓 LINE Login 失敗的使用者再次使用啟用自動登入的授權網址重試，使用者將會持續反覆地在 LINE Login 上失敗。為了避免持續登入失敗，一旦自動登入失敗，你可以使用 `disable_auto_login` 參數，提示使用者改用已停用自動登入的授權網址重新嘗試 LINE Login。

以下是兩種建議的回應方式。

- [向使用者顯示錯誤訊息並提示其重新嘗試登入](https://developers.line.biz/en/docs/line-login/how-to-handle-auto-login-failure/#recommended-to-log-in-again)
- [將使用者重新導向至未啟用自動登入的授權網址](https://developers.line.biz/en/docs/line-login/how-to-handle-auto-login-failure/#redirect-to-authorization-url)

#### Display an error message to users and prompt them to reattempt login 

向使用者顯示登入失敗訊息，並提示其重新嘗試登入。

由於這個畫面是[在自動登入失敗時](https://developers.line.biz/en/docs/line-login/how-to-handle-auto-login-failure/#when-automatic-login-fails)顯示的，因此在提示使用者重新嘗試登入時，你需要停用自動登入。若要停用自動登入，請在授權網址的查詢參數中將 `disable_auto_login` 參數設為 `true`，並如下所示重新導向使用者。

<pre class="language-text">
<code>https://access.line.me/oauth2/v2.1/authorize?<b style="color:#06C755;">disable_auto_login=true</b>&response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%3Fkey%3Dvalue&state=12345abcde&scope=profile%20openid&nonce=09876xyz</code>
</pre>

我們建議在這個畫面中加入一個連結，連往 LINE 服務中心的 [I can't automatically log in to a website with LINE](https://help.line.me/line/ios/sp?lang=en&contentId=20020693) 頁面（`https://help.line.me/line/ios/sp?lang=en&contentId=20020693`）。

以下是提示使用者重新嘗試登入的畫面範例。

![向使用者顯示錯誤訊息的畫面範例](https://developers.line.biz/media/line-login/handle-auto-login-failure/auto-login-failure-message-en.png)

#### Redirect users to an authorization URL without auto login 

將自動登入失敗的使用者直接重新導向至已停用自動登入的授權網址。透過直接重新導向使用者，你可以在不讓使用者察覺自動登入已失敗的情況下顯示登入畫面。若要停用自動登入，請在授權網址的查詢參數中將 `disable_auto_login` 參數設為 `true`，並如下所示重新導向使用者。

<pre class="language-text">
<code>https://access.line.me/oauth2/v2.1/authorize?<b style="color:#06C755;">disable_auto_login=true</b>&response_type=code&client_id=1234567890&redirect_uri=https%3A%2F%2Fexample.com%2Fauth%3Fkey%3Dvalue&state=12345abcde&scope=profile%20openid&nonce=09876xyz</code>
</pre>

如果你想要事先讓使用者知道將會發生重新導向，你可以顯示一則重新導向訊息。

以下是顯示重新導向訊息的畫面範例。

![將使用者重新導向至未啟用自動登入的授權網址](https://developers.line.biz/media/line-login/handle-auto-login-failure/auto-login-redirect-to-login-en.png)

## When Universal Links or App Links don't work and the LINE app won't launch 

我們使用 [Universal Links](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content/) 和 [App Links](https://developer.android.com/training/app-links) 功能，在[外部瀏覽器](https://developers.line.biz/en/glossary/#external-browser)上執行自動登入。

Universal Links 或 App Links 在外部瀏覽器或某些應用程式內瀏覽器（in-app browser）中可能無法運作，導致自動登入無法運作。在這種情況下，LINE 應用程式不會啟動，而會在外部瀏覽器或應用程式內瀏覽器上顯示[電子郵件地址登入](https://developers.line.biz/en/docs/line-login/integrate-line-login/#mail-or-qrcode-login)畫面。這可能會視使用者作業系統的規格而發生。由於作業系統的規格並未完全公開，因此 LINE Platform 可能難以避免造成自動登入失敗的條件。

![](https://developers.line.biz/media/line-login/handle-auto-login-failure/auto-login-failure-case-2-en.png)

### Notes on making Universal Links work on iOS 

在以下情況中，Universal Links 可能無法運作：

- 透過 JavaScript 將使用者重新導向至授權網址。
- 使用者自行輸入網址並直接前往授權網址。

藉由留意上述情況，你或許能夠迴避 Universal Links 無法運作的問題。例如，讓使用者點按一個按鈕來前往授權網址並開始登入程序。
