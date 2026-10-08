# Set Up Python and Your Workspace

Python is the language and the interpreter follows your saved instructions.

## What you will learn

Python is the language and the interpreter follows your saved instructions. A useful way to think about the idea is: A Python file is a recipe card and the interpreter is the reader.

## Example

~~~python
message = 'Hello, Python!'  # Store a welcome message.
print(message)  # Display the saved message.
print(3 + 4)  # Calculate and display a result.
~~~

Read the comments and predict the output before running it: **Hello, Python! then 7**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Running a script lets you experiment independently and understand errors.

## Common mistakes

- Install Python but forget to reopen the terminal
-  run commands from the wrong folder
-  name your file after a standard module.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
