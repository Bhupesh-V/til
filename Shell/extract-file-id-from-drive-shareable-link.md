# Extract file id from drive shareable link

I host my blog images on Google Drive sometimes, the normal shareable link is not
the actual image source.
Instead this is :

`https://drive.google.com/uc?export=view&id=<INSERT-ID>`

`INSERT_ID` is the file id (in the shareable link)which is higlighted below

[https://drive.google.com/file/d/**1ifRiquoNw3awVTX6geyNoDp8FW6tafOE**/view?usp=sharing]()

here is a bash script to convert the link.

```bash
#!/usr/bin/env bash

str="$1"
# remove everything after the last /
remove_last=${str%/*}
# get everything after the last /
get_last=${remove_last##*/}
echo "https://drive.google.com/uc?export=view&id=$get_last"
```

[Also a Python version](https://gist.github.com/Bhupesh-V/7ad79f1cf6e007df1be02aeba22ec586)

You can now use it in `<img>` src