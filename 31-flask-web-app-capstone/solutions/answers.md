# Build a Simple Web App with Flask — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
from flask import Flask  # Install Flask in an environment before running.
app = Flask(__name__)  # Create the application.
@app.route('/')  # Connect the home URL to the next function.
def home():  # Define a response handler.
    return 'Hello from Flask!'  # Send a response to the browser.
if __name__ == '__main__':  # Run only when this file is started directly.
    app.run(debug=True)  # Start a local development server.
~~~

## Exercise checks

### 🟢 EASY 1

Create a Flask route at / that returns Hello from Flask!.

**Expected example:** Browser displays Hello from Flask!

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Add a /about route with a short response.

**Expected example:** About page text appears

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Use a route parameter to greet a name.

**Expected example:** /hello/Ari -> Hello, Ari!

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Return a clear 404 or friendly response for an unknown route.

**Expected example:** Not found response

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a tiny Flask app with two pages and a form that validates input locally.

**Expected example:** Valid and invalid inputs get different responses

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

