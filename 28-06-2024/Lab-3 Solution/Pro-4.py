# WAP to print numbers between two given numbers which is divisible by 2 but not divisible by 3

start = int(input("Enter the start range : "))
end = int(input("Enter the end range : "))

for i in range(start, end):
    if i%2==0 and i%3!=0:
        print(i)