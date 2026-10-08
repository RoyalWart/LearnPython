# Functions: Reusable Instructions

A function gives a reusable operation a name, inputs, and a result.

## What you will learn

A function gives a reusable operation a name, inputs, and a result. A useful way to think about the idea is: A function is a small machine: pass inputs in and receive a result back.

## Example

~~~python
def rectangle_area(width, height):  # Define a reusable area calculator.
    area = width * height  # Multiply the two input dimensions.
    return area  # Send the result to the caller.
print(rectangle_area(4, 5))  # Call the function and display its result.
~~~

Read the comments and predict the output before running it: **20**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Functions name steps, avoid copy-paste, and make individual parts easier to check.

## Common mistakes

- Define a function but never call it
-  confuse print with return
-  hide required inputs in global state.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
