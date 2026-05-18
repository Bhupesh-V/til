# Audio/Video Ops

## Reducing Background Noise

```sh
ffmpeg -i input.mp4 -af "afftdn=nr=12:nf=-25" -c:v copy output.mp4 
ffmpeg -i input.mp4 -af "anlmdn=s=0.001" -c:v copy output.mp4
```

- `afftdn`: Activates the FFT denoise filter.
- `nr=12`: Noise reduction strength in dB (default is 12). Increase this value for stronger noise removal, but values too high may distort human speech.
- `nf=-25`: Noise floor in dB (default is -25). Adjusts the threshold below which audio is treated as noise.
- `-c:v copy`: Copies the video stream directly without re-encoding to save processing time and preserve original video quality.


## Video to Audio

```
ffmpeg -i input.mp4 -b:a 192k output.mp3
```

- `-b:a` is bitrate, use 192k or 320k.

## Waveform Videos

This creates a white colored wave form on a black background
```
ffmpeg -i audio.mp3 -filter_complex "[0:a]showwaves=s=1280x720:mode=line:colors=white" -c:v libx264 -preset fast -crf 23 -c:a copy output.mp4
```

ffmpeg -y -i final.mp3 -loop 1 -i bg.jpg -filter_complex "[0:a]showwaves=s=1920x300:colors=0x00A8E8:mode=cline,format=rgba[v];[1:v][v]overlay=0:780[outv]" -map "[outv]" -map 0:a -c:v libx264 -c:a aac -shortest -pix_fmt yuv420p final_podcast.mp4

ffmpeg -y -i final.mp3 -loop 1 -i bg.jpeg -filter_complex "[0:a]showwaves=s=1080x100:colors=0x00A8E8:mode=cline,format=rgba[wave];[1:v][wave]overlay=0:260:shortest=1[outv]" -map "[outv]" -map 0:a -c:v libx264 -c:a aac -pix_fmt yuv420p final_podcast.mp4

ffmpeg -y -i final.mp3 -loop 1 -i bg.jpeg -filter_complex "[0:a]showwaves=s=1080x200:colors=0xFFD700:mode=cline,format=rgba[wave];[1:v][wave]overlay=0:160:shortest=1[outv]" -map "[outv]" -map 0:a -c:v libx264 -c:a aac -pix_fmt yuv420p final_podcast.mp4

<!-- ffmpeg -i input -filter_complex "[0:a]showwaves=s=1280x720:mode=line,format=yuv420p[v]" -map "[v]" -map 0:a -c:v libx264 -c:a copy output.mkv -->

<!-- ffmpeg -i final.mp3 -loop 1 -i bg.jpeg -filter_complex "[0:a]showwaves=s=1080x200:colors=0xFFD700:mode=line,format=yuv420p[v];[1:v][wave]overlay=0:160:shortest=1[outv]" -map "[outv]" -map 0:a -c:v libx264 -c:a aac -pix_fmt yuv420p final_podcast.mp4 -->

### Circular Waveform

```
ffmpeg -i ../final.mp3 -loop 1 -i ../bg.jpeg -filter_complex "[0:a]aformat=channel_layouts=mono,showwaves=s=400x400:mode=line:colors=0xff1646:draw=full,geq='p(mod(W/PI*(PI+atan2(H/2-Y,X-W/2)),W), H-2*hypot(H/2-Y,X-W/2))':a='alpha(mod(W/PI*(PI+atan2(H/2-Y,X-W/2)),W), H-2*hypot(H/2-Y,X-W/2))'" -c:v libx264 -pix_fmt yuv420p -c:a aac circular.mp4 -y
```

[source](https://www.reddit.com/r/ffmpeg/comments/1fwvjb2/comment/lqlx4hd/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button)

Variations

```
ffmpeg -i ../final.mp3 -loop 1 -i ../bg.jpeg -filter_complex "[0:a]aformat=channel_layouts=mono,showwaves=s=650x650:mode=line:colors=0xFFD700:draw=full,geq='p(mod(W/PI*(PI+atan2(H/2-Y,X-W/2)),W), H-2*hypot(H/2-Y,X-W/2))':a='alpha(mod(W/PI*(PI+atan2(H/2-Y,X-W/2)),W), H-2*hypot(H/2-Y,X-W/2))'[wave]; [1:v][wave]overlay=(W-w)/2:(H-h)/2" -c:v libx264 -pix_fmt yuv420p -c:a aac -shortest -t 10 circular.mp4 -y
```