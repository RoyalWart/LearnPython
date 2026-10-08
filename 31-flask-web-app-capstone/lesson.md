# Build a Simple Web App with Flask

A web app handles browser requests and sends responses; Flask connects routes to Python functions.

## What you will learn

A web app handles browser requests and sends responses; Flask connects routes to Python functions. A useful way to think about the idea is: A web app is a conversation between a browser asking and a server answering.

## Example

~~~python
from flask import Flask  # Install Flask in an environment before running.
app = Flask(__name__)  # Create the application.
@app.route('/')  # Connect the home URL to the next function.
def home():  # Define a response handler.
    return 'Hello from Flask!'  # Send a response to the browser.
if __name__ == '__main__':  # Run only when this file is started directly.
    app.run(debug=True)  # Start a local development server.
~~~

Read the comments and predict the output before running it: **The browser displays Hello from Flask!**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

A small web app shows how Python logic can become accessible through a browser.

## Common mistakes

- Keep debug mode local only
-  validate user input
-  do not expose a development server as a public production app.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
