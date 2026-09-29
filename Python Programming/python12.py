'''#WAP to calculate factori of a given number
num = int(input("Enter a integer:"))
x = num
fact = 1
while x > 0:
    fact = fact * x
    x -= 1
print("Factorial of number", num, "is", fact)'''
'''
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
def Grade(a):
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
grade = Grade(percentage)

print("Total marks obtained is",total)
print("Percentage obtained is",percentage)
print("Grade obtained is ",grade)
'''

#Write a function to  calculate area of circle
'''
r = float(input("Enter radius of circle:"))
def area(a):
    return 3.1416*r**2
print("Area of circle is",area(r))'''

'''#Write a function to cheack whether a string is pallidrome
s = input("Enter a word:")
b = s[::-1]
def pal(a):
    if s.upper()==b.upper():
        return "Word is a pallindrome"
    else:
        return "Word is not a pallindrome"
print(pal(s))
print(b)
'''
#Write a function to find maximum eliment in a list without using max function.
l=[1,2,23,43,12,54,78,56]
def large(a):
    a.sort()
    return a[-1]
print(large(l))