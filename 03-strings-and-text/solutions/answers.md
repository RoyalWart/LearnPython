# Strings and Text — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
nickname = '  Samira  '  # Store text with extra spaces.
clean_name = nickname.strip()  # Return text without outside spaces.
first_letter = clean_name[0]  # Read the first character at index zero.
print(f'{first_letter}: Hi, {clean_name}!')  # Format a readable greeting.
~~~

## Exercise checks

### 🟢 EASY 1

Store The Wild Robot and display the title in uppercase.

**Expected example:** THE WILD ROBOT

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Trim outside spaces from the text two spaces, coding time, two spaces.

**Expected example:** coding time

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

For python, display the first two and last two characters.

**Expected example:** py / on

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Format Ari and 18 into the sentence Ari scored 18 points.

**Expected example:** Ari scored 18 points.

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Normalize the username with outside spaces and mixed case SunnyFox.

**Expected example:** sunnyfox

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

