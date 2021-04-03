# Converting 📅⏲ datetime object to string & vice-versa
<!-- 7 Nov, 2020 -->

Sometimes only the standard lib `datetime` is necessary to do all date/time related tasks. 

> I am logging this here because I always forget how to do this 😶 (I want to end this once and for all)

## `datetime` object to string

```python
>>> from datetime import datetime
>>> d = datetime.now()
>>> d
datetime.datetime(2020, 11, 7, 20, 15, 58, 389341)
>>> d.strftime("%d %b, %Y")
'07 Nov, 2020'
```

## From string to `datetime` object

```python
>>> from datetime import datetime
>>> date_string = "2020-06-20T08:22:54Z"
>>> datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ')
datetime.datetime(2020, 6, 20, 8, 22, 54)
```

Both `strptime` & `strftime` can ofc be chained.

```python
>>> from datetime import datetime
>>> date_string = "2020-06-20T08:22:54Z"
>>> datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%SZ').strftime("%d %b, %Y")
```

This can be handy when you are getting date/time fields from external resource (like an API) and only want to display a part of it (like days, month etc).

[**Format codes for `strptime` and `strftime`**](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes)

|Directive|Meaning|Example|
|--- |--- |--- |
|%a|Weekday as locale’s abbreviated name.|Sun, Mon, …, Sat (en_US);So, Mo, …, Sa (de_DE)|
|%A|Weekday as locale’s full name.|Sunday, Monday, …, Saturday (en_US);Sonntag, Montag, …, Samstag (de_DE)|
|%w|Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.|0, 1, …, 6|
|%d|Day of the month as a zero-padded decimal number.|01, 02, …, 31|
|%b|Month as locale’s abbreviated name.|Jan, Feb, …, Dec (en_US);Jan, Feb, …, Dez (de_DE)|
|%B|Month as locale’s full name.|January, February, …, December (en_US);Januar, Februar, …, Dezember (de_DE)|
|%m|Month as a zero-padded decimal number.|01, 02, …, 12|
|%y|Year without century as a zero-padded decimal number.|00, 01, …, 99|
|%Y|Year with century as a decimal number.|0001, 0002, …, 2013, 2014, …, 9998, 9999|
|%H|Hour (24-hour clock) as a zero-padded decimal number.|00, 01, …, 23|
|%I|Hour (12-hour clock) as a zero-padded decimal number.|01, 02, …, 12|
|%p|Locale’s equivalent of either AM or PM.|AM, PM (en_US);am, pm (de_DE)|
|%M|Minute as a zero-padded decimal number.|00, 01, …, 59|
|%S|Second as a zero-padded decimal number.|00, 01, …, 59|
|%f|Microsecond as a decimal number, zero-padded on the left.|000000, 000001, …, 999999|
|%z|UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).|(empty), +0000, -0400, +1030, +063415, -030712.345216|
|%Z|Time zone name (empty string if the object is naive).|(empty), UTC, GMT|
|%j|Day of the year as a zero-padded decimal number.|001, 002, …, 366|
|%U|Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.|00, 01, …, 53|
|%W|Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.|00, 01, …, 53|
|%c|Locale’s appropriate date and time representation.|Tue Aug 16 21:30:00 1988 (en_US);Di 16 Aug 21:30:00 1988 (de_DE)|
|%x|Locale’s appropriate date representation.|08/16/88 (None);08/16/1988 (en_US);16.08.1988 (de_DE)|
|%X|Locale’s appropriate time representation.|21:30:00 (en_US);21:30:00 (de_DE)|
|%%|A literal '%' character.|%|

