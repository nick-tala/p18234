from array import *
import random

print('askisi 1')

#create matrix with zeros
matrix = [[0 for i in range(10)] for j in range(10)]

#print matrix with zeros
for r in matrix:
    for c in r:
        print(c,end = " ")
    print()


#set matrix with random zeros and ones
for i in range(10):
    for j in range(10):
        num=random.randint(0, 1)
        if num==1:
            matrix[i][j]='S'
        if num==0:
            matrix[i][j]='O'       
        
print()

#print matrix with random zeros and ones
for r in matrix:
    for c in r:
        print(c,end = " ")
    print()       

# count horizontal
count_rows=0

for i in range(10):
    for j in range(8):
        
        if matrix[i][j]=='S' and matrix[i][j+1]=='O' and matrix[i][j+2]=='S':
            count_rows=count_rows+1

print()
print('horizontal ' , count_rows)

#count vertical
count_columns=0

for j in range(10):
    for i in range(8):
        
        if matrix[i][j]=='S' and matrix[i+1][j]=='O' and matrix[i+2][j]=='S':
            count_columns=count_columns+1

print()
print('vertical ' , count_columns)

# count diagonal
count_diag=0

for i in range(0,8):
    for j in range(0,8):
        
        if matrix[i][j]=='S' and matrix[i+1][j+1]=='O' and matrix[i+2][j+2]=='S':
            count_diag=count_diag+1

print()
print('diagonal ' , count_diag)
