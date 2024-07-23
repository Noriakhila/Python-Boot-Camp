'''#mr.x is trying to create a new password for his instagram account hese are the required conditions
    #for creating a new password:
    #1.minimum length is 8 ,maximum length is 15
    #2.only @,/ is allowed in a password
    #3.no spaces are allowed
    #4.only alpha numerics are allowed
    #you are supposed to print weak ability if length is exact 8
    #medium length is btw 8 to 12
#strong length is btw 12 to 15 '''
password=input
l=len(password)
count=0
for i in n:
    if("@"in password ) and ("/"in password):
        count+=1
    if(password==8):
        print("weak")
    elif(password>8 and password<12):
        print("medium")
    else:
        print("strong")