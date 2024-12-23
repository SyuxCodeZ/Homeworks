# the print and inputs

print("~~~Temparature Check~~~~")

temp = int(input("Please Enter The Temparature: "))

# the conditional statements

if temp >= 30:
    print("It Is Definitely Summer In Your Place")

elif temp <= 10:
    print("It Is Definitely Winter In Your Place")

else:
    print(f"{temp} is not valid")