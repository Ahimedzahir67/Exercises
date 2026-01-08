# 1. [span_3](start_span)Create a Dictionary mapping month numbers to days[span_3](end_span)
month_days = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# 2. [span_4](start_span)Input Handling: Ask the user to input the month number[span_4](end_span)
month = int(input("Enter month number (1-12): "))

# 3. [span_5](start_span)Check and Output using if-else statements[span_5](end_span)
if month in month_days:
    if month == 2:
        # [span_6](start_span)Advanced Requirement: Leap Year Adjustment[span_6](end_span)
        # [span_7](start_span)Ask the user if it is a leap year[span_7](end_span)
        leap = input("Is it a leap year? (yes/no): ").strip().lower()
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        # [span_8](start_span)Print the number of days from the dictionary[span_8](end_span)
        print(f"There are {month_days[month]} days in month {month}.")
else:
    print("Invalid month number! Please enter a value between 1 and 12.")