# WAP to print fibonacci series for the given number n

userInput = int(input("Enter the number you want fibonacci : "))

n1 = 0
n2 = 1

print(n1)
print(n2)

for i in range(1,userInput):
    new = n1 + n2
    n1 = n2
    n2 = new
    print(new)