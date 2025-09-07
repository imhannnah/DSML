import numpy
def translationalMatrix(tx=0,ty=0):
    return numpy.matrix([[1,0,tx],[0,1,ty],[0,0,1]])
matrix=translationalMatrix(1,1)
print("Scaling Matrix:")
print(matrix)
