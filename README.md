# 📚 E-Library Data Insights Dashboard

**A Python-based Object-Oriented Library Management & Data Visualization CLI Application**

---

## 📖 Overview
The **E-Library Data Insights Dashboard** is an interactive command-line tool built with Python to manage book borrowing records, perform statistical analysis, filter transactions, generate summary reports, and visualize library usage trends using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.

---

## ✨ Features
- **Load CSV Dataset:** Import borrowing records and automatically parse transaction dates.
- **Add New Transaction:** Add new book borrowing entries dynamically using OOP (`Library` & `Management` classes).
- **Calculate Statistics:** Compute mean, standard deviation, and maximum borrowing duration using NumPy.
- **Filter Transactions:** Search and filter records by **Genre**, **Date Range**, or **Minimum Borrowing Duration**.
- **Generate Summary Report:** View total transactions, unique users, unique books, late returns (`>14 days`), and top 3 genres.
- **Interactive Visualizations:**
  1. **Bar Chart:** Top 5 Most Borrowed Books
  2. **Line Graph:** Monthly Borrowing Trends
  3. **Pie Chart:** Distribution of Books by Genre
  4. **Heatmap:** Borrowing Activity by Day of the Week & Genre

---

## 📂 Project Structure
```text
Dataset/
│
├── main.py                              # Main Python application (OOP & Menu Dashboard)
├── library_borrowing_transactions.csv   # Sample dataset (5,000 borrowing records)
└── README.md                            # Project documentation
```

### Dataset Schema (`library_borrowing_transactions.csv`)

| Column Name | Description | Example |
| :--- | :--- | :--- |
| `tra_id` | Unique Transaction ID | `TRA100001` |
| `date` | Date of Borrowing (`YYYY-MM-DD`) | `2025-04-12` |
| `user_id` | Unique Library Member ID | `USR1042` |
| `title` | Title of the Borrowed Book | `Atomic Habits` |
| `genre` | Book Category / Genre | `Self-Help` |
| `bor_dur` | Borrowing Duration (in days) | `12` |

---

## ⚙️ Installation

1. **Clone or Download the Project**
   Place `main.py` and `library_borrowing_transactions.csv` inside the same folder.

2. **Install Required Libraries**
   Run the following command in your terminal or command prompt:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```

---

## ▶️ How to Run

1. Open your terminal/command prompt and navigate to the project directory:
   ```bash
   cd path/to/Dataset
   ```

2. Run the Python script:
   ```bash
   python main.py
   ```
   *(On Windows, you can also use `py main.py`)*

3. **Using the Dashboard:**
   - First, select **`1`** to load your CSV file (`library_borrowing_transactions.csv`).
   - Choose options **`2` to `6`** to add records, view statistics, filter data, generate reports, or plot charts.
   - Select **`7`** to exit the dashboard.

---

## 👨‍💻 Author
- **Virendra Nakum**
 
