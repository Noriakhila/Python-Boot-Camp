'''helloworld123'''
inp="hello world 123"
sum=0
num="0123456789"
for i in inp:
    if(i in num):
        sum+=int(i)
print(sum)
