'''i=1
while(i<5):
    print(i)
    i +=1'''

'''secret_number = 3
guess = int(input("guess a number: "))
while guess != secret_number:
    guess = int(input("guess a number: "))
else:
    print("Congratulations! You did right guess")'''

"""while True:
    print("I'm stuck inside a loop.")"""

"""# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)"""


'''counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)'''



'''password = ""
while password != "python": ##password has to be python to exit the loop since condition is false
    password = input("Enter the password: ")
else:
    print("Access granted!")'''

'''n=1
while (n<=10):
    print(n)
    n += 1'''

'''n=int(input("Enter the number: "))
while (n<=3):
    if(n%2==0):
        print("even number")
    else:
        print("odd number")
        n=n+1'''
'''i=1
while(i<=10):
    print(i)
    i += 1 '''

'''j=0
while(j<=20):
    print(j)
    j += 2'''

'''num=10
while(num>=1):
    print(num)
    num -= 1
    print("Blast Off!")'''

'''secret_number = 7
guess = int(input("enter the number :"))
while(secret_number != guess):
  guess = int(input("enter the number :"))
  
  print("correct number")'''


'''sum = 0
i = 1

while i <= N:
    sum = sum + i
    i = i + 1
print("Sum of first", N, "numbers is", sum)'''

           
'''i=1
while i<=100:
     print(i)
     i += 1'''
'''i=100
while i>=1:
    print(i)
    i -= 1'''
'''n=int(input("Enter number :")) #multiplication of number n
i=1
while i<=10:
    print(n*i)
    i+=1'''
#Print all even numbers from 1 to 20.
'''i=2
while(i<=20):
    print("even number", i)
    i += 2'''
'''i=1
while(i<=20):
    print(i)
    i += 2'''
'''i=1
sum=0
while(i<=10):
    sum=sum+i
    i+=1
    print(sum)'''

#Find the sum of even numbers from 1 to 20.
'''i=2
sum=0
while(i<=20):
    sum=sum+i
    i+=2
    
print("sum of even numbers",sum)'''

#Count how many numbers are between 1 and 100.
'''i=1
count=0
while(i<=100):
    count=count+1
    i+=1
print("count is", count)'''

#Print numbers divisible by 3 from 1 to 30.
'''i=1
while(i<=30):
     if (i%3==0):
         print(i)
     i+=1'''
   
'''n=int(input("Enter number "))
i=1
while(i<=10):
    print(n*i)
    i+=1'''

#Ask the user for a number and print numbers from 1 to that number.
'''n=int(input("Enter  anumber "))
i=1
while(i<=n):
        print(i)
        i+=1'''

#Ask the user to enter a password until they enter the correct one.
'''password = "abc@123"
guess=input("Enter the password :")
while(guess != password):
    guess=input("Enter the password :")

print("It's correct")'''

#Ask the user to enter a number until they enter 0.
'''number = 0
guess = int(input("Enter a number :"))
while(guess!=number):
    guess = int(input("Enter a number :"))

print("it's correct")'''

#Ask the user to enter positive numbers and stop when a negative number is entered.

'''number = int(input("Enter a number"))
while(number%2==0):
    print("Positive number")
    number = int(input("Enter a number"))

print("negative number")'''

#Write a Python program that prints connection attempts numbered 1, 2, and 3, then prints Maximum attempts reached
'''attempts=1
while(attempts<=3):
    print("Connection attempts", attempts)
    attempts+=1
print("Maximum attempts reached")'''

#Imagine your script is checking server connection attempts. If the attempt number reaches 3, you want to stop the loop immediately using break.
'''attempts=1
while(attempts<=5):
    print("attempts",attempts)
    if(attempts==3):
        break
    attempts+=1
print("loop stopped")'''
    
#You're writing a Python script that counts from 1 to 5. If you forget to update the counter, the loop may run forever
#Write a corrected program that prints the numbers from 1 to 5 and then stops.

'''count=1
while(count<=5):
    print("count", count)
    count+=1
print("count stop")'''

#A deployment script checks numbered deployment steps. When it reaches step 4, it must stop immediately
#Your task is to print steps 1, 2, 3, and 4, then print Deployment check completed.

'''step=1
while(step<=6):
    print("Deployment step", step)
    if(step==4):
        break
    step+=1
print("Deployment Step Completed")'''    

#cenario: You are writing a simple script to monitor a service. The service is initially unavailable, and your script should check its status repeatedly until it becomes available.

'''check=1
while(check<=3):
    print("Checking service...")
    check+=1
print("Service is running")'''    


#A script checks a service up to five times. In this exercise, assume the service becomes available on the third check.
'''attempts=1
while(attempts<=5):
    print("checking service: attempt",attempts )
  
    if(attempts==3):
        print("service is available")
        break
    attempts+=1
print()'''
        
        
#Imagine you're writing a Python script to monitor a service on a cloud server. The service is initially unavailable but becomes available on the third check.
#For this exercise, we'll simulate the service status rather than connect to a real server

'''attempt=1
while(attempt<=5):
    print("checking service...: attempt",attempt)
   
    if(attempt==3):
        print("Service available")
        break
    else:
         print("Service unavailable")
    attempt+=1'''
     

#Server health checks--A script needs to simulate checking a server four times, printing the check number each time.
'''check=1
while(check<=4):
    print("checking server health: check",check)
    check+=1 
print("Health check completed")'''
    
       
'''check=1
while(check<=5):
    print("checking server health: check",check)
    if(check==5):
        print("Service unavailable after 5 attempts?")
        break
    check+=1'''

#A script tries to connect to a server. The connection fails on the first two attempts and succeeds on the third.
'''attempt=1
while(attempt<=5):
    print("Connection attempt :",attempt)
    
    if(attempt==3):
        print("connection sucessfull")
        break
    print("connection failed")
    attempt+=1'''
    
        
#You are simulating a deployment process with five steps. The deployment should stop if step 4 is reached, and it should print a message confirming the deployment has stopped.
'''step=1
print("Start Deployment...")
while(step<=5):
    
    print("Deployment Step :",step)
    if(step==4):
        print("Deployment stopped at step 4")
        break
    step+=1'''
    






















