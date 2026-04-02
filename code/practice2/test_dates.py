#
# Exercise: show that our dates strategy can generate invalid dates
# and how Hypothesis shrinking can simplifies test cases
#

from hypothesis import Phase, settings, given, strategies as st

years = st.integers(min_value=1970, max_value=2100)
months = st.integers(min_value=1, max_value=12)
days = st.integers(min_value=1, max_value=31)
dates = st.tuples(years, months, days)

def valid_date(date):
    """Check if a date is valid. Does not handle leap years."""
    days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y,m,d = date
    return d <= days_of_month[m-1] 


# Configure Hypothesis to run more tests and only specific phases
# Try removing Phase.shrink and observe the counter-examples found
@settings(max_examples=500, phases=[Phase.generate, Phase.shrink])
@given(dates)
def test_valid_date(date):
    assert valid_date(date)
