# Dictionaries store data values in key:value pairs
#They are unordered,mutable(changeble) and don't allow duplicates
'''dict = {
    "Key" : "value",
    "name" : "sravan",
    "learning" : "coding",
    "age" : "32",
    "percentage" : "76.7",
    "subjects" : ["python", "AWS"], # lists
    "topics" : ("lists","loops") # tuples
}
print(dict)'''

#  We can search the values with the key name , ex below
'''print(dict["name"])
print(dict["topics"])'''

# we can change the value as well
'''dict["name"] = "Haryaaksh"
print(dict["name"])'''

# we can add the new key name and value to the existing dictionart
'''dict["surname"] = "Boosa"
print(dict)'''

# we can create an empty dictionary and add values
'''null_dict = {}
print(null_dict)
null_dict["name"] = "Rock"
print(null_dict)'''

#Nested Dictionary

'''student = {
    "Name" : "Haryaaksh",
    "Subjects" : {
        "Maths" : 96,
        "Tel" : 87,
    }
}
print(student)
print(student["Subjects"])
print(student["Subjects"]["Maths"])''' 

#dictionary methods
#1.keys() - returns a list of all the keys in the dictionary
'''info = {
    "Key" : "value",
    "name" : "sravan",
    "learning" : "coding"
}'''

'''print(info.keys()) # prints only keys details and it won't take nested keys

 # we can convert above keys to list or tuples also 
print(list(info.keys())) # converts keys to list
print(tuple(info.keys())) # converts keys to tuple 
print(len(info.keys())) # prints the length of keys in the dictionary
print(len(list(info.keys()))) # prints the length of keys in the dictionary after converting to list '''

# 2.  .values() - returns a list of all the values in the dictionary
'''print(info.values()) # prints only values details and it won't take nested values
print(list(info.values())) # converts values to list ''' 

#3. items() - returns a list of all the key-value pairs as tuples

'''print(info.items()) # prints only key-value pairs as tuples and it won't take nested values
print(list(info.items()))  

pairs = list(info.items())
print(pairs[0]) # prints the first key-value pair as tuple '''  

# 4. get() - returns the key according to the value 

'''print(info.get("name")) # prints the key according to the value
print(info.get("learning")) '''

#5.update() - updates the dictionary with the key-value pairs from another dictionary or from an iterable of key-value pairs
'''info.update({"pl" : "python"})  
info.update({"topic" : "lists", "topic2" : "loops" }) # add multiple key-values also
print(info) # adds the new key-value pair to the existing dictionary  '''

