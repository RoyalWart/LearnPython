# Scope and Namespaces

Scope controls where a name is available; function parameters and returns make data flow visible.

## What you will learn

Scope controls where a name is available; function parameters and returns make data flow visible. A useful way to think about the idea is: A namespace is a room with labeled drawers; local names belong to one room.

## Example

~~~python
tax_rate = 0.1  # Set a shared module-level configuration value.
def final_price(price):  # Receive price as a local parameter.
    tax = price * tax_rate  # Calculate a local value.
    return price + tax  # Return without changing global state.
print(final_price(20))  # Display the final price.
~~~

Read the comments and predict the output before running it: **22.0**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Clear scope prevents mysterious bugs and makes functions reusable with different inputs.

## Common mistakes

- Assume function-local names exist outside
-  change a global from many places
-  reuse a built-in name such as sum.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
