'''find the duplicates in an array'''
my_list=list(map(int,input().split(",")))
d=[]
for i in my_list:
    if(i not in d):
        d.append(i)
print(d)    
