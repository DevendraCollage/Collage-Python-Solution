# WAP to convert the fahrenheit to celsius and vice versa.

# Read the fahrenheit from the user
fahrenheit = float(input("Enter the fahrenheit here : "))
# Convert given fahrenheit into celsius
c = (fahrenheit - 32) * (5/9)
# Print the converted temperature
print("Fahrenheit to Celsius : ", c)

# Read the celsius from the user
celsius = int(input("Enter the celsius here : "))
# Convert given celsius to fahrenheit
f = (celsius*9/5)+32
print("Celsius to Fahrenheit :",f)