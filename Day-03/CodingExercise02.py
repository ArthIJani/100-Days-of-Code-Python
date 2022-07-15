#BMI Calulator 2.0
height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
  print(f"Your BMI is {bmi}, You are Underweight")
elif bmi < 25:
  print(f"Your BMI is {bmi}, You are Normal Weight")
elif bmi < 30:
  print(f"Your BMI is {bmi}, You are Over Weight")
elif bmi < 35:
  print(f"Your BMI is {bmi}, You are Obese")
else:
  print(f"Your BMI is {bmi}, You are Clinically Obese")