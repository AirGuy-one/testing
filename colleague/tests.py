# tests

from .functions import contains_substring
from .functions import replace_substring
from .functions import get_unique_characters
from .functions import to_uppercase
from .functions import find_longest_word


def test_contains_substring():
    assert contains_substring("Hello World", "World") == True
    assert contains_substring("Hello World", "Python") == False


def test_replace_substring():
    assert replace_substring("Hello World", "World", "Python") == "Hello Python"
    assert replace_substring("Hello World", "World", "Universe") == "Hello Universe"


def test_get_unique_characters():
    assert get_unique_characters("hello") == {'h', 'e', 'l', 'o'}
    assert get_unique_characters("abc") == {'a', 'b', 'c'}

# test that contain a mistake
def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"


def test_find_longest_word():
    assert find_longest_word("This is a test") == "This"
    assert find_longest_word("") == ""
