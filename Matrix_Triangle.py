# Making Matrix triangle Left and right and Diaognal taking runtime data from use.

import numpy as np
import array as ar

m,n=[int (a) for a in input("Enter Values for Row and Col: ").split()]
x=m*n
myar= ar.array ('i', [])
print("Enter %d element in Matrix"%x)

for i in range(x):
    b=int(input())  # After this enter Elements
    myar.append(b)
myar1=np.reshape(myar,(m,n))
print(myar1)
# for r in range(m):
#     for c in range(n):
#         if r >= c: # condition for lower Triangle
#             print(myar1[r][c],end=" ")
#     print()

# for r in range(m):
#     for c in range(n):
#         if r <= c: # condition for Upper Triangle
#             print(myar1[r][c],end=" ")
#     print()

for r in range(m):
    for c in range(n):
        if r == c: # condition for DIAGONAL
            print(myar1[r][c],end=" ")
    print()
