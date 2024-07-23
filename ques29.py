'''to print vowels and consonats'''
str=input()
inp=str.lower()
vowel="aeiou"
con="bcdfghjklmnpqrstvwxyz"
count=0
a,b="",""
c=0
for i in str:
    if(i in vowel):
        count+=1
        a=a+i
    elif i in con:
        c+=1
        b=b+i
    else:
        continue
print(count)
print(c)
print(a+b)


    