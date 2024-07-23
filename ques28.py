'''consonants without spaces'''
vowel="aeiou"
consonant="bcdnghjklmnpqrstvwxyz"
count=0
c=0
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for j in inp:
    if(j in consonant):
        c+=1
print(count)
print(c)
