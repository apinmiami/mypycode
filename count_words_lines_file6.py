# This are examples of word counts and line counts in a file
# By Anant Panchal
import os
import sys
try:
    str=input("Enter a file name: ")
    if os.path.isfile("D://PYTHON/DATA flair python/NOTES/"+str+".txt"):
        f=open("D://PYTHON/DATA flair python/NOTES/"+str+".txt", "r")
        if f.readable():
            mylist=f.readlines()
            wc=lc=cc=0
            for line in mylist:
                lc=lc+1
                words=line.split()
                wc=wc+len(words)
                cc=cc+len(line)
                print("Total Lines: ", lc)
                print("Total Words: ", wc)
                print("Total Characters: ", cc)


    else:
        print("File not found***")
        sys.exit()


except Exception as obj:
    print(obj)