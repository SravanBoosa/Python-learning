#Lists - A collection of multiple elements
# A built in data type that stores set of values

#it can store elements of different types(interger,, float, string etc)
# ex - for above line -- store = ["sravan",92,65.3,"Delhi"]
# ex marks = [94, 78.8,87 65.4]

'''marks = [94,78.8,87,65.4]
print(marks)
print(type)
print(marks[0])
print(len(marks))# to check the length (no of elements)'''

'''student=["sravan",95.4,17,"Delhi"]
print(student)
student[0]="Haryaaksh" # we can change elements in listas well
student[2]=3
print(student)'''

#List Slicing
# Slicing allows you to create a new list that contains only the elements you want without modifying the original list.
# list_name[starting_idx:ending_idx] #ending idx is not included
#marks=[87,64,33,95,76]
#       0   1  2  3  4
#      -5  -4 -3 -2 -1 #negative index
#marks[1:4]is [64,33,95]

'''marks=[87,64,33,95,76]
print(marks[1:4]) # prints till index 3 which is 95
print(marks[1:]) # prints all elements
print(marks[:3]) # prints till  index 2 which is 33
print(marks[:])  # prints all values

del marks[0:2] # delete elements
print(marks[:])'''

#List Methods

'''#list=[2,3,4]
#1. append - list.append(5) # add one element at the end [4,2,3,5]
list=[4,2,3]
list.append(5)
print(list)'''

#2.extend - add multiple elements at a time
'''list=[2,3,4]
list.extend([5,6,7])
print(list)'''

#2.sort - sort in ascending order - ex-[2,3,4]
'''ages=[24,65,46,35]
#ages.sort()
#print(ages.sort) # prints nothing
#print(ages) # prints ascending order which comes after sort command'''


#3. reverse - reverse order 
'''ages=[24,65,46,35]
ages.reverse() # prints in reverse order [35,46,65,24]
print(ages)'''

#4. insert - insert element at perticular index
# Index places a new element at a specific index, shifting the current and subsequent items to the right

'''list = [2,1,4]
list.insert(1,5)
print(list) # o/p [2,5,1,4]'''

'''#5.remove - remove first occurrence of element
list=[2,1,3,1]
list.remove(1)
print(list) # o/p [2,3,1]'''

'''list = [2,5,1,4]
list.remove(5)
print(list) # o/p [2,1,4]'''

'''#6.pop - remove perticular element at index
list=[2,5,1,4]
list.pop(3) # removes elelmt no3 which is last element 4
print(list) # o/p [2,5,1] '''

#list.  shows the list of methods available for list data type

'''my_list=[]
for i in range(5):
    my_list.insert(0,i+1)
print(my_list)    #o/p is [5,4,3,2,1]'''

'''my_list=[10,1,8,3,5]
total=0
for i in range(len(my_list)): # length command return no of elememts as 5 it become range(5)
    total += my_list[i]
print(total) # o/p is 27 (addition of all from index 0 to 4 total = total+my-list[0] then [1]  [2]...)             

#But the for loop can do much more. It can hide all the actions connected to the list's indexing, and deliver all the list's elements in a handy way.
my_list=[10,1,8,3,5]
total=0
for i in my_list:
    total += i # the i variable is assigned the values of all the subsequent list's elements
print(list)'''

# Q - WAP -
#step 1: create an empty list named beatles;
#step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
#step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
#step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
#step 5: use the insert() method to add Ringo Starr to the beginning of the list.
'''beatles = []
print(beatles)
beatles.append("John Lennon")
beatles.append("McCartney")
beatles.append("George Harrison")
print(beatles)
for i in range(2):
    member=input("Add a member :")
    beatles.append(member)
print(beatles)
del beatles[3:5]
print(beatles)
beatles.insert(0,"Ringo Starr")
print(beatles)'''
    

'''lst = [1,2,3,4,5]
lst_2 = []
add = 0
for i in lst:
    add += i
    lst_2.append(i)
print(lst_2)'''    

'''list_1 = ["A", "B", "C"]
list_2 = list_1[:] # The slice operator [:] creates a new copy of the entire list.
list_3 = list_2[:]

del list_1[0] # list_1 is now ['B', 'C']
del list_2[0] # list_2 is now ['B','C']  
# list_3 is still ['A', 'B', 'C'] because it was created as a copy of list_2 before the deletion.

print(list_3)'''



