# This program holds the logic for data storage while using the app and bringing it back during start up.

import os
import json

class TransactionData:
    def __init__(self, file_name="data.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, file_name)
    def transaction_load_data_json(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except FileNotFoundError:
            return {}
    def transaction_save_data_json(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
    def delete_transaction_entry(self, title_to_delete):
        data = self.transaction_load_data_json()
        title_to_delete = title_to_delete.strip().title()
        for key in list(data.keys()):
            if data[key].get("title", "").strip().title() == title_to_delete:
                del data[key]
                break
        self.transaction_save_data_json(data)
    def append_entry(self, new_entry):
        data = self.transaction_load_data_json()
        key = new_entry.get("title", "").strip().title()
        data[key] = new_entry
        self.transaction_save_data_json(data)


class CategoriesData:
    def __init__(self, file_name="categories.json"):
        base_path = os.path.dirname(__file__)
        self.file_path = os.path.join(base_path, file_name)
    def load_categories_data_json(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
                return data if isinstance(data, dict) else {}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
    def save_categories_data_json(self, data):
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)
    def delete_category(self, name):
        categories = self.load_categories_data_json()
        name = name.strip().title()
        if name not in categories:
            raise ValueError(f'The category "{name}" does not exist.')
        del categories[name]
        self.save_categories_data_json(categories)
    def append_category(self, name, color):
        categories = self.load_categories_data_json()
        name = name.strip().title()
        if not isinstance(categories, dict):
            categories = {}
        if name in categories:
            raise ValueError(f'The category "{name}" already exists')
        categories[name] = color
        self.save_categories_data_json(categories)