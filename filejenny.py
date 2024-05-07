f=open("filejenny.txt","r")
# print("file created")
while True:
    data=f.read(1)
    if not data:
        break
    