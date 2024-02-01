# Docker image load & save

**_Posted on 01 Feb, 2024_**


Short guide on how to export and import docker images across different machines.

1. Build for different platforms
   ```
   docker build -t ugit-optimized-linux --platform linux/amd64 .
   ```

2. Save the image
   ```
   docker save <image:tag> > test.tar
   ```

3. Tranfer the image to another machine.
4. Load the image
   ```
   docker load < test.tar
   ```

## References

- https://pspdfkit.com/blog/2019/docker-import-export-vs-load-save/