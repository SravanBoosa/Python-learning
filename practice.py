'''a = 6
b = 3
a /= 2 * b
print(a)''' 

'''a = 10.0
b = 12.0
c = (10.0**2 + 12.0**2) **0.5
print(" The value of c is ", c)'''

'''num = input("Enter a Number: ")
print(num - 2)'''

'''a=10
b=10.5
c=0
d=5
a=float(a)
b=int(a)
print(a,b)
print(type(a),type(b))
print(bool(c),bool(d))'''

'''operator=input("Enter the operator")
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
if(operator=='+'):
    print(num1+num2)
elif(operator=='-'):
    print(num1-num2)
else:
    print("operation invalid")'''

'''name="sravan"
age=40
height=6
print(name,age,height)'''

'''a=100
b=3.14
c="python"
d=1
print(type(a), type(b), type(c), bool(d))'''

'''a=20
b=10
a=a-b
b=a+b
print(a,b)#swapping'''

'''x=10
y=15
z=20
print(x+y+z)
print(x-y-z)'''

'''first_name="sravan"
last_name="kumar"
print(first_name , last_name)'''

'''city_name=input("Enter your city name:")
language_name=input("Which language do you speak:")
print(city_name, language_name)'''

'''a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
print(a % 2 == 0 , "even")
print(a % b == 1, "odd") '''           


'''#even or add numbers check
num=int(input("Enter the number:"))
if(num%2==0):
    print("even number")
else:
    print("odd number") '''

'''#greterthan or lessthan numbers
num1=int(input("Enter number one :"))
num2=int(input("Enter number two :"))
if(num1>=num2):
    print("number one is greaterthan number two")
elif(num2<=num1):
    print("number two is lessthan number one")
else:
    print("invalid numbers")'''
'''#pass or fail
marks=int(input("Enter the marks :"))
if(marks>=35):
    print("pass")
else:
    print("fail")'''

'''#name & colour
name=input("Enter your name:")
print("Hi", name)
colour=input("Your favorite colour is :")
print("Hi", name , "\nyour favorite colour is", colour)'''

'''n=5
while(n<=5):
    print(n)
    n=n+1
    print(n)
    print("end")'''
'''Name="Sravan"
Age=34
City="Karimnagar"
print(Name,Age,City, sep=",")'''
'''text = "pythonprogramming"
print(text[3:12])
print(text[4])
name="sravan"
print(name[2:5])'''

'''a=25
b=15
print("Addition is :", a+b)
print("Subtraction is :", a-b)
print("Multiplication is :", a*b)
print("Division is :", a/b)
print("floor division is :", a//b)
print("Modulo is :", a%b)'''

'''length=20
width=10
print("Area is :",length*width)
print("perimeter is :",2*(length*width))'''

'''celesius=35
print("Fahrenheit is :", (celesius*9/5)+32)'''

'''number = 27
remainder = number%2
print(remainder) '''
# Use the modulus operator % to determine whether the number is even or odd.

#swap values
'''a=10
b=20
a,b=b,a
print("a value is :",a)
print("b value is :", b)'''

'''Basic_salary=30000
HRA=5000
Travel_allowance=2000
Tax=3000
Total_salary = Basic_salary+HRA+Travel_allowance-Tax
print(Total_salary)'''

# Q-You have:total_minutes = 250
# Convert it into:
# Hours = 4
# Minutes = 10

'''total_minutes = 250
hours= total_minutes//60
minutes=total_minutes%60
print("hours:", hours)
print("minutes:", minutes)'''

'''name=input("Enter your name")
age=int(input("Enter your age"))
print("Hello", name)
print("You are", age , "years old")'''

'''a = int(input("Enter first number :"))
b = int(input("Enter second number :"))
sum = a+b
print("Sum is", sum)'''

'''price = int(input("Enter price : "))
quantity = int(input("Enter quantity : "))
Total_cost = price*quantity
print(Total_cost)'''

'''a = int(input("Enter value : "))
b = int(input("Enter value : "))
a,b = b,a
print(a,b)'''

'''#Ask the user for their current age and display how old they will be next year.
age = int(input("Enter the current age : "))
age_of_next_year = age+1
print("age of next year", age_of_next_year)'''

'''a=int(input("Enter the number"))
b=int(input("Enter the number"))
add=a+b
print("add = ", add)'''

#Bill with discount: Ask for the original price and discount percentage. Calculate the discount amount and final price.
'''total_bill=float(input("Enter the amount: " ))
discount=float(input("Enter the discount percentage : "))
discount_amount=total_bill*discount/100
final_price=total_bill-discount_amount
print(final_price)'''
