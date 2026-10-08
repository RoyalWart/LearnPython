# Contributing

Everyone here is learning. Contributions are welcome, including typo fixes.

## The workflow (this is how real teams work)

1. Fork the repo (or get added as a collaborator)
2. Make a branch: `git checkout -b add-lesson-files`
3. Make your changes
4. Run the tests: `CHECK_SOLUTIONS=1 pytest` (Windows PowerShell: `$env:CHECK_SOLUTIONS=1; pytest`)
5. Commit with a clear message: `git commit -m "Add file reading lesson"`
6. Push and open a Pull Request
7. A friend reviews it. Be kind, be specific, ask questions.

## Adding a lesson

Copy the structure of `01-basics/`:
`README.md`, `examples.py`, `exercises.py`, `test_exercises.py`, `solutions.py`

Rules of thumb:
- 20-30 minutes per lesson
- Use examples teens care about (games, music, sports, social media)
- Every exercise needs a test, and every test must pass against `solutions.py`
- Mark difficulty with ⭐ / ⭐⭐ / ⭐⭐⭐

## Code review checklist
- Does it run?
- Would a beginner understand the explanation?
- Are variable names clear?
- Do the tests pass?
