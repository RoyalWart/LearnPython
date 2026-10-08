# Modules and Importing — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import math  # Load the standard-library math toolbox.
radius = 3  # Store a sample circle radius.
area = math.pi * radius ** 2  # Calculate area using pi.
print(round(area, 2))  # Display the result to two decimals.
~~~

## Exercise checks

### 🟢 EASY 1

Import math and display the square root of 144.

**Expected example:** 12.0

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Choose one snack from mango, toast, popcorn using random.choice.

**Expected example:** One listed snack

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Write add_tax(100) with ten percent tax.

**Expected example:** 110.0

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Use datetime to display today's date.

**Expected example:** A date such as 2026-10-08

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Split a calculator into a reusable helper and a main-guarded demo.

**Expected example:** Importing helpers does not run the demo

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

