print("Floyd's Triangle\n")

num_of_rows = int(input("Enter the number of rows you'd like: "))

z = 0

for x in range(1, num_of_rows + 1):

    print(" " * (num_of_rows - x), end="")

    for y in range(x):
        z += 1
        print(z, end=" ")

    print()
