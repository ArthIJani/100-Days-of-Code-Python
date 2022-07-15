#life in weeks
age = int(input("What is your current age: "))
yearsleft = 90 - age
days = 365 * yearsleft
weeks = 52 * yearsleft
months = 12 * yearsleft
print(f"You have {days} days, {weeks} weeks and {months} months left")