# Reading and Writing Files

A file stores information beyond a program run; use with so it closes safely.

## What you will learn

A file stores information beyond a program run; use with so it closes safely. A useful way to think about the idea is: A file is a notebook that stays on your desk after the program stops.

## Example

~~~python
with open('journal.txt', 'w', encoding='utf-8') as file:  # Open a UTF-8 file for writing.
    file.write('Today I learned about files.\n')  # Save a line of text.
with open('journal.txt', 'r', encoding='utf-8') as file:  # Reopen it for reading.
    saved_text = file.read()  # Read the saved text.
print(saved_text)  # Display the file contents.
~~~

Read the comments and predict the output before running it: **Today I learned about files.**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Files let programs remember notes, settings, and results without a database.

## Common mistakes

- Use write mode when you meant to preserve old content
-  omit a text encoding
-  look for a relative path in the wrong folder.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
