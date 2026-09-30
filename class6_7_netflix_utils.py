import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    # TODO 1:
    # Log a DEBUG message containing the shape.
    # Print the shape, first five rows, column names, and data types.
    logger.debug(f"Dataframe shape: {df.shape}")

    print("shape: ", df.shape)
    print("first 5 rows:")
    print(df.head())
    print("column names: ", df.columns)
    print("data types: ")
    print(df.dtypes)

def remove_duplicates(df):
    """Remove exact duplicate rows."""
    # TODO 2:
    # Remove exact duplicate rows.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before_len = len(df)
    new_df = df.drop_duplicates()
    after_len = len(new_df)
    logger.debug(f"row count before: {before_len} row count after: {after_len}")
    return new_df

def drop_missing_rows(df):
    """Remove rows containing missing values."""
    # TODO 3:
    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
    before_len = len(df)
    rows_dropped = df.dropna()
    after_len = len(rows_dropped)
    logger.debug(f"row count before: {before_len} row count after: {after_len}")
    return rows_dropped