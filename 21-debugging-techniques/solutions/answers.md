# Debugging Techniques — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def average(numbers):  # Define a function that expects a number list.
    total = sum(numbers)  # Inspect the intermediate total.
    count = len(numbers)  # Inspect how many values were received.
    print(f'Debug: total={total}, count={count}')  # Display useful temporary evidence.
    return total / count  # Calculate the average.
print(average([2, 4, 6]))  # Run a small reproducible example.
~~~

## Exercise checks

### 🟢 EASY 1

Given a function that returns the wrong average, print total and count to inspect them.

**Expected example:** total=12, count=3

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Reproduce a division-by-zero bug with the smallest input.

**Expected example:** The error points to a zero denominator

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Fix one bug and verify the original example still works.

**Expected example:** Expected original result returns

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Read a traceback and identify its final exception type and line.

**Expected example:** Correct error type and source line named

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Debug a small program by stating a hypothesis, changing one thing, and recording the result.

**Expected example:** A short evidence-based debugging note

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

