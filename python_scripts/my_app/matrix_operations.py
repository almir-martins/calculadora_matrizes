import numpy as np


class Calculadora_Matriz:
    """
    Classe que implementa todas as operações com matrizes e escalres da aplicaçao\n.
    """

    def is_square(self, A):
        """
        Verifica se a matriz passada como parâmetro é quadrada\n.

        Parameters
        A : list
            A  matriz

        :return: Boolean True se a matriz for quadrada ou False se não
        """
        m = np.array(A)
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
        """
        Verifica se duas matrizes passada como parâmetros são de mesma ordem\n.

        Parameters
        m : list
            A  matriz

        Parameters
        n : list
            A  matriz

        :return: Boolean True se a matriz forem da mesma ordem ou False se não
        """
        if m.shape == n.shape:
            return True
        return False

    # ===================================
    # As quatro operações básicas
    # ===================================
    # Adição de matriz
    def soma_matriz(self, A_, B_):
        """
        Soma duas matrizes\n.

        Parameters
        A : list
            A primeira matriz a ser somada
        B : List
            A segunda matriz a ser somada
        :return: Uma matriz resultante da soma das matrizes A e B
        """
        A = np.array(A_)
        B = np.array(B_)
        if self.is_same_order(A, B):
            try:
                return A + B

            # Matriz não contém somente números
            except np.core._exceptions._UFuncNoLoopError:
                print("Os elementos precisam ser números!")

            except Exception as e:
                return "Erro desconhecido"
        else:
            return "As matrizes precisam ser de mesma ordem"

    # Subtração de matriz
    def subtrai_matriz(self, A_, B_):
        """
        Soma duas matrizes\n.

        Parameters
        A : list
            A primeira matriz a ser somada
        B : List
            A segunda matriz a ser somada
        :return: Uma matriz resultante da soma das matrizes A e B
        """
        A = np.array(A_)
        B = np.array(B_)
        if self.is_same_order(A, B):
            try:
                return A - B

            # Matriz não contém somente números
            except np.core._exceptions._UFuncNoLoopError:
                print("Os elementos precisam ser números!")

            except Exception as e:
                return "Erro desconhecido"
        else:
            return "As matrizes precisam ser de mesma ordem"

    # Produto de matriz
    def multiplica_matriz(self, A, B):
        """
        Multiplica duas matrizes\n.

        Parameters
        A : list
            A primeira matriz
        B : List
            A segunda matriz
        :return: Uma matriz resultante da multiplicação das matrizes A e B
        """
        try:
            return np.dot(A, B)

        # Matriz não contém somente números
        except np.core._exceptions._UFuncNoLoopError:
            return "Os elementos precisam ser números!"

        # Matrizes de tamanhos diferentes
        except ValueError:
            return "Para multiplicar duas matrizes o nº de colunas da primeira \ndeve ser igual ao nº de linhas da segunda."

        except Exception as e:
            return "Erro desconhecido"

    # Divisão de matriz
    def divide_matriz(self, A_, B_):
        """
        Divide duas matrizes\n.

        Parameters
        A : list
            A primeira matriz
        B : List
            A segunda matriz
        :return: Uma matriz resultante da divisão das matrizes A e B
        """
        A = np.array(A_)
        B = np.array(B_)

        if (self.is_square(A)) and (self.is_square(B)) and (self.is_same_order(A, B)):
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
        """
        Soma os elementos de uma matriz com um escalar\n.

        Parameters
        A : list
            A matriz a ser somada
        num : int
            O escalar a ser somado
        :return: A matriz resultante da soma
        """
        if ("," in num) or ("." in num):
            num = round(float(num), 1)
        else:
            num = int(num)
        return np.array(A) + num

    def subtrai_escalar(self, A, num):
        """
        Subtrai os elementos de uma matriz de um escalar\n.

        Parameters
        A : list
            A matriz a ser subtraída
        num : int
            O escalar a ser subtraído
        :return: A matriz resultante da subtração
        """
        if ("," in num) or ("." in num):
            num = round(float(num), 1)
        else:
            num = int(num)
        return np.array(A) - num

    # Produto por escalar
    def multiplica_escalar(self, A, num):
        """
        Multiplica os elementos de uma matriz por um escalar\n.

        Parameters
        A : list
            A matriz a ser multiplicada
        num : int
            O escalar a ser multiplicado
        :return: A matriz resultante da multiplicação
        """
        if ("," in num) or ("." in num):
            num = round(float(num), 1)
        else:
            num = int(num)
        return np.array(A) * num

    # Divisão por escalar
    def divide_escalar(self, A, num):
        """
        Divide os elementos de uma matriz por um escalar\n.

        Parameters
        A : list
            A matriz a ser Dividida
        num : int
            O escalar a ser dividido
        :return: A matriz resultante da divisão
        """
        if ("," in num) or ("." in num):
            num = round(float(num), 1)
        else:
            num = int(num)
        return np.array(A) / num

    # ===================================
    # Operações complementares
    # ===================================
    # Cálculo de Determinante
    def calcula_determinante(self, A):
        """
        Calcula o determinante da matriz A\n.

        Parameters
        A : list
            A matriz para cálculo do determinante

        :return: O determninate DetA
        """
        if not self.is_square(A):
            return "A matriz deve ser quadrada"
        try:
            return round(np.linalg.det(A), 2)
        except:
            return "Matriz não possui determninante."

    # Cálculo de inversa
    def calcula_inversa(self, A):
        """
        Calcula a matriz inversa caso exista\n.

        Parameters
        A : list
            A matriz para cálculo da Inversa

        :return: A matriz Inversa (list) ou mensagem erro (str)
        """
        if not self.is_square(A):
            return "A matriz deve ser quadrada"
        try:
            return np.linalg.inv(A)
        except:
            return "Matriz não inversível"

    # Cálculo de Transposta
    def calcula_transposta(self, A):
        """
        Calcula a matriz transposta da matrriz A\n.

        Parameters
        A : list
            A matriz para cálculo da Inversa

        :return: A matriz tranposta
        """
        m = np.array(A)
        return m.transpose()
