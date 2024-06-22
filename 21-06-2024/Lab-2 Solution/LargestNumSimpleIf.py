# WAP to find out largest number from the given three number

# Read the three numbers from the user
num1 = int(input("Enter the number 1 here : "))
num2 = int(input("Enter the number 2 here : "))
num3 = int(input("Enter the number 3 here : "))

# Find out the largest number from given three numbers
if num1 > num2 and num1 > num3:
    print(f"The {num1} is Greatest Among them!")
elif num2 > num3:
    print(f"The {num2} is Greatest Among them!")    
else:
    print(f"The {num3} is Greatest Among them!")    