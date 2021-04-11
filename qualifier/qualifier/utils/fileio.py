# Jamal A. Rizvi
# Functions which can be called from aother program to load and save CSV data.
# Date: April 4, 2021
# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv

# Function to read the CSV file from path provided.
def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

#Function to save CSV file to path provided. 
def save_csv(csvoutpath, data):
    """Saves the CSV file to path provided.

    Args:
        csvpath (Path): The csv file path.
        data: A list of the rows of data for the CSV file.
        header: An optional header for the CSV.

    Returns:
        A list of lists that contains the rows of data to the CSV file.

    """  
 
    with open(csvoutpath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["lender", "max_loan_amount", "max_loan_to_value", "max_debt_to_income", "min_credit_score" , "interest_rate"])
        writer.writerows(data)