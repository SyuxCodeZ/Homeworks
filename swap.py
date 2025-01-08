def swap_three(a, b, c):
    return c, a, b

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

num1, num2, num3 = swap_three(num1, num2, num3)

print("num1 =", num1)
print("num2 =", num2)
print("num3 =", num3)
