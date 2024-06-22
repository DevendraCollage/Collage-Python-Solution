# WAP to print the percentage of te given student.

# Get the marks of the five subject from the user
ca = float(input("Enter the marks of Computer Algorithms : "))
flutter = float(input("Enter the marks of Flutter : "))
python = float(input("Enter the marks of Python : "))
dotnet = float(input("Enter the marks of .Net : "))
iat = float(input("Enter the marks of Advanced Technologies : "))

# Calculate the total marks and print 
total = ca + flutter + python + dotnet + iat
print("The total of the given subject marks is : ",total)

# Calculate the percentage and print
percentage = total / 5
print("The percentage of the given marks is : ",percentage,"%")