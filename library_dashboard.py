import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime as dt

class Library:
    def __init__(self, tra_id=None, user_id=None, title=None, genre=None, bor_dur=None, date=None):
        self.tra_id = tra_id
        self.date = date
        self.user_id = user_id
        self.title = title
        self.genre = genre
        self.bor_dur = bor_dur

    def display(self):
        print(f"Transaction ID  : {self.tra_id}")
        print(f"Date            : {self.date}")
        print(f"User ID         : {self.user_id}")
        print(f"Title           : {self.title}")
        print(f"Genre           : {self.genre}")
        print(f"Borrow Duration : {self.bor_dur} days")


class Management(Library):
    def __init__(self, tra_id=None, user_id=None, title=None, genre=None, bor_dur=None, date=None):
        super().__init__(tra_id, user_id, title, genre, bor_dur, date)
        self.data = pd.DataFrame()

    def load_data(self):
        file_name = input("Enter CSV File Name :- ").strip()
        try:
            self.data = pd.read_csv(file_name)
            self.data["date"] = pd.to_datetime(self.data["date"])
            print("Dataset Loaded Successfully!")
            return self.data
        except FileNotFoundError:
            print("File Not Found!")
            return pd.DataFrame()

    def add_books(self):
        try:
            tra_id = input("Enter Transaction ID :- ").strip()
            user_id = input("Enter User ID :- ").strip()
            name = input("Enter Book Title :- ").strip()
            genre = input("Enter Genre Name :- ").strip()
            bor_dur = int(input("Enter Borrowing Duration (days) :- ").strip())
            date = pd.to_datetime(dt.now().strftime("%Y-%m-%d"))

            self.tra_id = tra_id
            self.user_id = user_id
            self.title = name
            self.genre = genre
            self.bor_dur = bor_dur
            self.date = date

            row = {
                "tra_id": tra_id,
                "date": date,
                "user_id": user_id,
                "title": name,
                "genre": genre,
                "bor_dur": bor_dur,
            }

            self.data = pd.concat([self.data, pd.DataFrame([row])], ignore_index=True)
            print("Data Added Successfully!")
            return row

        except ValueError:
            print("Enter Valid Info (Borrowing Duration must be a number).")

    def calculate_statistics(self):
        if self.data.empty:
            print("Please Load Dataset First !")
            return

        dur = np.array(self.data["bor_dur"], dtype=float)
        average = np.mean(dur)
        std = np.std(dur)
        maximum = np.max(dur)

        print("\n--- LIBRARY STATISTICS ---")
        print(f"Average Borrow Duration   : {average:.2f} days")
        print(f"Std Dev of Borrow Time    : {std:.2f} days")
        print(f"Max Borrow Duration       : {int(maximum)} days")

    def filter_transactions(self):
        if self.data.empty:
            print("No Data available!")
            return

        try:
            print("Filter Data")
            print("1. Genre")
            print("2. Date Range")
            print("3. Min Duration")

            choice = input("Enter choice (1/2/3) :- ").strip()

            if choice == "1":
                genre = input("Enter Genre :- ").strip()
                result = self.data[self.data["genre"].str.lower() == genre.lower()]

            elif choice == "2":
                start = input("Start Date (YYYY-MM-DD) :- ").strip()
                end = input("End Date (YYYY-MM-DD) :- ").strip()
                result = self.data[(self.data["date"] >= start) & (self.data["date"] <= end)]

            elif choice == "3":
                days = int(input("Enter Minimum Days :- "))
                result = self.data[self.data["bor_dur"] >= days]

            else:
                print("Invalid choice!")
                return

            if result.empty:
                print("No matching records found.")
            else:
                print(result.head(20).to_string(index=False))

        except ValueError:
            print("Invalid input! Please check date format or number.")

    def generate_report(self):
        if self.data.empty:
            print("No Data available.")
            return

        print("\n--- E-LIBRARY REPORT ---")
        print("Total Transactions :", len(self.data))
        print("Unique Users       :", self.data["user_id"].nunique())
        print("Unique Books       :", self.data["title"].nunique())
        print("Late Returns (>14d):", (self.data["bor_dur"] > 14).sum())

        print("\nTop 3 Genres:")
        print(self.data["genre"].value_counts().head(3))
        print("------------------------")

    def show_visualizations(self):
        if self.data.empty:
            print("No Data available for visualization.")
            return

        print("\n=== Select Graph to View ===")
        print("1. Bar Chart (Top 5 Books)")
        print("2. Line Graph (Monthly Trend)")
        print("3. Pie Chart (Books by Genre)")
        print("4. Heatmap (Day vs Genre)")

        try:
            choice = input("Enter Choice (1-4) :- ").strip()

            if choice == "1":
                plt.figure(figsize=(8, 5))
                top_books = self.data["title"].value_counts().head(5)
                sns.barplot(x=top_books.values, y=top_books.index)
                plt.title("Top 5 Most Borrowed Books")
                plt.xlabel("Count")
                plt.ylabel("Book Title")
                plt.show()

            elif choice == "2":
                plt.figure(figsize=(10, 5))
                monthly = self.data["date"].dt.to_period("M").value_counts().sort_index()
                plt.plot(monthly.index.astype(str), monthly.values, marker="o")
                plt.title("Monthly Borrowing Trend")
                plt.xlabel("Month")
                plt.ylabel("Total Borrowings")
                plt.xticks(rotation=45)
                plt.show()

            elif choice == "3":
                plt.figure(figsize=(7, 7))
                genre_counts = self.data["genre"].value_counts()
                plt.pie(genre_counts.values, labels=genre_counts.index, autopct="%1.1f%%")
                plt.title("Books by Genre")
                plt.show()

            elif choice == "4":
                plt.figure(figsize=(8, 5))
                day_name = self.data["date"].dt.day_name()
                table = pd.crosstab(day_name, self.data["genre"])
                sns.heatmap(table, annot=True, fmt="d", cmap="YlGnBu")
                plt.title("Borrowing by Day & Genre")
                plt.show()

            else:
                print("Invalid Choice! Please enter 1 to 4.")

        except Exception as e:
            print("Error:", e)


obj = Management(tra_id=None, user_id=None, title=None, genre=None, bor_dur=None, date=None)

while True:
    print("\n================ E-Library Data Insights Dashboard ================")
    print("1. Load CSV Dataset")
    print("2. Add New Transaction")
    print("3. Calculate Statistics")
    print("4. Filter Transactions")
    print("5. Generate Summary Report")
    print("6. Show Visualizations")
    print("7. Exit")

    try:
        choice = input("Enter Choice (1-7) :- ").strip()

        if choice == "1":
            obj.load_data()

        elif choice == "2":
            obj.add_books()

        elif choice == "3":
            obj.calculate_statistics()

        elif choice == "4":
            obj.filter_transactions()

        elif choice == "5":
            obj.generate_report()

        elif choice == "6":
            obj.show_visualizations()

        elif choice == "7":
            print("Exiting Dashboard. Goodbye!")
            break

        else:
            print("Invalid Choice! Please enter a number from 1 to 7.")

    except Exception as e:
        print("Something Went Wrong:", e)
