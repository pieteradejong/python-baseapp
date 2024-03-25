from enum import Enum
import csv
import logging
import json
import sys

"""
Libary of re-usable functionality.
"""


"""
Below: Usage for colors:

"""


class TextColor(Enum):
    RED = "\033[91m"
    YELLOW = "\033[93m"
    GREEN = "\033[92m"
    PURPLE = "\033[95m"
    MAGENTA = "\033[35m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    REGULAR = "\033[0m"


def print_colored(text: str, color: TextColor):
    print(f"{color.value}{text}{TextColor.END.value}")


# from colors import TextColor, print_colored

print_colored("Hello, World!", TextColor.RED)
print_colored("This is green text!", TextColor.GREEN)

"""

"""


def read_csv_file(file_path: str) -> list:
    """
    Reads a CSV file and returns a list of dictionaries,
    where each dictionary represents a row in the CSV,
    with the column headers as keys.

    :param file_path: The path to the CSV file.
    :return: A list of dictionaries.
    """
    data = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


"""
Load config from json.
"""


def load_config():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            if "CANDIDATE_ID" not in config or not config["CANDIDATE_ID"]:
                raise ValueError("CANDIDATE_ID is not set in the config file.")
            return config
    except FileNotFoundError:
        logging.error("The configuration file config.json does not exist.")
        sys.exit(1)
    except json.JSONDecodeError:
        logging.error("Error decoding config.json. Ensure it is valid JSON.")
        sys.exit(1)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
        sys.exit(1)
