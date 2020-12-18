# Finding the file creation date/time on Linux
<!-- 18 Dec, 2020 -->
### 1. Find inode number of file.
   ```bash
   $ ls -i myfile.md
   9344160 myfile.md
   ```
### 2. Find name of your root partition
   ```bash
   $ df -h
   Filesystem      Size  Used Avail Use% Mounted on
   udev            924M     0  924M   0% /dev
   tmpfs           191M  1.4M  190M   1% /run
   /dev/sda1       146G   38G  101G  28% /
   tmpfs           954M  121M  833M  13% /dev/shm
   ...
   ```
### 3. Use the inode no in `stat` & `debugfs`
   ```bash
   sudo debugfs -R 'stat <9344160>' /dev/sda1
   ```
   Look for **crtime**, that is our file creation date/time

Here is a one liner if your filesystem is ext4
```bash
sudo debugfs -R "stat <$(ls -i myfile.md | awk '{ print $1}')>" /dev/sda1 | grep 'crtime'
```

- debugfs is a ext2, ext3, ext4 file system debugger. The `-R` flag causes debugfs to execute a single command. In our case that command is `stat` which is used to check file status. We need to run debugfs where our filesystem is mounted, i.e `/dev/sda1`.

> **Note**: this will not work on older file systems.
  Although this has changed with modern file systems such as ext4 & Btrfs which has been designed to store file creation time.
