#from: https://www.w3schools.com/python/python_functions.asp

"""Exercise 1: Create a function in Python
Write a program to create a function that takes two arguments, name and age, and print their value."""

def userInfo(name, age):
    print("Your info: " + name + str(age))
    


userInfo("Ana ", 26)

"""Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:"""

def youngestKid(*kids):
    print("the youngest is: " + kids[2])

youngestKid("ana", "pablo", "maria", "juana")

"""Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

E.g. if you send a List as an argument, it will still be a List when it reaches the function:"""

def readList(items):
    for x in items:
        print(x)

groceryList = ["Apple", "Juice", "Sandwich"]

readList(groceryList)

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#from: https://pynative.com/python-functions-exercise-with-solutions/
"""Exercise 2: Create a function with variable length of arguments
Write a program to create function func1() to accept a variable length of arguments and print their value.

Note: Create a function in such a way that we can pass any number of arguments to this function and the function should process them and display each argument’s value.

Read: variable length of arguments in functions

Function call:"""

def anyArgument(note):
    for x in note:
        print(x)

list = [20, 40, 60]
listb = [80, 100]

anyArgument(list)
anyArgument(listb)