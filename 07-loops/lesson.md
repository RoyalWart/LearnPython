# Loops: for and while

A loop repeats an action for each value or while a condition remains true.

## What you will learn

A loop repeats an action for each value or while a condition remains true. A useful way to think about the idea is: A loop is a playlist that repeats tracks until it reaches the end or stop signal.

## Example

~~~python
total = 0  # Start a running total at zero.
for number in range(1, 5):  # Visit one through four.
    total += number  # Add the current number to the total.
print(total)  # Display the finished sum.
~~~

Read the comments and predict the output before running it: **10**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Loops power repeated work such as checking items, counting scores, and trying again.

## Common mistakes

- Expect range to include its final value
-  forget to update a while-loop condition
-  change a list while looping over it.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
