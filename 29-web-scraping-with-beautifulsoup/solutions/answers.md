# Web Scraping with BeautifulSoup — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
from bs4 import BeautifulSoup  # Install beautifulsoup4 before running this example.
html = '<h1>Club News</h1><p>Meetup on Friday</p>'  # Use local sample markup.
soup = BeautifulSoup(html, 'html.parser')  # Parse the HTML structure.
heading = soup.find('h1')  # Find the first heading element.
print(heading.get_text())  # Extract readable text from the heading.
~~~

## Exercise checks

### 🟢 EASY 1

Parse local HTML containing one h1 and one paragraph.

**Expected example:** Club News

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Find all paragraph elements in a sample HTML string.

**Expected example:** Each paragraph text is listed

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Handle a missing h2 without crashing.

**Expected example:** Friendly missing-heading result

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Extract titles from a small local HTML sample using BeautifulSoup.

**Expected example:** All available titles appear

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a scraper for a permitted page, check missing fields, and explain rate limits.

**Expected example:** Records or a clear polite stop

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

