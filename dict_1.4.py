"""KAVIRAJ DESAI - 20CE023
Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}

Expected Result : {0: 10, 1: 20, 2: 30}"""
dict = {
    "add" : "+",
    "subtract" : "-",
    "multiply" : "*",
}
print("The dictionary is : ",dict)
#creating new dictionary with remaining elements
dict1 = {
    "divide" : "%",
    "modulo" : "/"
}
#using update function to add the elements to the previous dictionary
dict.update(dict1)
print("updated dictionary is : ",dict)