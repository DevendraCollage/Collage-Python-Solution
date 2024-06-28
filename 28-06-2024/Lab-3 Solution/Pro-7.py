# WAP to print sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n

userInput = int(input("Enter the range you want to print : "))

sum = 0

for i in range(1,userInput+1):
    if i % 2 == 0:
        sum = sum - i
    else:
        sum = sum + i

print(f"The Sum is : {sum}")            