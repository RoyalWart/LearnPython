# Conditionals and Decisions — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
temperature = 18  # Store the current temperature.
if temperature >= 25:  # Check the warm range first.
    print('Wear light clothes.')  # Suggest a warm-weather choice.
elif temperature >= 15:  # Check the mild range next.
    print('Bring a light jacket.')  # Suggest a mild-weather choice.
else:  # Handle every lower temperature.
    print('Wear a warm coat.')  # Suggest a cold-weather choice.
~~~

## Exercise checks

### 🟢 EASY 1

Print big for 12 and small for 4 using a threshold of 10.

**Expected example:** big / small

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Check whether 7 is even or odd.

**Expected example:** odd

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Convert score 84 into bands: 90+ A, 80+ B, 70+ C, otherwise practice.

**Expected example:** B

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Allow entry only when age is 15 or older and permission is True.

**Expected example:** allowed

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Create a three-choice weather helper that gives advice and handles unknown choices.

**Expected example:** Valid choices show advice; unknown choice asks for a valid option

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

