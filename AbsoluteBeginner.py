#You are provided with a number check whether its odd or even. 
#Print "Odd" or "Even" for the corresponding cases.

#Note: In case of a decimal, Round off to nearest integer and then find the output. Incase the input is zero, print "Zero".


#Input Description:
#A number is provided as the input.

#Output Description:
#Find out whether the number is odd or even. Print "Odd" or "Even" for the corresponding cases. Note: In case of a decimal, Round off to nearest integer and then find the output. In case the input is zero, print "Zero".

#Sample Input :
#2
#Sample Output :
#Even

a = int(input())
if a==0:
    print('Zero')
elif a%2==0:
    print('Even')
else:
    print('Odd')
    
    
# The area of an equilateral triangle is ¼(√3a2) where "a" represents a side of the triangle. You are provided with the side "a". Find the area of the equilateral triangle.


# Input Description:
# The side of an equilateral triangle is provided as the input.

# Output Description:
# Find the area of the equilateral triangle and print the answer up to 2 decimal places after rounding off.

# Sample Input :
# 20
# Sample Output :
# 173.21

a = int(input())
area = (0.25*1.732050807568877)*(a*a) 
print(round(area,2))

# You are given three numbers A, B & C. Print the largest amongst these three numbers.


# Input Description:
# Three numbers are provided to you.

# Output Description:
# Find and print the largest among the three

# Sample Input :
# 1
# 2
# 3
# Sample Output :
# 3

a = input()
b = input()
c = input()

if a>b and a>c:
  print(a)
elif b>a and b>c:
  print(b)
else:
  print(c)
  
  
# You are provided with a number, "N". Find its factorial.


# Input Description:
# A positive integer is provided as an input.

# Output Description:
# Print the factorial of the integer.

# Sample Input :
# 2
# Sample Output :
# 2

a = int(input())
output = 1
 
for i in range(1, a+1):
    output = output*i

print(output)

# You are given A = Length of a rectangle & B = breadth of a rectangle. Find its area “C”.

# (A and B are natural numbers)


# Input Description:
# The inputs are two natural numbers representing the length and the breadth of a rectangle.

# Output Description:
# Find the area of the rectangle formed by the provided input. Round off the answer to the first decimal place if required.

# Sample Input :
# 2
# 3
# Sample Output :
# 6

l = int(input())
b = int(input())
c = l*b
print(c)

# You are provided with a number "N", Find the Nth term of the series: 1, 4, 9, 16, 25, 36, 49, 64, 81, .......

# (Print "Error" if N = negative value and 0 if N = 0).


# Input Description:
# An integer N is provided to you as the input.

# Output Description:
# Find the Nth term in the provided series.

# Sample Input :
# 18
# Sample Output :
# 324
a = int(input())
c = a*a
print(c)

# you are given with Principle amount($), Interest Rate(%) and Time (years) in that order. Find Simple Interest.

# Print the output up to two decimal places (Round-off if necessary).

# (S.I. = P*T*R/100)


# Input Description:
# Three values are given to you as the input. these values correspond to Principle amount, Interest Rate and Time in that particular order.

# Output Description:
# Find the Simple interest and print it up to two decimal places. Round off if required.

# Sample Input :
# 1000 2 5

p,r,t = input().split( )
si = float(p)*float(r)*float(t)*0.01
print(round(si,2))

# Write a code to get the input and print it 5 times.


# Input Description:
# A single line contains an integer N.

# Output Description:
# Output contains 5 lines with each line having the value N.

# Sample Input :
# 4
# Sample Output :
# 4
# 4
# 4
# 4
# 4

n = input()
for i in range(0,5):
    print(n)
    
# You are given with a number A i.e. the temperature in Celcius. Write a program to convert this into Fahrenheit. 

# Note: In case of decimal values, round-off to two decimal places.


# Input Description:
# A number is provided in Celcius as the input of the program.

# Output Description:
# The output shall be the temperature converted into Fahrenheit corresponding to the input value print up to two decimal places and round off if required.

# Sample Input :
# 12
# Sample Output :
# 53.60

n = input()
faren = float((int(n)*1.8)+32)
print(round(faren,2))

# You are provided with the radius of a circle "A". Find the length of its circumference.

# Note: In case the output is coming in decimal, roundoff to 2nd decimal place. In case the input is a negative number, print "Error".


# Input Description:
# The Radius of a circle is provided as the input of the program.

# Output Description:
# Calculate and print the Circumference of the circle corresponding to the input radius up to two decimal places.

# Sample Input :
# 2
# Sample Output :
# 12.57
A = float(input())

if A > 0:
  C = 2*3.142857142857143*A
  print("%.2f" %C)
else:
  print("Error")
  
# You are given a number A in Kilometers. Convert this into B: Meters and C: Centi-Metres.


# Input Description:
# A number "A" representing some distance in kilometer is provided to you as the input.

# Output Description:
# Convert and print this value in meters and centimeters.

# Sample Input :
# 2
# Sample Output :
# 2000
# 200000

a = int(input())
#Meters
b = a*1000
#Centi meteres
c = a*100000
print(b)
print(c)

# Using the method of looping, write a program to print the table of 9 till N in the format as follows:
# (N is input by the user)

# 9 18 27...

# Print NULL if 0 is input


# Input Description:
# A positive integer is provided as an input.

# Output Description:
# Print the table of nine with single space between the elements till the number that is input.

# Sample Input :
# 3
# Sample Output :
# 9 18 27
num = int(input())
lst=[]
if num==0:
    print('NULL')
for i in range(1,num+1):
  lst.append(i*9)

print(*lst)

# You are given the coefficients of a quadratic equation in order A, B & C.

# Where A is the coefficient of X2,  B is the coefficient of X and C is the constant term in the most simplified form.

# Example: For  X2 + 5X + 6 = 0, you are given the input as: 1 5 6.

# Write a program to find all of the roots of the quadratic.

# Note: The output should be up to 2nd decimal place (round off if needed) and in case of a recurring decimal use braces i.e. for eg: 0.33333..... => 0.33.

# Note: Use Shri Dharacharya's Method to solve i.e. X = {-b + √(b² - 4ac) } / 2a & {-b-√(b² -4ac)} / 2a


# Input Description:
# Three numbers corresponding to the coefficients of x(squared), x and constant are given as an input in that particular order

# Output Description:
# Print the two values of X after rounding off to 2 decimal places if required.

# Sample Input :
# 1 5 6
# Sample Output :
# -2.00
# -3.00

#X = {-b + √(b² - 4ac) } / 2a
#Y = {-b-√(b² -4ac)} / 2a
a,b,c = tuple(map(int,input().split()))

import math as mt
d = mt.sqrt((b*b) - (4*a*c))
x = float((-b + d) / (2*a))
y = float((-b -d) / (2*a))

print('{:.2f}'.format(round(x,2)))
print('{:.2f}'.format(round(y,2)))

# You are given with a number "N", find its cube.


# Input Description:
# A positive integer is provided.

# Output Description:
# Find the cube of the number.

# Sample Input :
# 2
# Sample Output :
# 8
#Cube of a number
n=int(input())
cubeOfNumb = n**3
print(cubeOfNumb)

# Write a code to get an integer N and print the even values from 1 till N in a separate line.


# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the even values from 1 to N in a separate line.

# Sample Input :
# 6
# Sample Output :
# 2
# 4
# 6

#get 'n' value and Print even numbers till 'n'
n= int(input())
for i in range(1,n+1):
    if i%2==0:
        print(i)

# Write a code to get 2 integers A and N. Print the integer A, N times in separate line.


# Input Description:
# First line contains an integer A. Second line contains an Integer N.

# Output Description:
# Print the integer A, N times in a separate line.

# Sample Input :
# 2 3
# Sample Output :
# 2
# 2
# 2
n, m = tuple(map(int,(input().split())))
for i in range(1,m+1):
  print(n)


# You are given Two Numbers, A and B. If C = A + B. Find C.

# Note: Round off the output to a single decimal place.


# Input Description:
# You are provided with two numbers A and B.

# Output Description:
# Find the sum of the two numbers (A + B)

# Sample Input :
# 1
# 1
# Sample Output :
# 2
a=int(input())
b=int(input())
c=a+b
print(c)

# Write a code get an integer number as input and print the sum of the digits.


# Input Description:
# A single line containing an integer.

# Output Description:
# Print the sum of the digits of the integer.

# Sample Input :
# 124
# Sample Output :
# 7

#print sum of a number
n = input()
sum =0
for i in n:
  sum = sum +int(i)

print(sum)


# Print the First 3 multiples of the given number "N". (N is a positive integer)

# Note: print the characters with a single space between them.


# Input Description:
# A positive integer is provided to you as an input.

# Output Description:
# Print the First 3 multiples of the number with single spaces between them as an output.

# Sample Input :
# 2
# Sample Output :
# 2 4 6
#print first 3 multiples of a given n number
n= int(input())
lst = []
for i in range(1,4):
  lst.append(n*i)

print(*lst)

# Write a code to get 2 integers as input and find the HCF of the 2 integer without using recursion or Euclidean algorithm.


# Input Description:
# A single line containing 2 integers separated by space.

# Output Description:
# Print the HCF of the integers.

# Sample Input :
# 2 3
# Sample Output :
# 1

import math as mt
m,n = tuple(map(int,(input()).split()))
print(mt.gcd(m,n))

# Write a code to get an integer N and print the digits of the integer.


# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the digits of the integer in a single line separated by space,

# Sample Input :
# 348
# Sample Output :
# 3 4 8

n = input()
lst = []
for i in n:
  lst.append(i)

print(*lst)

# you will be provided with a number. Print the number of days in the month corresponding to that number.

# Note: In case the input is February, print 28 days. If the Input is not in valid range print "Error".


# Input Description:
# The input is in the form of a number.

# Output Description:
# Find the days in the month corresponding to the input number. Print Error if the input is not in a valid range.

# Sample Input :
# 8
# Sample Output :
# 31

import calendar as cal

m = int(input())
if m>12 or m==0:
    print('Error')
else:
    print(cal.monthrange(2023,m)[1])
    
# You are provided with two numbers. Find and print the smaller number.


# Input Description:
# You are provided with two numbers as input.

# Output Description:
# Print the small number out of the two numbers.

# Sample Input :
# 23 1
# Sample Output :
# 1

m,n = tuple(map(int,input().split()))
if m>n:
    print(n)
elif n>m:
    print(m)
    
# Let "A"  be a string. Remove all the whitespaces and find it's length.


# Input Description:
# A string is provide as an input

# Output Description:
# Remove all the whitespaces and then print the length of the remaining string.

# Sample Input :
# Lorem Ipsum
# Sample Output :
# 10
x = input()
z = x.replace(" ","")
print(len(z))

# Write a program to get a string as input and reverse the string without using temporary variable.


# Input Description:
# A single line containing a string.

# Output Description:
# Print the reversed string.

# Sample Input :
# GUVI
# Sample Output :
# IVUG

z = input()
print(z[::-1])

# Write a code to get an integer N and print values from 1 till N in a separate line.


# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the values from 1 to N in a separate line.

# Sample Input :
# 5
# Sample Output :
# 1
# 2
# 3
# 4
# 5

n = int(input())
for i in range(1,n+1):
    print(i)
    
# Write a code to get an integer N and print the sum of  values from 1 to N.


# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the sum of values from 1 to N.

# Sample Input :
# 10
# Sample Output :
# 55

n = int(input())
sum = 0
for i in range(1,n+1):
    sum+=i    
print(sum)

# Write a code get an integer number as input and print the odd and even digits of the number separately.


# Input Description:
# A single line containing an integer.

# Output Description:
# Print the even and odd integers of the integer in a separate line.

# Sample Input :
# 1234
# Sample Output :
# 2 4
# 1 3

m = input()
oddLst=[]
evenLst=[]

for i in m:
    if int(i)%2==0:
        evenLst.append(i)
    else:
         oddLst.append(i)
evenLst.sort()
oddLst.sort()
print(*evenLst)
print(*oddLst)

Write a code to get an integer N and print the values from N to 1.


# Input Description:
# A single line contains an integer N.

# Output Description:
# Print the values from N to 1 in a separate line.

# Sample Input :
# 10
# Sample Output :
# 10
# 9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1


n = int(input())
lst = []

for i in range(1,n+1):
  lst.append(i)


lst.sort(reverse=True)
for i in lst:
  print(i)
  
# Let "A" be a year, write a program to check whether this year is a leap year or not.

# Print "Y" if its a leap year and "N" if its a common year.


# Input Description:
# A Year is the input in the form of a positive integer.

# Output Description:
# Print "Y" if its a leap year and "N" if its a common year.

# Sample Input :
# 2020
# Sample Output :
# Y
year = int(input())

if year%4==0:
    print('Y')
else:
    print('N')
