from numpy import matrix
from numpy import matmul
from numpy import diag
from scipy.linalg import svd #linear algebra
A = matrix([[1,2,3],
            [4,5,6],
            [7,8,9]])
print(A)
U, S, V = svd(A) # Singular-value decomposition
print("\n",U) # A is decomposed into 3 matrices U, a diagonal matrix and V
print("\n",S)
print("\n",V) # Here S contains only the diagonal elements of the diagonal matrix
Sigma = diag(S)# create diagonal matrix from diagonal elements
print("\n",Sigma)
B = matmul(U,matmul(Sigma,V)) # reconstruct matrix
print("\n",B)
