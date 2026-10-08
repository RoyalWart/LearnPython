# Virtual Environments and pip

A virtual environment isolates one project's installed packages; pip installs packages into the active environment.

## What you will learn

A virtual environment isolates one project's installed packages; pip installs packages into the active environment. A useful way to think about the idea is: A virtual environment is a project's own toolbox, separate from other projects.

## Example

~~~python
import sys  # Import interpreter information.
print(sys.executable)  # Show which Python interpreter is running.
print('Create an environment with: python -m venv .venv')  # Show the standard environment command.
print('Install with: python -m pip install requests')  # Use pip through this interpreter.
~~~

Read the comments and predict the output before running it: **The program displays the active interpreter and setup commands.**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Isolation prevents one project's package updates from breaking another project.

## Common mistakes

- Activate the environment before installing
-  use python -m pip
-  do not commit the .venv directory.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
