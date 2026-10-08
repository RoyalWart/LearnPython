# Error Handling — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
text = '42'  # Store text that represents a whole number.
try:  # Begin the operation that may fail.
    number = int(text)  # Attempt the conversion.
except ValueError:  # Handle the specific conversion problem.
    print('Please enter a whole number.')  # Explain how to recover.
else:  # Continue only when conversion worked.
    print(number + 1)  # Use the converted value.
~~~

## Exercise checks

### 🟢 EASY 1

Convert valid text 8 to an integer and display it.

**Expected example:** 8

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Handle the text eight without crashing.

**Expected example:** Not a whole number

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Write safe_divide so dividing 9 by 0 returns None.

**Expected example:** None

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Try opening missing notes.txt and show a helpful message.

**Expected example:** Create notes.txt first.

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Distinguish blank input, invalid number text, and valid numeric text.

**Expected example:** A value is required / Enter a number / numeric value

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

