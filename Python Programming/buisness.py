'''age=int(input("Enter Your Age:"))
day=input("Enter week day:\n(eg; mon,tue,thur,fri,sat,sun)\n")
price=0
if day==("sat" or "sun"):
    price=price-2

if age<12:
    price += 8
elif age>=12 and age<=59:
    price += 12
elif age>=60:
    price += 9
print("Your Ticket Price is $",price)'''

a=float(input("Enter First Side of Triangle:"))
b=float(input("Enter Second Side of Triangle:"))
c=float(input("Enter Trird Side of Triangle:"))
if a+b>c and b+c>a and a+c>b :
    if a==b==c:
        print("Triangle is Equilatrol triangle.")
    elif a==b or a==c or b==c:
        print("Triangle is Isosceles triangle.")
    else:
        print("Triangle is Scalene.")
else:
    print("Not a Valid Triangle.")
