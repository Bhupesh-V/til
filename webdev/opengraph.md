# I learned about Open Graph protocol
<!-- 18 Jun 2019 -->
### What it does ?
- [Open Graph](http://ogp.me/) Makes your website into rich "graph" objects.
- Now, what I understand from it is that it provides us to add
  additional metadata to your website which makes it more **rich** on social media.
  For e.g you see the thumbnails of links in the Telegram - *courtesy of OpenGraph*

### How ?
Information is added into the `<head>` tags.
For e.g below is the metadata of one of my [blogs](https://bhupeshv.me/30-Seconds-of-C++/)

```html
<meta property="og:description" content="A collection of C++ STL features (functions/libraries) which can be learned in 30 seconds or less" />
<meta property="og:title" content="30 Seconds of C++" />
<meta property="og:url" content="/30-Seconds-of-C++/" />
<meta property="og:image" content="/images/blog5.png"/>
```

### Sidenotes
Socila Media platforms like Twitter, LinkedIn, Telegram heavily use this meta info to render links, display images etc.