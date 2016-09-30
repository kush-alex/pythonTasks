'''Матрица состоит из нулей и единиц. Найдите в ней самую
длинную цепочку подряд идущих нулей по горизонтали, вертикали или диагонали.
'''
from sys import stdout

def print_matrix(m):
    for a in range(len(m)):
        for b in range(len(m[a])):
            stdout.write(str(m[a][b])+" ")
        stdout.write("\n")
        stdout.flush()

def sub_matrix(m,x,y):
    new_matrix=[]
    for a in range(len(m)-x):
        temp=[]
        for b in range(len(m[a])-y):
            temp.append(m[a+x][b+y])
        new_matrix.append(temp)
    return new_matrix
