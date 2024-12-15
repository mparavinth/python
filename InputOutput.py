# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# To take an integer value

# Output Description:
# Print the integer value

# Sample Input :
# 2
# Sample Output :
# 2

userInput = input()
print(userInput)


# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# A single line contains integers separated by space

# Output Description:
# Print the integer list of integers separated by space

# Sample Input :
# 2 3 4 5 6 7 8
# Sample Output :
# 2 3 4 5 6 7 8

userInput = input()
print(userInput)

# Write a code to get the input in the given format and print the output in the given format.


# Input Description:
# First-line indicates two integers which are the size of array and 'K' value. Second-line indicates an integer contains elements of an array.

# Output Description:
# Print the taken input in the same format.

# Sample Input :
# 5 3
# 1 2 3 4 5
# Sample Output :
# 5 3
# 1 2 3 4 5

userInput = input()
print(userInput)

userInputTwo = input()
print(userInputTwo)

# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# First-line indicates two integers separated by space. Second-line indicates two integers separated by space. Third-line indicates two integers separated by space.

# Output Description:
# Print the input in the same format.

# Sample Input :
# 2 4
# 2 4
# 2 4
# Sample Output :
# 2 4
# 2 4
# 2 4

userInput1 = input()
print(userInput1)

userInput2 = input()
print(userInput2)

userInput3 = input()
print(userInput3)

# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# Three integers are given in line by line.

# Output Description:
# Print the integers in a single line separate by space.

# Sample Input :
# 2
# 4
# 5
# Sample Output :
# 2 4 5

userInput = input()
userInput2 = input()
userInput3 = input()
print(userInput+' '+userInput2+' '+userInput3)

# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# First-line indicates two integers separated by space. Second-line indicates three integers separated by space. Third-line indicates three integers separated by space

# Output Description:
# Print the input in the same format.

# Sample Input :
# 2 5
# 2 5 6
# 2 4 5
# Sample Output :
# 2 5
# 2 5 6
# 2 4 5

a = input()
print(a)

b = input()
print(b)

c = input()
print(c)

# Write a code to get the input in the given format and print the output in the given format


# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by space.

# Sample Input :
# guvi
# Sample Output :
# g u v i


userInput = input()
print(" ".join(userInput))


# Write a code to get the input in the given format and print the output in the given format.


# Input Description:
# A single line contains three float values separated by space.

# Output Description:
# Print the float value separated by line.

# Sample Input :
# 2.3 4.5 7.8
# Sample Output :
# 2.3
# 4.5
# 7.8

userIn = input().split()
for i in userIn:
    print(i)


# Write a code to get the input in the given format and print the output in the given format.


# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by line.

# Sample Input :
# guvigeek
# Sample Output :
# g
# u
# v
# i
# g
# e
# e
# k


userInput = input()
for char in userInput:
    print(char)
    
    
 # Write a code to get the input in the given format and print the output in the given format.


# Input Description:
# A single line contains a string.

# Output Description:
# Print the characters in a string separated by comma.

# Sample Input :
# guvi
# Sample Output :
# g,u,v,i

txt = input()
a = len(txt)

for i in range(a):
    if i != a-1:
        print(txt[i], end=",")
    else:
        print(txt[i])