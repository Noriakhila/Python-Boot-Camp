'''question_7  you are given with a comma separated natural numbers 1 to 10   print the even numbers
'''
#number=list(map(int,input().split(",")))
#for i in range(1,11):
 #   if(i%2==0):
  #      print(i,end=" ")
'''
how many even numbers are their in the above question'''
number=list(map(int,input().split(",")))
count=0
for i in range(1,11):
    if(i%2==0):
     count+=1
print(count)
