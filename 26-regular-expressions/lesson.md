# Regular Expressions

A regular expression is a pattern describing a shape of text to search for.

## What you will learn

A regular expression is a pattern describing a shape of text to search for. A useful way to think about the idea is: A regex is a stencil that matches text with a chosen shape.

## Example

~~~python
import re  # Import regular-expression helpers.
text = 'Order A-204 is ready'  # Store text containing a code.
match = re.search(r'[A-Z]-\d{3}', text)  # Find a letter, dash, and three digits.
if match:  # Check that the pattern matched.
    print(match.group())  # Display the matching text.
~~~

Read the comments and predict the output before running it: **A-204**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Patterns help find or validate repeated forms such as simple codes and dates.

## Common mistakes

- Use raw strings for patterns
-  choose simple checks for simple rules
-  test both matching and nonmatching samples.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
