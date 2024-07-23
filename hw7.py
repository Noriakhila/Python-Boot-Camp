'''reverse '''
n=int(input())
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10