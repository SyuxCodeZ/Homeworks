# Program to convert multiple decimal numbers to binary
print("Enter decimal numbers separated by spaces:")
user_input = input()  # Get input from the user
number_strings = user_input.split()  # Split the input into a list of strings

# Outer loop: Process each number
for num_str in number_strings:
    decimal = int(num_str)  # Convert the string to an integer
    binary = ""  # Start with an empty binary string

    # Inner loop: Convert the number to binary
    while decimal > 0:
        remainder = decimal % 2  # Find the remainder
        binary = str(remainder) + binary  # Add remainder to the binary string
        decimal = decimal // 2  # Divide the number by 2

    # Print the binary result
    print(f"Binary of {num_str} -> {binary}")
