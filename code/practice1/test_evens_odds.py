
from hypothesis import given, strategies as st

# a strategy for even integers
evens = st.integers().map(lambda x: 2*x)

# a strategy for odd integers
odds = st.integers().map(lambda x: 2*x+1)

@given(odds, odds)
def test_add_odd_numbers(x, y):
    assert (x+y)%2 == 0  # check that the sum is even
