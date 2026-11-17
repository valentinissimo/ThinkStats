# Keeping forked v3 clean and updated with origin/v3.

**Fork workflow convention:** `origin` = your fork, `upstream` = their repo (the original repo I forked from).

Local set-up:

v3
├── notebooks from Allen Downey
└── stays close to upstream

study (branch)
├── inherits latest v3
└── has folder my_nb which include copy of folder nb

Copying nb to folder my_nb avoids that my exercises create merge conflicts later: `cp -r nb my_nb`

v3 is clean, the routine to keep it a pure mirror of the original repo, when the original repo `upstream` gets new commits is: git fetch upstream v3, git switch v3, git merge --ff-only upstream/v3, git push origin v3, then git switch study and rebase or merge. Remember that a rebase of study now needs a force-push, since it’s on your fork:

**With merge**

```bash
git fetch upstream v3
git switch v3
git merge --ff-only upstream/v3    # refuses instead of making a merge commit,
                                   # so it doubles as a "v3 is still clean" check
git push origin v3                 # optional: keeps your fork's v3 in sync
git switch study
git merge v3                       # brings the new upstream commits into study
git push                           # plain push, no force needed
```

**With rebase (recommended)**

```bash
git fetch upstream v3
git switch v3
git merge --ff-only upstream/v3    # refuses instead of making a merge commit,
                                   # so it doubles as a "v3 is still clean" check
git push origin v3                 # optional: keep your fork in sync on origin
git switch study
git rebase v3                      # replays your study commits on top of the updated v3
git push --force-with-lease        # a rebase rewrites your study commits,
                                   # so the next push to origin/study will be rejected.
                                   # The safer way to force it is with --force-with-lease
```

Rebasing study is fine by the guide’s rule since it’s only yours. But if you’ve pushed study to your fork, a rebase needs a force-push afterwards, while a merge doesn’t.

**Compare the two methods**

|           | Merge (your choice)                 | Rebase (this alternative)                                                 |
| --------- | ----------------------------------- | ------------------------------------------------------------------------- |
| On study  | git merge v3                        | git rebase v3                                                             |
| Then      | git push                            | git push --force-with-lease                                               |
| History   | One merge commit, nothing rewritten | Linear, but your study commits get new hashes                             |
| Conflicts | Resolved once, in one go            | Possibly once per replayed commit, each followed by git rebase --continue |

# Set-up Environment

Add `import my_env_setup` at the beginning of each chapter, in the first cell I will execute.

## Code for my_env_setup.py

```python
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
```
