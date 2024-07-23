'''second largest element'''
my_list_list=list(map(int,input().split(" ")))
max=my_list[1]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
        print(max) 
