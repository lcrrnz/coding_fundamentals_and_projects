import unittest
import os
import sys
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from my_first_repository.module_1.finance_manager_project.utilities.math_logic import Calculations
from my_first_repository.module_1.finance_manager_project.utilities.validate_date import validate_date
from my_first_repository.module_1.finance_manager_project.data.data_saving import CategoriesData

class TestFinanceLogic(unittest.TestCase):

    def setUp(self):
        self.test_categories_path = os.path.join("data", "categories.json")
        if os.path.exists(self.test_categories_path):
            os.rename(self.test_categories_path, self.test_categories_path + ".bak")

    def tearDown(self):
        if os.path.exists(self.test_categories_path):
            os.remove(self.test_categories_path)
        if os.path.exists(self.test_categories_path + ".bak"):
            os.rename(self.test_categories_path + ".bak", self.test_categories_path)

    def test_valid_date(self):
        result = validate_date("09/15/2025")
        self.assertIsInstance(result, datetime)

    def test_invalid_date_format(self):
        result = validate_date("2025-09-15")
        self.assertEqual(result, "Date format must be MM/DD/YYYY.")

    def test_future_date(self):
        future = "12/31/2999"
        result = validate_date(future)
        self.assertEqual(result, "Date cannot be in the future.")

    def test_income_calculation(self):
        calc = Calculations()
        calc.income_calculation(1000)
        self.assertEqual(calc.total_income, 1000)

    def test_spent_calculation(self):
        calc = Calculations()
        calc.spent_calculation(250)
        self.assertEqual(calc.total_spent, 250)

    def test_balance_calculation(self):
        calc = Calculations()
        calc.income_calculation(1000)
        calc.spent_calculation(400)
        self.assertEqual(calc.balance, 600)

    def test_calculate_totals(self):
        data = {
            "1": {"type": "Income", "amount": "500"},
            "2": {"type": "Expense", "amount": "200"},
            "3": {"type": "Income", "amount": "300"},
        }
        calc = Calculations.get_calculator(data)
        self.assertEqual(calc.total_income, 800)
        self.assertEqual(calc.total_spent, 200)
        self.assertEqual(calc.balance, 600)

    def test_category_persistence(self):
        handler = CategoriesData()
        test_data = {"Food": "#FF0000", "Transport": "#00FF00"}
        handler.save_categories_data_json(test_data)
        self.assertTrue(os.path.exists(self.test_categories_path))

        loaded = handler.load_categories_data_json()
        self.assertEqual(loaded, test_data)

if __name__ == "__main__":
    unittest.main()