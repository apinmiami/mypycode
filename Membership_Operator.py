# Example of Membership operators in , not in
a=("Anant panchal welcomes you")
e="apincybers@gmail.com"
if "@" in e and ".com" in e:
    print("Email is valid")
else:
    print("Email is not valid")
print('n' in a , "Miami" in a)
print("Miami" not in a, "n" not in a)
print("@" in e, ".com" in e)
print()

m=[10,20,40,40,50]
s=int(input("Enter a number : "))
if s in m:
    print("Search successful", s)
else:
    print("Search not successful")
