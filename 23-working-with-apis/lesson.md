# Working with APIs

An API is a documented way for programs to request information or actions from another service.

## What you will learn

An API is a documented way for programs to request information or actions from another service. A useful way to think about the idea is: An API is a menu of actions another program makes available over a network.

## Example

~~~python
import requests  # Install requests in an environment before running this example.
response = requests.get('https://api.github.com', timeout=10)  # Make a bounded network request.
response.raise_for_status()  # Turn an HTTP error status into an exception.
data = response.json()  # Decode JSON into Python values.
print(data.get('current_user_url'))  # Display one response field if present.
~~~

Read the comments and predict the output before running it: **A GitHub API URL is displayed.**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

APIs let programs exchange useful data through a defined agreement.

## Common mistakes

- Set a timeout
-  check status codes
-  network access and requests are required
-  never put tokens or passwords in code.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
