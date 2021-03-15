# Parsing `git status` for tracked & untracked changes
**_Posted on 15 Mar, 2021_**

## Get count of untracked changes ➕️ (new files)

```bash
git status --porcelain | grep -c "??\s"
```

## Get count of tracked "deleted" files
```bash
git status --porcelain | grep -c "AD\s"
```

## Get count of modified files
```bash
git status --porcelain | grep -c "M\s"
```

## Get count of tacked changes
```bash
git status --porcelain | grep -c "A\s"
```

