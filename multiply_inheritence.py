

class A:
    def __init__(self,*m):
        self.m = m
        print(self.m)
        # self.n = n

class B():

    def sum(self):
        sum = 0
        for i in self.m:
            sum  += i
        return sum

class C(A,B):
    def avg(self):
        ag = (self.sum())/len(self.m)
        return ag



obj1 = C(20,4,3,10)
print(obj1.sum())
print(obj1.avg())





