# This is example of various scenario in Constructor or we call it __init__
# By Anant
class Marks1:
    def __init__(self, hindi, english):
        self.hindi=hindi
        self.english=english

class Marks2(Marks1):
    def __init__(self,comp,maths,h,e):
        super().__init__(h,e)
        self.comp=comp
        self.maths=maths
    def results(self):
        print(self.maths+self.comp+self.hindi+self.english)

M1=Marks2(100,200,200,80)
M1.results()











# class Top:
#     def __init__(self):
#         print("Constructor of Top class")
# class First(Top):
#     def __init__(self):
#         super().__init__()
#         print("Constructor of First Class")
#
# class Second(First):
#     def __init__(self): # if you comment both below and pass it than object of First class will be called
#         super().__init__() # If you comment this only second class object will be called
#         print("Constructor of Second Class")
#
# S1=Second()
