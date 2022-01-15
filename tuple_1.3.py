"""KAVIRAJ DESAI - 20CE023
Write a Python program to add an item in a tuple."""
#taking values from users
n1=input("Enetr first number: ")
n2=input("Enetr second number: ")
n3=input("Enetr third number: ")
n4=input("Enetr fourth number: ")
n5=input("Enetr fifth number: ")
number=(n1,n2,n3,n4,n5)
print("Inputs are: ",number)
#changing tuple into List to perform append function
L1=list(number)
#adding the element
L1.append(160)
#changing List into tuple for original output
tup=tuple(L1)
print("Updated tupple is: ", tup)

