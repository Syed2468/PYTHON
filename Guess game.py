import time 
import random
p1=input("Enter p1 name:")
p2=input("Enter p2 name:")
print("Hello {} and {}".format(p1,p2))
print("You have three choice ")
print("ALL THE BEST")
n=[]
while(len(n)!=5):
    d=random.randint(1,10)
    if(d in n):
        continue
    else:
        n.append(d)
p_1=[]
p_2=[]
s1=0
s2=0
for i in range(3):
    print("{} enter ur guess:".format(p1))
    a=int(input())
    if(a not in p_1 or a not in p_2):
        p_1.append(a)
        if(a in n):
            print("---->CORRECT")
            s1=s1+1
        else:
            print("---->WRONG")
    print("{} enter ur guess:".format(p2))
    b=int(input())

    if(b not in p_1 or b not in p_2):
        p_2.append(b)
        if(b in n):
            print("---->CORRECT")
            s2=s2+1
        else:
            print("---->WRONG")
            
print("The original nos are {}".format(n))
print("{} guessed the number {}".format(p1,p_1))
print("{} guessed the number {}".format(p2,p_2))

if(s1==s2):
    print("MATCH DRAW")
elif(s1>s2):
    print("{} has own the game".format(p1))
else:
    print("{} has own the game".format(p2))
