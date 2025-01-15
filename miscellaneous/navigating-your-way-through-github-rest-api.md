# Navigating your way through Github API

1. GET repositories of a user
   ```
   https://api.github.com/users/{username}/repos?type=owner&per_page=100"
   ```

2. GET all PRs of a user.
   ```
	https://api.github.com/search/issues?q=author%3A{username}+type%3Apr&per_page=100
   ```

3. GET all issues opened by a user
   ```
	https://api.github.com/search/issues?q=author%3A{username}+type%3Aissue&per_page=100
   ```

4. GET all python repos with stars in desecending order
   ```
	https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&per_page=100
   ```

5. List all files inside a repo
   ```
	https://api.github.com/repos/{username}/{repo}/git/trees/{branch}?recursive=1
   ```

6. GET a single file in `base64` format
   ```
	https://api.github.com/repos/Bhupesh-V/defe/contents/README.md
   ```