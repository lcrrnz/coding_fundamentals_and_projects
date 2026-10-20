# This function refreshes any visual table using formatted data and assigned category colors.
def update_table(window, key, table_data, row_colors=None):
    if row_colors is not None:
        window[key].update(values=table_data, row_colors=row_colors)
    else:
        window[key].update(values=table_data)