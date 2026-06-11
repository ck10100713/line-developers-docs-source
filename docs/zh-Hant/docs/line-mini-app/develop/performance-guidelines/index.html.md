# 效能指南（Performance guidelines）

為了向使用者提供最佳的 LINE MINI App 體驗，請將 LINE MINI App 的效能納入考量。

關於 HTML5 效能重要性的良好參考資料 [Why does speed matter?](https://web.dev/learn/performance/why-speed-matters)，可在 web.dev 上找到。

在測量效能方面，我們建議使用 Google 提供的效能測量工具，例如 [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) 和 [PageSpeed Insights](https://pagespeed.web.dev/)。

LY Corporation 建議達到以下分數。

Performance measurement tool | Score
-|-
[Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) | Performance: 50 and above

<!-- note start -->

**注意**

- 測量時請勿執行 LINE Login。當同時執行 LINE Login 時，所測量的會是 LINE Login 頁面的效能，導致無法測量到 LINE MINI App 本身的效能。
- 請務必在正式環境（實際環境）中測量。請注意，網路環境可能會影響效能分數。

<!-- note end -->
