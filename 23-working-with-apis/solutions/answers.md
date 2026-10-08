# Working with APIs — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import requests  # Install requests in an environment before running this example.
response = requests.get('https://api.github.com', timeout=10)  # Make a bounded network request.
response.raise_for_status()  # Turn an HTTP error status into an exception.
data = response.json()  # Decode JSON into Python values.
print(data.get('current_user_url'))  # Display one response field if present.
~~~

## Exercise checks

### 🟢 EASY 1

Use requests with a timeout to fetch a public JSON endpoint.

**Expected example:** A JSON response is received when online

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Check the HTTP status before reading the response body.

**Expected example:** Success continues; HTTP failure raises an error

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Decode JSON and safely read an optional field with get.

**Expected example:** Field value or None

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Handle a request timeout and display a helpful message.

**Expected example:** Request timed out message

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a small API reader that validates status, timeout, JSON shape, and missing fields.

**Expected example:** Useful output or clear error message

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

