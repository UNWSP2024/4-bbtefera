# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
  budget = float(input("Enter your monthly budget: "))
total_expenses = 0

while (expense := input("Enter expense (or 'done' to finish): ").lower()) != 'done':
        total_expenses += float(expense)

balance = budget - total_expenses
print(f"\nBudget: ${budget:.2f}\nExpenses: ${total_expenses:.2f}\nBalance: ${balance:.2f}")
print("Under budget!" if balance > 0 else "Over budget!" if balance < 0 else "Exactly on budget!")

    ######################


if __name__ == '__main__':
    main()
