def damage(base, multiplier=1):
    return base * multiplier


def total(*nums):
    return sum(nums)


def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply


double = make_multiplier(2)
print(damage(10, multiplier=3))
print(total(1, 2, 3, 4))
print(double(21))
print(sorted(["pear", "fig", "banana"], key=lambda w: len(w)))
