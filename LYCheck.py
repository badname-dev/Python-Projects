a = int(input("Enter the year: "))
if a%4==0 & a%400==0 or a%400==0:
    print("Leap Year")
else:
    print("Not a Leap Year")