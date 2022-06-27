# Calculadora de matrizes

Desenvolvido: Almir Martins Lopes
- Iniciado em: 27/05/2022
## Trabalho realizado na faculdade de matemática - Univesp

Este trabalho consistiu em criar uma calculadora de matrizes on-line para auxiliar os alunos de séries diversas no aprendizado de operações com matrizes, tanto em sala de aula como em aulas à distãncia. A calculadora também tem a finalidade de servir como ferramenta de apoio à professores no ensino de álgebra e na inserção da tecnologia como um contraponto ao estudo tradicional lousa-caderno.

## Passo 1

Na primeira fase realizei o planejamento da aplicação em modelos gerais. Partindo de um brainstorming das ideias que poderiam ser aplicadas foram surgindo o esboço da aplicação:
- Qual o escopo da aplicação;
- Que problema ela resolve;
- Quem vai utilizar;
- Qual é o entregável;
- Qual a melhor forma de distribuição;

## Passo 2
Partindo do esboço, desenvolvendo as funcionalidades que estariam na aplicação e em qual formato ela seria construída entrou o planejamento da arquitetura e estrutura de construção.
- Quais as classes deveriam ser implementadas;
- Como separar as responsabilidades na arquitetura;
- Como estruturar as interfaces do usuário;

## Passo 3
Chega a hora de por a mão na massa e iniciar a codificação. Já com a estrutura da aplicação planejada com suas classes e interfaces o processo de desenvolvimento fica mais simplificado. 
- Separar as responsabilidades macro por classes;
- Criar os métodos e classes usando o paradigma da orientação a objetos;
- Focar no reuso de código;
- Criar todo o backend para as interfaces;
- Tratar erros, excessões e casos de uso;

## Passo 4
Com o backend já desenvolvido começo a desenvolver a interface. No passo 1 já foi decidido por uma aplicação web e no passo 2 foi escolhido a biblioteca Streamlit para desenvolvimento das páginas e todo o frontend.
- Criação das páginas;
- Sepração das páginas por tipo de ações;
- Criação dos formulários e botões;
- Tratamento dos formulários para envio ao backend;

## Passo 5
Nessa etapa é começo a integrar o frontend com o backend testando as funcionalidades e os casos de uso em servidor local testando todo o funcionamento da aplicação e sua qualidade visual. 
- Integrar as interfaces com as classes de backend;
- Testar os casos de uso e exceptions;
- Verificar e corrigir a usabilidade das interfaces.
- Focar na UX;

## Passo 6
Esta é a etapa final. Com a aplicação rodando e realizado todos os testes em servidor local é nesta etapa que é realizado o deploy da aplicação, nesse caso no servidor Cloud Heroku.
- Montar a árvore de diretórios conforme requisitos do servidor;
- Criar os arquivos de configuração: procfile, setup.sh e runtime.txt
- Definir as bibliotecas a serem instaladas no servidor: requirements.txt;
- Fazer deploy no servidor de produção;
- Testar novamente;