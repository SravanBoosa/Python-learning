# for loops sequential traversal for traversing list, string,tuples etc.
# for variable in sequence
    #statements

#for i in range(1,10):
'''for i in range(1,10)
    print(i)'''

#factorial of a number
'''num=int(input("Enter a number :"))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print(fact)'''

#multiplication 
'''n=int(input("Enter  anumber :"))
for i in range(1,11):
    print(n*i)'''
#pass is a null statement that does nothing. it is used as a placeholder for future code.
'''for i in range(1,11):
    pass
print("Hello")'''

# find the sum of first n natural numbers ()
'''n=int(input("Enter a number :"))
sum=0
for i in range(1,n+1):
    sum +=i
print("total sum is",sum)'''

'''n=int(input("enter number: "))
count=0
for i in range(1,11,1):
     
      print(i*n)
      count=count+1
print("count is",count)'''      

'''for i in range(10,0,-1):
    print(i)'''

'''for i in range(10,0,1):
    print(i)'''
#
'''i=5
for i in range(i,0,-1):
    print(i)
print("Server shutting down!")'''


#Write a Python program using for and range() to print all odd numbers between 1 and 20
'''i=1
for i in range(i,20,2):
    print(i)
print("end")

#using if condition for odd numbers
#for i in range(1,21)
for i in range(1, 21,2):
    if i % 2 != 0:
        print(i)'''

#for even numbers
'''for i in range(2, 21,2):  # for i in range(1,21) and based on if condition it will cheeck 
    if i % 2 == 0:
        print(i)'''
#Sum of numbers using a for loop  , Calculate the sum of numbers from 1 to 10 and print total sum
'''i=1
sum=0
for i in range(1,11,1):
    print(i)
    sum=sum+i
print("total sum is :",sum)'''    

#Count even numbers from 1-20 and use if condition and Count how many even numbers are present and print
'''i=1
count=0
for i in range(1,21):
    if(i%2==0):
        print(i)
        count=count+1 #Increases the counter by 1 for each even number.
print("Total even numbers:", count) '''       


#uppose you want to count how many numbers are divisible by 3 between 1 and 30.
#Which condition would you use?
#A. i % 3 == 0
#B. i % 3 != 0

'''i=1
count=0
for i in range(1,31):
    if(i%3==0):
        print(i)
        count=count+1
print("Total count",count)'''        


#Calculate the sum of even numbers from 1 to 20.
'''i=1
sum=0
for i in range(1,21):
    if(i%2==0):
        print(i)
        sum+=i
print("sum of even numbers:",sum)'''        
        
        






