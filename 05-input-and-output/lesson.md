# User Input and Output

input asks a question and returns text; print displays a result.

## What you will learn

input asks a question and returns text; print displays a result. A useful way to think about the idea is: Input is a question at a counter, and the reply arrives as text.

## Example

~~~python
name = 'Mina'  # Use a sample reply without pausing for keyboard input.
name = name.strip()  # Remove accidental spaces around the reply.
print(f'Welcome, {name}!')  # Display a personalized message.
age_text = '16'  # Store digits as text, just like input returns.
age = int(age_text)  # Convert text to a whole number.
print(age + 1)  # Calculate and display the next number.
~~~

Read the comments and predict the output before running it: **Welcome, Mina! then 17**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Input lets a program respond to a person instead of repeating fixed output.

## Common mistakes

- Forget input returns text
-  convert invalid text without handling it
-  write vague prompts without saying what format to enter.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
