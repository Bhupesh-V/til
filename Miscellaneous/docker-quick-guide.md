# Docker quick guide
<!-- 18 Oct 2020 -->

1. Remove docker image.
```bash
docker rmi <img-id>
```

2. Remove docker container.
```bash
docker rm <container-id>
```

3. Build a docker image with a name.
```bash
docker build -f <dockerfile-path> -t name .
```

4. Run a container.
```bash
docker run -p 3000:3000 <container-id>
```

5. Stop a container.
```bash
docker stop <container-id>
```

6. Run a container in detach mode (run in background).
```bash
docker run -d <container-id>
```