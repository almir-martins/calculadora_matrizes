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
            "RA": [1824151, 1823082, 1836029, 1836480, 1831626, 1823009, 1825164],
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
        "Nosso projeto baseia-se na apresen-\n"
        + "tação de uma ferramenta denominada\n"
        + "Calculadora de matrizes que objetiva\n"
        + "auxiliar alunos e professores no\n"
        + "cálculo e conferência de resultados\n"
        + "das operações com matrizes, fazendo\n"
        + "com que o docente tenha disponibi-\n"
        + "lidade  para um olhar mais atento\n"
        + "aos alunos, podendo assim, identifi-\n"
        + "ficar as dificuldades dos mesmos na\n"
        + "hora de calcular manualmente, e \n"
        + "ainda, contribuir de uma maneira \n"
        + "mais efetiva para a resolução de \n"
        + "dúvidas.\n"
        # e ainda, contribuir de uma maneira mais efetiva para a resolução de dúvidas. "
    )
# ============================================
# Menu lateral - Fim
# ============================================
