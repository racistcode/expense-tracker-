from database import create_table
from expenses import add_expense


def main():
    create_table()

    print("================================")
    print("       EXPENSE TRACKER")
    print("================================")

    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    description = input("Enter description: ")

    add_expense(amount, category, description)

    print("\nExpense added successfully!")


if __name__ == "__main__":
    main()