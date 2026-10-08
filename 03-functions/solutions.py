def total(*nums):
    return sum(nums)


def apply_twice(f, x):
    return f(f(x))


def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


def build_profile(name, **details):
    profile = {"name": name}
    profile.update(details)
    return profile


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sort_by_length(words):
    return sorted(words, key=len)
