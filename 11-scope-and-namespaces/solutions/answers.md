# Scope and Namespaces — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
tax_rate = 0.1  # Set a shared module-level configuration value.
def final_price(price):  # Receive price as a local parameter.
    tax = price * tax_rate  # Calculate a local value.
    return price + tax  # Return without changing global state.
print(final_price(20))  # Display the final price.
~~~

## Exercise checks

### 🟢 EASY 1

Use a function-local label and return it to the caller.

**Expected example:** ready

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Pass Nia into a greeting function instead of reading a global.

**Expected example:** Hi, Nia

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Refactor a discount calculation to accept price 100 and discount 0.2 as parameters.

**Expected example:** 80

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Call square with 3 and 5 and show both results.

**Expected example:** 9 / 25

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Rename a list variable called list so Python's built-in remains usable.

**Expected example:** sum([2, 4, 6]) -> 12

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

