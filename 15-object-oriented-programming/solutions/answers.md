# Object-Oriented Programming — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
class Pet:  # Define a blueprint for pet objects.
    def __init__(self, name):  # Set up each new pet.
        self.name = name  # Store state on this object.
    def greet(self):  # Define behavior for each pet.
        return f'Hi, I am {self.name}.'  # Use this object's own name.
print(Pet('Pip').greet())  # Create a pet and call its method.
~~~

## Exercise checks

### 🟢 EASY 1

Create a Pet class with a name and greet method; make Pip greet.

**Expected example:** Hi, I am Pip.

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Create two pet objects and show that their names are separate.

**Expected example:** Pip / Mo

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Add a method that increases a character's health by 5.

**Expected example:** Health rises by 5

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Create a base Animal and a Dog subclass with a speak method.

**Expected example:** Dog-specific sound appears

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Model a game character with health, a method to take damage, and a boundary at zero.

**Expected example:** Health never drops below zero

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

