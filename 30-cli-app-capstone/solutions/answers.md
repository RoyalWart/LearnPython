# Build a Simple CLI App — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
def show_menu():  # Define one function for the app menu.
    print('1. Add task')  # Display the first action.
    print('2. List tasks')  # Display the second action.
    print('3. Quit')  # Display the exit action.
show_menu()  # Display the menu for the user.
~~~

## Exercise checks

### 🟢 EASY 1

Display a CLI menu with Add, List, Quit.

**Expected example:** Three menu choices appear

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Read a choice and handle an unknown command.

**Expected example:** Helpful invalid-choice message

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Add one task and list it in the same run.

**Expected example:** The task appears in the list

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Save and reload tasks using a text file.

**Expected example:** Saved tasks return after restart

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a CLI to-do app with add/list/complete/quit, validation, and persistence.

**Expected example:** Each command produces a clear response

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

