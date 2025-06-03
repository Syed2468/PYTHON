def calculate_percentage(person):
    total_marks=sum(person["marks"])
    return(total_marks/4)
a=[{"name":"raju","age":23,"marks":[45,50,40,60]},
   {"name":"rose","age":12,"marks":[75,85,88,90]},
   {"name":"virat","age":53,"marks":[65,71,60,80]}]
b=sorted(a,key=calculate_percentage,reverse=True)
pos=1
for i in b:
    if pos==1:
        des="FIRST"
    elif pos==2:
        des="SECOND"
    elif pos==3:
        des="THIRD"
    percentage=calculate_percentage(i)
    print("{} wit per {:.2f} % stands->{}".format(i["name"],percentage,des))
    pos=pos+1