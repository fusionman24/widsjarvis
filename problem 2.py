import csv
import datetime
import matplotlib.pyplot as plt
import os

# Step 1: Define categories and initialize storage file
categories = ["Food", "Transportation", "Entertainment", "Utilities", "Others"]
filename = "expenses.csv"

# Ensure the file exists
if not os.path.exists(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])  # Header

# Step 2: Functions to add, edit, or delete expense entries
def add_expense(date, category, amount, description=""):
    if category not in categories:
        print(f"Invalid category! Choose from: {categories}")
        return
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    print("Expense added successfully.")

def view_expenses():
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def delete_expense(entry_no):
    with open(filename, mode='r') as file:
        rows = list(csv.reader(file))
    if 0 < entry_no < len(rows):
        del rows[entry_no]
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Expense deleted successfully.")
    else:
        print("Invalid entry number.")

# Step 3: Summary and report functions
def summarize_by_category():
    summary = {category: 0 for category in categories}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            category, amount = row[1], float(row[2])
            summary[category] += amount
    return summary

def total_spending(period="monthly"):
    today = datetime.date.today()
    total = 0
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            date = datetime.datetime.strptime(row[0], "%Y-%m-%d").date()
            amount = float(row[2])
            if period == "monthly" and date.year == today.year and date.month == today.month:
                total += amount
            elif period == "weekly" and (today - date).days <= 7:
                total += amount
    return total

# Step 4: Visualize spending
def visualize_spending():
    summary = summarize_by_category()
    categories, amounts = summary.keys(), summary.values()
    plt.figure(figsize=(8, 5))
    plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
    plt.title("Spending by Category")
    plt.show()

# Example Usage
if __name__ == "__main__":
    # Add some dummy data (You can use inputs for actual usage)
    add_expense("2024-12-01", "Food", 250, "Lunch at a restaurant")
    add_expense("2024-12-05", "Transportation", 50, "Bus fare")
    add_expense("2024-12-03", "Entertainment", 100, "Movie ticket")

    print("\n--- Viewing All Expenses ---")
    view_expenses()

    print("\n--- Total Spending (Monthly) ---")
    print(f"Total: {total_spending('monthly')}")

    print("\n--- Spending by Category ---")
    print(summarize_by_category())

    print("\n--- Visualizing Spending ---")
    visualize_spending()
