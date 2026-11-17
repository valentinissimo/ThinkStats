"""
my_env_setup.py - Environment & Path Setup Module for ThinkStats Notebooks

Why this module is necessary:
    Notebooks live in `nb/`, but raw datasets live in `data/`.
    Importing this module solves two distinct Python requirements simultaneously:
      1. sys.path modification -> Allows importing `.py` scripts (thinkstats.py, nsfg.py) from `nb/`.
      2. os.chdir modification -> Allows loading raw data files (2002FemPreg.dct, etc.) from `data/`.
"""

import os
import sys
from pathlib import Path

# Step 1: Anchor to the physical location of THIS file (`nb/` directory).
# Path(__file__) is absolute and permanent—it never changes regardless of 
# Jupyter's current working directory, kernel restarts, or cell order.
nb_dir = Path(__file__).resolve().parent

# Step 2: Locate the repo's `data/` directory relative to `nb/`
# (Goes up one level to project root, then down into `data/`).
data_dir = nb_dir.parent / "data"

# Step 3: Tell Python where to find MODULE IMPORTS (e.g., `import thinkstats`).
# `sys.path` is the list of directories Python searches for `.py` files.
# Adding `nb_dir` guarantees imports work even after changing working directory.
if str(nb_dir) not in sys.path:
    sys.path.insert(0, str(nb_dir))

# Step 4: Tell Python where to find RAW DATA FILES (e.g., `open("2002FemPreg.dct")`).
# `os.chdir` changes the working directory so bare default filenames in functions 
# like `read_stata()` resolve naturally inside `data/`.
if data_dir.is_dir():
    os.chdir(data_dir)