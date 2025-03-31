weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in m: "))
bmi = weight / height**2

if bmi < 18.5:
    print(f"your BMI is {'%.0f'%bmi}, you are underweight")
elif bmi < 25:
    print(f"your BMI is {'%.0f'%bmi}, you are normal weight")
elif bmi < 30:
    print(f"your BMI is {'%.0f'%bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"your BMI is {'%.0f'%bmi}, you are obese")
else:
    print(f"your BMI is {'%.0f'%bmi}, you are clinically obese")
