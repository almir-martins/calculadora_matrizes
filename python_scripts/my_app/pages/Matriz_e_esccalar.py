# ============================================
# Implementando a interface via Streamlit
# ============================================
import streamlit as st

st.title("Calculadora de Matrizes")

# =================================================
# Página para operações com escalar - Início
# =================================================
A, B = st.columns([6, 1])
A.write("Matriz A")
B.write("Escalar b")

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
B11 = lin1col7.text_input("b")

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

# ===================
# Área com os botões
botao1, botao2, botao3, botao4 = st.columns([2, 3, 3, 3])
if botao1.button("Soma (A + b)"):
    st.write("")
else:
    st.write("")

if botao2.button("Subtração (A - b)"):
    st.write("")
else:
    st.write("")

if botao3.button("Multiplicação (A * b)"):
    st.write("")
else:
    st.write("")

if botao4.button("Divisão (A / b)"):
    st.write("")
else:
    st.write("")

# =================================================
# Página para operações com escalar - Fim
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
