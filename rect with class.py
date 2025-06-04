class sim:
    def dim(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        print(self.a*self.b)
    def peri(self):
        print(self.a+self.b)
    
l=[]
n=int(input("Enter the number of rectangles :"))
for i  in range(n):
    r=sim()
    a=int(input("Enter the width {}".format(i+1)))
    b=int(input("Enter the length {}".format(i+1)))
    r.dim(a,b)
    l.append(r)
for i in range(n):
    print("RECTANLE NO. ",i+1)
    l[i].area()
    l[i].peri()
    
    
