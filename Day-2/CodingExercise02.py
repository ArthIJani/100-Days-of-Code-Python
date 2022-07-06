#BMI Calculator
height = float(input("Enter your height in m: "))
weight = int(input("Enter your weight in kg: "))
bmi = weight / (height ** 2)
print(int(bmi))