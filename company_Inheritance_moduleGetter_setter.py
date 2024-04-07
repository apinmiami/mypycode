# This is example of inheritance using getter setter module
# By Anant
import Getters_Setters as getset
class Company(getset.Employee): # Is A Relationship Method
    def setCompanyName(self,cname):
        self.cname=cname
    def getCompanyName(self):
        return self.cname

C1=Company()
C1.setid(100)
C1.setname("Anant")
C1.setdepartment("Computer")
C1.setsalary(100000)
C1.setCompanyName("Data Flair")
print("id=", C1.getid())
print("Name=", C1.getname())
print("Salary=", C1.getsalary())
print("Department=", C1.getdepartment())
print("Company Name: ", C1.getCompanyName())


