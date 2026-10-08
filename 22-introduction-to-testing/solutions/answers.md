# Introduction to Testing — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def double(number):  # Define the behavior to verify.
    return number * 2  # Return twice the input.
assert double(3) == 6  # Check an ordinary value.
assert double(0) == 0  # Check a boundary value.
print('All checks passed')  # This appears only if both assertions pass.
~~~

## Exercise checks

### 🟢 EASY 1

Write an assertion that double(3) equals 6.

**Expected example:** Assertion passes

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Add a boundary assertion that double(0) equals 0.

**Expected example:** Assertion passes

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Write a unittest test for double(-2).

**Expected example:** Expected result is -4

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Test a function with normal, boundary, and invalid inputs.

**Expected example:** All three cases are checked

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Create a small test suite for a function you wrote and run it twice.

**Expected example:** Same result on both runs

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

