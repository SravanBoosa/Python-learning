'''x = int(input("Enter a number: "))
y = int(input("Enter another number: "))

x = x / y
y = y / x

print(y)'''

'''p=q=r=10
print(p,q,r)'''

'''def add(a,d):
    x = a
    y = d
    c = x + y
    print(c)
add(4,5)'''

#math is module in python which we can import to use the mathematical functions. 
#The math module provides access to the mathematical functions defined by the C standard.
'''import math 
num = 16
result = math.sqrt(num)
print(result)
print(int(result))'''

# if we want to import only a specific function from the math module, we can do it as follows:
'''from math import sqrt
num = 16
result = sqrt(num)
print(result)'''

'''import math
result = math.ceil(59.4) # ceil provide the value of the number rounded up to the nearest integer o/p is 60
result1 = math.floor(59.4) # floor provide the value of the number rounded down to the nearest integer o/p is 59
result2= math.pow(2,3) # pow provide the value of the number raised to the power of the other number o/p is 8
print(result)
print(result1)
print(result2)'''

#Ask for the user's first name and last name separately, then print the full name.
'''firstname= input("Enter first name :")
lastname= input("Enter last name :")
print("Fullname is: ", firstname +" kumar "+lastname)'''

#Ask for a word and print it in uppercase.
'''name= input("Enter name :")
print(name.upper())
print(name.lower())'''

#Ask for a sentence and print the number of characters in it
'''senti = str(input("Enter sentence :"))
print(len(senti))'''