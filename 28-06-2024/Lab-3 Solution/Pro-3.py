# WAP to print odd numbers between 1 to n

userN = int(input("Enter the number you want to print : "))

for i in range(0,userN):
    if i%2!=0:
        print(i)