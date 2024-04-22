class BudgetCategory:
    def __init__(self, budget, budgetcategory = "", budgetamount = 0):
        self.__budgetcategory = budgetcategory
        self.__budgetamount = budgetamount
        self.expenses = {}
        self.budget = budget
    
    def add_expense(self, amount, category):
        if amount>0:
            self.__budgetamount = amount
            self.__budgetcategory = category
            self.budget -= amount
              
    def get_budgetcategory(self):
        return self.__budgetcategory
    
    def get_budgetamount(self):
        return self.__budgetamount
    
    def set_budget(self):
        self.expenses[self.__budgetcategory] = self.__budgetamount
            

    def display_category_summary(self):
        for e, a  in self.expenses.items():
            print(f'Expenses: {e}, Amount: {a}')


food_category = BudgetCategory(500)
while True:
    r = input("Press Q to quit, S to show all the categories, A to add an expense: ").lower()
    if r == 'q':
        break
    elif r == 'a':
        category = input("Choose the category for the expense: ")
        amount = int(input("Choose the amount for the expense: "))
        food_category.add_expense(amount, category)
        food_category.set_budget()
    elif r == 's':
        food_category.display_category_summary()
    else:
        print('Invalid input!! ')
