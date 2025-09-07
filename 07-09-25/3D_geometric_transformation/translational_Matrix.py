import numpy
def translationalMatrix(tx=0,ty=0,tz=0):
    return numpy.matrix([[1,0,0,tx],
                         [0,1,0,ty],
                         [0,0,1,tz],
                         [0,0,0,1]])
matrix=translationalMatrix(1,1,1)
print("Translation Matrix :")
print(matrix)
