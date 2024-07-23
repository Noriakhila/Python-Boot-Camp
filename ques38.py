'''hello-----wor----ld=--------helloworld'''
str="hello---wor---ld"
count=0
ans=""
for i in str:
    if (i=="-"):
        count+=1
    else:
        ans=ans+i
print("-"*count+ans)