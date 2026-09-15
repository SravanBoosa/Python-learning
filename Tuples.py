#Tuples
# A tuple is an ordered, immutable (cannot be changed) collection of items in Python.
#Ordered: Items have a fixed order and can be accessed by index.
#Immutable: Once a tuple is created, you cannot add, remove, or modify its elements.
#Allows duplicates: The same value can appear multiple times.
#Can store different data types: Integers, strings, lists, other tuples, etc.

# ex
'''person = ("John", 25, 5.9, True)
print(type(person))
print(person[0])'''

# we can create empty tuple as well
'''tup=()
print(type(tup))'''

# to create a single element in tuple , follow instructions
'''tup=(3,)
print(type(tup))# class tuple , correct process '''

'''tup=(3);print(type(tup)) #o/p is  class int'''

# Tuples Slicing
#The syntax is:
#tuple[start:stop:step]
#start: Index where slicing begins (included).
#stop: Index where slicing ends (excluded).
#step: Number of positions to move each time (optional).

# Slicing in tuples means extracting a portion of a tuple to create a new tuple.
'''numbers = (10, 20, 30, 40, 50)
print(numbers[1:4])'''

#Slicing using negative index
'''numbers = (10, 20, 30, 40, 50)
print(numbers[-4:-1]) # o/p (20,30,40)'''

#tuple[start:stop:step]
#Using a step

'''numbers = (10, 20, 30, 40, 50, 60)
print(numbers[::2])'''

#Start from the beginning and take every second element.
# Output: (10, 30, 50)

#Reverse a tuple

numbers = (10, 20, 30, 40)
print(numbers[::-1])

#A step of -1 means move backwards.
#Output: (40, 30, 20, 10)


#Tuples Method
#1. index method -
# tup.index(el) # returns index first occurence
#ex
'''tup = (2,3,4,3,5) # Although 3 appears twice, index() returns the index of the first occurrence.
print(tup.index(3)) # o/p shows the elememt ondex as 1 '''

#2. Count- The count() method returns the number of times a specified value appears in the tuple.
'''tup = (2,3,4,2,5)
print(tup.count(2)) # o/p- The value 2 appears 2 times.'''

'''list = []
movie1 = input("Enter 1st movie name :")
movie2 = input("Enter 1st movie name :")
movie3 = input("Enter 1st movie name :")
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)'''    

'''grade = ('C', 'D', 'A', 'A', 'B', 'B', 'A')
print(grade.count('A')) '''

'''grade = ['C', 'D', 'A', 'A', 'B', 'B', 'A']
grade.sort()
print(grade)'''


