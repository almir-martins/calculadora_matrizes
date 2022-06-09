import numpy as np

class Calculadora_Matriz:

    # Verifica se a matriz é quadrada
    def is_square(self, m):
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
    def is_same_order(self, m, n):
        if m.shape == n.shape:
            return True
        return False

    # ===================================
    # As quatro operações básicas
    # ===================================
    # Adição de matriz
    def soma_matriz(self, A, B):
        if (self.is_square(A)) and (self.is_square(B)) and (self.is_same_order(A, B)):
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
    def subtrai_matriz(self, A, B):
        if (self.is_square(A)) and (self.is_square(B)) and (self.is_same_order(A, B)):
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
    def multiplica_matriz(self, A, B):
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
    def divide_matriz(self, A, B):
        if (
            (is_squaself.is_squarere(A))
            and (self.is_square(B))
            and (self.is_same_order(A, B))
        ):
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
    def soma_escalar(self, A, num):
        return A + num

    def subtrai_escalar(self, A, num):
        return A - num

    # Produto por escalar
    def multiplica_escalar(self, A, num):
        return A * num

    # Divisão por escalar
    def divide_escalar(self, A, num):
        return A / num

    # ===================================
    # Operações complementares
    # ===================================
    # Cálculo de Determinante
    def calcula_determinante(self, A):
        return np.linalg.det(A)

    # Cálculo de inversa
    def calcula_inversa(self, A):
        if not self.is_square(A):
            return "A matriz deve ser quadrada"
        try:
            return np.linalg.inv(A)
        except:
            return "Matriz não inversível"

    # Cálculo de Transposta
    def calcula_transposta(self, A):
        return A.transpose()


# N = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
# cm = Calculadora_Matriz()
# print(cm.calcula_inversa(N))
