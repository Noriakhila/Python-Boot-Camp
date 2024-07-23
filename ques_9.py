''' finnd the sum of elements  thtat is present in k+N index k is given by the user
k=3 
N=2
 i/p:
 3 6 8 4 61 2 
o/p:
2
i/p:k=3, N=4
80 70 54 36 72
0/p:error
'''
'''my_list=list(map(int,input().split(" ")))
k=int(input())
N=int(input())
if(len(my_list)<k+N):
    print("error")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+N],end=" ")
        break'''
'''print the element at a particular index  by circular method
k=20
70 54 36 72 999 89 76    k=20,7
 1  2  3  4  5   6  7     idx   '''
my_list=list(map(int,input().split(" ")))
k=int(input())
n=k%len(my_list)
print(my_list[n-1])