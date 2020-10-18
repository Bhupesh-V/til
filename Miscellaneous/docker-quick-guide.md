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
docker run -p 3000:3000 <name>
```

5. Stop a container.
```bash
docker stop <container-id>
```