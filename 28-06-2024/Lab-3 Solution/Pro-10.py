# WAP to find factors of the given number.

userFact = int(input("Enter the number here : "))

for i in range(1,userFact+1):
    if userFact % i == 0:
        print(i,",")