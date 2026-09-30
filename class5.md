# Weekly Announcements
* **Office Hours Request Link:** https://forms.gle/cQStrQGdnsVZYPgT7
* **MP 1** is posted on Canvas under **Assignments**.
    * MP 1 - Part 1 and Part 2 are available. 
* **MP1-WSU 2** is due TODAY (Friday, 9/25).
    

## MP1-WSU 2
If you’re ready and would like to complete it now, feel free to do so. 

---

# Class 5: Virtual Environments, Modules, and Exceptions

## Learning Objectives

By the end of today's class, you will be able to:

1. Use virtual environments to manage project-specific dependencies.
2. Organize related functions in a separate Python module and import them.
3. Distinguish between raising an exception in a utility function and handling it in the main program.

> Note: All exercises we do in class are expected to be completed inside the class-exercise directory. Please make sure to navigate there (e.g., `cd class-exercise`) before starting any coding practice during class.

---

# Part 1: Virtual Environments

## What Is a Virtual Environment? (quiz)

A Python virtual environment is a directory that contains:
- Its own copy of the Python interpreter
- Its own separate place to install packages (completely isolated from your computer's main Python)

When it's **activated**, your terminal temporarily "points" at this folder's Python and packages instead of your computer's global ones. When you **deactivate**, everything goes back to normal.


## Why Virtual Environments? (quiz)

**The problem:**

```bash
pandas==1.0
# Works for this project.

# Later, another project needs newer pandas.
pandas==7.0
# Now the first project might break.
```

**The solution:** Virtual environments separate environments per project. Virtual environments are like having separate toolboxes for each project. Installing pandas in Project A's toolbox doesn't affect Project B's toolbox.

## Creating a Virtual Environment

**Step 1 — Create the environment**

Inside the `class-exercise` folder, run the following command:

```bash
python -m venv venv
```

This creates a new folder named `venv` in your current directory. Nothing is activated yet — this step just builds the venv folder.

```bash
# Mac (Terminal): ls
# Windows (cmd.exe): dir
# Windows (PowerShell): ls  
```

**Step 2 — Activate it**

```bash
# Mac/Linux
source venv/bin/activate

# Windows (cmd.exe or PowerShell)
venv\Scripts\activate
```

**Step 3 — Confirm it's actually active**

Your prompt should now show `(venv)` at the start:

```bash
(venv) $
```

If you want to double-check which Python you're actually using:

```bash
# Mac/Linux
which python

# Windows
where python
```

It should point INSIDE your venv folder. If it does not point inside your `venv` folder, the environment isn't active — go back to Step 2.

**Step 4 — Install packages (only affects this environment)**

```bash
pip install pandas
pip install pyyaml
pip install dotenv
```

**Step 5 — Verify what's installed**

```bash
pip list
# Shows: pandas, numpy, ...
```

This list only contains what you've installed *in this venv* — not everything on your computer.

**Step 6 — Deactivate when you're done**

```bash
deactivate
```

Your prompt loses the `(venv)` prefix, and you're back to your computer's global Python.

## Requirements Files for Sharing

Your venv folder itself never gets committed to Git — so if your collaborator makes a copy of your repo, they don't get your packages. How do they know what to install?

**The solution:** `requirements.txt` — a plain text file listing every package (and exact version) your project needs. Anyone can use it to recreate your exact environment.

**Step 1 — Generate it from your active venv**

```bash
# Make sure venv is activated (you'll see (venv) in prompt)
(venv) $ pip freeze > requirements.txt
```

`pip freeze` lists every package currently installed *in your active venv*, with exact version numbers. The `>` redirects that list into a new file called `requirements.txt` instead of printing it to the screen.

**Step 2 — Look at what got generated**

**Example output:**

```text
dotenv==0.9.9
numpy==2.5.3
pandas==3.0.6
python-dateutil==2.9.0.post0
...
```

Notice `pandas` is there because you installed it — but so are `numpy`, `python-dateutil`, etc. Those are _dependencies_ pandas needs to work; `pip` pulled them in automatically, and `pip freeze` captures all of them, not just what you explicitly typed.

**Step 3 — Update `.gitignore`**

Your `class-exercise/.gitignore` file already contains `*.txt`, which ignores all text files. However, `requirements.txt` should be committed.

In the `.gitignore` file under `class-exercise`, update that section to:

```gitignore
# Ignore all text files except requirements.txt
*.txt
!requirements.txt
```

**Step 4 — Check and commit it to Git**

Unlike the `venv/` folder, `requirements.txt` should be committed because it is a small text file that tells others which packages to install.

```bash
git status
git add requirements.txt
git add .gitignore
git commit -m "Add requirements.txt"
```

Before committing, confirm that `requirements.txt` appears in `git status` but `venv/` does not.

**Step 5 — Someone else can now recreate your exact setup**

For example, 

```bash
# Create their own venv (their own venv folder, never yours)
python -m venv venv

# Activate vevn
source venv/bin/activate        # Mac/Linux
#OR
venv\Scripts\activate           # Windows

# Install the exact same packages and versions you had
pip install -r requirements.txt

# Now they have the same environment!
```

**Key idea:** `venv/` = never committed, recreated locally by each person. `requirements.txt` = always committed, tells everyone what to install.

---

# Part 2: Python Modules

A **module** is a Python file that contains related functions, classes, or variables. Other Python files can import and use them.


## Why Use Modules?

As a program grows, keeping all of the code in _one_ file becomes difficult to read and maintain.

```text
One large file                    Separate modules

program.py                        main.py
├── command-line arguments        └── controls the program
├── path functions
├── data functions                file_utils.py
└── main logic                    └── contains file functions
```

Separating code into modules helps you:

- Keep related functions together.
- Reuse functions in other programs.
- Test one part of a program at a time.
- Keep the main program easier to read.

## Example of Creating and Importing a Module

**message_utils.py**

```python
def create_message(name):
    return f"Hello, {name}!"
```

**main.py**

```python
from message_utils import create_message

message = create_message("Alice")
print(message)
```

When `main.py` runs, it looks for a file named `message_utils.py` and imports the `create_message()` function.


## Module-Level Loggers

Each module can create its own logger:

```python
import logging

logger = logging.getLogger(__name__)
```

The main program should configure logging once using `logging.basicConfig()`. Imported modules should use the _same_ configuration from the main program.

```text
main.py
└── logging.basicConfig(...)
└── logger = logging.getLogger(__name__)

utils_1.py
└── logger = logging.getLogger(__name__)

utils_2.py
└── logger = logging.getLogger(__name__)
```

Example:

```text
10:15:10 DEBUG    utils_1 — Reading data/data1.txt
10:15:10 DEBUG    utils_1 — Reading data/data2.txt
10:15:10 DEBUG    utils_2 — Checking missing values data/data1.txt
10:15:10 DEBUG    utils_2 — Checking missing values data/data2.txt
10:15:10 DEBUG    __main__ — Run data load 
```
---

# Part 3: Exceptions

A function may encounter a problem that it cannot resolve by itself (e.g., file not found / missing). When the problem occurs, it may not know whether the complete program should stop, ask for another file, or try something else.

When a function encounters a problem, there are two separate questions:
1. What went wrong?
2. What should the program do about it?

The function is usually responsible for answering the first question, while the calling code (e.g., main) decides the second.

In other words, the function should raise an exception and let the caller (e.g., main) decide what to do.

For example, suppose we have a function that requires a file to exist:

```python
def require_file(filepath):
    path = Path(filepath)

    if not path.is_file():
        #Log the error before raising the exception
        logger.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")

    return path
```

> Here, the function does not terminate the program (e.g. `sys.exit()`). It reports the problem by raising an exception.


## What Does raise Mean?

```
raise ...  → "Tell Python something went wrong."

print(...) → "Show this to the user."
logging    → "Record this information about what the program is doing."
```

When raise and except run like:
1. FileNotFoundError is _raised_.
    - The function stops immediately.
2. Python looks for an _except_ block that can handle the error.
    - If it reaches the top level without being handled, the program stops and Python prints a traceback.


## Handling an Exception (quiz)

The caller (main) should handle the error with `try` and `except`:

```python
# Using backup data
import sys

try:
    path = require_file("notes.txt")
except FileNotFoundError:
    # Try another file instead
    path = require_file("backup.txt")
```

OR

```python
# Terminating the program
import sys

try:
    path = require_file("notes.txt")
except FileNotFoundError as error:
    logger.error(f"Unable to continue: {error}")
    sys.exit(1)
```

This creates a clear separation:

| Location | Responsibility |
| :--- | :--- |
| Function | Detect the problem, log it, and raise an exception |
| Main program | Catch the exception and decide whether the program should stop |

## Common Exceptions

| Exception | Example |
| :--- | :--- |
| `FileNotFoundError` | A required file does not exist |
| `ValueError` | A value or option is unsupported |
| `TypeError` | A value has the wrong type |
| `KeyError` | A dictionary key does not exist |

Example of an unsupported value:

```python
def validate_mode(mode):
    supported_modes = ["quick", "full"]

    if mode not in supported_modes:
        logger.error(f"Unsupported mode: {mode}")
        raise ValueError(f"Unsupported mode: {mode}")

    return mode
```


In short:
* `raise` reports a problem to the caller.
* `try` marks code where an exception might occur.
* `except` handles a specific exception.
* `sys.exit()` terminates the application.
* A function generally should not decide to terminate the entire application.
* Catch specific exceptions when possible.
* Logging and raising serve different purposes.

---

# Try It Yourself — Build a File Inspector with Modules

## After completing this activity
* Raise your hand and check in with either me or a TA.
* Once we have confirmed that you have completed it, you may leave.

## Before You Start

1. Open your **`class-exercise`** folder.

Create or confirm the following files:

```text
class-exercise/
├── class5_file_utils.py
├── class5_file_inspector.py
└── data/
    └── notes.txt
```

You may add any sample text to `data/notes.txt` or leave it empty.

2. Activate venv

```bash
# Mac/Linux
source venv/bin/activate

# Windows (cmd.exe or PowerShell)
venv\Scripts\activate
```

## Task

Build a small command-line program using two Python modules.

- `class5_file_utils.py` will contain reusable file-related functions.
- `class5_file_inspector.py` will handle command-line input and control the program.
- The utility module should log and raise exceptions.
- The main program should catch the exceptions and decide when to exit.

**Complete the TODOs.**

### Step 1 — Complete `class5_file_utils.py`

```python
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


def inspect_file(filepath_str):
    """Return basic information about an existing file."""
    # TODO 1: Create a Path object.

    # TODO 2: If the path is not a file:
    #         Log an ERROR message.
    #         Raise FileNotFoundError (e.g. file not found).

    # TODO 3: Return a dictionary containing:
    #         name and extension.
    pass


def inspect_extension(file_info):
    """Confirm that the file uses a supported text extension."""
    supported_extension = ".txt"

    # TODO 4: If file_info["extension"] does not equal
    #         supported_extension:
    #         Log an ERROR message (e.g. unsupported format).
    #         Raise ValueError.

    # TODO 5: Return file_info.
    pass
```

### Step 2 — Complete `class5_file_inspector.py`

```python
import argparse
import logging
import sys

from class5_file_utils import inspect_file, inspect_extension

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Inspect a text file"
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Path to a .txt file"
    )
    args = parser.parse_args()

    # TODO 1: Call inspect_file() inside a try block.

    # TODO 2: Catch FileNotFoundError.
    #         Log an ERROR message (e.g. file not found), and 
    #         exit with sys.exit(1).

    # TODO 3: Call inspect_extension() inside a separate try block.

    # TODO 4: Catch ValueError.
    #         Log an ERROR message (e.g. unsupported format), and 
    #         exit with sys.exit(1).

    # TODO 5: Log an INFO message containing the
    #         file name and extension.


if __name__ == "__main__":
    main()
```

## Try These Commands

```bash
python class5_file_inspector.py --input data/notes.txt
python class5_file_inspector.py --input data/missing.txt
python class5_file_inspector.py --input class5_file_inspector.py
```

Expected successful output:

```text
10:15:02 INFO     __main__ — File: notes.txt, extension: .txt
```

Example missing-file output:

```text
10:15:10 ERROR    class5_file_utils — File not found: data/missing.txt
10:15:10 ERROR    __main__ — File doesn't exist: File not found: data/missing.txt
```

Example unsupported-extension output:

```text
10:15:20 ERROR    class5_file_utils — Unsupported text format: .py
10:15:20 ERROR    __main__ — Unsupported format: Unsupported text format: .py
```

## Save Your Work to GitHub

```bash
git status
git add class5_file_utils.py class5_file_inspector.py 
git commit -m "Practice modules and exception handling"
git push
```

---