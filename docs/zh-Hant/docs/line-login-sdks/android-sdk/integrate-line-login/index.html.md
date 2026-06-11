# 在你的 Android 應用程式整合 LINE Login（Integrating LINE Login with your Android app）

本主題說明如何將 LINE SDK for Android 整合至你既有的 Android 應用程式，以實作 [LINE Login](https://developers.line.biz/en/docs/line-login/overview/)。若想了解 LINE Login 能做到哪些事，請閱讀 [Trying the sample app](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/try-line-login/) 並試用 LINE Login for Android 範例應用程式。

## Prerequisites 

要建置與使用 LINE SDK for Android，你需要：

- 一個[provider](https://developers.line.biz/en/glossary/#provider) 與一個 LINE Login 頻道（channel）。你可以在 LINE Developers Console 中[同時建立兩者](https://developers.line.biz/console/register/line-login/channel/)。
- 將 `minSdkVersion` 設為 24 或以上（Android 7.0 以後版本）。

<!-- tip start -->

**將 minSdkVersion 設為早於 24（早於 Android 7.0）**

若你想將 `minSdkVersion` 設為早於 24（早於 Android 7.0），請使用較早版本的 LINE SDK for Android。詳情請見 [Releases](https://github.com/line/line-sdk-android/releases)。

<!-- tip end -->

<!-- note start -->

**資源命名衝突**

請勿使用以 `linesdk_` 開頭的資源 ID，因為這可能與 SDK 內的資源產生衝突。

<!-- note end -->

## Upgrading from earlier SDK versions 

如果你是從 LINE SDK v4.x 或更早版本升級，了解目前版本有以下主要差異會有所幫助：

- 開始登入時，你必須指定 [Scopes](https://developers.line.biz/en/docs/line-login/integrate-line-login/#scopes)，以決定你的應用程式可存取哪些使用者資料。
- 如果你在登入時指定 `OPENID_CONNECT` scope，便可取得一組 [ID token](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/managing-users/#get-id-token)，以安全地驗證使用者的身分。

## Add LINE SDK dependency 

要整合 LINE SDK for Android，請依下列步驟將所需的程式庫匯入你的專案，並設定專案的 Android manifest 檔案。

### Import the library into your project 

在你的模組層級 `build.gradle` 檔案中加入 LINE SDK 相依套件。

[![Maven Central](https://img.shields.io/maven-central/v/com.linecorp.linesdk/linesdk.svg?label=Maven%20Central){:zoom="false"}](https://search.maven.org/search?q=g:%22com.linecorp.linesdk%22%20AND%20a:%22linesdk%22)

```groovy
repositories {
   ...
   mavenCentral()
}

dependencies {
    ...
    implementation 'com.linecorp.linesdk:linesdk:latest.release'
    ...
}
```

### Add Android compilation options 

啟用 Java 1.8 支援。在與上述相同的 `build.gradle` 檔案中加入：

```
android {
...
  compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
...
}
```

## Setting the Android manifest file 

要指定你的應用程式需要網際網路存取權限，請在你的 `AndroidManifest.xml` 檔案中加入 `INTERNET` 權限。

```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

<!-- note start -->

**Note**

請確認發起登入呼叫的 activity，其啟動模式（launch mode）並未設為 `singleInstance`，因為這可能會導致該 activity 無法接收 `onActivityResult` callback。

<!-- note end -->

## Linking your app to your channel 

要將你的應用程式連結到 LINE Login 頻道，請在 [LINE Developers Console](https://developers.line.biz/console/) 上你的頻道設定的 **LINE Login** 分頁中啟用 **Mobile app**，並填妥這些欄位。

- **Package names：** 必填。用來啟動 Google Play 商店的應用程式套件名稱。
- **Package signatures：** 選填。你可以輸入多組簽章，每組各佔一行。
- **Android URL scheme：** 選填。用來啟動你的應用程式的自訂 URL scheme。

![Android Package names, Package signatures, and URL scheme settings.](https://developers.line.biz/media/line-login/integrate-login-android/android-app-settings.png)

### Set Package Signatures 

Package signatures 對於強化你的應用程式與 LINE 應用程式之間的驗證互動至關重要。Package signature 有兩種類型：debug package signature 與 release package signature。這些都與 SHA-1 格式的 key hash 相關。

#### Debug package signature 

Debug package signature 是由 Debug 憑證產生的，而該憑證會在你執行或除錯應用程式時由 Android Studio 自動產生。

```bash
# For macOS
keytool -exportcert -alias androiddebugkey -keystore ~/.android/debug.keystore -storepass android -keypass android | openssl sha1

# For Windows
keytool -exportcert -alias androiddebugkey -keystore %USERPROFILE%\.android\debug.keystore -storepass android -keypass android | openssl sha1
```

#### Release package signature 

Release package signature 是由用來將應用程式發布至商店的 Release 憑證所產生。請將 `<RELEASE_KEY_ALIAS>` 與 `<RELEASE_KEY_PATH>` 替換為你實際的 release key alias 與路徑。

```bash
keytool -exportcert -alias <RELEASE_KEY_ALIAS> -keystore <RELEASE_KEY_PATH> | openssl sha1
```

#### Using the Google Play Console to get Release key hash 

如果你使用 [Play App Signing](https://developer.android.com/studio/publish/app-signing?hl=en#app-signing-google-play)，你應使用從 Google Play Console 取得的 SHA-1 憑證指紋，而非在終端機上產生 Release key hash。詳情請見 Play Console 說明中的 [Use Play App Signing](https://support.google.com/googleplay/android-developer/answer/9842756?hl=en)。

在 Google Play Console 中，前往 **Setup** > **App signing**，然後複製 SHA-1 憑證指紋的值。

## Adding the LINE Login button 

要讓使用者登入你的 Android 應用程式，你可以建立一個 LINE 品牌的登入按鈕，帶領使用者完成驗證與授權流程。

加入登入按鈕有 2 種方式：

- [使用 LINE SDK 內建的登入按鈕](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/#use-button)
- [使用自訂的登入按鈕](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/#use-code)

### Use the LINE SDK's built-in login button 

LINE SDK 提供了一個預先定義好的登入按鈕。你可以將登入按鈕加入應用程式的使用者介面，為使用者提供快速登入的方式，如下所示：

1. 在你的版面配置 XML 檔案中加入登入按鈕。

   ```xml
   <com.linecorp.linesdk.widget.LoginButton
       android:id="@+id/line_login_btn"
       android:layout_width="match_parent"
       android:layout_height="wrap_content" />
   ```

1. 在你的 activity 或 fragment 中找到該 view，設定必要的參數，並為其指派一個 listener。

   ```java
   import java.util.Arrays;

   // A delegate for delegating the login result to the internal login handler.
   private LoginDelegate loginDelegate = LoginDelegate.Factory.create();

   LoginButton loginButton = rootView.findViewById(R.id.line_login_btn);

   // if the button is inside a Fragment, this function should be called.
   loginButton.setFragment(this);

   loginButton.setChannelId(channelIdEditText.getText().toString());

   // configure whether login process should be done by Line App, or inside WebView.
   loginButton.enableLineAppAuthentication(true);

   // set up required scopes and nonce.
   loginButton.setAuthenticationParams(new LineAuthenticationParams.Builder()
           .scopes(Arrays.asList(Scope.PROFILE))
           // .nonce("<a randomly-generated string>") // nonce can be used to improve security
           .build()
   );
   loginButton.setLoginDelegate(loginDelegate);
   loginButton.addLoginListener(new LoginListener() {
       @Override
       public void onLoginSuccess(@NonNull LineLoginResult result) {
           Toast.makeText(getContext(), "Login success", Toast.LENGTH_SHORT).show();
       }

       @Override
       public void onLoginFailure(@Nullable LineLoginResult result) {
           Toast.makeText(getContext(), "Login failure", Toast.LENGTH_SHORT).show();
       }
   });
   ```

### Use a customized login button 

除了使用預設的登入按鈕外，你也可以用自己的程式碼自訂使用者介面與登入流程。

#### Download and add the images to your project 

LINE Login 按鈕的圖片組包含了 iOS、Android 與桌面應用程式的圖片。Android 的圖片組包含了多種螢幕密度與按鈕狀態的圖片。在本指南中，我們將使用 Android 資料夾中的 "base" 與 "pressed" 登入按鈕圖片。

1. 下載並解壓縮 [LINE Login button images](https://vos.line-scdn.net/line-developers/docs/media/line-login/login-button/LINE_Login_Button_Image.zip)。
2. 將 "base" 與 "pressed" 登入按鈕圖片加入各螢幕密度對應的 `drawable` 資料夾中。

#### Configure the images 

在使用這些圖片之前，你需要加入想要使用的登入按鈕文字。各語言的建議登入按鈕文字請參見 [LINE Login button design guidelines](https://developers.line.biz/en/docs/line-login/login-button/)。你也需要定義圖片的可拉伸區域，以便在不扭曲 LINE 圖示的情況下加入按鈕文字。

1. 為每張圖片建立 [9-patch files](https://developer.android.com/guide/topics/resources/drawable-resource#NinePatch#NinePatch)，並為登入按鈕文字定義可拉伸區域。
2. 在你的應用程式登入畫面中，以可點擊的 text view 形式加入按鈕，並設定你想要的登入按鈕文字。
3. 在你的 drawable 資料夾中加入 selector XML 檔案，以定義對應於該 text view 狀態的圖片。

## Starting the login activity 

當使用者點擊登入按鈕時，你的應用程式會呼叫 `getLoginIntent()` 取得 login intent 並啟動登入 activity。必須將 context 與頻道 ID 傳入此方法。如果裝置上已安裝 LINE，便會開啟 LINE 執行登入，而不會詢問使用者的 LINE 憑證。如果未安裝 LINE，使用者會被重新導向至瀏覽器中的 LINE Login 畫面，以輸入其 LINE 憑證（電子郵件地址與密碼）。

1. 設定一個 on-click listener，以監聽按鈕何時被點擊。
1. 在 `onClick` callback 中，呼叫 `LineLoginApi` 的 `getLoginIntent()` 方法，以取得用來啟動登入 activity 的 login intent。
1. 透過呼叫 `startActivityForResult()` 並將 login intent 與 request code 作為參數傳入，啟動驗證流程。request code 是一個用來識別此請求的整數。

以下是當使用者點擊登入按鈕時，如何啟動 activity 來讓使用者登入的範例。

```java
private static final int REQUEST_CODE = 1;
...

final TextView loginButton = (TextView) findViewById(R.id.login_button);
loginButton.setOnClickListener(new View.OnClickListener() {

    public void onClick(View view) {
        try {
            // App-to-app login
            Intent loginIntent = LineLoginApi.getLoginIntent(
              view.getContext(),
              Constants.CHANNEL_ID,
              new LineAuthenticationParams.Builder()
                .scopes(Arrays.asList(Scope.PROFILE))
                        // .nonce("<a randomly-generated string>") // nonce can be used to improve security
                .build());
            startActivityForResult(loginIntent, REQUEST_CODE);
        }
        catch(Exception e) {
            Log.e("ERROR", e.toString());
        }
    }
});
```

<!-- note start -->

**Note**

如果你不想使用 app-to-app 登入，而是希望讓使用者透過瀏覽器中的 LINE Login 畫面登入，請使用 `getLoginIntentWithoutLineAppAuth()` 方法。

<!-- note end -->

## Handling the login result 

使用者登入後，登入結果會在 activity 的 `onActivityResult()` 方法中回傳。你的應用程式必須覆寫（override）此方法以處理登入結果。

使用 `LineLoginResult` 物件的 `getResponseCode()` 方法來判斷登入是否成功。如果 `getResponseCode()` 回傳 `SUCCESS`，表示登入成功。任何其他值都表示失敗。請參見 [Handling errors](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/handling-errors/) 以判斷發生了哪種錯誤類型。

以下顯示你的應用程式可如何處理登入結果的範例。

```java
public void onActivityResult(int requestCode, int resultCode, Intent data) {
    super.onActivityResult(requestCode, resultCode, data);
    if (requestCode != REQUEST_CODE) {
        Log.e("ERROR", "Unsupported Request");
        return;
    }

    LineLoginResult result = LineLoginApi.getLoginResultFromIntent(data);

    switch (result.getResponseCode()) {

        case SUCCESS:
            // Login successful
            String accessToken = result.getLineCredential().getAccessToken().getTokenString();

            Intent transitionIntent = new Intent(this, PostLoginActivity.class);
            transitionIntent.putExtra("line_profile", result.getLineProfile());
            transitionIntent.putExtra("line_credential", result.getLineCredential());
            startActivity(transitionIntent);
            break;

        case CANCEL:
            // Login canceled by user
            Log.e("ERROR", "LINE Login Canceled by user.");
            break;

        default:
            // Login canceled due to other error
            Log.e("ERROR", "Login FAILED!");
            Log.e("ERROR", result.getErrorData().toString());
    }
}
```

### Get the access token 

登入結果包含一個 `LineCredential()` 物件，其中含有使用者的存取權杖（access token）。如上述範例所示，你可以使用以下程式碼取得存取權杖。

```java
String accessToken = result.getLineCredential().getAccessToken().getTokenString();
```

### Get user profile immediately after login 

LINE SDK 會在使用者登入時自動取得其個人檔案資訊。使用者的個人檔案資訊包含顯示名稱、使用者 ID、狀態消息，以及個人檔案媒體 URL。透過呼叫 `LineLoginResult` 物件中的 `getLineProfile()` 方法可存取這些資訊。以下取自上述範例的程式碼片段，示範了如何從登入結果取得使用者的個人檔案資訊並將其傳入 intent。

```java
transitionIntent.putExtra("display_name", result.getLineProfile().getDisplayName());
transitionIntent.putExtra("status_message", result.getLineProfile().getStatusMessage());
transitionIntent.putExtra("user_id", result.getLineProfile().getUserId());
transitionIntent.putExtra("picture_url", result.getLineProfile().getPictureUrl().toString());
```

使用者 ID 僅在個別 provider 內具唯一性。同一位 LINE 使用者在不同 provider 中會有不同的使用者 ID。請避免使用使用者 ID 來跨不同 provider 識別使用者。

### Using user data on your server 

<!-- warning start -->

**使用者冒用（User impersonation）**

當 `LineProfile` 物件中的使用者 ID 或其他資訊是由用戶端傳送到你的後端伺服器時，請勿信任這些資訊。惡意的用戶端可能會傳送任意的使用者 ID 或格式錯誤的資訊到你的伺服器，以冒用某個使用者。

正確的做法是，用戶端應將存取權杖傳送給伺服器，再由伺服器使用該權杖來取得使用者資料。

<!-- warning end -->

通常，後端伺服器會根據使用者 ID、顯示名稱或其他某些 LINE 帳號屬性來驗證使用者的身分。但與其直接從用戶端將這些資訊傳送到你的伺服器，用戶端應改為傳送存取權杖。接著伺服器應使用此權杖，向 LINE Platform 的伺服器安全地驗證使用者的身分。

從 [Get the access token](https://developers.line.biz/en/docs/line-login-sdks/android-sdk/integrate-line-login/#get-access-token) 了解更多關於存取權杖的資訊。

在這些頁面了解更多應從你的後端呼叫哪些 API：

- [Verify access token validity](https://developers.line.biz/en/reference/line-login/#verify-access-token)
- [Get user profile](https://developers.line.biz/en/reference/line-login/#get-user-profile)

## Using the `LineApiClient` interface 

透過呼叫 `LineApiClient` 介面的各個方法來使用 SDK。要這麼做，請建立一個 `lineApiClient` 物件的靜態變數並初始化該變數。

1. 建立該物件的靜態變數，以呼叫各種方法。

   ```java
   private static LineApiClient lineApiClient;
   ```

2. 如下所示，在你的 activity 的 `onCreate()` 方法中初始化 `lineApiClient` 變數。初始化時需要頻道 ID 與 context。

   ```java
   LineApiClientBuilder apiClientBuilder = new LineApiClientBuilder(getApplicationContext(), "your channel id here");
   lineApiClient = apiClientBuilder.build();
   ```

<!-- note start -->

**Note**

LINE SDK for Android 中的所有方法都會執行網路操作，如果在主執行緒（main thread）上呼叫，將會造成 `NetworkOnMainThreadExceptions`。為避免此問題，請使用 `AsyncTask` 來呼叫這些方法。

<!-- note end -->
