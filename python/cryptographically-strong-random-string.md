# Cryptographically strong random string

One liner

```bash
python3 -c "import secrets;print(secrets.token_urlsafe())"
```

Sample Runs

```bash
>>> import secrets
>>> secrets.token_urlsafe()
'noLCpWgg5bJbALwlqAKKWUcb4nZg0LvxIUFHyhyei-I'
>>> secrets.token_urlsafe()
'8HhV5FMm2vxfrSoO9o_v65FRy6bLbvc89POSX0fnMqk'
>>> secrets.token_urlsafe()
'bClPydJqA7_0GsDvUAqqShUH5ZucWzdErg0tZIGZU2k'
>>> secrets.token_urlsafe()
'82LSHzCKkwo5y__3NZrck27ZbDL1WiKoSYxQQki8uvA'
>>> 
```