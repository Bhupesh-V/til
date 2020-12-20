# Converting videos to High quality GIFs
<!-- Dec 6, 2020 -->

Converting videos to gifs using ffmpeg is a pain in the ass if you don't know what's happening.
GIF size getting 10x the size of original video ? Don't worry, I got you!

1. Always create a custom palette
2. Don't increase/decrease file dimensions
3. Save unnecessary frame conversion by using `-t` to convert video until timestamp.
4. Experiment with `fps` (default value is 24)

```bash
# Get video dimensions
ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=s=x:p=0 video.mp4
# generate a palette
ffmpeg -i video.mp4 -vf "fps=22,scale=1024:-1:flags=lanczos,palettegen" palette.png
# use the generated palette
ffmpeg -t 29 -i video.mp4 -i palette.png -filter_complex "fps=22,scale=1024:-1:flags=lanczos[x];[x][1:v]paletteuse" output.gif
```

Download complete script [**here**](https://github.com/Bhupesh-V/.Varshney/blob/master/scripts/convert-to-gif.sh)

### Resources

- [High quality GIF from video](https://d12frosted.io/posts/2018-10-13-gifify.html)
