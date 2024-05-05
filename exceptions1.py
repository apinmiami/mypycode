# Theseare  exception HANDLING EXAMPLES IN PYTHON
a=int(input("Enter a First number : "))
b=int(input("Enter a second number: "))
try:               # Tis try block
    c = a // b
    print(f"Division is {c}")
except ZeroDivisionError as obj:  # this is exception block and Zerodivision error is class and obj is obj
                                    # object of that class
    print("Unable to devide by Zero")
    print(obj)
finally:  # this will always executed if code is terminated
    print("***end of program***")