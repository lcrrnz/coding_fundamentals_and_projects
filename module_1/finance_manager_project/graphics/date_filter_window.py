#this program holds the logic for date filtering data window.
import FreeSimpleGUI as sg
from datetime import datetime
from my_first_repository.module_1.finance_manager_project.utilities.table_builder import build_table
from my_first_repository.module_1.finance_manager_project.utilities.table_update import update_table
from my_first_repository.module_1.finance_manager_project.utilities.validate_date import validate_date
from my_first_repository.module_1.finance_manager_project.utilities.math_logic import Calculations

def date_filter(data, categories):
    headings = ["Category", "Type", "Title", "Amount", "Date"]
    row_colors = []
    table_data = []
    calculator = Calculations.get_calculator(data)
    build_table(data, categories, row_colors, table_data)
    layout = [
        [sg.Text("Select the date range to review")],
        [sg.Text("Start Date"), sg.InputText(key="Start Date", size=(12, 1)), sg.CalendarButton("📅", target="Start Date", format="%m/%d/%Y", close_when_date_chosen=True)],
        [sg.Text("End Date "), sg.InputText(key="End Date", size=(12, 1)), sg.CalendarButton("📅", target="End Date", format="%m/%d/%Y", close_when_date_chosen=True)],
        [sg.Table(values=table_data,
                headings=headings,
                row_colors=row_colors,
                text_color="black",
                background_color="white",
                max_col_width=25,
                auto_size_columns=True,
                display_row_numbers=True,
                justification='center',
                num_rows=15,
                key='-TABLE-',
                enable_events=True)],
        [sg.Text(f"Total Income: ${calculator.total_income}", key="INCOME"),
        sg.Text(f"Total Spent: ${calculator.total_spent}", key="SPENT"),
        sg.Text(f"Balance: ${calculator.balance}", key="BALANCE")],
        [sg.Button("Apply Filter"), sg.Button("Cancel")]
    ]
    window = sg.Window("Date filter View", layout, size=(500, 500))
    while True:
        filtered_dates = {}
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Apply Filter":
            start = validate_date(values["Start Date"])
            end = validate_date(values["End Date"])
            errors = []
            if isinstance(start, str):
                errors.append(f"• Enter the Start Date{start}")
            if isinstance(end, str):
                errors.append(f"• Enter the End Date{end}")
            if errors:
                sg.popup_error("Please fix the following:\n\n" + "\n".join(errors))
                continue
            for key, entry in data.items():
                try:
                    entry_date = datetime.strptime(entry["date"], "%m/%d/%Y")
                    if start <= entry_date <= end:
                        filtered_dates[key] = entry
                except ValueError:
                    continue
            calculator = Calculations.get_calculator(filtered_dates)
            row_colors = []
            table_data = []
            build_table(filtered_dates, categories, row_colors, table_data)
            update_table(window, "-TABLE-", table_data, row_colors)
            window["INCOME"].update(f"Total Income: ${calculator.total_income}")
            window["SPENT"].update(f"Total Spent: ${calculator.total_spent}")
            window["BALANCE"].update(f"Balance: ${calculator.balance}")
    window.close()