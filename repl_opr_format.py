# example of replacement operator and format() method
rno=501
name="anant"
age=65
str="Roll no is {rn} and Name is {nm} and AGE is {ag}"

print(str.format(rn=rno, nm=name, ag=age))
print("(*)"*16)

str="Roll no is {0} and Name is {1} and AGE is {2}"
print(str.format(rno,name,age))