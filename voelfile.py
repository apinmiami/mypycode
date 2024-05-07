import os
try:
    str="filejenny.txt"
    if(os.path.isfile(str)):
        f=open(str,"r")
        count=0
        sp=0
        dg=0
        while True:
            ch=f.read(1)
            if not ch:
                break
            if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
                count+=1

            elif(ch.isspace()):
                sp=sp+1
            elif(ch.isdigit()):
                dg+=1
                print("total vovel", count)
                print("Total space", sp)
                print("total Digit", dg)



except Exception as msg:
    print(msg)
