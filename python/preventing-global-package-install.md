# Preventing global package install with `PIP_REQUIRE_VIRTUALENV`


To make sure you have an virtual env activated whenever you do `pip install`, add the following line to your `.bashrc`

```bash
export PIP_REQUIRE_VIRTUALENV=true
```

If you now try to install packages outside a virtual environment `pip` will remind you.

```
$ pip install django
ERROR: Could not find an activated virtualenv (required).
```

In some cases you will need to install global packages (like vim plugins etc). For that create a separate bash function like this

```bash
gpip() {
    PIP_REQUIRE_VIRTUALENV=false pip "$@"
}
```
