# User Input and Output — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
name = 'Mina'  # Use a sample reply without pausing for keyboard input.
name = name.strip()  # Remove accidental spaces around the reply.
print(f'Welcome, {name}!')  # Display a personalized message.
age_text = '16'  # Store digits as text, just like input returns.
age = int(age_text)  # Convert text to a whole number.
print(age + 1)  # Calculate and display the next number.
~~~

## Exercise checks

### 🟢 EASY 1

Ask for a favorite color and print a sentence containing it.

**Expected example:** Input teal -> Your favorite color is teal.

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Ask for a whole number and display it plus 10.

**Expected example:** Input 5 -> 15

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Ask for width 3 and height 6, then display rectangle area.

**Expected example:** Input 3 and 6 -> 18

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Ask for a name with extra spaces; trim and greet the person.

**Expected example:** Input two spaces Jo two spaces -> Hello, Jo!

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Create a two-question survey about snack and activity; display both answers.

**Expected example:** Snack: mango / Activity: cycling

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

