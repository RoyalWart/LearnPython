# Object-Oriented Programming

A class describes shared behavior and an object is one instance with its own state.

## What you will learn

A class describes shared behavior and an object is one instance with its own state. A useful way to think about the idea is: A class is a blueprint; each object is a thing built from that blueprint.

## Example

~~~python
class Pet:  # Define a blueprint for pet objects.
    def __init__(self, name):  # Set up each new pet.
        self.name = name  # Store state on this object.
    def greet(self):  # Define behavior for each pet.
        return f'Hi, I am {self.name}.'  # Use this object's own name.
print(Pet('Pip').greet())  # Create a pet and call its method.
~~~

Read the comments and predict the output before running it: **Hi, I am Pip.**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Classes help model related things that keep state and share behavior, such as game characters or pets.

## Common mistakes

- Use self for the current object
-  initialize each object's state in __init__
-  inherit only when there is a genuine shared relationship.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
