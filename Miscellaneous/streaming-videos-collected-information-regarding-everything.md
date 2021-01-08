# Streaming videos, things behind the curtain
<!-- 17 Dec, 2020 -->

> This is a log of things I learn on how streaming "videos" works & what are the modern ways companies do it and possibly everything about it.


- TCP is more appropriate for serving video on demand

- Live streaming via TCP/IP, then it would be forced to wait for dropped packets before it could continue processing newer data. That's not good because:
  1. Old data will be re-transmitted (that's probably for a frame that was already displayed and therefore worthless).
  2. New data can't arrive until after old data was re-transmitted.

- UDP is ideal for teleconferencing.
- [**QUIC**](https://en.wikipedia.org/wiki/QUIC) protocol for transport layer over UDP. It is fast, secure and reliable. It builds on top of UDP

- The `<audio>` and `<video>` tags are protocol agnostic, no browser currently supports anything other than HTTP without requiring plugins, although this looks set to change. Protocols other than HTTP may also be subject to blocking from firewalls or proxy servers.

- Netflix and other streaming providers make extensive use of _distributed content delivery networks (CDN)_, which store content in locations around the world that are much closer to users.

- **Adaptive Streaming**: Quality of video is automatically chosen based on user's network and processing capabilities. (think YouTube's Auto setting. DASH)

## Protocols

1. [DASH](https://en.wikipedia.org/wiki/Dynamic_Adaptive_Streaming_over_HTTP)
   Used by YouTube, Netflix or Amazon Prime Video (and many others). [DASH’ manifest](https://github.com/google/shaka-player/blob/master/docs/design/dash-manifests.md) is called the Media Presentation Description (or MPD) and is at its base XML.
   It’s an adaptive bitrate streaming technique that enables high-quality streaming of videos over the web from conventional HTTP web servers. Via this technique, the content is made available to the viewer at different bit rates. YouTube client automatically adapts the video rendering as per the internet connection speed of the viewer thus cutting down the buffering as much as possible.
2. [HLS](https://en.wikipedia.org/wiki/HTTP_Live_Streaming)
   Developed by Apple, used by DailyMotion, Twitch.tv, and many others. The HLS manifest is called the playlist and is in the m3u8 format (which are m3u playlist files, encoded in UTF-8).
3. [Smooth Streaming](https://en.wikipedia.org/wiki/Adaptive_bitrate_streaming#Microsoft_Smooth_Streaming)
   Developed by Microsoft, used by multiple Microsoft products and MyCanal.


### Resources

- [TCP vs UDP on video stream](https://stackoverflow.com/questions/6187456/tcp-vs-udp-on-video-stream)
- [Live streaming web audio and video](https://developer.mozilla.org/en-US/docs/Web/Guide/Audio_and_video_delivery/Live_streaming_web_audio_and_video)
- [How video streaming works on the web: An introduction](https://medium.com/canal-tech/how-video-streaming-works-on-the-web-an-introduction-7919739f7e1)

