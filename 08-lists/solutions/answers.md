# Lists and List Operations — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
snacks = ['apple', 'toast']  # Make an ordered list.
snacks.append('yogurt')  # Add an item at the end.
first_snack = snacks[0]  # Read the first item at index zero.
print(first_snack, len(snacks))  # Display an item and the count.
~~~

## Exercise checks

### 🟢 EASY 1

Create a list of three hobbies and display the first one.

**Expected example:** drawing

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Append tea to a drinks list that starts with water.

**Expected example:** ['water', 'tea']

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Find the largest value in [7, 12, 9, 15].

**Expected example:** 15

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Keep only names longer than four letters from Mia, Rohan, Alexandra.

**Expected example:** ['Rohan', 'Alexandra']

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Create three to-dos, remove stretch as completed, and show what remains.

**Expected example:** ['read', 'draw']

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

