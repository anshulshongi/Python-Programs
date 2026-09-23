#functions in python 

def square(n):
    '''return square of number'''
    result = n*n
    print(square.__doc__)
    print(result)
square(4)


def add(a,b):
   return a+b
print(add(4,5))

def calc(a,b):
  return a+b ,a*b,a-b
x,y,z=(calc(10,5))
print(x)
print(y)
print(z)

def greet():
   print("Hello everyone, Welcome to Python")
greet()

square = lambda x : x*x
print(square(5))

add = lambda y,z : y+z
print(add(2,3))

#write a function calculator function accept two numbers and an operator and perform addition, subtraction, multiplication, and division
'''a=int(input("Enter a number"))
b=int(input("enter second number"))
c=input('Enter operation')
def calculator(a,b):
   if c=="+":
      return a+b
   elif c=="-":
      return a-b
   elif c=="*":
      return a*b
   elif c=="/":
      return a/b

print(calculator(a,b))'''

#write a function that accepts two numbers and return largest number
a=int(input("Enter a number:"))
b=int(input("Enter second number:"))
def largest(a,b):
   return max(a,b)
print("largest number is",largest(a,b))


#Function that accepts a nymber and checks whether uf it is even or odd
a=int(input("Enter a number:"))
def even_odd(a):
   if a%2==0:
      return "number is even."
   else :
      return "number is odd."
print(even_odd(a))