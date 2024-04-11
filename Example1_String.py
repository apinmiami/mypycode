# Continue from Example_string.py
# 1. Deleting/Updating from a string
# Examples :-

# str1 = "Hello I'm Geek"
# print("Intial String")
# print(str1)
#
# # Updating a character of a string
# # As python strings are immutable, they dont support item updating directly
# ### These are following two ways
# # ONE WAY
# list1=list(str1) # type casting to list data type
# list1[2] = "p"
# # print(list1)
# str2="".join(list1)
# print("\nUpdating character at 2nd index: ")
# print(str2)
#
# # second Way
#
# str3=str1[0:2]+'p'+str1[3:]
# print(str3)

# UPDATING ENTIRE STRING
# In Python Programming, As Python strings are immutable in nature, we cannot
# update the existing string. We can only assign a completely
# new value to the variable with the same name.
# Example:-
# str1 = "Hello I'm Geek"
# print("Initial String")
# print(str1)
#
# # Now updating string
# str1="Welcome to the greek world"
# print("\nUpdated string: ")
# print(str1)

# DELETING A CHARACTER
# Python strings are immutable, that means we cannot delete a character from it.
# When we try to delete thecharacter using the del keyword,
# it will generate an error.
# Example
# str1="Hello i'm geek"
# print("intial string: ")
# print(str1)
# print("Deleting charater at 2nd index:")
# del str1[2]
# print(str1) # Will show error (TypeError: 'str' object doesn't support item deletion)

# But using slicing we can remove the character from the original string and store the result in a new string.
# Example
# str1="Hello i'm geek"
# print("intial string: ")
# print(str1)
# # Deleting a character
# str2=str1[0:2] + str1[3:]
#print(str2)
#
##  Deliting entire string
### In Python Programming, Deletion of the entire string is possible
### with the use of del keyword. Further, if we try to print the string,
# this will produce an error because the String is deleted and is unavailable to be printed.

# Escape Sequencing in Python
# Example:-
# str1='''I'm a "geek"'''
# print("\nIntialize string usin triple quotes")
# print(str1)
# # Escaping single quote
# str2='I\'m a "Geek"'
# print("\nEscaping single quote: ")
# print(str2)
# # Escaping double quote
# str3="I'm a \"Geek\""
# print("\nEscaping double quote")
# print(str3)
# # Printing path with the use of escape sequence
# # example:-
# str3="C:\\Python\\Geeks\\"
# print("\nEscaping back slashes: ")
# print(str3)
# # printing path with use of tab
# # example
# str4="Hi\tGeeks"
# print("\nTab: ")
# print(str4)
# ## printing paths with the use of New line
# # Example
# str5="Python\nGeeks"
# print("\nNew Line: ")
# print(str5)

### To ignore the escape sequences in a String, r or R is used,
# this implies that the string is a raw string and escape sequences inside it are to be ignored.
# Example:-
# Printing Hello in octale
str1="\110\145\154\154\157"
print("\nPrinting in octale with the use of escape sequence: ")
print(str1)
# Using raw String to
# ignore Escape Sequences
String1 = r"This is \110\145\154\154\157"
print("\nPrinting Raw String in Octal Format: ")
print(String1)
