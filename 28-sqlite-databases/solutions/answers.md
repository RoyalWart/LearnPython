# SQLite Databases — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import sqlite3  # Import SQLite support included with Python.
connection = sqlite3.connect(':memory:')  # Open a temporary practice database.
connection.execute('CREATE TABLE notes (text TEXT)')  # Create one text column.
connection.execute('INSERT INTO notes VALUES (?)', ('Learn SQL',))  # Insert safely with a placeholder.
rows = connection.execute('SELECT text FROM notes').fetchall()  # Read the rows.
print(rows)  # Display the query result.
connection.close()  # Close the database connection.
~~~

## Exercise checks

### 🟢 EASY 1

Create an in-memory SQLite table called notes.

**Expected example:** Table creation succeeds

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Insert Learn SQL using a parameter placeholder.

**Expected example:** One row is stored

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Select and display the text from notes.

**Expected example:** Learn SQL

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Update a row and commit it to a file-backed database.

**Expected example:** Updated value persists after reconnecting

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a small notes database with add, list, and safe parameterized search.

**Expected example:** Rows can be added, listed, and searched

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

