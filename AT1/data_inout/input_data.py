import os
import pathlib as pl

import numpy as np


# Esse método recebe como parâmetro o nome da instancia
#   e retorna uma matriz Numpy
def read_instance(instace: str) -> np.matrix:
    # caminho relativo da instância
    relative = "files/instances/" + instace + ".txt"
    # dados lidos
    data = []

    # verifica a existência do diretório dado
    if not os.path.exists(relative):
        raise Exception("Não existe o diretório: " + str(pl.Path(relative).absolute()))

    # lê cada linha do arquivo, sendo que cada linha é
    with open(relative, "r") as file:
        for line in file:
            data.append(line.strip().split(" "))

    return _str_to_matrix(data)


# Recebe os dados lidos do arquivo e retorna uma matriz
#   Numpy
def _str_to_matrix(data: list) -> np.matrix:
    return np.matrix(data, dtype=int)
