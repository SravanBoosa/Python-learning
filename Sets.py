#Set is a collection of the unrderes items
#each element in the set must be unique & immutable
# we can't store list and dictionary in set becoz both are mutable
'''collection = {1,2,3,4}
print(type(collection))
print(collection)'''

# it will ignore duplicate values
'''strg = {1,2,2,2, "am","am","sravan"}
print(strg) # o/p is {1, 2, 'am', 'sravan'}
print(len(strg)) # total no ofitems 4'''

# To create an empty set
'''num = set() #empty set; syantax
print(type(num)) # class 'set'  '''

# SET Metthods
#1.add - set.add(element) # adds an element
# sets - mutable - changeble
# set - elements - immutable

'''num = set()
num.add(1)
num.add(2)
num.add(2)
num.add(3)
print(len(num)) # o/p 3
print(num) #o/p {1,2,3}'''

#2.remove
'''num.remove(2)
print(num) # o/p {1,3} '''

#3.clear - empty the set
'''num = {1,2,3,4,"name", "college"}
print(len(num)) # o/p - 6
num.clear()
print(len(num))# o/p - 0
print(num) # o/p is set{} '''
#4. pop -  remove a random value , prints random value in o/p

'''num = {1,2,3,4,"name", "college"}
print(num.pop()) # o/p -1 
print(num.pop()) # o/p - name
print(num.pop()) # o/p - 2 '''

#5. union - combines both set vailues and return new
'''set1 = {1,2,3}
set2 = {2,3,4,5}
print(set1.union(set2)) # 0/p {1,2,3,4,5}
print(set1) # o/p {1,2,3}
print(set2) # o/p {2,3,4,5}'''
#6.intersection - combines common values and return new
'''set1 = {1,2,3}
set2 = {2,3,4,5}
print(set1.intersection(set2)) # o/p - {2,3}'''

