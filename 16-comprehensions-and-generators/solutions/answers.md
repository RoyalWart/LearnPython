# Comprehensions and Generator Expressions — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
numbers = [1, 2, 3, 4]  # Store values to transform.
squares = [number * number for number in numbers]  # Make a list of squares.
even_squares = [value for value in squares if value % 2 == 0]  # Keep even squares.
print(even_squares)  # Display the filtered values.
~~~

## Exercise checks

### 🟢 EASY 1

Use a list comprehension to square 1 through 4.

**Expected example:** [1, 4, 9, 16]

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Filter the even squares from that list.

**Expected example:** [4, 16]

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Use a comprehension to uppercase a list of names.

**Expected example:** ['AVA', 'BO']

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Create a generator expression for numbers 1 through 3 and consume it once.

**Expected example:** 1 / 2 / 3

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Compare list and generator behavior with a large range without storing every result.

**Expected example:** Generator yields values one at a time

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

