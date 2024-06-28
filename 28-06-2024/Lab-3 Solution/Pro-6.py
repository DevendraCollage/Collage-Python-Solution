# WAP to print sum of series 1 + 4 + 9 + 16 + 25 + 36 + ...n

userInput = int(input("Enter the range you want to print : "))
sum = 0

for i in range(1, userInput+1):
    sum = sum + i**2 # This is the power of the i

print(sum)    