# Build a Simple CLI App

A command-line app is operated with typed choices and clear text feedback.

## What you will learn

A command-line app is operated with typed choices and clear text feedback. A useful way to think about the idea is: A CLI is a conversation through the terminal: the program asks and the person replies.

## Example

~~~python
def show_menu():  # Define one function for the app menu.
    print('1. Add task')  # Display the first action.
    print('2. List tasks')  # Display the second action.
    print('3. Quit')  # Display the exit action.
show_menu()  # Display the menu for the user.
~~~

Read the comments and predict the output before running it: **Three numbered actions are displayed.**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

A CLI capstone combines functions, input, validation, loops, and file storage into one usable tool.

## Common mistakes

- Plan the user flow first
-  validate choices
-  save data only after the basic workflow works.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
