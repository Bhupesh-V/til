# Everything about date & time in python
**_Posted on 02 Apr, 2021_** 

> Earth rotates just like my head trying to understand dates and time-zones.

## Get current date & time

```python
>>> import datetime
# without timezone
>>> datetime.datetime.now().strftime("%d %b, %Y (%I:%M:%S %p)")
'02 Apr, 2021 (01:37:43 PM)'
# with local timezone
>>> datetime.datetime.now(datetime.timezone.utc).astimezone().strftime("%d %b, %Y (%I:%M:%S %p) %Z")
'02 Apr, 2021 (01:38:20 PM) IST'
```

## Current date/time to Unix timestamp

```python
>>> import time
>>> t = datetime.datetime.now(datetime.timezone.utc).astimezone()
>>> t.timetuple()
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=2, tm_hour=13, tm_min=43, tm_sec=15, tm_wday=4, tm_yday=92, tm_isdst=-1)
>>> time.mktime(t.timetuple())
1617351195.0
```


## Unix timestamp to date/time

```python
>>> import time
>>> t = datetime.datetime.now(datetime.timezone.utc).astimezone()
>>> t.timetuple()
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=2, tm_hour=13, tm_min=43, tm_sec=15, tm_wday=4, tm_yday=92, tm_isdst=-1)
>>> time.mktime(t.timetuple())
1617351195.0
>>> time.localtime(time.mktime(t.timetuple()))
time.struct_time(tm_year=2021, tm_mon=4, tm_mday=2, tm_hour=13, tm_min=46, tm_sec=32, tm_wday=4, tm_yday=92, tm_isdst=0)
# verify
>>> time.strftime("%d %b, %Y (%I:%M:%S %p)", h)
'02 Apr, 2021 (01:46:32 PM IST)'
```

