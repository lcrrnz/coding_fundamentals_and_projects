# This program manages category creation, editing, and deletion within the app.
import FreeSimpleGUI as sg
from my_first_repository.module_1.finance_manager_project.data import data_saving
from my_first_repository.module_1.finance_manager_project.utilities.load_category_table import load_categories
from my_first_repository.module_1.finance_manager_project.utilities.table_update import update_table

def create_category_window():
    layout = [
        [sg.InputText("Category Name", key="Category Name")],
        [sg.InputText(key="COLOR", visible=False), sg.ColorChooserButton("Choose Color", target="COLOR")],
        [sg.Button("Create"), sg.Button("Cancel")]
    ]
    window = sg.Window("Create Category", layout, size=(400, 200))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Create":
            name = values["Category Name"].strip().title()
            color = values["COLOR"]
            if not name or not color:
                sg.popup_error("Please enter a category name and choose a color.")
                continue
            try:
                categories_handler = data_saving.CategoriesData()
                categories_handler.append_category(name, color)
                sg.popup(f'Category {name}, created successfully')
            except ValueError as error:
                sg.popup_error(str(error))
            break
    window.close()

def delete_category_window(category_list):
    layout = [
        [sg.Text("Select the category to delete")],
        [sg.Combo(values=category_list, key="Category Name", readonly=True, size=(30, 1))],
        [sg.Button("Delete"), sg.Button("Cancel")]
    ]
    window = sg.Window("Delete Category", layout, size=(400, 200))

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Delete":
            name = values["Category Name"]
            if not name:
                sg.popup_error("Please select a category to delete.")
                continue
            confirm = sg.popup_yes_no(f"Are you sure you want to delete '{name}'?")
            if confirm == "Yes":
                try:
                    categories_handler = data_saving.CategoriesData()
                    categories_handler.delete_category(name)
                    sg.popup(f'Category "{name}" deleted successfully.')
                except ValueError as error:
                    sg.popup_error(str(error))
            break
    window.close()

def main_category_window(category_handler):
    categories = load_categories(category_handler)
    if not categories:
        sg.popup("Please create your first category")
    headings = ["Category"]
    table_data = [[name, color] for name, color in categories.items()]
    row_colors = [(i, color) for i, (name, color) in enumerate(categories.items())]
    layout = [
        [sg.Button("Create Category"), sg.Button("Delete Category"), sg.Button("Cancel")],
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
            ]
    window = sg.Window("Categories Manager", layout, size=(500, 400))
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "Cancel"):
            break
        if event == "Create Category":
            create_category_window()
            categories = load_categories(category_handler)
            table_data = [[name, color] for name, color in categories.items()]
            update_table(window, "-TABLE-", table_data, row_colors)
        elif event == "Delete Category":
            delete_category_window(list(categories.keys()))
            categories = load_categories(category_handler)
            table_data = [[name, color] for name, color in categories.items()]
            update_table(window, "-TABLE-", table_data, row_colors)
    window.close()