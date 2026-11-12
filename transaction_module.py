from storage import save_transaction


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

    #directory
    add_transaction = {
        "type" : "Income",
        "amount": amount,
        "category": input("Enter your category :"),
        "date": input("Enter date yy-mm-dd : ")
    }
    #insert directory to list
    transactions.append(add_transaction)
    save_transaction(transactions)
   

def add_expense(transactions):
    add_transaction = {
            "type" : "Expense",
            "amount": float(input("Enter your expense : ")),
            "category": input("Enter your category :"),
            "date": input("Enter date yy-mm-dd : ")
    }
    transactions.append(add_transaction)
    save_transaction(transactions)
    