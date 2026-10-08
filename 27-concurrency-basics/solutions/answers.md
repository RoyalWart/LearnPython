# Concurrency Basics — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import asyncio  # Import asynchronous task tools.
async def say_later(message):  # Define a coroutine that can pause.
    await asyncio.sleep(0.1)  # Yield control during the wait.
    print(message)  # Display the message after waiting.
async def main():  # Define the asynchronous entry point.
    await asyncio.gather(say_later('A'), say_later('B'))  # Run both waits together.
asyncio.run(main())  # Start the event loop.
~~~

## Exercise checks

### 🟢 EASY 1

Use asyncio.gather to run two short waiting tasks.

**Expected example:** Both task names appear

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Add a third asynchronous waiting task.

**Expected example:** Three names appear

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Explain which part of an async function yields control.

**Expected example:** The await expression

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Compare a blocking sleep with asyncio.sleep in two tasks.

**Expected example:** Async waits overlap; blocking waits delay

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Build a tiny async sequence with clear task names and handle one task error.

**Expected example:** Other task behavior is explained

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

