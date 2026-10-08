# Dictionaries and Sets

A dictionary maps keys to values; a set keeps unique values.

## What you will learn

A dictionary maps keys to values; a set keeps unique values. A useful way to think about the idea is: A dictionary is a labeled contact list; a set is a guest list with no duplicates.

## Example

~~~python
player = {'name': 'Kai', 'score': 18}  # Map labels to player details.
player['score'] += 2  # Update the score under its key.
print(player.get('level', 1))  # Supply a default for a missing key.
visited = {'park', 'library', 'park'}  # Store unique places in a set.
print(len(visited))  # Display the count of unique places.
~~~

Read the comments and predict the output before running it: **1 then 2**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

These structures model profiles, settings, inventory, tags, and unique identifiers.

## Common mistakes

- Read a missing key without a default
-  use a set when order matters
-  expect a set to support list indexing.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
