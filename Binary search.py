n= [20,30,40,50,60,70,80,90,100]
found=False
lb=0
ub= len(n)-1
searchvalue=int(input("enter a number"))
while found==False and lb<= ub:
    index= int(((lb+ub)/2))
    if n[index]== searchvalue:
        found=True
    elif n[index]<searchvalue:
        lb= index+1
    elif n[index]>searchvalue:
        ub=index-1
if found:
    print("found",index)
else:
    print("not found bruhh!!")




