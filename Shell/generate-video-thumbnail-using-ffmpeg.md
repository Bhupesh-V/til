# Generate Video thumbnail using ffmpeg
**_Posted on 22 Jul, 2022_**

```bash
ffmpeg -hide_banner -loglevel error -stats -i <filepath> -ss 00:00:00.000 -vframes 1 thumbnail.jpg
```

## Stuff to think about
- How do you decide a new frame timestamp?
