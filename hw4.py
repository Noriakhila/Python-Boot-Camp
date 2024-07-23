'''find the peak element in array'''
n=list(map(int,input().split(" ")))
peak=0
for i in range(1,len(n)-1):
    if(n[i]>=n[i-1]) and (n[i]>=n[i+1]):
        peak+=1
        if(peak>0):
            print(n[i])
            break
    else:
        print(n)