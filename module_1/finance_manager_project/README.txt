## 💰 FinanceManager – Personal Finance Tracker (Python + PySimpleGUI)

**FinanceManager** is a desktop application built with Python and PySimpleGUI that helps users manage their personal finances with clarity and control. It allows tracking of income and expenses, categorizing transactions, filtering by date, and exporting data — all in a clean, user-friendly interface.

---

### 🚀 Features

- 📊 **Transaction Table**: View all income and expense records in a color-coded table
- 🏷️ **Category Manager**: Create, edit, and assign custom colors to financial categories
- ➕ **Add Income/Expense**: Input title, amount, category, and date
- ✅ **Validation**:
  - Ensures categories exist before adding transactions
  - Validates date format (`MM/DD/YYYY`) and prevents future dates
- 📅 **Date Filtering**: Filter transactions by start and end date
- 📤 **CSV Export**: Export filtered transactions to CSV with totals and headers
- 🎨 **Color Coding**: Display transactions with category-specific colors for quick visual reference

---

### 💾 Data Persistence

- Automatically saves data on modification or exit
- Loads existing data on startup
- Stores category colors alongside category names
- Uses local JSON files (`data.json`, `categories.json`) for simplicity and portability

---

### 🧠 Architecture & Best Practices

- Modular design with clear separation of concerns:
  - `graphics/` – GUI components
  - `utilities/` – logic and validation
  - `data/` – persistence and data handling
- Object-oriented structure with classes like `Transaction`, `Category`, and `FinanceManager`
- Clean, maintainable code with descriptive identifiers and reusable functions
- GUI-independent logic for testability and scalability

---

### 🧪 Unit Testing

- Includes `test_logica.py` with 8+ unit tests covering:
  - Date validation
  - Financial calculations
  - Data persistence
  - Category handling
- Tests are GUI-independent and use `unittest` with `os` and `sys.path` adjustments for portability

---

### 📦 Packaging & Distribution

- Packaged with **PyInstaller** in `--onedir` mode for stability
- Includes `.exe` file and required dependencies in a single folder
- README and instructions included for end users
- Shared via Google Drive as a compressed `.zip` for easy access

---

### 🛠️ Technologies Used

- Python 3.13
- PySimpleGUI
- JSON for data storage
- PyInstaller for packaging
- Unittest for testing