'''
 leap years btwn ranges'''
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(i%4==0) and (i%100!=0):
        print(i)
'''leap year'''
year=int(input())
if(year%400==0):
    print("leap")
else:
    print("not a leap)