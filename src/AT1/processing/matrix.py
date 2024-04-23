import numpy as np


# Extrai informações da matriz Numpy gerada
def get_meta_data(matrix: np.matrix, instance: str) -> dict:
    meta = dict()

    meta['instance'] = instance         # nome_instancia
    meta['num_rows'] = matrix.shape[0]  # qtd_linhas
    meta['num_cols'] = matrix.shape[1]  # qtd_colunas

    return meta
