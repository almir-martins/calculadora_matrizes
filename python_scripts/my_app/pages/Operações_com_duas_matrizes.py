# ============================================
# Implementando a interface via Streamlit
# ============================================
import streamlit as st

st.title("Calculadora de Matrizes")

# =================================================
# Página para operações com duas matrizes - Início
# =================================================
A, B = st.columns([6, 5])
A.write("Matriz A")
B.write("Matriz B")

# Primeira linha com todas as colunas
(
    lin1col1,
    lin1col2,
    lin1col3,
    lin1col4,
    lin1col5,
    lin1col6,
    lin1col7,
    lin1col8,
    lin1col9,
    lin1col10,
    lin1col11,
) = st.columns(11)
A11 = lin1col1.text_input("A11")
A12 = lin1col2.text_input("A12")
A13 = lin1col3.text_input("A13")
A14 = lin1col4.text_input("A14")
A15 = lin1col5.text_input("A15")
separador = lin1col6.write(" ")
B11 = lin1col7.text_input("B11")
B12 = lin1col8.text_input("B12")
B13 = lin1col9.text_input("B13")
B14 = lin1col10.text_input("B14")
B15 = lin1col11.text_input("B15")


# Segunda linha com todas as colunas
(
    lin2col1,
    lin2col2,
    lin2col3,
    lin2col4,
    lin2col5,
    lin2col6,
    lin2col7,
    lin2col8,
    lin2col9,
    lin2col10,
    lin2col11,
) = st.columns(11)
A21 = lin2col1.text_input("A21")
A22 = lin2col2.text_input("A22")
A23 = lin2col3.text_input("A23")
A24 = lin2col4.text_input("A24")
A25 = lin2col5.text_input("A25")
separador = lin2col6.write(" ")
B21 = lin2col7.text_input("B21")
B22 = lin2col8.text_input("B22")
B23 = lin2col9.text_input("B23")
B24 = lin2col10.text_input("B24")
B25 = lin2col11.text_input("B25")


# Terceira linha com todas as colunas
(
    lin3col1,
    lin3col2,
    lin3col3,
    lin3col4,
    lin3col5,
    lin3col6,
    lin3col7,
    lin3col8,
    lin3col9,
    lin3col10,
    lin3col11,
) = st.columns(11)
A31 = lin3col1.text_input("A31")
A32 = lin3col2.text_input("A32")
A33 = lin3col3.text_input("A33")
A34 = lin3col4.text_input("A34")
A35 = lin3col5.text_input("A35")
separador = lin3col6.write(" ")
B31 = lin3col7.text_input("B31")
B32 = lin3col8.text_input("B32")
B33 = lin3col9.text_input("B33")
B34 = lin3col10.text_input("B34")
B35 = lin3col11.text_input("B35")


# Quarta linha com todas as colunas
(
    lin4col1,
    lin4col2,
    lin4col3,
    lin4col4,
    lin4col5,
    lin4col6,
    lin4col7,
    lin4col8,
    lin4col9,
    lin4col10,
    lin4col11,
) = st.columns(11)
A41 = lin4col1.text_input("A41")
A42 = lin4col2.text_input("A42")
A43 = lin4col3.text_input("A43")
A44 = lin4col4.text_input("A44")
A45 = lin4col5.text_input("A45")
separador = lin4col6.write(" ")
B41 = lin4col7.text_input("B41")
B42 = lin4col8.text_input("B42")
B43 = lin4col9.text_input("B43")
B44 = lin4col10.text_input("B44")
B45 = lin4col11.text_input("B45")


# Quinta linha com todas as colunas
(
    lin5col1,
    lin5col2,
    lin5col3,
    lin5col4,
    lin5col5,
    lin5col6,
    lin5col7,
    lin5col8,
    lin5col9,
    lin5col10,
    lin5col11,
) = st.columns(11)
A51 = lin5col1.text_input("A51")
A52 = lin5col2.text_input("A52")
A53 = lin5col3.text_input("A53")
A54 = lin5col4.text_input("A54")
A55 = lin5col5.text_input("A55")
separador = lin5col6.write(" ")
B51 = lin5col7.text_input("B51")
B52 = lin5col8.text_input("B52")
B53 = lin5col9.text_input("B53")
B54 = lin5col10.text_input("B54")
B55 = lin5col11.text_input("B55")


# ===================
# Área com os botões
botao1, botao2, botao3, botao4 = st.columns([2, 3, 3, 3])
if botao1.button("Soma (A + B)"):
    st.write("")
else:
    st.write("")

if botao2.button("Subtração (A - B)"):
    st.write("")
else:
    st.write("")

if botao3.button("Multiplicação (A * B)"):
    st.write("")
else:
    st.write("")

if botao4.button("Divisão (A / B)"):
    st.write("")
else:
    st.write("")

# =================================================
# Página para operações com duas matrizes - Fim
# =================================================

# ============================================
# Menu lateral - Início
# ============================================
st.sidebar.title("Menu")

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Selecione a opção desejada:",
        (
            "Operações com duas matrizes \n(soma, subtração, divisão, multiplicação)",
            "Operações com uma matriz \n(Inversa, Determinante, Transposta)",
            "Operações com escalar \n(soma, subtração, divisão, multiplicação)",
        ),
    )
# ============================================
# Menu lateral - Fim
# ============================================
