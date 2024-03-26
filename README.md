# GRAFOS

Repositório dedicado a atividades relacionadas à disciplina de grafos

## AT1

**Objetivo:** Implementar um protótipo de software com funções para entrada de dados e saída dos
resultados, que será usado para realização das atividades práticas durante a disciplina.

1. Desenvolver um protótipo de software que faça a leitura do arquivo de uma dada instância,
   mostrar um determinado resultado na tela e salvar em um outro arquivo;

2. O nome da instância deverá ser passado como argumento (parâmetro) para o método no
   comando de execução. Exemplo:

        python3 main.py exemple

3. Uma função de entrada deverá ler o conteúdo do arquivo da respectiva instância e armazená-lo
   em uma matriz do tipo Numpy;

4. Obtenha a dimensão da matriz (i.e. quantidade de linhas e de colunas);

5. Como resultado, uma função de saída deverá mostrar na tela e salvar em arquivo o nome da
   instância e a dimensão da respectiva matriz no formato: nome_instância qtd_linhas qtd_colunas.

### Estrutura de pastas

- **files**  - arquivos de entrada e saida
    - **instances**  - datasets
    - **results**  - arquivos de resultados
- **data_inout**  - métodos de input e output de arquivos
- **processing**  - métodos de processamento dos dados lidos
- **main.py**  - core da aplicação