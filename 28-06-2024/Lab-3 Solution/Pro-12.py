# WAP to print sum of digits of given number.

userN = int(input("Enter the number here : "))
temp = userN

sum = 0

for i in range(1,userN):
    sum = sum + (userN%10)
    userN = userN // 10

print(f"The Sum of the digit {temp} is {sum}")    
