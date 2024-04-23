import numpy as np


# Recebe os dados lidos do arquivo e retorna uma matriz
#   Numpy
def list_to_matrix(data: list) -> np.matrix:
    return np.matrix(data, dtype=int)
