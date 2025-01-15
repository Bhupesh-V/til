# Live Editing HTML
<!-- 6 Nov 2019 -->
Yes !, you can live edit webpages by adding the following in the `<html>` tag.

```html
<!DOCTYPE html>
<html contenteditable>
<head>
	<title>Yay! Live Editing</title>
</head>
<body>
	<p>Try Editing Tis</p>
</body>
</html>
```

Setting `contenteditable="true"` will make its content editable.

So what ?
Well you can use this HTML5 feature to make a motepad right into your browser.

```html
data:text/html, <html contenteditable <head ><title>Notepad</title></head><body style="background-color:black;color: white;"></body></html>
```