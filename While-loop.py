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



