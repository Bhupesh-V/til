# Docker multi-platform build using buildx

**_Posted on 01 Feb, 2024_**

## Build for different platforms

> Tip: To figure which platforms to build for, head over to dockerhub and find what architectures your base image supports. For example, the [alpine](https://hub.docker.com/_/alpine) image supports `linux/amd64`, `linux/arm64` etc.


```
docker buildx build --load\
--platform linux/amd64,linux/arm64,linux/386,linux/s390x,linux/arm/v7,linux/arm/v6,linux/ppc64le \
-t image:tag \
-f Dockerfile .
```

- Builds generated using buildx will not be available in the local docker registry. To push the image to the registry, use the `--push` flag.
- To load the image into the local docker registry, use the `--load` flag.
  - After load you can choose to export it to a tar file using `docker save <image:tag> > test.tar` and test it on another machine using `docker load < test.tar`.
