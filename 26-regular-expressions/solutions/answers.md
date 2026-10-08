# Regular Expressions — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import re  # Import regular-expression helpers.
text = 'Order A-204 is ready'  # Store text containing a code.
match = re.search(r'[A-Z]-\d{3}', text)  # Find a letter, dash, and three digits.
if match:  # Check that the pattern matched.
    print(match.group())  # Display the matching text.
~~~

## Exercise checks

### 🟢 EASY 1

Use re.search to find A-204 in a sentence.

**Expected example:** A-204

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Use re.findall to find all two-digit numbers in score 17 and level 4.

**Expected example:** ['17']

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Validate a simple three-digit code with a regex.

**Expected example:** Valid code matches; invalid does not

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Extract email-like text from a sample paragraph and discuss limits.

**Expected example:** Matching text is listed

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Write a regex for a format you choose and test valid and invalid examples.

**Expected example:** Both outcomes are reported

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

