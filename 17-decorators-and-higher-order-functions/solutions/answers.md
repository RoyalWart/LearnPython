# Decorators and Higher-Order Functions — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
from functools import wraps  # Import a helper for preserving function details.
def announce(function):  # Accept a function as input.
    @wraps(function)  # Preserve its name and documentation.
    def wrapper(*args, **kwargs):  # Accept the original call arguments.
        print('Starting')  # Add behavior before the wrapped call.
        return function(*args, **kwargs)  # Return the wrapped result.
    return wrapper  # Give the new function back to the caller.
~~~

## Exercise checks

### 🟢 EASY 1

Write a higher-order function that calls a supplied function on 4.

**Expected example:** 16 when given a square function

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Create a decorator that prints Starting before a function runs.

**Expected example:** Starting appears first

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Ensure a decorator returns the wrapped function result.

**Expected example:** Wrapped result is 12

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Use functools.wraps and confirm the decorated name is preserved.

**Expected example:** Original function name remains visible

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a timing or logging decorator and demonstrate it on two functions.

**Expected example:** Both calls show the added behavior

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

