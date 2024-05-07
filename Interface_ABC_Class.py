# Example of Fully Abstact class or interface in PYTHON
from abc import *
class DB(ABC):
    @abstractmethod
    def conn(self):
        pass
    @abstractmethod
    def discon(self):
        pass
class oracle(DB):
    def conn(self):
        print("Oracle connection")
    def discon(self):
        print("Oracle Disconnection")

class Mysql(DB):
    def conn(self):
        print("Mysql connection ")
    def discon(self):
        print("Mysql Disconnection ")

dname=input("Enter databse name ")
cname=globals()[dname]
x=cname()
x.conn()
# x.discon()

