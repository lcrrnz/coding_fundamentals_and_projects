# This program handles getting the data stored in the JSON save file and exporting it to CSV.
import os
import json
import csv
from my_first_repository.module_1.finance_manager_project.utilities.math_logic import Calculations

class DataHandler:
    def __init__(self, file_name="finance_report.csv", json_file="data.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, json_file)
        self.export_path = os.path.join(base_path, file_name)
    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                json_data = json.load(file)
                return json_data
        except FileNotFoundError:
            return {}
    def csv_file_export(self):
        data = self.read_json()
        keys = ("Category", "Type", "Title", "Amount", "Date")
        try:
            if not data:
                print("No data available. File will contain only default categories")
                return
            with open(self.export_path, 'w', newline="") as file:
                writer = csv.DictWriter(file, fieldnames=keys)
                writer.writeheader()
                # Transform and format data
                formatted_data = []
                for entry in data.values():
                    formatted_data.append({
                        "Category": entry.get("category", ""),
                        "Type": entry.get("type", ""),
                        "Title": entry.get("title", ""),
                        "Amount": f"${entry.get('amount', 0):,.2f}",
                        "Date": entry.get("date", "")
                    })
                writer.writerows(formatted_data)
                # Add totals
                calculator = Calculations.get_calculator(data)
                writer.writerow({
                    "Category": "TOTAL", "Type": "Income", "Title": "", "Amount": f"${calculator.total_income:,.2f}", "Date": ""
                })
                writer.writerow({
                    "Category": "TOTAL", "Type": "Expense", "Title": "", "Amount": f"${calculator.total_spent:,.2f}", "Date": ""
                })
                writer.writerow({
                    "Category": "TOTAL", "Type": "Balance", "Title": "", "Amount": f"${calculator.balance:,.2f}", "Date": ""
                })
            print("Export complete.")
        except PermissionError as error:
            print(f'Unable to create file due to {error}')

