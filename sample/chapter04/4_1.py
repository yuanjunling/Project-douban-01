class A:
    aa = 1
    def __init__(self,x,y):
        self.x = x
        self.y = y

a = A(1,2)
b = A(3,5)
a.aa = 101
A.aa = 100
print(a.x,a.y,a.aa)
print(A.aa)
print(a.aa)
print(b.aa)