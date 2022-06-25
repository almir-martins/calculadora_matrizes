import numpy as np


class Forms:
    def is_set(self, field):
        if not str(field) == "":
            return True

    def is_a_number(self, field):
        if "," in field:
            field = field.replace(",", ".")
        try:
            float(field)
            return True
        except ValueError:
            return False

    def check_scalar(self, scalar):
        if self.is_set(scalar) and self.is_a_number(scalar):
            return True
        return False

    def check_input(self, input):
        if self.is_set(input) and self.is_a_number(input):
            if ("," in input) or ("." in input):
                return float(input.replace(",", "."))
            return int(input)
        else:
            return "Valor inválido"

    def get_matrix_A(self, inputs):
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


# def is_set(field):
#     if not str(field) == "":
#         return True


# def is_a_number(field):
#     if "," in field:
#         field = field.replace(",", ".")
#     try:
#         float(field)
#         return True
#     except ValueError:
#         return False


# def check_scalar(scalar):
#     if is_set(B11) and is_a_number(B11):
#         return True
#     return False


# def check_input(input):
#     if is_set(input) and is_a_number(input):
#         if ("," in input) or ("." in input):
#             return float(input.replace(",", "."))
#         return int(input)
#     else:
#         return "Valor inválido"


# def get_matrix_A():
#     inputs = [
#         [A11, A12, A13, A14, A15],
#         [A21, A22, A23, A24, A25],
#         [A31, A32, A33, A34, A35],
#         [A41, A42, A43, A44, A45],
#         [A51, A52, A53, A54, A55],
#     ]
#     matrix_A = []
#     # Passa por todos os campos na ordem da matriz (Aij)
#     for i in range(5):  # itera pelas linhas
#         elem = []
#         for j in range(5):  # itera pelas colunas
#             # Se o valor do campo for numérico insere na matriz da linha
#             if not check_input(inputs[i][j]) == "Valor inválido":
#                 elem.append(check_input(inputs[i][j]))
#         # Se a matriz linha tiver elementos é inserida na matriz A
#         if len(elem) >= 1:
#             matrix_A.append(elem)

#     return matrix_A


"""
   Send a message to a recipient.

   :param str sender: The person sending the message
   :param str recipient: The recipient of the message
   :param str message_body: The body of the message
   :param priority: The priority of the message, can be a number 1-5
   :type priority: integer or None
   :return: the message id
   :rtype: int
   :raises ValueError: if the message_body exceeds 160 characters
   :raises TypeError: if the message_body is not a basestring
"""

"""
Send a message to a recipient.

:param str sender: The person sending the message
:return: the message id
"""
