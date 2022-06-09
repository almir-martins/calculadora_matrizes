# ============================================
# Implementando a interface via Streamlit
# ============================================
import streamlit as st
import pandas as pd

st.title("Calculadora de Matrizes")

st.header("Trabalho de Conclusão de Curso - UNIVESP")
st.subheader("Licenciatura em matemática - Turma 2018")

st.write(
    pd.DataFrame(
        {
            "Nome": [
                "Almir Martins Lopes",
                "Antonio Ramalho de Lima",
                "Ariany Nascimento Silva",
                "Euclides Ferreira Miranda",
                "Karoline Alves Conceição",
                "Tatiane Pinheiro Ruela",
                "Valeria Gramlich Mistrello",
            ],
            "RA": [1824151, 20, 1836029, 1836480, 1831626, 0, 0],
        }
    )
)


# ============================================
# Menu lateral - Início
# ============================================
st.sidebar.title("Instruções")

# Using "with" notation
with st.sidebar:
    st.text(
        "Selecione a opção desejada:\n"
        + "(Operações com duas matrizes (soma, subtração, divisão, multiplicação),\n"
        + "Operações com uma matriz (Inversa, Determinante, Transposta),\n"
        + "Operações com escalar (soma, subtração, divisão, multiplicação))"
    )
# ============================================
# Menu lateral - Fim
# ============================================
