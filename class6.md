
## Weekly Announcements

* **Office Hours Request Link:** https://forms.gle/cQStrQGdnsVZYPgT7
* **MP 1** is posted on Canvas under **Assignments**.
    * MP 1 - Parts 1-3 are available. 
* **MP1-WSU 3** is due on Friday (10/2) and will be available the night before.


> WSU 2: Great progress, everyone!!!

---
# Class 6: Pandas Basics and Basic Cleaning

## Learning Objectives

By the end of today's class, you will be able to:

1. Load and inspect tabular data using pandas.
2. Select columns and filter rows using conditions.
3. Detect and remove duplicate rows.
4. Detect missing values and remove rows or columns containing them.

> Note: All exercises we do in class are expected to be completed inside the `class-exercise` directory. Please make sure to navigate there (e.g., `cd class-exercise`) before starting any coding practice during class. Also make sure your virtual environment is active before running Python or installing packages.

---

# Part 1: Pandas

## What Is Pandas?

Pandas is a Python library for working with tabular data.

```text
DataFrame = a two-dimensional table
Series    = one column from a DataFrame
```

A DataFrame is similar to a spreadsheet:

```text
Index | title          | type    | release_year
----- | -------------- | ------- | ------------
0     | Example Movie  | Movie   | 2022
1     | Example Show   | TV Show | 2020
2     | Another Movie  | Movie   | 2018
```

Each column is a Series:

```python
print(type(df)) 
# <class 'pandas.core.frame.DataFrame'>
print(type(df["title"]))
# <class 'pandas.core.series.Series'>
```

## Loading a CSV File Using Pandas

Place the `messy_netflix_titles.csv` dataset in the `data/` directory.

```python
from pathlib import Path

import pandas as pd

data_path = Path("data") / "messy_netflix_titles.csv"
df = pd.read_csv(data_path)
```

---

# Part 2: Inspecting a DataFrame (quiz)

Before analyzing a dataset, _observe_ them -- first understand its size, columns, and data types. You may notice missing or inconsistent values in this dataset.

```python
print(df.shape) # returns (number of rows, number of columns)

#You can access each value separately
rows = df.shape[0]
columns = df.shape[1]

print(df.head()) # displays the first five rows by default.
print(df.head(10)) # displays the first ten rows.
print(df.tail()) # displays the last five rows.

print(list(df.columns)) # displays the list of column names.

df.info() # displays Column names, Non-null counts, Data types, and Memory usage

print(df.describe()) # displays the summary of numeric columns.
# or print(df["release_year"].describe())

print(df.sample(5)) # randomly selects 5 samples
# or print(df.sample(5, random_state=1))
```

## First Look Checklist

When opening an unfamiliar dataset, a useful first sequence is:

```python
print(df.shape) 
print(df.head())
print(df.columns) 
print(df.dtypes) 
df.info() 
print(df.describe())
```

### Check Whether a Column Is Numeric

Use `pd.api.types.is_numeric_dtype()` to check whether a column contains a numeric data type.

```python
print(df.dtypes)

is_numeric = pd.api.types.is_numeric_dtype(df["viewer_score"])
print(is_numeric)
is_numeric = pd.api.types.is_numeric_dtype(df["title"])
print(is_numeric)
```

---

# Part 3: Selecting Data

## Selecting One Column

```python
titles = df["title"]

print(titles.head())
print(type(titles))
```

Selecting one column returns a Series.

## Selecting Multiple Columns

```python
selected = df[["title", "type"]]

print(selected.head())
print(type(selected))
```

Selecting multiple columns returns a DataFrame.

Summary:

```text
df["title"]                  → Series
df[["title", "type"]]        → DataFrame
```

## Selecting Rows with a Boolean Condition

The condition creates a Boolean Series:

```python
is_movie = df["type"] == "Movie"

print(is_movie.head())
```

Then the Boolean Series is used to select matching rows.

```python
movies = df[df["type"] == "Movie"]

print(movies.head())
print(movies.shape)
```


## Numeric Conditions

```python
recent = df[df["release_year"] >= 2020]
```

## Combining Conditions

Use `&` for AND and `|` for OR. Put each condition inside parentheses.

```python
recent_movies = df[(df["type"] == "Movie") & (df["release_year"] >= 2020)]
```

```python
movies_or_recent = df[(df["type"] == "Movie") | (df["release_year"] >= 2020) ]
```

## Selecting Rows and Columns Together

```python
result = df.loc[df["release_year"] >= 2020,["title", "type"]]

print(result.head())
```

```
Method        Example
.loc[]        df.loc[df['release_year'] > 2020, 'title']
.iloc[]       df.iloc[0:10, 3:5]
```
---

# Part 4: Duplicate Rows

## Detecting Duplicates

`.duplicated()` returns a Boolean Series. To view the duplicated rows:

```python
print(df[df.duplicated()])
```

## Removing Duplicates

```python
before = len(df)

df = df.drop_duplicates()

print(f"Removed {before - len(df)} duplicate row(s)")
```

Two rows that look similar are not always duplicates. `drop_duplicates()` removes rows only when all column values match.

---

# Part 5: Missing Values

## Detecting Missing Values

```python
print(df.isna().sum())
```

## Dropping Missing Rows or Columns

```python
# Drop rows containing one or more missing values
rows_dropped = df.dropna()

# Drop columns containing one or more missing values
columns_dropped = df.dropna(axis=1)
```

- Use `dropna()` when only a small number of rows contain missing values.
- Use `dropna(axis=1)` when removing an entire column is appropriate for the project.
- Always inspect the missing values before deciding what to remove.

---

# Try It Yourself — Build a Netflix Pipeline

The `messy_netflix_titles.csv` dataset intentionally contains duplicates, missing values, inconsistent text, and numeric outliers. In this class, remove duplicate rows and rows containing missing values. Observe the remaining text and outlier problems, but do not fix them yet.

Note: some values in `type` use inconsistent capitalization or extra whitespace. An exact condition such as `df["type"] == "Movie"` will not select those inconsistent values. That is expected for this exercise. We will clean text and numeric outliers in the next class.


## After completing all the steps below
* Get checked off by either me or a TA.
* Once you have been checked off, you may leave.



## Before You Start

Make sure your virtual environment is active:

```bash
# Mac/Linux
source venv/bin/activate        

# Windows
venv\Scripts\activate           
#OR
venv\Scripts\activate.ps1
```

Open your `class-exercise` folder. Place the provided `messy_netflix_titles.csv` file inside a `data/` directory.

## Task

Build a small command-line program that loads, inspects, and performs basic cleaning on the Netflix dataset.

- `class6_7_netflix_utils.py` will contain reusable pandas functions.
- `class6_7_netflix_pipeline.py` will handle command-line input and control the program.

You will continue using and updating these same files in Class 7.

Your program should:

1. Load the CSV file.
2. Display a basic overview.
3. Remove exact duplicate rows.
4. Remove rows containing missing values.

**Complete the TODOs.**

### Step 1 — Complete `class6_7_netflix_utils.py`

```python
import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    pass


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    pass


def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    pass
```

### Step 2 — Complete `class6_7_netflix_pipeline.py`

```python
import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from class6_7_netflix_utils import (
    drop_missing_rows,
    remove_duplicates,
    show_overview,
)

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Explore Netflix titles"
    )
    parser.add_argument(
        "--input",
        default="data/messy_netflix_titles.csv",
        help="Path to the Netflix CSV file"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Show debug messages"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.DEBUG if args.verbose else logging.INFO,
        format="%(asctime)s %(levelname)-8s %(name)s — %(message)s",
        datefmt="%H:%M:%S"
    )

    # TODO 4:
    # Create a Path object from args.input.
    # Inside a try block, load that path using pd.read_csv().
    # Catch FileNotFoundError, log an ERROR message,
    # and exit with sys.exit(1).
    # Log an INFO message.

    # TODO 5:
    # Call show_overview().
    # Log an INFO message.

    # TODO 6:
    # Call remove_duplicates().
    # Call drop_missing_rows().
    # Log an INFO message after each step that
    # includes the number of rows removed.

if __name__ == "__main__":
    main()
```

## Try These Commands

```bash
python class6_7_netflix_pipeline.py
python class6_7_netflix_pipeline.py --verbose
python class6_7_netflix_pipeline.py --input data/messy_netflix_titles.csv
python class6_7_netflix_pipeline.py --input data/missing.csv
```

## Expected Output

Using the provided dataset, the beginning of your output should include:

```text
10:15:02 INFO     __main__ — Loaded 25 rows and 7 columns
10:15:02 INFO     __main__ — Displayed DataFrame overview
10:15:02 INFO     __main__ — Removed 1 duplicate row(s)
10:15:02 INFO     __main__ — Dropped 7 rows with missing values

Shape: (25, 7)
Columns: [...]
Data types: ...
```

With `--verbose`, the output should also include DEBUG messages from `class6_7_netflix_utils`.

Example missing-file output:

```text
10:15:10 ERROR    __main__ — Input file not found: data/missing.csv
```

## Save Your Work to GitHub

```bash
git status
git add class6_7_netflix_utils.py class6_7_netflix_pipeline.py
git commit -m "Start the Class 6-7 Netflix pipeline"
git push
```
