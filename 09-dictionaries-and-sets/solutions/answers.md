# Dictionaries and Sets — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
player = {'name': 'Kai', 'score': 18}  # Map labels to player details.
player['score'] += 2  # Update the score under its key.
print(player.get('level', 1))  # Supply a default for a missing key.
visited = {'park', 'library', 'park'}  # Store unique places in a set.
print(len(visited))  # Display the count of unique places.
~~~

## Exercise checks

### 🟢 EASY 1

Create a pet dictionary with name Pixel and type cat; display its name.

**Expected example:** Pixel

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Remove duplicate colors from blue, red, blue.

**Expected example:** Two unique colors

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Count occurrences in red, blue, red.

**Expected example:** red: 2 / blue: 1

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Store item prices 2.5, 3, and 4; calculate the total.

**Expected example:** 9.5

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Find the shared interest in music/coding and coding/sport.

**Expected example:** coding

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

