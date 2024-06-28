# WAP to check whether the given number is palindrome or not

userInput = int(input("Enter the number here : "))

temp = userInput
rev = 0

while temp > 0:
    x = temp%10
    rev = rev * 10 + x
    temp = temp // 10

if rev == userInput:
    print(f"The Number {userInput} is Palindrome!")    
else:
    print(f"The Number {userInput} is Not Palindrome!")    