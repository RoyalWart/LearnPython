# 03 · Functions

A function is a reusable, named piece of code. Write once, use anywhere.

```python
def damage(base, multiplier=1):
    """Docstring: say what the function does."""
    return base * multiplier

damage(10)        # 10
damage(10, 3)     # 30
damage(10, multiplier=2)   # keyword argument
```

## Return vs print
`print` shows something on screen. `return` hands a value back to the
caller. Functions should usually **return**, so other code can use the result.

## Scope
Variables made inside a function stay inside it.

## *args and **kwargs
```python
def total(*nums):          # nums is a tuple of any number of arguments
    return sum(nums)

def profile(**details):    # details is a dict
    return details
```

## Functions are values
You can pass them around:
```python
def apply_twice(f, x):
    return f(f(x))

apply_twice(lambda n: n + 3, 10)   # 16
```
`lambda` makes a tiny one-line function.

## Closures: functions that make functions
```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
double(5)   # 10
```

## Recursion: a function that calls itself
Needs a **base case** to stop. `factorial(n) = n * factorial(n-1)`.

## Good habits
- One function, one job
- Clear names: `calculate_damage`, not `cd`
- Add a docstring

## Your turn
`pytest 03-functions`
