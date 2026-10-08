# Reading and Writing Files — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
with open('journal.txt', 'w', encoding='utf-8') as file:  # Open a UTF-8 file for writing.
    file.write('Today I learned about files.\n')  # Save a line of text.
with open('journal.txt', 'r', encoding='utf-8') as file:  # Reopen it for reading.
    saved_text = file.read()  # Read the saved text.
print(saved_text)  # Display the file contents.
~~~

## Exercise checks

### 🟢 EASY 1

Write Hello from a file! to hello.txt.

**Expected example:** File contains Hello from a file!

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Read hello.txt and display its contents.

**Expected example:** Hello from a file!

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Append a second diary line without replacing the first.

**Expected example:** Both diary lines remain

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Read a file one line at a time without extra blank lines.

**Expected example:** Each saved line appears once

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Load player.txt or show New player when the save is missing.

**Expected example:** Saved name or New player

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

