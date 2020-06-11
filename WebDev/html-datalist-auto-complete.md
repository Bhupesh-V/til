# Auto-complete in plain HTML
<!--21 Dec 2019 -->
You can make a type-ahead/autocomplete like thing in plain HTML
using the `<datalist></datalist>` tag.

## Usage
```html
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
<h1>Type Ahead HTML</h1>
<input list="test" placeholder="Choose an option">
<datalist id="test">
	<option value="C++">
	<option value="Python">
	<option value="Go">
	<option value="JavaScript">
	<option value="HTML">
</datalist>
</body>
</html>
```

Now as you type `G` it will show _Go_ ;)

### Resources
- [tweet by Álvaro Trigo](https://twitter.com/IMAC2/status/1206913760696373253)