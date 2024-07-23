''' given a space separated integer list find the average of elements in the even index'''
num=list(map(int,input().split(" ")))
sum=0
avg=0
for i in range(0,len(num),2):
    if(i%2==0):
        sum+=num[i]
        avg=sum/len(num)
         print("avg")
