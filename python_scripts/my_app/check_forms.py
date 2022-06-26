import numpy as np


class Forms:
    """
    Classe que implementa as verificações e checagem\n
    dos dados vindas do formulários
    """

    def is_set(self, field):
        """
        Verifica se o formulário foi preenchido com algum valor\n.

        Parameters
        field : str
            O valor vindo do formulário

        :return: Boolean True se o campo possuir valor
        """
        if not str(field) == "":
            return True

    def is_a_number(self, field):
        """
        Verifica se o valor preenchido no formulário é um número\n.

        Parameters
        field : str
            O valor vindo do formulário

        :return: Boolean True se o valor for número ou False se não.
        """
        if "," in field:
            field = field.replace(",", ".")
        try:
            float(field)
            return True
        except ValueError:
            return False

    def check_scalar(self, scalar):
        """
        Verifica se o valor do escalar foi preenchido no formulário e se é um número\n.

        Parameters
        scalar : str
            O valor vindo do formulário

        :return: Boolean True se houver valor e se for número ou False se não.
        """
        if self.is_set(scalar) and self.is_a_number(scalar):
            return True
        return False

    def check_input(self, input):
        """
        Verifica se o valor foi preenchido no formulário e se é um número\n.

        Parameters
        input : str
            O valor vindo do formulário

        :return: Boolean True se houver valor e se for número ou False se não.
        """
        if self.is_set(input) and self.is_a_number(input):
            if ("," in input) or ("." in input):
                return float(input.replace(",", "."))
            return int(input)
        else:
            return "Valor inválido"

    def get_matrix_A(self, inputs):
        """
        Verifica todos os valores nos campos da matriz A:\n
        - Se foram preenchidos\n
        - Se são números\n

        Parameters
        inputs : list
            Uma lista com todos os elementos da matriz A

        :return: list, uma lista no formato de matriz somente com os elementos informados válidos.
        """
        matrix_A = []
        # Passa por todos os campos na ordem da matriz (Aij)
        for i in range(5):  # itera pelas linhas
            elem = []
            for j in range(5):  # itera pelas colunas
                # Se o valor do campo for numérico insere na matriz da linha
                if not self.check_input(inputs[i][j]) == "Valor inválido":
                    elem.append(self.check_input(inputs[i][j]))
            # Se a matriz linha tiver elementos é inserida na matriz A
            if len(elem) >= 1:
                matrix_A.append(elem)

        return matrix_A

    def get_matrix_B(self, inputs):
        """
        Verifica todos os valores nos campos da matriz B:\n
        - Se foram preenchidos\n
        - Se são números\n

        Parameters
        inputs : list
            Uma lista com todos os elementos da matriz B

        :return: list, uma lista no formato de matriz somente com os elementos informados válidos.
        """
        matrix_B = []
        # Passa por todos os campos na ordem da matriz (Aij)
        for i in range(5):  # itera pelas linhas
            elem = []
            for j in range(5):  # itera pelas colunas
                # Se o valor do campo for numérico insere na matriz da linha
                if not self.check_input(inputs[i][j]) == "Valor inválido":
                    elem.append(self.check_input(inputs[i][j]))
            # Se a matriz linha tiver elementos é inserida na matriz A
            if len(elem) >= 1:
                matrix_B.append(elem)

        return matrix_B
