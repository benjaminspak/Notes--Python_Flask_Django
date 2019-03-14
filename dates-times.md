### Dates and Times Python

##### Datetime Basics
```python

import datetime
dir(datatime)
datetime.datetime.now()  # Data & time call
store = datetime.datetime.now()
store.replace(hour=9, minute=0, second=0, microsecond=0)  # Alter the date time.
```

##### Time Deltas

```python
import datetime
now = datetime.datetime.now()
# now == datetime.datetime(2019, 2, 28, 13, 48, 2, 923763)

datetime.timedelta(hours=5)
# How to get the timedelta time readout.
# >> datetime.timedelta(0, 18000)

datetime.timedelta(days=3)
# Get the timedelta time readout.
# >> datetime.timedelta(3)

now + datetime.timedelta(days=3)
# >>> datetime.datetime(2019, 3, 3, 13, 48, 2, 923763)
```

##### Time
```python
now = datetime.datetime.now()
now.time()
```

##### Date
```python
now = datetime.datetime.now()
now.date()
```