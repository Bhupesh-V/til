# `async` & `defer` Attributes
<!-- 21 Jul 2019 -->
Usually javascript files interrupt the parsing of HTML document.
To prevent this 2 special attributes of the `<script>` elements are used.


### `async`

```js
<script async src="script.js">
```
- The async attribute is used to indicate to the browser that the script file can be executed asynchronously.
- Therefore the HTML parser does not need to pause and wait for the JS code to load, it is intead fetched in parallel.
- It is only available for externally located script files.


### `defer`

```js
<script defer src="script.js">
```
- The defer attribute tells the browser to only execute the script file once the HTML document has been fully parsed.
- The js file can be downloaded but it does not executes until the whole HTML is parsed.