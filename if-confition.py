'''num = int(input("Enter a number: "))
if(num%2 == 0):
    print("The number is even")
else:
    print("The number is odd")

num=20
if (num==20):
    print("BINGO!")
elif (num!=20):
    print("MISSED!")'''

'''num1=int(input("Enter the number1 "))
num2=int(input("Enter the number2 "))
num3=int(input("Enter the number3 "))
if(num1>num2 and num1>num3):
    print("largest number is", num1)
elif(num2>num1 and num2>num3):
    print("largest number is", num2)
else:
    print("largest number is", num3)'''

'''input1=int(input("Enter the number1 "))
input2=int(input("Enter the number2 "))
if(input1 == input2):
    print("Jinx")
else:
    print("Not Jinx")'''  

'''country = input("Enter the country name : ")
if(country == "brazil"):
   print("1958,1962,1970,1994,2002")
elif(country == "italy"):
   print("1934,1938,1982,2006")
elif(country == "france"):
    print("1998,2018")
elif(country == "germany"):
    print("1954,1974,1990,2014")
else:
     print("I don't know")'''  

'''age=int(input("Enter the age of the voter:"))
if(age>=18):
    print("eligibale to vote")
else:
    print("Not eligible to vote")'''

'''num = int(input("Enter the number:"))
if(num%5 == 0):
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")'''
 
'''number = int(input("Enter the number: "))
if(number>0):
    print("The number is positive", number)
elif(number<0):
    print("The number is negative", number)
else:
    print("The number is zero", number)'''

'''marks = int(input("Enter the marks of the student: "))
if(marks>=35):
    print("Pass")
elif(marks<35):
    print("Fail")'''

'''num= float(input("Enter number:"))
if(num%5==0):
   print("Divisible by 5")'''

'''num1 = int(input("Enter number:"))
num2 = int(input("Enter number:"))
if(num1>num2):
    largest_number = num1
else:
    largest_number = num2
print("larger number is", largest_number)''' 

'''colour = input("Enter colour :")
if(colour == "Red"):
    print("Stop")
elif(colour == "Green"):
    print("Go")
elif(colour == "Yellow"):
    print("wait")
else:
    print("Invalid signal")'''

#Leap Year - It is divisible by 400, or 4
'''year = int(input("Enter year :"))
if(year%4==0):
    print("Leap Year")
else:
    print("Not a Leap Year")'''


'''marks=int(input("Enter marks : "))
if(marks>=90):
    print("it is grade A")
elif(90>marks>=80):
    print("it is grade B")
elif(80>marks>=70):
    print("it is grade C")
elif(70>marks):    
    print("it is grade D")'''


#. Positive, Negative, or Zero
'''num=int(input("Enter nuber : "))
if(num==0):
    print("number is zero")
elif(num>0):
    print("number is positive")
elif(num<0):
    print("number is negative")
print("end")'''    

#Take a number and check whether it is divisible by both 3 and 5, divisible by only one of them, or divisible by neither.

'''n1=int(input("enter number : "))
if(n1%3==0 and n1%5==0):
    print("divisible by both numbers")
elif(n1%3==0 or n1%5==0):
    print("divisible by one of them")
else:
   print("divisible by neither")'''

#Take three numbers and print the largest. Also handle the case where all three numbers are equal.

'''n1=int(input("enter first number "))
n2=int(input("enter second number "))
n3=int(input("enter third number "))
if(n1==n2==n3):
    print("All numbers are equal")
elif(n1>=n2 and n1>=n3):
    print("n1 is largest number")
elif(n2>=n3 and n2>=n1):
    print("n2 is largest number")
else:
    print("n3 is largest number")
print("end")'''

#Take a year and determine whether it is a leap year.
#Hint: A year divisible by 400 is a leap year. A year divisible by 100 but not 400 is not. Other years divisible by 4 are leap years.    

'''year = int(input("enter year "))
if(year%400==0):
    print("Leap Year")
elif(year%100==0):
    print("Not leap year")
elif(year%4==0):
    print("leap Year")
else:
    print("Not leap yar")
print("end")'''

#Simple Calculator
#Take two numbers and an operator (+, -, *, /). Use conditional statements to perform the operation. Handle division by zero and invalid operators.

'''n1=float(input("enter first number :"))
n2=float(input("enter second number :"))
operator=input("enter operator(+,-,*,/,//,%):")

if(operator == "+"):
    print("add", n1+n2)
elif(operator == "-"):
    print("subtraction", n1-n2)
elif(operator == "*"):
    print("Multiplication", n1*n2)
elif(operator == "/"):
    if(n2!=0):
        print("division", n1/n2)
    else:
        print("error and can't devide by zero")
elif(operator == "//"):
    if(n2!=0):
        print("Floor Division", n1//n2)
    else:
        print("error and can't devide by zero")
elif(operator == "%"):
    if(n2!=0):
        print("Modulo", n1%n2)
    else:
        print("Can't calculate the modulo")
else:
    print("invalid operator")
    
print("end")'''         

#Login System
#Store a username and password in variables. Ask the user to enter both.

'''username="rav"
password="pass123"

u1=input("Enter username")
pw=input("Enter password")

if(u1==username and password==pw):
    print("Login Sucessfull")
elif(pw!=password):    
    print("Incorrect Password")
elif(u1!=username):
    print("Username Incorrect")
else:
    print("end")'''
     

#Electricity Bill Calculator Calculate the bill based on units consumed:
#First 100 units: ₹2 per unit Next 100 units: ₹3 per unit Above 200 units: ₹5 per unit
#Use progressive billing: each rate applies only to the units in that range.

'''units=float(input("Total units consumed"))
if(units<0):
   print("invalid")
elif(units<=100):
    bill=2*units
    print("Electricity bill", bill)
elif(units<=200):
    bill=(((100*2)+((units-100)*3)))
    print("Electicity bill", bill)
else:
    bill=(((100*2)+(100*3)+((units-100)*5)))
    print("Electicity bill", bill)
print("end")'''    

          

