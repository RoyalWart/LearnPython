# Recursion and Advanced Algorithms

Recursion solves a problem by calling the same function on a smaller case until a stopping point.

## What you will learn

Recursion solves a problem by calling the same function on a smaller case until a stopping point. A useful way to think about the idea is: Recursion is like opening a smaller box inside each box until reaching the last one.

## Example

~~~python
def countdown(number):  # Define a function that handles a smaller number each time.
    if number <= 0:  # Check the base case first.
        print('Go!')  # Handle the stopping point.
        return  # End this call.
    print(number)  # Display the current step.
    countdown(number - 1)  # Move toward the base case.
countdown(3)  # Start the recursive process.
~~~

Read the comments and predict the output before running it: **3, then 2, then 1, then Go!**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

It is useful for nested structures and self-similar problems when each step clearly moves toward a base case.

## Common mistakes

- Write the base case first
-  ensure every call moves toward it
-  recursion depth limits very large inputs.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
