# Docker 🐋 quick guide
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
   > For the love of God always add a `-d` while running a container. Speaking this from experience.

   If you don't run in detach mode, you won't be able to Ctrl+C (or exit), instead use Ctrl+PC (yes the P key and C key).

7. List docker volumes.
   ```bash
   docker volume ls
   ```

8. Remove docker volume.
   ```bash
   docker volume rm <volume-name>
   ```


## Docker Compose

1. Build and run containers.
   ```bash
   docker-compose up -d
   ```

2. Stop containers.
   ```bash
   docker-compose stop
   ```

3. Check logs/console messages.
   ```bash
   docker-compose logs <image name>
   ```

4. List all containers.
   ```bash
   docker-compose ps
   ```
