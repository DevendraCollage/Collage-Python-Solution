# WAP to purposefully raised and error and correct it.

# This here i will generate the Indentation error :
num1 = int(input("Enter the number 1 here : "))
num2 = int(input("Enter the number 2 here : "))
# if(num1 > num2):
# print("Number 1 Greater Among Them!") # This generate an Indentation error
# else:
# print("Number 2 is Greater Among Them!")  # This generate an Indentation error

# This is right code to solve the Indentation error in the above code
if(num1 > num2):
    print("Number ", num1, " Greater Among Them!") 
else:
    print("Number", num2, "Greater Among Them!")