# FORMATTING Of String
# Strings in Python or string data type in Python can be formatted with the use of format()
# method which is a very versatile and powerful tool for formatting Strings.
# Format method in String contains curly braces {} as placeholders
# which can hold arguments according to position or keyword
# to specify the order.

# Example
# Default order
# str1="{} {} {}".format('Geeks', 'For', 'Life')
# print("Print string in default order: ")
# print(str1)
#
# # Positional Formating
# str2="{1} {0} {2}".format('Geeks', 'For', 'Life')
# print('\n Printing string in Positional order:')
# print(str2)
#
# # Key word  formating
# str3="{l} {f} {g}".format(g='Geeks', f="for", l='Life')
# print("\nPrint string in order of Keywords: ")
# print(str3)
a='OrbitQuiz'
val=0
for i in a:
    val +=ord(i)
    print(val)

val="QuizOrbit"
val1="quizorbit"
print(len(val))
print(len(val))