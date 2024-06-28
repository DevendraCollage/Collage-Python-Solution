# WAP to print multiplication table of given number.

mulTable = int(input("Enter the number you want multiplication table : "))

for i in range(1,11):
    print(f"{mulTable} x {(i)} = {mulTable*i}")