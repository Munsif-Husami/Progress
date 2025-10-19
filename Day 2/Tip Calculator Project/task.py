print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10 12 15 "))
people = float(input("How many people to split the bill? "))
actual_bill = bill+(bill*(tip/100))
actual_split = (actual_bill/people)
actual_split = round(actual_split,4)
print(f"Each person should pay ${actual_split:.2f}")






