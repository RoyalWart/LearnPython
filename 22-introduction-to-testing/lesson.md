# Introduction to Testing

A test is a small promise that your code should keep for a chosen input.

## What you will learn

A test is a small promise that your code should keep for a chosen input. A useful way to think about the idea is: A test is like a checklist that verifies one behavior.

## Example

~~~python
def double(number):  # Define the behavior to verify.
    return number * 2  # Return twice the input.
assert double(3) == 6  # Check an ordinary value.
assert double(0) == 0  # Check a boundary value.
print('All checks passed')  # This appears only if both assertions pass.
~~~

Read the comments and predict the output before running it: **All checks passed**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Tests catch regressions and make changes safer.

## Common mistakes

- Test ordinary and boundary values
-  keep tests repeatable
-  test behavior rather than private implementation details.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
