''' replace the elemnts in an array with average of max and min elements:
test case:
13 2 67 20 68
68+2==70
35 35 35 35 35'''
my_list=list(map(int,input().split(" ")))
avg=0
max=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
for j in range(len(my_list)):
    if(my_list[j]<min):
        min=my_list[j]
avg=(max+min)//2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)
