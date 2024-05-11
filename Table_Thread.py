# Tg his will show while using simple procedure methos and thread method time comexity
from threading import *
import time

# def Table(n):
#     for i in range(1,11):
#         print(n*i)
#         # time.sleep(1)
#
# def Square():
#     for i in range(1,11):
#         print(i*i)
#         # time.sleep(1)
#
#
#
# start=time.time()
# Table(5)
# Square()
# End=time.time()
# print(End-start) # in this time taken almost 4 sec


# Now thread method

# def Table(n):
#     for i in range(1,11):
#         print("\nThis is FTH", n*i)
#         time.sleep(1)
#
# def Square():
#     for i in range(1,11):
#         print("\nTis is STH", i*i)
#         time.sleep(1)
#
#
# T1=Thread(target=Table, args=(5,))
# T2=Thread(target=Square)

# T1.start()
# T2.start()
# start=time.time()
# T1.join()
# T2.join()
#
# End=time.time()
# print(End-start) # in this time taken almost 10 sec

# this is procedure method normal function calling without thread
def Table(n):
    for i in range(1,11):
        print("\nThis func1", n*i)
        time.sleep(1)

def Square():
    for i in range(1,11):
        print("\nThis is fun2",  i*i)
        time.sleep(1)



start=time.time()
Table(5)
Square()
End=time.time()
print(End-start)  # here you see time taken is 20 sec0nds without thread, compare to previous one