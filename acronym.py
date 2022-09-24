acronym=[str(i) for i in input().split()]
list_1=[]
for i in acronym:
    list_1+=[i[0]]
print(".".join(str(i) for i in list_1))