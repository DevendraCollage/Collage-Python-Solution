# WAP to find whether the given number is prime or not.

userInput = int(input("Enter the number here : "))

flag = True

for i in range(2,userInput):
    if userInput % i == 0:
        flag = False
        break

if (flag):
    print(f"The {userInput} is Prime Number!")    
else:
    print(f"The {userInput} is not Prime Number!")    