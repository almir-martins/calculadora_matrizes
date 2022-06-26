# ============================================
# Implementando a interface via Streamlit
# ============================================
import streamlit as st
import numpy as np
import matrix_operations
import check_forms

st.title("Calculadora de Matrizes")

# =================================================
# Importação da classe de operações e formulários
# =================================================
cm = matrix_operations.Calculadora_Matriz()
cf = check_forms.Forms()


# =================================================
# Página para operações com escalar - Início
# =================================================
A, B = st.columns([6, 1])
A.write("Matriz A")
B.write("Escalar k")

# Primeira linha com todas as colunas
(
    lin1col1,
    lin1col2,
    lin1col3,
    lin1col4,
    lin1col5,
    lin1col6,
    lin1col7,
) = st.columns(7)
A11 = lin1col1.text_input("A11")
A12 = lin1col2.text_input("A12")
A13 = lin1col3.text_input("A13")
A14 = lin1col4.text_input("A14")
A15 = lin1col5.text_input("A15")
separador = lin1col6.write(" ")
B11 = lin1col7.text_input("k")

# Segunda linha com todas as colunas
(
    lin2col1,
    lin2col2,
    lin2col3,
    lin2col4,
    lin2col5,
    lin2col6,
    lin2col7,
) = st.columns(7)
A21 = lin2col1.text_input("A21")
A22 = lin2col2.text_input("A22")
A23 = lin2col3.text_input("A23")
A24 = lin2col4.text_input("A24")
A25 = lin2col5.text_input("A25")
separador = lin2col6.write(" ")
B21 = lin2col7.write("")

# Terceira linha com todas as colunas
(
    lin3col1,
    lin3col2,
    lin3col3,
    lin3col4,
    lin3col5,
    lin3col6,
    lin3col7,
) = st.columns(7)
A31 = lin3col1.text_input("A31")
A32 = lin3col2.text_input("A32")
A33 = lin3col3.text_input("A33")
A34 = lin3col4.text_input("A34")
A35 = lin3col5.text_input("A35")
separador = lin3col6.write(" ")
B31 = lin3col7.write("")

# Quarta linha com todas as colunas
(
    lin4col1,
    lin4col2,
    lin4col3,
    lin4col4,
    lin4col5,
    lin4col6,
    lin4col7,
) = st.columns(7)
A41 = lin4col1.text_input("A41")
A42 = lin4col2.text_input("A42")
A43 = lin4col3.text_input("A43")
A44 = lin4col4.text_input("A44")
A45 = lin4col5.text_input("A45")
separador = lin4col6.write(" ")
B41 = lin4col7.write("")

# Quinta linha com todas as colunas
(
    lin5col1,
    lin5col2,
    lin5col3,
    lin5col4,
    lin5col5,
    lin5col6,
    lin5col7,
) = st.columns(7)
A51 = lin5col1.text_input("A51")
A52 = lin5col2.text_input("A52")
A53 = lin5col3.text_input("A53")
A54 = lin5col4.text_input("A54")
A55 = lin5col5.text_input("A55")
separador = lin5col6.write(" ")
B51 = lin5col7.write("")

# ================================
# Área com os botões e métodos
# ================================
inputs_A = [
    [A11, A12, A13, A14, A15],
    [A21, A22, A23, A24, A25],
    [A31, A32, A33, A34, A35],
    [A41, A42, A43, A44, A45],
    [A51, A52, A53, A54, A55],
]

scalar = B11

# Botões
botao1, botao2, botao3, botao4 = st.columns([2, 3, 3, 3])
if botao1.button("Soma (A + k)"):
    # Se o escalar não for válido
    if not cf.check_scalar(scalar):
        st.write("ATENÇÃO - O escalar deve ter formato numérico válido.")
    # Se os dados da matriz A não estiverem corretos
    elif len(cf.get_matrix_A(inputs_A)) < 1:
        st.write("ATENÇÃO - A matriz A deve ter formato válido.")
    else:
        # Calcula o resultado chamando a classe em matrix_operations.py
        result = cm.soma_escalar(cf.get_matrix_A(inputs_A), scalar)

        # Transforma o resultado em Latex
        lines = str(result).replace("[", "").replace("]", "").splitlines()
        rv = [r"\begin{bmatrix}"]
        rv += ["  " + " & ".join(l.split()) + r"\\" for l in lines]
        rv += [r"\end{bmatrix}"]
        st.write("A soma da matriz A pelo escalar k é:")
        st.latex("".join(rv))


if botao2.button("Subtração (A - k)"):
    # Se o escalar não for válido
    if not cf.check_scalar(scalar):
        st.write("ATENÇÃO - O escalar deve ter formato numérico válido.")
    # Se os dados da matriz A não estiverem corretos
    elif len(cf.get_matrix_A(inputs_A)) < 1:
        st.write("ATENÇÃO - A matriz A deve ter formato válido.")
    else:
        # Calcula o resultado chamando a classe em matrix_operations.py
        result = cm.subtrai_escalar(cf.get_matrix_A(inputs_A), scalar)

        # Transforma o resultado em Latex
        lines = str(result).replace("[", "").replace("]", "").splitlines()
        rv = [r"\begin{bmatrix}"]
        rv += ["  " + " & ".join(l.split()) + r"\\" for l in lines]
        rv += [r"\end{bmatrix}"]
        st.write("A subtração da matriz A pelo escalar k é:")
        st.latex("".join(rv))


if botao3.button("Multiplicação (A * k)"):
    # Se o escalar não for válido
    if not cf.check_scalar(scalar):
        st.write("ATENÇÃO - O escalar deve ter formato numérico válido.")
    # Se os dados da matriz A não estiverem corretos
    elif len(cf.get_matrix_A(inputs_A)) < 1:
        st.write("ATENÇÃO - A matriz A deve ter formato válido.")
    else:
        # Calcula o resultado chamando a classe em matrix_operations.py
        result = cm.multiplica_escalar(cf.get_matrix_A(inputs_A), scalar)

        # Transforma o resultado em Latex
        lines = str(result).replace("[", "").replace("]", "").splitlines()
        rv = [r"\begin{bmatrix}"]
        rv += ["  " + " & ".join(l.split()) + r"\\" for l in lines]
        rv += [r"\end{bmatrix}"]
        st.write("A multiplicação da matriz A pelo escalar k é:")
        st.latex("".join(rv))


if botao4.button("Divisão (A / k)"):
    if B11 == "0":
        st.write("ATENÇÃO - DIVISÃO POR ZERO")
        st.write("Operação impossível!")
    else:
        # Se o escalar não for válido
        if not cf.check_scalar(scalar):
            st.write("ATENÇÃO - O escalar deve ter formato numérico válido.")
        # Se os dados da matriz A não estiverem corretos
        elif len(cf.get_matrix_A(inputs_A)) < 1:
            st.write("ATENÇÃO - A matriz A deve ter formato válido.")
        else:
            # Calcula o resultado chamando a classe em matrix_operations.py
            result = cm.divide_escalar(cf.get_matrix_A(inputs_A), scalar)

            # Transforma o resultado em Latex
            lines = str(result).replace("[", "").replace("]", "").splitlines()
            rv = [r"\begin{bmatrix}"]
            rv += ["  " + " & ".join(l.split()) + r"\\" for l in lines]
            rv += [r"\end{bmatrix}"]
            st.write("A divisão da matriz A pelo escalar k é:")
            st.latex("".join(rv))

# =================================================
# Página para operações com escalar - Fim
# =================================================
# ============================================
# Menu lateral - Início
# ============================================
st.sidebar.title("Instruções")

# Using "with" notation
with st.sidebar:
    st.text(
        "Para preencher a matriz corretamente\n"
        + "insira os valores nas posições dos\n"
        + "elementos desejados e deixe os \n"
        + "demais em branco (sem preencher).\n"
        + "\n"
        + "Exemplo 1:\n"
        + "Para somar duas matrizes quadradas\n"
        + "2x2 preencha os elementos\n"
        + "A11, A12, A21, A22 (Matriz A)\n"
        + "B11, B12, B21, B22 (Matriz B)\n"
        + "e pressione o botão 'Soma (A + B)'\n\n"
        + "Exemplo 2:\n"
        + "Para calcular calcular a transposta\n"
        + "de uma matriz 3x2 preencha os elem\n"
        + "A11, A12, A21, A22, A31, A32\n"
        + "e pressione o botão 'Transposta'"
    )
# ============================================
# Menu lateral - Fim
# ============================================
