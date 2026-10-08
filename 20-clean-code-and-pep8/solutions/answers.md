# Clean Code and PEP 8 — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def calculate_average(scores):  # Use a descriptive snake_case function name.
    total = sum(scores)  # Give the intermediate value a meaningful name.
    count = len(scores)  # Keep the number of items visible.
    return total / count  # Return one clear result.
print(calculate_average([4, 8]))  # Display the average of two scores.
~~~

## Exercise checks

### 🟢 EASY 1

Rename vague variables x and y in a rectangle program.

**Expected example:** width and height

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Format a function with four-space indentation and a descriptive name.

**Expected example:** Readable, consistently indented function

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Split a long calculation into named intermediate steps.

**Expected example:** Each step has a meaningful name

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Refactor duplicated greeting code into one function.

**Expected example:** One function handles both names

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Review a small script and make a checklist of three readability improvements.

**Expected example:** Three specific improvements listed

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

