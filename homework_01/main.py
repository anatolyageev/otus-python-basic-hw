"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [n ** 2 for n in args]


def even(args):
    return list(filter(lambda x: x % 2 == 0, args))


def odd(args):
    return list(filter(lambda x: x % 2 != 0, args))


def prime(args):
    return list(filter(prime_checker, args))


def prime_checker(num):
    if num <= 1:
        return False
    for n in range(2, int(num / 2 + 1)):
        if num % n == 0:
            return False
    else:
        return True


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

options = {EVEN: even,
           ODD: odd,
           PRIME: prime
           }


def filter_numbers(args, f_type=ODD):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    method = options[f_type]
    return method(args)

