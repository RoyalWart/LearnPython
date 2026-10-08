# Conditionals and Decisions

A condition evaluates to true or false and selects which block runs.

## What you will learn

A condition evaluates to true or false and selects which block runs. A useful way to think about the idea is: A conditional is a fork in a trail: each path depends on a true or false test.

## Example

~~~python
temperature = 18  # Store the current temperature.
if temperature >= 25:  # Check the warm range first.
    print('Wear light clothes.')  # Suggest a warm-weather choice.
elif temperature >= 15:  # Check the mild range next.
    print('Bring a light jacket.')  # Suggest a mild-weather choice.
else:  # Handle every lower temperature.
    print('Wear a warm coat.')  # Suggest a cold-weather choice.
~~~

Read the comments and predict the output before running it: **Bring a light jacket.**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Decisions let software respond differently to scores, choices, dates, and situations.

## Common mistakes

- Use one equals sign in a comparison
-  forget the colon or indentation
-  put a broad condition before a more specific one.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
