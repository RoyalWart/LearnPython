# SQLite Databases

SQLite stores structured rows in a database file or temporary in-memory database.

## What you will learn

SQLite stores structured rows in a database file or temporary in-memory database. A useful way to think about the idea is: A database is a filing cabinet and a table is one labeled drawer.

## Example

~~~python
import sqlite3  # Import SQLite support included with Python.
connection = sqlite3.connect(':memory:')  # Open a temporary practice database.
connection.execute('CREATE TABLE notes (text TEXT)')  # Create one text column.
connection.execute('INSERT INTO notes VALUES (?)', ('Learn SQL',))  # Insert safely with a placeholder.
rows = connection.execute('SELECT text FROM notes').fetchall()  # Read the rows.
print(rows)  # Display the query result.
connection.close()  # Close the database connection.
~~~

Read the comments and predict the output before running it: **[('Learn SQL',)]**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Databases make structured information searchable and persistent across program runs.

## Common mistakes

- Use placeholders instead of joining user text into SQL
-  commit changes to persistent databases
-  close connections when done.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
