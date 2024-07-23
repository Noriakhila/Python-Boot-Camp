''' ABC 4=EFG'''
n=input()
for i in n:
    n=ord(i)+4
    if n>=90:
        print(chr(n-26))
    else:
        print(chr(n))

    