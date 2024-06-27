
from dateutil.tz._common import tzrangebase

from datetime import datetime, timedelta

import pytest

DST_OFFSET = timedelta(hours=1)
STD_OFFSET = timedelta(hours=0)
TRANSITIONS = (datetime(2024, 3, 31, 2, 0, 0), datetime(2024, 10, 27, 2, 0, 0))

class MockTZRangeBase(tzrangebase):
    def __init__(self, dst_offset, std_offset, dst_abbr, std_abbr, transitions):
        self._dst_offset = dst_offset
        self._std_offset = std_offset
        self._dst_abbr = dst_abbr
        self._std_abbr = std_abbr
        self._transitions = transitions
        self.hasdst = True

def test_dst_none():
    mock_tz = MockTZRangeBase(DST_OFFSET, STD_OFFSET, 'DST', 'STD', TRANSITIONS)
    assert mock_tz.dst(None) is None

def test_tzrangebase_init_raises_not_implemented_error():
    with pytest.raises(NotImplementedError, match='tzrangebase is an abstract base class'):
        tzrangebase()

def test_print_branch_coverage():
    mock_tz = MockTZRangeBase(DST_OFFSET, STD_OFFSET, 'DST', 'STD', TRANSITIONS)

    if not hasattr(mock_tz, 'branch_coverage'):
        print("No branch coverage information available")
        return
    
    print("\n\nBranch coverage:\n")

    total = len(mock_tz.branch_coverage.keys())

    for item, hit in mock_tz.branch_coverage.items():
        print(f"{item}: {'hit' if hit else 'miss'}")

    hit = len([v for v in mock_tz.branch_coverage.values() if v])
    print(f"\nTotal: {hit}/{total} ({hit/total:.2%})")