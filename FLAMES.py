name1=input("Enter Boy Name:")
name2=input("Enter Girl Name:")
l1=list(name1)
l2=list(name2)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l1[i]='$'
            l2[j]='$'
a=l1.count('$')
b=l2.count('$')
tot=a+b
ans=['FRIEND','LOVE','AFFECTION','MARRIAGE','ENEMY','SISTER']
F=0
while(len(ans)!=1):
    F=(F+(tot-1))%len(ans)
    ans.pop(F)
print(ans)