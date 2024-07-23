'''peak elemnet'''
'''n=list(map(int,input().split(" ")))
peak=0
for i in range(1,len(n)-1):
    if(n[i]>=n[i-1]) and (n[i]>=n[i+1]):
        peak=n[i]
        break
print(peak)'''
''' peak elements in  array
n=list(map(int,input().split(" ")))
for i in range(1,len(n)-1):
    if(n[i]>=n[i-1]) and (n[i]>=n[i+1]):
        print(n[i],end=" ")'''
''' peak element i present at last'''
n=list(map(int,input().split(" ")))
count=0
for i in range(1,len(n)-1):
    if(n[i]>=n[i-1]) and (n[i]>=n[i+1]):
        count=i
    if(n[-1]>n[-2]and n[-1]>count):
        count=len(my_list)-1
    print(n[count])
