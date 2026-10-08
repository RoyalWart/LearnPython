# Debugging Techniques

Debugging is a process of gathering evidence, testing a theory, and narrowing a failure.

## What you will learn

Debugging is a process of gathering evidence, testing a theory, and narrowing a failure. A useful way to think about the idea is: Debugging is detective work: inspect clues before changing the whole program.

## Example

~~~python
def average(numbers):  # Define a function that expects a number list.
    total = sum(numbers)  # Inspect the intermediate total.
    count = len(numbers)  # Inspect how many values were received.
    print(f'Debug: total={total}, count={count}')  # Display useful temporary evidence.
    return total / count  # Calculate the average.
print(average([2, 4, 6]))  # Run a small reproducible example.
~~~

Read the comments and predict the output before running it: **Debug: total=12, count=3, then 4.0**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Debugging strengthens problem-solving and turns mistakes into useful information.

## Common mistakes

- Read the final traceback line
-  reproduce the smallest failing case
-  change one thing at a time and remove temporary debugging output later.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
