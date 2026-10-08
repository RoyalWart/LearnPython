# Concurrency Basics

Concurrency lets tasks make progress while another task waits; async is useful for waiting-heavy work.

## What you will learn

Concurrency lets tasks make progress while another task waits; async is useful for waiting-heavy work. A useful way to think about the idea is: Concurrency is like putting another task on your schedule while one is waiting.

## Example

~~~python
import asyncio  # Import asynchronous task tools.
async def say_later(message):  # Define a coroutine that can pause.
    await asyncio.sleep(0.1)  # Yield control during the wait.
    print(message)  # Display the message after waiting.
async def main():  # Define the asynchronous entry point.
    await asyncio.gather(say_later('A'), say_later('B'))  # Run both waits together.
asyncio.run(main())  # Start the event loop.
~~~

Read the comments and predict the output before running it: **A and B appear after overlapping waits**. Then change one value and predict again. This is a simple problem-solving loop: understand the input, trace each step, and compare your prediction with the result.

## A clean-code comparison

~~~python
unclear = 5  # This name does not explain what the value means.
remaining_attempts = 5  # This name communicates the value's purpose.
~~~

Prefer clear names and small steps. When a program behaves unexpectedly, a readable version is easier to inspect and fix.

## Why does this matter?

Network and file waits can overlap, but concurrency does not automatically speed up heavy calculations.

## Common mistakes

- Use async with async-compatible libraries
-  blocking work still blocks
-  make task errors and lifetimes explicit.

## Problem-solving checkpoint

1. Restate what the program should do in one sentence.
2. Pick a tiny example and write down its expected result.
3. Trace the values one step at a time.
4. If the output differs, find the first step where your prediction changed.
5. Try a boundary case, not only the ordinary case.
