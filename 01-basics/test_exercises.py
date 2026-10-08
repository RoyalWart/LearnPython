def test_greet(ex):
    assert ex.greet("Sam") == "Hello, Sam!"


def test_is_even(ex):
    assert ex.is_even(4) is True
    assert ex.is_even(7) is False
    assert ex.is_even(0) is True


def test_celsius_to_fahrenheit(ex):
    assert ex.celsius_to_fahrenheit(0) == 32
    assert ex.celsius_to_fahrenheit(100) == 212


def test_sum_to(ex):
    assert ex.sum_to(4) == 10
    assert ex.sum_to(100) == 5050
    assert ex.sum_to(0) == 0


def test_count_vowels(ex):
    assert ex.count_vowels("Python Rocks") == 2
    assert ex.count_vowels("AEIOU") == 5
    assert ex.count_vowels("xyz") == 0


def test_fizzbuzz(ex):
    assert ex.fizzbuzz(15) == "FizzBuzz"
    assert ex.fizzbuzz(9) == "Fizz"
    assert ex.fizzbuzz(10) == "Buzz"
    assert ex.fizzbuzz(7) == "7"
