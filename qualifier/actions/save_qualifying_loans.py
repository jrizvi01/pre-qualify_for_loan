import sys
import questionary
from pathlib import Path

def save_qualifying_loans(qualifying_loans):

    # @TODO: Complete the usability dialog for savings the CSV Files.
    save_loans = questionary.confirm("Would you like to save the loan?").ask()
    csvoutpath = questionary.text("Enter a file path to a save the qualifying loans sheet (.csv):").ask()
    csvoutpath = Path(csvoutpath)
    if not csvoutpath.exists():
        sys.exit(f"Oops! Can't find this path: {csvoutpath}")
        
    return csvoutpath