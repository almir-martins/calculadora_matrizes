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
