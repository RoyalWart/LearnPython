# Virtual Environments and pip — answer guide

Try the exercises before reading this file. Your code can differ from these examples as long as it produces the expected behavior. Use the lesson example as a pattern, then trace your own values one step at a time.

## Model example from the lesson

~~~python
import sys  # Import interpreter information.
print(sys.executable)  # Show which Python interpreter is running.
print('Create an environment with: python -m venv .venv')  # Show the standard environment command.
print('Install with: python -m pip install requests')  # Use pip through this interpreter.
~~~

## Exercise checks

### 🟢 EASY 1

Create a virtual environment named .venv.

**Expected example:** The .venv folder exists

**Check:** Adapt the lesson example and compare every displayed value.

### 🟢 EASY 2

Show the activation command for Windows PowerShell.

**Expected example:** .venv\Scripts\Activate.ps1

**Check:** Change the requested input, then recalculate the result rather than changing the expected output by guesswork.

### 🟡 MEDIUM 3

Show the activation command for macOS or Linux.

**Expected example:** source .venv/bin/activate

**Check:** Test both cases separately and make sure each follows the intended branch or behavior.

### 🟡 MEDIUM 4

Install requests through the active Python interpreter.

**Expected example:** Package installs in the active environment

**Check:** Keep the operation in one function, pass its inputs explicitly, and call it with both sample values.

### 🔴 HARD 5

Record project dependencies in requirements.txt and keep .venv out of version control.

**Expected example:** requirements.txt is present; .venv is ignored

**Check:** This challenge has multiple valid solutions; verify each normal case and the boundary case.

