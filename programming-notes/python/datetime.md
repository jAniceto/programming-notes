# Datetime module

The `datetime` module is a standard library module that supplies classes for manipulating dates and times. While date and time arithmetic is supported, the focus of the implementation is on efficient attribute extraction for output formatting and manipulation.

The `datetime` module has three types for storing a point in time:

* `date` for year, month, day of month
* `time` for hours, minutes, seconds, microseconds, time zone info
* `datetime` combines `date` and `time`. It has the methods `date()` and `time()` to get the corresponding date and time objects, and there's a handy `combine` function to combine date and time into a datetime.


## Parsing and formatting date strings

`datetime.strptime` is the main routine for parsing strings into datetimes. It can handle all sorts of formats, with the format determined by a format string you give it:

```python
from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
```

`datetime.strftime` is the routine to format datetime objects to string.
```python
import datetime

t = datetime.datetime(2012, 2, 23, 0, 0)
t.strftime('%m/%d/%Y')
# output: '02/23/2012'
```

Format options available in the [datetime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) and at [strftime.org](http://strftime.org/).

To summarize:
* `strptime` = "string parse time"
* `strftime` = "string format time"
