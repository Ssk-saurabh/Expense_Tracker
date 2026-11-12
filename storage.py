import json
from pathlib import Path

FILE_PATH = Path(r"C:\Users\sadhu\Desktop\SEMESTER 3\External_Code\Python\Expense_tracker\transaction_history.json")

def save_transaction(transactions):
    with open(FILE_PATH, "w") as file:
        json.dump(transactions,file,indent=4)


def load_transaction():
    print("looking for file:",FILE_PATH)
    try:
        with open(FILE_PATH, "r") as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("JSON file is empty or corrupted . Starting Fresh")
        return[]
    