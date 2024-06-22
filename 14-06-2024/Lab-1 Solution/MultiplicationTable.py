# WAP to print the multiplication table of the given number by the user.

# Function to print the multiplication table
def mul_table(n,i):
    if i > 10:
        return
    print(f"{n} x {i} = {n*i}")
    mul_table(n, i+1)

n = int(input("Enter the number here : "))

# Call the function and print the result
mul_table(n,1)