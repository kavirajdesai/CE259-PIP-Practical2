"""KAVIRAJ DESAI - 20CE023
Write a Python script to merge two Python dictionaries."""
#creating dictionary
dict1={
    "123": "321",
}
dict2={
    "flower":"beautiful",
}
print("Dictionary 1 is: ", dict1)
print("/nDictionary 2 is: ", dict2)
#for meging first copy element in another dictionary
dict3=dict1.copy()
#using update function combine the two dictonary
dict3.update(dict2)
print("Merged dictionay is: ", dict3)
