# WAP to find out largest number from given two numbers using simple if and ternary operator.

# Read the two numbers from the user
num1 = int(input("Enter the number 1 : "))
num2 = int(input("Enter the number 2 : "))

# Find largest number using simple if
if num1 > num2:
    print(f"The {num1} is Greatest Among Them!")
else:
    print(f"The {num2} is Greatest Among Them!")    

# Find largest number using ternary operator
print(f"The {num1} is Greatest Among them!") if num1 > num2 else print(f"The {num2} is Greatest Among Them!")    