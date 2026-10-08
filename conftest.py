"""Shared test helper.

Tests get a fixture called `ex` that loads the lesson's exercises.py.
In CI (CHECK_SOLUTIONS=1) it loads solutions.py instead, so we know
the tests themselves are correct.
"""
import importlib.util
import os
from pathlib import Path

import pytest


@pytest.fixture
def ex(request):
    folder = Path(request.fspath).parent
    name = "solutions" if os.environ.get("CHECK_SOLUTIONS") else "exercises"
    path = folder / f"{name}.py"
    spec = importlib.util.spec_from_file_location(f"{folder.name}_{name}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
