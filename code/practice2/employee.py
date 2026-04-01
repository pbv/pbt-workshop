# -----------------------------------------------------------
# Encoding an employee directory to/from CSV
#
# Pedro Vasconcelos, 2025
# -----------------------------------------------------------
import csv
import io
from datetime import date

def encode(table):
    "Encode an employee directory as into CSV." 
    buff = io.StringIO()
    writer = csv.writer(buff)
    for row in table:
        writer.writerow(row)
    output = buff.getvalue()
    buff.close()
    return output

def decode(txt):
    "Decode CSV text into an employee directory."
    reader = csv.reader(io.StringIO(txt))
    result = []
    for row in reader:
        (id, name, start, notes) =  row
        values = (int(id),
                  name,
                  date.fromisoformat(start),
                  notes)
        result.append(values)
    return result



# --------------------------------------------------------------------
# Exercise: define a round-trip property to find errors
# in the following "naive" implementations
# --------------------------------------------------------------------
def naive_encode(table):
    lines = []
    for row in table:
        line = ','.join(map(str, row))
        lines.append(line)
    return '\n'.join(lines)

def naive_decode(txt):
    rows = []
    for line in txt.split('\n'):
        (id, name, start, notes) = line.split(',')
        row = (int(id),name,date.fromisoformat(start),notes)
        rows.append(row)
    return rows
    
