'''find the sum of squares of digit in a nnumber'''
n=int(input())
sum=0
while n>0:
    r=n%10
    sum=r**2+sum
    n=n//10
print(sum)
