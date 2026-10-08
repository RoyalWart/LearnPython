# 🐍 Complete Guide: Installing Python and pip

This guide takes you from "I have nothing installed" to "I can run Python code and install packages", on **Windows, macOS, or Linux**. Read the sections for your system and skip the others.

**How to use this guide**

1. Read [Part 1](#part-1-the-basics-what-are-we-installing) quickly so the words make sense.
2. Follow **only your operating system's** section in [Part 2](#part-2-install-python).
3. Run the checks in [Part 3](#part-3-verify-your-installation).
4. Learn pip in [Part 4](#part-4-pip-the-package-installer) and virtual environments in [Part 5](#part-5-virtual-environments).
5. If anything goes wrong, go to [Part 8: Troubleshooting](#part-8-troubleshooting). Almost every common problem is listed there.

---

## Table of contents

- [Part 1: The basics (what are we installing?)](#part-1-the-basics-what-are-we-installing)
- [Part 2: Install Python](#part-2-install-python)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [Part 3: Verify your installation](#part-3-verify-your-installation)
- [Part 4: pip, the package installer](#part-4-pip-the-package-installer)
- [Part 5: Virtual environments](#part-5-virtual-environments)
- [Part 6: Set up VS Code for Python](#part-6-set-up-vs-code-for-python)
- [Part 7: Set up this course's repo](#part-7-set-up-this-courses-repo)
- [Part 8: Troubleshooting](#part-8-troubleshooting)
- [Part 9: Upgrading and uninstalling](#part-9-upgrading-and-uninstalling)
- [Part 10: Quick reference and glossary](#part-10-quick-reference-and-glossary)

---

## Part 1: The basics (what are we installing?)

| Term | What it means |
|------|---------------|
| **Python** | The programming language. When you "install Python" you install the *interpreter*, the program that reads your `.py` files and runs them. |
| **pip** | Python's package installer. It downloads add-on libraries (called *packages*) written by other people, like `pytest` or `requests`. It comes bundled with Python. |
| **PyPI** | The Python Package Index at [pypi.org](https://pypi.org). The giant online store of packages that pip downloads from. |
| **Terminal** | A text window where you type commands. Also called *command line*, *shell*, or *console*. |
| **PATH** | A list of folders your computer searches when you type a command. If Python's folder isn't on PATH, typing `python` says "command not found". Many problems come from this. |
| **Virtual environment** | A private, disposable copy of Python's package space for one project. Explained in [Part 5](#part-5-virtual-environments). |

### Which Python version?

Install the **latest stable Python 3** from [python.org](https://www.python.org/downloads/). This course needs **Python 3.10 or newer**; 3.12 or newer is recommended.

> ⚠️ **Python 2 is dead.** If you see any tutorial using `print "hello"` (no brackets), it's Python 2. Ignore it.

### Opening a terminal

| System | How to open it |
|--------|----------------|
| **Windows** | Press the Windows key, type `PowerShell`, press Enter. (Or install **Windows Terminal** from the Microsoft Store.) |
| **macOS** | Press `Cmd + Space`, type `Terminal`, press Enter. |
| **Linux** | Press `Ctrl + Alt + T` (works on most distros), or search for "Terminal". |

> 💡 **Tip:** Anything in a gray code block in this guide that doesn't start with `>>>` is something you type in the terminal and then press **Enter**. Don't type the `$` or `>` symbol if you see one at the start of a line; it's just showing the prompt.

---

## Part 2: Install Python

### Windows

There are two ways. **Method A is recommended.**

#### Method A: Official installer (recommended)

1. Go to <https://www.python.org/downloads/>.
2. Click the big yellow **Download Python 3.x.x** button. This downloads an `.exe` file.
3. Double-click the downloaded file to start the installer.
4. **⚠️ CRITICAL STEP:** On the first screen, at the **bottom**, tick the box:

   **☑ Add python.exe to PATH**

   (Older installers word it "Add Python 3.x to PATH". Same thing.) If you forget this, Python will install but typing `python` in a terminal won't work. See [Troubleshooting](#python-is-not-recognized-as-an-internal-or-external-command-windows).

5. Click **Install Now** (the default option is fine; it installs for your user only and does not need administrator rights).
6. Wait for it to finish. On the last screen, if you see **"Disable path length limit"**, click it. It's harmless and avoids rare errors later. Then click **Close**.
7. **Close any terminal windows that were open**, then open a *new* one. (An already-open terminal won't know about the change.)
8. Continue to [Part 3: Verify](#part-3-verify-your-installation).

> ℹ️ The installer also installs the **`py` launcher**. On Windows you can type `py` instead of `python`. It's useful when you have several Python versions. Both are covered below.

#### Method B: Microsoft Store

1. Open the **Microsoft Store**, search **Python 3.12** (or newer), and install the one published by the **Python Software Foundation**.
2. Open a new PowerShell window and continue to [Part 3](#part-3-verify-your-installation).

The Store version works fine for learning, but it occasionally behaves differently with file paths and some tools. If you hit weird problems, uninstall it and use Method A.

#### Windows: one more thing about PowerShell

When you later try to activate a virtual environment, PowerShell may refuse with *"running scripts is disabled on this system"*. Fix it once, now:

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Type `Y` and press Enter if asked. This is safe: it lets you run scripts you created yourself, while still blocking unsigned scripts downloaded from the internet.

---

### macOS

macOS may include an old system Python or a stub that only prompts you to install developer tools. **Don't rely on it.** Install your own.

#### Method A: Official installer (recommended for beginners)

1. Go to <https://www.python.org/downloads/macos/> (or the main downloads page; it detects macOS).
2. Download the **macOS 64-bit universal2 installer** (a `.pkg` file).
3. Double-click it and click through: **Continue → Continue → Agree → Install**. Enter your Mac password if asked.
4. When it finishes, a Finder window may open. Find **`Install Certificates.command`** and **double-click it**. This lets Python make secure internet connections. (Skipping this causes the SSL error described in [Troubleshooting](#ssl-certificate-verify-failed-errors).) A terminal window flashes up, does its job, and you can close it.
5. Open a **new** Terminal window and continue to [Part 3](#part-3-verify-your-installation).

> ⚠️ **On macOS the command is `python3`, not `python`.** And pip is `pip3` (or better, `python3 -m pip`). Wherever this guide says `python`, use `python3` on a Mac. Inside a virtual environment, plain `python` works again (see Part 5).

#### Method B: Homebrew (for people comfortable with terminals)

Homebrew is a package manager for macOS. If you don't have it, install it from <https://brew.sh> (copy the one-line command from the site). Then:

```bash
brew install python
```

Homebrew keeps Python up to date with `brew upgrade python`.

---

### Linux

Most Linux distributions already include Python 3, but often **without pip and venv**. Install everything you need with your package manager. You'll be asked for your password; nothing shows as you type it, which is normal.

#### Debian, Ubuntu, Linux Mint, Pop!_OS, Raspberry Pi OS

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

> `python3-venv` is **essential** on Debian/Ubuntu. Without it, creating virtual environments fails with an *"ensurepip is not available"* error.

#### Fedora

```bash
sudo dnf install python3 python3-pip
```

#### Arch Linux / Manjaro

```bash
sudo pacman -S python python-pip
```

#### openSUSE

```bash
sudo zypper install python3 python3-pip
```

> ⚠️ **On Linux the command is `python3`, not `python`.** Use `python3` and `python3 -m pip` wherever this guide says `python` and `pip` (until you're inside a virtual environment, where plain `python` and `pip` work).

> ⚠️ **Never install Python packages system-wide with `sudo pip install`.** It can break parts of your operating system that depend on Python. Use virtual environments (Part 5). Modern Linux will actually block you with an "externally-managed-environment" error. See [Troubleshooting](#error-externally-managed-environment-linux-and-macos-homebrew).

#### Check your version is new enough

Run `python3 --version`. If it prints something older than 3.10, check whether your distro offers a newer one (for example `sudo apt install python3.12`), or ask for help in the repo.

#### ChromeOS (Chromebook)

Enable the **Linux development environment** in ChromeOS settings (Settings → Advanced → Developers → Linux development environment → Turn on). This gives you a Debian terminal; then follow the Debian/Ubuntu instructions above.

---

## Part 3: Verify your installation

Open a **new** terminal window (important! old windows don't see new installs) and run these checks.

### Check 1: Python's version

| System | Command |
|--------|---------|
| Windows | `python --version` (or `py --version`) |
| macOS / Linux | `python3 --version` |

✅ **Expected:** something like `Python 3.12.4` (any 3.10+ is fine).

### Check 2: pip's version

| System | Command |
|--------|---------|
| Windows | `python -m pip --version` |
| macOS / Linux | `python3 -m pip --version` |

✅ **Expected:** something like `pip 24.0 from C:\...\site-packages\pip (python 3.12)`.

> 💡 **Why `python -m pip` instead of just `pip`?** Writing `python -m pip` guarantees pip belongs to *that exact Python*. Plain `pip` might belong to a different Python on your computer, which causes the confusing "I installed it but Python can't find it" problem. **From now on, always use `python -m pip`.** (Inside an activated virtual environment, plain `pip` is safe too.)

### Check 3: Run Python interactively

Start the interactive mode (the *REPL*):

| System | Command |
|--------|---------|
| Windows | `python` |
| macOS / Linux | `python3` |

You'll see a `>>>` prompt. Try:

```python
>>> 2 + 2
4
>>> print("Hello, world!")
Hello, world!
>>> exit()
```

`exit()` (or `Ctrl+Z` then Enter on Windows, `Ctrl+D` on Mac/Linux) gets you back to the normal terminal.

### Check 4: Run a script file

1. Create a file named `hello.py` containing:

   ```python
   name = input("What's your name? ")
   print(f"Nice to meet you, {name}!")
   ```

2. In the terminal, go to the folder containing it (see the tip below), then run:

   | System | Command |
   |--------|---------|
   | Windows | `python hello.py` |
   | macOS / Linux | `python3 hello.py` |

✅ **Expected:** it asks for your name and greets you.

> 💡 **Moving around in the terminal**
>
> ```
> cd folder_name      # go into a folder
> cd ..               # go up one folder
> ls                  # list files (macOS/Linux/PowerShell)
> dir                 # list files (Windows; also works in PowerShell)
> pwd                 # show where you are (macOS/Linux/PowerShell)
> ```
>
> Tip: you can type the first few letters of a name and press **Tab** to auto-complete it.

### ✅ Installation checklist

- [ ] `python --version` (or `python3 --version`) shows 3.10 or higher
- [ ] `python -m pip --version` shows a pip version
- [ ] The REPL opens and `2 + 2` gives `4`
- [ ] `hello.py` runs

If all four pass, **Python is installed.** If any fail, go to [Part 8](#part-8-troubleshooting).

---

## Part 4: pip, the package installer

pip downloads and installs packages from PyPI. Packages are code other people wrote: data tools, web frameworks, game libraries, testing tools, and more.

> 📝 **Reminder:** use `python -m pip` on Windows, or `python3 -m pip` on macOS/Linux, when you're **outside** a virtual environment. Inside an activated virtual environment, `python -m pip` and `pip` both work. Examples below use `python -m pip`; substitute `python3` if that's your system.

### Everyday commands

| What you want | Command |
|---------------|---------|
| Install a package | `python -m pip install requests` |
| Install a specific version | `python -m pip install requests==2.31.0` |
| Install "at least" a version | `python -m pip install "requests>=2.31"` |
| Upgrade a package | `python -m pip install --upgrade requests` |
| Uninstall a package | `python -m pip uninstall requests` |
| List installed packages | `python -m pip list` |
| Show details about one package | `python -m pip show requests` |
| Install from a requirements file | `python -m pip install -r requirements.txt` |
| Save installed packages to a file | `python -m pip freeze > requirements.txt` |
| Upgrade pip itself | `python -m pip install --upgrade pip` |
| Get help | `python -m pip --help` |

> 💡 Put quotes around version specifiers containing `>` or `<` (like `"requests>=2.31"`). Otherwise the terminal treats `>` as "save output to a file".

### Try it: install and use a package

1. Install `requests` (a popular library for talking to websites):

   ```bash
   python -m pip install requests
   ```

   You'll see text scroll by, ending with `Successfully installed requests-...`.

2. Use it. Create `try_requests.py`:

   ```python
   import requests

   response = requests.get("https://api.github.com")
   print(response.status_code)   # 200 means success
   ```

3. Run it. You should see `200`.

If you get `ModuleNotFoundError: No module named 'requests'`, pip installed it for a *different* Python than the one running your script. See [Troubleshooting](#modulenotfounderror-after-pip-install-worked).

### Understanding requirements.txt

A `requirements.txt` is a plain text list of packages a project needs, one per line:

```text
pytest>=8.0
requests==2.31.0
```

Anyone can then install everything with a single command:

```bash
python -m pip install -r requirements.txt
```

This is how projects (including this course) tell you what to install. To create one for your own project after you've installed packages in your virtual environment:

```bash
python -m pip freeze > requirements.txt
```

### Where do packages come from, and can I trust them?

pip downloads from PyPI, where **anyone can upload anything**. Basic safety habits:

- ✅ Install packages that are well known, or recommended by your course, teacher, or a trusted tutorial.
- ✅ Double-check the spelling. Attackers publish look-alike names (`reqeusts` instead of `requests`).
- ✅ Check the package's page on pypi.org: release history, download numbers, link to its source code.
- ❌ Don't install a random package because a stranger in a chat or video told you to.
- ❌ Never run `sudo pip install` or run pip as administrator.

### Understanding pip's output

| Message | Meaning |
|---------|---------|
| `Collecting xyz` | Found it, downloading. |
| `Requirement already satisfied: xyz` | You already have it. Not an error. |
| `Successfully installed xyz-1.2.3` | ✅ Done. |
| `WARNING: You are using pip version X; however, version Y is available` | Just a notice. Upgrade pip when convenient (`python -m pip install --upgrade pip`). Not an error. |
| `ERROR: Could not find a version that satisfies the requirement xyz` | Misspelled name, or no internet, or the package doesn't support your Python version. |
| `ERROR: No matching distribution found` | Same family of problem as above. |

---

## Part 5: Virtual environments

### Why you need them

Imagine Project A needs `somelib` version 1 and Project B needs `somelib` version 2. If all packages live in one shared place, the two projects fight. A **virtual environment** (venv) gives each project its own private package space, so:

- Projects can't break each other.
- You can delete the environment and start fresh without touching anything else.
- Your system Python stays clean (important on Linux and macOS).
- You can share an exact list of required packages (`requirements.txt`).

**Rule: make one virtual environment per project. Always.**

### Create one

Open a terminal, go into your project folder, then run:

| System | Command |
|--------|---------|
| Windows | `python -m venv .venv` |
| macOS / Linux | `python3 -m venv .venv` |

This creates a folder called `.venv` containing a private copy of Python. (The name `.venv` is a common convention; any name works.)

### Activate it

Activating tells your terminal "use *this* project's Python and pip from now on".

| System / shell | Command |
|----------------|---------|
| **Windows, PowerShell** (the default) | `.venv\Scripts\Activate.ps1` |
| **Windows, Command Prompt (cmd)** | `.venv\Scripts\activate.bat` |
| **macOS / Linux (bash or zsh)** | `source .venv/bin/activate` |

✅ **How to know it worked:** your prompt now starts with `(.venv)`:

```text
(.venv) PS C:\Users\you\python-learning-repo>
```

While activated, **plain `python` and `pip` work on every operating system**, and they point at the venv.

Confirm which Python you're using:

| System | Command |
|--------|---------|
| Windows | `where python` |
| macOS / Linux | `which python` |

The first path listed should be inside your `.venv` folder.

### Use it

Install packages normally. They go into `.venv` only:

```bash
pip install pytest
python my_script.py
```

### Deactivate it

```bash
deactivate
```

The `(.venv)` marker disappears and you're back to your normal system Python.

### Delete it

A venv is disposable. Deactivate, then delete the `.venv` folder. Recreate it any time with the commands above plus `pip install -r requirements.txt`.

### Golden rules of venvs

1. **Activate every time you open a new terminal** to work on the project. The `(.venv)` marker tells you it's active. No marker = not active.
2. **Never copy or move a `.venv` folder.** It stores absolute paths. Recreate it instead.
3. **Never commit `.venv` to Git.** It's large and machine-specific. This course's `.gitignore` already excludes it.
4. If something installed "but isn't found", the first question is always: *"Is my venv activated?"*

---

## Part 6: Set up VS Code for Python

VS Code is a free, popular editor. Download it from <https://code.visualstudio.com/>.

### Install the Python extension

1. Open VS Code.
2. Click the **Extensions** icon in the left bar (four squares), or press `Ctrl+Shift+X` (`Cmd+Shift+X` on Mac).
3. Search **Python**.
4. Install the one by **Microsoft** (it has millions of installs).

### Open your project folder

**File → Open Folder…** and choose your project folder (for this course: `python-learning-repo`). Open the *folder*, not a single file. This lets VS Code see your `.venv`.

### Select the interpreter (very important!)

VS Code needs to know which Python to use.

1. Press `Ctrl+Shift+P` (`Cmd+Shift+P` on Mac) to open the Command Palette.
2. Type **Python: Select Interpreter** and press Enter.
3. Choose the one that mentions `.venv` (for example `Python 3.12.4 ('.venv')`).

If it isn't listed, choose **Enter interpreter path…** → **Find…** and select:
- Windows: `.venv\Scripts\python.exe`
- macOS / Linux: `.venv/bin/python`

### Run code

- Open a `.py` file and click the **▶ Run** button in the top right, **or**
- Use the built-in terminal: **Terminal → New Terminal** (`` Ctrl+` ``). If your interpreter is selected, VS Code usually activates the venv automatically in new terminals. Look for `(.venv)`.

### Quality-of-life tips

- **Auto-save:** File → Auto Save.
- **Format on save:** Settings → search "format on save".
- **Run a single test:** with the Python extension you can enable pytest from the Testing panel (flask icon). Command Palette → *Python: Configure Tests* → pytest.

---

## Part 7: Set up this course's repo

Once Python is installed and verified, do this once:

```bash
# 1. Get the code (replace with the real URL)
git clone <the repo URL>
cd python-learning-repo

# 2. Create the virtual environment
python -m venv .venv          # macOS/Linux: python3 -m venv .venv

# 3. Activate it
.venv\Scripts\Activate.ps1    # Windows PowerShell
source .venv/bin/activate     # macOS / Linux

# 4. Install the course tools
pip install -r requirements.txt

# 5. Test it works (failures are EXPECTED here, since you haven't done the exercises yet)
pytest 01-basics
```

(Run only the lines for your system. Lines 2-3 and the activation commands have a version for each OS.)

✅ **Success looks like:** pytest runs and reports failing tests mentioning `NotImplementedError`. That means everything is installed correctly and the exercises are waiting for you.

**Every time you come back to work on the course:**

1. Open a terminal in the `python-learning-repo` folder.
2. Activate the venv (the one command from step 3).
3. Work. Run `pytest 01-basics` etc.

---

## Part 8: Troubleshooting

Find your error message below. Each entry explains **why** it happens and **how to fix** it.

### "python is not recognized as an internal or external command" (Windows)

**Full message examples:** `'python' is not recognized...` · `The term 'python' is not recognized as the name of a cmdlet...`

**Why:** Python's folder isn't on PATH. Usually the *Add python.exe to PATH* box wasn't ticked, or you're using a terminal window opened *before* installing.

**Fix, in order of easiness:**

1. **Close all terminals, open a new one**, and retry.
2. Try the launcher: `py --version`. If this works, simply use `py` wherever the guide says `python` (for example `py -m venv .venv`, `py -m pip install ...`).
3. **Re-run the installer** (from python.org), choose **Modify** → Next → tick **Add Python to environment variables** → Install. Or choose **Repair** and tick the PATH box.
4. Manual fix: Start menu → search *"Edit environment variables for your account"* → select `Path` → **Edit** → **New**, and add both of these (adjust the version/username to match):

   ```text
   C:\Users\<you>\AppData\Local\Programs\Python\Python312\
   C:\Users\<you>\AppData\Local\Programs\Python\Python312\Scripts\
   ```

   Click OK on every window, then open a **new** terminal.

### Typing `python` opens the Microsoft Store (Windows)

**Why:** Windows has placeholder "app execution aliases" that hijack the `python` command when Python isn't properly on PATH.

**Fix:** Settings → **Apps → Advanced app settings → App execution aliases** (on some versions: *Apps & features → App execution aliases*). Turn **off** the entries named `python.exe` and `python3.exe`. Then make sure Python is installed with PATH ticked (see above), and open a new terminal.

### `python: command not found` (macOS / Linux)

**Why:** On these systems the command is `python3`. There is no plain `python` outside a virtual environment.

**Fix:** use `python3`. (Inside an activated venv, `python` works.) Optionally, on Debian/Ubuntu: `sudo apt install python-is-python3` adds a `python` alias.

### `pip` is not recognized / `pip: command not found`

**Why:** Same PATH problem, or the pip command isn't on PATH even though Python is.

**Fix:** Use `python -m pip ...` (Windows) or `python3 -m pip ...` (macOS/Linux) instead. This doesn't depend on PATH for pip. On Linux, if pip isn't installed at all: `sudo apt install python3-pip` (Debian/Ubuntu).

### `No module named pip`

**Fix:** Bootstrap pip with the built-in tool:

```bash
python -m ensurepip --upgrade        # macOS/Linux: python3 -m ensurepip --upgrade
```

On Debian/Ubuntu, if that says ensurepip is disabled: `sudo apt install python3-pip`.

### `ModuleNotFoundError` after pip install worked

**Example:** `ModuleNotFoundError: No module named 'requests'`, even though `pip install requests` said "Successfully installed".

**Why:** pip installed the package for **one Python**, but your script ran with **another**. Typical causes: virtual environment not activated; VS Code using a different interpreter than your terminal; plain `pip` belongs to a different Python than `python`.

**Fix checklist:**

1. Is your venv **activated** (do you see `(.venv)`)? If not, activate it and run the pip install again.
2. Always install with `python -m pip install <package>` so pip and Python match.
3. In VS Code, run **Python: Select Interpreter** and pick the `.venv` one.
4. Verify with: `python -m pip list` and look for the package.
5. Make sure you spelled the *import* correctly. Some packages have different install and import names (for example you `pip install pillow` but `import PIL`).

### `error: externally-managed-environment` (Linux, and macOS Homebrew)

**Why:** Modern Linux distributions and Homebrew protect the system Python so that pip can't accidentally break your OS (this is a rule called PEP 668). It's a safety feature, not a bug.

**Fix:** Use a virtual environment (Part 5). Inside an activated venv, pip works normally.

> ❌ Do **not** use `--break-system-packages` as a habit. It disables the protection and can damage your system. (It's okay inside throwaway containers, but not on your own computer.)

### `ensurepip is not available` / venv creation fails (Debian/Ubuntu)

**Fix:**

```bash
sudo apt install python3-venv
```

If it names a specific version, install that (for example `sudo apt install python3.12-venv`).

### "Running scripts is disabled on this system" (PowerShell activation)

**Why:** PowerShell blocks scripts by default.

**Fix (one time):**

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Or sidestep it: use Command Prompt (`cmd`) and run `.venv\Scripts\activate.bat`.

### `PermissionError` / "Access is denied" / `Permission denied` during pip install

**Why:** pip tried to write into a protected system folder.

**Fix:** Use a virtual environment (you own that folder). If you can't, `python -m pip install --user <package>` installs into your user folder. **Don't** use `sudo` or "Run as administrator" to force it.

### `SSL: CERTIFICATE_VERIFY_FAILED` errors

**Why:** Python can't validate secure website certificates.

**Fix:**
- **macOS (python.org install):** run **`Install Certificates.command`** (found in *Applications → Python 3.x*), then retry.
- **School/work networks:** some networks inspect encrypted traffic with their own certificate, which breaks this check. Try a home network or mobile hotspot, or ask the network admin.
- Make sure your computer's date and time are correct.

### pip is very slow, times out, or can't connect

- Check your internet.
- Retry (PyPI has occasional hiccups).
- Behind a proxy (school/work)? Ask the admin for the proxy address, then: `python -m pip install --proxy http://proxy:port <package>`.

### `ERROR: Could not find a version that satisfies the requirement ...`

- Check the **spelling** of the package name.
- Check that you have internet.
- A very new Python release may not yet be supported by some packages. Check the package's PyPI page ("Requires: Python ...") or use a slightly older Python for that project.
- Your pip may be very old: `python -m pip install --upgrade pip`.

### I have several Pythons and I'm confused

It's common. Find out which is which:

| System | Commands |
|--------|----------|
| Windows | `where python` · `py --list` |
| macOS / Linux | `which -a python3` |

To see what a given command actually runs:

```bash
python -c "import sys; print(sys.executable); print(sys.version)"
```

(Use `python3` on macOS/Linux outside a venv.) This prints the exact path and version. **Inside a venv, the path should include `.venv`.**

On Windows you can choose a version explicitly: `py -3.12 -m venv .venv`.

### The command prompt shows an old Python version

An older Python is earlier on your PATH. Use `py -3.12` (Windows), call the newer one by full name (`python3.12`), or recreate your venv with the Python you want.

### VS Code says "Import could not be resolved" (yellow squiggles) but the code runs

VS Code is looking at a different interpreter. Fix with **Python: Select Interpreter** (Part 6) and pick the `.venv` one. If it still complains, reload the window: Command Palette → *Developer: Reload Window*.

### `pytest: command not found`

pytest isn't installed in the active environment. Activate your venv and run `pip install -r requirements.txt`. Or run it as a module: `python -m pytest`, which also fixes most "pytest can't find my files" problems.

### `ModuleNotFoundError` for my *own* file

Python imports from the folder you run it in. Run scripts from the project root, check that file names don't clash with standard library names (don't name a file `random.py` or `test.py`), and check spelling and capitalization.

### I typed something and nothing seems to happen

If the terminal shows `...` or `>>>` unexpectedly, you're inside the Python REPL or in the middle of a multi-line statement. Press `Ctrl+C`, then type `exit()` to leave.

### Still stuck?

Copy the **full error message** (the last line says *what* went wrong; the lines above say *where*), note your operating system and Python version, and ask for help, either in an issue on this repo or by searching the exact error text online. Good questions include:

1. What you were trying to do
2. The exact command you ran
3. The full error
4. Output of `python --version` (or `python3 --version`) and `python -m pip --version`

---

## Part 9: Upgrading and uninstalling

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

### Upgrade Python

Python versions are installed **side by side**. A new minor version (3.12 → 3.13) is a separate install. Your old virtual environments keep using the old one.

1. Install the new version using Part 2.
2. Delete your project's `.venv`.
3. Recreate it with the new Python (`py -3.13 -m venv .venv` on Windows, `python3.13 -m venv .venv` on macOS/Linux) and reinstall: `pip install -r requirements.txt`.

Patch updates (3.12.3 → 3.12.4) replace the old one when you run the new installer.

### Uninstall packages

```bash
python -m pip uninstall <package>
```

To wipe everything for a project, delete `.venv` and recreate it.

### Uninstall Python

- **Windows:** Settings → Apps → Installed apps → Python 3.x → Uninstall. Also uninstall *Python Launcher* if listed.
- **macOS (python.org):** delete `/Library/Frameworks/Python.framework/Versions/3.x` and `/Applications/Python 3.x`. (Homebrew: `brew uninstall python`.)
- **Linux:** *Don't remove your system Python.* Parts of the OS depend on it. Only remove extra versions you installed yourself (for example `sudo apt remove python3.13`).

---

## Part 10: Quick reference and glossary

### Command cheat sheet

| Task | Windows | macOS / Linux |
|------|---------|---------------|
| Check Python version | `python --version` | `python3 --version` |
| Run a script | `python script.py` | `python3 script.py` |
| Open the REPL | `python` | `python3` |
| Create venv | `python -m venv .venv` | `python3 -m venv .venv` |
| Activate venv | `.venv\Scripts\Activate.ps1` | `source .venv/bin/activate` |
| Deactivate venv | `deactivate` | `deactivate` |
| Install package | `python -m pip install NAME` | `python3 -m pip install NAME` |
| Install from file | `python -m pip install -r requirements.txt` | `python3 -m pip install -r requirements.txt` |
| List packages | `python -m pip list` | `python3 -m pip list` |
| Save packages | `python -m pip freeze > requirements.txt` | `python3 -m pip freeze > requirements.txt` |
| Run tests | `python -m pytest` | `python3 -m pytest` |

*Inside an activated venv, use plain `python` and `pip` on every system.*

### Glossary

| Word | Meaning |
|------|---------|
| **Argument / flag** | An extra word after a command, like `--version` or `-m`. |
| **Interpreter** | The program that reads Python code and runs it. |
| **Module** | A single `.py` file you can `import`. |
| **Package** | A bundle of modules (often downloaded with pip). |
| **PATH** | The list of folders searched when you type a command. |
| **PEP** | *Python Enhancement Proposal*, a numbered design document (PEP 8 is the style guide). |
| **PyPI** | The online repository pip downloads from. |
| **REPL** | *Read-Eval-Print Loop*: the interactive `>>>` prompt. |
| **requirements.txt** | A text file listing a project's packages. |
| **Shell** | The program inside the terminal that reads your commands (PowerShell, bash, zsh). |
| **Standard library** | The modules that ship with Python itself, with no pip needed (`math`, `random`, `json`, `datetime`...). |
| **venv** | Virtual environment: a private package space for one project. |

### Links

- Download Python: <https://www.python.org/downloads/>
- Official Python tutorial: <https://docs.python.org/3/tutorial/>
- pip documentation: <https://pip.pypa.io/>
- Package search: <https://pypi.org/>
- VS Code: <https://code.visualstudio.com/>
- Git: <https://git-scm.com/downloads>

---

*You made it. Installing tools is honestly the most frustrating part of programming. Once this works, the fun starts. Head to `01-basics/README.md`.* 🚀