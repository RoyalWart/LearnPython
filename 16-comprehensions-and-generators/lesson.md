# Comprehensions and Generator Expressions

A comprehension builds a collection from an iterable; a generator yields values one at a time.

## What you will learn

A comprehension builds a collection from an iterable; a generator yields values one at a time. A useful way to think about the idea is: A comprehension is a compact recipe; a generator is a dispenser that gives one item when asked.

## Example

~~~python
numbers = [1, 2, 3, 4]  # Store values to transform.
squares = [number * number for number in numbers]  # Make a list of squares.
even_squares = [value for value in squares if value % 2 == 0]  # Keep even squares.
print(even_squares)  # Display the filtered values.
~~~

Read the comments and predict the output before running it: **[4, 16]**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

These tools express clear transformations without hiding the steps.

## Common mistakes

- Keep each comprehension simple
-  use a regular loop for complex logic
-  generators are consumed as they are iterated.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
