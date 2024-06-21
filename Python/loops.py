# Iterator = The variable in which we store the value.
# Iteration = The process of checking the condition repeatedly is called iteration.
# Initialization: It refers to the starting position of the loop.
# Linear search: The process of searching through a value one by one in a line.



# LOOP : Loops are used for sequential traversal. For traversing list, string, tuples etc.


#  WHILE LOOP


# print numbers 1 to 5
# i = 1
# while i<= 5:
# 	print("YES", i)
# 	i += 1 


# print number reverse 10 to 1
# i = 10
# while i>=1:
# 	print("Yes", i)
# 	i -=1


# print 1 to 100
# x = 1
# while x <=100:
# 	print(x)
# 	x +=1


# print 100 to 1
# x = 100
# while x>=1:
# 	print(x)
# 	x -= 1



# Create a multiplication table
# x = int(input("Enter number: "))
# y = 1
# while y <= 10:
# 	print(f"{x}x{y} = ",x*y)
# 	y += 1


# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# while i < len(num):
# 	print(num[i])
# 	i += 1


# hero = ["ironman", "batman", "spider-man", "flash"]
# idx = 0
# while idx < len(hero):
# 	print(hero[idx])
# 	idx += 1



# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 49

# while i < len(num):
# 	if num[i]==x:
# 		print(f"found at {x}")
# 	else:
# 		print("finding..")
# 	i+=1



# -------------- BREAK ---------------
# Break : It is used to terminate the loop when encountered.


# x = 1
# while x <= 5:
# 	print(x)
# 	if x==3:
# 		break
# 	x += 1
# print("Loop ended")



# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)


# num = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i = 0
# x = 49

# while i < len(num):
# 	if num[i]==x:
# 		print(f"Found at {x}")
# 		break
# 	else:
# 		print("finding")
# 	i+=1
# print("loop ended")




# --------- CONTINUE -------------
# Continue : It terminates execution in the current iteration & continues execution of the loop with the next iteration.


# Print numbers 1 to 10 exclude 4

# x = 1
# while x <= 10:
# 	if x==4:
# 		x+=1
# 		continue
# 	print(x)
# 	x+=1



# Print all even numbers

# x = 1
# while x <= 10:
# 	if x%2!=0:
# 		x+=1
# 		continue
# 	print(x)
# 	x+=1


# Print all odd numbers

# x = 1
# while x<=10:
# 	if x%2==0:
# 		x+=1
# 		continue
# 	print(x)
# 	x+=1





#-------------------    FOR LOOP    -------------------


# Print the word reservoir except o

# string = "reservoir"
# for x in string:
# 	if x=="o":
# 		print("o found")
# 		break
# 	print(x)



# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# abc = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for x in abc:
# 	print(x)


# Search for number x in list
# abc = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 16]
# x = 16
# idx = 0

# for y in abc:
# 	if y==x:
# 		print("num found at idx", idx)
# 		break
# 	idx+=1
	



# --------------------    RANGE    -----------------------
# RANGE : Range functions returns a sequence of numbers, starting from O by default, and increments by 1 (by default), and stops before a specified number.
# range(start, stop, step)

# for x in range(10):
# 	print(x)


# for x in range(0,5):
# 	print(x)

# for x in range (2, 10, 2):
# 	print(x)




# Print numbers from 1 to 100.

# for x in range(1,101):
# 	print(x)



# Print numbers from 100 to 1.
# for x in range(100,0,-1):
# 	print(x)



# Print the multiplication table of a number n.

# x = int(input("Enter number: "))
# for i in range(1, 11):
# 	print(f"{x}x{i}= ",x*i)




# --------------   PASS STATEMENT   -------------

# Pass: pass is a null statement that does nothing. It is used as a placeholder for future code.

# for x in element:
# 	pass



# -----------------------------------------------------------------------------------
# find the sum of first n numbers. (using while)

# USING WHILE LOOP

# n = 8
# sum = 0
# i = 1

# while i<=n:
# 	sum+=i
# 	i+=1
# print(sum)



# USING FOR LOOP

# n = int(input("Enter number: "))
# sum = 0

# for i in range(1,n+1):
# 	sum+=i
# print(f"Total sum: {sum}")



# find the factorial of first n numbers.
# WHILE LOOP
# n = 4
# fact = 1
# i = 1 
# while i<=n:
# 	fact*= i
# 	i+=1
# print(fact)


# FOR LOOP
# n = int(input("Enter number: "))
# fact = 1

# for i in range (1,n+1):
# 	fact*=i
# print(f"Factorial: {fact}")







# print name 10 times

# x = 10
# y = 1

# while y<=x:
# 	print("Harsh, ",y)
# 	y+=1


# print counting from 1 to 50
# x = 1
# y = 51
# while x<y:	
# 	print(x)
# 	x+=1	



# print counting from 10 to 40

# x = 10
# y = 41
# while x<y:
# 	print(x)
# 	x+=1



# print backward counting from 30 to 1

# x = 30
# y = 1

# while x>=y:
# 	print(x)
# 	x-=1




# print counting with the help of user input 
# x = int(input("Enter nnumber: "))
# y = 1
# while x>=y:
# 	print(y)
# 	y+=1



# print table of 5

# x = 5
# i = 1
# while i<=10:
# 	print(f"{x}x{i} ={x*i}")
# 	i+=1


# print table of x number
# x = int(input("enter number: "))
# print("-"*20)
# y = 1
# while y<11:
# 	print(f"{x}x{y}={x*y}")
# 	y+=1




# print hello world 15 times

# x = 15
# y = 1
# while x>=y:
# 	print("Hello World!", y)
# 	y+=1



# counting from 40 to 50

# x = 40
# y = 50

# while x<=y:
# 	print(x)
# 	x+=1



# print counting from to 60 to 40

# x = 60
# y = 40

# while x>=y:
# 	print(x)
# 	x-=1




# create multiplication table


# x = int(input("enter number: "))
# i = 1
# while i<=10:
# 	print(f"{x}x{i}={x*i}")
# 	i+=1



# 1 to 20 even number
# x = 1
# y = 20

# while x<=y:
# 	if x%2==0:
# 		print("Even,",x)
# 	x+=1



# print odd numbers 1 to 30

# x = 1
# y = 30
# while x<=y:
# 	if x%2!=0:
# 		print("Odd,", x)
# 	x+=1




# print all number from 58 to 89 who is divisible of 7

# x = 58
# y = 89

# while x<=y:
# 	if x%7==0:
# 		print(f"{x} is Divisible by 7")
# 	x+=1




# print all number from 1 to 100 which is divisible by 5 and 8

# x = 1
# y = 100

# while x<=100:
# 	if x%5==0 and x%8==0:
# 		print(f"{x} is divisible of 5 and 8")
# 	x+=1




# print numbers from 100 to 200 which is divisible by 10 or 5.

# x = 100
# while x<=200:
# 	if x%10==0 or x%5==0:
# 		print(f"{x} is divisible by 5 or 10")
# 	x+=1



# print square value from 1 to 10

# x = 1
# while x<=10:
# 	print(f"{x}x{x}={x*x}")
# 	x+=1



# print even number from 340 to 300

# x = 340
# y = 300

# while x>=y:
# 	if x%2==0:
# 		print(f"Even: {x}")
# 	x-=1



# ----------------------------------------------------------------------

# 1. find the sum of first 10 number 1 to 10

# x = 1
# y = 0

# while x<=10:
# 	y+=x
# 	x+=1
# 	print(y)


# 2. Find the average of first 5 number

# x = 5
# y = 1
# s = 0
# while x>=y:
# 	s+=y
# 	y+=1
# print(f"Avg of first 5 no: {s/x}")





# 3. Count total Number of even Number from 1 to 25


# x = 1
# y = 0

# while x<=25:
# 	if x%2==0:
# 		y+=1
# 	x+=1
# print(f"Total even no: {y}")



# 4. Count total Number of odd Number from 20 to 36.

# x = 20
# y = 0 

# while x<=36:
# 	if x%2!=0:
# 		y+=1
# 	x+=1
# print("total odd: ", y)



# 5. Count total number who is divisible of 7 from 1 to 80.

# x = 1
# y = 0

# while x<=80:
# 	if x%7==0:
# 		y+=1
# 	x+=1
# print(y)




# --------------------------------------------------------------------------------

# BREAK : Break statement are used to Break the loop according to condition.

# CONTINUE: It is used to skip the number of text according to condition.



# Break list when 5 is found.



# x = 10
# y = 1

# while x>=y:
# 	if y==5:
# 		break
# 	else:
# 		print(y)
# 	y+=1



# Print 1 to 10 and skip 3 , 7


# x = 10
# y = 0

# while x>y:
# 	y+=1
# 	if y==3 or y==7:	
# 		continue
# 	else:
# 		print(y)


# ------   OR   ---------

# x = 10
# y = 0

# while x>y:
# 	y+=1
# 	if y==3 or y==7:
# 		continue
# 	print(y)




# print 50 to 80 and skip 60 to 70

# x = 49
# y = 80

# while x<y:
# 	x+=1
# 	if x>=60 and x<=70:
# 		continue
# 	else:
# 		print(x)






# ----------------------    FOR LOOP     ---------------------------------

# FOR LOOP : it is used to run set of statement.
#  			OR
#			it is used to iterate the block of code.

# for variable in range():
# 	print(variable)

# RANGE - (start, end, step)

# 1 to 20
# x = range(21)
# for i in x:
# 	print(i)

# ----- OR ------
# for x in range(1,21):
# 	print(x)



# print number from to 100 to 140

# x = range(100,141)
# for i in x:
# 	print(i)



# print backward Counting from 20 to 10
# x = range(20,9,-1)
# for i in x:
# 	print(i)



# print all even number from 1 to 15

# for x in range(1,16):
# 	if x%2==0:
# 		print(x)



# print all odd number from 25 to 40.

# s = 0
# for x in range(25, 41):
# 	if x%2!=0:
# 		s+=1
# 	x+=1
# print(s)



# print leap year from 1947 to 2024

# for i in range(1947,2025):
# 	if i%4==0:
# 		print(i)


# print number 10 to 80 with 5 step size
# for i in range(10,81,5):
# 	print(i)


# Factorial
# s= 1

# for i in range(1,6):
# 	s*=i
# print(s)


# Count odd numbers from 1 to 15
# s = 0
# for i in range(1,16):
# 	if i%2!=0:
# 		s+=1
# print(f"Total Odd numbers: {s}")



# Write program to print the number from 100 to 50 who is divisibly by 3 or 7 and number should be even.

# for i in range(100,49,-1):
# 	if (i%3==0 or i%7==0) and i%2==0:
# 		print(i)

# OR 

# for i in range(100,49,-1):
# 	if i%3==0 or i%7==0:
# 		if i%2==0:
# 			print(i)





# ----------   FOR LOOP - TEXT   -------------------

# for i in range(10):
# 	print("Hello World!",i)


# Print only capital 
# x = "PriNce"
# for i in x:
# 	if i.isupper():
# 		print(i)



# Print text with seconds delay
# import time
# x = "PrinCe"

# for i in x:
# 	print(i)
# 	time.sleep(1)




# Print name using range 

# USING FOR LOOP

# x = "Prince sharma"

# y = len(x)
# for i in range(y):
# 	print(x[i])



# USING WHILE LOOP

# x = "Prince"
# y = 0
# while y<len(x):
# 	print(x[y])
# 	y+=1



# Print name using loop
# While loop
# x = "Harsh"
# l = 0

# while l<len(x):
# 	print(x[l])
# 	l+=1 
	
# For loop
# x = "Harsh"
# l = len(x)
# for i in range(l):
# 	print(x[i])




# print number from 20 to 40 and break at 30

# x = 40
# y = 20
# while x>=y:
# 	if y==30:
# 		break
# 	y+=1
# 	print(y)

# for i in range(20,40):
# 	print(i)
# 	if i==30:
# 		break


	

# print 1 to 30 but print number horizantally

# for i in range(1,31):
# 	print(i,end=", ")



# Show index number of each letter from the text.

# x = "Rohit Sharma"

# for i in range(len(x)):
# 	print(f"{x[i]}, index number: {i}")


# Show index number of each letter from the text in negative index 

# x = "rohit sharma"
# y = len(x)

# for i in range(y):
# 	print(x[i], i-y)
	

# x = "harsh"
# y = len(x)
# z = 0
# while y>z:
#  	print(x[z], z-y)
#  	z+=1



# extract all numbers
# extract all letters

# x = "programming123"
# y = ""
# for i in x:
# 	if i.isalpha():	
# 		y+=i
# print(y)


# Count all the digits
# x = "pr3o5gra6mm4ing123"
# y = 0

# for i in x:
# 	if i.isdigit():
# 		y+=1
		
# print(f"Count of digits: {y}")








# 1.  print the hello world 10 times with the help of While loop
# x = 1
# while x<=10:
# 	print("Hello World!")
# 	x+=1


# 2.  find the all Number from 50 to 100 that is divisibe of 7 and 9. 
# for i in range(50,101):
# 	if i%7==0 and i%9==0:
# 		print(f"Number divisible by 7 and 9: {i}")


# 3.  Count the all Number form 30 to 80 that is divisible of 6 and 8
# a=0
# for i in range(30, 81):
# 	if i%6==0 and i%8==0:
# 		a+=1
# print(f"Count of numbers divisible by 6 and 8: {a}")



# 4.  Write a python program to count the all even Number from 20 to 40.
# a = 0
# for i in range(20,41):
# 	if i%2==0:
# 		a+=1
# print(f"Count of even numbers 20 t0 40: {a}")



# 5.  Write a python program to sum the total value from 10 to 20 ?
# x = 0
# for i in range(10,21):
# 	x+=i
# print(f"Sum of numbers 10 till 20: {x}")


# 6.  write a python program to count the all even and Odd Number from 10 ot 35
# x = 0 
# for i in range(10,36):
# 	if i%2!=0:
# 		x+=1
# print(f"Total odd num from 10 to 35: {x}")


# 7.  write a python Program to show the factorial of Any number according to the help of user input
# x = int(input("Enter a number: "))
# y = 1
# for i in range(1,x+1):
# 	y*=i
# 	print(i,y)


# 8.  find the Average of the first 10 Number with the help of while loop
# x = 0
# y = 0
# while x<10:
# 	x+=1
# 	y+=x	
# print(f"Average of first 10 num: {y/x}")
	


# 9.  Reverse the Number from 80 to 50 with help of for  and while Loop
# FOR
# for i in range(80,49,-1):
# 	print(i)

# WHILE
# x = 80
# while x>=50:
# 	print(x)
# 	x-=1


# 10. print your name of alphabet with the help of while loop
# x = "Harsh"
# y = 0
# while len(x)>y:
# 	print(x[y])
# 	y+=1


# 11. print the reverse name with the help of while loop.
# x = "Harsh"
# y = 1
# while len(x)>=y:
# 	y+=1
# print(x[y::-1])



# 12. write a python program to show the square root from 1 to 15

# x = 0
# for i in range(1,16):
# 	x += 1
# 	print(f"Square of {x}: {i**2}")


# 13. wrtie a python program to show the number between 100 to 150 that is divisible of 5 and 9 and 3
# x = 100
# y = 150
# while x<=y:
# 	if x%3==0 and x%5==0 and x%9==0:
# 		print(x)
# 	x+=1



# x = [12,45,7,9,56,23,25,45,78,89,56,23,25,24,26]

# print the NUmebr that is divisible bt 9
# for i in x:
# 	if i%9==0:
# 		print(i)


# find the number who is repeated more than one time

# for i in x:
# 	if x.count(i)>1:
# 		print(i)



# show positive and negative index of the Number
# Positive
# a = 0
# for i in x:
# 	print(f"Index of {i}: {a}")
# 	a+=1

# Negative

# a = len(x)
# for i in range(a):
# 	print(x[i], i-a)
	

# show the index Number of the even number elements
# a = 0
# for i in x:
# 	if x[a]%2==0:
# 		print(a)
# 	a+=1


# y = 0
# while y<len(x):
# 	if x[y]%2==0:
# 		print(y)
# 	y+=1



# show the Negative index of odd Elements

# a = 0 
# b = len(x)
# for i in x:
# 	if x[a]%2!=0:
# 		print(a-b)
# 	a+=1	
	

# factorial
# x = int(input("enter number: "))
# f = 1
# y = 1
# while x>=y:
# 	f*=y
# 	y+=1
# print("Factorial: ", f)


# x = int(input("enter number: "))
# f = 1
# for i in range(1, x+1):
# 	f*=i
# print(f"Factorial of {x}: {f}")



# REVERSE

# x = "brillica"
# y = len(x)
# while y>0:
# 	y-=1
# print(x[::-1])

# OR 

# x = "brillica"
# y = len(x)-1
# while y>=0:
# 	print(x[y], end="")
# 	y-=1

# OR 

# x = "brillica"
# y = len(x)-1
# for i in range(y, -1, -1):
# 	print(x[i])



# x = "harshmahar10@gmail.com"

# y = ""

# for i in x:
# 	if i.isalpha():
# 		y+=i
# print(f"Alphabet: {y}")
# print(f"Count of alphabet: {len(y)}")


# Special Char
# x = "harshmahar10@gmail.com"
# for i in x:
# 	if i.isalnum():
# 		continue
# 	print(f"Special char: {i}")


# Print text before g  
# x = "harshmahar10@gmail.com"
# for i in x:
# 	if i.isalpha():
# 		if i=="g":
# 			break
# 		print(i, end="")



# PRINT TOTAL NUMBER OF A

# x = "ramayana"
# y = 0
# for i in x:
# 	if i=="a":
# 		y+=1
# print(f"Total A: {y}")



# PRINT A AND R

# x = "ramayana"
# for i in x:
# 	if i=="a" or i=="r":
# 		print(i)


# PRINT ALL A FROM TEXT

# for i in x:
# 	if i=="a":
# 		print(i)



# Print repeated text.
# x = "programming"
# for i in x:
# 	if x.count(i)>1:
# 		print(i)



# print all index of even 
# x = "programming"
# y = len(x)
# for i in range(0, y):
# 	if i%2==0:
# 		print(x[i], i)



# x = "PrinceKR"
# for i in x:
# 	if i.isupper():
# 		print(i)



# x = "pr3o5gra6mm4ing123"
# y = 0
# for i in x:
# 	if i.isdigit():
# 		y+=1
# print(y)



# find the sum of numbers
# x = "p34ert345j4j34534j"
# a = 0
# for i in x:
# 	if i.isdigit():
# 		a += int(i)
# print(a)


# Store the number and text in A and B variable.
# x = "p34ert345j4j34534j"
# a = ""
# b = ""

# for i in x:
# 	if i.isalpha():
# 		a+=i
# 	elif i.isdigit():
# 		b+=i
# print(a)
# print(b)






# --------------------------------------------------------------------------------

#		LIST

# ---------------------------------------------------------------------------------------

# LIST = List is used to store multiple values in a single variable. It is always written in square brackets.


# Main uses of LIST
# 1. Lists are written in square brackets..
# 2. Lists are ordered.
# 3. Lists are changable or mutable.
# 4. Lists are indexed
# 5. List allow duplicate values.
# 6. Multiple type of data can be stored.



# Storing values of multiple data type. 
# x = [100, "Friday", 78.23, 45j, True, None, 200, 855]
# print(f"List: {x}")
# print(f"Data Type: {type(x)}")
# print(f"Length : {len(x)}")



# Storing the duplicate values
# x = [45,45,45,45,444,444,4,4,4,45]
# print(x)



# List Manipulation

# 1. Pop -   
# It is used to delete the values from list with the help of indexing. It deletes the last value by default.
# x.pop() - Deletes the last value.
# x.pop(2) - Deletes the value at 2nd index. 

# x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# x.pop(2)
# print(x)


# 2. Remove -   
# It is used to delete a specific value.
# x.remove(value)

# x = [12, 43, 123, 12, 34, 532, 12]
# x.remove(12)
# print(x)


# 3. Clear -   
# It deletes all the values from the list.

# x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# x.clear()
# print(x)


# 4. Del
# Del is used to delete the variable or a value according to index.

# del  -  keyword

# x = [45,78,89,56,23,23]

# del x[-1]    Indexing
# del x[0:3]   Slicing
# del x        Deletes the variable  
# print(x)





# x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# 1. Delete Sunday from list
# Pop
# x.pop(0)
# print(x)

# Remove
# x.remove("Sunday")
# print(x)

# Delete
# del x[0]
# print(x)






# x = [12,45,78,"fri",89,8,"thu",56,62,3,32,"sun"]

# Delete last value with pop
# x.pop()
# print(x)

# Delete fri with remove
# x.remove("fri")
# print(x)

# delete first three elements
# del x[0:3]
# print(x)

# delete all values from list
# x.clear()
# print(x)

# delete variable of list
# del x



# ----------------------------------------------------------------------
#     HOW TO ADD THE VALUE IN A LIST
# -----------------------------------------------------------------------

# 1. Insert - It is used to add the value according to index number

# x = [12,45,78,89,23,23]
# x.insert(0, "harsh")
# print(x)


# 2. Append - It is used to add the value in the end of a list. 

# x = [12,45,78,89,23,23]
# x.append("harsh")
# print(x)

# 3. Extend - It is used to add multiple values in the end of a list.

# x = [1,2,3]
# y = [4,5,6]
# x.extend(y)
# print(x)

# x = [1,2,4,5,6]
# print(x.extend("harsh"))



# Create a new list and all value of x and convert in capital letter
# x = ["virat", "rohit", "anikul", "rakesh"]
# y = []

# for i in x:
# 	i = i.upper()
# 	y.append(i)
# print(y)


# 1. delete third value
# 2. add 200 in 2nd index
# 3. add 500 in last of list
# 4. delete 4th and 5th position value.
# 5. add [1,1,1] in list
# 6. add "python" in last
# 7. delete 89 from list
# 8. delete all value from list
# 9. show length of list
# 10. show data type of x


# x = [45,78,89,56,12,25,36,75,34]

# 1.
# x.pop(2)
# print(x)

# 2.
# x.insert(2, 200)
# print(x)

# 3.
# x.append(500)
# print(x)

# 4. 
# x.pop(5)
# x.pop(6)
# print(x)

# 5. 
# y = [1,1,1]
# x.extend(y)
# print(x)


# 6.
# x.append("python")
# print(x)


# 7. 
# x.remove(89)
# print(x)


# 8.
# x.clear()
# print(x)


# 9. 
# print(len(x))



# 10.
# print(type(x))






# 1. Create a list with the help of user input
# x = input("Enter : ")

# for i in range(len(x)):
# 	y = x.split()
# print(y)



# 2. Write a python program to delete the first and last value form the list
# x = [45,78,89,56,23,1,2,45]

# x.pop() and x.pop(0)
# print(x)


# 3. Repeat welcome 29 times in horizontally
# x = 29
# y =0
# while x>=0:
# 	y+=1
# 	x-=1
# 	print(x+y, end=" ")



# 4. Extract value with the help of indexing and slicing
# x = [12,45,78,89,56,23,1,100,"Prince","priyanshu",21j,True]

# 1. ["prince","priyanshu"] with the help of Negative slicing
# print(x[-4:-2])


# 2. [78,89,56]  Negative and positive slicing
# print(x[2:5])  #  Positive
# print(x[-10:-7])  # Negative


# 3. extract boolen value
# print(x[-1])

# 4. delete "priyanshu" from list
# x.remove("priyanshu")
# print(x)


# 5. Add "python" in 5th index
# x.insert(5, "python")
# print(x)

# 6. add 100 to 105 in last of list
# x = [12,45,78,89,56,23,1,100,"Prince","priyanshu",21j,True]
# y = [100,101,102,103,104,105]
# x.extend(y)
# print(x)


# 7. remove the first value from the list
# x.pop(0)
# print(x)


# 8. Delete the "prince" with help of del and pop function
# x.pop(-4)
# del x[-4]
# print(x)


# 5. write a python program to show the age in year base of Date of Birth
# x = input("Enter DOB: ")
# print(x[-4:])


# 6. add all number in a blank list
# x = "prince124sharma#$"

# y = []
# for i in x:
# 	if i.isdigit():
# 		y+=i
# print("".join(y))




# 7. Reverse this text with the helo of the for loop
# x = "prince124sharma#$"
# for i in range(len(x),0,-1):
# 	y = x[-1::-1]
# print(y, end="")



# 8. Extract and reverse all number only with the help of loop
# x = "prince124sharma#$"
# y = ""
# for i in x:
# 	if i.isdigit():
# 		y+=i
# print(y[-1::-1])


# 9. print all special charactor
# for i in x:
# 	if i.isalnum():
# 		continue		
# 	print(i)



# 10. print all unique alphabet from the x wih the help of loop
# c = "himachal pradesh"
# for i in c:
# 	if c.count(i)>1:
# 		continue
# 	print(i)




# print the one by one one alphabet with the help of while loop
# x = "prince sharma"
# y = 0
# while len(x)>y:
# 	print(x[y])
# 	y+=1
















# 1. Create a list with the help of user input
# 2. Write a python program to delete the first and last value form the list
# x = [45,78,89,56,23,1,2,45]

# x.pop() and x.pop(0)
# print(x)





# 3. Repeat welcome 29 times in horizontally

# for i in range(1,30):
# 	print("Welcome", i)




# 4. Extract value with the help of indexing and slicing
# x = [12,45,78,89,56,23,1,100,"Prince","priyanshu",21j,True]

# 1. ["prince","priyanshu"] with the help of Negative slicing

# print(x[-4:-2])


# 2. [78,89,56]  Negative and positive slicing
# print(x[2:5])
# print(x[-10:-7])



# 3. extract boolen value
# x = [12,45,78,89,56,23,1,100,"Prince","priyanshu",21j,True]
# print(x[-1])


# 4. delete "priyanshu" from list
# x.pop(-3)
# x.pop(x.index("priyanshu"))
# x.remove("priyanshu")
# del x[-3]
# print(x)


# 5. Add "python" in 5th index
# x.insert(5, "python")
# print(x)

# 6. add 100 to 105 in last of list
# y = [100,101,102,103,104,105]
# x.extend(y)
# print(x)

# 7. remove the first value from the list
# x.pop(0)
# print(x)

# 8. Delete the "prince" with help of del and pop function



# 5. write a python program to show the age in year base of Date of Birth


# x = "prince124sharma#$"
# 6. add all number in a blank list
# y = []
# for i in x:
# 	if i.isdigit():
# 		y+=i
# print("".join(y))

# 7. Reverse this text with the helo of the for loop
# for i in x:
# 	y = x[::-1]
# print(y)

# 8. Extract and reverse all number only with the help of loop
# 9. print all special charactor

# c = "himachal peadesh"
# 10. print all unique alphabet from the x wih the help of loop


# x = "prince sharma"

# print the one by one one alphabet with the help of while loop.
# for i in x:
	# print(i)




# x = [45,78,89,56,253,23]

# print(x[::-1])

# 1. 253
# print(x[-2])

# 2. 45,78
# print(x[0:2])

# 3. 23,253
# print(x[-1:-3:-1])

# 4. 89,78,45
# print(x[2::-1])

# 5. 56, 89
# print(x[-3:-5:-1])



#----------------------------------------------------------------
# List Methods:
# Python has a set of built-in methods that you can use on lists.

# Method Description
# append()           =  Adds an element at the end of the list.	
# clear()			 =  Deletes all values in a list.	
# copy()			 =  It is used to create a duplicate copy of the list.
# count()			 =  Counts the number of values in a list.
# extend()			 =  Adds multiple values at the end of the list.
# index()			 =  Shows the index number of a value in the list.	
# insert()   		 =  Adds a value at the specified index number.
# pop()				 =  Deletes a value based on the specified index number from the list.
# remove() 			 =  Removes a specific value from the list.
# reverse()  		 =  Reverses the list.
# sort()			 =  Sorts the list in ascending.
# sort(reverse=True) =  Sorts the list in descending order.


# sort() :    It is used to arrange the data in ascending or descending order. 
			# It changes the original data.
			# Variable is not required.
			# Sort is faster

# sorted():   It is used to arrange the data in ascending or descending order. It doesn't change the original data.
			# It does not changes the original data.
			# Variable is required.
			# Sorted is slower comparatively to sort.


# max(): It extracts the maximum value from the list.

# min(): It extracts the minimum value from the list.


# Sort

# Ascending order
# x = [45,78,89,56,253,23]
# x.sort()
# print(x)

# Descending order
# x = [45,78,89,56,253,23]
# x.sort(reverse=True)
# print(x)


# Sorted

# Ascending order
# x = [45,78,89,56,253,23]
# y = sorted(x)
# print(y)

# Desceding order
# y = sorted(x, reverse=True)
# print(y)



# x = [45,78,89,56,253,23]
# y = sorted(x)
# print(y)
# print(x)


# x = [45,89,56,25,41,10,96,35,78]

# arrange the data ascending order in
# x.sort()
# print(x)


# extract the maximum value from the list
# x.sort()
# print(x[-1])

# extract the minimum value from the list
# x.sort()
# print(x[0])

# second highest value
# x.sort()
# print(x[-2])

# second lowest value
# x.sort()
# print(x[1])

# top 3 number from list
# x.sort()
# print(x[-1:-4:-1])

# bottom 3 number from list
# x.sort(reverse=True)
# print(x[-1:-4:-1])


# Sort text
# x = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# x.sort(reverse=True)
# print(x)



# Reverse: It is used to reverse the list.
# x = [12,85,20,100]
# x.reverse()
# print(x)



# Count : It is used to count the values from the list.

# Count number of 12
# x = [12,45,54,76,12,543,76,45]
# print(x.count(12))


# Index : It shows the index number of any value in the list.
# x = [12,45,54,76,12,543,76,45]
# print(x.index(54))


# MAX : It extracts the maximum value from the list 
# x = [45,89,56,25,41,10,96,35,78]
# print(max(x))


# MIN: It extracts the minimum value from the list
# x = [45,89,56,25,41,10,96,35,78]
# print(min(x))



# Copy: It is used to create a duplicate copy of the list.

# x = [12,45,78,89,23]
# y = x.copy()
# x.clear()
# print(y)
# print(x)



x = [12,45,78,89,65,23,10]
# 1. Extract all even values.
# for i in x:
# 	if i%2==0:
# 		print(i)


# 2. Extract all odd number.
# for i in x:
# 	if i%2!=0:
# 		print(i)


# 3. Create a blank list and all even number from x.
# y = []
# for i in x:
# 	if i%2==0:
# 		y.append(i)
# print(y)


# 4. Create a blank list and all odd number from x.
# y = []
# z = []
# for i in x:
# 	if i%2==0:
# 		y.append(i)
# 	elif i%2!=0:
# 		z.append(i)	
# print(f"Even: {y}")
# print(f"Odd: {z}")



x = [12,45,78,12,12,12]

# 1. delete all 12.

# while 12 in x:
# 	x.remove(12)
# print(x)


# 2. Delete even numbers.


# 3. Delete odd numbers.







# ------------------------------------------------------------------------------

# NESTED LIST - When one list is used inside an another list, it is called nested list.

# x = [12,45,78,[1,2,3],100,200]
# print(len(x))


# x = [[1,2,3],[4,5,6], [7,8,9]]
# print(len(x))



# x = [[1,2,3],[4,5,6], [7,8,9]]

# index
# print(x[0][1])  # 2
# print(x[0][0])	# 1
# print(x[1][1])	# 5
# print(x[2][-1])	# 9
# print(x[2][0])	# 7
# print(x[2][1])	# 8



# x = [[12,45,78, [100,200,300]]]


# print(x[0][3][2])		# 300
# print(x[0][3][1]) 	# 200
# print(x[0][2])		# 78
# print(x[0][0])		# 12
# print(x[0][1])		# 45














