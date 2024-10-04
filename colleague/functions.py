# functions

def contains_substring(s, substring):
    """
    Проверяет, содержит ли строка подстроку.
    Возвращает True, если содержит, иначе False.
    """
    return substring in s


def replace_substring(s, old, new):
    """
    Заменяет все вхождения подстроки в строке.
    Возвращает изменённую строку.
    """
    return s.replace(old, new)


def get_unique_characters(s):
    """
    Возвращает множество уникальных символов строки.
    """
    return set(s)


def to_uppercase(s):
    """
    Преобразует строку в верхний регистр.
    Ожидаемое поведение: вернуть строку в верхнем регистре.
    Ошибка: возвращает исходную строку без изменений.
    """
    return s  # Ошибка: нужно использовать s.upper()


def find_longest_word(s):
    """
    Находит самое длинное слово в строке.
    Возвращает строку с этим словом.
    """
    words = s.split()
    return max(words, key=len) if words else ''
