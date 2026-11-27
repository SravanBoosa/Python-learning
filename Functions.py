'''def message():
    print("Hello")
message()'''

'''def hi(): ##It does not accept any arguments.
    print("hi")

hi(5) #You are passing one argument (5), which the function doesn't expect. '''


'''def message():
    print("Enter a value: ")
message() ###This calls or executes the function we created.#It displays:Enter value:  '''


'''def message(name):
    print("Hello", name)

message("Rahul")
message("Priya")'''

'''def message():
    print("Enter a value: ") #Whenever this function is called, it displays "Enter a value:".

message() #This calls or executes the function we created.#It displays:Enter value:
a = int(input())  input takes a value from the user  & stores that number in a variable called a.
message()
b = int(input())
message()
c = int(input())

print("volues of a, b,c:", a,b,c)'''

'''def mes():
    print("Enter name:")
mes()
a=input()
print("Name is :", a)'''

#---------------
#---------------


'''def cal_sum(a,b):
    sum = a+b
    return sum
print(cal_sum(3,6))
print(cal_sum(11,15))'''

'''def diff_sum(c,d):
    diff = c-d
    return diff
print(diff_sum(8,3))'''    

'''def print_hello():
    print("Hello") ##o/p returns nothing
output = print_hello()
print(output)'''

'''def cal_prod(a,b):
    prod = a*b
    return prod
print(cal_prod(17,19))'''

'''def cal_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    return avg
print(cal_avg(78,85,97))'''


'''
------------------
Function Types
------------------ '''

'''def cal_sum(a=5, b=6):
    print(a+b)
    return(a+b)
print(cal_sum()) '''

'''def cal_prod(a,b=5):
    return(a*b)
print(cal_prod(3))'''

'''def square(s=6):
    return s**2
print(square())
print(square(9))'''

'''def cal_diff(a,b):
    result= a-b
    return result
result = cal_diff(10,5)
print(result)'''  


'''def print_info(name,age=18):
    print(name,age)
print("name", 19)'''

'''def multi_num(a,b=6):
   
    return(a*b)
print(multi_num(5))'''

#def input(input_num()):
#   return int(input()) # defines a function to get numeric input from the user:
#asks for input and shows in display , not saved

'''def multi_num():
    a=int(input("Enter first number :"))
    b=int(input("Enter second number :"))
    result=  a*b
    return result
print(multi_num())'''


'''def multi_num(a,b):
    result = a*b  ##better method ""Outside the function,
    return result # This function accepts two parameters. It receives values from outside.
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))

print(multi_num(a,b))'''

'''def multi_num(a,b):
    return a*b
print(multi_num(5,7))'''

'''cities=["hyderabad", "Bengaluru", "Vizag", "Chennai"]
sports=["Football", "cricket"]
def print_len(list):
    print(len(list))
print_len(cities)
print_len(sports)'''

#---------
#---------
#-positional arguments - *args
'''def numbers(*args):
    print("Enter numbers: ", args)
numbers(2,5,7,13)'''

#--Keyword-arguements **kwargs
'''def details(**kwargs):
    print("employee details :", kwargs)
details(name="sravan", place="Karimnagar")'''

'''def values(**b):
    print("assigned values of alphabets:", b)
values(a=2,b=3,c=4) '''   


#-- combine both positional and keyword arguements

'''def show(*a,**b):
    print(a)
    print(b)
show(2,3,name="sravan",job="cloudebgineer")'''

'''def adding(a,b,c):
    print("addition :", a+b+c)
adding(a=2,b=3,c=1)
adding(1,c=3,b=2)
adding(3,2,c=1)'''


'''def introduction(first_name="john", last_name="Smith"):
     print("Hello, my name is", first_name, last_name)
introduction("James", "Doe") #o/p is - Hello, my name is James Doeintroduction("Henry")
introduction("Henry")#o/p- Hello, my name is Henry Smith
introduction(first_name="William") # o/p- Hello, my name is William Smith
introduction(last_name="Hopkins") # o/p - Hello, my name is john Hopkins '''

'''def hi(name):
    print("Hi,", name)

hi("Greg")'''

'''def hi_all(name_1, name_2):
    print("Hi,", name_2)
    print("Hi,", name_1)

hi_all("Sebastian", "Konrad")'''

'''def address(street, city, postal_code):
    print("Your address is:", street, "St.,", city, postal_code)

s = input("Street: ")
p_c = input("Postal Code: ")
c = input("City: ")
address(s, c, p_c)'''

#input() asks the user to enter something.
#"Street: " is the message displayed to the user.
#The entered value is stored in the variable s.

#o/p Street: kapuwada
#Postal Code: 505001
#City: karimnagar
#Your address is: kapuwada St., karimnagar 505001

'''def details(name,place,pincode):
    print("Your details are:", name,place,pincode)
n=input("name: ")
p=input("place: ")
pi=input("pincode: ")
details(n,p,pi)'''

#Remember:
#Parameters = Variables written inside the function definition.
#Arguments = Values or variables passed when calling the function.


'''def add_numbers(a, b=2, c):
    print(a + b + c)

add_numbers(a=1, c=3)'''
#o/p SyntaxError: non-default argument follows default argument
#Python does not allow a parameter without a default value (c) to come after a parameter with a default value (b=2) in a normal function definition.

#---------------

















   
