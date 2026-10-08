# Data Structures and Algorithms

A data structure organizes values and an algorithm describes steps for working with them.

## What you will learn

A data structure organizes values and an algorithm describes steps for working with them. A useful way to think about the idea is: A data structure is a container design; an algorithm is a recipe for using it.

## Example

~~~python
def find_name(names, target):  # Search a list for a requested name.
    for index, name in enumerate(names):  # Check each name in order.
        if name == target:  # Compare this item with the target.
            return index  # Stop as soon as it is found.
    return -1  # Report that no matching item exists.
print(find_name(['Ava', 'Bo'], 'Bo'))  # Search a small example list.
~~~

Read the comments and predict the output before running it: **1**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Choosing a suitable approach helps code stay understandable as data grows.

## Common mistakes

- Binary search requires sorted data
-  explain how work grows with input size
-  prefer the simplest suitable built-in operation.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
