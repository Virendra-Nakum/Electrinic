import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class ELibrary:
    def __init__(self, data_books=None, data_issues=None):
        self.data_books = data_books
        self.data_issues = data_issues

    def add_book(self):
        try:
            print()
            print("=" * 10)
            print("== Add a Book ==")
            print("=" * 10)

            title = input("Enter Book Title : ").lower()
            author = input("Enter Author Name : ")
            genre = input("Enter Book Genre : ")
            quantity = int(input("Enter Quantity of Book : "))

            new_book = {"Title": title,"Author": author,"Genre": genre,"Quantity": quantity}

            self.data_books = pd.concat([self.data_books, pd.DataFrame([new_book])],ignore_index=True)

            self.data_books.to_csv("books.csv", index=False)
            print("Book Added Successfully !!")
            print(self.data_books.tail(1))

        except  :
            print("Something Went Wrong !!")

    def update_inventory(self):
        try:
            print()
            print("=" * 10)
            print("== Update Book Quantity ==")
            print("=" * 10)

            title = input("Enter Book Name : ").lower()
            quantity = int(input("Enter New Quantity : "))

            if title in self.data_books["Title"].values:
                self.data_books.loc[self.data_books["Title"] == title, "Quantity"] = quantity

                self.data_books.to_csv("books.csv", index=False)
                print("Book Quantity Updated Successfully !!")
            else:
                print("Please Enter Valid Book Name !!")

        except :
            print("Please Enter Valid Quantity !!")
 

    def issue_book(self):
        try:
            print()
            print("=" * 10)
            print("== Issue a Book ==")
            print("=" * 10)

            title = input("Enter Book Name : ").lower()
            member = input("Enter Student Name : ")
            quantity = int(input("Enter Number of Books : "))
            date = input("Enter Issue Date (YYYY-MM-DD) : ")
 
 
            new_issue = {"Title": title,"Student": member,"Quantity Issued": quantity,"Date": date}

            self.data_issues = pd.concat([self.data_issues, pd.DataFrame([new_issue])],ignore_index=True)

            self.data_books.loc[self.data_books["Title"] == title, "Quantity"] -= quantity

            self.data_books.to_csv("books.csv", index=False)
            self.data_issues.to_csv("issues.csv", index=False)

            print("Book Issued Successfully !!")
 
        except  :
            print("Something Went Wrong !!")

    def generate_report(self):
        try:
            while True:
                print()
                print("=" * 10)
                print("== Generate Report ==")
                print("=" * 10)
                print("1. Books Available By Genre")
                print("2. Books Available By Author")
                print("3. Monthly Book Issues")
                print("4. Books Issued By Genre")
                print("5. Book Quantity Heatmap")
                print("6. Back To Main Menu")

                ch = int(input("Enter Your Choice : "))

                data = pd.merge(self.data_issues, self.data_books, on="Title")

                if ch == 1:
                    genre_books = self.data_books.groupby("Genre")["Quantity"].sum().reset_index()

                    sns.barplot(x=genre_books, y=genre_books.values)
                    plt.title("Books Available By Genre")
                    plt.xlabel("Genre")
                    plt.ylabel("Available Books")
                    plt.show()

                elif ch == 2:
                    author_books = self.data_books.groupby("Author")["Quantity"].sum().reset_index()

                    sns.barplot(x=author_books, y=author_books.values)
                    plt.title("Books Available By Author")
                    plt.xlabel("Author")
                    plt.ylabel("Available Books")
                    plt.xticks(rotation=45)
                    plt.show()

                elif ch == 3:
                    data["Date"] = pd.to_datetime(data["Date"])
                    data["Month"] = data["Date"].dt.to_period("M").astype(str)

                    monthly_issues = data.groupby("Month")["Quantity Issued"].sum().reset_index()

                    plt.plot(monthly_issues, monthly_issues.values, marker="o")
                    plt.title("Monthly Book Issues")
                    plt.xlabel("Month")
                    plt.ylabel("Books Issued")
                    plt.show()

                elif ch == 4:
                    genre_issues = data.groupby("Genre")["Quantity Issued"].sum().reset_index()

                    plt.pie(genre_issues.values,labels=genre_issues,autopct="%1.1f%%")
                    plt.title("Books Issued By Genre")
                    plt.show()

                elif ch == 5:
                    book_issues = data.groupby("Title")["Quantity Issued"].sum().reset_index()

                    book_quantity = self.data_books[["Title", "Quantity"]]
                    heatmap_data = pd.merge(book_quantity, book_issues, on="Title")
                    
                    correlation = heatmap_data[["Quantity", "Quantity Issued"]].corr()
                    sns.heatmap(correlation, annot=True, cmap="coolwarm")
                    plt.title("Book Quantity and Issues")
                    plt.show()

                elif ch == 6:
                    break
                else:
                    print("Please Enter Valid Choice !!")

        except :
            print("Something Went Wrong !!")

    def library_analysis(self):
        try:
            while True:
                print()
                print("=" * 10)
                print("== Library Analysis ==")
                print("=" * 10)
                print("1. Total Books Available")
                print("2. Total Books Issued")
                print("3. Most Issued Books")
                print("4. Book With Lowest Issues")
                print("5. Back To Main Menu")

                ch = int(input("Enter Your Choice : "))

                if ch == 1:
                    total_books = self.data_books["Quantity"].sum()
                    print("Total Books Available :", total_books)

                elif ch == 2:
                    total_issued = self.data_issues["Quantity Issued"].sum()
                    print("Total Books Issued :", total_issued)

                elif ch == 3:
                    top_books = self.data_issues.groupby("Title")["Quantity Issued"].sum().sort_values(ascending=False)
                    print(top_books)

                elif ch == 4:
                    low_books = self.data_issues.groupby("Title")["Quantity Issued"].sum().sort_values()

                    print("Book With Lowest Issues :")
                    if len(low_books) > 0:
                        print(low_books.idxmin())
                    else:
                        print("No Issue Records Available")

                elif ch == 5:
                    break
                else:
                    print("Invalid Choice !!")

        except :
            print("Something Went Wrong !!")

    def load_data(self):
        try:
            while True:
                print()
                print("=" * 10)
                print("== Data Loading and Data Cleaning ==")
                print("=" * 10)
                print("1. Load Data Sets")
                print("2. Check Missing Values")
                print("3. Fill Missing Values With 0")
                print("4. Drop Rows With Missing Values")
                print("5. First 5 Rows")
                print("6. Data Info")
                print("7. Back To Main Menu")

                ch = int(input("Enter Your Choice : "))

                if ch == 1:
                    self.data_books = pd.read_csv("books.csv")
                    self.data_issues = pd.read_csv("issues.csv")
                    print("DataSets Loaded Successfully !!")

                elif ch == 2:
                    print("Books Missing Values")
                    print(self.data_books.isna().sum())

                    print("Issues Missing Values")
                    print(self.data_issues.isna().sum())

                elif ch == 3:
                    self.data_books = self.data_books.fillna(0)
                    self.data_issues = self.data_issues.fillna(0)
                    print("Missing Values Filled Successfully !!")

                elif ch == 4:
                    self.data_books = self.data_books.dropna()
                    self.data_issues = self.data_issues.dropna()
                    print("Missing Rows Removed Successfully !!")

                elif ch == 5:
                    print(self.data_books.head())
                    print(self.data_issues.head())

                elif ch == 6:
                    self.data_books.info()
                    self.data_issues.info()

                elif ch == 7:
                    break
                else:
                    print("Invalid Choice !!")

                if ch in [3, 4]:
                    self.data_books.to_csv("books.csv", index=False)
                    self.data_issues.to_csv("issues.csv", index=False)

        except :
            print("Something Went Wrong !!")

    def main_menu(self):
        while True:
            print()
            print("===== E-Library Management System =====")
            print("1. Data Loading and Data Cleaning")
            print("2. Add New Book")
            print("3. Update Book Quantity")
            print("4. Issue a Book")
            print("5. Generate Report With Data Visualization")
            print("6. Library Analysis")
            print("7. Exit")

            try:
                choice = int(input("Enter Your Choice : "))

                if choice == 1:
                    self.load_data()
                elif choice == 2:
                    self.add_book()
                elif choice == 3:
                    self.update_inventory()
                elif choice == 4:
                    self.issue_book()
                elif choice == 5:
                    self.generate_report()
                elif choice == 6:
                    self.library_analysis()
                elif choice == 7:
                    print("Exiting From Program. Goodbye !!")
                    break
                else:
                    print("Invalid Choice !!")

            except :
                print("Please Enter a Number !!")

if __name__ == "__main__" :
    obj=ELibrary()
    obj.main_menu()
