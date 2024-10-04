# tests

from .functions import bubble_sort
from .functions import factorial
from .functions import fibonacci
from .functions import reverse_string
from .functions import sum_list


def test_sum_list():
    assert sum_list([1, 2, 3, 4, 5]) == 15
    assert sum_list([-1, 1, -2, 2]) == 0
    assert sum_list([]) == 0
    assert sum_list([100]) == 100


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(7) == 5040


def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(10) == 55


def test_bubble_sort():
    assert bubble_sort([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    assert bubble_sort([5, 1, 4, 2, 8]) == [1, 2, 4, 5, 8]
    assert bubble_sort([]) == []
    assert bubble_sort([1]) == [1]


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
