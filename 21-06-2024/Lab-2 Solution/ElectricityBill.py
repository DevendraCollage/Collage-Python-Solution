'''
WAP to calculate electricity bill based on following criteria. Which takes the unit from the user.
a. First 1 to 50 units = Rs. 2.60/unit</br>
b. Next 50 to 100 units = Rs. 3.25/unit</br>
c. Next 100 to 200 units = Rs. 5.26/unit</br>
d. above 200 units = Rs. 8.45/unit
'''

#? Read the electricity unit from the user
unit = int(input("Enter the electricity unit : "))
bill = 0;

#? Calculate the bill of the given user unit
if unit<=50:
    bill = 2.60 * unit
    print("1 unit electricity unit price : Rs.2.60/unit")
    print(f"Your {unit} unit price is : {bill}")
elif unit<=100:
    bill = 50 * 2.60 + (unit-50) * 3.25
    print("1 unit electricity unit price : Rs.2.60/unit")
    print(f"Your {unit} unit price is : {bill}")
elif unit<=200:
    bill = 50 * 2.60 + 50 * 3.25 + ((unit-100) * 5.26)
    print("1 unit electricity unit price : Rs.2.60/unit")
    print(f"Your {unit} unit price is : {bill}")
else:
    bill = 50 * 2.60 + 50 * 3.25 + 100 * 5.26 + (8.45 * (unit-200))           
    print("1 unit electricity unit price : Rs.2.60/unit")
    print(f"Your {unit} unit price is : {bill}")  