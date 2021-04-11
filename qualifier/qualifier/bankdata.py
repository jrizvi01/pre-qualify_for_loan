# Jamal A. Rizvi
# April 4, 2021
# -*- coding: utf-8 -*-
# This function ask for the file path to the latest banking data and load the CSV file.


import csv
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import (load_csv, save_csv)


def load_bank_data():
    """Ask for the file path to the latest banking data and load the CSV file.

    Returns:
        The bank data from the data rate sheet CSV file.
    """

    csvpath = questionary.text("Enter a file path to a rate-sheet (.csv):").ask()
    csvpath = Path(csvpath)
    if not csvpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvpath}")

    return load_csv(csvpath)