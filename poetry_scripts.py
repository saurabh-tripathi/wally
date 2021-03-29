#!/usr/bin/env python3
"""QA task code for poetry."""
import subprocess
import sys
from typing import List


def execute(name: str, command: List[str], failure_message: str) -> None:
    """
    Execute a command with output sent to the console.

    If exit code is non-zero will exit with non-zero and display the provided failure message.
    """
    print("--------------------------------------------------------------------------------")
    print(f"Running task: {name} ({command})")
    print("--------------------------------------------------------------------------------")
    completed_process = subprocess.run(command)
    if completed_process.returncode != 0:
        print("FAILURE")
        print(failure_message)
        sys.exit(1)


# The following section defines individual methods to run specific sub-tasks, used by poetry
# hooks given in the pyproject.toml file. Add new tasks to all() below as well.
def test() -> None:
    """Run all tests."""
    execute("test", ["pytest"], "Please fix the failing test.")


def format() -> None:
    """
    Run formatting checks.

    This routine runs any formatting checks. Failure message provides remediation instructions if available.
    """
    execute("format", ["isort", "--check-only", "."], 'Import ordering incorrect. Run "poetry run isort ." to fix.')
    execute("format", ["black", "--check", "."], 'Running "poetry run black ." will fix most issues.')


def lint() -> None:
    """Run linter checks."""
    execute("lint", ["flake8"], "Address any remaining flake8 issues manually.")


def type_check() -> None:
    """Run type checks."""
    execute(
        "type_check", ["mypy", "."], 'Mypy check failed. See above for errors, run "poetry run mypy ." to confirm fix.'
    )


def docs() -> None:
    """Run pydoc checks."""
    execute(
        "pydocstyle",
        ["pydocstyle", "."],
        'Pydoc issues found. Please correct, run "poetry run pydocstyle ." to confirm fix.',
    )


def unit() -> None:
    """Run all unit tests. These should be fast running with no external system dependencies."""
    execute("unit tests", ["pytest", "tests/unit"], "Please fix the failing test.")


# This routine runs all the defined tasks in order
def qa() -> None:
    """Run all qa checks.

    This routine runs all the defined tasks in order, except integration which requires some care for now because
    it calls Sagemaker Featurestore for real and requires permissions.
    """
    format()
    lint()
    type_check()
    test()
    docs()
    unit()


if __name__ == "__main__":
    qa()
