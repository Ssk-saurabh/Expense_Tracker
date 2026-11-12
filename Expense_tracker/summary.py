def calculate_summary(transactions):

    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "Income":
            income += transaction["amount"]

        elif transaction["type"] == "Expense":
            expense += transaction["amount"]

    return income, expense
        

def view_summary(transactions):
    income , expense = calculate_summary(transactions)

    print(f"Total Income : {income} ")
    print(f"Total Expense : {expense} ")
    print(f"Remaining Balance : {income - expense} ")


def view_transection_details(transactions):
    # IMPORTANT CONCEPT -------------
    if not transactions:
        print("transaction list is empty....")
        return
    
    for transaction in transactions:
        print("\nType:", transaction["type"])
        print("Amount:", transaction["amount"])
        print("Category:", transaction["category"])
        print("Date:", transaction["date"])
        