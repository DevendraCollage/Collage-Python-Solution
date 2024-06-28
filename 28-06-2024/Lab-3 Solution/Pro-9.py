# WAP to find factorial of the given number.

factNum = int(input("Enter the number here : "))

fact = 1

for i in range(1,factNum):
    fact = fact * (i+1)

print(f"The Factorial of {factNum} = {fact}")    