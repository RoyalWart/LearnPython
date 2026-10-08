# Decorators and Higher-Order Functions

A higher-order function accepts or returns another function; a decorator wraps behavior around a function.

## What you will learn

A higher-order function accepts or returns another function; a decorator wraps behavior around a function. A useful way to think about the idea is: A decorator is like a reusable jacket around a function.

## Example

~~~python
from functools import wraps  # Import a helper for preserving function details.
def announce(function):  # Accept a function as input.
    @wraps(function)  # Preserve its name and documentation.
    def wrapper(*args, **kwargs):  # Accept the original call arguments.
        print('Starting')  # Add behavior before the wrapped call.
        return function(*args, **kwargs)  # Return the wrapped result.
    return wrapper  # Give the new function back to the caller.
~~~

Read the comments and predict the output before running it: **Starting, then the wrapped function result**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

This pattern supports reusable timing, logging, caching, and other behavior without rewriting a function.

## Common mistakes

- Forward arguments and return values
-  decorators return functions
-  use functools.wraps for useful metadata.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
