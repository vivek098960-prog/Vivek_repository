

# Basics

# Keywords: Predefined words that have meaning in a language
#Inbuilt functions: The prewritten code saved in memory

# print: print function is used to show text on screen
print("Hello anchal", "nikhil", "3875837587385")
print("Hello vikram")

# end parameter in print function
# Note: print function after showing text on screen goes to next line automatically
# that's why next print always occurs in next line
print("Hello", end=" ")  # Now print function will add space instead of next line after printing
print("gagneza")

# Data types

# Basic data types
# int: numbers
# float: decimal points
# string: Used to store names, company names, identification numbers, etc. String data is always in quotes
# bool: True/False
# complex: used to store complex numbers



# Variables: Variables are entities where a single piece of data is stored
#Syntax:
x=100
#100 integer is stored in x variable
print(x)

# Python rules:
# 1- Python is case sensitive
# 2- Name of variable can only contain numbers, alphabets, or _ (underscore)
# 3- Name of variable cannot start with numbers

_rt = 90  # Correct

niharika_80 = 100  # Correct

x2 = 100  # Correct

# 34xy = 56  # Wrong (invalid variable name; example only)

y = 23.5
s = "niharika"
print(s, y)



# Checking datatype of variable
# type function is used to tell the datatype of a variable
var = "vikram"
print(type(var))

i = 100
print(type(i))

# Type casting: It is used to convert a variable type to another type
# int(), float(), str(), bool(), complex -> these functions are used to change the dtype
x = 100
# Convert above into float
x = float(x)
# Note: The above function will not change x but will return the float copy of x
print(x)

x = "100"
print(type(x))
x = int(x)
print(type(x))

x = "niharika"
y = "anchal"
print(x, "and", y, "are enemies")

s = 120
s = float(s)
print(s)


# Input function
# Input function is used to take data from the user (external input)
# This function will show an input box where you fill data and when you press
# Enter, that data will be stored in the assigned variable
# x = input()
# print("My input is", x)

# Note: input function always gives us a string
# Sometimes we don't want only an empty box; we want to label it
# y = input("Enter the value")

# Taking input and type casting
# inp = input("Enter the number")
# inp = int(inp)
# print(inp)

# OR

# inp = int(input("Enter the number"))
# print(inp)

# s = input("Enter a value")
# s = int(s)
# print(s)

# Operators

# Operators are special symbols used to perform specific operations



# Relational operators
# < -> Less than
# > -> Greater than
# == -> Equal to
# !=  -> Not equal to
# >= -> Greater than or equal to
# <=  -> Less than or equal to

# These operators are used to compare two values and return True or False

a = 90
b = 100
print(a < b)  # Return True
print(b >= a)  # True
print(7 != 7)  # 7 is not equal to 7 -> wrong: False
# Note: != operator returns True if both side values are not the same

# Arithmetic operators
# Used to calculate something
# + - / *
# % :- Modulus operator
# // :- Floor division operator
# ** :- Exponent

print(12 + 89 / 5 * 7)
print(10 % 3)  # It tells the remainder of 10 divided by 3
print(10 / 3)  # It gives us division result in decimal form (3.3333)
print(10 // 3)  # It always gives the division result as an integer (3)
print(3 ** 5)  # It tells 3 to the power of 5

# Precedence: Which operator works first? 2+3*4 -> 2+12 -> 14
# Associativity: Direction of operator evaluation
# EX: 2*3*4 -> 6*4 means * has left to right associativity
# ** : 2**3**2 -> 2**9 -> 512 has right to left associativity
# EX =: x=9+8 : Here = will assign right value to left variable, so its associativity is also right to left

print(2 ** 9)  # Demonstrates exponent operator

# Task1: Take two numbers from input and print their sum in one line
# print their product in second line
# print their division in third line

# Example: 34 5 (example input, not executable code)
# Sum of both numbers is: 39
# Product of both numbers is: 170
# Division of both numbers is: 6.8

# Relational Operators (Summary)
# == : Compares two values and tells if both are the same: a==b
# <  : Compares two values and tells if left value is less than right value
# >  : Compares two values and tells if left value is greater than right value
# <= : Compares two values and tells if left value is smaller or equal to right value
# >= : Compares two values and tells if left value is greater or equal to right value
# != : Compares and returns True if both values are not the same


a = 90
b = 100
print(a != b)
print(a <= b)

# Q: Check if number is even or not
# num = int(input("Enter number"))
# print(num % 2 == 0)

# Logical operators
# These operators work on boolean values -> compare boolean values
# and: Returns True if both sides are True
# or: Returns True if any one side is True
# not: Actually reverses the boolean value
# Note: not is a unary operator (works on single operand)

print(True and False)
print(True or False)  # Left side is True
print(not True)

# Ex: Check if number is greater than 100 and also less than 150
num = 90
print(num > 100 and num < 150)

# Check if number is divisible by 5 and 7 both
num = 30

print(num % 5 == 0 and num % 7 == 0)

# ch = input("Please enter one character")
# Check if given character is a vowel or not
# print(ch == 'a' or ch == 'o' or ch == 'e' or ch == 'i' or ch == 'u')
# If any of above returns True, then the whole expression will return True

# Task: Check whether a given character is a vowel or not
# Condition: Don't use logical operators

# Membership operator
# in operator : is used to check if left value is present in right collection/sequence
s = "Theta Prime Solutions"
print("The" in s)

# not in : Checks if left value is not present in right sequence or collection
print("our" not in s)

# Identity operator
# is operator: It is used to check if both variables point to the same memory location

l1 = [1, 2, 3, 4]
l2 = [1, 2, 3, 4]
print(l1 == l2)  # True (same values)
print(l1 is l2)  # False (different memory locations)

# Assignment operator
# =: Assignment operator is used to assign right side value to left side

# Types:
# += -= /= *= %= //= **= .....
x = 100
# Increase the value of x by 10
x = x + 10
print(x)

# Or (using compound assignment)
x = 100
x += 10
print(x)

x = 100
x *= 2  # 200
print(x)

# Binary/Bitwise operators
# &  : Bitwise AND
# |  : Bitwise OR
# ~  : Bitwise NOT (Invert)
# ^  : Bitwise XOR
# << : Left shift
# >> : Right shift

# String

# String is a sequence of characters
# Immutable: String cannot be updated
# Indexable: We can access string by using the position
# Iterable: We can apply a loop over string directly

s = "Theta prime solutions"
print(s)

# Note: String can be stored in single quotes or double quotes

# Multiline string
# A string in which next line is acceptable

s = '''
My name is Maninder.
I work at Chandigarh.
I am a developer
'''
print(s)

# Note: Counting in programming starts from 0
s = "Theta prime solutions"
# Indexing/slicing
# Indexing is extracting the position of an element
# Syntax: variable[number]
print(s[0])
print(s[5])  # space
print(s[2])
# Note: Space is also a character

s = "Theta prime solutions"
# Accessing from last character
print(s[-1])  # -1 means last position
print(s[-2])  # Second last position


# Slicing
# Taking out a part of a sequence
# Syntax: variable[start:stop]
s = "Theta prime solutions"
print(s[0:3])
# Last index is excluded
print(s[6:9])



s="Theta prime solutions"
print(s[6:-3])

#lut
print(s[-7:-4])#-4 is excluded

print(s[-4:-1])

#Important notes:
#When we dont write start it assumes 0
s="Theta prime solutions"
print(s[:7])

#When we dont write stop it will assume all rest of string
print(s[8:])



#Task: There is string given by user
s = "Demo String"  # Using fixed string instead of input()
print(s[-5:])

s="sql is python python is sql"
print(s[-5:])

#Task: Print central character of user entered string

#len function-> It is use to find the total elements in a sequence
s="Theta"
print(len(s))#Length count is natural
#Note: This function can only be applied on a sequence or collection


# Steps in slicing
# Syntax: variable[start:stop:step]
s = "ABCDEFGHIJKLMNOPQRST"
print(s[3:15:3])  # Starts at 3, then 6, 9, 12, stops at 15 (excluded)

# Q: Print all characters with a gap of 2
s = "Theta Prime Solutions"
print(s[::2])

# Reverse the string
# Note: By default step is +1 in indexing/slicing
s = "Theta Prime Solutions"
print(s[::-1])  # Way to print string in reverse

#Methods of string
#Functions that can only applied on particular dtypes
#We can apply method using . operator
s="rohan sharma"
print(s.isupper())#This will tell if whole string is in upper case or not
print(s.islower())#This will tell if whole string is in lower case or not
print(s.isalpha())#This will tell if all characters are alphabets
s="435232152"
print(s.isnumeric())#This will tell if all characters are numeric
s="arrg243535"
print(s.isalnum())#This will tell if all characters are either alphabets or numeric

#title format
#When character after space is capital and all other characters are small
s="Theta Prime Solutions"
print(s.istitle())

print(s.startswith("The"))#It tells if the string starts with given substring

print(s.endswith("ns"))#It tells if the strings ends with given substring

#parameters are data given to function in round bracket

s="theta prime"
s=s.upper()#This function will return the upper case form of given string

s="ABC"
s=s.lower()#This function will return the lower case form of given string
print(s)

s="theta prime solutions"
s=s.title()#This will return string in the form of title format
print(s)

#Replace method: it is use to replace a substring with another substring
s="omg"
s=s.replace("om","a")
#here "om" will be replaced with "a"
print(s)

s="omg"
s=s.replace("o","")#Here o character will be deleted
print(s)
#Note: replace function will replace all substrings occuring
s="aaaaaaaa"
s=s.replace("a","o")
print(s)

#Index vs find
s="Maninder"
print(s.index("inder"))
#index function will tell the position of substring passed

print(s.find("inder"))
#Index method will create error if substring not found but find method will return -1
#when substring not found

#count
#it will tell the count of substring passed
s="Theta Prime Solutions"
print(s.count("a"))


#Strip function
s="aaaaaamaninderaaaaaaa"
s=s.lstrip("a")
#Above fxn will remove all a trailing charcaters on left side
print(s)
s="aaaaaamaninderaaaaaaa"
s=s.rstrip("a")
print(s)
#IT will remove all 'a' characters occuring at right side

s="aaaaaamaninderaaaaaaa"
s=s.strip("a")
print(s)
#IT will remove trailing characters from left and right side both

#Split function
#It will break the string into multistrings
s="My name is rohan"
l=s.split(" ")
print(l)
#It will convert my string to the list of multiple strings


#Join
#IT is use to make a string from list of multiple strings
l=["Niharika","&","Anchal","are","enemies","but","vikram","hate","it"]
#Join fxn needs a concatenator to join all strings
s=" ".join(l)
print(s)
#Note: Here space is acting like a joiner

#Escape sequences
#These are characters that starts from '/' and have different meaning
#when parsed in string
#Example:
#\n -> next line
#\t -> horizontal tab
#\v-> vertical tab
#\b-> backspace
#\Uxxx -> unicode character
s="Kaduu is my \nfavourite vegetable"
print(s)

s="Anchal and\bVikram are enemies"
print(s)

#Arithmatic operations on string
s1="Theta"
s2="Prime"
s=s1+s2#Concating two strings
print(s)

print(s1*5)#Repeating a string

#\\: Double slash will make the escape sequences to parse as it is
s="Karan \\\n anchal are best friends"
print(s)

#Raw String: A string in which escape sequences does not parsed
#SyntaX: write r before string
s=r"Karan and \nAnchal are\t best friends"
print(s)

#Task: print all the even position characters in a string in one line



#Formatted string
#String in which we can add external data
x = 15  # Predefined value instead of input()
y = 25  # Predefined value instead of input()
#Use curly brackets where there is custom string from external
print(f"Sum of {x} and {y} is {x+y} ")
#We have to write f before starting of string

# if-else conditions

# if-else conditions are used to execute a statement according to a condition
# Syntax:
# if condition:
#     statement1
#     statement2
# else:
#     statements
# The space before the statements indicate the relevance of statements with the block

# Example: Basic if-else
X = 50  # Define X for demonstration
if X > 30:  # If condition is true then statement will execute, otherwise it will go to else block
    print("X is greater than 30")
else:
    print("X is less than or equal to 30")

#Task: Print Great if x is greater than 100 otherwise print small
x=120
if x>100: #IF x smaller than 100 then else statement will run
  print("Greater")
else:
  print("small")


#Check if gmail address is correct or not
#Condition:gmail should have .com at last and should contain @
#maninder@gmail.com

mail="manindergmail.com"
if mail.endswith(".com") and "@" in mail:
  print("Correct")
else:
  print("Incorrect")



#Task: Print yes if number is divisble by 8 and print not if not divisible by 8
num=68
if num%8==0:
  print("Yes")
else:
  print("NOt")
# Task: You have two numbers, print the highest of them
# (Using predefined values instead of input for continuous execution)
x = 45
y = 78
if x > y:
    print(f"Highest: {x}")
else:
    print(f"Highest: {y}")

# When we have more than 1 condition, we use elif statements
# Syntax:
# if condition1:
#     statement1
# elif condition2:
#     statement2
# elif condition3:
#     statement3
# else:
#     statement4
# Note: We can have multiple elif blocks, but only one will execute

#Find highest of three numbers
x=10
y=20
z=30
if x>y and x>z:
  print(x)
elif y>x and y>z:
  print(y)
else:
  print(z)

# Make a calculator
# Predefined values for demonstration (replace with input() for interactive use)
num1 = 50
num2 = 30
op = "+"  # Try '+', '-', '*', '/'
print(f"Calculator: {num1} {op} {num2}")
if op == "+":  # If user enters '+' character
    print(f"Result: {num1 + num2}")
elif op == "-":
    print(f"Result: {num1 - num2}")
elif op == "/":
    print(f"Result: {num1 / num2}")
elif op == "*":
    print(f"Result: {num1 * num2}")
else:
    print("Operation not allowed")


print("Thanks for using my calculator")


# Example: Email validation
# Reject those email ids whose domain length is not between 9 and 15
# Examples: maninder@gmail.com, rohan@thetaprimesolutions.com, niharika@yahoo.in

# Predefined test cases (replace with input() for interactive use)
mail = "rohan@thetaprimesolutions.com"
print(f"Validating: {mail}")

if "@" in mail:
    ind = mail.index("@")  # Find @ index
    domain = mail[ind + 1:]  # Extract domain
    
    if 9 < len(domain) < 15:
        print(f"Accepted - Domain length: {len(domain)}")
    else:
        print(f"Rejected - Domain length {len(domain)} not between 9-15")
else:
    print("Rejected - No @ symbol found")


# Email structure example: maninder@thetaprimesolutions.com
# maninder -> username
# thetaprimesolutions -> second level domain
# .com/.in/.co.in/.edu -> Top level domains

# Loop/Iterations

#ITeration-> Repeat
#MAny times in our programming we have to repeat certain amount of coding lines
#instead of repeating them again and again we use to take the concept of
#iteration

#Loops are of two kinds:
#while loop
#for loop



#while loop
#in while loop we provide a condition , our code keeps on repeating until
#condition fails

#Syntax:
#while condition:
  #statements
  #statements
  #statements


#Working: while will repeat the statements and check the condition
#it will keep this doing until condition become False



#Write hello world 10 times on screen
#Means here condition should be in sucha way that it should fails after 10 times
#but should true in 10 times

x=1
while x<=10:#11<=10 -> False
  print("Hello world")
  x=x+1#2   3   4  5

#when x will become 11 loop will be stopped and we will move to next code after loop

#print counting from 50 to 1
x=50
while x>0:
  print(x)
  x=x-1




#Print first 10 multiples of 5 using while loop


x=1
while x<=10:
  print(x*5)
  x=x+1



x=0
while x<=50:
  print(x)
  x=x+5

#Pattern questions
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********

#What to repeat?
#How much to repeat? Done-> 10 lines to print thats why 10 iterations will be there

x=1
while x<=10:
  print("*"*x)#String repeatition concept
  x=x+1





#          *
#         **
#        ***
#       ****
#      *****
#     ******
#    *******
#   ********
#  *********


x=1
while x<=10:
  print(" "*(10-x) +  "*"*x)
  x=x+1



#" "*(10-x) -> give spaces

("Maini"*5) +("pal"*5)

#      *
#     ***
#    *****
#   *******
#  *********
# ***********
#Length of traingle will be last line total stars

#break and continue
#break: A keyword that is use to stop the loop forcefully

x=1

while x<=50:
  if x==25:
    break#We will get out of loop permanently
  print(x)
  x=x+1#25

# Example: Simple calculator (demonstrating while loop with break)
# To make this interactive, replace the predefined values with input() calls
# Example with predefined values:
print("\n--- Calculator Example ---")
num1 = 100
num2 = 50
ch = "+"
print(f"Calculation: {num1} {ch} {num2}")

if ch == "+":
    print(f"Result: {num1 + num2}")
elif ch == "-":
    print(f"Result: {num1 - num2}")
elif ch == "*":
    print(f"Result: {num1 * num2}")
elif ch == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Operation not allowed")

print("Thanks for using calculator")







#LCM -> Least common multiple
#Note: Whe you have a question of input
#Generate output manually by assumimg different inputs


#Note: IF we want to find lcm then we have to find the multiples


# 15

# 9

# 9
# 18
# 27
# 36
# 45-> yes
# 54
# 63
# 72
# ..


# 15
# 30
# 45
#Pick one number and keep finding its multiple and also keep checking that if that number is divisble by second number or not
#If any multiple occur that is also divisible by second number -> its LCM

num1=89
num2=15
x=1
while True:
  multiple=num1*x#9*1=9   9*2=18  9*3=27  9*4=36  9*5=45.........
  if multiple%num2==0:#Common multiples will pass this condition(True)
    print("LCM is ",multiple)
    break
  x=x+1


# Suppose there is monday on 1st october and user will enter the number of day between 1 and 31

# Print the name of weekday on that day.

# Example if user enter 4
# then print Thursday

# if user enter 8 print Monday

num = 8  # Predefined value
if num==1 or num==8 or num==15 or num==22 or num==29:
  print("Monday")
elif num==2 or num==9 or num==16 or num==23 or num==30:
  print("Tuesday")
elif num==3 or num==10 or num==17 or num==24 or num==31:
  print("Wed")
elif num==4 or num==11 or num==18 or num==25:
  print("Ths")
elif num==5 or num==12 or num==19 or num==26:
  print("Fri")
elif num==6 or num==13 or num==20 or num==27:
  print("SAt")
elif num==7 or num== 14 or num==21 or num==28:
  print("Sun")


x=0

while x<10:
  print("HEllo world")
  x=x+1

#for loop
#for loop is use to iterate over a object or when we have particular amount of iterations
#We can apply for loop over datatypes which are sequence or iterables
#Syntax:
#for variable in container:
    #Statements
    #statements
    #.......

#Example:
s="Rohan Sharma"
for x in s:
  print(x)
#Work: Above syntax will take out elements from container one by one and keep storing it in variable

#range function
#range function is use to generate the sequence of numbers
#range(10) -> 0 1 2 3 4 5 6 7 8 9(10 excluded)
#range(5,30)-> 5 6 7 8 9 10 11 12 13 14 ........29(5->start,   30->stop)
#range(5,30,3)->5 8 11 14 17 20 23 26 29
#Here 3 is no of steps
#5->start
#30 -> stop

#How we can use this function with for loop?

for x in range(3, 15):  # Limited to show 12 values instead of 47
    print(x)


for x in range(1,11):
  print("*"*x)
#Task: Solve all patterns using for loop

# Example: Count vowels in a string
print("\n--- Vowel Counter Example ---")
s = "Rohan Sharma"  # Predefined for continuous execution; replace with input() for interactive use
count = 0
for x in s.lower():  # Convert to lowercase to catch both cases
    if x in "aeiou":
        count += 1

print(f"String: '{s}' - Vowel count: {count}")




# Example: Print first 10 multiples of 8
print("\nFirst 10 multiples of 8:")
for i in range(1, 11):
    print(i * 8, end="  ")
print()  # New line




#Q:Check if given no is prime or not

#Prime no is that which does not have any factor other than  itself or 1

num=49
#Note: If a number is prime it will complete the loop
#if a number is not prime it will come thorugh break
flag=0
for x in range(2,num):
    if num%x==0:
      flag=1
      break


if flag==1:
  print("Not prime")
else:
  print("Prime")


# Container datatypes

#List
#It is a container dtype that is use to store multiple elements of different types in a sequence
#Syntax: Use square bracket
l=[23,45,'mani',6.7]
print(l)
#Indexing:
print(l[-1])
#Slicing
print(l[0:2])

#Characterstics of list
#Mutable: We can update a existing list
l[0]=100
print(l)
#ORdered: List store elements in same order in which we create them
#Iterable: We can apply loop directly on list
l=[4,6,8,8,7,0]
for x in l:
  print(x)


#Methods of list
#append method
l=[3,4,5,6]
l.append(100)
print(l)
#append method is use to add an element at last position of list

#Extend: It is use when we want to add sequence of multiple elements at last of list
l=[3,4,5,6]
l.extend(['mani','theta',3,4,5])
print(l)
#Note: In extend we have to pass another iterable

#remove: IT is use to remove an element from list
#We have to pass that element in function
l=[45,67,89,89,89]
l.remove(89)
print(l)
#It will only delete first occuring element

#pop
#IT is used when we want to remove element by its position
l=['mani','rohan',45,67,8.9]
l.pop(1)#IT will remove element fro 1st position
print(l)

#insert
#It is use to add an element on a particular position
l=['mani','rohan',45,67,8.9]
l.insert(1,78)#Here 1 is position and 78is element
print(l)

#If we want to add something at multiple positions
l=['a','b','c','d','e','f','g','h','i','j']
l[2:7]=2,6#Packing
print(l)

#Sorting
l=[3,4,5,6,5,4,3]
l.sort()#This will keeplist in ascending order
print(l)

#If we want descending
l.sort(reverse=True)
print(l)

#count: it tells the count of element which we pass in list
l=[23,4,5,5,5,5,56,7,8,8,8,8,8,8,8]
print(l.count(8))#PAss element whose count we want to check


#How many students get highest marks?

l=[34,5,5,67,56,45,34,23,67,67,67,8,9,67,12]
#1- Find highest marks
l.sort()
high=l[-1]
#2- Find count of that marks
print(l.count(high))

#index: It tells the position of element in a list
l=['mani','rohan','khurana']
l.index('rohan')

l1=[3,4,5]
l2=l1#Shallow copy: whatever happends in first list same will occur in second one
l1[0]=100
print(l1)
print(l2)

#Deep copy: Copied list will be in different memory
l2=l1.copy()#Function to create deep copy
l1[0]=200
print(l1,l2)

l=[4,5,6]
l.clear()#Delete all elements from list
print(l)
#USe range and for loop
#Enter 5 integers frm user and keep appending them in list

#Nested list
l=[[2,3,4],[5,4,3],[5,4,4]]
l[2][0]#Will extract 5 from last list

#Task: Take 5 integers from input and eneter in list
#Task: There are n zeros in a list remove them from list #Hint: use count and remove
#Task: There are two list join them


#When we apply loop on a list :
#We have two ways to do that
###1: USing range method: for x in range(len(l))

####2: USing direct method

l=[34,56,45]
l[0]=100
l

#IF we want updation in same list use range method
for i in range(len(l)):#0 1 2 3 4 5..... len(l)
      l[i]=0

print(l)

#Usig direct method: In this method each element of list gets copied to x one by one
l=[4,5,55,7,8,9,0]
for x in l:
  print(x)#If we changing x here it will not change list elements


#There is a list of numbers. MAke another list which will be square of that list
l1=[3,4,3,2,3]
l2=[]
for x in l1:
  l2.append(x**2)
print(l2)

#Tuple
#Tuple is a also a sequence of elements like a list
#But once tuple is made its elements cannot be changed(Immutable)
#Syntax: variable=()
#Indexable and iterable
#Ex
t=(56,'mani',6,7,8,9.0,[3,45,5],(7,6,5))
t[0:5]
for x in t:
  print(x)

#t[0]=100-> not possible

t=(56,'mani',6,7,8,9.0,[3,45,5],(7,6,5))
print(t.count(8))#Tells count of element passed
print(t.index(8))#Tell position of element

t=(2,3,4,5)
#We can change tuple to list and list to tuple using typecasting
l=list(t)#tuple->list
print(l)
l[0]=100
t=tuple(l)#List->tuple
print(t)

#Builtin helpful functions
l=[4,5,55,6,7]
print(max(l))#Tell largest element in list
print(min(l))#Tell smallest element in list
print(sum(l))#Tell sum of elements

#We can pass any iterator in these functions
#Task: Find sum of integers of list without using sum function


#Dictionary
#In this dtype we use to orient data in the form of key:value pair
#It used when we want to search data with a name
#Ex:Syntax: {key:value}
rec={"Rohan":20,"Vivek":30,"Mani":40}
rec['Mani']
#Properties of dictionary:
#Dict is indexable
#Dict is unordered

#Note: Value can be of any dtype but key can be only immutable dtype like
#string,tuple,int,float,complex...
rec={"Name":['Mani',"Rohan","Vivek"],"Marks":[3,4,5],'uid':[1,2,3]}


#Methods of dictionary
rec={"a":45,"b":56,"c":56,"d":67}
#get method: It is use to get the value of a key and if not found it will result in a default value
rec.get("g","None")
#Def: If rec have "a" it will tell its value if not it will tell "None"

l=[4,5,5,67,8,89,9,5,6,7,8,]
#find central element
#Beech mei h
#Center of length

position=len(l)//2
l[position]

#Pop method
#it is use to remove key passed
rec={"a":45,"b":56,"c":56,"d":67}
rec.pop("b")
print(rec)

#Update
#It is use to update the value of existing key, if that key does not found it will create new key:value pair
rec={"a":45,"b":56,"c":56,"d":67}
rec.update({"a":0,"h":90})#We have to pass dictionary in this method
print(rec)

rec={"a":45,"b":56,"c":56,"d":67}
#setdefault: It is use when we want to make a key:value pair when not found
#syntax: setdefault(key,value)
#IF key is founded  its value will be returned but if key is not founded it will make
#its key:value pair in dictionary
print(rec.setdefault("g",100))
print(rec)

rec={"a":45,"b":56,"c":56,"d":67}
#keys: it is use to return the list of keys only
print(rec.keys())
#values: It is use to return the list of all values in the dictionary
print(rec.values())

#items: It is use to return key and values in tuple form
print(rec.items())

#Set: It is an unordered collection of items
#Syntax: use {}

s={3,4,6.7,'mani',4,4,4}
print(s)
#Indexing not possible
#Iterable
#Note: We can only store unique items
for x in s:
  print(x)




#Methods of set
s={3,4,6.7,'mani',4,4,4}
s.add(45)#It is use to add element in a set
print(s)

s.remove(45)
print(s)#It is use to remove element from set


#union
#It is use to combine two sets together
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.union(s2))
#Return a set which contain elements of both sets(Duplicacy not allowed)

#intersection: IT return set of common elments between two sets
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.intersection(s2))

#difference
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.difference(s2))
#It will return set of elements contain those which are only present in s1

#symmetric_difference
#Return set of elements which are not common with both set
s1={1,2,3,4}
s2={3,4,5,6}
print(s1.symmetric_difference(s2))


#subset
s1={1,2,3,4}
s2={1,2,3,4,5,6}
print(s1.issubset(s2))
#s1 is subset of s2 because it have all elements that are present in s2

s1={1,2,3,4}
s2={1,2,3,4,5,6}

count=0
for x in s1:
  if x in s2:
    count=count+1


if count==len(s1):
  print("s1 is subset of s2")
else:
  print("No")

# Functions

#USer defined functions
#Functions are use to increase the reusability
#They are use to perform taks which are repeatable
#Syntax:
#def fxn_name():
#   statements
#   .........

#Ex: Make a function that print("Hello world")
#When fxn is defined it is saved somewhere
def fxn():
  print("Hello world")



#Calling a fxn
fxn()

#Functions
#Sometimes to run a function we need some data to feed
#Ex: Make a function that will print sum of two numbers


def Sum(x,y):#x and y are parameters
    res=x+y
    print(res)



Sum(23,45)#We are sending two arguments




#Function that returns something
#MAke a function that is return square of a number

def sqr(x):
  res=x*x#16
  return res#res returned will be back to function calling


result=sqr(4)#the returned value will be stored in result variable
print(result)

#Task: Make  a function that will take a number and return total factors of it within 1 and 100 in list form
def fxn(x):#x is 200
  l=[]
  for f in range(1,x):#range(1,200)
        if x%f==0:
          l.append(f)#l will will keep apending that number which is factor of 200
  return l



factors=fxn(200)#List returned by above function is stored into factors variable
print(factors)

#Task: Make a function that will accept two numbers and return largest number from both

#Sometimes function demands infinite arguments
#Arbitrary arugments
def fxn(*args):#args is  a tuple
  print(args)



fxn(454,5,5,5,4,3,2,3,5,5,6,6,77,8,9,9)#All these arguments will be sent to args variable in the form of tuple

#Keyword arguments
def fxn(x,y,z):
  res=x+y+z
  print(res)


fxn(y=0,z=89,x=100)#another way to send arguments to function


#Sending infinite keyword arguments
def fxn(**kwargs):#kwargs is a dictionary
  print(kwargs)


fxn(a=90,c=90,r=89)
#all keyword arguments will take the form of dictionary

# Exception handling

# Handling errors that may occur during execution
# try-except: We use try where there is a chance of error in future
# If error occurs, execution goes to the except block
print("\n--- Exception Handling Example ---")
try:
    x = 10  # Predefined values
    y = 5
    print(f"Division: {x} / {y} = {x / y}")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Exception handling completed\n")

# raise keyword: Custom error raising
print("--- Raise Keyword Example ---")
num1 = 60  # Predefined values
num2 = 30
if num1>100 or num2>100:
  raise ValueError("Numbers are greater than 100")
else:
  print(num1+num2)

#Syntax: raise Error_type(Message)

# File handling
# File handling is the concept of dealing with file reading, writing, and updating
# There are 3 modes to open a file:
# 'r' - read mode
# 'w' - write mode (overwrites existing file)
# 'a' - append mode (adds to end of file)

print("\n--- File Handling Examples ---")

# Example 1: Create and write to a file
print("Creating 'sample.txt' file...")
f = open("sample.txt", 'w')
f.write("Hello World\n")
f.write("This is line 2\n")
f.write("This is line 3 with letter a, a, a")
f.close()
print("File created successfully\n")

# Example 2: Read from a file
print("Reading from 'sample.txt'...")
f = open("sample.txt", 'r')
content = f.read()  # Read entire file
print("File content:")
print(content)
f.close()

# Example 3: Count occurrences of a character
print("\nCounting 'a' characters...")
f = open("sample.txt", 'r')
content = f.read()
count = content.count('a')
print(f"Character 'a' appears {count} times")
f.close()

# Example 4: Append to existing file
print("\nAppending to 'sample.txt'...")
f = open("sample.txt", 'a')
f.write("\nAppended line: Hello Everyone!")
f.close()
print("Append complete\n")

# Example 5: Update file content
print("Updating file content...")
f = open("sample.txt", 'r')
s = f.read()
f.close()

# Replace content
s = s.replace('Hello', 'Hi')

f = open("sample.txt", 'w')
f.write(s)
f.close()
print("File updated successfully")

#Take out text of a webpage using request module

# Libraries and packages

#Module: A python file
#Package: Collection of particular type of files
#Library-> collection of packages and modules

#import-> it is use to load the module in our working file
import math
math.sqrt(2)
#sqrt is a function that is available in math module


#from and import
#Ex: we only want to import sqrt fxn
from math import sqrt
#Benefit is we can now access sqrt fxn without . operator
sqrt(2)

# Numpy

#Numpy-> numeric python
#Numpy is used when we have lot of data to be stored in an array like dtype
import numpy as np
#as np means from now numpy will be called as np

#numpy is use to create the nd-array
#nd-array means n-dimensional array where data can be stored in any dimensions

arr=np.array([3,4,5,6])
print(arr)



#1d array
import numpy  as np
arr=np.array([2,3,4,5,6,7])

#2d array
arr2d=np.array([[3,4,5],
                [5,6,7]])

arr2d

#3d array
arr3d=np.array([[[3,4,5],[5,6,7]],[[5,6,7],[7,8,9]]])
arr3d

arr=np.array([[4,5],
             [6,7]])
print(arr.ndim)#Tells the dimensions of an array
print(arr.size)#total no of elements in array
print(arr.dtype)#Tells the dtype of array
#Note:We can only store one dtype in numpy array
print(arr.shape)
#3x2

#Different ways to create the array
zeros=np.zeros((4,5))
#Zeros fxn will create an array filled up with 0's and will be of shape passed as tuple
zeros

ones=np.ones((4,5))
#It will create array filled up with 1's of given shape
ones


arr=np.random.randint(4,15,(7,8))
#4->start of range
#15-> end of range
#(7,8)->shape
#This fxn will create array of shape(7,8) within the given range of random elements
arr
#Task:Print the sum of primary diagonal of square array(rows=columns)-> loop

import numpy as np
#Indexing/slicing in a numpy array
#In case of 1d array:
#The indexing slicng will be same as done in a list
arr=np.array([3,4,5,6,7])
print(arr[1:6])


#In case of 2d array
arr2d=np.array([[2,3,3,4],
                [6,7,8,7],
                [0,0,1,2],
                [7,8,6,5]])
#Syntax:arr2d[ row , column]
print(arr2d[2,1])
print(arr2d[-1,-1])#Last row,last column


#Slicing
print(arr2d[ 1:3 , 1:3])#LAst index excluded

#Stats function in numpy
arr2d=np.array([[2,3,3,4],
                [6,7,8,7],
                [0,0,1,2],
                [7,8,6,5]])

print(np.min(arr2d))
print(np.max(arr2d))
print(np.sum(arr2d))
print(np.mean(arr2d))
print(np.std(arr2d))#Standard deviation of data
print(np.var(arr2d))#Variance


#USing axis parameter

arr2d=np.array([[2,3,3,4],
                [6,7,8,7],
                [5,0,1,2],
                [7,8,6,5]])


np.min(arr2d,axis=0)#IT is returning a 1d array contain the minimum of each column of orignal array
np.min(arr2d,axis=1)#IT returns a 1d array contain the minumum of each row of orignal


#Note: This concept will be same wrt all above stats function

#shaping of array

arr=np.array([[2,3,3,4],
                [6,7,8,7],
                [5,0,1,2],
                [7,8,6,5]])
print(arr.shape)
#16->1,16     16,1   2,8    8,2   4,4    4,2,2   2,2,4   8,2,1...

#reshape: IT is a function that is use to change the shape of array(if possible)

arr=np.reshape(arr,(8,2))
#1-> Array
#2-> shape()

arr
#Note: (16,)->1d     (16,1)->2d

#Operations on numpy array
import numpy as np
arr=np.array([[3,4,5],
              [5,6,7],
              [9,9,9]])

#Operation between single element
arr+23#Every element is added with 23
arr%2#ebery element get divided and remainder is result

arr>5#every element get compared to 5 and result is True on that element which>5
#In every operation new array is resulted

#Operations between two numpy arrays
arr1=np.array([[3,4,5],
               [4,5,6]])
arr2=np.array([[67,7,5],
               [4,0,6]])

arr1+arr2#When same shape arrays get in an operation then pointwise operation  is done


#Operation row wise
arr=np.array([[3,4,5],
               [4,5,6],
              [0,0,0]])
temp=np.array([[12,3,4]])
arr+temp#3x3    1x3  (column numbers should be same for row wise operation)
#Row wise operation is possible if number of values is same in both arrays for each row of main array

#Column wise operation
arr=np.array([[3,4,5],
               [4,5,6],
              [0,0,0]])
temp=np.array([[12],
               [45],
               [78]])
arr+temp

#Filtering in numpy
#Ex: extract out elements from an array which are even numbers
arr=np.array([[34,56,78],
              [4,5,6],
              [7,8,10]])
#First make a boolean array and mask it over this array
f=arr%2==0
arr[f]#Only those elements will come where there is true in 'f'

#USing bitwise and logical operators
arr=np.array([[34,56,78],
              [4,5,6],
              [7,8,10]])


#In the case of array use bitwise operators like: &(and) |(or) ~(not)
#Ex: Elements that are greater than 10 and are even
f=(arr>10) & (arr%2==0)
arr[f]

import numpy as np
#any function
#IT check and return True if any of the element is True
#Indirectly we use it to see if atleast one element passes the condition or not

#Syntax: np.any(condition)
#Check if any of element in array is >10 or not
arr=np.array([[40,45],
              [5,6]])

print(np.any(arr>10))

#all function
#IT checks and retur True if all of the elements are True
#Indirectly we check that if all elements are satisfying the condition or not
#Check if all elements are even
print(np.all(arr%2==0))


arr=np.array([[3,4,5,6],
              [6,7,7,7],
              [0,0,0,8]])
np.all(arr%2==0,axis=1)#To check for each row
#Above is return an 1d array of boolean values, with True for that
#row which is fully even

#Check each column use axis=0
np.all(arr%2==0,axis=0)
#Give 4 values representing each column

#Same thing is in the case of any function

#Where function
#Where function is use to return the position of elements where condition is satisfied
#Syntax: np.where(condition)
a=np.array([12,4,5,67])#1d
arr=np.array([[12,0,56],
              [4,55,6]])


print(np.where(a>10))#Return a 1d array full of positions where elements were >10 in 'a'
print(np.where(arr>10))#Return Two arrays : 1- Row indexes  2- column indexes


#Suppose there is a sawraj factory in mohalli
#We are recording 5 attendences everyday in a month and send monthly report to the Bombay
#Suppose we are using numpy array to store it
#Find on which day more than 5 employees were totally absent
#Suppose there are 100 employees
att=np.array([[99,100,100,100,100],
              [100,100,99,99,98],
              [91,90,90,90,90],
              [95,98,97,89,90]])

f=np.all(att<95,axis=1)
print(np.where(f))



#HW: Find the day where no employee was there in whole time
#HW: Find the day where no employee was there in a shift of day

#insert,delete and concat
#insert: it is use to insert a row or a column according to the axis
import numpy as np
arr=np.array([[3,4,5],
              [5,6,7]])
#Inserting a row
arr=np.insert(arr,1,[0,0,0],axis=0)
arr
#1 parameter- array
#2- index-> where we want to add
#3- values- Value we want to add
#4- axis-> row wise or column wise


#Insert a column
arr=np.array([[3,4,5],
              [5,6,7]])
arr=np.insert(arr,2,[[0,0],[5,5]],axis=1)
arr

# Concatenate function (correct name: concatenate, not concat)
final = np.concatenate((arr1, arr2), axis=0)
print("Concatenated array:")
print(final)

#delete
arr1=np.array([[2,3],
              [5,6],
               [0,0]])
arr1=np.delete(arr1,[1],axis=0)
arr1
#We have to pass the list of indexes of rows or columns which we want to delete
#axis=0->rows
#axis=1->columns

#Note: When we dont pass axis as parameter then it will convert whole array into 1d

import numpy as np
#Unique function: It is use to find the unique elements in the array
arr=np.array([[3,4,5],
              [5,6,6],
              [6,6,5]])
uni=np.unique(arr)#IT will return the 1d array of unique elements if main array
uni


#Returning count
uni,counts=np.unique(arr,return_counts=True)#IT will provide two things
#1- unique elements
#2- Their respective counts
uni,counts

#Returning counts and index
uni,index,counts=np.unique(arr,return_counts=True,return_index=True)
uni,index,counts
#IT will return three things: 1- unique elements  2- their first position   3- their count

# Pandas example with sample data
import pandas as pd

print("\n--- Pandas Example ---")
# Create sample dataframe instead of reading non-existent CSV
data = {
    'name': ['Maruti Swift', 'Hyundai i20', 'Ford EcoSport', 'Tata Nexon', 'Mahindra XUV500'],
    'fuel': ['Petrol', 'Diesel', 'Petrol', 'Diesel', 'Petrol'],
    'selling_price': [500000, 600000, 780000, 900000, 1100000],
    'km_driven': [50000, 75000, 30000, 45000, 20000],
    'seats': [5, 5, 5, 5, 7]
}

df = pd.DataFrame(data)
print("Sample Data:")
print(df)
print("\nData Info:")
print(df.info())

# Indexing and slicing
print("\n--- Pandas Indexing & Slicing ---")
# iloc: position-based indexing
print("\nRow 1-3, Column 0-2 (position-based):")
print(df.iloc[0:3, 0:2])

# loc: label-based indexing
print("\nRows with name and fuel columns:")
print(df.loc[0:2, 'name':'fuel'])



# Statistical functions
print("\n--- Statistical Functions ---")
print(f"Min price: {df['selling_price'].min()}")
print(f"Max price: {df['selling_price'].max()}")
print(f"Sum: {df['selling_price'].sum()}")
print(f"Mean: {df['selling_price'].mean()}")


#Operations on column
new=df['km_driven']+2000#A new column will be generated with 2000+ values for each km_driven
new

f=df['selling_price']>1000000
f
#IF we apply the boolean column in the square brackets of dataframe then it will only show that position where there is True
df[f]#Masking

#Above thing is giving us car rows where price is  greater than 10 lakh

#Task: Find the Petrol cars with price less than 500000
f=(df['fuel']=='Petrol') & (df['selling_price']<500000)
df[f]


#Only give car names
df.loc[ f , 'name' ]

#Filtering on string type of columns
f=df['name'].str.isalpha()#Return True/False series
df[f]

#Find the name of cars who starts with M letter
f=df['name'].str.startswith('M')
df[f]

#contains-> this function is use to check the pattern of string or to see if a substring present or not
#Find cars having swift their name
# SKIPPED: df=pd.read_csv("/content/drive/MyDrive/Car.csv")
  # File does not exist, using existing df from earlier example

f=df['name'].str.contains('Swift')#Swift substring will be searched in each name string
df[f]

#isin function
#IT is use to find the categories or values present in list or array type
cars=['Maruti Swift Dzire VDI','Maruti Swift Dzire VDI']

f=df['name'].isin(cars)#Will return True for that car which is present in list
df[f]

#Update method
import pandas as pd
# SKIPPED: df=pd.read_csv("/content/drive/MyDrive/Car.csv")
  # File does not exist, using existing df from earlier example
df

#Replace method: IT is use when we want to replace a particular values in a column with another values
#We have to pass dictionary with this syntax{oldvalue :new value}

df['fuel']=df['fuel'].replace({"Diesel":"D","Petrol":"P"})
df


#apply method
#IT is use to update a column with a custom logic
#We have to pass a function name in the parameter of apply function which will
#update each value of column
#Task: Make all maruti cars name in upper case

def fxn(x):
  if 'Maruti' in x:
    return x.upper()
  else:
    return x.lower()

df['name']=df['name'].apply(fxn)
df
#Note: We should make or use sucha function that can accept a value as parameter
#and return something

# SKIPPED: df=pd.read_csv("/content/drive/MyDrive/Car.csv")
  # File does not exist, using existing df from earlier example

#Indexing
#A row never leaves its index irrespective of copy or deleted or moved
x=df.iloc[0,:]  # First row instead of out-of-bounds 8123
x

#Set a column as index
# df=df.set_index("name")#From now name is not a column anymore
# Index example complete


#Reset index-> The index column will change into normal position numbers
# df=df.reset_index(drop=True)#drop=True means, whatever column was present in index will get deleted permanently
df



# SKIPPED: df=pd.read_csv("/content/drive/MyDrive/Car.csv")
  # File does not exist, using existing df from earlier example

#Inserting,concating and delete
#Adding a row
#TO add row we have to pass the dictionary with column name as key and their value which will get inserted as row
# SKIPPED: # df=df._append({"name":"santro","fuel":"Petrol","selling_price":23000},ignore_index=True)
  # Requires valid dataframe
df
#Note: The column values not given will be replaced by NaN(type of a null value)

#Deleting a row-> pass list of indexes
# df=df.drop(index=[1,3])
df

X=df.iloc[0:10]
Y=df.iloc[30:50]

#Combining two or more df's
final=pd.concat((X,Y),axis=0,ignore_index=True)
#axis=0->row wise
#axis=1 means column wise
#Ignore_index=True means to forget the old index and recreate them
final


import pandas as pd
# SKIPPED: df=pd.read_csv("/content/drive/MyDrive/Car.csv")
  # File does not exist, using existing df from earlier example

#sort values->IT is use to sort the dataframe in ascending or descending order according to the values of
#column we pass

# df=df.sort_values("selling_price")
df

#TO sort in descending order we have to pass ascending=False

# df=df.sort_values("selling_price",ascending=False)
df


# SKIPPED: df=pd.read_csv("/content/drive/MyDrive/Car.csv")
  # File does not exist, using existing df from earlier example

#Group by function
#IT is use to find the statistical information of dataframe for each type of category in a particular column
#When we apply group by it internally convert dataframe into n dataframes. where n is number of category in column

groups=df.groupby("fuel")#groups now contain individual df's for CNG,LPG,Petrol and Diesel cars

#Now whatever function we apply on groups ,it will be aplied on all df's in it
groups['selling_price'].mean()



groups.head(5)
#Note:Index of rows willbe same in groups also

#Getting multiple reports using group by
#agg function-> it is use to extract the multiple stats value from groups
#Pass the list of aggregate functions in the agg function
report=groups[['selling_price','km_driven']].agg(['mean','std','median'])
report

#Idxmax vs idxmin
#These function are use to find the index of min and max item in dataframe
df['selling_price'].idxmin()
#5713 means the car with minimum selling price have row number or index=5713

groups['selling_price'].idxmin()

#Find the name of car in each fuel category having min price
groups=df.groupby("fuel")

#1-> Find the index of cars having min price
index=groups['selling_price'].idxmin()#index is a kind of list of indexes of min price cars


#2- Now use loc method to find name
df.loc[index ,['name','fuel']]

# Matplotlib visualization (using sample data from above)
print("\n--- Matplotlib Examples ---")
from matplotlib import pyplot as plt

# Line plot
print("Creating line plot...")
year = [2001, 2002, 2003, 2004, 2005, 2006]
marks = [12, 3, 0, 90, 67, 8]
plt.figure()
plt.plot(year, marks, color='red', marker='o', linewidth=2)
plt.title("Year vs Marks")
plt.xlabel("Year")
plt.ylabel("Marks")
plt.grid(True)
plt.savefig('line_plot.png')
plt.close()
print("Line plot saved as 'line_plot.png'")

# Bar chart
print("Creating bar chart...")
X = ['Petrol', 'Diesel', 'Other']
y = [100, 30, 60]
plt.figure()
plt.bar(X, y, width=0.6, color=['red', 'blue', 'green'])
plt.title("Fuel Type Distribution")
plt.savefig('bar_chart.png')
plt.close()
print("Bar chart saved as 'bar_chart.png'")

# Machine Learning Example

print("\n--- Machine Learning Concepts ---")
print("\n1. Supervised Learning Types:")
print("   - Regression: Predicting continuous values")
print("   - Classification: Predicting categories")
print("\n2. Unsupervised Learning:")
print("   - Clustering: Grouping similar data")
print("\n3. Semi-supervised Learning:")
print("   - Learning from both labeled and unlabeled data")

print("\nMachine Learning Pipeline:")
print("1. Data Collection")
print("2. Data Cleaning (handle missing values)")
print("3. Data Preprocessing (encode, scale)")
print("4. Model Training")
print("5. Model Testing")
print("6. Model Deployment")

# Example: Simple preprocessing with sample data
print("\n--- Preprocessing Example (with sample data) ---")
import pandas as pd
import numpy as np

#sklearn - not installed. Install with: pip install scikit-learn
    ##from sklearn.preprocessing import LabelEncoder, StandardScaler
#from sklearn.model_selection import train_test_split

# Create sample insurance-like dataset
sample_data = {
    'age': [25, 35, 45, 55, 65],
    'gender': ['M', 'F', 'M', 'F', 'M'],
    'smoker': ['no', 'yes', 'no', 'no', 'yes'],
    'charges': [1000, 2000, 3000, 4000, 5000]
}

df = pd.DataFrame(sample_data)
print("Original Data:")
print(df)

# Separate independent (X) and dependent (y) variables
X = df.iloc[:, :-1]
y = df['charges']

print("\nIndependent Variables (X):")
print(X)
print("\nDependent Variable (y):")
print(y.values)

# Label Encoding for categorical variables
le = LabelEncoder()
X_encoded = X.copy()
X_encoded['gender'] = le.fit_transform(X['gender'])
X_encoded['smoker'] = le.fit_transform(X['smoker'])

print("\nAfter Label Encoding:")
print(X_encoded)

# Standard Scaling
sc = StandardScaler()
X_scaled = sc.fit_transform(X_encoded)
print("\nAfter Standard Scaling:")
print(X_scaled[:3])  # Show first 3 rows

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
print(f"\nTraining set size: {len(X_train)}")
print(f"Testing set size: {len(X_test)}")

print("\nML Notes:")
print("- Regression models: LinearRegression, SVR, DecisionTree, RandomForest")
print("- Classification models: LogisticRegression, SVM, DecisionTree, RandomForest, AdaBoost, XGBoost")
