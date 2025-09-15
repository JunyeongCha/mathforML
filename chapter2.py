import numpy as np

# #예제1
# A=np.array([[1,3,2], [2,-1,-4], [3,2,-1]])
# b=np.array([2,-5,-1])
# x=np.linalg.solve(A,b)
# print(x)
#
# #예제2
# A=np.array([[1,-1,1], [0,5,2], [3,1,0]])
# b=np.array([0,12,5])
# x=np.linalg.solve(A,b)
# print(x)

# #예
# A=np.array([[2,-5], [-1,3]])
# B=np.linalg.inv(A)
# print(B)

# #예
# A=np.array([[a,b], [c,d]])
# B=np.linalg.inv(A)
# print(B)

# #1번
# A=np.array([[1,3,-1], [2,5,1], [1,1,1]])
# b=np.array([1,5,3])
# x=np.linalg.solve(A,b)
# print(x)

# #2번
# A=np.array([[1,2,-1,3], [0,3,-3,1], [2,1,0,2]])
# b=np.array([0,3,-2])
# x=np.linalg.solve(A,b)
# print(x)

# #5번(a)
# x=np.array([[3,4,-1], [1,0,3], [2,5,-4]])
# y=np.linalg.inv(x)
# print(y)
# print(x.dot(y))
#
# #5번(b)
# x=np.array([[1,0,1], [0,1,1], [1,1,0]])
# y=np.linalg.inv(x)
# print(y)
# print(x.dot(y))

# #6번
# A=np.array([[1,2,3], [2,5,3], [1,0,8]])
# b=np.array([1,3,-1])
# x=np.linalg.solve(A,b)
# print(x)

# #7번
# A=np.array([[1,2,-3], [1,3,1], [2,5,-4], [2,6,2]])
# b=np.array([4,11,13,22])
# x=np.linalg.solve(A,b)
# print(x)