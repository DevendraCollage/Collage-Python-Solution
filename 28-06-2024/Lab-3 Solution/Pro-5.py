# WAP to print sum of 1 to n numbers

userInp = int(input("Enter the number you want the sum : "))

sum = 0

for i in range(0,userInp):
    sum = sum + (i+1)

print(f"The sum of 1 to {userInp} = {sum}")    