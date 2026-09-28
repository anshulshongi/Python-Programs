'''#WAP to calculate factori of a given number
num = int(input("Enter a integer:"))
x = num
fact = 1
while x > 0:
    fact = fact * x
    x -= 1
print("Factorial of number", num, "is", fact)'''

#WAP using functions to calculate total, percentage and grade of student based on mark in five subjects
sub1 = float(input("Enter subject_1 marks:"))
sub2 = float(input("Enter subject_2 marks:"))
sub3 = float(input("Enter subject_3 marks:"))
sub4 = float(input("Enter subject_4 marks:"))
sub5 = float(input("Enter subject_5 marks:"))
max = int(input("Enter maximun marks adding all subjects:"))
def sum(a,b,c,d,e):
    return a+b+c+d+e
total = sum(sub1,sub2,sub3,sub4,sub5)
def percent(a,b):
    return (a/b)*100
percentage = percent(total,max)
def grade(a):
    if a>90:
        return "A"
    elif a<=90 and a>80:
        return "B"
    elif a<=80 and a>70:
        return "C"
    elif a<=60 and a>50:
        return "D"
    else:
        return "Fail"

print("Total marks obtained is",total)
print("Percentage obtained is",percentage)
print("Grade obtained is ",grade(percentage))