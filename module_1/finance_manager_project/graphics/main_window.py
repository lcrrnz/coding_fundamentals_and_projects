# This program coordinates the financial manager’s interface and updates the main table based on user actions.
import FreeSimpleGUI as sg
from datetime import datetime
from my_first_repository.module_1.finance_manager_project.graphics import category_window
from my_first_repository.module_1.finance_manager_project.graphics.date_filter_window import date_filter
from my_first_repository.module_1.finance_manager_project.graphics.expense_window import main_expense_window
from my_first_repository.module_1.finance_manager_project.graphics.export_data_window import export_data_window
from my_first_repository.module_1.finance_manager_project.graphics.income_window import main_income_window
from my_first_repository.module_1.finance_manager_project.data import data_saving
from my_first_repository.module_1.finance_manager_project.utilities.table_builder import build_table
from my_first_repository.module_1.finance_manager_project.utilities.load_category_table import load_categories
from my_first_repository.module_1.finance_manager_project.utilities.table_update import update_table
from my_first_repository.module_1.finance_manager_project.utilities.math_logic import Calculations

def main_window():
    transaction_handler = data_saving.TransactionData()
    category_handler = data_saving.CategoriesData()
    categories = load_categories(category_handler)
    data = transaction_handler.transaction_load_data_json()
    calculator = Calculations.get_calculator(data)
    headings = ["Category", "Type", "Title", "Amount", "Date"]
    row_colors = []
    table_data = []
    build_table(data, categories, row_colors, table_data)
    layout = [
        [sg.Text("Welcome to your finance manager!")],
        [sg.Button("Income Manager"), sg.Button("Expense Manager"), sg.Button("Category Manager"),
        sg.Button("Export to CSV"), sg.Button("Filter by Date")],
        [sg.Table(values=table_data,
                headings=headings,
                row_colors=row_colors,
                text_color="black",
                background_color="white",
                max_col_width=50,
                auto_size_columns=True,
                display_row_numbers=True,
                justification='center',
                num_rows=20,
                key='-TABLE-',
                enable_events=True)],
        [sg.Text(f"Total Income: ${calculator.total_income}", key="INCOME"),
        sg.Text(f"Total Spent: ${calculator.total_spent}", key="SPENT"),
        sg.Text(f"Balance: ${calculator.balance}", key="BALANCE")]
    ]
    window = sg.Window("Finance Manager", layout, resizable=True)
    if not categories:
        sg.popup("Welcome to your Finance Manager!\nPlease go to the category manager to begin.")
    else:
        sg.popup("Welcome back to your Finance Manager!\nPlease wait while we load the data")
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        categories = load_categories(category_handler)
        if event != "Category Manager" and not categories:
            sg.popup("Please go to the Category Manager to begin.")
            continue
        if event == "Category Manager":
            category_window.main_category_window(category_handler)
            categories = load_categories(category_handler)
        elif event == "Income Manager":
            data = transaction_handler.transaction_load_data_json()
            main_income_window(data, categories, transaction_handler, category_handler)
        elif event == "Expense Manager":
            data = transaction_handler.transaction_load_data_json()
            main_expense_window(data, categories, transaction_handler, category_handler)
        elif event == "Export to CSV":
            data = transaction_handler.transaction_load_data_json()
            export_data_window(data, categories)
        elif event == "Filter by Date":
            data = transaction_handler.transaction_load_data_json()
            date_filter(data, categories)
        data = transaction_handler.transaction_load_data_json()
        calculator = Calculations.get_calculator(data)
        row_colors = []
        table_data = []
        build_table(data, categories, row_colors, table_data)
        update_table(window, "-TABLE-", table_data, row_colors)
        window["INCOME"].update(f"Total Income: ${calculator.total_income}")
        window["SPENT"].update(f"Total Spent: ${calculator.total_spent}")
        window["BALANCE"].update(f"Balance: ${calculator.balance}")
    window.close()