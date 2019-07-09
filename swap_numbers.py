#!/usr/bin/python3

#python program to swap two numbers using third variable.
#taking two numbers from user
num1= input("enter 1st number: ")
num2= input("enter 2nd number: ")
#swapping two numbers by taking a temporary variable
temp=num1
num1=num2
num2=temp
#printing numbers after swaping 
print("num1="+num1)
print("num2="+num2)
