# Record your Desktop using `ffmpeg`
<!--24 June 2020 -->
1. Make sure you have ffmpeg installed, by checking `ffmpeg -version`. If not install use `sudo apt-get install ffmpeg`.

2. Run the following command.
```bash
ffmpeg -video_size 1280x1024 -framerate 25 -f x11grab -i :0.0+0,0 -c:v libx264rgb -crf 0 -preset ultrafast output.mkv
```
- `-video_size` specifies the size of the recorded area. If you have a different screen size, use that instead of 1920x1080. If you want to record only an area of the screen, specify the area size here.

- `-framerate` specifies the frame rate, i. e. how many frames of video are recorded in a second. The lowest allowed framerate is 20.

- `-f x11grab` is what actually tells FFmpeg to record your screen. You shouldn't change that.

- `-i :0.0+0,0` is where you specify the x and y offset of the top left corner of the area that you want to record. For example, use :0.0+100,200 to have an x offset of 100 and an y offset of 200.

- `-c:v libx264rgb -crf 0 -preset ultrafast` are encoding options. These specify a fast and lossless recording.

> Run `xdpyinfo | grep 'dimensions:'` to know your monitor dimensions

## Resources
- [Record-Your-Desktop-Using-FFmpeg-on-Ubuntu-Linux](https://www.wikihow.com/Record-Your-Desktop-Using-FFmpeg-on-Ubuntu-Linux)