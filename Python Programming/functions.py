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
