# Using input function for taking input from user
# input() takes input as string by default

# a=input("Enter 1st number ") 
  
# # It will take input in the form of string
# to avoid this problem we have to define the data type of variable 

a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
print("sum =",a+b)