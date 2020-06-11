# Finding all Python Virtual Environments in your system
<!-- 10 June 2020 -->
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
Only problem, it is slow.

**Sample Ouput**

```
/home/bhupesh/Desktop/testFind/bin/activate
/home/bhupesh/Desktop/bits/bin/activate
/home/bhupesh/Desktop/cc-new/bin/activate
/home/bhupesh/Desktop/test-audio/bin/activate
/home/bhupesh/Desktop/comp-code/bin/activate
/home/bhupesh/Desktop/req-blog/bin/activate
/home/bhupesh/Desktop/py-cli/bin/activate
/home/bhupesh/Desktop/sian-env/bin/activate
/home/bhupesh/Desktop/ques/bin/activate
/home/bhupesh/Documents/api/bin/activate
/home/bhupesh/Documents/defe-venv/bin/activate
/home/bhupesh/Documents/bot-tutorial/bin/activate
/home/bhupesh/Documents/cc/bin/activate
/home/bhupesh/Documents/test-package/bin/activate
/home/bhupesh/Documents/qt-lear/bin/activate
/home/bhupesh/Documents/csv-voil/bin/activate
/home/bhupesh/Documents/bottest/bin/activate
/home/bhupesh/Documents/new-tutorialdb/bin/activate
/home/bhupesh/Documents/cc2/bin/activate
/home/bhupesh/Documents/plag/bin/activate
find /home -name "*activate"  2.57s user 4.14s system 7% cpu 1:31.72 total
```

## Using `locate`

```bash
locate -b '\activate' | grep "/home"
```
Grep your home directory for all activate scripts.

**Sample Output**

```
/home/bhupesh/Desktop/bits/bin/activate
/home/bhupesh/Desktop/cc-new/bin/activate
/home/bhupesh/Desktop/comp-code/bin/activate
/home/bhupesh/Desktop/py-cli/bin/activate
/home/bhupesh/Desktop/ques/bin/activate
/home/bhupesh/Desktop/req-blog/bin/activate
/home/bhupesh/Desktop/sian-env/bin/activate
/home/bhupesh/Desktop/test-audio/bin/activate
/home/bhupesh/Desktop/testFind/bin/activate
/home/bhupesh/Documents/api/bin/activate
/home/bhupesh/Documents/bot-tutorial/bin/activate
/home/bhupesh/Documents/bottest/bin/activate
/home/bhupesh/Documents/cc/bin/activate
/home/bhupesh/Documents/cc2/bin/activate
/home/bhupesh/Documents/csv-voil/bin/activate
/home/bhupesh/Documents/defe-venv/bin/activate
/home/bhupesh/Documents/new-tutorialdb/bin/activate
/home/bhupesh/Documents/plag/bin/activate
/home/bhupesh/Documents/qt-lear/bin/activate
/home/bhupesh/Documents/test-package/bin/activate
locate -b '\activate'  0.45s user 0.02s system 99% cpu 0.476 total
grep --color=auto --exclude-dir={.bzr,CVS,.git,.hg,.svn,.idea,.tox} "/home"  0.00s user 0.00s system 0% cpu 0.472 total
```


Now you can just do `source <path>`.