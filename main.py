"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    return annual_cost / (SEMESTERS_PER_YEAR * CLASS_DAYS_PER_SEMESTER)


def cost_per_credit(annual_cost, credits):
    return annual_cost / (SEMESTERS_PER_YEAR * credits)


def cost_per_class(annual_cost, credits):
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


def cost_per_minute(annual_cost):
    return annual_cost / (SEMESTERS_PER_YEAR * CS1430_MEETINGS_PER_SEMESTER * 50)
# ---- PROGRAM ----

def main():
    annual_cost = float(input("Cost of College per year: "))
    credits = int(input("Credits this semester: "))

    while True:
        print("1 Per semester")
        print("2 Per month")
        print("3 Per class day")
        print("4 Per credit")
        print("5 Per CS 1430 class")
        print("6 Per minute in CS 1430 class")
        print("Q Quit")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            print(f"{cost_per_semester(annual_cost):.2f}")
        elif choice == "2":
            print(f"{cost_per_month(annual_cost):.2f}")
        elif choice == "3":
            print(f"{cost_per_day(annual_cost):.2f}")
        elif choice == "4":
            print(f"{cost_per_credit(annual_cost, credits):.2f}")
        elif choice == "5":
            print(f"{cost_per_class(annual_cost, credits):.2f}")
        elif choice == "6":
            print(f"{cost_per_minute(annual_cost):.2f}")
        else:
            print("Not an option")

        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
