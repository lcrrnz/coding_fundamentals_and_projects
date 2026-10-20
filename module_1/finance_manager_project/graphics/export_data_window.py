#this program hold the logic to download data to CSV
import FreeSimpleGUI as sg
from datetime import datetime
from my_first_repository.module_1.finance_manager_project.utilities.table_builder import build_table
from my_first_repository.module_1.finance_manager_project.data.csv_exporter import DataHandler
from my_first_repository.module_1.finance_manager_project.utilities.math_logic import Calculations

def export_data_window(data, categories):
    headings = ["Category", "Type", "Title", "Amount", "Date"]
    row_colors = []
    table_data = []
    calculator = Calculations.get_calculator(data)
    build_table(data, categories, row_colors, table_data)
    layout = [
        [sg.Text("This is your current data available to download")],
        [sg.Table(values=table_data,
                headings=headings,
                row_colors=row_colors,
                text_color = "black",
                background_color = "white",
                max_col_width=50,
                auto_size_columns=True,
                display_row_numbers=True,
                justification='center', 
                num_rows=15,
                key='-TABLE-',
                enable_events=True)],
        [sg.Text(f"Total Income: ${calculator.total_income}", key="INCOME"),
        sg.Text(f"Total Spent: ${calculator.total_spent}", key="SPENT"),
        sg.Text(f"Balance: ${calculator.balance}", key="BALANCE")],
        [sg.Button("Download"), sg.Button("Cancel")]
    ]
    window = sg.Window("Export data to CSV", layout, size =(500,500))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Download":
            handler = DataHandler()
            try:
                handler.csv_file_export()
                sg.popup("Export Completed Successfully")
            except PermissionError as error:
                sg.popup_error(f"Export failed:\n{error}\n\nMake sure the file isn't open in another program.")
    window.close()
