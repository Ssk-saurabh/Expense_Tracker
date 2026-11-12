import json

transactions = []

# Save transactions into JSON file
def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)


# Load transactions from JSON file
def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []
    
    except json.JSONDecodeError:
        print("Warning: JSON file is corrupted. Starting with empty records.")
        return []


def add_income():
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
    save_transactions(add_transaction)
   

def add_expense():
    add_transaction = {
            "type" : "Expense",
            "amount": float(input("Enter your expense : ")),
            "category": input("Enter your category :"),
            "date": input("Enter date yy-mm-dd : ")
    }
    transactions.append(add_transaction)
    save_transactions(add_transaction)
    

def view_transection_details():
    # IMPORTANT CONCEPT -------------
    if not transactions:
        print("transaction list is empty....")
    for transaction in transactions:
        print("Amount:", transaction["amount"])
        print("Category:", transaction["category"])
        print("Date:", transaction["date"])
        print("\nType:", transaction["type"])

def calculate_summary(transaction):

    income = 0
    expense = 0

    for transaction in transactions:
        if transaction["type"] == "income":
            income += transaction["amount"]

        elif transaction["type"] == "expense":
            expense += transaction["expense"]

    return income, expense
        

def view_summary(transaction):

    income , expense = calculate_summary(transaction)

    print(f"Total Income : {income} ")
    print(f"Total Expense : {expense} ")
    print(f"Remaining Balance : {income - expense} ")






user_input = 0

while(user_input != 5):

    user_input = int(input("Choose your action: \n  1.Income \n  2.Expense \n  3.View transition \n  4.View Summary \n  5.Exit "))
    
    if(user_input == 1):
        add_income();
    elif(user_input == 2):
        add_expense();
    elif(user_input == 3):
        view_transection_details();
    elif(user_input == 4):
        view_summary(transactions);
    elif(user_input == 5):
            print("Exiting......")
    else:
        print("Wrong option. Choose again. ")
