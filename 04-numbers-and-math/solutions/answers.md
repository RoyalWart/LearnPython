# Numbers and Math Operations — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
total_minutes = 137  # Store a duration as a whole number of minutes.
hours = total_minutes // 60  # Find complete hours.
minutes = total_minutes % 60  # Find the leftover minutes.
print(hours, 'hours and', minutes, 'minutes')  # Display the converted duration.
~~~

## Exercise checks

### 🟢 EASY 1

Calculate the area of a rectangle with width 7 and height 4.

**Expected example:** 28

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Share 29 stickers equally among 4 friends; display each share and leftovers.

**Expected example:** 7 each, 1 left over

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Convert 155 minutes into hours and remaining minutes.

**Expected example:** 2 hours and 35 minutes

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Calculate a 15 percent tip on 20.00 and display tip and total to two decimals.

**Expected example:** 3.00 / 23.00

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Estimate travel time for 18 km at 12 km/h and round to two decimals.

**Expected example:** 1.5 hours

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

