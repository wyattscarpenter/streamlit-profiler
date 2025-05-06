#!/usr/bin/env python3

from os import system as s, name as os_name
from sys import argv

if "-h" in argv or "--help" in argv:
  print("Just run this script to check the types.")
  exit()
def pause() -> None:
  input("Press enter to exit...")

def h(string: str) -> None:
  """Print a header for a typechecker section"""
  print(f"---- {string.upper()}:")

def hs(header: str, system_command: str) -> int:
  """Print a header, then run a system command (returning its return code)."""
  h(header)
  return s(system_command)

h("uv")
s("uv --version --verbose || pip install uv --disable-pip-version-check --break-system-packages")
print("Trying to install requirements.txt as a preemptive fallback in case there is no pyproject.toml...") 
s("uv pip install -r requirements.txt")
s("uv pip install ruff pyright mypy pytype pip")
# One of these next two lines will work, depending on your operating system...
if os_name == 'nt':
  s("set PYRIGHT_PYTHON_FORCE_VERSION=latest")
else:
  s("export PYRIGHT_PYTHON_FORCE_VERSION=latest")

hs("ruff", "uv run ruff check --no-cache")
hs("pyright", "uv run pyright")
h("mypy")
s("uv run mypy --install-types --non-interactive")
s("uv run mypy . --strict --pretty --warn-unreachable --strict-bytes")
h("pytype")
s("uv run pytype .")
print("---- fin")
pause()
