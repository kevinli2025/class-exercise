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
    p = Path(args.input)
    try:
        df = pd.read_csv(p)
    except FileNotFoundError:
        logger.error(f"file not found: {p}")
        sys.exit(1)
    logger.info(f"rows: {df.shape[0]} columns: {df.shape[1]}")


    # TODO 5:
    show_overview(df)
    logger.info("displayed DF overview")
    # Call show_overview().
    # Log an INFO message.

    # TODO 6:
    # Call remove_duplicates().
    before_dupe_removal = len(df)
    df = remove_duplicates(df)
    dupe_diff = before_dupe_removal - len(df)
    logger.info(f"number of duplicate rows removed: {dupe_diff}")
    # Call drop_missing_rows().

    before_missing_removal = len(df)
    df = drop_missing_rows(df)
    removal_diff = before_missing_removal - len(df)
    logger.info(f"number of rows missing values removed: {removal_diff}")
    # Log an INFO message after each step that
    # includes the number of rows removed.

if __name__ == "__main__":
    main()