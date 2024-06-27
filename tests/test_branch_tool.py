from dateutil.rrule import rrulebase
from dateutil.tz._common import tzrangebase

from datetime import datetime, timedelta

import pytest

from dateutil.parser import parserinfo, parser
import pytest

from datetime import datetime, timedelta
from dateutil.rrule import rrule, DAILY

# Define a mock parserinfo
class MockParserInfo(parserinfo):
    def hms(self, s):
        return int(s[:-1])  # Simple mock implementation

class MockParser(parser):
    def __init__(self, info=None):
        super().__init__(info)

# Directly test the _parse_hms method
def test_parse_hms_with_none():
    info = MockParserInfo()
    p = MockParser()  # Instantiate parser without parserinfo

    tokens = ['10h', '36m', '28s']
    idx = 0
    hms_idx = None  # Explicitly set to None to test this branch

    # Access the _parse_hms method and call it
    new_idx, hms = p._parse_hms(idx, tokens, info, hms_idx)

    assert new_idx == idx
    assert hms is None

def test_parse_hms_with_hms_idx_backward():
    info = MockParserInfo()
    p = MockParser()  # Instantiate parser without parserinfo

    tokens = ['10h', '36m', '28s']
    idx = 2
    hms_idx = 1

    # Access the _parse_hms method and call it
    new_idx, hms = p._parse_hms(idx, tokens, info, hms_idx)

    assert new_idx == idx
    assert hms == 37  # 36 + 1 as per the code logic

def test_contains_elif_branch():
    # Create an rrule object with a known set of elements
    rr = rrule(DAILY, count=3, dtstart=datetime(1997, 9, 2, 9, 0))

    # Iterate once to make sure the cache is partially filled but not complete
    next(iter(rr))
    
    # Check for an item that is smaller than the first element to trigger the elif branch
    assert not datetime(1997, 9, 1, 9, 0) in rr



def test_print_branch_coverage_hms():
    info = MockParser()

    if not hasattr(info, 'branch_coverage'):
        print("No branch coverage information available")
        return
    
    print("\n\nBranch coverage:\n")

    total = len(info.branch_coverage.keys())

    for item, hit in info.branch_coverage.items():
        print(f"{item}: {'hit' if hit else 'miss'}")

    hit = len([v for v in info.branch_coverage.values() if v])
    print(f"\nTotal: {hit}/{total} ({hit/total:.2%})")

def test_print_branch_coverage_contains():
    info = rrulebase()

    if not hasattr(info, 'branch_coverage'):
        print("No branch coverage information available")
        return
    
    print("\n\nBranch coverage:\n")

    total = len(info.branch_coverage.keys())

    for item, hit in info.branch_coverage.items():
        print(f"{item}: {'hit' if hit else 'miss'}")

    hit = len([v for v in info.branch_coverage.values() if v])
    print(f"\nTotal: {hit}/{total} ({hit/total:.2%})")

# Ensure pytest picks up these tests
if __name__ == "__main__":
    pytest.main()
