import random
import time


def str_time_prop(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop, form='%Y-%m-%d %H:%M:%S'):
    return str_time_prop(start, end, form, prop)

def random_dates(start, end, form='%Y-%m-%d %H:%M:%S', numOfDates=5):
    dates = set()
    while len(dates) < numOfDates:
        dates.add(random_date(start, end, random.random(), form))
    return sorted(dates, key=lambda date: time.strptime(date, form))

if __name__ = "__main__":
    print(random_date("2010-08-21 00:00:00", "2020-08-21 00:00:00", random.random()))
    print(random_dates("2010-08-21 00:00:00", "2020-08-21 00:00:00"))
