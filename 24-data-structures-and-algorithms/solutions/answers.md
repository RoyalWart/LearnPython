# Data Structures and Algorithms — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def find_name(names, target):  # Search a list for a requested name.
    for index, name in enumerate(names):  # Check each name in order.
        if name == target:  # Compare this item with the target.
            return index  # Stop as soon as it is found.
    return -1  # Report that no matching item exists.
print(find_name(['Ava', 'Bo'], 'Bo'))  # Search a small example list.
~~~

## Exercise checks

### 🟢 EASY 1

Implement linear search for Bo in Ava, Bo, and return its index.

**Expected example:** 1

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Sort 7, 2, 5, 1 in ascending order.

**Expected example:** [1, 2, 5, 7]

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Use a set to check membership in a collection of visited places.

**Expected example:** True for park

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Implement binary search for 8 in a sorted list.

**Expected example:** Correct index or not found

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Compare linear and binary search growth and state why binary search needs sorted data.

**Expected example:** Linear checks grow with n; binary with log n

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

