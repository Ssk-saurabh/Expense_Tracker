from storage import save_transaction
from transaction_model import IncomeTransaction, ExpenseTransaction


def add_income(transactions):
    while True:
        try:
            amount = float(input("Enter your income : "))
            if(amount<=0):
                print("Enter positive amount")
                continue
            break

        except ValueError:
            print("Enter input is invalid, try again ")

    category = input("Enter your category: ")
    date = input("Enter date yy-mm-dd: ")
    income = IncomeTransaction(amount, category, date)
    transactions.append(income.to_dict())

    save_transaction(transactions)


    
   

def add_expense(transactions):
    while True:
        try:
            amount = float(input("Enter your expense: "))

            if amount <= 0:
                print("Enter positive amount")
                continue

            break

        except ValueError:
            print("Invalid input, try again")

    category = input("Enter your category: ")
    date = input("Enter date yy-mm-dd: ")

    expense = ExpenseTransaction(amount, category, date)

    transactions.append(expense.to_dict())

    save_transaction(transactions)
