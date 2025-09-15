############################2단원#################################
###2.1
# #연립방정식의 해 풀기 Ax=b라고 할때,
# A = np.array([[4,3], [3,2]])
# b = np.array([23,16])
#
# #solve로 x구하기->x=np.linalg.solve(A,b)
# x=np.linalg.solve(A,b)
# print(x) #[2. 5.]
#
# #check1: 위에서 생성한 x가 제대로 된건지 확인->np.allclose(np.dot(A,x),b)
# print(np.allclose(np.dot(A,x),b)) #True
#
# A = np.array([[4,3], [3,2]])
# b = np.array([23,16])
# #check2: inv이용->y=np.dot(np.linalg.inv(A),b)
# x=np.dot(np.linalg.inv(A),b)
# print(x) #[2. 5.]
#

# #i번째 인덱스 행,열 slicling-> 행->v[i,:] 열->v[:,i]
# v=np.array([[1,2], [3,4]])
# print(v[0,:])
# print(v[:,0])


# #행사다리꼴 판별
# import numpy as np
#
#
# def is_row_echelon(A):
#     matrix = np.array(A, dtype=float)
#     last_pivot_col = -1
#     found_zero_row = False
#
#     for row in matrix:
#         if np.all(np.isclose(row, 0)):
#             found_zero_row = True
#             continue
#         if found_zero_row:
#             return False
#         try:
#             current_pivot_col = np.where(~np.isclose(row, 0))[0][0]
#         except IndexError:
#             continue
#         if current_pivot_col <= last_pivot_col:
#             return False
#         last_pivot_col = current_pivot_col
#     return True
#
#
# # --- 함수 테스트 ---
#
# # 예시 1: 행사다리꼴인 경우 (True)
# A1 = np.array([[1, 2, 3, 4],
#                [0, 1, 2, 3],
#                [0, 0, 0, 1]])
# print(f"행렬 A1:\n{A1}")
# print(f"행사다리꼴인가? -> {is_row_echelon(A1)}\n")
#
# # 예시 2: 행사다리꼴인 경우 (0인 행 포함) (True)
# A2 = np.array([[1, -2, 0, 1],
#                [0, 0, 1, 3],
#                [0, 0, 0, 0],
#                [0, 0, 0, 0]])
# print(f"행렬 A2:\n{A2}")
# print(f"행사다리꼴인가? -> {is_row_echelon(A2)}\n")
#
# # 예시 3: 행사다리꼴이 아닌 경우 (피벗 위치 오류) (False)
# A3 = np.array([[1, 2, 3],
#                [0, 1, 2],
#                [0, 1, 4]])  # 3행의 피벗이 2행 피벗보다 오른쪽에 있지 않음
# print(f"행렬 A3:\n{A3}")
# print(f"행사다리꼴인가? -> {is_row_echelon(A3)}\n")
#
# # 예시 4: 행사다리꼴이 아닌 경우 (0인 행 위치 오류) (False)
# A4 = np.array([[1, 2, 3],
#                [0, 0, 0],
#                [0, 0, 1]])  # 0인 행 아래에 0이 아닌 행이 있음
# print(f"행렬 A4:\n{A4}")
# print(f"행사다리꼴인가? -> {is_row_echelon(A4)}\n")
#
# #기약 행사다리꼴 판별
# import sympy
# A = sympy.Matrix([
#     [1, 2, -1, -4],
#     [2, 3, -1, -11],
#     [-2, 0, -3, 22]
# ])
#
# rref_matrix, pivot_columns = A.rref()
#
# print("기약 행사다리꼴(RREF):")
# # pprint(rref_matrix) # 더 예쁘게 출력하려면 pprint 사용
# print(rref_matrix)
#
# print("\n피벗 열의 인덱스:")
# print(pivot_columns)
#
# #A가역->A를 기본행렬곱으로 분해
# import numpy as np
#
#
# # 여기에 제공하신 get_elementary_matrices 함수를 붙여넣으세요.
# def get_elementary_matrices(A):
#     # (함수 내용)
#     if A.shape[0] != A.shape[1] or np.linalg.det(A) == 0:
#         print("정사각행렬이 아니거나 비가역행렬입니다.")
#         return None
#     n = A.shape[0]
#     M = A.copy().astype(float)
#     inverse_elementary_matrices = []
#     for i in range(n):
#         if np.isclose(M[i, i], 0):
#             for k in range(i + 1, n):
#                 if not np.isclose(M[k, i], 0):
#                     M[[i, k]] = M[[k, i]]  # 행 교환
#                     E = np.identity(n)
#                     E[[i, k]] = E[[k, i]]
#                     inverse_elementary_matrices.append(E)  # 행 교환 행렬의 역행렬은 자기 자신
#                     break
#
#         pivot = M[i, i]
#         if not np.isclose(pivot, 1):
#             E = np.identity(n)
#             E[i, i] = pivot  # 역연산은 곱하기
#             inverse_elementary_matrices.append(E)
#             M[i, :] /= pivot  # M[i] -> (1/pivot) * M[i]
#
#         for j in range(n):
#             if i == j: continue
#
#             factor = M[j, i]
#             if not np.isclose(factor, 0):
#                 E = np.identity(n)
#                 E[j, i] = factor  # 역연산은 더하기
#                 inverse_elementary_matrices.append(E)
#                 M[j, :] -= factor * M[i, :]  # M[j] -> M[j] - factor * M[i]
#
#     print(f"--- 행렬 A ---\n{A}\n")
#     print("A를 구성하는 기본행렬들 (E1^-1, E2^-1, ... 순서):")
#     for i, E in enumerate(inverse_elementary_matrices):
#         print(f"--- E{i + 1} ---\n{np.round(E, 4)}\n")
#
#     A_reconstructed = np.identity(n)
#     for E in reversed(inverse_elementary_matrices):
#         A_reconstructed = A_reconstructed @ E
#
#     print("--- 검증: 기본행렬들을 모두 곱한 결과 ---")
#     print(np.round(A_reconstructed, 4))
#
#     return inverse_elementary_matrices
# print("===== 예시 1: 2x2 기본 행렬 테스트 =====")
# A1 = np.array([[2, 1],
#                [1, 1]])
# get_elementary_matrices(A1)
# # 테스트 예시 2
# print("\n\n===== 예시 2: 3x3 행 교환 필요 행렬 테스트 =====")
# A2 = np.array([[0, 1, -1],
#                [3, -1, 1],
#                [1, 1, -1]])
# get_elementary_matrices(A2)
# # 테스트 예시 3
# print("\n\n===== 예시 3: 3x3 복합 행렬 테스트 =====")
# A3 = np.array([[2, 4, 6],
#                [1, 3, 5],
#                [2, 4, 3]])
# get_elementary_matrices(A3)

##2.2
# #역행렬-> np.linalg.inv
# x=np.array([[1,2], [3,4]])
# y=np.linalg.inv(x)
# print(y)
# print(x.dot(y))

###2.3
# #행렬식->np.linalg.det
# x=np.array([[1,2], [3,4]])
# print(np.linalg.det(x))

