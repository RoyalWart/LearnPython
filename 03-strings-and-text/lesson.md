# Strings and Text

Strings are ordered text; indexes select characters and slices take a section.

## What you will learn

Strings are ordered text; indexes select characters and slices take a section. A useful way to think about the idea is: A string is a row of beads, and each index points to one bead.

## Example

~~~python
nickname = '  Samira  '  # Store text with extra spaces.
clean_name = nickname.strip()  # Return text without outside spaces.
first_letter = clean_name[0]  # Read the first character at index zero.
print(f'{first_letter}: Hi, {clean_name}!')  # Format a readable greeting.
~~~

Read the comments and predict the output before running it: **S: Hi, Samira!**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Text powers names, messages, search, and almost every human-facing part of a program.

## Common mistakes

- Forget that indexes start at zero
-  try to change a string character in place
-  compare user text without trimming or normalizing.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
