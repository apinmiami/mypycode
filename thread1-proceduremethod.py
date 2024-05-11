# tho create thread using procedureis is the program how t
from threading import *
import time

def dis():
    for i in range(1,11):
        print("\nThis is First", i)
        time.sleep(1)

def show():
    for i in range(100,111):
        print("\nThis is Second", i)
        time.sleep(1)

T1=Thread(target=dis)
T2=Thread(target=show)
Start=time.time()
T1.start()
T2.start()
End=time.time()
T1.join()
T2.join()
T1.setName("First")   # this is how you can give thread a name
T2.setName("Second")  # incase if u dont give it will show dwfault name after commenting this and
                      # usint getName method

print(T1.getName())
print(T2.getName())
Totaltime=End-Start
print(Totaltime)