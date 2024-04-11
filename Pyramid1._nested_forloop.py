# example of star pyramid
n=int(input("Enter the limit: "))
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#         print("*",end=" ")
#     print()
# example of number pyramid
# for i in range(1,n+1,1):
#     for j in range(1,i+1,1):
#       #  print("%d"%j,end=" ")
#         print("%d" %i, end=" ")
#     print()
#example of reverse pysramid
for i in range(1,n+1,1):
    for j in range(n,i-1,-1):
        print("*", end=" ")
    print()