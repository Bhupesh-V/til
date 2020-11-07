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

<table><thead><tr><th>Directive</th><th>Meaning</th><th>Example</th></tr></thead><tbody><tr><td>%a</td><td>Weekday as locale’s abbreviated name.</td><td>Sun, Mon, …, Sat (en_US);<br>So, Mo, …, Sa (de_DE)</td></tr><tr><td>%A</td><td>Weekday as locale’s full name.</td><td>Sunday, Monday, …, Saturday (en_US);<br>Sonntag, Montag, …, Samstag (de_DE)</td></tr><tr><td>%w</td><td>Weekday as a decimal number, where 0 is Sunday and 6 is Saturday.</td><td>0, 1, …, 6</td></tr><tr><td>%d</td><td>Day of the month as a zero-padded decimal number.</td><td>01, 02, …, 31</td></tr><tr><td>%b</td><td>Month as locale’s abbreviated name.</td><td>Jan, Feb, …, Dec (en_US);<br>Jan, Feb, …, Dez (de_DE)</td></tr><tr><td>%B</td><td>Month as locale’s full name.</td><td>January, February, …, December (en_US);<br>Januar, Februar, …, Dezember (de_DE)</td></tr><tr><td>%m</td><td>Month as a zero-padded decimal number.</td><td>01, 02, …, 12</td></tr><tr><td>%y</td><td>Year without century as a zero-padded decimal number.</td><td>00, 01, …, 99</td></tr><tr><td>%Y</td><td>Year with century as a decimal number.</td><td>0001, 0002, …, 2013, 2014, …, 9998, 9999</td></tr><tr><td>%H</td><td>Hour (24-hour clock) as a zero-padded decimal number.</td><td>00, 01, …, 23</td></tr><tr><td>%I</td><td>Hour (12-hour clock) as a zero-padded decimal number.</td><td>01, 02, …, 12</td></tr><tr><td>%p</td><td>Locale’s equivalent of either AM or PM.</td><td>AM, PM (en_US);<br>am, pm (de_DE)</td></tr><tr><td>%M</td><td>Minute as a zero-padded decimal number.</td><td>00, 01, …, 59</td></tr><tr><td>%S</td><td>Second as a zero-padded decimal number.</td><td>00, 01, …, 59</td></tr><tr><td>%f</td><td>Microsecond as a decimal number, zero-padded on the left.</td><td>000000, 000001, …, 999999</td></tr><tr><td>%z</td><td>UTC offset in the form ±HHMM[SS[.ffffff]] (empty string if the object is naive).</td><td>(empty), +0000, -0400, +1030, +063415, -030712.345216</td></tr><tr><td>%Z</td><td>Time zone name (empty string if the object is naive).</td><td>(empty), UTC, GMT</td></tr><tr><td>%j</td><td>Day of the year as a zero-padded decimal number.</td><td>001, 002, …, 366</td></tr><tr><td>%U</td><td>Week number of the year (Sunday as the first day of the week) as a zero padded decimal number. All days in a new year preceding the first Sunday are considered to be in week 0.</td><td>00, 01, …, 53</td></tr><tr><td>%W</td><td>Week number of the year (Monday as the first day of the week) as a decimal number. All days in a new year preceding the first Monday are considered to be in week 0.</td><td>00, 01, …, 53</td></tr><tr><td>%c</td><td>Locale’s appropriate date and time representation.</td><td>Tue Aug 16 21:30:00 1988 (en_US);<br>Di 16 Aug 21:30:00 1988 (de_DE)</td></tr><tr><td>%x</td><td>Locale’s appropriate date representation.</td><td>08/16/88 (None);<br>08/16/1988 (en_US);<br>16.08.1988 (de_DE)</td></tr><tr><td>%X</td><td>Locale’s appropriate time representation.</td><td>21:30:00 (en_US);<br>21:30:00 (de_DE)</td></tr><tr><td>%%</td><td>A literal '%' character.</td><td>%</td></tr></tbody></table>