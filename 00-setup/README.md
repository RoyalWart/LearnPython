# 00 · Setup

You need four things: Python, an editor, Git, and a GitHub account.

## 1. Install Python
Download from <https://www.python.org/downloads/>.
**Windows:** tick **"Add Python to PATH"** during install.

Check it worked:
```
python --version      # on Mac/Linux you may need: python3 --version
```

## 2. Install VS Code
<https://code.visualstudio.com/>, then install the **Python** extension
(the one by Microsoft) from the Extensions tab.

## 3. Install Git
<https://git-scm.com/downloads>. Then tell Git who you are:
```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

## 4. Get this repo
```
git clone <the repo URL>
cd python-learning-repo
```

## 5. Make a virtual environment
A virtual environment is a private box of Python packages for one project,
so projects don't mess each other up.
```
python -m venv .venv
```
Activate it:
- Windows: `.venv\Scripts\activate`
- Mac/Linux: `source .venv/bin/activate`

You'll see `(.venv)` in your terminal. Now install the tools:
```
pip install -r requirements.txt
```

## 6. Check everything works
```
pytest 01-basics
```
You should see **failures**. That's correct! You haven't written the
answers yet. Time for [`01-basics`](../01-basics/README.md).

## Git cheat sheet
```
git status                 # what changed?
git add .                  # stage changes
git commit -m "message"    # save a snapshot
git push                   # upload to GitHub
git pull                   # download friends' changes
git checkout -b my-branch  # new branch
```
