import storage
import summary
import transaction_module
from transaction_module import add_income, add_expense


user_input = 0
transactions = storage.load_transaction()

while(user_input != 5):


    user_input = int(input("Choose your action: \n  1.Income \n  2.Expense \n  3.View transition \n  4.View Summary \n  5.Exit "))
    
    if(user_input == 1):
        transaction_module.add_income(transactions)
    elif(user_input == 2):
        transaction_module.add_expense(transactions)
    elif(user_input == 3):
        summary.view_transection_details(transactions)
    elif(user_input == 4):
        summary.view_summary(transactions)
    elif(user_input == 5):
            print("Exiting......")
    else:
        print("Wrong option. Choose again. ")
