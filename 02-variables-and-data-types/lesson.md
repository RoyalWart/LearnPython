# Variables and Data Types

Variables are labeled containers; the value has a type such as text, integer, decimal, or boolean.

## What you will learn

Variables are labeled containers; the value has a type such as text, integer, decimal, or boolean. A useful way to think about the idea is: A variable label tells you what is in a container, and the type tells you what it can do.

## Example

~~~python
player_name = 'Mina'  # Store text with a descriptive name.
score = 12  # Store a whole-number score.
has_bonus = True  # Store a yes-or-no value.
score += 3  # Update the score by adding three.
print(player_name, score, has_bonus)  # Display the current values.
~~~

Read the comments and predict the output before running it: **Mina 15 True**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Good names and suitable types make program state easier to understand and prevent invalid operations.

## Common mistakes

- Confuse assignment with comparison
-  store a number as text when doing math
-  use a name before assigning it.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
