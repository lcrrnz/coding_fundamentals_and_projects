#This program provides helper functions for financial calculations and logic operations.
class Calculations:
    def __init__(self):
        self.total_income = 0
        self.total_spent = 0
    
    @property 
    def balance(self):
        return self.total_income - self.total_spent
    
    def income_calculation(self, amount):
        self.total_income += amount
        return amount
    
    def spent_calculation(self, amount):
        self.total_spent += amount
        return amount
    
    def calculate_totals(self, data):
        self.total_income = 0
        self.total_spent = 0
        for entry in data.values():
            try:
                amount = float(entry.get("amount", 0))
                if entry.get("type") == "Income":
                    self.income_calculation(amount)
                elif entry.get("type") == "Expense":
                    self.spent_calculation(amount)
            except (ValueError, TypeError):
                continue
    @staticmethod
    def get_calculator(data):
        calculator = Calculations()
        calculator.calculate_totals(data)
        return calculator