# WAP to check whether the given year is leap year or not

# Read the year from the user
year = int(input("Enter the year here : "))

# Check the year is leap or not
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"The {year} is Leap year!")
else:
    print(f"The {year} is not Leap year!")    