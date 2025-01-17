import math

def log(x,y =math.e):
    return math.log(x,y)
 
# Get input from the user
number = float(input("Enter the number: "))
base = input("Enter the base (default is e): ")

# Convert base input to float if provided, otherwise use default
base = float(base) if base else math.e

# Call the log function and print the result
result = log(number, base)
print(f"The logarithm of {number} with base {base} is {result}")
