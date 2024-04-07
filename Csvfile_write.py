# this is example to write csv file watch video 165 for theory
# By Anant Panchal
import csv
try:
    f=open("D://PYTHON/DATA flair python/NOTES/college.csv", "w",newline='')
    obj=csv.writer(f)
    obj.writerow(['college id', 'college name', 'Course'])
    print("File created ***")
    while True:
        cid=int(input("Enter college id: "))
        cname=input("College Name: ")
        course=input("Enter course name: ")
        obj.writerow([cid,cname,course])
        choice=input("Want to continue: ")
        if choice=="no":
            break




except Exception as msg:
    print(msg)