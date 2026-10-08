def greet(name):
    return f"Hello, {name}!"


def is_even(n):
    return n % 2 == 0


def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32


def sum_to(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def count_vowels(text):
    count = 0
    for ch in text.lower():
        if ch in "aeiou":
            count += 1
    return count


def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
