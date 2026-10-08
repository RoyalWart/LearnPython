# Lists and List Operations

A list stores values in order and lets a program add, remove, or inspect them.

## What you will learn

A list stores values in order and lets a program add, remove, or inspect them. A useful way to think about the idea is: A list is a numbered shelf with items kept in order.

## Example

~~~python
snacks = ['apple', 'toast']  # Make an ordered list.
snacks.append('yogurt')  # Add an item at the end.
first_snack = snacks[0]  # Read the first item at index zero.
print(first_snack, len(snacks))  # Display an item and the count.
~~~

Read the comments and predict the output before running it: **apple 3**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Lists model playlists, to-do items, scores, and survey answers.

## Common mistakes

- Use length as a valid last index
-  expect append to return the changed list
-  remove items during iteration without a plan.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
