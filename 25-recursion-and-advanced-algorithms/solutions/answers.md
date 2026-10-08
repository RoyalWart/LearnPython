# Recursion and Advanced Algorithms — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def countdown(number):  # Define a function that handles a smaller number each time.
    if number <= 0:  # Check the base case first.
        print('Go!')  # Handle the stopping point.
        return  # End this call.
    print(number)  # Display the current step.
    countdown(number - 1)  # Move toward the base case.
countdown(3)  # Start the recursive process.
~~~

## Exercise checks

### 🟢 EASY 1

Write countdown(3) with a base case at zero.

**Expected example:** 3 / 2 / 1 / Go!

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Write recursive factorial for 5.

**Expected example:** 120

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Use recursion to sum the nested list [1, [2, 3]].

**Expected example:** 6

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Trace recursive calls and identify the base case in a small function.

**Expected example:** Correct stopping call identified

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Compare a recursive and iterative solution for a larger input.

**Expected example:** Both return the same result

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

