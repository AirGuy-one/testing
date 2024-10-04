# functions

def sum_list(arr: list[int]) -> int:
    """Calculate the sum of all elements in a list."""
    total: int = 0
    for num in arr:
        total += num
    return total


def factorial(num: int) -> int:
    """Calculate the factorial of a given number."""
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


def fibonacci(num: int) -> int:
    """Return the nth Fibonacci number using recursion."""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


def bubble_sort(arr: list[int]) -> list[int]:
    """Sort a list of numbers using the Bubble Sort algorithm."""
    n: int = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def reverse_string(string: str) -> str:
    """Reverse a given string."""
    return string[0::-1]
