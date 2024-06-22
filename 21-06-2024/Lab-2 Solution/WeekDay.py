# WAP in python to display the name of the day according to the number given by the user

# Read the week number from the user
weekDay = int(input("Enter the number here : "))

# Print day name according to the given number
match weekDay:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")        
    case 3:
        print("Tuesday")    
    case 4:
        print("Wednesday")        
    case 5:
        print("Thursday")    
    case 6:
        print("Friday")        
    case 7:
        print("Saturday")    