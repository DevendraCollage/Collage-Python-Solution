# WAP to check whether the last digit is divisible by 2 or not

# Read the number from the user
num = int(input("Enter the number here : "))

# Get the last digit of the given number
lastDig = num % 10

# Check the last digit is divisible by 2 or not
if lastDig % 2 == 0:
    print(f"The {lastDig} is Divisible by 2!")
else:
    print(f"The {lastDig} is not Divisible by 2!")    