def Add(a,b):
    return a+b
def Sub(a,b):
    return a-b
def Mult(a,b):
    return a*b
def Div(a,b):
    return a/b
def Mod(a,b):
   return a%b
new=1
while new==1:
    num1 = float (input("Enter a number: "))
    num2 = float (input("Enter second number: "))
    choice = int(input("Enter opration you want to perform\n 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Modules\n Enter Choice: "))
    if choice == 1:
      print(num1,"+",num2,"= ",Add(num1,num2))
    elif choice == 2:
      print(num1,"-",num2,"= ",Sub(num1,num2))
    elif choice == 3:
       print(num1,"*",num2,"= ",Mult(num1,num2))
    elif  choice == 4:
       if num2 == 0:
          print("Can't Divide by Zero")
       else:
          print(num1,"/",num2,"= ",Div(num1,num2))
    elif  choice == 5:
        print(num1,"*",num2,"= ",Mod(num1,num2))
    else:
       print("invalid choice")
    new=int(input("do want to calculate next values (1 for yes/0 for no):"))