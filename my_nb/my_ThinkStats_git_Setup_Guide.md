# ThinkStats Fresh Setup Guide

## 1. Fork the Repository on GitHub

1. Go to [https://github.com/AllenDowney/ThinkStats](https://github.com/AllenDowney/ThinkStats).
2. Click **Fork** in the top-right corner and create the fork under your account (`valentinissimo/ThinkStats`).

## 2. Clone Locally & Configure Remotes

```bash
# Navigate to your development folder and clone your fork (sets up 'origin')
cd ~/dev
git clone [https://github.com/valentinissimo/ThinkStats.git](https://github.com/valentinissimo/ThinkStats.git)
cd ThinkStats

# Add Allen Downey's original repository as 'upstream'
git remote add upstream [https://github.com/AllenDowney/ThinkStats.git](https://github.com/AllenDowney/ThinkStats.git)

# Verify remotes (origin -> your fork, upstream -> AllenDowney)
git remote -v

# Ensure you are on the v3 branch
git switch v3
```

## 3. Set Up the Python Environment (uv)

```bash
# Install production dependencies only (excludes black, pytest, jupyter-book, etc.)
uv sync --no-dev
```

## 4. Create the study Branch & Personal Workspace (my_nb)

```bash
# Create and switch to a new branch from v3
git switch -c study

# Copy the original notebooks into a personal folder to avoid future rebase conflicts
cp -r nb my_nb

# Stage, commit, and push your personal workspace to GitHub
git add my_nb
git commit -m "Add my_nb folder for personal exercises"
git push -u origin study
```

## 5. Future Syncing Workflow (Keeping study Up to Date)

```bash
# 1. Update your local v3 branch from upstream and sync to your fork
git switch v3
git pull upstream v3
git push origin v3

# 2. Rebase your study branch onto the updated v3
git switch study
git rebase v3
git push --force-with-lease origin study
```
