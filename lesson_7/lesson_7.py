from time import time
from functools import reduce

"""Exercise 4"""


def measure_time(func):

    def wrapper(*args):
        start_time = time()
        print(func(*args))
        end_time = time()
        elapsed_time = end_time - start_time
        return (
            f"{round(elapsed_time, 3)} seconds have passed since "
            f'the function - "{func.__name__}" was called'
        )

    return wrapper


"""Exercise 1"""


def type_to_str(A: list) -> list:
    """Converts type int to str
    Return list
    """
    return list(map(str, A))


print(type_to_str([1, 2, 3]))
"""Exercise 2"""


@measure_time
def over_zero_filter(A: list) -> list:
    """Function filters a list of numbers
    which are over zero
    Returns a list of numbers
    """
    return list(filter(lambda a: a > 0, A))


print(over_zero_filter([num for num in range(-5, 10)]))
"""Exerise 3"""


@measure_time
def palindrome_filter(A: list) -> list:
    """Function filters a list of strings
    which are palindrome
    Returns a list of palindromes
    """
    for i in range(5000):
        for c in range(12000):
            pass
    return list(filter(lambda s: s == s[::-1], A))


print(palindrome_filter(["abccba", "bbccccbb", "шалаш", "Piter", "Mari"]))
"""Exercise 5"""


def area_apartment(A: list) -> int:
    """Calculates area of apartment
    by using functions: map and reduce
    Return area apartment
    """
    return reduce(
        lambda a, c: a + c, list(map(lambda x: x.get("length") * x.get("width"), A))
    )


rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width": 6.3},
]
print(area_apartment(rooms))
