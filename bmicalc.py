# the inputs

weight = float(input("Enter Your Weight: "))

height = float(input("Enter Your Height In Centimetres: "))

# the formula

bmi = weight / height ** 2

# conditional statements

if bmi <= 18:
    print("You Are Underweight")

elif bmi <= 29:
    print("Your BMI Is Normal")

elif bmi <= 33:
    print("You Are A Bit Underweight")

elif bmi <= 39:
    print("You Are Overweight")

elif bmi <= 48:
    print("You Are Obese")

else:
    print("You Are Extremely Diabolically Incredibly Immensely Substantially Hugely Enormously Obese")