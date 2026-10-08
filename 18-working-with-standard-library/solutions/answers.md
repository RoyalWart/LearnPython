# Working with Python Libraries — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import math  # Import common math helpers.
import random  # Import random selection tools.
from datetime import date  # Import the date class.
print(math.sqrt(81))  # Calculate a square root.
print(date.today())  # Display today's date.
print(random.choice(['red', 'blue']))  # Choose one item at random.
~~~

## Exercise checks

### 🟢 EASY 1

Use math.sqrt to calculate the square root of 81.

**Expected example:** 9.0

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Use random.choice to select a color from a two-item list.

**Expected example:** red or blue

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Use datetime.date.today to display the current date.

**Expected example:** A date such as 2026-10-08

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Use os.path to check whether a sample file path exists.

**Expected example:** True or False

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Use sys.executable to display which Python interpreter is running.

**Expected example:** Path to active interpreter

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

