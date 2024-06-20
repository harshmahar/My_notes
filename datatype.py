# Data Type:
# 1. Numerical data 	-  1. Integer (int)	2. Float	3. complex (21j)             
# 2. Text type data 	-  string (str) 											 
# 3. Sequence data 	-  list [], 	  tuple (),     range()							
# 4. Mapping data 	-  Dictionary {key:values}
# 5. set data 		-  set {}
# 6. Boolean data 	-  True, False
# 7. None 			-  None
# -----------------------------------------------------------------------

# list : list is always written in square bracket.
# x = ["data", "science",234, 453.5]

# tuple : tuple is written in round bracket.
# x = ("data", "science",234, 453.5)

# range() : It is used to print the numbers in a sequence.
# range(starting, ending, step_size)
# range(1,50, 2)

# set : set is always written in curly bracket.

# dictionary : dictionary is written in curly bracket and pair of key and values.'''

# '''x=75
# y=54j
# z=43.2
# a= "harsh mahar"

# print(x)
# print(type(x))

# print(y)
# print(type(y))

# print(z)
# print(type(z))

# print(a)
# print(type(a))
# '''


# How to find the length
#x = "Data Science"
#print(x)
#print(len(x))

#x = "12000"
#print(len(x))

# x="10"      #(If number is in string it will be joined not added)
# y="20"
# print(x+y)

# x= "data"
# y= "science"
# print(x+y)


# Forecasting of data
# It is to change the data type.
# 
# x=456
# print(type(x))

# x = str(x) #changed into string
# print(x)

# print(type(x))
# print(x*5)
# 

# #change into float, complex, list, int
# """x = "125"

# a = int(x) 
# print(a)
# print(type(a))

# b = float(x)
# print(b)
# print(type(b))

# c = list(x)
# print(c)
# print(type(c))
	
# d = complex(x)
# print(d)
# print(type(d))

# x="234"
# a=set(x)
# print(e)
# print(type(e))

# alphabet cant be converted into number
# number can be converted into alphabet
# number cant be converted into list, tuple, set, dictionary
# alphabet can be converted into list, tuple, set, dictionary
# length of numerical data cant be found. """

# x=12
# y=12
# z= x/y
# print(z)
# print(type(z))


# x=4325
# y= str(x)
# print(len(y))



# TYPES OF OPERATORS

# 1.	Arithmetic Operators
# 2.	Assignment Operators
# 3.	Comparison Operators
# 4.	Logical Operators
# 5.	Identity Operators
# 6.	Membership Operators
# 7.	Bitwise Operators
# ----------------------------------------------------

# 1. Arithmetic Operators
# +  : Addition
# -  : substraction
# *  : multiplication
# /  : Division
# %  : Modules  		- It shows the remainder.
# ** : Exponentation  - It is used to add the power on numbers.
# // : Floor Division - It shows the value before the decimal.
# '''


# # Modulus

# x = 45
# y = 20
# print("Modulus : ",x%y)

# print("The Modulus of", x, "and", y, "is :", x%y)'''


# # Exponentation

# x=5
# y=3

# print("Exponent : ",x**y)
# print("The Exponent of",x,"and",y, "is :", x**y)



# # Floor Division

# x=19
# y=5
# print("Floor : ", x//y)


# x = 13
# y = 7
# z = x%y
# print(type(z))

# -------------------------------------------------------------

# 2. Assignment Operators

# =  : Assign
# == : Equal to
# != : Not equal to
# += :		(or)	x = x + 1
# -= :		(or)	x = x - 1
# *= :		(or)	x = x * 1
# /= : 		(or)	x = x / 1
# '''

# Equal to
# x=45
# y=45
# print(x==y)

# Not equal to
# x=100
# y=200
# print(x==y)
# print(x!=y)

# Plus equal to (+=  or  x = x + 1)
# x = 50
# x+=5
# x+=10
# x+=20
# print(x)


# Minus equal to (-= or x = x - 1)
# x = 100
# x-=50
# x-=10
# print(x)


# Multipy equal to (*= or x = x * 1)
# x = 50
# x*=2
# x*=4
# print(x)

# Divide equal to (/= or x = x / 1)
# x = 50
# x/=5
# print(x)


# 3. Comparison Operators
# >  : Greater than
# <  : Less than
# >= : Greater than equal to
# <= : Less than equal to
# == : Equal to
# != : Not equal to


# x = 45
# y = 10
# print(x>y)
# print(x<y)

# x = 100
# y = 100
# print(x==y)
# print(x>=y)
# print(x<=y)


# if_else statement - it is used to divide the data in different categories.


# write a python program to show if number is greater than 10 then print YES else NO

# x = 10

# if x>50:
# 	print("Greater than 50")
# else:
# 	print("Smaller than 50")


# x = 15

# if x%2==1:
# 	print("Odd")
# else:
# 	print("Even")


# Write a code to check if x is ODD.

# x = 41

# if x%2==1:
# 	print("ODD number")



# Check the number is divisible of 9 or not
# 81 , 75, 40

# x = 82

# if x%9==0:
# 	print("Divisible by 9")


# User Input : It is a input where you enter the values in output screen.

# x = int(input("Enter any number : "))

# if x%2==0:
# 	print("Even Number")
# else:
# 	print("Odd Number")


# write a code with the help of user input and show number is greater than 200 print ("greater than 200") else print ("LESS than 200")


# x = int(input("Enter number : "))

# if x>200:
# 	print("Greater than 200")
# else:
# 	print("Less than 200")


# If text is equal to "Delhi" print "YES" or "NO"

# x = str(input("Enter Text: "))

# if x=="Delhi":
# 	print("YES")
# else:
# 	print("NO")


# Write a python Program to show the state and Capital According to user input state


# x = str(input("Enter State Name : "))

# if x =="Bihar":
# 	print("Patna")
# else:
# 	print("Other")


# 4. LOGICAL OPERATORS
# and : It returns TRUE when both conditions are met.
# or : It returns TRUE when at least one condition is met.
# not : It reverses the output of (and or)


# x = 20
# y = 10

# print(x>10 and y>5)

# if x>10 and y>5:
# 	print("Both Conditions are true")
# else:
# 	print("Wrong condition")


# If number is between 20 to 30 then "YES" else "NO"

# x = int(input("Enter number: "))

# if x>=20 and x<=30:
# 	print("Yes")
# else:
# 	print("No")


# Check if number is divisible by 10 or 5 then print YES else NO

# x = int(input("Enter number : "))

# if x%5==0 or x%10==0:
# 	print("YES")
# else:
# 	print("NO")


# Write a code to check which number is greater - x or y.


# x = int(input("enter 1st number: "))
# y = int(input("enter 2nd number: "))
# if x>y:
# 	print(x, " is greater than ",y)
# else:
# 	print(y, " is greater than ",x)


# Check if the number is divisible by 5 and 10.

# x = int(input("Enter number: "))
# if x%5==0 and x%10==0:
# 	print("Divisible by 5 and 10")
# else:
# 	print("Not divisible by 5 and 10")	


# write code to print the last digit of any number is the number is odd.

# x = int(input("Enter number: "))
# if x%2==1:
# 	print("Last Digit: ",x%10)

# or 

# x = int(input("Enter any number: "))
# y = x%10	
# if x%2==1:
# 	print("Last Digit: ",y)
	


# Write a code with user input to check if password is Equal then print "Correct Password" else "Wrong Password"

# p = "harsh123"
# x = str(input("enter password: "))
# if x==p:
# 	print("Correct Password")
# else:
# 	print("Incorrect Password. Try again")


# write code to print the discount and discounted amount if amount is less than 5000 then 20% else 30%


# x = float(input("Enter amount: "))

# if x<5000:
# 	print("Discount: ", x*0.2, "Amount: ",x-x*0.2)
# else:
# 	print("Discount: ", x*0.3, "Amount: ",x-x*0.3)

# or 

# amount = float(input("Enter amount: "))

# if amount<5000:
# 	d = amount*0.2
# 	a = amount-d
# else:
# 	d = amount*0.3
# 	a = amount-d

# print("Discount: ", d)
# print("Discounted Amount: ", a)



# --------------   ELIF  -----------------

# x = int(input("enter number: "))

# if x>=1 and x<10:
# 	print("first")

# elif x>=10 and x<20:
# 	print("second")
 
# elif x>=20 and x<30:
# 	print("third")

# else:
# 	print("fourth")

# --- OR ---

# x = int(input("Enter number: "))

# if x>=1 and x<10:
# 	a = "first"
# elif x>=10 and x<20:
# 	a = "second"
# elif x>=20 and x<30:
# 	a = "third"
# else:
# 	a="fourth"
# print(a)



# write code to show division 
# if percentage is greater or equal to 60 then print "First division"
# if percentage is greater or equal to 45 then print "Second division"
# if percentage is greater or equal to 30 then print "Third division"
# else print fail

# p = int(input("Enter Percentage: "))

# if p>60:
# 	d = "First Division"
# elif p>45:
# 	d = "Second Divsion"
# elif p>33:
# 	d = "Third Division"
# else:
# 	d = "Fail"
# print(d)



# write a code with user input to check which number is greater out of the three.

# x = int(input("Input 1st Number: "))
# y = int(input("Input 2nd Number: "))
# z = int(input("Input 3rd Number: "))

# if x>y and x>z:
# 	print(x, " is the greatest")
# elif y>x and y>z:
# 	print(y, " is the greatest")
# elif z>x and z>y:
# 	print(z, " is the greatest")
# else:
# 	print("Equal")


# --------------------------------------------------------------------------------

# SWAPPING
# MEMBERSHIP OPERATORS
# IDENTITY OPERATORS

# --------------------------------------------------------------------------

# What is swapping in python?
# When we exchange the values to other variable.

# x = 49
# y = 123

# print("x : ",x)
# print("y : ",y)

# print("after the update")

# x,y = y,x
# print("x : ",x)
# print("y : ",y)


# x = 20
# y = 30
# z = 40 
# print("x: ",x)
# print("y: ",y)
# print("z: ",z)

# print("after update")
# x,y,z = z,x,y
# print("x: ",x)
# print("y: ",y)
# print("z: ",z)
 
# x = 100  #-  300
# y = 200  #-  100  
# z = 300  #-  200  



# x,z = z,x  # x = 300, z = 100
# y,z = z,y  # y = 100 (z), z = 200 (y)

# print("x: ",x)
# print("y: ",y)
# print("x: ",z)


# Find the value of x

# x,y,z = 10,20,30
# x,z,x = z,x,y   # x ki value pehle 30 hui, then 20. it prints the latest value
# y=x

# print(x)


# A,B,C,D = 10, 20, 30, 40
# A = B  #  A = 20, B = 20
# C = D  #  C = 40, D = 40
# A,C,D = B, A, C   # A = 20, C = 20, D = 40
# print(A)
# print(B)
# print(D)


# x,y = "59"
# z = 12
# 5,9
# x,y = z,x   # x =12, y =12
# z,x = z, y  # z = 12, x =12
# x = y       # 12, 12

# print(x)
# print(y)
# print(z)

# ---------------------------------------------------------------------------

# MEMBERSHIP OPERATORS - in , not in

# x = "science"
# print("i" in x)
# print("I" in x)
# print("z" not in x)
# print("s" not in x)


# check 24 and 10 in list or not.
# x = [23,4,5,6,7,8,10]

# print(24 in x)
# print(10 in x)


# write code with user input to print YES or NO if name contains either "a" or "i"
# x = str(input("Enter name: "))

# if ("a" in x) or ("i" in x):
# 	print("YES")
# else:
# 	print("NO")	


# if Sunday in x then print present else not present

# x = ["Sunday", "Monday", "Tuesday", "Wednesday"]

# if "sunday" in x:
# 	print("Present")
# else:
# 	("Not present")



# Write a code to show the grade:
# If number is greater than 90 = A+
# If number is greater than 80 = A

# If number is greater than 70 = B+
# If number is greater than 60 = B
# If number is greater than 50 = C
# else fail

# x = int(input("Enter marks: "))

# if x>90:
# 	p = "A+"
# elif x>80:
# 	p = "A"
# elif x>70:
# 	p = "B+"
# elif x>60:
# 	p = "B"
# elif x>50:
# 	p ="C"
# else:
# 	p = "fail"
# print(p)



# Check if input year is leap year or not. 

# x = int(input("Enter year: "))

# if x%4==0:
# 	print("Leap Year")
# else:
# 	print("NOT")


# find are of circle

# r = 7
# pie = 22/7
# area = pie*r**2

# print(area)



# show average of first 5 numbers

# x = 1+2+3+4+5
# print(x/5)




# --------------        STRINGS       -------------------

# String : It is always written in double or single quotation.

# x = "abc123@$%^"

# print(x)
# print(type(x))
# print(len(x))


# upper : it  is used to convert the text into capital letters.
# lower : it  is used to convert the text into small letters.
# title : it is used to convert the first letter of each word to capital.
# capitalize : it only converts the first letter of text to capital.
# index: it is used to find the position of a character. 
# find:    ^ SAME
# count: it is used to count the repetition of a  character.
# swapcase: it is used to swap the upper case with lower case and vice versa.
# replace: It is used to replace old text with new text.
# split: It is used to covert string to list.
# join: It is used to convert list to string.
# strip: It is used to remove the extra space from starting and ending.


# upper

# x = "delhi"
# x = x.upper()
# print(x)

# ---- OR -----

# x = "delhi"
# print(x.upper())


# x = "Harsh Mahar"
# y = x.upper()
# print(y)


# -------------------------------------------------

#  lower

# x = "PATNA"
# x = x.lower()
# print(x)

#  ----- OR ------

# x = "PATNA"
# print(x.lower())



# x = "DATA SCIENCE"
# y = x.lower()
# print(y)
# -------------------------------------------------


#  title

# x = "gujarat"
# x = x.title()
# print(x)




# write a python program to check the text is equal or not

# x = "science"
# y = "scIENCE"

# if x == y.lower():
# 	print("YES")

# else:
# 	print("NO")
 



# x = str(input("Enter any name: "))
# y = x.upper()
# z = x.lower()

# if x == y or x == z:
# 	print("Yes")

# else:
# 	print("No")

# --------    OR    -----------

# x = str(input("Enter any name: "))
# y = x.upper
# z = x.lower
# if x == "Rohit".upper() or x == "rohit".lower():
# 	print("Yes")

# elif x == "Ranjan".lower() or x == "Ranjan".upper():
# 	print("Yes")

# else:
# 	print("No")


# -----------   OR   -----------

# x = str(input("Enter any name: ")).title()
# print(x)


# # --------      OR    -----------

# x = str(input("Enter any name: ")).title()

# if x == "Rohit":
# 	print("Yes")

# elif x == "Ranjan":
# 	print("Yes")

# else:
# 	print("No")


# -----------------------------------------------------------------------------

# SWAPCASE

# x = "scIENCE"
# x = x.swapcase()

# print(x)


# \'  Single Quote
# \\  Backslash
# \f  Form feed
# \r  Carriage Return
# \b  Backspace
# \n  New line
# \t  Tab
# \b  Backspace
# \f  Form feed



# String function


# String -  It is written in single or double quotations.

# x = "asd231"
# print(x)
# print(type(x))
# 1. Upper : Convert text to capital

# x = "prince"
# y = x.upper()
# print(y)



# 2. Lower: Covert text to small 

# x = "DATA SCIENCE"
# y = x.lower()
# print(y)



# 3. Title: Converts the first letter of each word.

# x = "leonardo dicaprio"
# y = x.title()
# print(y)


# 4. Capitalize: Convers the first letter of the first word.

# x = "lionel messi"
# y = x.capitalize()
# print(y)


# 5. Swapcase: Swaps the upper and lower case.

# x = "barCELona"
# y = x.swapcase()
# print(y)


# ----------------------------------------------------------------------------

# INDEXING AND SLICING

# Indexing: It is used to extract a single character from text.


# x = "D  E  L  H  I"
#      0  1  2  3  4   :-   Positive Indexing
#     -5 -4 -3 -2 -1   :-   Negative Indexing


# extract "m" from text

# x = "himachal"
# a = x[2]
# print(a)

#OR

#print(x[2])



# Extract r, a, A, P, h - positive

# x = "Arunachal Pradesh"
# y = x[-7]
# print(y)

# OR

# print(x[1])
# print(x[4])
# print(x[0])
# print(x[10])
# print(x[6])

# # Extract e, s, d, P  - negative

# print(x[-3])
# print(x[-2])
# print(x[-4])
# print(x[-7])



# Slicing: It is used to extract a range of characters from text.

# x[start : end : step]

# x = "Arithmetic"

# print(x[0:4])

# print(x[3:8])

# print(x[1:12:2])

# mach, desh, him, mac, rade
# step -  mca, hmca, aap

# x = "himachal pradesh"

# print(x[2:6])
# print(x[12:16])
# print(x[0:3])
# print(x[2:5])
# print(x[12:16])


# print(x[2:10:2])
# print(x[0:10:2])
# print(x[3:12:3])



# -----------------------
# rya, na, arya, hary  - negative
# x = "haryana"

# print(x[-5:-2])
# print(x[-2:])
# print(x[-6:-2])
# print(x[-7:-3])


# ----------------------------

# reverse text with slicing

# x = "Himachal Pradesh"
# print(x[-1::-1])

# x = "delhi"
# print(x[-1::-1])


# x = "Arunachal Pradesh"
# print(x[0:4])    # arun
# print(x[4:1:-1])   # anu
# print(x[3:6])   # nac
# print(x[5:2:-1])   # can
# print(x[-7:])   # Pradesh
# print(x[-1:-8:-1])   # hsedarP
# print(x[1:5])    # runa
# print(x[0:8:3].lower())   # anh
# print(x[6::-3].lower())   # hna
# print(x[-4:].upper())   # DESH





#-------------------------------------------------------------------------

#                INDEX AND FIND

# index() - it is used to show the position or index of alphabet
# find()  -  same ^

# x = "Data analyst"
# print(x.index(" "))


# x = "Data analyst"
# a = x.find(" ")
# print(f"Index of space: {a}")

# b = x.find("a")
# print(f"first a: {b}")

# c = x.find("a",b+1)
# print(f"second a: {c}")

# d = x.find("a",b+3)
# print(f"third a: {d}")

# e = x.find("a",b+5)
# print(f"fourth a: {e}")


# x = "india"

# a = x.find("i", x.find("i")+1)
# print(a)


# Count : It is used to count a particular character from the text.

# x = "data analyst"
# print(x.count("a"))



# count number of a
# x = "Arunachal"
# x = x.lower()
# print("Total Number of a: ",x.count("a"))



# 1. count length without space
# 2. count number of a and p
# 3. Extract first five letters
# 4. Extract first three letters

# x = "Python is A Programming LAnguage"  #   1.
# print("Length without space: ",len(x)-x.count(" ")) 

# a = x.lower()			#   2.
# p = a.count("a")+a.count("p")
# print(f"Number of a and p: {p}")


# a = x[0:5]       #   3.
# print(f"First five letters: {a}")

# b = x[-3:]			#   4.
# print(f"Last three letters: {b}")




# REPLACE : It is used to replace the values from old text to new text.

# x = "Data analyst"
# y= x.replace("a", "*")
# print(y)


# x = "python is a programming language"
# y = x.replace(" ","")
# print(len(y))



# SPLIT : It is used to convert the string to list based on delimiter.

# x = "python is a programming language"
# a = x.split(" ")  #  default delimiter is space like - x.split()
# print(type(a))
# print(a)



# JOIN: It is used to convert the list to a string.

# x = ['python', 'is', 'a', 'scripting', 'lang']
# a = " ".join(x)
# print(a)
# print(type(a))


# STRIP: It is used to delete the extra space from starting and ending of the text.

# x = "          data science        "
# a = x.strip()
# print(x)
# print(a)



# format: It is used to fill the values according to the position.
# startswith: It is used the check the first character of the text starts with a particular character or not.
# endswith: It is used the check the last character of the text ends with a particular character or not.
# isupper: It is used to check whether or not the text is in upper case. 
# islower: It is used to check whether or not the text is in lower case.
# isdigit:
# isdecimal
# isalpha()
# isalnum()
# isspace()
# istitle()




# format

# x = ("Hello {}")
# y = x.format("Good Morning")
# print(y)


# x = "Hello, {}. My name is {} and i am {} years old."

# y = x.format("good morning","Harsh", 23)
# print(y)



# startswith

# x = "rohit sharma"

# y = x.startswith("r")
# print(y)


# endswith

# a = str(input("enter your name: "))

# b = a.endswith("h")
# print(b)


# Check whether name ends with r or a, if yes then print name else not found.

# x = input("Enter your name: ")

# if x.endswith("r") or x.endswith("a"):
# 	print(x)
# else:
# 	print("Not Found")



# isupper

# x = input("Enter your name: ").upper()

# if x.isupper():
# 	print("yes")



# islower

# x = (input("Enter your name: ")).lower()

# if x.islower():
# 	print("Yes")
# else:
# 	print("No")



# isdigit

# x = input("Enter digit: ")

# if x.isdigit():
# 	print("Yes")
# else:
# 	print("No")



# isdecimal

# x = input("Enter number: ")

# if x.isdecimal():
# 	print("yes")



# isalpha()

# x = input("Enter text: ")
# if x.isalpha():
# 	print("Yes")



# isalnum()

# x = input("Enter text: ")
# if x.isalnum():
# 	print("Yes")



# isspace()
# x = input("Enter text: ")
# if x.isspace():
# 	print("Yes")

# istitle()

# x = input("Enter text: ")
# if x.istitle():
# 	print("Yes")
# else:
# 	print("No")




# Capitalize the first and last letter to capital.

# x = "india"

# x = x.title()

# y = x[0:-1]
# z = x[-1].upper()
# print(y+z)

#   OR 

# y = x[0].upper()
# z = x[4].upper()
# print(y+x[1:4]+z)



	

# reverse the string
# print first and last aplphabet from the text
# count total i
# count length without i

# x = "brillica"
#   1.   print(x[-1::-1])

#   2.    print(x[0]+x[-1])

#   3.   y = x.count("i")
# 		 print(f"total number of i: {y}")

#   4.  y = x.replace("i","")
#		print(len(y))




# Reverse the text
# x = "python is an object oriented programming language"
# x = x.split()
# y = x[-1::-1]
# print(y)

# y = " ".join(y)
# print(y)

# o = x.count(" ")
# print(o)





# 1.  write a code to check if the text is capital or not.

# x = input("Enter your name: ")
# print(x.isupper())




# 2.  write a code to check if the name is capital print yes else no.

# x = input("Enter any: ")
# y = x[0]
# if y.isupper():
# 	print("Yes")
# else:
# 	print("No")



# 3. print the first 3 letter in capital if length is greater than 5.
# x = input("Enter your name: ")
# if len(x)>5:
# 	print(x[0:3].upper())



# 4. print the data type of text or number
#    if input is digit then print number
#    if input is space then print space
#	 if input is text then print text
# 	 if input is special char then print special character
# 	 Else print None


# x = str(input("Enter text: "))

# if x.isdigit():
# 	print("Number",x)

# elif x.isspace():
# 	print("Space",x)

# elif x.isalpha():
# 	print("Text",x)

# elif x.isalnum():
# 	print("Text or number or both",x)

# else:
# 	print("Special Char",x)












