###################????####################
# #c가 행렬일때 w,v(고유값, 고유벡터)=np.linalg.eig(c)사용, v가 고유벡터->각 열이 각 고유값에 해당할때의 고유벡터
# c=np.array([[4,2], [3,5]])
# w,v=np.linalg.eig(c)
# print(w) #고유값 2,7
# print(v) #고유벡터
# print(v[:,0].reshape(2,1)) #고유값 람다=2일때의 고유벡터=v의 1열
# print(v[:,1].reshape(2,1)) #고유값 람다=7일때의 고유벡터=v의 2열

# #singlular판단->det=0이면 됨->is_singular함수 생성
# def is_singular(mat):
#     answer=np.linalg.det(mat)
#     if answer==0:
#         return True
#     else:
#         return False
# A = np.array([[4,3], [3,2]])
# print(is_singular(A)) #False