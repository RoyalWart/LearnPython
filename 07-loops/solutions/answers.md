# Loops: for and while — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
total = 0  # Start a running total at zero.
for number in range(1, 5):  # Visit one through four.
    total += number  # Add the current number to the total.
print(total)  # Display the finished sum.
~~~

## Exercise checks

### 🟢 EASY 1

Use a for loop to print numbers 1 through 5.

**Expected example:** 1 / 2 / 3 / 4 / 5 on separate lines

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Use a loop to add the numbers 1 through 4.

**Expected example:** 10

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Count vowels in adventure.

**Expected example:** 4

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Use a while loop to count from 1 through 3.

**Expected example:** 1 / 2 / 3 on separate lines

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Print the 4-times table from 1x through 5x.

**Expected example:** 4 / 8 / 12 / 16 / 20

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

