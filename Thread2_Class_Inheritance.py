# This is example of making thread by inheriting Thread class
from threading import *
import time
class Mth1(Thread):
    def run(self):    # here run is implicit method, it will exceute as noramal function will not run as
                      # thread so we donot call run method. its default when we inherit thread class.
        for i in range(1,11):
            print("\n Mythread1:", i)
            time.sleep(1)

class Mth2(Thread):
    def run(self):
        for i in range(1,11):
            print("\n Mythread2", i**2)
            time.sleep(1)
T1=Mth1()
T2=Mth2()
start=time.time()
T1.start()
T2.start()
T1.join()
T2.join()
end=time.time()
print("Default name of Mth1 is", T1.getName())
print("Default name of Mth2 is", T2.getName())
print("Total time of execution is", end-start)