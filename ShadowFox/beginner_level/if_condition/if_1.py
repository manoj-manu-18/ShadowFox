# BMI Calculator with If-Elif-Else Conditions
height = float(input("Enter the Height in Meters: "))
weight = float(input("Enter the Weight in Kg: "))

bmi = weight / (height ** 2)
print("BMI:", bmi)
    
if bmi >= 30:
    print("Obesity")
elif 25 <= bmi < 30:
    print("Overweight")
elif 18.5 <= bmi < 25:
    print("Normal")
else:
    print("Underweight")