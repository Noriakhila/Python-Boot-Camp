'''
take a space separated input from the user and print alternate elements
'''
number=list(map(int,input().split(" ")))
for i in range(0,len(number),2):
    print(number[i])
    '''
  question_7  you are given with a comma separated natural numbers 1 to 10   print the even numbers
