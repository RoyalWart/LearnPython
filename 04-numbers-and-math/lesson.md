# Numbers and Math Operations

Arithmetic operators let you model calculations; parentheses make operation order explicit.

## What you will learn

Arithmetic operators let you model calculations; parentheses make operation order explicit. A useful way to think about the idea is: A math expression is a calculator recipe; parentheses group steps.

## Example

~~~python
total_minutes = 137  # Store a duration as a whole number of minutes.
hours = total_minutes // 60  # Find complete hours.
minutes = total_minutes % 60  # Find the leftover minutes.
print(hours, 'hours and', minutes, 'minutes')  # Display the converted duration.
~~~

Read the comments and predict the output before running it: **2 hours and 17 minutes**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Programs become useful when they calculate scores, budgets, time, distance, and measurements.

## Common mistakes

- Expect slash division to be an integer
-  ignore operator precedence
-  round too early in a multi-step calculation.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
