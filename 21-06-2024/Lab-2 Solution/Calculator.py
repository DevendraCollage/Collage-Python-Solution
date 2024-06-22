# WAP to implement simple calculator which performs (add,sub,mul,div) of two no. based on user input.

# Read two number from the user
num1 = int(input("Enter the number 1 here : "))
num2 = int(input("Enter the number 2 here : "))
# Read the operation from the user
print("+ : Addition")
print("- : Subtraction")
print("* : Multiplication")
print("/ : Division")
choice = input("Enter the choice from the above : ")

# According to the choice print the operation
match choice:
    case '+':
        print(f"{num1} + {num2} = {num1+num2}")
    case '-':
        print(f"{num1} - {num2} = {num1-num2}")
    case '*':
        print(f"{num1} * {num2} = {num1*num2}")        
    case '/':
        print(f"{num1} / {num2} = {num1/num2}")