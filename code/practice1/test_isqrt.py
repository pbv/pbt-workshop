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

# -----------------------------------------------------
# unit tests
# ----------------------------------------------------

def test_isqrt_unit():
    assert isqrt(0) == 0
    assert isqrt(2) == 1
    assert isqrt(4) == 2
    assert isqrt(5) == 2
    assert isqrt(9) == 3


# ---------------------------------------------------
# property tests
# ---------------------------------------------------
    
@given(st.integers(min_value=0))
def test_isqrt_prop(n):
    r = isqrt(n)
    assert r**2<=n and (r+1)**2>n
