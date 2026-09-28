import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # 1. Read the file using pd.read_csv().
    # 2. Log the filepath at INFO.
    # 3. Print the first three rows (e.g. DataFrame.head(3))
    df = pd.read_csv(filepath)
    logger.info(f"inspecting {filepath.suffix}:{filepath.name}")
    print(df.head(3))


def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # TODO:
    # 1. Open the file and read it using json.load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    with open(filepath, "r") as f:
        data = json.load(f)
    logger.info(f"inspecting {filepath.suffix}:{filepath.name}")
    print(data)




def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # 1. Open the file and read it using yaml.safe_load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    with open(filepath, "r") as f:
        config = yaml.safe_load(f)
    logger.info(f"inspecting {filepath.suffix}:{filepath.name}")
    print(config)

    


def inspect_env():
    """Read a .env file and display basic information."""
    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]

    # TODO:
    # 1. Log at INFO that .env was loaded.
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.
    logger.info(f" .env loaded")
    print(keys)

def main():
    # 1. Create a Path object for the data directory.
    data_dir = Path("data")
    csv_path = data_dir / "sample.csv"
    json_path = data_dir / "sample.json"
    yaml_path = data_dir / "sample.yaml"

    inspect_csv(csv_path)
    inspect_json(json_path)
    inspect_yaml(yaml_path)
    inspect_env()
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.



if __name__ == "__main__":
    main()