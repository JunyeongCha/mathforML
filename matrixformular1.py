import numpy as np

##############1단원################################
###1.1
# #단위행렬->np.eye(n)=In
# unit_mat_4=np.eye(4)
# print(unit_mat_4)
###1.2
##행렬의 상등->np.allclose(A, B)
#
# #영행렬->np.zeros(행수,열수)
# zero_mat_43=np.zeros((4,3))
# print(zero_mat_43)
#
# #행렬의 type
# print(type(zero_mat_43))
#
###1.3
# #np.arange->범위설정, np.reshape:1차원에서 행/렬 변환
# x=np.arange(5)
# print(x.reshape(5,1))
# print(np.arange(5).reshape(5,1))
#
# #np.diag->대각 추출, 대각행렬생성
# y=np.arange(9).reshape(3,3)
# print(y)
# print(np.diag(y))
# print(np.diag(np.diag(y)))
# print(np.diag(np.array([1,2,3])))
#
# #원하는 원소로 행렬 생성
# x=np.array([[1,2,3], [4,5,6]])
# print(x)
#
# #행렬의 곱->>np.dot, @
# a=np.arange(4,8).reshape(2,2)
# b=np.arange(4).reshape(2,2) #a*b=10,19,14,27
# print(np.dot(a,b))
# print(a@b)
# print(a.dot(b))

# #행렬의 거듭제곱
# A = np.array([[4,3], [3,2]])
# print(np.linalg.matrix_power(A,4))

###1.4
# #전치 행렬->T,np.transpose
# y=np.arange(9).reshape(3,3)
# print(y.T)
# print(y.transpose())
# print(np.transpose(y))

# #대각합->np.trace
# x=np.array([[1,2], [3,4]])
# print(np.trace(x))

#대칭 판별: np.allclose(A, A.T)
#반대칭 판별: np.allclose(B, -B.T)
# #상삼각행렬 판별: np.allclose(C, np.triu(C))
# C = np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
#
# is_upper = np.allclose(C, np.triu(C))
# print(f"상삼각행렬인가? {is_upper}") #True
#
# #하삼각행렬 판별: np.allclose(C, np.tril(C))
# C = np.array([[1, 0, 0], [3, 4, 0], [1,2, 6]])
#
# is_lower = np.allclose(C, np.tril(C))
# print(f"하삼각행렬인가? {is_lower}") #True