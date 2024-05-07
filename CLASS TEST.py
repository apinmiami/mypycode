class Test:
    def __init__(self,n):
        self.n=n
    def __sub__(self,other):
        self.n=self.n-other.n
        return self.n

    def __add__(self,other):
        self.n=self.n+other.n
        return self.n
    def __mul__(self, other):
        x=self.n*other.n
        return x

m1=Test(50)
m2=Test(30)
m3=m1-m2
m4=m1+m2
m5=m1*m2
print("Subtraction over load is : ", m3)
print(m1+m2)

print(m5)
