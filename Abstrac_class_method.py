# These are examples of abstract class and methods, for understand theory see video 124 on website
# By Anant
from abc import ABC,abstractmethod
class Button(ABC):
    @abstractmethod
    def click(self):
        pass
    def display(self):
        print("This display is not abstract method")

class Mycolor(Button):
    def click(self):
        print("Color is Red")

class Myphoto(Button):
    def click(self):
        print("This is my Photo")

M1=Mycolor()   # Button 1
M2=Myphoto()   # Button 2
M1.click()
M2.click()
M1.display()
M2.display()





