#!/usr/bin/env python3
#Description of Function: A function that takes an input from the user and calculate someone's age. 

def age():
    try:
        year = int(input("Enter year of birth: "))

        currentyear = 2024

        age = currentyear - year

        print('You are ' + str(int(age)) + ' years old.')
    
    except ValueError:
         print('Please enter an int.')

age()


def helloWorld():
	print('Hello World')

helloWorld()