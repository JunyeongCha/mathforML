import numpy as np

# #1번
# A=np.array([[1,3], [4, -1]])
# B=np.array([[-1,2,5], [1,-1,4]])
# C=np.array([[1,0], [2, -1], [3,2]])
# print(A@(B@C))
# print((A@B)@C)
# print(np.allclose(A@(B@C),(A@B)@C))

# #2번
# A=np.array([[-2,3], [2,-3]])
# B=np.array([[-1,3], [2,0]])
# C=np.array([[-4,-3], [0,-4]])
# x=A@B
# y=A@C
# print(x)
# print(y)
#
# print(np.allclose(x,y))

# #3번
# A=np.array([[0,3], [2,-1]])
# po_0=np.eye(2)
# po_2=np.linalg.matrix_power(A,2)
# po_4=np.linalg.matrix_power(A,4)
# print(2*po_4-po_2-2*A+5*po_0)

# #4번
# A=np.array([[1,3], [2,5]])
# B=np.array([[1,1,3], [2,1,4]])
# C=(A@B).T
# D=(B.T)@(A.T)
# print(C)
# print(D)
# print(np.allclose(C,D))

# #5번(a)
# A=np.array([[1,2,3], [2,4,5], [3,5,6]])
# print(np.allclose(A, A.T))
# #5번(b)
# B=np.array([[0,2,3], [-2,0, 5], [-3,-5,0]])
# print(np.allclose(B, -B.T))

# #6번
# A=np.array([[1,2,3], [1,2,3], [4,5,6]])
# B=A.T
# print(np.allclose(A+A.T, (A+A.T).T)) #대칭
# print(np.allclose(A-A.T, -(A-A.T).T)) #반대칭

# #7번
# A=np.array([[2,3,-1], [1,8,1]])
# B=np.array([[2,3], [-3,1], [1,-1]])
# x=np.trace(A@B)
# y=np.trace(B@A)
# print(x)
# print(y)
# print(np.allclose(x,y))

# #8번
# A=np.array([[1,2,4], [0,3,1], [0,0,2]])
# B=np.array([[2,1,3], [0,2,4], [0,0,3]])
# x=A@B
# print(np.allclose(A, np.triu(A)))
# print(np.allclose(B, np.triu(B)))
# print(np.allclose(x, np.triu(x)))