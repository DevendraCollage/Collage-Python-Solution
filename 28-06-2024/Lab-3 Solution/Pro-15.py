# WAP to find armstrong number of given number

userInput = input("Enter the number here : ")

digit = int(userInput)
count = len(str(userInput))
sum = 0

for i in range(1,count+1):
    x = digit % 10
    sum = sum + x**count
    digit = digit // 10

if sum == int(userInput):
    print("Palindrome!")    
else:
    print("Not!")    