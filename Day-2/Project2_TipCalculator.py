print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people wants to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

per_person_bill = (tip / 100 * bill + bill)/people
print("Each person should pay: $",round(per_person_bill,2))