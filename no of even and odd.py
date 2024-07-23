'''
you are given with a space separated integer list find no of even elemnts and no of odd elements in a given list'''
n=list(map(int,input().split(" ")))
even_cnt=0
odd_cnt=0
for i in range(0,len(n)):
    if(n[i]%2==0):
        even_cnt+=1
    else:
        odd_cnt+=1
print(even_cnt)
print(odd_cnt)
