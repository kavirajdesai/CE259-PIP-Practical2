"""KAVIRAJ DESAI - 20CE023
Write a Python program to find the most common elements and their counts from list, tuple, dictionary"""
#finding the most common element from list
def most_frequent(List):
     return max(set(List), key = List.count) # returning the answers
List = [100,23,12,34,23,100,100,3]
a=most_frequent(List)
print(a,List.count(a))
#finding most common element from tuple
def most_frequent(List):
    return max(set(List), key = List.count)
List = list((12,34,23,12,14)) #converting tuple to list
a=most_frequent(List)
print(a,List.count(a))
#finding most common element from dictionary
def most_frequent(List):
    return max(set(List), key = List.count)
dict={
    1:10,
    2:200,
    2:200,
    3:450
}
List = list(dict.values()) #converting to list
a=most_frequent(List)
print(a,List.count(a))