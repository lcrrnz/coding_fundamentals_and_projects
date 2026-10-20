# This function formats and prepares data for display in the main table, including color and date handling.
from datetime import datetime
def build_table(data, categories, row_colors, table_data):
    for i, entry in enumerate(data.values()):
        cat_name = entry.get("category", "")
        color = categories.get(cat_name, "#FFFFFF")
        row_colors.append((i, color))
        try:
            date_fmt = datetime.strptime(entry.get("date", ""), "%m/%d/%Y").strftime("%m/%d/%y")
        except ValueError:
            date_fmt = entry.get("date", "") if entry.get("date", "") else "Invalid date"
        table_data.append([
            entry.get("category", ""),
            entry.get("type", ""),
            entry.get("title", ""),
            entry.get("amount", ""),
            date_fmt
        ])