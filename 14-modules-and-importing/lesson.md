# Modules and Importing

A module is a Python file or library that supplies reusable tools through import.

## What you will learn

A module is a Python file or library that supplies reusable tools through import. A useful way to think about the idea is: A module is a toolbox; import brings selected tools into the program.

## Example

~~~python
import math  # Load the standard-library math toolbox.
radius = 3  # Store a sample circle radius.
area = math.pi * radius ** 2  # Calculate area using pi.
print(round(area, 2))  # Display the result to two decimals.
~~~

Read the comments and predict the output before running it: **28.27**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Modules organize growing projects and let you reuse the Python standard library.

## Common mistakes

- Name your file after a module you need
-  use import star and obscure where names came from
-  run demonstration code during every import.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
