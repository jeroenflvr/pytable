import string

from typing import List, Tuple


p = [
    ["a", 1, "file1.py"],
    ["b", 2, "file2.py"],
    ["c", 3, "file3.py"],
    ["d", 4, "file4.py"],
    ["e", 5, "file5.py"],
    ["f", 6, "file6.py"],
]

# this is the function that we call from duckdb
def dcols(first_only: bool = False) -> list[str, int, str]:

    for col in p:
        if first_only:
            yield col[0]
        else:
            yield col[0], col[1], col[2]


if __name__ == "__main__":
    for col in dcols():
        print(col)
