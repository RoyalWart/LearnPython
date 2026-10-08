# Error Handling

An exception signals an operation failed; try and except let you recover from expected problems.

## What you will learn

An exception signals an operation failed; try and except let you recover from expected problems. A useful way to think about the idea is: An exception is a smoke alarm; handle it without disabling every alarm.

## Example

~~~python
text = '42'  # Store text that represents a whole number.
try:  # Begin the operation that may fail.
    number = int(text)  # Attempt the conversion.
except ValueError:  # Handle the specific conversion problem.
    print('Please enter a whole number.')  # Explain how to recover.
else:  # Continue only when conversion worked.
    print(number + 1)  # Use the converted value.
~~~

Read the comments and predict the output before running it: **43**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

People mistype, files go missing, and data is incomplete; useful recovery makes programs easier to use.

## Common mistakes

- Catch every exception and hide bugs
-  put unrelated operations into a giant try block
-  silently ignore failures.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
