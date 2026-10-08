# Clean Code and PEP 8

Clean code uses names, formatting, and small functions to make intent visible.

## What you will learn

Clean code uses names, formatting, and small functions to make intent visible. A useful way to think about the idea is: Readable code is a map another person can follow.

## Example

~~~python
def calculate_average(scores):  # Use a descriptive snake_case function name.
    total = sum(scores)  # Give the intermediate value a meaningful name.
    count = len(scores)  # Keep the number of items visible.
    return total / count  # Return one clear result.
print(calculate_average([4, 8]))  # Display the average of two scores.
~~~

Read the comments and predict the output before running it: **6.0**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Clear code takes less effort to debug, explain, review, and safely change.

## Common mistakes

- Use descriptive names
-  keep functions focused
-  use consistent four-space indentation and readable line lengths.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
