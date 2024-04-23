import os

RESULTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'files/results')) + '/'


def write_result(result: dict):
    path = RESULTS_PATH + 'log_AT1.txt'

    # escreve nome_instancia qtd_linhas qtd_colunas
    with open(path, "a") as file:
        file.write(f'{result.get("instance")} \t')
        file.write(f'{result.get("num_rows")} \t')
        file.write(f'{result.get("num_cols")} \n')

    # printa nome_instancia qtd_linhas qtd_colunas
    print(f'Instância: {result.get("instance")}')
    print(f'Número de linhas: {result.get("num_rows")}')
    print(f'Número de colunas: {result.get("num_cols")}')
