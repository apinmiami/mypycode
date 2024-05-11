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
Totaltime=End-Start
print(Totaltime)