"""KAVIRAJ DESAI - 20CE023
Write a Python script to concatenate following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60} """
dic1={
    1:10,
    2:20
}
dic2={
    3:30,
    4:40
}
dic3={
    5:50,
    6:60
}
print("The Dictionaries are: ", dic1, dic2, dic3)
#updating the first dictionary by adding elements of second dictionary
dic1.update(dic2)
#again updating first dictionary by adding elements of third dictionary
dic1.update(dic3)
print("The concatenated string is : ",dic1)