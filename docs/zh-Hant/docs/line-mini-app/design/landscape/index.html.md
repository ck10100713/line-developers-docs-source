# LINE MINI App 的安全區域（Safe area of LINE MINI App）

為了讓 LINE MINI App 的每一個部分都能完整顯示，即使在有瀏海（notch）的裝置上也是如此，我們建議使用 CSS 將 LINE MINI App 限制在安全區域（safe area）內。
LINE MINI App 同時支援一般模式（normal mode）與橫向模式（landscape mode）。一般模式與橫向模式需要不同的安全區域。

請依下列方式設定 LINE MINI App 頁面的 padding：

<!-- table of contents -->

## For normal mode 

- Bottom: 34px

範例 padding：
```
{
  padding-bottom: 34px;
}
```

![](https://developers.line.biz/media/line-mini-app/mini_design_safearea_normal.png)

## For landscape mode 

- Left and right: 44px
- Bottom: 21px

範例 padding：
```
{
  padding-right: 44px;
  padding-bottom: 21px;
  padding-left: 44px;
}
```

![](https://developers.line.biz/media/line-mini-app/mini_design_safearea_landscape.png)
