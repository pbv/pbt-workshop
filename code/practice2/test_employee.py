# -------------------------------------------------------------
# Hypothesis round-trip property for employee encoding/decoding
#
# Pedro Vasconcelos, 2025
# -------------------------------------------------------------

from employee import encode, decode
from hypothesis import given, strategies as st
from datetime import date

ids = st.integers(min_value=1,max_value=100)
names = st.text(min_size=1)  # avoid empty names
starts = st.dates(min_value=date(2000,1,1), 
                  max_value=date(2025,1,1))
notes = st.text()
rows = st.tuples(ids, names, starts, notes)
tables = st.lists(rows, min_size=1) # avoid empty tables

@given(tables)
def test_csv_round_trip(table):
    assert decode(encode(table)) == table
