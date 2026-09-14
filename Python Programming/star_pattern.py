'''
j="* "
for i in range(1,5):
    print(j)
    j=j+"* "

for i in "*":
    print(i)
    for j in "*":
        print(i,j)
        for k in "*":
            print(i,j,k)
            for l in "*":
                print(i,j,k,l)'''
'''
for i in range(1,5):
    for j in range(i):
        print("*", end =" ")
    print()'''
'''
for i in range(4,0,-1):
    for j in range(i):
        print("*", end =" ")
    print()
'''
'''n=5
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1 :
            print("*",end="  ")
        else:
            print(" ",end="  ")
    print()'''


'''for i in range(1,6):
    for j in range(i):
        print(i, end =" ")
    print()'''
'''
n=6
for i in range(1,n):
    for j in range(1,n):
        print("*",end="  ")
    print()'''
'''
for i in range(1,6):
    print("  "*(5-i), end ="")
    for j in range(i):
        print(" *", end="")
    print()


i=1
while i<6:
    print("  "*(5-i),end="")
    j=0
    while j<i:
        print(" *",end="")
        j+=1
    print()
    i+=1
'''



'''a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i==7:
        print("Found")
        break
else:
    print("Not Found")
'''
'''
b=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in b:
    if i%2==0:
        continue
    elif i==9:
        break
    print(i)
'''


'''num=[1,2,-3,-4,5,6,-3,0]
for i in num:
    if i<0:
        continue
    print(i'''


'''
for i in range(1,4):
    for j in range(1,11):
        print(i*j,end=" ")
    print()
'''
'''
a=[1,2,3,4,5,6,7,8,9]
for i in a:
    if i==8:
        print("Number mil gaya")
        break
else:
    print("Hum pe to hai hi na")



for i in range(1,6):
    if i==3:
        pass
    print(i)
'''

list=[1,2,3,4,5,6,7,8,9,10,11,2,77,2,8,78,]
largest=list[0]
for i in list:
    if i > largest:
        largest=i
print(largest)
