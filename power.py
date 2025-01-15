# Get input from the user
base = float(input("Enter The Number: "))
exponent = int(input("Enter The A Number To Calculate The Power: "))

# Initialize result
result = 1

# Calculate the power
for i in range(exponent):
  result = result * base

# Print the result
print(result)