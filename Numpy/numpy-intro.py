import numpy as np
a =np.array([1,2,3,5,7])
b =np.array((2,3,5))
print(a)

A =np.array([[1,2,3],[4,5,6]])
A.ndim

print(A.ndim)

B=np.array([[1,2,3,4],[2,4,5,9]])
print(B[1,2])

C =np.array([
    [[1,2,3],[4,5,6],[7,8,9]],
    [[1,2,3],[4,5,6],[7,8,9]]
    
])
print(C.ndim)
print(C[1,2,1])
print(type(C))



#SHAPE PROPERTY
D=np.arange(100)
print(D)
 
R =np.arange(100).reshape(4,25)
print(R.shape)

#slcing
Z=np.arange(100)
G=Z[3:10]
print(G)

b =A[3:10].copy()
print(Z[::5])

print(A[::-5])


idx =np.argwhere(Z==5)[0][0]

T=np.round(10*np.random.rand(5,4))
print(T)
print(T[3][1])

print(T[1,:])
#for column
print(T[:,1])
print(T[1:3,2:4])

import numpy.linalg  as la  
la.inv(np.random.rand(3,3))


