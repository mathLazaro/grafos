# GRAFOS

Repositório dedicado a atividades relacionadas à disciplina de grafos.

<hr>

## AT1

**Objetivo:** Implementar um protótipo de software com funções para entrada de dados e saída dos
resultados, que será usado para realização das atividades práticas durante a disciplina.

1. Desenvolver um protótipo de software que faça a leitura do arquivo de uma dada instância,
   mostrar um determinado resultado na tela e salvar em um outro arquivo

2. O nome da instância deverá ser passado como argumento (parâmetro) para o método no
   comando de execução. Exemplo:

        python3 main.py exemple

3. Uma função de entrada deverá ler o conteúdo do arquivo da respectiva instância e armazená-lo
   em uma matriz do tipo Numpy

4. Obtenha a dimensão da matriz (i.e. quantidade de linhas e de colunas)

5. Como resultado, uma função de saída deverá mostrar na tela e salvar em arquivo o nome da
   instância e a dimensão da respectiva matriz no formato: nome_instância qtd_linhas qtd_colunas

### Estrutura de pastas

- **files**  - arquivos de entrada e saida
    - **instances**  - datasets
    - **results**  - arquivos de resultados
- **data_inout**  - métodos de input e output de arquivos
- **processing**  - métodos de processamento dos dados lidos
- **main.py**  - core da aplicação

<hr>

## AT2

**Objetivo:** Representar conceitos básicos sobre grafos, e implementar funções para operações em **matrizes de
adjacência**.

### Funções implementadas:

- ***tipoGrafo(matriz)***
    - *Descrição:* Retorna o tipo do grafo representado por uma dada matriz de adjacências
    - *Saída:** Integer (0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 –
      pseudografo dirigido)
- ***verificaAdjacencia(matriz, vi, vj)***
    - *Descrição:* Verifica se os vértices vi e vj são adjacentes
    - *Saída:** Boolean (True se os vértices são adjacentes; False caso contrário)
- ***calcDensidade(matriz)***
    - *Descrição:* Retorna o valor da densidade do grafo
    - *Saída:* Float (valor da densidade com precisão de três casas decimais)
- ***insereAresta(matriz, vi, vj)***
    - *Descrição:* Insere uma aresta no grafo considerando o par de vértices vi e vj
    - *Saída:* matriz de adjacências (tipo numpy.ndarray) com a aresta inserida
- ***insereVertice(matriz)***
    - *Descrição:* Insere um vértice no grafo
    - *Saída:* matriz de adjacências (tipo numpy.ndarray) com o vértice inserido
- ***removeAresta(matriz, vi, vj)***
    - *Descrição:* Remove uma aresta do grafo considerando o par de vértices vi e vj
    - *Saída:* matriz de adjacências (tipo numpy.ndarray) com a aresta removida
- ***removeVertice(matriz, vi)***
    - *Descrição:* Remove um vértice do grafo
    - *Saída:* matriz de adjacências (tipo numpy.ndarray) com o vértice removido

### Estrutura de pastas

- **files**  - arquivos de entrada e saida
    - **instances**  - datasets
    - **results**  - log de resultado
- **data_inout**  - métodos de input e output de arquivos
- **functions**  - funções de manipulação de grafo
- **main.py**  - core da aplicação

<hr>

## AT3

**Objetivo:** Representar conceitos básicos sobre grafos, e implementar funções para operações em **lista de
adjacência**.

### Funções implementadas:

- ***criaListaAdjacencias(matriz)***
    - *Descrição:* Cria uma lista de adjacências de um grafo representado por uma matriz de adjacências
    - *Saída:* lista de adjacências (tipo Dictionary)
- ***tipoGrafo(listaAdj)***
    - *Descrição:* Retorna o tipo do grafo representado por uma dada lista de adjacências
    - *Saída:* Integer (0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 –
      pseudografo dirigido)
- ***verificaAdjacencia(listaAdj, vi, vj)***
    - *Descrição:* Verifica se os vértices vi e vj são adjacentes
    - *Saída:* Boolean (True se os vértices são adjacentes; False caso contrário)
- ***calcDensidade(listaAdj)***
    - *Descrição:* Retorna o valor da densidade do grafo
    - *Saída:* Float (valor da densidade com precisão de três casas decimais)
- ***insereAresta(listaAdj, vi, vj)***
    - *Descrição:* Insere uma aresta no grafo considerando o par de vértices vi e vj
    - *Saída:* lista de adjacências (tipo Dictionary) com a aresta inserida
- ***insereVertice(listaAdj, vi)***
    - *Descrição:* Insere um vértice no grafo.
    - *Saída:* lista de adjacências (tipo Dictionary) com o vértice inserido
- ***removeAresta(listaAdj, vi, vj)***
    - *Descrição:* Remove uma aresta do grafo considerando o par de vértices vi e vj
    - *Saída:* lista de adjacências (tipo Dictionary) com a aresta removida
- ***removeVertice(listaAdj, vi)***
    - *Descrição:* Remove um vértice do grafo
    - *Saída:* lista de adjacências (tipo Dictionary) com o vértice removido

### Estrutura de pastas:

Segue a mesma do exercício AT2.

## AT4

**Objetivo:** Implementar funções para o entendimento de conceitos de caminho e conectividade em grafos.

### Funções implementadas:

- ***warshall(matriz)***
    - *Descrição:* Obtém uma matriz de alcançabilidade a partir de uma matriz de adjacência.
    - *Saída:* matriz de alcançabilidade (numpy.ndarray)

- ***caminhoEuleriano(matriz)***
    - *Descrição:* Define se um grafo cumpre os requisitos para ser classificado como euleriano, ou seja, possui um
      caminho Euleriano.
    - *Saída:* valor booleano

### Estrutura de pastas:

- *instances* - instâncias
- *src* - implementações
- *main.py* - core da aplicação 
