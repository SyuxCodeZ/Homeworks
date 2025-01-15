# input variable

num = int(input("Enter A Number: "))

# initialized variable

count = 0

# while loop statement

while num != 0:

    num = num // 10
    
    count = count + 1

# finally print statement for ending

print (f"\nThe Amount Of Digits In The Given Number Is {count}")