'''find  the missing number in an array
test case:
1 2 3 4 5 6 7 8 9 10=55
1 2 3 4 6 7 8 9 10=50
55-50=5'''
my_list=list(map(int,input().split(",")))
num=int(input())
sum=0
miss=0
for i in range(0,len(my_list),1):
    sum+=my_list[i]
miss=num-sum
print(miss)
