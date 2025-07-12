from typing import List, Tuple
import random
import string
import time

def random_tuple_generator():
    """
    Generator function that yields a tuple (random_str1, random_int, random_str2)
    every 5 seconds indefinitely.
    """
    while True:
        # Generate a random string of 5 letters.
        random_str1 = ''.join(random.choices(string.ascii_letters, k=5))
        # Generate a random integer between 1 and 100.
        random_int = random.randint(1, 100)
        # Generate another random string of 5 letters.
        random_str2 = ''.join(random.choices(string.ascii_letters, k=5))
        # Yield the tuple.
        yield (random_str1, random_int, random_str2)
        # Pause execution for 5 seconds.
        time.sleep(5)

p = [
    ["a", 1, "file1.py"],
    ["b", 2, "file2.py"],
    ["c", 3, "file3.py"],
    ["d", 4, "file4.py"],
    ["e", 5, "file5.py"],
    ["f", 6, "file6.py"],
]


def dcols() -> List[Tuple[str, int, str]]:
    first_only = False

    for col in p:
        if first_only:
            yield col[0]
        else:
            yield col[0], col[1], col[2]



if __name__ == "__main__":
    for col in dcols():
        print(col)
