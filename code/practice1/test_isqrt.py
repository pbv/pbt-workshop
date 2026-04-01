# -------------------------------------------------------
# Example of testing an integer square root function
#
# Run this with
# pytest test_isqrt.py
#
# Pedro Vasconcelos, 2025
# -------------------------------------------------------
from isqrt import isqrt
from hypothesis import given, strategies as st

@given(st.integers(min_value=0))
def test_isqrt_correct(n):
    r = isqrt(n)
    assert r**2<=n and (r+1)**2>n
