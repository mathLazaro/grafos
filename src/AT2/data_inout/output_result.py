import os

RESULTS_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', 'files/results')) + '/'


def write_result(result: str):
    path = RESULTS_PATH + 'log_AT2.txt'

    # escreve o resultado no arquivo "
    with open(path, "a") as file:
        file.write(f'{result} \n\n')

    # printa o resultado no terminal
    print("\n" + str(result) + "\n")
