# 01 · Basics

## Variables and types
A variable is a name attached to a value.
```python
player = "Alex"      # str (text)
score = 120          # int (whole number)
speed = 3.5          # float (decimal)
alive = True         # bool (True/False)
```
Check a type with `type(score)`.

## Input and output
```python
name = input("Name? ")      # always returns a string!
print(f"Welcome, {name}")   # f-strings put values inside text
age = int(input("Age? "))   # convert with int(), float(), str()
```

## Conditionals
```python
if score >= 100:
    print("Level up!")
elif score >= 50:
    print("Almost")
else:
    print("Keep going")
```
Compare with `==  !=  <  >  <=  >=`. Combine with `and`, `or`, `not`.

## Loops
```python
for i in range(5):        # 0,1,2,3,4
    print(i)

health = 3
while health > 0:         # repeat while condition is True
    health -= 1
```
`break` exits a loop. `continue` skips to the next round.

## Useful operators
`+ - * /` normal · `//` floor divide · `%` remainder · `**` power

`%` is super useful: `n % 2 == 0` means n is even.

## Why this matters
Every program, from Minecraft to Instagram, is made of these pieces:
store data, make decisions, repeat things.

## Your turn
1. Run `python 01-basics/examples.py`. Change values and see what happens.
2. Open `exercises.py` and complete each function.
3. Check: `pytest 01-basics`
