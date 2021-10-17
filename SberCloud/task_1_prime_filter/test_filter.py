import pytest

def is_prime(number):
    """Проверка на простоту числа"""
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return number > 1

def filter_numbers(general_list):
    """Фильтр простых чисел"""
    return list(set(filter(is_prime, general_list)))


class TestPrimeFilter:

    def test_empty_list(self):
        numbers = []
        result = filter_numbers(numbers)
        assert result == []

    def test_non_prime_numbers(self):
        numbers = [4, 6, 8, 10, 12, 14, 15, 16, 18]
        result = filter_numbers(numbers)
        assert result == []

    def test_prime_number(self):
        numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        result = filter_numbers(numbers)
        assert result == numbers

    def test_different_number(self):
        numbers = [2, 4, 3, 5, 7, 12, 13, 16, 17]
        result = filter_numbers(numbers)
        assert result == [2, 3, 5, 7, 13, 17]