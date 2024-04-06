import os
import pathlib as pl


# Esse método recebe como parâmetro o nome da instancia
#   e retorna um multi array
def read_instance(instace: str) -> list:
    # caminho relativo da instância
    relative = "files/instances/" + instace + ".txt"
    # dados lidos
    data = []

    # verifica a existência do diretório dado
    if not os.path.exists(relative):
        raise Exception("Não existe o diretório: "
                        + str(pl.Path(relative).absolute()))

    # lê cada linha do arquivo
    with open(relative, "r") as file:
        for line in file:
            # converte cada 'casa' da matriz em inteiro
            data.append([int(i) for i in line.strip().split(" ")])

    return data
