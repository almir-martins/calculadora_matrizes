from types import new_class
import numpy as np

# Verifica se a matriz é quadrada
def is_square(m):
    try:
        if m.shape[0] == m.shape[1]:
            return True
        else:
            return False
    except:
        if m.shape[0] == 1:
            return True
        return False


# Verifica se as matrizes são de mesma ordem
def is_same_order(m, n):
    if m.shape == n.shape:
        return True
    return False


# ===================================
# As quatro operações básicas
# ===================================
# Adição de matriz
def soma_matriz(A, B):
    if (is_square(A)) and (is_square(B)) and (is_same_order(A, B)):
        try:
            return A + B

        # Matriz não contém somente números
        except np.core._exceptions._UFuncNoLoopError:
            print("Os elementos precisam ser números!")

        except Exception as e:
            return "Erro desconhecido"

    else:
        return "As matrizes precisam ser quadradas e de mesma ordem"


# Subtração de matriz
def subtrai_matriz(A, B):
    if (is_square(A)) and (is_square(B)) and (is_same_order(A, B)):
        try:
            return A - B

        # Matriz não contém somente números
        except np.core._exceptions._UFuncNoLoopError:
            print("Os elementos precisam ser números!")

        except Exception as e:
            return "Erro desconhecido"

    else:
        return "As matrizes precisam ser quadradas e de mesma ordem"


# Produto de matriz
def multiplica_matriz(A, B):
    try:
        return np.dot(A, B)

    # Matriz não contém somente números
    except np.core._exceptions._UFuncNoLoopError:
        return "Os elementos precisam ser números!"

    # Matrizes de tamanhos diferentes
    except ValueError:
        return "Matrizes de tamanhos diferentes!"

    except Exception as e:
        return "Erro desconhecido"


# Divisão de matriz
def divide_matriz(A, B):
    if (is_square(A)) and (is_square(B)) and (is_same_order(A, B)):
        try:
            return np.dot(A, np.linalg.inv(B))

        # Matriz não contém somente números
        except np.core._exceptions._UFuncNoLoopError:
            print("Os elementos precisam ser números!")

        except Exception as e:
            return "Erro desconhecido"

    else:
        return "As matrizes precisam ser quadradas e de mesma ordem"


# ===================================
# Operações básicas com escalar
# ===================================
def soma_escalar(A, num):
    pass


def subtrai_escalar(A, num):
    pass


# Produto por escalar
def multiplica_escalar(A, num):
    pass


# Divisão por escalar
def divide_escalar(A, num):
    pass


# ===================================
# Operações complementares
# ===================================
# Cálculo de Determinante
def calcula_determinante(A):
    return np.linalg.det(A)


# Cálculo de inversa
def calcula_inversa(A):
    return np.linalg.inv(A)


# Cálculo de Transposta
def calcula_transposta(A):
    return A.transpose()


# ====================================================
#                    Área de testes
# ====================================================

M = np.array([["2", 2, 2], [2, 2, 2]])
N = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
O = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])

P = np.array([1, 2, 3])
Q = np.array([1, 2, 3])
R = np.array([[1], [2], [3]])

calcula_inversa(O)
print()
# soma_matriz(O, R)

# subtrai_matriz(P, Q)
# multiplica_matriz(P, R)
# divide_matriz(N, O)
# multiplica_escalar(A, num)
# calcula_determinante(A)
# calcula_inversa(A)
# calcula_transposta(A)
# np.linalg.inv(Q)

# divide_matriz(O, R)
# print(len(R))
# print(is_square(P))
