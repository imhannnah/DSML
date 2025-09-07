import numpy

def scalingMatrix(tx=0,ty=0,tz=0):
    return numpy.matrix([
        [tx,0,0,0],
        [0,ty,0,0],
        [0,0,tz,0],
        [0,0,0,1]])
matrix = scalingMatrix(1,1,1)
print("Scaling Matrix:")
print(matrix)
