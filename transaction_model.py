
class Transaction():

    def __init__(self,amount , category, date):
        self.amount = amount
        self.category = category
        self.date = date


    def to_dict(self):
        return {
            "type": self.type,
            "amount":self.amount,
            "category":self.category,
            "date":self.date
    }

class IncomeTransaction(Transaction):
    def __init__(self , amount , category , date):
        super().__init__(amount , category , date)
        self.type= "Income"
        

class ExpenseTransaction(Transaction):
    def __init__(self, amount, category, date):
        super().__init__(amount, category, date)
        self.type = "Expense"
