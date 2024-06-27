from __future__ import unicode_literals
import unittest


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