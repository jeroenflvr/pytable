# PyTables DuckDB Extension

This executes your python function and returns the data as a table.

## function requirements

- yield results


## example

The Python dcols() function.
```python
import string

from typing import List, Tuple


TESTDATA = [
    ["a", 1, "file1.py"],  # each row is a tuple 
    ["b", 2, "file2.py"],
    ["c", 3, "file3.py"],
    ["d", 4, "file4.py"],
    ["e", 5, "file5.py"],
    ["f", 6, "file6.py"],
]

# this is the function that we call from duckdb
def dcols(first_col_only: bool = False) -> list[str, int, str]:

    for col in TESTDATA:
        if first_col_only:
            yield col[0]
        else:
            yield col[0], col[1], col[2]


if __name__ == "__main__":
    for col in dcols():
        print(col)
```

Calling dcols() from duckdb.
```sql
$ PYTHONPATH=. ./build/release/duckdb
┌─────────┐
│ Success │
│ boolean │
├─────────┤
│ true    │
└─────────┘
DuckDB v1.3.2 (Ossivalis) 0b83e5d2f6
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D create or replace view first as select * from pytable("first_test:dcols", columns = {"name": VARCHAR, "value": INTEGER, "comment": VARCHAR});
D select * from first;
┌─────────┬───────┬──────────┐
│  name   │ value │ comment  │
│ varchar │ int32 │ varchar  │
├─────────┼───────┼──────────┤
│ a       │     1 │ file1.py │
│ b       │     2 │ file2.py │
│ c       │     3 │ file3.py │
│ d       │     4 │ file4.py │
│ e       │     5 │ file5.py │
│ f       │     6 │ file6.py │
└─────────┴───────┴──────────┘
D

$
```

Calling dcols() with the keyword argument "first_col_only".
```sql
$ PYTHONPATH=. ./build/release/duckdb
┌─────────┐
│ Success │
│ boolean │
├─────────┤
│ true    │
└─────────┘
DuckDB v1.3.2 (Ossivalis) 0b83e5d2f6
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D create or replace view first as select * from pytable("first_test:dcols", kwargs={"first_col_only": True}, columns = {"name": VARCHAR});
D select * from first;
┌─────────┐
│  name   │
│ varchar │
├─────────┤
│ a       │
│ b       │
│ c       │
│ d       │
│ e       │
│ f       │
└─────────┘
D

$
```