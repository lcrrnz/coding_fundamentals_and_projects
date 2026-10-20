# Entry point for the finance manager system. Initializes the GUI and routes user actions to income, expense, category, and export modules.
from my_first_repository.module_1.finance_manager_project.graphics.main_window import main_window


if __name__ == "__main__":
    try:
        main_window()
    except Exception as error:
        print(f"Fatal error encountered: {error}")