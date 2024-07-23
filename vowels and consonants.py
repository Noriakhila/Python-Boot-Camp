''' to print how many vowels are there in a string and consonants'''
str=input()
vowel=['a','e','i','o','u']
count=0
con=0
for i in str:
    if(i in vowel):
        count+=1
    else:
        con+=1
print(con)
print(count)
