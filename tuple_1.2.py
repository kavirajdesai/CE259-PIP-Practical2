"""KAVIRAJ DESAI - 20CE023
Write a Python program to create a tuple with numbers and print one item. """
#taking values from users
n1=input("Enetr first number: ")
n2=input("Enetr second number: ")
n3=input("Enetr third number: ")
n4=input("Enetr fourth number: ")
n5=input("Enetr fifth number: ")
number=(n1,n2,n3,n4,n5)
print("Inputs are: ",number)
#showing only one element
fourthNumber=number[3]
print("Fourth Number is: ",fourthNumber)

