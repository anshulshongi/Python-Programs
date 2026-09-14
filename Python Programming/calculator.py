c=1
while c==1:
    num1 = float (input("Enter a number: "))
    num2 = float (input("Enter second number: "))
    choice = int(input("Enter opration you want to perform\n 1. Addition\n 2. Subtraction\n 3. Division\n 4. Multiplication\n  Enter Choice: "))
    if choice == 1:
      print(num1,"+",num2,"= ",num1+num2)
    elif choice == 2:
      print(num1,"-",num2,"= ",num1-num2)
    elif choice == 3:
       print(num1,"/",num2,"= ",num1/num2)
    elif  choice == 4:
       print(num1,"*",num2,"= ",num1*num2)
    else:
       print("invalid choice")
    c=int(input("do want to calculate next values (1 for yes/0 for no):"))