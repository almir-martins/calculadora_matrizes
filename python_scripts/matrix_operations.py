import numpy as np


# ===================================
# As quatro operações básicas
# ===================================
# Adição de matriz
def soma_matriz(A, B):
    try:
        C = A + B

    # Matriz não contém somente números
    except np.core._exceptions._UFuncNoLoopError:
        print("Os elementos precisam ser números!")

    # Matrizes de tamanhos diferentes
    except ValueError:
        print("Matrizes de tamanhos diferentes!")

    # except Exception as e:
    #     print(e)
    #     print("Eroooou")

    else:
        print(f"Tamanho A = {len(A)}")
        print(f"Tamanho B = {len(B)}")
        print(f"A = \n{A}")
        print()
        print(f"B = \n{B}")
        print()
        print(f"A+B = \n{C}")
        print()
        print("TUDO FUNCIONANDO OK")
        print()


# Subtração de matriz
def subtrai_matriz(A, B):
    try:
        C = A - B

    # Matriz não contém somente números
    except np.core._exceptions._UFuncNoLoopError:
        print("Os elementos precisam ser números!")

    # Matrizes de tamanhos diferentes
    except ValueError:
        print("Matrizes de tamanhos diferentes!")

    # except Exception as e:
    #     print(e)
    #     print("Eroooou")

    else:
        print(f"Tamanho A = {len(A)}")
        print(f"Tamanho B = {len(B)}")
        print(f"A = \n{A}")
        print()
        print(f"B = \n{B}")
        print()
        print(f"A+B = \n{C}")
        print()
        print("TUDO FUNCIONANDO OK")
        print()


# Produto de matriz
def multiplica_matriz(A, B):
    try:
        C = np.dot(A, B)

    # Matriz não contém somente números
    except np.core._exceptions._UFuncNoLoopError:
        print("Os elementos precisam ser números!")

    # Matrizes de tamanhos diferentes
    except ValueError:
        print("Matrizes de tamanhos diferentes!")

    # except Exception as e:
    #     print(e)
    #     print("Eroooou")

    else:
        print(f"A = \n{A}")
        print()
        print(f"B = \n{B}")
        print()
        print(f"A*B = \n{C}")
        print()
        print("TUDO FUNCIONANDO OK")
        print()


# Divisão de matriz
def divide_matriz(A, B):

    if np.shape(B) < 1:
        print(f"A matriz precisa ser quadrada")
    elif np.shape(B)[0] != np.shape(B)[1]:
        print(f"A matriz precisa ser quadrada")
    else:
        C = np.dot(A, np.linalg.inv(B))

    print(f"A = \n{A}")
    print()
    print(f"B = \n{B}")
    print()
    print(f"A/B = \n{C}")
    print()
    print("TUDO FUNCIONANDO OK")
    print()


# ===================================
# Operações básicas com escalar
# ===================================
# Produto por escalar
def multiplica_escalar(A, num):
    pass


# ===================================
# Operações complementares
# ===================================
# Cálculo de Determinante
def calcula_determinante(A):
    det = np.linalg.det(A)
    print(f"Det = {det}")


# Cálculo de inversa
def calcula_inversa(A):
    inv = np.linalg.inv(A)
    print(f"Inv = {inv}")


# Cálculo de Transposta
def calcula_transposta(A):
    transposta = A.transpose()
    print(f"Transposta = {transposta}")


# ====================================================
#                    Área de teste
# ====================================================

M = np.array([["2", 2, 2], [2, 2, 2]])
N = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
O = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

P = np.array([1, 2, 3])
Q = np.array([1, 2, 3])
R = np.array([[1], [2], [3]])

print()
# soma_matriz(M, N)
# subtrai_matriz(P, Q)
# multiplica_matriz(P, R)
# divide_matriz(N, O)
# multiplica_escalar(A, num)
# calcula_determinante(A)
# calcula_inversa(A)
# calcula_transposta(A)
# np.linalg.inv(Q)
print(len(np.shape(O)))
