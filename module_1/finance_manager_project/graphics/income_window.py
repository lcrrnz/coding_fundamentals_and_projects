# This program handles income registration with field validation and calendar-based date selection.
import FreeSimpleGUI as sg
from my_first_repository.module_1.finance_manager_project.data import data_saving
from my_first_repository.module_1.finance_manager_project.utilities.table_builder import build_table
from my_first_repository.module_1.finance_manager_project.utilities.table_update import update_table
from my_first_repository.module_1.finance_manager_project.utilities.load_category_table import load_categories
from my_first_repository.module_1.finance_manager_project.utilities.validate_date import validate_date
from my_first_repository.module_1.finance_manager_project.utilities.math_logic import Calculations

def add_income_window(category_handler):
    categories = load_categories(category_handler)
    if not categories:
        sg.popup_error("Please create a category before adding income.")
        return
    layout = [
        [sg.Text("Add income")],
        [sg.Text("Title"), sg.InputText(key="Title")],
        [sg.Text("Amount"), sg.InputText(key="Amount")],
        [sg.Text("Date"), sg.InputText(key="Date", size=(12, 1)), sg.CalendarButton("📅", target="Date", format="%m/%d/%Y", close_when_date_chosen=True)],
        [sg.Text("Category"), sg.Combo(values=list(categories.keys()), key="Category", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
            ]
    window = sg.Window("Add Income", layout, size=(400, 200))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Save":
            title = values["Title"].strip().title()
            amount = values["Amount"]
            date_str = values["Date"]
            category = values["Category"]
            errors = []
            if not title:
                errors.append("• Title is required.")
            if not amount.replace('.', '', 1).isdigit():
                errors.append("• Amount must be a number.")
            date = validate_date(date_str)
            if isinstance(date, str):
                errors.append(f"• {date}")
            if not category:
                errors.append("• Category must be selected.")
            if errors:
                sg.popup_error("Please fix the following:\n\n" + "\n".join(errors))
                continue
            entry = {
                "title": title,
                "amount": float(amount),
                "date": date.strftime("%m/%d/%Y"),
                "category": category,
                "type": "Income"
            }
            handler = data_saving.TransactionData()
            handler.append_entry(entry)
            sg.popup(f'Income "{title}" saved successfully.')
            break
    window.close()

def delete_income_window(title_list):
    layout = [
        [sg.Text("Select the income to delete")],
        [sg.Combo(values=title_list, key="Title", readonly=True, size=(30, 1))],
        [sg.Button("Delete"), sg.Button("Cancel")]
    ]
    window = sg.Window("Delete Income", layout, size=(400, 200))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Delete":
            title = values["Title"]
            if not title:
                sg.popup_error("Please select an income to delete.")
                continue
            confirm = sg.popup_yes_no(f"Are you sure you want to delete '{title}'?")
            if confirm == "Yes":
                try:
                    handler = data_saving.TransactionData()
                    handler.delete_transaction_entry(title)
                    sg.popup(f'Income "{title}" deleted successfully.')
                except ValueError as error:
                    sg.popup_error(str(error))
            break
    window.close()

def main_income_window(data, categories, transaction_handler, category_handler):
    headings = ["Category", "Type", "Title", "Amount", "Date"]
    row_colors = []
    table_data = []
    calculator = Calculations.get_calculator(data)
    income_data = {key: entry for key, entry in data.items() if entry.get("type") == "Income"}
    build_table(income_data, categories, row_colors, table_data)
    layout = [
        [sg.Button("Add Income"), sg.Button("Delete Income"), sg.Button("Cancel")],
        [sg.Table(values=table_data,
                headings=headings,
                row_colors=row_colors,
                text_color = "black",
                background_color = "white",
                max_col_width=25,
                auto_size_columns=True,
                display_row_numbers=True,
                justification='center',
                num_rows=15,
                key='-TABLE-',
                enable_events=True)],
        [sg.Text(f"Total Income: ${calculator.total_income}", key="INCOME"),
        sg.Text(f"Total Spent: ${calculator.total_spent}", key="SPENT"),
        sg.Text(f"Balance: ${calculator.balance}", key="BALANCE")]
            ]
    window = sg.Window("Income Manager", layout, size=(500, 400))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Add Income":
            add_income_window(category_handler)
        elif event == "Delete Income":
            titles = [entry.get("title", "") for entry in data.values() if entry.get("type") == "Income"]
            delete_income_window(titles)
        data = transaction_handler.transaction_load_data_json()
        calculator = Calculations.get_calculator(data)
        row_colors = []
        table_data = []
        income_data = {key: entry for key, entry in data.items() if entry.get("type") == "Income"}
        build_table(income_data, categories, row_colors, table_data)
        update_table(window, "-TABLE-", table_data, row_colors)
        window["INCOME"].update(f"Total Income: ${calculator.total_income}")
        window["SPENT"].update(f"Total Spent: ${calculator.total_spent}")
        window["BALANCE"].update(f"Balance: ${calculator.balance}")
    window.close()