class Myclass:
    def __init__(self,n):
        self.n=n
    def __add__(self, other):
        self.n=self.n+other.n
        return self.n
    def __mul__(self, other):
        print(self.n * other.n)
        self.n=self.n*other.n
        print(self.n*other.n)
        return self.n



M1=Myclass(50)
M2=Myclass(20)
M3=M1+M2
M4=M1*M2
print(M3)
        # will show error bcz this operator is not overloaded
print(M4)