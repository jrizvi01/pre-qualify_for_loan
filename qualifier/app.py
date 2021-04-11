# Jamal A. Rizvi
# A python program to match applicants with qualifying loans based on standard criteria such as 
# credit score, debt-to-income ratio, loan-to-value etc.
# April 4, 2021
# -*- coding: utf-8 -*-
"""Loan Qualifier Application.

This is a command line application to match applicants with qualifying loans.

qualifying_loans.csv file was produced using the following data:

Credit score: 750
Monthly debt: 1500
Monthly income: 4000
Desired loan amount: 210000
Home value: 250000

"""
import csv
import sys
import fire
import questionary
from pathlib import Path

from qualifier.utils.fileio import (load_csv, save_csv)


# This function asks for the file path to the latest banking data and load the CSV file.
from qualifier.bankdata import load_bank_data

#  This function opens the prompt dialog to get the applicant's financial information.
from qualifier.applicantinfo import get_applicant_info

# This function determines which loans the user qualifies for.
from qualifier.findqualifyingloans import find_qualifying_loans


# This function is called to save the qualifying loans to a CSV file.
from qualifier.savequalifyingloans import save_qualifying_loans

    
def run():
    """The main function for running the script."""

    # Load the latest Bank data
    bank_data = load_bank_data()

    # Get the applicant's information
    credit_score, debt, income, loan_amount, home_value = get_applicant_info()

    # Find qualifying loans
    qualifying_loans = find_qualifying_loans(
        bank_data, credit_score, debt, income, loan_amount, home_value
    )

    # Save qualifying loans
    csvoutpath = save_qualifying_loans(qualifying_loans)
    save_csv(csvoutpath, qualifying_loans)


if __name__ == "__main__":
    fire.Fire(run)

