from __future__ import unicode_literals

from datetime import datetime, date
import unittest
from six import PY2
from dateutil.rrule import rrule, DAILY
from dateutil import tz
from dateutil.rrule import (
    rrule, rruleset, rrulestr,
    YEARLY, MONTHLY, WEEKLY, DAILY,
    HOURLY, MINUTELY, SECONDLY,
    MO, TU, WE, TH, FR, SA, SU
)

from freezegun import freeze_time

import pytest

class WeekdayTest(unittest.TestCase):
    def test_contains_elif_branch(self):
        from datetime import datetime, timedelta
        from dateutil.rrule import rrule, DAILY

        # Create an rrule object with a known set of elements
        rr = rrule(DAILY, count=3, dtstart=datetime(1997, 9, 2, 9, 0))

        # Iterate once to make sure the cache is partially filled but not complete
        next(iter(rr))
        
        # Check for an item that is smaller than the first element to trigger the elif branch
        self.assertFalse(datetime(1997, 9, 1, 9, 0) in rr)

    # Make sure to include this test in your existing test class
    if __name__ == '__main__':
        unittest.main()