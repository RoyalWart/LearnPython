# Functions: Reusable Instructions — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def rectangle_area(width, height):  # Define a reusable area calculator.
    area = width * height  # Multiply the two input dimensions.
    return area  # Send the result to the caller.
print(rectangle_area(4, 5))  # Call the function and display its result.
~~~

## Exercise checks

### 🟢 EASY 1

Write double(number) that returns twice its input.

**Expected example:** double(6) -> 12

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Write make_greeting(name) that returns a friendly greeting.

**Expected example:** make_greeting('Lee') -> Hello, Lee!

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Return the larger of 4 and 9 from a function.

**Expected example:** 9

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Write is_adult(age) that returns True for 18 or older.

**Expected example:** is_adult(16) -> False

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Write average(scores), returning None for an empty list.

**Expected example:** average([10, 20, 30]) -> 20 / average([]) -> None

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

