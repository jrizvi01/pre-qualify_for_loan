# Jamal A. Rizvi
# April 4, 2021
# -*- coding: utf-8 -*-

# This function saves the qualifying loans to a CSV file.

import csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import load_csv


def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """

    save_loans = questionary.confirm("Would you like to save the loan?").ask()
    csvoutpath = questionary.text("Enter a file path to save the qualifying loans sheet (.csv):").ask()
    csvoutpath = Path(csvoutpath)
    if not csvoutpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvoutpath}")
    # csvoutpath = Path('c:/Users/Laptop/Documents/UC Berkeley/Module Challenges/Module 2/Starter_Code/qualifier/data/qualifying_loans.csv')
    return csvoutpath
