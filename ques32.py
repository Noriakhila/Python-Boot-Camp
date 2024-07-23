'''reverse of number hello world 123=hello world 321'''
inp="hello world 123"
sum=0
s=0
num="0123456789"
for i in inp:
    if(i in num):
        sum+=int(i)
        s+=i
n=int(s)
while(n>0):
    r=n%10
    e=e*10+r
    n=n//10
print(e)

