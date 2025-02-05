# enter your bill amount

bill = int(input("Enter Your Bill: "))

# conditional statements

if bill == 0:
    pass
elif bill > 100:
    print ("Your Bill Is Due In 3 Days")
elif bill > 500:
    print ("Your Bill is Due Tomorrow")
elif bill > 1000:
    print ("Your Bill is Due Next Week")   
elif bill > 1500:
    print ("Your Bill is Due Next Week And A Half")
elif bill > 2000:
    print ("Your Bill is Due Next Month")
else:
    print ("your bill is due next year")