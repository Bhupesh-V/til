# Finding all Python Virtual Environments in your system

So if you work with Python all day, you already know about Virtual Environments.
The only problem with me 😅 is that I end up creating a lot of them when using and making my side-projects.
We know that there is a `activate` script that can be used for this purpose.

shut up & give me answer

Ok

## Using `find`

```bash
find /home -name "*activate"
```

This will list out all activate scripts in your home directory (should work fine).
Only problem it is slow

## Using `locate`

```bash
locate -b '\activate' | grep "/home"
```

Grep your home directory for all activate scripts.


Now you can just do `source <path>`.