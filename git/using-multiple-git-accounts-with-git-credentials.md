# Using multiple git user configs with credentials store (multiple github accounts)

**_Posted on 18 Feb, 2023_**

So, you have decided to have 2 separate accounts for work and personal.
Here are steps to follow to use both git configurations simultaneously with same `.git-credentials`.

## Step 1: Separate Work/Personal directories

Create a `work` and a `personsal` directory in your Documents folder. Use these directories to separate your git directories.

```bash
  Documents
  ├── work
  │   ├── ...
  │   └── ...
  └── personal
      ├── ...
      └── ...
```

## Step 2: Separate git config for each account

- Create `.gitconfig-personal` in the `personal` dir.

  ```
  [credential]
    helper = store
  [user]
    name = Personal_Username
    email = personal_email@domain.com
  [credential "https://github.com"]
    username = Personal_Username
    helper = store
  ```

- Create `.gitconfig-work` in the `work` dir.

  ```
  [credential]
    helper = store
  [user]
    name = Work_Username
    email = work_email@domain.com
  [credential "https://github.com"]
    username = Work_Username
    helper = store
  ```

## Step 3: Update global `.gitconfig` to switch the profile based on directory

- Update your global config using following command.

  ```bash
  git config --global --edit
  ```

- Add the following config.

  ```bash
  [includeIf "gitdir:~/Documents/work/"]
      path = ~/Documents/work/.gitconfig-work
  [includeIf "gitdir:~/Documents/personal/"]
      path = ~/Documents/personal/.gitconfig-personal
  ```

## Step 4: Register Access Tokens

- Check your `.git-credentials` file & add [github access tokens](https://github.com/settings/tokens) for each account.

  ```bash
  https://Personal_Username:PERSONAL_TOKEN@github.com
  https://Work_Username:WORK_TOKEN@github.com
  ```

That's it, the next time you pull/push/clone a private repo, git will automatically choose the correct token for each config.
